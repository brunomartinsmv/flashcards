# Flashcards

Este repositório mantém o fluxo pessoal do Bruno para gerar, validar e importar
flashcards com base em ciência cognitiva e repetição espaçada. Hoje o foco é
espanhol e inglês rumo à fluência; outros idiomas entram no mesmo padrão depois.

Domínio: [`CONTEXT.md`](CONTEXT.md). Decisões: [`docs/adr/`](docs/adr/).

## Por que funciona (versão técnica)

A memória humana sofre decaimento ao longo do tempo quando não há revisão. A
curva do esquecimento, descrita por Hermann Ebbinghaus, caracteriza essa perda
de informação e motivou a ideia de revisar em momentos estratégicos.

Dois efeitos robustos sustentam a repetição espaçada:

### 1) Spacing effect (prática distribuída)

Revisões espaçadas superam revisões concentradas (massed practice). A
meta-análise clássica de Cepeda et al. (2006) sintetiza centenas de estudos e
mostra que a distribuição temporal melhora a retenção. Um resultado central é
que o intervalo ideal entre revisões (ISI) aumenta conforme o intervalo até o
teste final aumenta. Ou seja, quanto maior o prazo até a avaliação, mais
espaçado deve ser o estudo.

### 2) Testing effect (recuperação ativa)

Testar-se (recuperar ativamente) melhora a retenção de longo prazo mais do que
apenas reler, mesmo quando a releitura aumenta a confiança imediata. Em estudos
com atrasos de dias a semanas, testes anteriores produzem retenção superior em
comparação à releitura repetida.

### 3) Otimização de intervalos

Estudos posteriores mapearam o espaçamento ao longo de semanas e meses,
mostrando que existe um "ridgeline" temporal: intervalos muito curtos
desperdiçam esforço, e intervalos muito longos deixam a informação se perder
antes da revisão. O melhor intervalo depende do tempo até a prova, reforçando a
ideia de espaçamento adaptativo.

![Curva do esquecimento](assets/ForgettingCurve.svg)

O método de Leitner operacionaliza esses efeitos com simplicidade: cards
corretos avançam para caixas com intervalos maiores; cards errados voltam para
revisões frequentes.

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

Spaced repetition é robusta, mas não é uma fórmula mágica. A meta-análise de
prática distribuída mostra que o ganho depende do intervalo entre sessões e do
tempo até o teste final: intervalos muito curtos ou muito longos reduzem a
eficiência. Estudos posteriores mostram a mesma relação em prazos longos
(semanas a meses), sugerindo que o espaçamento deve ser ajustado ao horizonte
de retenção.

O testing effect também tem limites: recuperar ativamente pode parecer mais
difícil e pode reduzir a confiança imediata, mesmo quando melhora a retenção no
longo prazo. Isso implica que o usuário pode sentir que está "indo pior" no
curto prazo, quando na verdade está aprendendo mais.

Na prática, flashcards são excelentes para fatos, definições, fórmulas e
discriminações simples. Para habilidades complexas, eles ajudam na base
conceitual, mas não substituem prática deliberada (resolver problemas,
escrever, programar, etc.). Use flashcards como camada de memória, não como
única estratégia.

## Fluxo atual (idiomas)

Pipeline por **Lote** (ver Process Skill + profile do idioma):

1. **Inventory Gate** — export do Deck com ≤ 7 dias
   (`idioms__spanish.txt` / `idioms__english.txt` em `Documents/`).
2. Gerar seguindo
   [`skills/language-anki-flashcards/SKILL.md`](skills/language-anki-flashcards/SKILL.md)
   e o profile em `skills/language-anki-flashcards/profiles/`.
3. Salvar em `flashcards/<language>/anki_<slug>_YYYY-MM-DD_cloze.tsv`.
4. Validar:

   ```bash
   python3 skills/language-anki-flashcards/scripts/validate_flashcards.py \
     flashcards/spanish/anki_espanhol_YYYY-MM-DD_cloze.tsv
   ```

5. **Review Gate** — editar/rejeitar cards.
6. **Prompt Import** — importar no Anki em seguida (lote menor se New estiver alto).

Espanhol e inglês rodam em paralelo. Input da semana tem prioridade sobre os
temas default do profile.

## Formato ativo

Novos lotes usam o note type **Cloze** e quatro colunas separadas por tab:

1. `Text`: frase no idioma-alvo com um `{{c1::Target}}`;
2. `Extra`: Support (PT e/ou sentido na frase — ver profile);
3. `Notas`: regência, contraste ou variante (pode ficar vazio);
4. `Tags`: tags separadas por espaços.

No Anki, use Cloze com campo `Notas` (ou ignore essa coluna) e mapeie a quarta
coluna para Tags.

O arquivo `anki_espanhol_2026-07-24_producao.tsv` é Basic de transição e não é
modelo. Lotes antigos em `flashcards/spanish/` entram no inventário anti-duplicata.

## Estrutura

```text
flashcards/spanish/                 Lotes ES
flashcards/english/                 Lotes EN
skills/language-anki-flashcards/    Process Skill, profiles, validador
CONTEXT.md                          glossário do domínio
docs/adr/                           decisões estruturais
assets/                             diagramas deste README
archive/legacy/                     prompts/exemplo genéricos antigos
archive/spaced-repetition/          docs e fontes científicas
```

## Dependência externa

Exports vivos ficam fora do repo (`Documents/idioms__*.txt`). Sem export fresco
o validador falha no Inventory Gate (`--skip-inventory-gate` só para debug).

## Referências (artigos e fontes)

- Ebbinghaus, H. (2013, reimp.). *Memory: A Contribution to Experimental Psychology*. Annals of Neurosciences. https://doi.org/10.5214/ans.0972.7531.200408
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). *Distributed practice in verbal recall tasks: A review and quantitative synthesis*. Psychological Bulletin. https://doi.org/10.1037/0033-2909.132.3.354
- Roediger, H. L., & Karpicke, J. D. (2006). *Test-enhanced learning: Taking memory tests improves long-term retention*. Psychological Science. https://doi.org/10.1111/j.1467-9280.2006.01693.x
- Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). *Spacing effects in learning: A temporal ridgeline of optimal retention*. Psychological Science. https://doi.org/10.1111/j.1467-9280.2008.02209.x
- *Método de Leitner* (visão geral). https://en.wikipedia.org/wiki/Leitner_system
