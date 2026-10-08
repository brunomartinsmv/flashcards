from pathlib import Path
import csv, re

BASE = Path('flashcards/cpa')
SOURCE = Path('flashcards/cpa/fontes/apostila_cpa.txt')
pages = SOURCE.read_text(encoding='utf-8').split('\f')

def rows(path):
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.reader(f, delimiter='\t'))

files = sorted(BASE.glob('cpa_[0-9][0-9].tsv'))
assert len(files) == 27, len(files)
all_rows = []
fronts = set()
for path in files:
    data = rows(path)
    assert data[:3] == [
        ['#separator:Tab'], ['#html:true'], ['#tags column:3'],
    ], (path, data[:3])
    assert ['#deck column:4'] in data
    assert ['#columns:Frente', 'Verso', 'Tags', 'Deck'] in data
    notes = [r for r in data if r and not r[0].startswith('#')]
    assert notes, path
    for row in notes:
        assert len(row) == 4 and all(row), (path, row)
        front, back, tags, deck = row
        assert deck.startswith(f'CPA::{path.stem[-2:]} '), (path, deck)
        assert [f'#deck:{deck}'] in data, (path, deck)
        assert front not in fronts, ('duplicate front', front)
        fronts.add(front)
        assert 'cpa::apostila' in tags.split(), (path, tags)
        assert f'cpa::{path.stem[-2:]}' in tags.split(), (path, tags)
        refs = re.findall(r'p\. impressa ([0-9]+(?: e [0-9]+)*) \(PDF ([0-9]+(?: e [0-9]+)*)\)', back)
        assert refs, ('missing page ref', front)
        for printed, pdf in refs:
            printed_pages = [int(x) for x in printed.split(' e ')]
            pdf_pages = [int(x) for x in pdf.split(' e ')]
            assert printed_pages == pdf_pages, (front, printed_pages, pdf_pages)
            for page in pdf_pages:
                assert pages[page - 1].strip(), ('empty cited page', front, page)
                assert re.search(rf'(?m)^\s*{page}\s*$', pages[page - 1]), ('footer mismatch', front, page)
    all_rows.extend(notes)
consolidated = rows(BASE / 'cpa_apostila_completo.tsv')
assert ['#deck column:4'] in consolidated
consolidated_notes = [r for r in consolidated if r and not r[0].startswith('#')]
assert len(consolidated_notes) == len(all_rows)
assert {tuple(r) for r in consolidated_notes} == {tuple(r) for r in all_rows}
assert len(consolidated_notes) == len(fronts)
coverage = list(csv.DictReader((BASE / 'apostila/cobertura.csv').open(encoding='utf-8-sig', newline='')))
assert len(coverage) == 37, len(coverage)
assert {r['Tarefa'] for r in coverage} == {f'CPA {i:02d}' for i in range(3, 40)}
inventory = list(csv.DictReader((BASE / 'apostila/inventario_subtopicos.csv').open(encoding='utf-8-sig', newline='')))
assert inventory and all(int(r['Quantidade de cartões']) > 0 and r['IDs/cartões vinculados'] for r in inventory)

# Numeric examples used in the cards.
assert round(1500 * 1.014**6, 2) == 1630.49
assert round((1.15 / 1.05 - 1) * 100, 2) == 9.52
assert round(((1.04**12) - 1) * 100, 2) == 60.10
assert round(12000000 * 0.006 / 252, 2) == 285.71
assert round(50000 * 0 + 25000/1.08 + 20000/1.08**2 + 15000/1.08**3 - 50000, 2) == 2202.41
assert round(100*10 + 100*12) / 200 == 11
assert round(27000 * 0.15, 2) == 4050
print(f'OK: {len(files)} topical decks, {len(fronts)} unique notes, {len(coverage)} study tasks, {len(inventory)} indexed subtopics; cited page footers and numeric examples verified.')
