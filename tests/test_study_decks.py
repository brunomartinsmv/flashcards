"""Verifica que os validadores rejeitam perdas e alterações nos artefatos."""
import json
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


if __name__ == '__main__':
    unittest.main()
