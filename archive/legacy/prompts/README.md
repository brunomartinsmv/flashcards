# Prompts genéricos de flashcards (legado)

Estes prompts pertencem ao fluxo genérico anterior e foram preservados para
consulta. Para o fluxo ES→PT atual, use
`../../../skills/spanish-anki-flashcards/SKILL.md`.

Eles geram flashcards no formato TSV do Anki a partir de notas.

## Prompts disponiveis

- `anki_prompt_completo.md` (modo CLI):
  Use quando tiver um arquivo local e quiser instrucoes detalhadas.
- `anki_prompt_resumido.md` (modo CLI):
  Versao curta para uso rapido.
- `anki_prompt_web.md`:
  Use em chats web: cole o conteudo ou anexe o arquivo no proprio chat.

## Regras rapidas

- Um card = um conceito
- Respostas curtas e objetivas
- Formato TSV com 3 campos (PERGUNTA, RESPOSTA, TAGS)
- 2 a 5 tags por card

O exemplo correspondente está em `../examples/`.
