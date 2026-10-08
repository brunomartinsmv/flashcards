# Meus flashcards

Este repositório reúne os flashcards que eu uso para estudar. Começou com idiomas e agora também recebe CPA e outros conteúdos que fizerem parte dos meus estudos.

Os cartões refletem minhas escolhas de assunto, a forma como prefiro perguntar e responder e a organização que uso no Anki. Qualquer pessoa pode aproveitar o material, adaptar os cartões e compartilhar suas versões, respeitando a licença e os créditos.

## Coleções

| Conteúdo | Material | Guia |
| --- | --- | --- |
| Italiano | 587 cartões de léxico, 450 frases e coleção básica anterior | [Italiano](flashcards/italian/README.md) |
| Espanhol | 600 cartões de léxico, 450 frases e lotes anteriores Basic e Cloze | [Espanhol](flashcards/spanish/README.md) |
| Inglês | 600 cartões de léxico, 450 frases e lotes anteriores Cloze | [Inglês](flashcards/english/README.md) |
| CPA | 317 notas da apostila em 27 temas e quatro coleções anteriores | [CPA](flashcards/cpa/README.md) |
| Consolidados antigos | Lotes anteriores reunidos por idioma e modelo | [Consolidados](flashcards/consolidados/README.md) |

Esses números descrevem os arquivos distribuídos. As versões por tema e os arquivos completos repetem a mesma coleção; não devem ser somados nem importados juntos.

## Como importar no Anki

1. Escolha uma coleção e leia o README da pasta.
2. Importe o arquivo completo ou os arquivos por tema. Use apenas uma dessas opções.
3. Confira o separador, o tipo de nota e o mapeamento dos campos na prévia do Anki.

CSV, TSV e TXT são formatos de texto. Os cabeçalhos de cada arquivo indicam o separador, o uso de HTML, as tags e, quando presente, o deck de destino. Basic usa pergunta e resposta. Cloze usa lacunas como `{{c1::palavra}}` dentro de uma frase.

Nos cartões novos de idiomas, a frente fica no idioma estudado e o verso em português. O destino fica em `idioms::italian`, `idioms::spanish` ou `idioms::english`, com subdecks por coleção, nível e tema. CPA usa `CPA::<número e tema>`. A coluna especial Deck cria os subdecks para cartões novos. Atualizações de notas existentes preservam o deck atual no Anki.

## Uso de IA e autoria

Usei IA para ajudar a gerar, traduzir e organizar os flashcards, seguindo as instruções e o formato que eu escolhi. A seleção dos assuntos, a direção dos cartões e a estrutura dos decks seguem minha visão pessoal de estudo. A IA participa como ferramenta de produção; a coleção registra minhas escolhas editoriais e autorais.

Isso não significa que cada cartão tenha passado por revisão manual individual. Podem existir erros ou traduções que precisem de contexto. Confira o material durante o estudo e sugira correções por issue ou pull request. As regras de CPA devem ser lidas junto da edição da fonte indicada no verso.

## Organização e fontes

Salve os arquivos importáveis diretamente em `flashcards/<conteúdo>/`. Use número e tema no nome quando houver uma ordem de estudo. Subpastas guardam scripts, índices e documentação de apoio.

Livros e apostilas ficam apenas no computador. O `.gitignore` exclui `livros/`, `books/`, `apostilas/`, formatos de livros e PDFs, além da extração textual da apostila CPA e de relatórios pessoais do Anki. Publique referências bibliográficas e perguntas próprias, sem distribuir o texto integral das fontes. Um arquivo já rastreado pelo Git não passa a ser ignorado automaticamente.

Os scripts e instruções de geração ficam em [scripts/](scripts/README.md) e [skills/](skills/README.md). O [CONTEXT.md](CONTEXT.md) descreve as decisões atuais; os [ADRs](docs/adr/README.md) e o [arquivo histórico](archive/README.md) preservam o fluxo anterior de idiomas.

## Licença e créditos

Copyright © 2026 Bruno Martins ([brunomartinsmv](https://github.com/brunomartinsmv)). Os novos flashcards desta release e a documentação autoral nova estão sob [Creative Commons Attribution 4.0 International, CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). A licença permite copiar, adaptar e compartilhar, inclusive comercialmente, com atribuição, link da licença e indicação das alterações.

Exemplo de crédito:

> Flashcards de Bruno Martins, https://github.com/brunomartinsmv/flashcards, CC BY 4.0. Adaptado por [seu nome]; alterações: [descrição].

Os scripts e os materiais anteriores mantêm a licença Apache 2.0 já existente, salvo indicação própria. Créditos e licenças de terceiros continuam válidos e não são substituídos pela licença da coleção. A licença só alcança os direitos que o autor pode conceder. Consulte [LICENSE-CONTENT.md](LICENSE-CONTENT.md), [LICENSE](LICENSE) e [NOTICE](NOTICE).

## Histórico

As mudanças de cada versão ficam no [CHANGELOG.md](CHANGELOG.md), no formato [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
