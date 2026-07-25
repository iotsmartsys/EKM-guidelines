# Especificação — `<FUNCIONALIDADE OU CONTRATO>`

**ID:** `<PROJETO-DOMÍNIO>`

**Classe da fonte:** Normativa

**Estado normativo:** Rascunho [`Draft`]

**Estado da implementação:** Não iniciada [`Not Started`]

**Estado da entrega:** Não pronta [`Not Ready`]

**Revisão de implementabilidade:** Pendente de revisão [`Pending Review`]

**Parecer humano da especificação:** Pendente [`Pending`]

**Versão:** 0.1

**Responsável:** `<RESPONSÁVEL>`

**Relação normativa:** Nova [`New`] | Altera [`Amends`] `<ID@VERSÃO>` |
Substitui [`Supersedes`] `<ID@VERSÃO>` | Corrige [`Corrects`] `<ID@VERSÃO>` |
Descontinua [`Retires`] `<ID@VERSÃO>`

## Responsabilidades sobre o documento

- O Autor da Especificação é responsável pelas seções 1 a 12, pelo estado
  inicial pendente da seção 13 e pelo estado inicial da seção 14.1.
- A modalidade de confecção fica fora do contrato; a EKM não prevê nem exige
  automação da autoria.
- O responsável humano pela intenção emite o parecer da seção 13.
- O Engenheiro Analista é responsável exclusivamente pelo registro da seção
  14.2.
- O Autor não executa nem simula a revisão de implementabilidade.
- Durante a elaboração, o estado normativo é Rascunho [`Draft`].
- Ao concluir a autoria, o Autor altera o estado normativo para Proposta
  [`Proposed`] e mantém a revisão como Pendente de revisão [`Pending Review`] e
  o parecer humano como Pendente [`Pending`].
- O parecer humano da especificação e a aprovação humana posterior para
  implementação são decisões diferentes.
- Parecer humano, aprovação para implementação, Líder Técnico, integridade,
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

`<API, FORMATO DE COMUNICAÇÃO, PERSISTÊNCIA, CONCORRÊNCIA, SEGURANÇA, COMPATIBILIDADE>`

## 7. Falhas e condições de borda

`<COMPORTAMENTO ESPERADO DIANTE DE ERROS>`

## 8. Fora de escopo

`<LIMITES EXPLÍCITOS>`

## 9. Critérios de aceite

`<EVIDÊNCIA OBJETIVA PARA CADA REQUISITO>`

## 10. Validações obrigatórias

`<TESTES, PROCESSOS DE CONSTRUÇÃO, HARDWARE, ANÁLISE ESTÁTICA OU AUDITORIA>`

## 11. Ativos de conhecimento afetados

`<DOCUMENTOS QUE PODEM OU DEVEM MUDAR E O QUE PRESERVAR>`

## 12. Relações, desvios e lacunas

`<OUTRAS ESPECIFICAÇÕES, EKM-GAP, COMPORTAMENTO ATUAL DIVERGENTE>`

## 13. Parecer humano da especificação

Ao concluir a autoria, esta seção permanece com resultado Pendente
[`Pending`]. O arquiteto ou outro responsável humano autorizado deve declarar:

**Resultado:** Pendente [`Pending`] | Intenção aceita [`Accepted`] |
Revisão necessária [`Revision Required`]

**Responsável humano:** `<NOME OU PENDENTE>`

**Data:** `<AAAA-MM-DD OU PENDENTE>`

**Marco versionado avaliado:** `<BRANCH E SHA OU A REGISTRAR>`

**Escopo do parecer:** `<INTENÇÃO, REQUISITOS, LIMITES E DECISÕES ABRANGIDOS>`

**Ressalvas:** `<LISTA OU NENHUMA>`

**Referência na transação:** `<EKM-CHG-NNNN OU PENDENTE>`

Intenção aceita [`Accepted`] significa apenas que a especificação representa a intenção conhecida
e pode seguir para análise técnica. Não declara implementabilidade nem autoriza
alteração de código.

Revisão necessária [`Revision Required`] retorna à autoria. Pendente
[`Pending`] impede a revisão de implementabilidade.

O parecer é inicialmente declarativo. Nenhum agente pode inventar, presumir ou
conceder essa decisão, e a EKM não alega verificar automaticamente identidade,
autenticidade ou autoridade.

## 14. Registro da revisão de implementabilidade

### 14.1 Estado entregue ao Engenheiro Analista

Antes da transferência ao Analista, esta seção deve registrar:

**Resultado:** Pendente de revisão [`Pending Review`]

**Revisão executada:** Não.

**Parecer humano da especificação:** Pendente [`Pending`] |
Intenção aceita [`Accepted`]

