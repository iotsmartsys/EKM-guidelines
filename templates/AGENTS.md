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
- Classifique individualmente todos os requisitos e dimensões obrigatórias em uma matriz de evidências. Um bloqueio interrompe a implementação, mas não encerra a análise restante.
- Execute a Technical Readiness Review e a implementação em execuções separadas. A execução da revisão deve encerrar sem alterar implementação, inclusive com resultado `Implementable`.
- Trate `Implementable` como apto para aprovação humana, não como autorização automática. Implemente somente após aprovação explícita do responsável para a revisão e o baseline registrados.
- Antes da primeira alteração, reconfirme especificação, branch, commit, worktree, resultado aprovado e transação `Open`. Mudança material exige nova revisão integral.
- Se qualquer requisito obrigatório exigir inferência relevante, não implemente nenhum item; registre a lacuna e proponha o ajuste na especificação.
- Após ajuste aprovado da especificação, repita a análise integral antes de implementar.
- Em `Needs Clarification`, altere somente registros EKM e a correção normativa explicitamente aprovada.
- Reporte `Needs Clarification` como bloqueio, nunca como implementação concluída.
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

Informe resultado, requisitos, arquivos, contratos, conhecimento alterado, validações, pendências, desvios, revisão e aprovação que autorizaram a implementação, reconfirmação do baseline, estado EKM e operações externas.
