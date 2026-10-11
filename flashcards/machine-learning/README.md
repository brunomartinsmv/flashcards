# Machine learning

539 cartões em português, em 26 estudos do básico ao avançado. Cada nota Basic contém uma pergunta, uma resposta, tags e o subdeck de destino. Há 141 exercícios e quatro figuras originais geradas com a skill imagegen, usadas em sete cartões.

A [ordem de estudo](INDICE.md) começa em fundamentos e preparação de dados, passa por validação, regressões, vizinhos, SVM, Naive Bayes, árvores, ensembles e agrupamento, e termina em ajuste, redes neurais, reforço e interpretação. Os hiperparâmetros apresentados são pontos de partida para validação, não receitas universais.

Os estudos 13 a 21 acrescentam estatística descritiva, probabilidade, distribuições, Bayes, inferência, intervalos e comparação de modelos, além de regressão, classificação, calibração, agrupamento, ranking, previsão temporal e avaliação de reforço. O [inventário de métricas](documentacao/COBERTURA_METRICAS.md) lista 83 métricas, perdas e indicadores. Cada item tem definição, interpretação, fórmula ou regra de cálculo e exemplo numérico. O script de conferência verifica 101 exercícios, incluindo os de estatística.

Para começar sem base estatística, estude 01, depois 13 a 15, e retome 02 e 03. Consulte 16 a 18 ao estudar avaliação supervisionada, e 19 a 21 junto das técnicas correspondentes. A numeração original foi mantida para preservar os cartões já importados. Uma coleção de cartões apoia a revisão; o domínio do assunto também exige resolver problemas e trabalhar com dados.

Os estudos 22 a 26 acrescentam 100 cartões de probabilidade conjunta e condicionamento, inferência estatística, séries temporais, análise multivariada e estatística bayesiana. São módulos iniciais, com 24 exercícios numéricos conferidos. O [plano de estudo e expansão](documentacao/PLANO_DE_ESTUDO.md) liga esses temas à coleção separada de [álgebra linear](../algebra-linear/README.md).

## Importação no Anki

1. Extraia [Machine learning - Anki e imagens.zip](<Machine learning - Anki e imagens.zip>).
2. Copie os quatro arquivos PNG de `media/` diretamente para a pasta `collection.media` do perfil do Anki. Não copie a subpasta inteira. No macOS, ela normalmente fica em `~/Library/Application Support/Anki2/<perfil>/collection.media`.
3. Importe [00 - Machine learning completo.tsv](<00 - Machine learning completo.tsv>) com um tipo de nota Basic que tenha um único cartão de pergunta e resposta. Se o nome local for "Básico", escolha esse tipo. Use Frente → primeiro campo, Verso → segundo campo, Tags → coluna especial Tags e Deck → coluna especial Deck. Confira que Verso esteja mapeado; a seleção automática pode deixar esse campo sem coluna.
4. Confira na prévia o separador Tab e a opção de permitir HTML. Os cabeçalhos já declaram ambos, além das colunas especiais. Os subdecks novos ficam em `Machine learning::<número e tema>`.
5. Abra um cartão com imagem para conferir a mídia. A cópia e a importação precisam ser feitas no Anki Desktop; depois, sincronize para o celular.

Para a primeira importação, use o TSV completo de 539 cartões e ignore os complementos. Como alternativa, importe os 26 CSVs numerados, com separador vírgula e o mesmo mapeamento. Eles contêm as mesmas notas do TSV; escolha uma opção.

Os dois complementos ficam disponíveis para atualizações futuras. Quem tem apenas os 189 iniciais pode importar os complementos de 250 e 100 cartões. Quem tem os 439 anteriores pode usar somente o de 100. O ZIP é um pacote de texto e imagens, não um `.apkg`. Atualizações de notas existentes podem preservar o deck em que já estavam.

