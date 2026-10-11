"""Confere formato, correspondência editorial, mídia e integridade do pacote."""

import csv
import hashlib
import io
import json
import re
import zipfile
from collections import Counter
from pathlib import Path

import numpy as np

from gerar_colecao import ROOT, load_modules, render_card, package_paths


def read_deck(path, delimiter):
    text = path.read_text(encoding="utf-8")
    headers = [line for line in text.splitlines() if line.startswith("#")]
    assert "#html:true" in headers and "#tags column:3" in headers and "#deck column:4" in headers
    assert "#separator:" + ("Tab" if delimiter == "\t" else "Comma") in headers
    return list(csv.reader(io.StringIO("\n".join(line for line in text.splitlines() if not line.startswith("#"))), delimiter=delimiter))


def main():
    data = {"modulos": load_modules()}
    expected = [render_card(m, c) for m in data["modulos"] for c in m["cartoes"]]
    actual = read_deck(ROOT / "00 - Machine learning completo.tsv", "\t")
    assert actual == expected, "O TSV completo diverge da fonte editorial."
    assert all(len(row) == 4 and all(field.strip() for field in row) for row in actual)
    fronts = [c["frente"] for m in data["modulos"] for c in m["cartoes"]]
    assert len(data["modulos"]) == len({m["numero"] for m in data["modulos"]}), "Números de módulo duplicados."
    assert len(fronts) == len(set(fronts)), "Frentes duplicadas."
    thematic = []
    for m in data["modulos"]:
        rows = read_deck(ROOT / f'{m["numero"]:02d} - {m["tema"]}.csv', ",")
        assert rows == [render_card(m, c) for c in m["cartoes"]]
        thematic.extend(rows)
    assert thematic == actual
    supplement = read_deck(ROOT / "00 - Estatística e métricas complemento.tsv", "\t")
    assert supplement == [render_card(m, c) for m in data["modulos"] if 13 <= m["numero"] <= 21 for c in m["cartoes"]]
    extension = read_deck(ROOT / "00 - Probabilidade inferência e modelos complemento.tsv", "\t")
    assert extension == [render_card(m, c) for m in data["modulos"] if m["numero"] >= 22 for c in m["cartoes"]]
    from numpy.testing import assert_allclose
    core = json.loads((ROOT / "exemplos/resultados_nucleo.json").read_text(encoding="utf-8"))
    core_checks = [c["verificacao_nucleo"] for m in data["modulos"] for c in m["cartoes"] if "verificacao_nucleo" in c]
    assert len(core_checks) == len({c["id"] for c in core_checks})
    assert set(core["calculados"]) == {c["id"] for c in core_checks}
    for check in core_checks:
        assert_allclose(core["calculados"][check["id"]], check["esperado"], rtol=1e-10, atol=1e-10)
    numerical = json.loads((ROOT / "exemplos/resultados_metricas.json").read_text(encoding="utf-8"))
    checks = [c["verificacao"] for m in data["modulos"] for c in m["cartoes"] if "verificacao" in c]
    assert len(checks) == len({c["id"] for c in checks}), "IDs de cálculo duplicados."
    assert set(numerical["calculados"]) == {c["id"] for c in checks}, "Cobertura dos cálculos incompleta."
    for check in checks:
        assert abs(numerical["calculados"][check["id"]] - check["esperado"]) < 1e-10, check["id"]
    fundamentals = json.loads((ROOT / "exemplos/resultados_fundamentos.json").read_text(encoding="utf-8"))["calculados"]
    basic_checks = [c["verificacao_fundamentos"] for m in data["modulos"] for c in m["cartoes"] if "verificacao_fundamentos" in c]
    assert len(basic_checks) == len({c["id"] for c in basic_checks})
    assert set(fundamentals) == {c["id"] for c in basic_checks}
    for check in basic_checks:
        np.testing.assert_allclose(fundamentals[check["id"]], check["esperado"], rtol=0, atol=1e-10)
    metric_names = {c["metrica"] for m in data["modulos"] for c in m["cartoes"] if "metrica" in c}
    for name in metric_names:
        cards = [c for m in data["modulos"] for c in m["cartoes"] if c.get("metrica") == name]
        assert any(c["tipo"] == "conceito" for c in cards) and any(c["tipo"] == "exercicio" and "verificacao" in c for c in cards), name
    image_refs = [name for row in actual for name in re.findall(r'<img src="([^"]+)"', row[0])]
    images = sorted((ROOT / "media").glob("*.png"))
    assert set(image_refs) == {p.name for p in images}, "Imagem ausente ou não usada."
    for path in images:
        assert path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"), f"PNG inválido: {path}"
    with zipfile.ZipFile(ROOT / "Machine learning - Anki e imagens.zip") as archive:
        assert archive.testzip() is None
        names = archive.namelist()
        assert len(names) == len(set(names)), "Entradas repetidas no ZIP."
        assert set(names) == {str(p.relative_to(ROOT)) for p in package_paths()}, "Arquivos ausentes ou inesperados no ZIP."
        for name in archive.namelist():
            assert archive.read(name) == (ROOT / name).read_bytes(), f"Pacote desatualizado: {name}"
        assert all("media/" + name in archive.namelist() for name in set(image_refs))
    results = json.loads((ROOT / "exemplos/resultados.json").read_text(encoding="utf-8"))
    assert results["reforco"]["trajetoria_gulosa"] == [0, 1, 2, 3, 4]
    assert results["reducao"]["variancia_retida"] >= 0.95
    assert results["imoveis"]["ridge"]["mae_reais"] < results["imoveis"]["baseline_media"]["mae_reais"]
    imported = json.loads((ROOT / "documentacao/importacao_anki.json").read_text(encoding="utf-8"))
    for path in [*ROOT.glob("*.tsv"), *ROOT.glob("[0-9][0-9] - *.csv")]:
        name = "flashcards/" + ROOT.name + "/" + path.name
        assert imported["sha256_arquivos"][name] == hashlib.sha256(path.read_bytes()).hexdigest(), "Teste Anki desatualizado: " + name
    report = {"cartoes": len(actual), "modulos": len(data["modulos"]), "imagens": len(images),
              "cartoes_complemento": len(supplement), "cartoes_novo_nucleo": len(extension),
              "exemplos_nucleo_verificados": len(core_checks), "exemplos_fundamentos_verificados": len(basic_checks), "metricas_perdas_indicadores": len(metric_names),
              "exemplos_numericos_verificados": len(checks),
              "cartoes_com_imagem": len(image_refs),
              "tipos": dict(Counter(c["tipo"] for m in data["modulos"] for c in m["cartoes"])),
              "integridade_zip": "OK", "csv_equivalente_tsv": True,
              "importacao_no_anki": "motor 2.1.66 em banco temporário; interface gráfica e perfil pessoal não usados", "revisao_visual_imagens": "realizada na criação",
              "sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in images}}
    (ROOT / "documentacao/validacao.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
