"""Verifica que os validadores rejeitam perdas e alterações nos artefatos."""
import csv
import io
import json
from html.parser import HTMLParser
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ('machine-learning', 'algebra-linear')


class ArtifactValidation(unittest.TestCase):
    def prepare(self, topic, directory):
        target = Path(directory) / 'flashcards' / topic
        shutil.copytree(ROOT / 'flashcards' / topic, target, ignore=shutil.ignore_patterns('__pycache__'))
        return target

    def run_script(self, target, name):
        return subprocess.run([sys.executable, str(target / 'scripts' / name)], capture_output=True, text=True)

    def test_complete_packages_pass(self):
        for topic in TOPICS:
            with self.subTest(topic=topic), tempfile.TemporaryDirectory() as directory:
                target = self.prepare(topic, directory)
                result = self.run_script(target, 'validar_colecao.py')
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_zip_member_fails(self):
        for topic in TOPICS:
            with self.subTest(topic=topic), tempfile.TemporaryDirectory() as directory:
                target = self.prepare(topic, directory)
                package = next(target.glob('*.zip'))
                with zipfile.ZipFile(package) as archive:
                    content = {n:archive.read(n) for n in archive.namelist() if n != 'ESTUDAR.html'}
                with zipfile.ZipFile(package, 'w', zipfile.ZIP_DEFLATED) as archive:
                    for name, data in content.items():
                        archive.writestr(name, data)
                result = self.run_script(target, 'validar_colecao.py')
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('Arquivos ausentes ou inesperados no ZIP', result.stderr)

    def test_changed_answer_fails(self):
        for topic in TOPICS:
            with self.subTest(topic=topic), tempfile.TemporaryDirectory() as directory:
                target = self.prepare(topic, directory)
                deck = next(target.glob('*completo.tsv'))
                text = deck.read_text(encoding='utf-8')
                lines = text.splitlines()
                first = next(i for i,line in enumerate(lines) if not line.startswith('#'))
                fields = lines[first].split('\t')
                fields[1] = 'Resposta adulterada'
                lines[first] = '\t'.join(fields)
                deck.write_text('\n'.join(lines)+'\n',encoding='utf-8')
                result = self.run_script(target, 'validar_colecao.py')
                self.assertNotEqual(result.returncode, 0)

    def test_changed_calculation_fails(self):
        for topic in TOPICS:
            with self.subTest(topic=topic), tempfile.TemporaryDirectory() as directory:
                target = self.prepare(topic, directory)
                result_path = target/'exemplos'/('resultados_metricas.json' if topic=='machine-learning' else 'resultados.json')
                data = json.loads(result_path.read_text(encoding='utf-8'))
                key = next(iter(data['calculados']))
                data['calculados'][key] = 123456
                result_path.write_text(json.dumps(data),encoding='utf-8')
                generated = self.run_script(target, 'gerar_colecao.py')
                self.assertEqual(generated.returncode, 0, generated.stderr)
                result = self.run_script(target, 'validar_colecao.py')
                self.assertNotEqual(result.returncode, 0)

    def test_obsolete_csv_rejected(self):
        for topic in TOPICS:
            with self.subTest(topic=topic), tempfile.TemporaryDirectory() as directory:
                target = self.prepare(topic, directory)
                old = target / '99 - Tema antigo.csv'
                old.write_text('#separator:Comma\nPergunta antiga,Resposta antiga\n', encoding='utf-8')
                generated = self.run_script(target, 'gerar_colecao.py')
                self.assertNotEqual(generated.returncode, 0)
                self.assertIn('CSVs fora da fonte editorial', generated.stderr)
                self.assertTrue(old.exists())
                validated = self.run_script(target, 'validar_colecao.py')
                self.assertNotEqual(validated.returncode, 0)
                self.assertIn('CSVs divergentes da fonte editorial', validated.stderr)

    def test_renamed_or_removed_module_preserves_old_csv(self):
        for topic in TOPICS:
            for change in ('renamed', 'removed'):
                with self.subTest(topic=topic, change=change), tempfile.TemporaryDirectory() as directory:
                    target = self.prepare(topic, directory)
                    source = target / 'fontes/cartoes.json'
                    data = json.loads(source.read_text(encoding='utf-8'))
                    first = data['modulos'][0]
                    previous = target / f'{first["numero"]:02d} - {first["tema"]}.csv'
                    saved = previous.read_bytes()
                    if change == 'renamed':
                        first['tema'] += ' revisado'
                    else:
                        data['modulos'].pop(0)
                    source.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
                    generated = self.run_script(target, 'gerar_colecao.py')
                    self.assertNotEqual(generated.returncode, 0)
                    self.assertIn(previous.name, generated.stderr)
                    self.assertEqual(previous.read_bytes(), saved)

    def test_images_without_prefix_use_media(self):
        class Images(HTMLParser):
            def __init__(self):
                super().__init__()
                self.sources = []

            def handle_starttag(self, tag, attrs):
                if tag == 'img':
                    self.sources.append(dict(attrs)['src'])

        with tempfile.TemporaryDirectory() as directory:
            target = self.prepare('machine-learning', directory)
            name = 'figura SVD & projeção.png'
            (target / 'media/ml_knn.png').rename(target / 'media' / name)
            source = target / 'fontes/cartoes.json'
            data = json.loads(source.read_text(encoding='utf-8'))
            for module in data['modulos']:
                for card in module['cartoes']:
                    if card.get('imagem') == 'ml_knn.png':
                        card['imagem'] = name
            source.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
            generated = self.run_script(target, 'gerar_colecao.py')
            self.assertEqual(generated.returncode, 0, generated.stderr)
            images = Images()
            images.feed((target / 'ESTUDAR.html').read_text(encoding='utf-8'))
            self.assertIn('media/' + name, images.sources)
            for filename in images.sources:
                self.assertTrue((target / filename).is_file(), filename)
            anki = (target / '00 - Machine learning completo.tsv').read_text(encoding='utf-8')
            anki_images = Images()
            rows = csv.reader(io.StringIO("\n".join(line for line in anki.splitlines() if not line.startswith('#'))), delimiter='\t')
            for row in rows:
                anki_images.feed(row[0])
            self.assertIn(name, anki_images.sources)
            self.assertTrue(all(not filename.startswith('media/') for filename in anki_images.sources))

    def test_broken_study_image_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            target = self.prepare('machine-learning', directory)
            page = target / 'ESTUDAR.html'
            page.write_text(page.read_text(encoding='utf-8').replace('src="media/', 'src="', 1), encoding='utf-8')
            validated = self.run_script(target, 'validar_colecao.py')
            self.assertNotEqual(validated.returncode, 0)
            self.assertIn('Referências de imagem inválidas na página de estudo', validated.stderr)


if __name__ == '__main__':
    unittest.main()
