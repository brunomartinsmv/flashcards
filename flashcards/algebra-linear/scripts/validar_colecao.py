"""Confere correspondência das notas, cálculos e conteúdo do ZIP."""
import csv
import hashlib
import io
import json
import zipfile
from collections import Counter
import numpy as np
from gerar_colecao import ROOT, load_modules, render_card, package_paths


def read_deck(path, delimiter):
    text = path.read_text(encoding='utf-8')
    headers = [line for line in text.splitlines() if line.startswith('#')]
    for header in ['#html:true', '#tags column:3', '#deck column:4', '#separator:'+('Tab' if delimiter=='\t' else 'Comma')]:
        assert header in headers, (path, header)
    return list(csv.reader(io.StringIO('\n'.join(line for line in text.splitlines() if not line.startswith('#'))), delimiter=delimiter))


def main():
    modules = load_modules()
    expected = [render_card(m, c) for m in modules for c in m['cartoes']]
    actual = read_deck(ROOT / '00 - Álgebra linear completo.tsv', '\t')
    assert actual == expected
    assert all(len(row)==4 and all(field.strip() for field in row) for row in actual)
    fronts = [c['frente'] for m in modules for c in m['cartoes']]
    assert len(fronts)==len(set(fronts)), 'Frentes duplicadas.'
    assert len(modules)==len({m['numero'] for m in modules})
    for m in modules:
        assert read_deck(ROOT / f'{m["numero"]:02d} - {m["tema"]}.csv', ',') == [render_card(m, c) for c in m['cartoes']]
    calculated = json.loads((ROOT / 'exemplos/resultados.json').read_text())['calculados']
    checks = [c['verificacao_nucleo'] for m in modules for c in m['cartoes'] if 'verificacao_nucleo' in c]
    assert len(checks)==len({c['id'] for c in checks})
    assert set(calculated)=={c['id'] for c in checks}
    for c in checks:
        np.testing.assert_allclose(calculated[c['id']], c['esperado'], rtol=1e-10, atol=1e-10)
    with zipfile.ZipFile(ROOT / 'Álgebra linear - Anki.zip') as archive:
        assert archive.testzip() is None
        names = archive.namelist()
        assert len(names) == len(set(names)), "Entradas repetidas no ZIP."
        assert set(names) == {str(p.relative_to(ROOT)) for p in package_paths()}, "Arquivos ausentes ou inesperados no ZIP."
        for name in archive.namelist():
            assert archive.read(name)==(ROOT/name).read_bytes(), f'Pacote desatualizado: {name}'
    imported = json.loads((ROOT / "documentacao/importacao_anki.json").read_text(encoding="utf-8"))
    for path in [*ROOT.glob("*.tsv"), *ROOT.glob("[0-9][0-9] - *.csv")]:
        name = "flashcards/" + ROOT.name + "/" + path.name
        assert imported["sha256_arquivos"][name] == hashlib.sha256(path.read_bytes()).hexdigest(), "Teste Anki desatualizado: " + name
    report = {'cartoes': len(actual), 'modulos': len(modules), 'exemplos_numericos_verificados': len(checks),
              'tipos': dict(Counter(c['tipo'] for m in modules for c in m['cartoes'])),
              'csv_equivalente_tsv': True, 'integridade_zip': 'OK', 'importacao_no_anki': 'motor 2.1.66 em banco temporário; interface gráfica e perfil pessoal não usados'}
    (ROOT/'documentacao/validacao.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
