from pathlib import Path
from collections import Counter
import csv
import json
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
LANGUAGES = {
    'italian': ('Italiano', 1),
    'spanish': ('Espanhol', 2),
    'english': ('Inglês', 3),
}


def slug(value):
    text = unicodedata.normalize('NFD', value.casefold())
    text = ''.join(char for char in text if not unicodedata.combining(char))
    return re.sub(r'[^a-z0-9]+', '_', text).strip('_')


def lemma(value):
    text = value.casefold().strip()
    text = re.sub(r'\s*\([^)]*\)', '', text)
    text = re.sub(r"^(?:il|lo|la|i|gli|le|el|los|las)\s+|^l'", '', text)
    return text.strip(' .!?')


def load_vocabulary():
    records = []
    for line in (Path(__file__).parent / 'vocabulario.txt').read_text().splitlines():
        if line.startswith('@'):
            number, theme, level = line[1:].split('|')
        elif line:
            translations = line.split('|')
            assert len(translations) == 4, line
            records.append((number, theme, level, translations))
    return records


def existing_fronts(folder):
    fronts = set()
    for path in folder.iterdir():
        if path.suffix not in {'.tsv', '.txt'}:
            continue
        with path.open(encoding='utf-8-sig', newline='') as stream:
            for row in csv.reader(stream, delimiter='\t'):
                if row and not row[0].startswith('#'):
                    fronts.add(lemma(row[0]))
    return fronts


def write_cards(path, cards, deck=None):
    with path.open('w', encoding='utf-8', newline='') as stream:
        stream.write('#separator:Comma\n#html:false\n#tags column:3\n')
        if deck:
            stream.write(f'#deck:{deck}\n')
        stream.write('#deck column:4\n')
        writer = csv.writer(stream, lineterminator='\n')
        writer.writerow(['#columns:Frente', 'Verso', 'Tags', 'Deck'])
        writer.writerows(cards)


def generate():
    records = load_vocabulary()
    assert len(records) == 600
    assert all(count == 25 for count in Counter(r[0] for r in records).values())
    report = {}
    for folder_name, (language, column) in LANGUAGES.items():
        folder = ROOT / 'flashcards' / folder_name
        known = existing_fronts(folder)
        themes = {}
        cards = []
        omitted = []
        for number, theme, level, translations in records:
            front = translations[column]
            back = translations[0]
            word = lemma(front)
            if word in known:
                omitted.append({'termo': front, 'portugues': back, 'motivo': 'Já está em um arquivo anterior do idioma.'})
                continue
            if folder_name == 'italian' and word == 'nipote':
                back += '; também pode significar neto, neta ou sobrinha, conforme o contexto.'
            deck = f'idioms::{folder_name}::Léxico::{level}::{number} {theme}'
            tags = f'lexico idioma::{slug(language)} tema::{slug(theme)} nivel::{slug(level)}'
            card = [front, back, tags, deck]
            cards.append(card)
            themes.setdefault((number, theme, level), []).append(card)
        distinct_words = {lemma(r[0]) for r in cards}
        single_words = {word for word in distinct_words if ' ' not in word}
        assert len(single_words) >= 500, (language, len(single_words))
        assert len({r[0] for r in cards}) == len(cards), language
        for (number, theme, level), group in themes.items():
            path = folder / f'Léxico {number} - {level} - {theme}.csv'
            write_cards(path, group, group[0][3])
        write_cards(folder / 'Léxico - Completo.csv', cards)
        report[folder_name] = {
            'cartoes': len(cards),
            'termos_distintos': len(distinct_words),
            'palavras_simples_distintas': len(single_words),
            'temas': len(themes),
            'omitidos_por_presenca_em_arquivos_anteriores': omitted,
        }
        with (folder / 'LEXICO.md').open('w', encoding='utf-8') as stream:
            stream.write(f'# Léxico de {language.lower()}\n\n')
            stream.write(f'{len(cards)} cartões, com {len(single_words)} palavras simples distintas, em {len(themes)} temas. Frente no idioma estudado; verso em português.\n\n')
            stream.write('Escolha os CSVs por tema ou `Léxico - Completo.csv`. Os dois formatos contêm os mesmos cartões. A coluna especial Deck cria os subdecks na importação dos cartões novos. Use um tipo de nota Basic com Frente e Verso.\n\n')
            stream.write('Básico e Intermediário são faixas didáticas desta coleção, atribuídas por tema. Não são níveis CEFR certificados por palavra. Nos substantivos de italiano e espanhol, o artigo ajuda a memorizar gênero e número. Em espanhol, `el agua` e `el águila` são femininos apesar do artigo `el` no singular. Os adjetivos aparecem na forma masculina singular quando há variação.\n\n')
            stream.write('Os sentidos ou classes gramaticais de palavras repetidas são identificados entre parênteses na frente, no idioma estudado. Algumas entradas são expressões necessárias para nomear um conceito, mas elas não contam no mínimo de 500 palavras simples. Inglês usa predominantemente grafia americana; espanhol inclui vocabulário latino-americano.\n\n')
            stream.write('A comparação de repetição usa apenas os arquivos TXT/TSV anteriores desta pasta. Não representa conferência do seu deck vivo no Anki. Notas já existentes, quando atualizadas, permanecem no deck atual.\n\n')
            for (number, theme, level), group in themes.items():
                name = f'Léxico {number} - {level} - {theme}.csv'
                stream.write(f'- [{name}](<{name}>): {len(group)} cartões.\n')
            stream.write('\nFonte editorial: seleção e tradução preparadas para esta coleção. Os níveis são uma organização de estudo, não uma lista oficial de frequência. Referência sobre níveis: [Conselho da Europa](https://www.coe.int/en/web/common-european-framework-reference-languages/level-descriptions). Não inclui áudio; importação no aplicativo Anki não foi executada.\n')
        print(language, len(cards), 'cartões;', len(single_words), 'palavras simples distintas')
    (Path(__file__).parent / 'manifesto.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    generate()
