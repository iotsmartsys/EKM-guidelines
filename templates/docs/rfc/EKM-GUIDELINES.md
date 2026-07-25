# EKM — Diretrizes de Engenharia e Preservação do Conhecimento

**Tipo:** Normativo

**Status:** Active

**Versão:** 1.4

**Modelo EKM:** 1.7

**Responsável:** `<RESPONSÁVEL>`

**Escopo:** Todo o repositório

## 1. Objetivo

Preservar intenção, decisões, contratos e evidências suficientes para compreender, evoluir, auditar e reconstruir o sistema sem depender de conversas ou memória individual.

## 2. Fontes

- Especificações definem o que o sistema deve fazer.
- Diretrizes definem como mudanças e conhecimento devem ser tratados.
- RFCs e ADRs registram decisões e consequências.
- Código e testes implementam e evidenciam comportamentos.
- Relatórios registram execuções e não alteram requisitos implicitamente.

## 3. Estados das especificações

Estado normativo: `Draft`, `Proposed`, `Approved`, `Active`, `Superseded`, `Withdrawn` ou `Archived`.

Estado da implementação: `Not Started`, `In Progress`, `Implemented`, `Validated`, `Regressed`, `Blocked` ou `Retired`.

Os estados são independentes e toda alteração exige evidência.

Estado da entrega: `Not Ready`, `Ready for Integration` ou `Done`.

O projeto deve declarar sua referência de produção. Após `Done`, a identidade ID+versão da especificação é imutável; evoluções usam nova especificação relacionada como `Amends`, `Supersedes`, `Corrects` ou `Retires`.

## 4. Governança e parecer humano

A EKM busca autonomia governada. Decisões relevantes, aprovações e
responsabilidade final permanecem humanas.

A modalidade de confecção da especificação fica fora do contrato. A EKM não
prevê nem exige automação da autoria. Ao concluir a autoria, a especificação
fica `Proposed` com parecer humano `Pending`.

Antes da Technical Readiness Review, o arquiteto ou responsável humano
autorizado registra `Accepted` ou `Revision Required`. `Accepted` confirma que o
documento representa a intenção conhecida e autoriza somente a análise técnica.
Não declara implementabilidade nem autoriza código.

O parecer é inicialmente declarativo. Nenhum agente pode inferi-lo ou
fabricá-lo, e o projeto não alega verificar automaticamente identidade,
autenticidade ou autoridade.

## 5. Proteção normativa

- Não remover decisões vigentes.
- Não substituir fonte normativa por resumo.
- Não perder obrigação, contexto, risco ou trade-off em reorganização editorial.
- Não resolver conflito normativo silenciosamente.
- Remoção ou enfraquecimento de conhecimento exige autorização humana explícita.

## 6. Baseline

O baseline inclui branch, commit e todo o worktree observado no início. Alterações preexistentes devem ser preservadas e reconciliadas separadamente.

## 7. Transações e lacunas

Mudanças usam `EKM-CHG-NNNN`; lacunas usam `EKM-GAP-NNNN`.

Estados: `Open`, `Blocked`, `Superseded` e `Closed`.

## 8. Technical Readiness Review

Depois do parecer humano `Accepted` e antes de qualquer alteração, analisar se
a especificação é passível de implementação no baseline e declarar:

- `Implementable`: todos os requisitos obrigatórios são executáveis sem inferência relevante;
- `Needs Clarification`: existe decisão ausente, contradição ou ambiguidade com impacto normativo.

Em `Needs Clarification`, nenhum item nem artefato de implementação pode ser alterado. Registrar requisito, evidência, lacuna, decisão ausente, impacto das alternativas e ajuste recomendado. Somente registros EKM e a correção normativa aprovada podem mudar. Depois, repetir a análise integral.

Inferência relevante inclui escolhas sobre comportamento, produto, arquitetura, API, protocolo, persistência, concorrência, segurança, compatibilidade, configuração operacional ou aceite. Implementação parcial exige divisão de escopo explicitamente aprovada.

A revisão é cumulativa: encontrar um bloqueio interrompe qualquer intenção de implementação, mas não encerra a análise. Todos os requisitos, precondições, estados normativos, APIs, ciclos de vida, dependências, compatibilidade e validações devem ser classificados.

Use uma matriz com:

| Requisito ou dimensão | Resultado | Evidência | Lacuna ou impacto | Decisão necessária |
|---|---|---|---|---|
| `<ID OU ASPECTO>` | `Supported`, `Gap`, `Conflict` ou `Not Applicable` | `<EVIDÊNCIA>` | `<IMPACTO OU NONE>` | `<DECISÃO OU NONE>` |

Technical Readiness Review e implementação ocorrem em execuções separadas. A execução da revisão encerra sem alterar implementação, mesmo com `Implementable`.

`Implementable` significa apto para aprovação humana. A implementação exige
aprovação explícita do responsável para a revisão e seu baseline. Antes da
primeira alteração, reconfirmar especificação, parecer humano, branch, commit,
worktree, resultado aprovado e transação `Open`. Mudança material exige novo
parecer humano e nova revisão integral.

`Needs Clarification` deve ser reportado como bloqueio, nunca como implementação concluída. Este controle é manual e não presume múltiplos agentes, CI/CD ou `EKM Gate`.

## 9. Adoção incremental

Classifique domínios como `Unmapped`, `Inventoried`, `Mapped`, `Reviewed`, `Specified` ou `Reconstructible`.

Use specification on touch: funcionalidade relevante modificada deve alcançar ao menos `Specified` antes da implementação.

## 10. Definition of Done

Uma transação só pode ser fechada quando o parecer humano da especificação foi
registrado, uma análise válida autorizou a implementação antes da primeira
alteração e requisitos, implementação, conhecimento, evidências, mapa, gaps e
diferenças do baseline estiverem reconciliados. Validações pendentes e operações
externas devem ser declaradas.

Mudança funcional fica `Ready for Integration` após validação e reconciliação, e `Done` somente após integração à referência de produção.

## 11. Automação e garantias previstas

Um futuro `EKM Gate` poderá automatizar regras verificáveis de estrutura,
presença declarada do parecer, rastreabilidade, imutabilidade e estados. Ele
permanece `Planned / Not Defined`; não alegar garantia automática sem
especificação, ferramenta e política implantadas. Julgamento semântico e
autenticidade do parecer permanecem humanos. A automação desse gate não implica
automação da autoria da especificação.

## 12. Regras específicas do projeto

`<REGISTRAR REFERÊNCIA DE PRODUÇÃO E RESTRIÇÕES PERMANENTES CONFIRMADAS>`
