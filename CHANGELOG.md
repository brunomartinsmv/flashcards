# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-10-08

### Added

- Coleções de italiano, espanhol e inglês com mais de 500 palavras simples por idioma e 450 frases por idioma, divididas em três níveis e cinco temas por nível.
- Coleção CPA com 317 notas da apostila em 27 temas, quatro decks anteriores e índices de cobertura do plano de estudos.
- Consolidados dos lotes anteriores de idiomas e scripts de geração das coleções.
- READMEs por conteúdo, declaração do uso de IA e instruções de importação.
- CC BY 4.0 para os flashcards novos e a documentação autoral nova, com exemplo de atribuição e NOTICE. Apache 2.0 preservada nos scripts e materiais anteriores.

### Changed

- Escopo do repositório ampliado para todos os flashcards usados pelo autor.
- Arquivos importáveis organizados diretamente na pasta de cada conteúdo.
- Destinos dos novos cartões de idiomas dentro de `idioms::italian`, `idioms::spanish` e `idioms::english`, com subdecks por nível e tema.
- README principal e descrição do repositório atualizados para a biblioteca pessoal compartilhada.

### Fixed

- Frentes da apostila CPA diferenciadas das dos TXT anteriores (arranjo de pagamento e risco de concentração), para importação conjunta no mesmo tipo Basic.
- Versos de `la notizia` e `la noticia` restritos ao singular `notícia`; inglês `news` mantém `notícia; notícias`.
- Corte de IMA-B 5 / IMA-B 5+ alinhado à metodologia ANBIMA (inferior vs igual ou superior a 5 anos).
- Distinção Ibovespa × IBrX corrigida: ambos ponderam por free float; negociabilidade na seleção e tetos no Ibovespa.
- Condicional `se` preservada nas traduções do cartão do alarme; inglês de `com mais calma` passado para `more calmly`.
- Isenção de CPR restringida às condições da Lei 11.033/2004, art. 3º, V, e da Lei 8.929/1994, art. 2º, § 2º.
- Tags `idioma::italiano`, `idioma::espanhol` e `idioma::ingles` unificadas entre os geradores de frases e de léxico.
- Reserva hoteleira em italiano e espanhol passada para `a nome mio` e `a nombre mío`.
- Importação do léxico orientada a um tipo de nota Basic por idioma, para evitar colisão de frentes iguais.
- Exemplo de resgate em 6 meses alinhado à faixa de 181 a 360 dias da tabela regressiva.
- Quórum de instalação de assembleia geral de fundos alinhado à Resolução CVM 175 e sigla CPR corrigida na isenção de renda fixa.
- Frases de idiomas com aviso prévio em inglês e prazo prometido de reparo em italiano.
- Tradução de entrega antecipada em inglês, cálculos de resgate líquido e duration e seleções das revisões CPA08 e CPA20.
- Nomes de CSVs CPA compatíveis com Windows e leitura explícita de UTF-8 no gerador de léxico.
- Traduções de padrão estatístico em italiano, direção de “contar com alguém” e gênero de `il nipote`.
- Requisitos de isenção de rendimentos de FII corrigidos com referência complementar à Lei 11.033/2004.
- Guia de origem CPA esclarece que o gerador e o relatório dos TXT anteriores não estão disponíveis.

### Removed

- PDF de referência científica da árvore publicada. A referência bibliográfica permanece; o histórico Git anterior não foi reescrito.

### Security

- Livros, apostilas, formatos de e-book, PDFs, extração integral da apostila CPA e relatórios pessoais do Anki excluídos da publicação por regras do `.gitignore`.


## [1.0.0] - 2026-07-24

### Added

- Domain vocabulary and relationships in `CONTEXT.md` (Language, Fluency, Production, Lote, Inventory Gate, Review Gate, Prompt Import, and related terms).
- Architecture Decision Records under `docs/adr/`:
  - `0001` Process Skill + Language Profiles
  - `0002` Cloze as the default note type
  - `0003` Inventory Gate, Review Gate, and Prompt Import
- Shared process skill `skills/language-anki-flashcards/` with Language Profiles for Spanish and English and `scripts/validate_flashcards.py`.
- Language Folders under `flashcards/spanish/` and `flashcards/english/`.
- Spanish weekly **Lotes** (May–June 2026 Basic batches and the 2026-07-24 Cloze / Basic transition pair).
- `.gitignore` for local junk and Python bytecode.

### Changed

- README rewritten around the personal language → Anki workshop (inventory, Cloze format, validation, import policy) instead of the generic prompt toolkit.
- Legacy generic prompts, banking example, and spaced-repetition reference material moved under `archive/`.

### Deprecated

- Basic/`_____` note type for new **Lotes** (kept only as legacy; Cloze is the default going forward).

## [0.1.0] - 2026-02-19

### Added

- Initial repository: README on spaced repetition (spacing effect, testing effect, Leitner).
- Generic Anki generation prompts (complete, short, and web).
- Banking services example (notes + TSV output).
- Assets for the forgetting curve and Leitner system.
- Local copies of spaced-repetition reference sources.
- MIT `LICENSE` and GitHub repository settings for description/topics.

### Fixed

- Portuguese spelling and diacritics in the README.

[Unreleased]: https://github.com/brunomartinsmv/flashcards/compare/v1.1.0...HEAD
[1.0.0]: https://github.com/brunomartinsmv/flashcards/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/brunomartinsmv/flashcards/releases/tag/v0.1.0

[1.1.0]: https://github.com/brunomartinsmv/flashcards/compare/v1.0.0...v1.1.0
