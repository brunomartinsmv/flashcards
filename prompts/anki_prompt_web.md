# Prompt: Geracao de Flashcards Anki (uso em chat web)

## Contexto

Voce vai criar flashcards para o Anki a partir do conteudo fornecido no chat. O conteudo pode ser colado diretamente abaixo ou enviado como arquivo anexado.

## Conteudo de entrada

- Se o usuario colar o texto, use exatamente o conteudo colado.
- Se o usuario anexar um arquivo, use o conteudo do arquivo anexado.
- Nao invente informacoes que nao estejam no conteudo fornecido.

**CONTEUDO:**
[COLE O TEXTO AQUI OU ANEXE O ARQUIVO]

## Nivel de detalhamento

Escolha o nivel de detalhamento desejado:

- **Minimo (~30-40 flashcards):** apenas conceitos fundamentais e informacoes criticas
- **Medio (~50-70 flashcards):** conceitos principais + exemplos importantes + valores-chave
- **Maximo (~90-120 flashcards):** cobertura completa com detalhes, comparacoes e casos praticos

**Nivel escolhido:** [INSERIR: Minimo/Medio/Maximo]

## Formato de saida

O resultado deve ser TSV (Tab-Separated Values) com 3 campos por linha:

```
PERGUNTA[TAB]RESPOSTA[TAB]TAGS
```

Regras de formatacao:
- Nao use quebras de linha dentro de PERGUNTA, RESPOSTA ou TAGS
- Cada linha deve ter exatamente 3 campos separados por TAB

## Principios de criacao

### Perguntas
- Uma pergunta = um conceito
- Seja especifico e direto
- Use verbos claros: "O que e...", "Qual...", "Quem...", "Quando...", "Como..."
- Evite perguntas longas ou ambíguas

### Respostas
- Concisas, mas completas
- Linguagem clara e objetiva
- Sem informacoes desnecessarias

### Tipos de flashcards
- Definicoes e conceitos
- Valores numericos e datas
- Leis, formulas e normas
- Comparacoes e diferencas
- Procedimentos e processos
- Exemplos e aplicacoes

## Sistema de tags

### Tags primarias (obrigatorias)
- Use o nome da secao/topico principal em kebab-case
- Ex.: `#termodinamica`, `#gramatica-portuguesa`

### Tags secundarias (recomendadas)
- `#conceitos`, `#valores`, `#legislacao`, `#formulas`, `#exemplos`, `#comparacao`, `#procedimentos`, `#historia`, `#personalidades`

### Regras
- Sempre em minusculas
- Separe tags com espaco
- Cada card deve ter 2 a 5 tags

## Conteudo muito longo?

Se o conteudo for grande, divida por secoes e gere os flashcards por partes. No final, una tudo em um unico arquivo TSV.

## Checklist final

- Todas as secoes do material cobertas
- Valores numericos e datas corretos
- Formato TSV valido (3 campos por linha)
- Sem duplicacao de conceitos
- Tags consistentes
- Total de flashcards dentro do esperado