O manual oficial explica [campos especiais, HTML e imagens na importação](https://docs.ankiweb.net/manual/importing/text-files). O teste de importação usou o motor Anki 2.1.66 em bancos temporários. Conferiu Frente, Verso, Tags, Deck, mídia e reimportação sem duplicatas, tanto para TSV quanto para CSV. O [relatório de importação](documentacao/importacao_anki.json) identifica os arquivos por SHA-256. Não houve teste pela interface gráfica nem alteração do perfil pessoal.

## Estudo e prática

Abra [ESTUDAR.html](ESTUDAR.html) no navegador para consultar cartões, buscar temas e revelar respostas. As imagens usam caminhos locais e precisam ficar ao lado da página na pasta `media/`.

A [calculadora de classificação](documentacao/calculadora_metricas.html) permite alterar TP, FN, FP e TN e observar as mudanças nas métricas e nos denominadores.

[exemplos/metricas.py](exemplos/metricas.py) recalcula os 101 exemplos numéricos. [Resultados dos cálculos](exemplos/resultados_metricas.json) registram valores e versões. Há métricas com mais de uma convenção, como sMAPE, ECE, NDCG e CRPS; os cartões declaram a variante usada. No exemplo de CRPS, a distribuição é degenerada, e o cálculo se reduz ao erro absoluto.

[exemplos/exemplos.py](exemplos/exemplos.py) executa seis experiências sem baixar dados. Usa dados sintéticos, com semente 42, para prever preços, detectar cancelamento, agrupar clientes, reduzir dimensionalidade, validar uma série temporal e aprender uma política de Q-learning. No exemplo de classificação, nove modelos são comparados, incluindo a baseline. Os desenhos são ilustrações conceituais; não reproduzem exatamente os dados do script.

```sh
python3 flashcards/machine-learning/exemplos/exemplos.py
python3 flashcards/machine-learning/exemplos/metricas.py
python3 flashcards/machine-learning/exemplos/fundamentos.py
python3 flashcards/machine-learning/exemplos/nucleo_estatistico.py
```

Se faltarem dependências, crie um ambiente separado e instale as versões em [exemplos/requirements.txt](exemplos/requirements.txt). [Resultados da execução](exemplos/resultados.json) registram métricas, versões e semente. Leia [o guia dos exemplos](exemplos/README.md) antes de interpretar os números.

[exemplos/nucleo_estatistico.py](exemplos/nucleo_estatistico.py) confere os 24 exercícios novos de probabilidade, inferência, previsão, covariância e atualização Beta-Bernoulli. [Resultados](exemplos/resultados_nucleo.json) registram esses cálculos separadamente dos 101 exemplos anteriores.

[exemplos/fundamentos.py](exemplos/fundamentos.py) verifica outras 11 contas dos primeiros módulos. O total é de 136 exercícios numéricos conferidos. Os cinco exercícios restantes classificados como exercício exigem ler as figuras.

A [auditoria da primeira edição](documentacao/AUDITORIA.md) registra correções, testes e limites.

## Fontes e manutenção

[fontes/cartoes.json](fontes/cartoes.json) guarda os 189 cartões iniciais, e [fontes/estatistica_metricas.json](fontes/estatistica_metricas.json) guarda o complemento. [fontes/nucleo_estatistico.json](fontes/nucleo_estatistico.json) guarda os 100 cartões dos estudos 22 a 26. Os três arquivos são fontes editoriais editáveis. Os versos apontam para documentação técnica ou para o script autoral nos casos práticos. [Referências](fontes/REFERENCIAS.md) e [prompts das imagens](fontes/prompts_imagens.json) documentam a origem. A geração usou o modo integrado da skill imagegen; os PNGs finais estão em [media/](media/).

```sh
python3 flashcards/machine-learning/scripts/gerar_colecao.py
python3 flashcards/machine-learning/scripts/validar_colecao.py
```

Ao alterar exemplos, execute-os antes de gerar o pacote. Depois de gerar CSV e TSV, execute o teste Anki indicado em [scripts/README.md](../../scripts/README.md). A conferência exige que os hashes desse teste correspondam aos arquivos atuais. Ao alterar cartões ou documentação, regenere os arquivos e o ZIP. Se o relatório de validação mudar, gere o ZIP novamente e valide uma segunda vez para incluir o relatório atualizado. [documentacao/validacao.json](documentacao/validacao.json) registra a conferência estrutural mais recente.

Redes convolucionais, recorrentes, Transformers e DQN recebem explicações conceituais. Os exemplos executáveis de redes usam MLP, e o de reforço usa Q-learning tabular. A coleção não esgota todas as técnicas ou todas as métricas possíveis em machine learning. As métricas específicas de outros domínios podem exigir complementos. Métricas sintéticas não comprovam desempenho em dados reais.

Conteúdo autoral preparado com auxílio de IA sob as instruções de Bruno Martins, seguindo [CC BY 4.0](../../LICENSE-CONTENT.md). Scripts seguem a [licença do repositório](../../LICENSE). A documentação consultada e os direitos de terceiros mantêm seus próprios créditos.
