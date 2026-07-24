#!/usr/bin/env python3
"""Validate Anki language flashcard TSV against Inventory (+ Inventory Gate)."""
from __future__ import annotations

import argparse
import re
import sys
import time
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
EXPORT_FRESHNESS_DAYS = 7

# language slug -> Deck Export path (mirrors Language Profiles)
EXPORTS: dict[str, Path] = {
    "spanish": Path("/Users/bruno/Documents/idioms__spanish.txt"),
    "english": Path("/Users/bruno/Documents/idioms__english.txt"),
}

BANNED_EASY = {
    "spanish": {
        "organizar",
        "revisar",
        "importar",
        "comparar",
        "descansar",
        "ahorrar",
        "correr",
        "pagar",
    },
    "english": {
        "organize",
        "revise",
        "import",
        "compare",
        "important",
        "different",
        "information",
    },
}


def strip_markup(s: str) -> str:
    s = re.sub(r"\{\{c\d+::(.*?)(?::.*?)?\}\}", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("_____", "")
    return s


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", strip_markup(s)).lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip(" .?!¿¡,;:")


def accentless(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def load_lines(path: Path) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    if not path.exists():
        return out
    for ln in path.read_text(encoding="utf-8").splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        parts = ln.split("\t")
        if len(parts) >= 2:
            out.append((parts[0].strip(), parts[1].strip()))
    return out


def detect_language(path: Path, explicit: str | None) -> str | None:
    if explicit:
        return explicit.lower()
    parts = path.resolve().parts
    for slug in EXPORTS:
        if slug in parts:
            return slug
    name = path.name.lower()
    if "espanhol" in name or "spanish" in name:
        return "spanish"
    if "english" in name or "ingles" in name or "inglês" in name:
        return "english"
    return None


def language_folder(lang: str) -> Path:
    return REPO_ROOT / "flashcards" / lang


def export_age_days(export: Path) -> float | None:
    if not export.exists():
        return None
    return (time.time() - export.stat().st_mtime) / 86400.0


def inventory_gate(lang: str) -> list[str]:
    errors: list[str] = []
    export = EXPORTS[lang]
    age = export_age_days(export)
    if age is None:
        errors.append(
            f"Inventory Gate: Deck Export ausente: {export} "
            f"(exporte o deck `{lang}` e tente de novo)"
        )
    elif age > EXPORT_FRESHNESS_DAYS:
        errors.append(
            f"Inventory Gate: Deck Export velho ({age:.1f}d > {EXPORT_FRESHNESS_DAYS}d): {export}"
        )
    return errors


def is_twin(exclude: Path, other: Path) -> bool:
    a, b = exclude.name, other.name
    return a.replace("_cloze", "_producao") == b or a.replace("_producao", "_cloze") == b


def inventory(lang: str, exclude: Path | None = None) -> tuple[set[str], set[str]]:
    fronts: set[str] = set()
    targets: set[str] = set()
    exclude_resolved = exclude.resolve() if exclude else None
    paths = [EXPORTS[lang], *sorted(language_folder(lang).glob("*.tsv"))]
    for path in paths:
        if exclude_resolved and path.resolve() == exclude_resolved:
            continue
        if exclude and path.exists() and is_twin(exclude, path):
            continue
        for front, back in load_lines(path):
            n = norm(front)
            if not n:
                continue
            fronts.add(n)
            fronts.add(accentless(n))
            for m in re.findall(r"<b>(.*?)</b>", front, flags=re.I):
                targets.add(norm(m))
            for m in re.findall(r"\{\{c\d+::(.*?)(?::.*?)?\}\}", front):
                targets.add(norm(m))
            if "<br" in back.lower() or "\n" in back:
                first = re.split(r"<br\s*/?>|\n", back, maxsplit=1, flags=re.I)[0].strip()
                if first and len(first) < 60:
                    targets.add(norm(first))
    return fronts, targets


def validate(path: Path, lang: str | None, skip_gate: bool) -> int:
    if not path.is_file():
        print(f"ERROR: arquivo não encontrado: {path}")
        return 2

    language = detect_language(path, lang)
    if not language or language not in EXPORTS:
        print(
            "ERROR: idioma não detectado. Use path em flashcards/<language>/ "
            "ou --lang spanish|english"
        )
        return 2

    errors: list[str] = []
    warns: list[str] = []

    if skip_gate:
        age = export_age_days(EXPORTS[language])
        if age is None:
            warns.append(f"Deck Export ausente (gate ignorado): {EXPORTS[language]}")
        elif age > EXPORT_FRESHNESS_DAYS:
            warns.append(
                f"Deck Export velho ({age:.1f}d; gate ignorado): {EXPORTS[language]}"
            )
    else:
        errors.extend(inventory_gate(language))

    fronts_inv, targets_inv = inventory(language, exclude=path)
    cards = load_lines(path)
    seen_local: set[str] = set()
    target_counts: dict[str, int] = {}
    banned = BANNED_EASY.get(language, set())

    for i, (front, back) in enumerate(cards, 1):
        n = norm(front)
        if not n:
            errors.append(f"L{i}: frente vazia")
            continue
        if n in seen_local or accentless(n) in seen_local:
            errors.append(f"L{i}: duplicata interna")
        seen_local.add(n)
        seen_local.add(accentless(n))
        if n in fronts_inv or accentless(n) in fronts_inv:
            errors.append(f"L{i}: frente já no inventário: {front[:80]}")
        if "anki" in front.lower() or "duolingo" in front.lower():
            errors.append(f"L{i}: card meta proibido")

        if language == "spanish":
            for bad in ("manana", "articulo", "facil", "dificil", "tambien", "rapido"):
                if bad in front.lower():
                    errors.append(f"L{i}: possível acento faltando ({bad})")

        target = None
        m = re.search(r"\{\{c\d+::(.*?)(?::.*?)?\}\}", front)
        if m:
            target = m.group(1).strip()
        elif "_____" in front:
            target = re.split(r"<br\s*/?>", back, maxsplit=1, flags=re.I)[0].strip()
        if target:
            tn = norm(target)
            target_counts[tn] = target_counts.get(tn, 0) + 1
            if tn in banned:
                warns.append(f"L{i}: alvo cognato/fácil saturado: {target}")
            if tn in targets_inv:
                warns.append(f"L{i}: alvo já usado no inventário: {target}")

        if "_____" not in front and "{{c" not in front and "<b>" not in front:
            warns.append(f"L{i}: sem lacuna/cloze/negrito")

    for t, c in target_counts.items():
        if c > 2:
            errors.append(f"alvo '{t}' aparece {c}× neste lote (máx. 2)")

    print(f"Arquivo: {path}")
    print(f"Idioma: {language}")
    print(f"Deck Export: {EXPORTS[language]}")
    print(f"Cards: {len(cards)}")
    print(f"Erros: {len(errors)} | Avisos: {len(warns)}")
    for e in errors[:40]:
        print("ERROR:", e)
    for w in warns[:30]:
        print("WARN:", w)
    if len(errors) > 40:
        print(f"... +{len(errors)-40} erros")
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tsv", type=Path, help="arquivo .tsv do Lote")
    parser.add_argument(
        "--lang",
        choices=sorted(EXPORTS),
        help="idioma (default: detecta pela pasta/nome)",
    )
    parser.add_argument(
        "--skip-inventory-gate",
        action="store_true",
        help="não falhar por Deck Export ausente/velho (só avisa)",
    )
    args = parser.parse_args()
    return validate(args.tsv, args.lang, args.skip_inventory_gate)


if __name__ == "__main__":
    sys.exit(main())
