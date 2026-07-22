# EKM — Diretrizes de Engenharia e Preservação do Conhecimento

**Tipo:** Normativo

**Status:** Active

**Versão:** 1.0

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

## 7. Adoção incremental

Classifique domínios como `Unmapped`, `Inventoried`, `Mapped`, `Reviewed`, `Specified` ou `Reconstructible`.

Use specification on touch: funcionalidade relevante modificada deve alcançar ao menos `Specified` antes da implementação.

## 8. Definition of Done

Uma transação só pode ser fechada quando requisitos, implementação, conhecimento, evidências, mapa, gaps e diferenças do baseline estiverem reconciliados. Validações pendentes e operações externas devem ser declaradas.

## 9. Regras específicas do projeto

`<REGISTRAR RESTRIÇÕES PERMANENTES CONFIRMADAS PARA ESTE REPOSITÓRIO>`
