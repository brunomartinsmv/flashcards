# Álgebra linear

120 cartões em português, em seis estudos de 20 cartões. Esta é a primeira etapa da coleção. A sequência cobre vetores, matrizes, sistemas lineares, espaços vetoriais, projeções, mínimos quadrados, autovalores e SVD. Os exemplos usam contas pequenas para resolver à mão.

Consulte a [ordem de estudo](INDICE.md) e o [plano de expansão](documentacao/PLANO_DE_ESTUDO.md). Os últimos módulos introduzem conceitos usados em regressão e PCA. Pressupõem domínio dos primeiros módulos; não substituem um curso completo com demonstrações e listas de exercícios.

## Importação no Anki

Extraia [Álgebra linear - Anki.zip](<Álgebra linear - Anki.zip>) e importe [00 - Álgebra linear completo.tsv](<00 - Álgebra linear completo.tsv>). Escolha um tipo Basic, ou Básico, que gere um único cartão de pergunta e resposta. Mapeie Frente e Verso para os dois campos, Tags para a coluna especial Tags e Deck para a coluna especial Deck. Confira separador Tab e HTML na prévia. Os cabeçalhos declaram essas opções, e os destinos ficam em `Álgebra linear::<número e tema>`.

Como alternativa, importe os seis CSVs numerados com separador vírgula. Eles contêm os mesmos cartões do TSV. Escolha uma dessas opções para evitar duplicação. Não há imagens para copiar nesta coleção. O ZIP reúne arquivos de texto e apoio; não é um `.apkg`.

Abra [ESTUDAR.html](ESTUDAR.html) no navegador para buscar perguntas e revelar respostas. Tente resolver cada exercício antes de consultar o verso.

## Conferência e manutenção

[exemplos/algebra.py](exemplos/algebra.py) recalcula 33 exercícios com NumPy, incluindo projeções, sistemas, mínimos quadrados e SVD. [Resultados](exemplos/resultados.json) registram os valores e a versão usada. Instale, em um ambiente separado se necessário, a dependência de [exemplos/requirements.txt](exemplos/requirements.txt).

```sh
python3 flashcards/algebra-linear/exemplos/algebra.py
python3 flashcards/algebra-linear/scripts/gerar_colecao.py
python3 flashcards/algebra-linear/scripts/validar_colecao.py
```

A [fonte editorial](fontes/cartoes.json) guarda as perguntas e respostas editáveis. Depois de alterar cartões ou documentação, gere os arquivos e execute o teste Anki descrito em [scripts/README.md](../../scripts/README.md) antes de validar. Se o relatório de validação mudar, gere o ZIP novamente para incluir o relatório atualizado e valide uma segunda vez.

A validação confere os cálculos, a correspondência entre JSON, CSV e TSV, as frentes duplicadas e a integridade do ZIP. O motor Anki 2.1.66 importou esta coleção junto da de ML em bancos temporários, conferindo Frente, Verso, Tags, Deck e reimportação sem duplicatas. O [relatório de importação](documentacao/importacao_anki.json) registra hashes dos arquivos. Não houve teste pela interface gráfica nem alteração do perfil pessoal. O [relatório](documentacao/validacao.json) registra esses limites.

As [referências](fontes/REFERENCIAS.md) incluem o curso 18.06 do MIT e a documentação do NumPy. Perguntas e exercícios foram escritos para esta coleção, sem reproduzir o texto das fontes.

Conteúdo autoral preparado com auxílio de IA sob as instruções de Bruno Martins, seguindo [CC BY 4.0](../../LICENSE-CONTENT.md). Scripts seguem a [licença do repositório](../../LICENSE). As fontes mantêm seus próprios créditos.
