# Instruções para agentes

Este repositório adota Engineering Knowledge Management (EKM).

Antes de alterar código, build, testes, automações ou documentação, leia nesta ordem:

1. `docs/rfc/EKM-GUIDELINES.md`;
2. `docs/rfc/KNOWLEDGE-MAP.md`;
3. as especificações ativas relacionadas em `docs/specs/`;
4. `docs/rfc/EKM-CHANGELOG.md` e a transação aberta.

## Regras obrigatórias

- A especificação define o comportamento esperado; não invente contratos ausentes.
- Antes de alterar qualquer artefato de implementação, execute a Technical Readiness Review integral e declare `Implementable` ou `Needs Clarification`.
- Se qualquer requisito obrigatório exigir inferência relevante, não implemente nenhum item; registre a lacuna e proponha o ajuste na especificação.
- Após ajuste aprovado da especificação, repita a análise integral antes de implementar.
- Em `Needs Clarification`, altere somente registros EKM e a correção normativa explicitamente aprovada.
- Preserve APIs, contratos e conhecimento normativo salvo autorização explícita.
- Considere todo o worktree inicial como baseline.
- Abra ou identifique uma transação EKM antes de mudança relevante.
- Registre lacunas em vez de preenchê-las por suposição.
- Não transforme descoberta em decisão de produto, arquitetura, contrato, persistência, segurança, compatibilidade ou comportamento.
- Não reescreva versão de especificação já integrada à referência de produção; crie uma nova especificação relacionada.
- Não presuma que exista `EKM Gate` ou garantia automatizada sem ferramenta e política explicitamente implantadas.
- Não execute operações Git ou externas não autorizadas.
- Preserve alterações preexistentes e fora do escopo.

## Relatório obrigatório

Informe resultado, requisitos, arquivos, contratos, conhecimento alterado, validações, pendências, desvios, estado EKM e operações externas.
