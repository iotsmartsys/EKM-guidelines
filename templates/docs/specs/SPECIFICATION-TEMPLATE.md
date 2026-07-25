# Especificação — `<FUNCIONALIDADE OU CONTRATO>`

**ID:** `<PROJETO-DOMÍNIO>`

**Tipo:** Normativo

**Estado normativo:** Draft

**Estado da implementação:** Not Started

**Estado da entrega:** Not Ready

**Technical readiness:** Pending Review

**Parecer humano da especificação:** Pending

**Versão:** 0.1

**Responsável:** `<RESPONSÁVEL>`

**Relação normativa:** `New | Amends <ID@VERSÃO> | Supersedes <ID@VERSÃO> | Corrects <ID@VERSÃO> | Retires <ID@VERSÃO>`

## Ownership do documento

- O Autor da Especificação é responsável pelas seções 1 a 12, pelo estado
  inicial pendente da seção 13 e pelo estado inicial da seção 14.1.
- A modalidade de confecção fica fora do contrato; a EKM não prevê nem exige
  automação da autoria.
- O responsável humano pela intenção emite o parecer da seção 13.
- O Engenheiro Analista é responsável exclusivamente pelo registro da seção
  14.2.
- O Autor não executa nem simula a Technical Readiness Review.
- Durante a elaboração, o estado normativo é `Draft`.
- Ao concluir a autoria, o Autor altera o estado normativo para `Proposed` e
  mantém `Technical readiness: Pending Review` e
  `Parecer humano da especificação: Pending`.
- O parecer humano da especificação e a aprovação humana posterior para
  implementação são decisões diferentes.
- Parecer humano, aprovação para implementação, Tech Lead, integridade,
  validação funcional e integração são registrados na transação `EKM-CHG`.

## 1. Objetivo

`<RESULTADO OBSERVÁVEL PRETENDIDO>`

## 2. Contexto e problema

`<POR QUE A FUNCIONALIDADE EXISTE OU PRECISA MUDAR>`

## 3. Escopo

`<COMPORTAMENTOS ABRANGIDOS>`

## 4. Requisitos

- **`<PREFIXO>-001`:** `<REQUISITO TESTÁVEL>`.
- **`<PREFIXO>-002`:** `<REQUISITO TESTÁVEL>`.

## 5. Fluxos e estados

`<FLUXOS NORMAIS, ALTERNATIVOS E TRANSIÇÕES>`

## 6. Contratos e invariantes

`<API, WIRE, PERSISTÊNCIA, CONCORRÊNCIA, SEGURANÇA, COMPATIBILIDADE>`

## 7. Falhas e condições de borda

`<COMPORTAMENTO ESPERADO DIANTE DE ERROS>`

## 8. Fora de escopo

`<LIMITES EXPLÍCITOS>`

## 9. Critérios de aceite

`<EVIDÊNCIA OBJETIVA PARA CADA REQUISITO>`

## 10. Validações obrigatórias

`<TESTES, BUILDS, HARDWARE, ANÁLISE ESTÁTICA OU AUDITORIA>`

## 11. Ativos de conhecimento afetados

`<DOCUMENTOS QUE PODEM OU DEVEM MUDAR E O QUE PRESERVAR>`

## 12. Relações, desvios e lacunas

`<OUTRAS ESPECIFICAÇÕES, EKM-GAP, COMPORTAMENTO ATUAL DIVERGENTE>`

## 13. Parecer humano da especificação

Ao concluir a autoria, esta seção permanece com `Resultado: Pending`. O
arquiteto ou outro responsável humano autorizado deve declarar:

**Resultado:** `Pending | Accepted | Revision Required`

**Responsável humano:** `<NOME OU PENDING>`

**Data:** `<AAAA-MM-DD OU PENDING>`

**Checkpoint avaliado:** `<BRANCH E SHA OU PENDING>`

**Escopo do parecer:** `<INTENÇÃO, REQUISITOS, LIMITES E DECISÕES ABRANGIDOS>`

**Ressalvas:** `<LISTA OU NENHUMA>`

**Referência na transação:** `<EKM-CHG-NNNN OU PENDING>`

`Accepted` significa apenas que a especificação representa a intenção conhecida
e pode seguir para análise técnica. Não declara implementabilidade nem autoriza
alteração de código.

`Revision Required` retorna à autoria. `Pending` impede a Technical Readiness
Review.

