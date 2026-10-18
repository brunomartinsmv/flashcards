# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Páginas da Wikipedia sobre repetição espaçada e memória convertidas para `archive/spaced-repetition/docs/wikipedia.md`.

### Fixed

- CPA: páginas citadas corrigidas em 31 cartões cuja referência apontava para outro assunto, como blockchain, subadquirente, sandbox, come-cotas, fundos, previdência, PIB e risco climático.
- CPA: quatro cartões sem base na apostila foram substituídos por conteúdo da própria apostila. IPCA × INPC virou IPCA × IGP-M, PIB nominal × real virou valor agregado, análise fundamentalista × técnica virou aluguel de ações e blockchain permissionada virou DeFi. Risco de concentração agora reflete o que a apostila diz sobre fundos de ações.
- CPA: respostas vagas passam a trazer os dados da apostila, como o limite de R$ 20.000,00 em vendas mensais de ações, a garantia do FGCoop, as datas e alíquotas do come-cotas e a definição de subadquirente. O cartão sobre cliente que insiste em operação inadequada cita a Resolução CVM 30, art. 7º.
- CPA: cinco cartões complementam a apostila onde ela simplifica. No aluguel de ações, a titularidade passa ao tomador, e o doador recebe reembolsos equivalentes aos proventos (B3). O subcredenciador participa do arranjo, mas não é credor do emissor (Banco Central). O FGCoop não cobre LCD e não tem o teto global do FGC (Banco Central). O PIB pela ótica da produção soma valor adicionado e impostos líquidos sobre produtos (IBGE). No exemplo de empréstimo DeFi, a devolução não é garantida.
- Machine learning: vírgulas faltantes em cinco frentes; respostas mais claras nos exercícios de k-NN ponderado e da árvore com chuva de 5 mm.
- Idiomas: `a nombre de esta persona` corrigido para `a este nombre`; conexão de voo em espanhol e italiano (`conexión`, `coincidenza`); `llegó hasta` substituído por `solo llegó`; frente inglesa do despertador mais natural (`Today I'm waking up before seven.`); `pepper` e `pan` especificados como `bell pepper` e `frying pan`.

### Migração

O Anki identifica notas Basic pela frente. Ao reimportar com "atualizar notas existentes", as frentes abaixo entram como notas novas, e a versão antiga continua no deck. Para manter o histórico de revisão, antes de importar procure a frente antiga no navegador do Anki e troque-a pela nova. Se preferir, importe e depois exclua a nota antiga.

| Deck | Frente antiga | Frente nova |
| --- | --- | --- |
| `CPA::03 Riscos, mitigação e autorregulação` | Como a apostila define risco de concentração? | O que a apostila diz sobre risco de concentração em fundos de ações? |
| `CPA::07 PIB, inflação, Selic e políticas econômicas` | Como se distinguem PIB nominal e PIB real? | Uma indústria compra R$ 1.000 de matéria-prima e vende o produto por R$ 1.800. Quanto ela acrescenta ao PIB? |
| `CPA::07 PIB, inflação, Selic e políticas econômicas` | Qual é a diferença entre IPCA e INPC segundo a apostila? | Como a apostila diferencia IPCA e IGP-M? |
| `CPA::12 Oferta pública, governança e ações` | Como diferenciar análise fundamentalista de análise técnica? | Como funciona o aluguel de ações e quem recebe os proventos durante o contrato? |
| `CPA::32 Blockchain, criptoativos, tokenização e smart contracts` | Como diferenciar blockchain permissionada de pública? | Como as finanças descentralizadas (DeFi) diferem do sistema financeiro tradicional? |
| `idioms::english::Frases::01 Básico::01 Rotina e organização` | I wake up before seven today. | Today I'm waking up before seven. |
| `idioms::english::Léxico::Básico::05 Cozinha e utensílios` | pan | frying pan |
| `idioms::english::Léxico::Básico::07 Frutas e vegetais` | pepper | bell pepper |
| `idioms::italian::Frases::02 Intermediário::02 Serviços compras e viagens` | Dato che il volo è stato cancellato, abbiamo riprenotato il primo collegamento disponibile. | Dato che il volo è stato cancellato, abbiamo riprenotato la prima coincidenza disponibile. |
| `Machine learning::17 Métricas de classificação binária` | Como ler TP TN FP e FN em uma matriz de confusão? | Como ler TP, TN, FP e FN em uma matriz de confusão? |
| `Machine learning::06 Árvores florestas e boosting` | XGBoost LightGBM e CatBoost são o mesmo algoritmo? | XGBoost, LightGBM e CatBoost são o mesmo algoritmo? |
| `Machine learning::12 Exemplos práticos e decisões de configuração` | No exemplo de clientes, os números 0 1 e 2 dos clusters representam classes reais? | No exemplo de clientes, os números 0, 1 e 2 dos clusters representam classes reais? |
| `Machine learning::24 Séries temporais modelos e diagnóstico` | Como distinguir tendência sazonalidade e ciclo? | Como distinguir tendência, sazonalidade e ciclo? |
| `Machine learning::24 Séries temporais modelos e diagnóstico` | O que p d e q configuram em ARIMA(p,d,q)? | O que p, d e q configuram em ARIMA(p,d,q)? |
| `idioms::spanish::Frases::01 Básico::02 Serviços compras e viagens` | Mi reserva está a nombre de esta persona. | Mi reserva está a este nombre. |
| `idioms::spanish::Frases::02 Intermediário::02 Serviços compras e viagens` | Como cancelaron el vuelo, cambiamos la reserva al primer enlace disponible. | Como cancelaron el vuelo, cambiamos la reserva a la primera conexión disponible. |
| `idioms::spanish::Frases::03 Avançado::01 Rotina e organização` | Habría preferido encargarme de esto antes, pero la información llegó hasta el final de la jornada. | Habría preferido encargarme de esto antes, pero la información solo llegó al final de la jornada. |

## [2.0.0] - 2026-10-09

Versão major: o repositório passou de workshop de idiomas para biblioteca pessoal de flashcards, com licenciamento novo (CC BY 4.0 nos cartões e na documentação autoral desta versão; Apache 2.0 nos scripts e materiais anteriores).

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

[Unreleased]: https://github.com/brunomartinsmv/flashcards/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/brunomartinsmv/flashcards/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/brunomartinsmv/flashcards/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/brunomartinsmv/flashcards/releases/tag/v0.1.0
