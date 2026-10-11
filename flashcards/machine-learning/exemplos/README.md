# Exemplos executáveis

Todos os dados são sintéticos. Os valores e grupos têm nomes de cenários reais apenas para facilitar o aprendizado.

| Experiência | O que configurar | O que observar |
| --- | --- | --- |
| Imóveis | `Ridge(alpha=1)` e escala no pipeline | MAE em reais contra previsão da média |
| Cancelamento | Grade de `C` na logística, quatro folds estratificados | Precision, recall e F1 da classe positiva no teste reservado |
| Clientes | `n_clusters=3`, `n_init=10` e padronização | Centroides, silhouette e comparação com rótulos sintéticos por ARI |
| Redução | `PCA(n_components=0.95, svd_solver='full')` | Quantas componentes retêm 95% da variância e F1 com e sem PCA |
| Série temporal | Grade de `alpha` e `TimeSeriesSplit` | Treino em 150 dias e teste nos 30 finais, com baseline do último valor |
| Reforço | `alpha=0.3`, `gamma=0.9`, `epsilon=0.2` | Política que caminha pelos estados 0 → 1 → 2 → 3 → 4 |

Na classificação, os outros modelos têm configurações ilustrativas fixas. Só a logística recebe busca por validação cruzada. A MLP usa `max_iter=1500`, pois o limite inicial de 500 produziu um aviso de convergência. Essa comparação demonstra interfaces e métricas; não é uma competição com orçamento igual para determinar o melhor algoritmo. Não ajuste modelos repetidamente olhando os resultados do teste.

O agrupamento é descritivo e usa todos os clientes sintéticos. Os rótulos de geração servem apenas para uma avaliação didática. Os nomes numéricos dos clusters não têm significado fixo. Na redução, PCA e a escala são ajustados apenas no treino, dentro do pipeline.

No reforço, há cinco estados em uma linha. Ação 0 move para a esquerda e ação 1 para a direita. O estado 4 é terminal, com recompensa 1; os demais passos recebem -0,01. As fronteiras mantêm o agente na linha. O exemplo não implementa um robô físico ou o labirinto da figura.

## Execução

Na raiz do repositório, execute o script com um Python que tenha NumPy e scikit-learn. Para criar um ambiente separado, se necessário:

```sh
python3 -m venv /tmp/flashcards-ml-venv
/tmp/flashcards-ml-venv/bin/python -m pip install -r flashcards/machine-learning/exemplos/requirements.txt
/tmp/flashcards-ml-venv/bin/python flashcards/machine-learning/exemplos/exemplos.py
```

O script grava `resultados.json` ao lado do código. As versões registradas no arquivo são as usadas na execução entregue. Pode haver diferenças numéricas entre ambientes. Um aviso de convergência exige revisar o ajuste; aumentar `max_iter` não garante que o modelo ficou adequado.

## Cálculos de estatística e métricas

Execute `python3 flashcards/machine-learning/exemplos/metricas.py` na raiz para conferir os 101 exercícios numéricos do complemento. O script compara resultados de NumPy, SciPy e scikit-learn, ou implementações das fórmulas declaradas, com os valores esperados registrados nos cartões. Divergências interrompem a execução. `resultados_metricas.json` guarda os valores calculados e as versões.

Vários exemplos usam a mesma matriz de confusão para permitir comparação entre denominadores. Outros usam conjuntos pequenos específicos, como dois erros de regressão ou uma lista de relevância. Não são estimativas de desempenho em dados reais. Medidas de resumo fornecidas no enunciado, como a e b do silhouette ou B e W de Calinski-Harabasz, são usadas diretamente nas fórmulas; não representam um dataset bruto implícito.
