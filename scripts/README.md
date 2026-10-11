# Scripts

[Frases](frases/README.md) e [léxico](lexico/README.md) guardam os dados editáveis e seus geradores. Execute os comandos a partir da raiz. Eles reescrevem os arquivos derivados; não importam no Anki. Scripts sob Apache 2.0, conforme [LICENSE](../LICENSE).

## Coleções de ML e álgebra linear

Os geradores e verificadores de cada coleção ficam nas respectivas subpastas `scripts/`. Na raiz do repositório, `validar_importacao_anki.py` importa ambas em bancos temporários com o motor do Anki. Não abre a interface nem acessa perfis pessoais. Ele verifica campos, tags, subdecks, imagens e reimportação sem duplicatas, usando o mapeamento Basic com as colunas 1 e 2 para Frente e Verso.

Para executar o teste isoladamente:

```sh
python3 -m venv /tmp/flashcards-anki-audit
/tmp/flashcards-anki-audit/bin/python -m pip install anki==2.1.66
/tmp/flashcards-anki-audit/bin/python scripts/validar_importacao_anki.py
```

A versão 2.1.66 verifica o formato suportado desde Anki 2.1.54. Isso não comprova todas as versões mais recentes nem o funcionamento do diálogo gráfico no perfil do usuário. Os relatórios registram os hashes dos CSVs e TSVs usados. Rode novamente após mudar esses arquivos; os validadores rejeitam relatórios desatualizados.

`python3 -m unittest discover -s tests -p 'test_study_decks.py' -v` testa se os validadores aceitam pacotes completos e rejeitam ZIP sem arquivo, resposta alterada e cálculo incorreto. Requer as dependências dos exemplos, mas não requer o pacote Anki. O workflow `Study decks` executa exemplos, importação e testes em Linux.