O Autor e o responsável humano não devem preencher estado de referência analisado,
requisitos analisados, matriz, lacunas ou evidência da revisão. Não use Não
aplicável [`Not Applicable`] para representar uma revisão que não aconteceu.

O valor deve estar como Intenção aceita [`Accepted`] antes da transferência ao
Engenheiro Analista.

### 14.2 Registro exclusivo do Engenheiro Analista

Antes de modificar esta especificação, o Engenheiro Analista executa o ponto de
controle de admissão. Se o resultado for Marco bloqueado
[`Checkpoint Blocked`], não altera este documento e entrega um relatório
somente leitura à Coordenação, que o registra na transação.

Somente após o resultado Admitido [`Accepted`], o Analista preserva a seção
14.1 como evidência da transferência e preenche o registro abaixo.

**Contrato EKM aplicável:** `<FONTE E VERSÃO DO PROTOCOLO>`

**Estado de referência analisado:** `<BRANCH, COMMIT E ÁRVORE DE TRABALHO>`

| Controle de admissão | Esperado | Observado | Resultado |
|---|---|---|---|
| Branch e SHA | `<MARCO VERSIONADO>` | `<EVIDÊNCIA>` | Admitido [`Accepted`] |
| Árvore de trabalho | Limpa [`Clean`] | `<EVIDÊNCIA>` | Admitido [`Accepted`] |
| Estados e parecer humano | Proposta / Intenção aceita / Pendente de revisão / Não iniciada / Não pronta | `<ESTADOS E PARECER>` | Admitido [`Accepted`] |
| Transação | Aberta [`Open`] | `<ESTADO>` | Admitido [`Accepted`] |
| Contrato e artefatos | `<VERSÃO E ARTEFATOS>` | `<EVIDÊNCIA>` | Admitido [`Accepted`] |

**Resultado do ponto de controle de admissão:** Admitido [`Accepted`]

Após o resultado Admitido [`Accepted`], preencha o restante desta seção e
atualize o metadado de revisão de implementabilidade.

**Resultado da revisão de implementabilidade:** Implementável
[`Implementable`] | Precisa de esclarecimento [`Needs Clarification`]

**Requisitos analisados:** `<LISTA OU INTERVALO>`

**Dependências e fontes consultadas:** `<LISTA>`

| Requisito ou dimensão | Resultado | Natureza da lacuna | Evidência | Lacuna ou impacto | Decisão necessária |
|---|---|---|---|---|---|
| `<ID OU ASPECTO>` | Suportado [`Supported`], Lacuna [`Gap`], Conflito [`Conflict`] ou Não aplicável [`Not Applicable`] | Normativa [`Normative`], Estado de referência [`Baseline`], Ferramentas [`Tooling`], Evidência [`Evidence`] ou Nenhuma [`None`] | `<EVIDÊNCIA>` | `<IMPACTO OU NENHUM>` | `<DECISÃO OU NENHUMA>` |

**Lacunas ou decisões ausentes:** `<NENHUMA OU ITENS RASTREÁVEIS>`

| Dúvida ou decisão já declarada | Classificação | Evidência | Ação |
|---|---|---|---|
| `<ITEM OU NENHUM>` | Bloqueante [`Blocking`], Não bloqueante [`Non-blocking`], Fora de escopo [`Out of scope`] ou Opção não solicitada [`Unrequested option`] | `<EVIDÊNCIA>` | `<RETORNO À AUTORIA OU NENHUM>` |

**Evidência do resultado:** `<COMANDOS, INSPEÇÕES E CONCLUSÃO>`

**Reconciliação de saída:** `<METADADOS, SEÇÃO 14, TRANSAÇÃO E PRÓXIMO PONTO DE CONTROLE>`

**Referência na transação:** `<EKM-CHG-NNNN E MARCO VERSIONADO>`

A revisão deve continuar após o primeiro bloqueio até classificar todos os
itens. Sua execução encerra sem alterar implementação, inclusive com o
resultado Implementável [`Implementable`].

Distinga decisão indispensável, comportamento fora de escopo e opção não
solicitada. Somente decisão indispensável ausente produz Lacuna [`Gap`]. A natureza da
lacuna explica sua origem, mas não cria um terceiro resultado da revisão.

Uma especificação que Precisa de esclarecimento [`Needs Clarification`] não
autoriza implementação parcial nem
alteração de artefatos de implementação. Somente registros EKM e a correção
normativa aprovada podem mudar. Após correção normativa, um novo parecer humano
deve aceitar o marco versionado antes que a análise seja repetida integralmente.

Implementável [`Implementable`] é recomendação técnica. Aprovação humana e
reconfirmação do estado de referência são registradas na transação antes da
implementação.
