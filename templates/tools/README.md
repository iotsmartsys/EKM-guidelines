# Guardas estruturais EKOM

`validate_ekom_documents.py` verifica somente regras objetivas do roteamento
EKOM 3.1:

- campos mínimos dos relatórios;
- estrutura mínima das ADRs;
- ausência de headings típicos de relatório em especificações.

Uso sobre todo o projeto:

```sh
python3 tools/validate_ekom_documents.py .
```

Em adoção legada, valide primeiro somente arquivos novos ou alterados:

```sh
python3 tools/validate_ekom_documents.py . docs/specs/nova.md docs/reports/mudanca/analysis/resultado.md
```

A guarda não decide se uma ADR é necessária, se um achado é relevante ou se a
evidência é suficiente. Esses pontos permanecem sob julgamento humano.
