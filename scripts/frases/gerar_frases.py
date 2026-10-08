#!/usr/bin/env python3
"""Gera CSVs Anki de frases a partir de frases.json, sem alterar decks antigos."""
from __future__ import annotations
import csv, json, re, unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'scripts' / 'frases'
DATA = BASE / 'frases.json'
LANGS = {'it': ('italian', 'Italiano'), 'es': ('spanish', 'Espanhol'), 'en': ('english', 'Inglês')}
NIVEIS = {'basico': ('01', 'Básico'), 'intermediario': ('02', 'Intermediário'), 'avancado': ('03', 'Avançado')}
TEMAS = {'01': 'Rotina e organização', '02': 'Serviços compras e viagens', '03': 'Relações e comunicação', '04': 'Trabalho e colaboração', '05': 'Estudos e projetos'}
HEAD = ['#separator:Comma', '#html:false', '#tags column:3', '#deck column:4', '#columns:Frente,Verso,Tags,Deck']

def norm(s: str) -> str:
    s = unicodedata.normalize('NFKC', s).casefold()
    s = re.sub(r'[^\w]+', ' ', s, flags=re.UNICODE)
    return ' '.join(s.split())

def main() -> None:
    rows = json.loads(DATA.read_text(encoding='utf-8'))
    assert len(rows) == 450, f'Esperadas 450 intenções, encontradas {len(rows)}'
    ids = Counter((r['nivel'], r['tema']) for r in rows)
    assert set(ids) == {(n,t) for n in NIVEIS for t in TEMAS}
    assert all(v == 30 for v in ids.values()), ids
    all_counts = {}
    for lang, (folder, lang_name) in LANGS.items():
        fronts = [r[lang].strip() for r in rows]
        assert all(fronts), f'Frente vazia: {lang}'
        dup = [k for k,v in Counter(map(norm, fronts)).items() if v > 1]
        assert not dup, f'Frentes repetidas em {lang}: {dup[:5]}'
        old_file = BASE / 'frentes_anteriores.json'
        old = set(json.loads(old_file.read_text(encoding='utf-8')).get({'it':'italian','es':'spanish','en':'english'}[lang], []))
        collisions = sorted(set(map(norm, fronts)) & set(old))
        assert not collisions, f'Colisões locais em {lang}: {collisions[:5]}'
        target = ROOT / 'flashcards' / folder
        datasets = []
        for nivel, (nnum, nlabel) in NIVEIS.items():
            level_rows = [r for r in rows if r['nivel'] == nivel]
            level_items = []
            for tema, tlabel in TEMAS.items():
                selected = [r for r in level_rows if r['tema'] == tema]
                cards = []
                deck = f'idioms::{folder}::Frases::{nnum} {nlabel}::{tema} {tlabel}'
                for r in selected:
                    tags = f'frases idioma::{folder} nivel::{nnum}_{nivel} tema::{tema}_{tema_slug(tlabel)}'
                    cards.append([r[lang], r['pt'], tags, deck])
                name = f'Frases {nnum} - {nlabel} - {tema} {tlabel}.csv'
                write_csv(target/name, cards, deck)
                level_items += cards
            assert len(level_items) == 150
            level_name = f'Frases {nnum} - {nlabel} - Completo.csv'
            write_csv(target/level_name, level_items)
            datasets += level_items
        write_csv(target/'Frases - Completo.csv', datasets)
        all_counts[lang] = {'total': len(datasets), 'por_nivel': dict(Counter(r['nivel'] for r in rows)), 'por_tema_nivel': {f'{n}/{t}': ids[(n,t)] for n in NIVEIS for t in TEMAS}}
    old_inventory = json.loads((BASE / 'frentes_anteriores.json').read_text(encoding='utf-8'))
    manifest = {
        'fonte': 'scripts/frases/frases.json',
        'gerador': 'scripts/frases/gerar_frases.py',
        'escopo': 'arquivos locais; nenhuma coleção Anki ao vivo foi alterada',
        'direcao': 'frente no idioma estudado; verso em português brasileiro',
        'faixas': {'01 Básico': 150, '02 Intermediário': 150, '03 Avançado': 150},
        'temas_por_faixa': {f'{n} {name}': 30 for n,name in TEMAS.items()},
        'intencoes_alinhadas': len(rows),
        'cartoes_total': 1350,
        'por_idioma': {LANGS[k][0]: v for k,v in all_counts.items()},
        'colisoes_exatas_com_frentes_locais': {LANGS[k][0]: 0 for k in LANGS},
        'inventario_local_anterior': {k: {'frentes_unicas_normalizadas':len(v)} for k,v in old_inventory.items()},
        'arquivos_csv_por_idioma': 19,
        'observacao': 'Comparação de frentes com arquivos locais TSV/TXT preexistentes, após retirar marcação cloze/HTML e normalizar caixa e pontuação. A verificação não cobre decks remotos nem coleções Anki não exportadas.'
    }
    (BASE / 'manifesto.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'total_intencoes':len(rows),'cartoes':1350,'idiomas':all_counts},ensure_ascii=False,indent=2))

def tema_slug(value: str) -> str:
    value = unicodedata.normalize('NFKD', value).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '_', value).strip('_')

def write_csv(path: Path, cards: list[list[str]], deck: str|None=None) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8',newline='') as f:
        for h in HEAD[:4]: f.write(h+'\n')
        if deck: f.write('#deck:'+deck+'\n')
        f.write(HEAD[4]+'\n')
        w=csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        w.writerows(cards)

if __name__ == '__main__': main()
