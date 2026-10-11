"""Gera arquivos Basic para o Anki a partir da fonte editorial em JSON."""

import csv
import html
import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_modules():
    return json.loads((ROOT / "fontes/cartoes.json").read_text(encoding="utf-8"))["modulos"]


def markup(text):
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", html.escape(text))


def render_card(module, card):
    front = markup(card["frente"])
    back = markup(card["verso"])
    source = card.get("fonte", module["fonte"])
    if source.startswith("local:"):
        citation = html.escape(source.removeprefix("local:"))
    else:
        citation = '<a href="' + html.escape(source, quote=True) + '">Referência técnica</a>'
    back += '<br><br><small>Fonte: ' + citation + ". Exemplo autoral quando aplicável.</small>"
    tags = f'algebra_linear algebra_linear::{module["numero"]:02d} nivel::{module["nivel"]} tipo::{card["tipo"]}'
    deck = f'Álgebra linear::{module["numero"]:02d} {module["tema"]}'
    return [front, back, tags, deck]


def write_deck(path, rows, delimiter):
    with path.open("w", encoding="utf-8", newline="") as stream:
        stream.write("#separator:" + ("Tab" if delimiter == "\t" else "Comma") + "\n")
        stream.write("#html:true\n#tags column:3\n#deck column:4\n")
        stream.write("#columns:" + delimiter.join(["Frente", "Verso", "Tags", "Deck"]) + "\n")
        csv.writer(stream, delimiter=delimiter, lineterminator="\n").writerows(rows)


def package_paths():
    paths = [ROOT / '00 - Álgebra linear completo.tsv', ROOT / "README.md", ROOT / "INDICE.md", ROOT / "ESTUDAR.html"]
    paths.extend(ROOT.glob("[0-9][0-9] - *.csv"))
    for directory in ["fontes", "exemplos", "scripts", "documentacao"]:
        paths.extend(p for p in (ROOT / directory).rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    return sorted(paths)


def main():
    modules = load_modules()
    all_rows = []
    index = ["# Ordem de estudo", "", "| Estudo | Tema | Cartões | Nível |", "| --- | --- | ---: | --- |"]
    for module in modules:
        name = f'{module["numero"]:02d} - {module["tema"]}.csv'
        rows = [render_card(module, card) for card in module["cartoes"]]
        write_deck(ROOT / name, rows, ",")
        all_rows.extend(rows)
        index.append(f'| {module["numero"]:02d} | [{module["tema"]}]({name.replace(" ", "%20")}) | {len(rows)} | {module["nivel"]} |')
    complete = ROOT / "00 - Álgebra linear completo.tsv"
    write_deck(complete, all_rows, "\t")
    index.extend(["", f"Total: {len(all_rows)} notas Basic.", "", "Escolha o TSV completo ou os CSVs por estudo. Ambos contêm as mesmas notas.", ""])
    (ROOT / "INDICE.md").write_text("\n".join(index), encoding="utf-8")

    cards_html = []
    for front, back, tags, deck in all_rows:
        cards_html.append('<article data-tags="' + tags + '"><small>' + html.escape(deck)
                          + '</small><h2>' + front + '</h2><details><summary>Mostrar resposta</summary>'
                          + '<p>' + back + '</p></details></article>')
    page = '''<!doctype html><html lang="pt-BR"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Álgebra linear: cartões de estudo</title>
<style>body{font:17px/1.6 system-ui;background:#f3f5f7;color:#172330;max-width:850px;margin:30px auto;padding:16px}
article{background:white;padding:22px;margin:18px 0;border-radius:12px}h2{font-size:20px}small{color:#4e6175}
img{display:block;max-width:100%;max-height:480px;object-fit:contain;margin:12px auto}summary{cursor:pointer;color:#1455a0}
input{padding:12px;font:inherit;width:90%}code{background:#eef1f5}header{margin-bottom:25px}</style>
<header><h1>Álgebra linear</h1><p>TOTAL_CARDS cartões de introdução e prática. Tente responder antes de abrir o verso.</p>
<label>Buscar tema ou pergunta <input id="busca" type="search" placeholder="Ex.: projeção, SVD ou algebra_linear::03"></label>
<p id="contagem"></p></header>''' + "\n".join(cards_html) + '''
<script>const cards=[...document.querySelectorAll('article')];const input=document.querySelector('#busca');
function filter(){const q=input.value.toLocaleLowerCase('pt-BR');let n=0;
for(const c of cards){c.hidden=!(c.textContent+' '+c.dataset.tags).toLocaleLowerCase('pt-BR').includes(q);if(!c.hidden)n++;}
document.querySelector('#contagem').textContent=n+' cartões exibidos';}input.addEventListener('input',filter);filter();</script></html>'''
    page = page.replace("TOTAL_CARDS cartões", f"{len(all_rows)} cartões")
    (ROOT / "ESTUDAR.html").write_text(page, encoding="utf-8")

    package = ROOT / "Álgebra linear - Anki.zip"
    with zipfile.ZipFile(package, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in package_paths():
            archive.write(path, path.relative_to(ROOT))
    print(f"Gerados {len(all_rows)} cartões em {len(modules)} módulos; pacote {package.name}.")


if __name__ == "__main__":
    main()
