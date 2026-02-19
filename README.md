# Flashcards prontos para o Anki

Transforme notas em flashcards de qualidade, com base em ciência cognitiva. Este repo existe para reduzir o trabalho chato de criar bons cards e acelerar sua aprendizagem com repetição espaçada.

## Por que funciona (versão técnica)

A memória humana sofre decaimento ao longo do tempo quando não há revisão. A curva do esquecimento, descrita por Hermann Ebbinghaus, caracteriza essa perda de informação e motivou a ideia de revisar em momentos estratégicos.

Dois efeitos robustos sustentam a repetição espaçada:

### 1) Spacing effect (prática distribuída)

Revisões espaçadas superam revisões concentradas (massed practice). A meta-análise clássica de Cepeda et al. (2006) sintetiza centenas de estudos e mostra que a distribuição temporal melhora a retenção. Um resultado central é que o intervalo ideal entre revisões (ISI) aumenta conforme o intervalo até o teste final aumenta. Ou seja, quanto maior o prazo até a avaliação, mais espaçado deve ser o estudo.

### 2) Testing effect (recuperação ativa)

Testar-se (recuperar ativamente) melhora a retenção de longo prazo mais do que apenas reler, mesmo quando a releitura aumenta a confiança imediata. Em estudos com atrasos de dias a semanas, testes anteriores produzem retenção superior em comparação à releitura repetida.

### 3) Otimização de intervalos

Estudos posteriores mapearam o espaçamento ao longo de semanas e meses, mostrando que existe um "ridgeline" temporal: intervalos muito curtos desperdiçam esforço, e intervalos muito longos deixam a informação se perder antes da revisão. O melhor intervalo depende do tempo até a prova, reforçando a ideia de espaçamento adaptativo.

![Curva do esquecimento](assets/ForgettingCurve.svg)

O método de Leitner operacionaliza esses efeitos com simplicidade: cards corretos avançam para caixas com intervalos maiores; cards errados voltam para revisões frequentes.

![Sistema de Leitner](assets/Leitner_system_alternative.svg)

### Implicações práticas para flashcards

- **Um card = um conceito**: facilita recuperação ativa.
- **Respostas curtas**: minimiza carga cognitiva e evita ambiguidades.
- **Tags**: permitem organizar revisões por tema e prioridade.
- **Revisão em ciclos**: aumenta o espaçamento conforme a lembrança estabiliza.

Referências principais:
- [Hermann Ebbinghaus e a curva do esquecimento (Britannica)](https://www.britannica.com/biography/Hermann-Ebbinghaus)
- [Meta-análise do spacing effect (Psychological Bulletin, 2006)](https://pubmed.ncbi.nlm.nih.gov/16719566/)
- [Testing effect: test-enhanced learning (Psychological Science, 2006)](https://pubmed.ncbi.nlm.nih.gov/16507066/)
- [Otimização de intervalos (Psychological Science, 2008)](https://pubmed.ncbi.nlm.nih.gov/19076480/)
- [Método de Leitner](https://en.wikipedia.org/wiki/Leitner_system)

## Evidências e limites

Spaced repetition é robusta, mas não é uma fórmula mágica. A meta-análise de prática distribuída mostra que o ganho depende do intervalo entre sessões e do tempo até o teste final: intervalos muito curtos ou muito longos reduzem a eficiência. Estudos posteriores mostram a mesma relação em prazos longos (semanas a meses), sugerindo que o espaçamento deve ser ajustado ao horizonte de retenção.

O testing effect também tem limites: recuperar ativamente pode parecer mais difícil e pode reduzir a confiança imediata, mesmo quando melhora a retenção no longo prazo. Isso implica que o usuário pode sentir que está \"indo pior\" no curto prazo, quando na verdade está aprendendo mais.

Na prática, flashcards são excelentes para fatos, definições, fórmulas e discriminações simples. Para habilidades complexas, eles ajudam na base conceitual, mas não substituem prática deliberada (resolver problemas, escrever, programar, etc.). Use flashcards como camada de memória, não como única estratégia.

## O problema real

Spaced repetition funciona, mas criar bons flashcards é difícil. Cards ruins geram revisões ineficientes: perguntas vagas, respostas longas e sem tags. Esse repo resolve isso com prompts que orientam a criação de cards claros, objetivos e prontos para o Anki.

## O que este repo oferece

- Prompts detalhados para gerar flashcards no formato TSV do Anki
- Prompt resumido para uso rápido (modo CLI)
- Prompt para uso direto em chat web (sem caminho de arquivo)
- Exemplo completo (entrada .md e saída .tsv)
- Materiais visuais para explicar o método

## Como usar

**Escolha seu modo**
- **CLI / arquivo local:** use `prompts/anki_prompt_completo.md` (ou `prompts/anki_prompt_resumido.md`) e informe o caminho do arquivo
- **Web / chat:** use `prompts/anki_prompt_web.md` e cole o conteúdo no chat ou anexe o arquivo

1. Prepare um arquivo de notas em `.md` ou `.txt`
2. Escolha o prompt em `prompts/`
3. Cole o prompt em um LLM
4. Siga o modo escolhido (caminho do arquivo ou conteúdo colado/anexado)
5. Gere o arquivo `.tsv` e importe no Anki

Prompts disponíveis:
- `prompts/anki_prompt_completo.md` (modo CLI)
- `prompts/anki_prompt_resumido.md` (modo CLI)
- `prompts/anki_prompt_web.md`

## Exemplo completo

Entrada (trecho):

```md
## Conta-corrente
A conta-corrente e o tipo de conta mais comum e a mais completa oferecida pelos bancos.

## Conta-salario
E de responsabilidade do empregador realizar a abertura desse tipo de conta.
```

Saída (trecho TSV):

```tsv
O que e conta-corrente?	E o tipo de conta mais comum e completa oferecida pelos bancos, aberta por qualquer pessoa para receber pagamentos, pagar contas, fazer transferencias, ter cartao de credito e cheque, e sacar dinheiro.	#conta-corrente #conceitos
Quem e responsavel pela abertura de uma conta-salario?	O empregador - empresa ou orgao publico.	#conta-salario #conceitos
```

Arquivos completos do exemplo:
- `examples/servicos_bancarios.md`
- `examples/flashcards_servicos_bancarios.tsv`

## Importar no Anki (checklist rápido)

- Tipo: texto separado por tabulações
- Campo 1 -> Frente
- Campo 2 -> Verso
- Campo 3 -> Tags

## Estrutura do repo

- `assets/` imagens usadas no README
- `prompts/` prompts de geração de flashcards
- `examples/` exemplo completo de entrada e saída
- `docs/` notas curtas e explicações
- `archive/` materiais de referência antigos (não usados no README)

## Referências (artigos e fontes)

- Ebbinghaus, H. (2013, reimp.). *Memory: A Contribution to Experimental Psychology*. Annals of Neurosciences. https://doi.org/10.5214/ans.0972.7531.200408
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Distributed practice in verbal recall tasks: A review and quantitative synthesis*. Psychological Bulletin. https://doi.org/10.1037/0033-2909.132.3.354
- Roediger, H. L., & Karpicke, J. D. (2006). *Test-enhanced learning: Taking memory tests improves long-term retention*. Psychological Science. https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). *Spacing effects in learning: A temporal ridgeline of optimal retention*. Psychological Science. https://doi.org/10.1111/j.1467-9280.2008.02209.x
- *Método de Leitner* (visão geral). https://en.wikipedia.org/wiki/Leitner_system