O parecer é inicialmente declarativo. Nenhum agente pode inventar, presumir ou
conceder essa decisão, e a EKM não alega verificar automaticamente identidade,
autenticidade ou autoridade.

## 14. Registro da Technical Readiness Review

### 14.1 Estado entregue ao Engenheiro Analista

Antes do handoff ao Analista, esta seção deve registrar:

**Resultado:** `Pending Review`

**Revisão executada:** Não.

**Parecer humano da especificação:** `Pending | Accepted`

O Autor e o responsável humano não devem preencher baseline analisado,
requisitos analisados, matriz, lacunas ou evidência da revisão. Não use
`Not Applicable` para representar uma revisão que não aconteceu.

O valor deve estar `Accepted` antes do handoff ao Engenheiro Analista.

### 14.2 Registro exclusivo do Engenheiro Analista

Antes de modificar esta especificação, o Engenheiro Analista executa o gate de
admissão. Se o resultado for `Checkpoint Blocked`, não altera este documento e
entrega um relatório read-only à Coordenação, que o registra na transação.

Somente após `Accepted`, o Analista preserva a seção 14.1 como evidência do
handoff e preenche o registro abaixo.

**Contrato EKM aplicável:** `<FONTE E VERSÃO DO PROTOCOLO>`

**Baseline analisado:** `<BRANCH, COMMIT E WORKTREE>`

| Controle de admissão | Esperado | Observado | Resultado |
|---|---|---|---|
| Branch e SHA | `<CHECKPOINT>` | `<EVIDÊNCIA>` | `Accepted` |
| Worktree | `Clean` | `<EVIDÊNCIA>` | `Accepted` |
| Estados e parecer humano | `Proposed / Accepted / Pending Review / Not Started / Not Ready` | `<ESTADOS E PARECER>` | `Accepted` |
| Transação | `Open` | `<ESTADO>` | `Accepted` |
| Contrato e artefatos | `<VERSÃO E ARTEFATOS>` | `<EVIDÊNCIA>` | `Accepted` |

**Resultado do gate de admissão:** `Accepted`

Após `Accepted`, preencha o restante desta seção e atualize o metadado
`Technical readiness`.

**Resultado da Technical Readiness Review:** `Implementable | Needs Clarification`

**Requisitos analisados:** `<LISTA OU INTERVALO>`

**Dependências e fontes consultadas:** `<LISTA>`

| Requisito ou dimensão | Resultado | Natureza da lacuna | Evidência | Lacuna ou impacto | Decisão necessária |
|---|---|---|---|---|---|
| `<ID OU ASPECTO>` | `Supported`, `Gap`, `Conflict` ou `Not Applicable` | `Normative`, `Baseline`, `Tooling`, `Evidence` ou `None` | `<EVIDÊNCIA>` | `<IMPACTO OU NONE>` | `<DECISÃO OU NONE>` |

**Lacunas ou decisões ausentes:** `<NENHUMA OU ITENS RASTREÁVEIS>`

| Dúvida ou decisão já declarada | Classificação | Evidência | Ação |
|---|---|---|---|
| `<ITEM OU NONE>` | `Blocking`, `Non-blocking`, `Out of scope` ou `Unrequested option` | `<EVIDÊNCIA>` | `<RETORNO À AUTORIA OU NONE>` |

**Evidência do resultado:** `<COMANDOS, INSPEÇÕES E CONCLUSÃO>`

**Reconciliação de saída:** `<METADADOS, SEÇÃO 14, TRANSAÇÃO E GATE SEGUINTE>`

**Referência na transação:** `<EKM-CHG-NNNN E CHECKPOINT>`

A revisão deve continuar após o primeiro bloqueio até classificar todos os
itens. Sua execução encerra sem alterar implementação, inclusive com
`Implementable`.

Distinga decisão indispensável, comportamento fora de escopo e opção não
solicitada. Somente decisão indispensável ausente produz `Gap`. A natureza da
lacuna explica sua origem, mas não cria um terceiro resultado da revisão.

Uma especificação `Needs Clarification` não autoriza implementação parcial nem
alteração de artefatos de implementação. Somente registros EKM e a correção
normativa aprovada podem mudar. Após correção normativa, um novo parecer humano
deve aceitar o checkpoint antes que a análise seja repetida integralmente.

`Implementable` é recomendação técnica. Aprovação humana e reconfirmação do
baseline são registradas na transação antes da implementação.
