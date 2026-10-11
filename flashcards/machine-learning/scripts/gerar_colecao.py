"""Gera arquivos Basic para o Anki a partir da fonte editorial em JSON."""

import csv
import html
import json
import re
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_modules():
    modules = []
    for name in ["cartoes.json", "estatistica_metricas.json", "nucleo_estatistico.json"]:
        modules.extend(json.loads((ROOT / "fontes" / name).read_text(encoding="utf-8"))["modulos"])
    return modules


def markup(text):
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", html.escape(text))


def render_card(module, card):
    front = markup(card["frente"])
    if card.get("imagem"):
        front += (
            '<br><img src="' + html.escape(card["imagem"], quote=True)
            + '" style="max-width:100%;height:auto" alt="Ilustração do exercício">'
        )
    back = markup(card["verso"])
    source = card.get("fonte", module["fonte"])
    if source.startswith("local:"):
        citation = html.escape(source.removeprefix("local:"))
    else:
        citation = '<a href="' + html.escape(source, quote=True) + '">Referência técnica</a>'
    back += '<br><br><small>Fonte: ' + citation + ". Exemplo autoral quando aplicável.</small>"
    tags = f'ml ml::{module["numero"]:02d} nivel::{module["nivel"]} tipo::{card["tipo"]}'
    deck = f'Machine learning::{module["numero"]:02d} {module["tema"]}'
    return [front, back, tags, deck]


def write_deck(path, rows, delimiter):
    with path.open("w", encoding="utf-8", newline="") as stream:
        stream.write("#separator:" + ("Tab" if delimiter == "\t" else "Comma") + "\n")
        stream.write("#html:true\n#tags column:3\n#deck column:4\n")
        stream.write("#columns:" + delimiter.join(["Frente", "Verso", "Tags", "Deck"]) + "\n")
        csv.writer(stream, delimiter=delimiter, lineterminator="\n").writerows(rows)


def package_paths():
    paths = [ROOT / '00 - Machine learning completo.tsv', ROOT / "00 - Estatística e métricas complemento.tsv", ROOT / "00 - Probabilidade inferência e modelos complemento.tsv", ROOT / "README.md", ROOT / "INDICE.md", ROOT / "ESTUDAR.html"]
    paths.extend(ROOT.glob("[0-9][0-9] - *.csv"))
    for directory in ["media", "fontes", "exemplos", "scripts", "documentacao"]:
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
    complete = ROOT / "00 - Machine learning completo.tsv"
    write_deck(complete, all_rows, "\t")
    supplement = ROOT / "00 - Estatística e métricas complemento.tsv"
    write_deck(supplement, [render_card(m, c) for m in modules if 13 <= m["numero"] <= 21 for c in m["cartoes"]], "\t")
    extension = ROOT / "00 - Probabilidade inferência e modelos complemento.tsv"
    write_deck(extension, [render_card(m, c) for m in modules if m["numero"] >= 22 for c in m["cartoes"]], "\t")
    index.extend(["", f"Total: {len(all_rows)} notas Basic, uma pergunta por nota.", "", "Escolha o TSV completo ou os CSVs por estudo. Ambos contêm as mesmas notas.", ""])
    (ROOT / "INDICE.md").write_text("\n".join(index), encoding="utf-8")
    coverage = ["# Cobertura de métricas, perdas e indicadores", "",
                "Cada item abaixo tem definição, interpretação e exemplo numérico resolvido. O inventário declara a cobertura; não representa todas as métricas possíveis de qualquer domínio.", "",
                "| Estudo | Métrica, perda ou indicador | Exemplo verificável |", "| --- | --- | --- |"]
    for m in modules:
        names = sorted({c["metrica"] for c in m["cartoes"] if "metrica" in c})
        for name in names:
            exercise = next(c for c in m["cartoes"] if c.get("metrica") == name and c["tipo"] == "exercicio")
            coverage.append(f'| {m["numero"]:02d} | {name} | {exercise["verificacao"]["id"]} |')
    coverage.extend(["", "Estatística descritiva, probabilidade e inferência têm módulos próprios, com exercícios adicionais.", ""])
    (ROOT / "documentacao/COBERTURA_METRICAS.md").write_text("\n".join(coverage), encoding="utf-8")

    cards_html = []
    for front, back, tags, deck in all_rows:
        front = front.replace('src="ml_', 'src="media/ml_')
        cards_html.append('<article data-tags="' + tags + '"><small>' + html.escape(deck)
                          + '</small><h2>' + front + '</h2><details><summary>Mostrar resposta</summary>'
                          + '<p>' + back + '</p></details></article>')
    page = '''<!doctype html><html lang="pt-BR"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Machine learning: cartões de estudo</title>
<style>body{font:17px/1.6 system-ui;background:#f3f5f7;color:#172330;max-width:850px;margin:30px auto;padding:16px}
article{background:white;padding:22px;margin:18px 0;border-radius:12px}h2{font-size:20px}small{color:#4e6175}
img{display:block;max-width:100%;max-height:480px;object-fit:contain;margin:12px auto}summary{cursor:pointer;color:#1455a0}
input{padding:12px;font:inherit;width:90%}code{background:#eef1f5}header{margin-bottom:25px}</style>
<header><h1>Machine learning</h1><p>TOTAL_CARDS cartões de introdução e revisão. Tente responder antes de abrir o verso.</p>
<label>Buscar tema ou pergunta <input id="busca" type="search" placeholder="Ex.: SVM, ml::07 ou nivel::avancado"></label>
<p id="contagem"></p></header>''' + "\n".join(cards_html) + '''
<script>const cards=[...document.querySelectorAll('article')];const input=document.querySelector('#busca');
function filter(){const q=input.value.toLocaleLowerCase('pt-BR');let n=0;
for(const c of cards){c.hidden=!(c.textContent+' '+c.dataset.tags).toLocaleLowerCase('pt-BR').includes(q);if(!c.hidden)n++;}
document.querySelector('#contagem').textContent=n+' cartões exibidos';}input.addEventListener('input',filter);filter();</script></html>'''
    page = page.replace("TOTAL_CARDS cartões", f"{len(all_rows)} cartões")
    (ROOT / "ESTUDAR.html").write_text(page, encoding="utf-8")

    package = ROOT / "Machine learning - Anki e imagens.zip"
    with zipfile.ZipFile(package, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in package_paths():
            archive.write(path, path.relative_to(ROOT))
    print(f"Gerados {len(all_rows)} cartões em {len(modules)} módulos; pacote {package.name}.")


if __name__ == "__main__":
    main()
