# Especificação — `<FUNCIONALIDADE OU CONTRATO>`

**ID:** `<PROJETO-DOMÍNIO>`

**Tipo:** Normativo

**Estado normativo:** Draft

**Estado da implementação:** Not Started

**Estado da entrega:** Not Ready

**Technical readiness:** Pending Review

**Versão:** 0.1

**Responsável:** `<RESPONSÁVEL>`

**Relação normativa:** `New | Amends <ID@VERSÃO> | Supersedes <ID@VERSÃO> | Corrects <ID@VERSÃO> | Retires <ID@VERSÃO>`

## Ownership do documento

- O Autor da Especificação é responsável pelas seções 1 a 12 e pelo estado
  inicial pendente da seção 13.1.
- O Engenheiro Analista é responsável exclusivamente pelo registro da seção
  13.2.
- O Autor não executa nem simula a Technical Readiness Review.
- Durante a elaboração, o estado normativo é `Draft`.
- Ao concluir a autoria, o Autor altera o estado normativo para `Proposed` e
  mantém `Technical readiness: Pending Review`.
- Aprovação humana, implementação, Tech Lead, integridade, validação funcional e
  integração são registradas na transação `EKM-CHG`.

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

## 13. Registro da Technical Readiness Review

### 13.1 Estado entregue pelo Autor da Especificação

No checkpoint de saída da autoria, esta seção deve permanecer exatamente como:

**Resultado:** `Pending Review`

**Revisão executada:** Não.

O Autor não deve preencher baseline analisado, requisitos analisados, matriz,
lacunas ou evidência da revisão. Não use `Not Applicable` para representar uma
revisão que não aconteceu.

### 13.2 Registro exclusivo do Engenheiro Analista

Ao executar a revisão, o Engenheiro Analista preserva a seção 13.1 como
evidência do handoff, preenche o registro abaixo e atualiza o metadado
`Technical readiness` com o resultado.

**Resultado:** `Implementable | Needs Clarification`

**Baseline analisado:** `<BRANCH, COMMIT E WORKTREE>`

**Requisitos analisados:** `<LISTA OU INTERVALO>`

**Dependências e fontes consultadas:** `<LISTA>`

| Requisito ou dimensão | Resultado | Evidência | Lacuna ou impacto | Decisão necessária |
|---|---|---|---|---|
| `<ID OU ASPECTO>` | `Supported`, `Gap`, `Conflict` ou `Not Applicable` | `<EVIDÊNCIA>` | `<IMPACTO OU NONE>` | `<DECISÃO OU NONE>` |

**Lacunas ou decisões ausentes:** `<NENHUMA OU ITENS RASTREÁVEIS>`

**Evidência do resultado:** `<COMANDOS, INSPEÇÕES E CONCLUSÃO>`

**Referência na transação:** `<EKM-CHG-NNNN E CHECKPOINT>`

A revisão deve continuar após o primeiro bloqueio até classificar todos os
itens. Sua execução encerra sem alterar implementação, inclusive com
`Implementable`.

Distinga decisão indispensável, comportamento fora de escopo e opção não
solicitada. Somente decisão indispensável ausente produz `Gap`.

Uma especificação `Needs Clarification` não autoriza implementação parcial nem
alteração de artefatos de implementação. Somente registros EKM e a correção
normativa aprovada podem mudar. Após correção normativa, a análise deve ser
repetida integralmente.

`Implementable` é recomendação técnica. Aprovação humana e reconfirmação do
baseline são registradas na transação antes da implementação.
