# Prompt Resumido: Geração de Flashcards Anki

## Instruções Rápidas

Crie flashcards no formato Anki (TSV) a partir do seguinte arquivo:

**Arquivo de entrada:** `[INSERIR CAMINHO]`

**Arquivo de saída:** `[INSERIR CAMINHO]/flashcards_[NOME].txt`

**Nível de detalhamento:** [Mínimo: ~40 / Médio: ~70 / Máximo: ~110 flashcards]

---

## Formato TSV
```
PERGUNTA[TAB]RESPOSTA[TAB]TAGS
```

## Diretrizes

### Criar flashcards para:
1. ✅ Definições e conceitos principais
2. ✅ Valores numéricos, datas e quantidades
3. ✅ Leis, normas, resoluções e fórmulas
4. ✅ Comparações e diferenças
5. ✅ Exemplos e casos práticos
6. ✅ Processos e procedimentos

### Qualidade das perguntas:
- Uma pergunta = um conceito
- Seja específico e direto
- Use: "O que é...", "Qual...", "Quando...", "Como...", "Quantos..."
- Evite ambiguidade

### Qualidade das respostas:
- Conciso mas completo
- Linguagem clara e objetiva
- Sem informações desnecessárias

### Sistema de tags:
- **Tag primária:** nome da seção (#seção-principal)
- **Tags secundárias:** tipo de conteúdo (#conceitos, #valores, #legislacao, #formulas, #exemplos)
- **Tags específicas:** elementos únicos (#lei-123, #1995, #autor-nome)
- **Formato:** 2-5 tags por flashcard, em minúsculas, separadas por hífen

---

## Checklist de Verificação

Após criar os flashcards, confirme:

- [ ] Todas as seções do material cobertas
- [ ] Valores numéricos e datas corretos
- [ ] Formato TSV válido (3 campos por linha)
- [ ] Codificação UTF-8
- [ ] Tags aplicadas consistentemente
- [ ] Sem duplicação de conceitos
- [ ] Total de flashcards dentro do esperado

---

## Comandos de Verificação

```bash
# Verificar arquivo criado
ls -lh "[CAMINHO]"

# Verificar codificação UTF-8
file "[CAMINHO]"

# Contar flashcards
wc -l "[CAMINHO]"

# Ver primeiras linhas
head -n 5 "[CAMINHO]"

# Distribuição de tags
grep -o '#[a-z-]*' "[CAMINHO]" | sort | uniq -c | sort -rn
```

---

## Importação no Anki

1. Arquivo → Importar
2. Tipo: "Texto separado por tabulações"
3. Mapear: Campo1→Frente, Campo2→Verso, Campo3→Tags
4. Importar

---

**Uso:** Cole este prompt + caminho do arquivo + nível desejado
