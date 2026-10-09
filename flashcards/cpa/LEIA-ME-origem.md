# Decks de CPA para Anki

Preparados em 06/10/2026 a partir do texto anexado pelo usuário, do programa detalhado da CPA vigente a partir de 2026 e de fontes oficiais. Questões autorais de estudo, sem reprodução de questões oficiais de prova.

| Arquivo | Cartões | Situações contextualizadas |
| --- | ---: | ---: |
| 01_sfn_orgaos.txt | 45 | 22 |
| 02_participantes_spb_pagamentos.txt | 70 | 18 |

Cada cartão tem pergunta na frente, resposta com explicação no verso e tags de tema e tipo. As questões contextualizadas aparecem no final de cada arquivo. O Anki pode mudar a ordem de apresentação conforme as opções de estudo.

## Importação

1. No Anki para computador, abra Arquivo > Importar e selecione um dos arquivos .txt.
2. Escolha o tipo de nota Básico, que gera um cartão por nota. Evite o tipo que também cria cartão invertido.
3. Confira o separador Tabulação e o mapeamento: coluna 1 para Frente, coluna 2 para Verso, coluna 3 para Tags.
4. Mantenha a interpretação de HTML ativada para exibir links e quebras de linha no verso.
5. Confira o baralho de destino. Os cabeçalhos sugerem CPA::01 SFN e órgãos e CPA::02 Participantes, SPB e pagamentos. Se sua versão não reconhecer o cabeçalho de baralho, crie e selecione esses baralhos manualmente.
6. Confira a prévia e importe. Repita com o segundo arquivo.

Use as tags cpa::caso para selecionar situações contextualizadas, cpa::conceito para conceitos e cpa::comparacao para distinções.

## Fontes e escopo

Os versos trazem links para consulta. O escopo de participantes segue os itens 1.1.3.1.1 a 1.1.3.1.16 do programa da CPA. Foram acrescentadas as infraestruturas e funções de pagamento solicitadas pelo usuário.

- [Programa detalhado da CPA](https://www.anbima.com.br/data/files/6A/52/6F/A1/BED73910B07B2739B82BA2A8/Programa-Detalhado-CPA-ANBIMA.pdf)
- [Estrutura do SFN, BCB](https://www.bcb.gov.br/estabilidadefinanceira/sfn)
- [SPB, BCB](https://www.bcb.gov.br/estabilidadefinanceira/spb)
- [Instituições de pagamento, BCB](https://www.bcb.gov.br/estabilidadefinanceira/instituicaopagamento)
- [Sistemas autorizados e seus operadores, BCB](https://www.bcb.gov.br/estabilidadefinanceira/sistemasautorizados_spb)

A classificação normativa/supervisora é didática. Supervisores também editam normas. As competências podem se sobrepor conforme a atividade. A condição de instituição de pagamento não autoriza atividades bancárias e não significa integração ao SFN. VGBL é seguro de pessoas com cobertura por sobrevivência, embora seja estudado junto da previdência aberta.

## Verificação

Na preparação original, os arquivos 01 e 02 foram reabertos como UTF-8 e analisados como dados tabulados: 115 cartões, três campos preenchidos por nota, frentes únicas e contagem de casos. O relatório `validacao.json` e o gerador `criar_decks.py` usados naquela preparação não estão disponíveis neste repositório. Esta seção registra a verificação original, sem oferecer um comando de regeneração desses dois decks.

Os scripts em [apostila/scripts/](apostila/scripts/README.md) geram e validam apenas a coleção posterior baseada na apostila. Eles não regeneram os TXT 01 e 02. Para importar os TXT, confira os campos na prévia do Anki conforme as instruções acima.
