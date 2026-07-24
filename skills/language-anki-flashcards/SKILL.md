---
name: language-anki-flashcards
description: >-
  Gera e valida Lotes Cloze de idiomas para Anki do Bruno (Process Skill +
  Language Profiles). Use when creating language flashcards, weekly lotes,
  spanish/english Anki cards, Inventory Gate, or validating flashcards/*.tsv.
---

# Language Anki Flashcards (Process Skill)

Domínio: ver `CONTEXT.md` e `docs/adr/0001`–`0003`.

Este arquivo é o **Process Skill** compartilhado. Sempre carregue também o
**Language Profile** do idioma do ciclo:

- `skills/language-anki-flashcards/profiles/spanish.md`
- `skills/language-anki-flashcards/profiles/english.md`

## Pipeline por Lote

1. **Inventory Gate** — **Deck Export** existe e tem ≤ **7 dias** (`Export Freshness`). Senão, pare e peça reexport.
2. Monte o **Inventory**: Deck Export + `flashcards/<language>/*.tsv` (exceto o arquivo em validação / twins cloze↔produção).
3. Preferir **Input** da semana; senão **Theme Defaults** do profile.
4. Gerar um **Lote** semanal (~10–20 **Cards**; ~5 se New do Deck estiver alto).
5. Salvar em `flashcards/<language>/anki_<slug>_YYYY-MM-DD_cloze.tsv`.
6. Validar:

   ```bash
   python3 skills/language-anki-flashcards/scripts/validate_flashcards.py \
     flashcards/<language>/anki_<slug>_YYYY-MM-DD_cloze.tsv
   ```

7. **Review Gate** — Bruno edita/rejeita Cards.
8. **Prompt Import** — importar no Deck logo em seguida (não estocar no repo).

**Generation Queue**: idiomas ativos em paralelo (hoje spanish + english).

## Formato Cloze (padrão)

Note type Anki: **Cloze**. Colunas (tab):

1. `Text` — frase no idioma-alvo com **um** `{{c1::Target}}` (dica opcional: `{{c1::alvo::dica}}`)
2. `Extra` — **Support** (ver profile: L1 e/ou in-context)
3. `Notas` — regência, contraste, variante (opcional)
4. `Tags` — espaço-separadas: tema nível lote

Sem reversed cards. Basic/`_____` só legado; não gerar novos.

## Regras comuns de conteúdo

- Um **Target** por **Card**
- Frases curtas, plausíveis na vida do Bruno
- Ênfase em **Production** / recuperação (não cognato transparente)
- Sem cards meta (Anki, Duolingo, “importar frases”)
- Rejeitar duplicata de frente normalizada; avisar Target já usado ≥1×; erro se mesmo Target >2× no lote

## Legacy Backlog

Não suspender/reescrever o Deck antigo em massa. A barra de qualidade vale para **Lotes** novos.

## Cadência (estudo)

- Terminar reviews antes dos novos; meta ≥80% dos dias estudados
- FSRS: retenção desejada **90%** (máx. 92%)
- Com New alto: **Lote** reduzido + **Prompt Import**, não pular a esteira nem acumular TSV
- Alertas pós-import: Again nos novos >20%; young <85–88%; retenção >97% com 1–2s/card → fáceis demais; backlog 2 dias → reduzir novos
