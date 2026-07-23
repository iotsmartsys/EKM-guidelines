# EKM — Diretrizes de Engenharia e Preservação do Conhecimento

**Tipo:** Normativo

**Status:** Active

**Versão:** 1.2

**Modelo EKM:** 1.5

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

## 4. Proteção normativa

- Não remover decisões vigentes.
- Não substituir fonte normativa por resumo.
- Não perder obrigação, contexto, risco ou trade-off em reorganização editorial.
- Não resolver conflito normativo silenciosamente.
- Remoção ou enfraquecimento de conhecimento exige autorização humana explícita.

## 5. Baseline

O baseline inclui branch, commit e todo o worktree observado no início. Alterações preexistentes devem ser preservadas e reconciliadas separadamente.

## 6. Transações e lacunas

Mudanças usam `EKM-CHG-NNNN`; lacunas usam `EKM-GAP-NNNN`.

Estados: `Open`, `Blocked`, `Superseded` e `Closed`.

## 7. Technical Readiness Review

Antes de qualquer alteração, analisar integralmente a especificação e declarar:

- `Implementable`: todos os requisitos obrigatórios são executáveis sem inferência relevante;
- `Needs Clarification`: existe decisão ausente, contradição ou ambiguidade com impacto normativo.

Em `Needs Clarification`, nenhum item nem artefato de implementação pode ser alterado. Registrar requisito, evidência, lacuna, decisão ausente, impacto das alternativas e ajuste recomendado. Somente registros EKM e a correção normativa aprovada podem mudar. Depois, repetir a análise integral.

Inferência relevante inclui escolhas sobre comportamento, produto, arquitetura, API, protocolo, persistência, concorrência, segurança, compatibilidade, configuração operacional ou aceite. Implementação parcial exige divisão de escopo explicitamente aprovada.

## 8. Adoção incremental

Classifique domínios como `Unmapped`, `Inventoried`, `Mapped`, `Reviewed`, `Specified` ou `Reconstructible`.

Use specification on touch: funcionalidade relevante modificada deve alcançar ao menos `Specified` antes da implementação.

## 9. Definition of Done

Uma transação só pode ser fechada quando uma análise válida autorizou a implementação antes da primeira alteração e requisitos, implementação, conhecimento, evidências, mapa, gaps e diferenças do baseline estiverem reconciliados. Validações pendentes e operações externas devem ser declaradas.

Mudança funcional fica `Ready for Integration` após validação e reconciliação, e `Done` somente após integração à referência de produção.

## 10. Automação e garantias previstas

Um futuro `EKM Gate` poderá automatizar regras verificáveis de estrutura, rastreabilidade, imutabilidade e estados. Ele permanece `Planned / Not Defined`; não alegar garantia automática sem especificação, ferramenta e política implantadas. Julgamento semântico permanece humano.

## 11. Regras específicas do projeto

`<REGISTRAR REFERÊNCIA DE PRODUÇÃO E RESTRIÇÕES PERMANENTES CONFIRMADAS>`
