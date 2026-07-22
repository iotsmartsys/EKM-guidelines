# Instruções para agentes

Este repositório adota Engineering Knowledge Management (EKM).

Antes de alterar código, build, testes, automações ou documentação, leia nesta ordem:

1. `docs/rfc/EKM-GUIDELINES.md`;
2. `docs/rfc/KNOWLEDGE-MAP.md`;
3. as especificações ativas relacionadas em `docs/specs/`;
4. `docs/rfc/EKM-CHANGELOG.md` e a transação aberta.

## Regras obrigatórias

- A especificação define o comportamento esperado; não invente contratos ausentes.
- Preserve APIs, contratos e conhecimento normativo salvo autorização explícita.
- Considere todo o worktree inicial como baseline.
- Abra ou identifique uma transação EKM antes de mudança relevante.
- Registre lacunas em vez de preenchê-las por suposição.
- Interrompa a parte afetada quando houver ambiguidade de produto, arquitetura ou compatibilidade.
- Não execute operações Git ou externas não autorizadas.
- Preserve alterações preexistentes e fora do escopo.

## Relatório obrigatório

Informe resultado, requisitos, arquivos, contratos, conhecimento alterado, validações, pendências, desvios, estado EKM e operações externas.
