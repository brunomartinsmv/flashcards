"""Importa as coleções de estudo em bancos Anki temporários, sem usar perfis pessoais."""
import csv
import hashlib
import importlib.metadata
import io
import json
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

from anki.collection import Collection
from anki.import_export_pb2 import ImportCsvRequest

ROOT = Path(__file__).resolve().parents[1]
ML = ROOT / 'flashcards/machine-learning'
AL = ROOT / 'flashcards/algebra-linear'


def read_rows(path):
    delimiter = '\t' if path.suffix == '.tsv' else ','
    return list(csv.reader(io.StringIO('\n'.join(line for line in path.read_text(encoding='utf-8').splitlines() if not line.startswith('#'))), delimiter=delimiter))


def import_file(collection, path):
    metadata = collection.get_csv_metadata(str(path), None)
    assert metadata.is_html and metadata.tags_column == 3 and metadata.deck_column == 4
    assert list(metadata.column_labels) == ['Frente', 'Verso', 'Tags', 'Deck']
    # Reproduz a escolha do tipo Basic e o mapeamento Frente/Verso no diálogo.
    metadata.global_notetype.id = collection.models.by_name('Basic')['id']
    metadata.global_notetype.field_columns[:] = [1, 2]
    collection.import_csv(ImportCsvRequest(path=str(path), metadata=metadata))


def verify_notes(collection, expected):
    assert collection.note_count() == len(expected)
    assert len(collection.find_cards('')) == len(expected)
    actual = {}
    image_cards = 0
    for nid in collection.find_notes(''):
        note = collection.get_note(nid)
        front, back = note.fields
        cards = note.cards()
        assert len(cards) == 1 and front and back
        assert front not in actual
        actual[front] = [back, set(note.tags), collection.decks.name(cards[0].did)]
        image_cards += '<img ' in front
    for front, back, tags, deck in expected:
        assert actual[front] == [back, set(tags.split()), deck], front
    return image_cards


def scenario(files, supplements=(), expected_files=None):
    expected = [row for path in (expected_files if expected_files is not None else files) for row in read_rows(path)]
    assert len(expected) == len({r[0] for r in expected}), 'Frentes repetidas entre coleções.'
    with TemporaryDirectory(prefix='flashcards-anki-') as directory:
        collection = Collection(str(Path(directory) / 'collection.anki2'))
        try:
            for image in (ML / 'media').glob('*.png'):
                shutil.copy2(image, Path(collection.media.dir()) / image.name)
            for path in files:
                import_file(collection, path)
            image_cards = verify_notes(collection, expected)
            for path in [*files, *supplements]:
                import_file(collection, path)
            assert verify_notes(collection, expected) == image_cards
            media = collection.media.check()
            assert not media.missing and not media.unused
            return {'notas':len(expected), 'cartoes':len(expected), 'cartoes_com_imagem':image_cards,
                    'frente_verso_tags_deck':'OK', 'reimportacao_sem_duplicatas':True, 'midia_ausente':list(media.missing)}
        finally:
            collection.close()


def main():
    report = {'anki':importlib.metadata.version('anki'),
              'tipo':'motor Anki em bancos temporários; sem interface gráfica e sem perfil pessoal',
              'tsv':scenario([ML/'00 - Machine learning completo.tsv', AL/'00 - Álgebra linear completo.tsv'],
                             [ML/'00 - Estatística e métricas complemento.tsv', ML/'00 - Probabilidade inferência e modelos complemento.tsv']),
              'csv':scenario(sorted(ML.glob('[0-9][0-9] - *.csv')) + sorted(AL.glob('[0-9][0-9] - *.csv')),
                             expected_files=[ML/'00 - Machine learning completo.tsv', AL/'00 - Álgebra linear completo.tsv'])}
    inputs = [*ML.glob("[0-9][0-9] - *.csv"), *AL.glob("[0-9][0-9] - *.csv"), *ML.glob("*.tsv"), *AL.glob("*.tsv")]
    report["sha256_arquivos"] = {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(inputs)}
    for root in [ML, AL]:
        (root/'documentacao/importacao_anki.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
