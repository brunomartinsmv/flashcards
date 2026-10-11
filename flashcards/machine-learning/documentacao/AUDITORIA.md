# Auditoria da primeira edição

Revisão em 10/10/2026, antes da primeira importação do usuário. Foram lidas as frentes e os versos dos 539 cartões de ML e dos 120 de álgebra linear, conferidas as quatro figuras e executados os exemplos. Isso não elimina a possibilidade de erros posteriores nem equivale a uma formação universitária.

## Correções

- Os CSVs declaravam tanto `#deck` quanto `#deck column`. Quando o subdeck já existia, o motor Anki podia interpretar o destino como um deck fixo. Os arquivos agora usam apenas a coluna especial Deck.
- Os validadores verificavam apenas os arquivos presentes no ZIP. Agora exigem o conjunto completo previsto pelo gerador e rejeitam entradas repetidas.
- Onze contas dos primeiros módulos de ML passaram a ter verificação numérica, além das 101 de estatística e métricas e das 24 do núcleo novo. Álgebra linear mantém 33 verificações.
- F1 usa a expressão por contagens para tratar casos em que precision e recall são zero. O cartão declara o caso sem denominador.
- As explicações do TCL, das distribuições contínuas e da normalização bayesiana receberam condições mais precisas. A razão observada de alertas falsos foi distinguida da FDR da inferência múltipla.
- Álgebra linear distingue coordenadas no subespaço de coeficientes de projeção, explicita a orientação dos dados no PCA e evita ambiguidade decimal na inversa.
- A calculadora rejeita campos vazios e contagens fora da representação inteira segura do JavaScript.

## Evidências

Os arquivos `resultados_fundamentos.json`, `resultados_metricas.json`, `resultados_nucleo.json` e os resultados de álgebra linear registram 169 verificações numéricas. As seis experiências sintéticas também foram executadas. Os exercícios com figuras foram conferidos visualmente; suas imagens não representam os dados exatos dos scripts.

O motor Anki 2.1.66 importou os dois TSVs completos em uma coleção temporária. Outra coleção recebeu os 32 CSVs. Em ambas, foram conferidas 659 notas Basic, cada uma com um cartão, frente, verso, tags e subdeck corretos. A reimportação manteve a contagem, inclusive após aplicar os complementos ao TSV completo. A mídia não apresentou arquivos ausentes ou não usados. O relatório `importacao_anki.json` identifica os arquivos usados por SHA-256.

O teste reproduz o mapeamento manual de Frente e Verso para as colunas 1 e 2. Os rótulos em português não garantem que o diálogo escolha essas colunas automaticamente. Não houve teste pela interface gráfica nem acesso ao perfil pessoal. O ambiente local usou Python 3.9.6; a versão do motor de teste é anterior à versão 26.5 do aplicativo instalado.

A suíte de regressão verifica pacotes válidos e três falhas deliberadas em cópias temporárias: arquivo removido do ZIP, resposta alterada e cálculo incorreto. O workflow `Study decks` repete os cálculos e a importação no Linux sem reescrever os artefatos distribuídos no checkout.

As páginas de estudo foram conferidas no navegador: busca, contagem e abertura das respostas. As sete referências de imagem carregaram na página de ML. A página de álgebra linear e a calculadora ficaram sem rolagem horizontal em viewport de 390 pixels. Na calculadora, a matriz padrão retornou acurácia de 85% e F1 de 80%; campos vazios, negativos e inteiros fora da faixa segura foram rejeitados. Com todas as contagens zero, a acurácia apareceu como indefinida.

## Fontes e escopo

As referências estão em `fontes/REFERENCIAS.md`, `fontes/REFERENCIAS_NUCLEO.md` e na coleção de álgebra linear. Fórmulas e condições foram comparadas com o manual do Anki, a documentação de scikit-learn, SciPy, NumPy e statsmodels, o curso 18.06 do MIT, Forecasting: Principles and Practice e Bayes Rules!. Os versos apontam para as fontes específicas quando disponíveis.

A coleção é introdutória e inclui apresentações conceituais de técnicas que ainda não têm ajustes executáveis próprios, como MANOVA, CCA, ARIMA e MCMC. Demonstrações, projetos com dados reais e diagnóstico de modelos ficam para expansões futuras.

## Correções após a revisão do PR

Em 11/10/2026, a revisão do Codex apontou dois casos de expansão. Os geradores agora montam a lista de CSVs a partir dos módulos atuais e rejeitam arquivos numerados que ficaram fora da fonte editorial, preservando-os. O teste de importação dos CSVs também usa os TSVs completos como referência, para não aceitar uma coleção maior só porque todos os CSVs foram importados.

A página de ML encaminha qualquer imagem para `media/`, independentemente do prefixo no nome. O validador confere essas referências e decodifica entidades HTML nos nomes dos arquivos. Os testes incluem um nome com espaços, acento e `&`.

A suíte passou de quatro para oito testes. Os casos de CSV obsoleto e referência de imagem foram reproduzidos no commit anterior e passam após a correção. O conteúdo dos cartões e as imagens existentes permaneceram iguais.
