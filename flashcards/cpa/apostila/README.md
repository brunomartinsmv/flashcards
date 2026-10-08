# Coleção CPA baseada na apostila

Coleção de cartões Basic para as tarefas CPA03 a CPA33, criada somente a partir de `flashcards/cpa/fontes/apostila_cpa.txt`, extraído de `livros/Apostila_CPA.pdf` (edição janeiro/2026). As perguntas foram contextualizadas e parafraseadas. Cada verso traz a página impressa e a página PDF usada como fonte.

O PDF e sua extração são fontes locais privadas e não são distribuídos. Para executar os scripts, prepare a extração conforme o [guia das fontes](../fontes/README.md). Para importar os cartões, ela não é necessária.

## Importação

Escolha uma opção de importação:

- `../`: 27 CSVs com número e título do estudo no nome, em ordem do planejamento. Exemplo: `05 - Sistemas Price e SAC.csv`.
- `../cpa_apostila_completo.tsv`: 317 notas únicas em um arquivo.
- `../cpa_XX.tsv`: 27 arquivos separados por tópico, um por módulo de conteúdo criado.

Escolha apenas uma dessas versões para importar, pois elas contêm as mesmas notas. Os arquivos seguem UTF-8 e incluem cabeçalhos de importação Anki para separador, HTML, tags e deck de destino. Os CSVs usam vírgula; os TSVs usam tabulação.

As quatro colunas são Frente, Verso, Tags e Deck. `#deck column:4` informa ao Anki que a última coluna contém o destino de cada cartão, por exemplo `CPA::05 Sistemas Price e SAC`. Ao importar novos cartões, os subdecks são criados dentro de CPA. Os arquivos por assunto também incluem `#deck:CPA::...`, como nos TXT originais. O consolidado distribui os cartões pelos mesmos 27 subdecks.

Cada nota recebe `cpa::apostila`, a tag da tarefa (`cpa::03`, por exemplo) e uma ou mais tags `tema::*`. As tags servem para filtrar os cartões nas revisões. O arquivo `inventario_subtopicos.csv` relaciona cada tag temática a cartões e páginas da apostila.

## Cobertura das tarefas

`cobertura.csv` lista as 37 tarefas do plano original, preservando título e descrição, e registra o deck, a seleção por tags ou a dependência de material pessoal. As revisões CPA08, CPA19, CPA20, CPA22, CPA30 e CPA39 reutilizam cartões existentes. Elas não ganham cartões artificiais.

As tarefas CPA34, CPA36 e CPA38 pedem simulados completos. A coleção não cria simulados nem substitui questões em condições de prova. CPA35 e CPA37 dependem das respostas erradas ou marcadas com dúvida nos simulados pessoais, que não foram fornecidas. Para corrigir essas tarefas, associe cada erro ao tema e à página da apostila, revise o deck correspondente e crie um cartão próprio que explique o erro. CPA39 pode selecionar todas as tags temáticas e os cartões pessoais de erro.

## Regras e cálculos

Valores tributários, limites e outras regras regulatórias aparecem identificados como "Segundo a apostila (edição janeiro/2026)". A coleção não verifica se esses dados continuam vigentes. Use a edição indicada como material de estudo, não como confirmação de regra atual.

Taxas e prazos foram escritos com unidade explícita. Exemplos numéricos derivados de fórmulas da apostila foram recalculados. Quando uma fórmula ou figura não apareceu na extração textual, a página do PDF foi renderizada para conferência antes de incluir o cartão.

## Arquivos

- `../cpa_apostila_completo.tsv`: coleção consolidada.
- `../cpa_XX.tsv`: decks temáticos separados.
- `cobertura.csv`: mapeamento de todas as tarefas CPA03 a CPA39.
- `inventario_subtopicos.csv`: índice de tags, cartões e referências de página.
- `scripts/gerar_colecao.py`: fonte estruturada dos cartões e gerador dos TSVs/índices.
- `scripts/validar_colecao.py`: verifica cabeçalhos e campos, frentes únicas, tags, referências e rodapés de página, cobertura das 37 tarefas e cálculos selecionados.

## Validação executada

Execute, a partir da raiz do repositório:

```sh
python3 flashcards/cpa/apostila/scripts/gerar_colecao.py
python3 flashcards/cpa/apostila/scripts/validar_colecao.py
```

A validação estrutural não comprova importação dentro do aplicativo Anki. Na tela de importação, confira Frente, Verso, Tags e a coluna especial Deck. Ao atualizar notas já existentes, o Anki preserva o deck atual delas; o destino indicado no arquivo é aplicado aos cartões novos.
