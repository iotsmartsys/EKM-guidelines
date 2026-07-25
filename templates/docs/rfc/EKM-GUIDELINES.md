# EKM — Diretrizes de Engenharia e Preservação do Conhecimento

**Classe da fonte:** Normativa

**Estado da fonte:** Vigente

**Versão do documento:** 1.5

**Versão do modelo EKM:** 1.8

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

### 2.1 Linguagem normativa

O português do Brasil é o idioma normativo. **DEVE** e **NÃO DEVE** expressam
obrigação; **PODE** expressa permissão; **RECOMENDA-SE** não cria obrigação;
**NÃO SE APLICA** exige motivo e evidência.

Nomes de ferramentas, comandos, arquivos, APIs e identificadores estáveis podem
permanecer no idioma original. Estados e resultados devem apresentar rótulo
canônico em português; os valores ingleses entre colchetes são identificadores
legados de compatibilidade. `Accepted`, `Pending` e `Blocked` nunca devem
aparecer sem o contexto da decisão ou etapa a que pertencem.

## 3. Estados das especificações

Estado normativo: Rascunho [`Draft`], Proposta [`Proposed`], Aprovada
[`Approved`], Vigente [`Active`], Substituída [`Superseded`], Retirada
[`Withdrawn`] ou Arquivada [`Archived`].

Estado da implementação: Não iniciada [`Not Started`], Em andamento
[`In Progress`], Implementada [`Implemented`], Validada [`Validated`],
Regredida [`Regressed`], Bloqueada [`Blocked`] ou Descontinuada [`Retired`].

Os estados são independentes e toda alteração exige evidência.

Estado da entrega: Não pronta [`Not Ready`], Pronta para integração
[`Ready for Integration`] ou Concluída [`Done`].

O projeto deve declarar sua referência de produção. Após `Done`, a identidade ID+versão da especificação é imutável; evoluções usam nova especificação relacionada como `Amends`, `Supersedes`, `Corrects` ou `Retires`.

## 4. Governança e parecer humano

A EKM busca autonomia governada. Decisões relevantes, aprovações e
responsabilidade final permanecem humanas.

A modalidade de confecção da especificação fica fora do contrato. A EKM não
prevê nem exige automação da autoria. Ao concluir a autoria, a especificação
fica `Proposed` com parecer humano `Pending`.

Antes da revisão de implementabilidade, o arquiteto ou responsável humano
autorizado registra `Accepted` ou `Revision Required`. `Accepted` confirma que o
documento representa a intenção conhecida e autoriza somente a análise técnica.
Não declara implementabilidade nem autoriza código.

O parecer é inicialmente declarativo. Nenhum agente pode inferi-lo ou
fabricá-lo, e o projeto não alega verificar automaticamente identidade,
autenticidade ou autoridade.

## 5. Proteção normativa

- Não remover decisões vigentes.
- Não substituir fonte normativa por resumo.
- Não perder obrigação, contexto, risco ou relação de ganhos e perdas em
  reorganização editorial.
- Não resolver conflito normativo silenciosamente.
- Remoção ou enfraquecimento de conhecimento exige autorização humana explícita.

## 6. Baseline

O estado de referência inclui branch, commit e toda a árvore de trabalho
observada no início. Alterações preexistentes devem ser preservadas e
reconciliadas separadamente.

## 7. Transações e lacunas

Mudanças usam `EKM-CHG-NNNN`; lacunas usam `EKM-GAP-NNNN`.

Estados: `Open`, `Blocked`, `Superseded` e `Closed`.

## 8. Revisão de implementabilidade

Depois do parecer humano `Accepted` e antes de qualquer alteração, analisar se
a especificação é passível de implementação no estado de referência e declarar:

- Implementável [`Implementable`]: todos os requisitos obrigatórios são executáveis sem inferência relevante;
- Precisa de esclarecimento [`Needs Clarification`]: existe decisão ausente, contradição ou ambiguidade com impacto normativo.

Em `Needs Clarification`, nenhum item nem artefato de implementação pode ser alterado. Registrar requisito, evidência, lacuna, decisão ausente, impacto das alternativas e ajuste recomendado. Somente registros EKM e a correção normativa aprovada podem mudar. Depois, repetir a análise integral.

Inferência relevante inclui escolhas sobre comportamento, produto, arquitetura, API, protocolo, persistência, concorrência, segurança, compatibilidade, configuração operacional ou aceite. Implementação parcial exige divisão de escopo explicitamente aprovada.

A revisão é cumulativa: encontrar um bloqueio interrompe qualquer intenção de implementação, mas não encerra a análise. Todos os requisitos, precondições, estados normativos, APIs, ciclos de vida, dependências, compatibilidade e validações devem ser classificados.

Use uma matriz com:

| Requisito ou dimensão | Resultado | Evidência | Lacuna ou impacto | Decisão necessária |
|---|---|---|---|---|
| `<ID OU ASPECTO>` | Suportado [`Supported`], Lacuna [`Gap`], Conflito [`Conflict`] ou Não aplicável [`Not Applicable`] | `<EVIDÊNCIA>` | `<IMPACTO OU NENHUM>` | `<DECISÃO OU NENHUMA>` |

Revisão de implementabilidade e implementação ocorrem em execuções separadas.
A execução da revisão encerra sem alterar implementação, mesmo com o resultado
Implementável [`Implementable`].

`Implementable` significa apto para aprovação humana. A implementação exige
aprovação explícita do responsável para a revisão e seu estado de referência. Antes da
primeira alteração, reconfirmar especificação, parecer humano, branch, commit,
árvore de trabalho, resultado aprovado e transação Aberta [`Open`]. Mudança material exige novo
parecer humano e nova revisão integral.

`Needs Clarification` deve ser reportado como bloqueio, nunca como implementação concluída. Este controle é manual e não presume múltiplos agentes, CI/CD ou `EKM Gate`.

## 9. Adoção incremental

Classifique domínios como `Unmapped`, `Inventoried`, `Mapped`, `Reviewed`, `Specified` ou `Reconstructible`.

Use specification on touch: funcionalidade relevante modificada deve alcançar ao menos `Specified` antes da implementação.

## 10. Critérios de conclusão

Uma transação só pode ser fechada quando o parecer humano da especificação foi
registrado, uma análise válida autorizou a implementação antes da primeira
alteração e requisitos, implementação, conhecimento, evidências, mapa, gaps e
diferenças do estado de referência estiverem reconciliados. Validações pendentes e operações
externas devem ser declaradas.

Mudança funcional fica `Ready for Integration` após validação e reconciliação, e `Done` somente após integração à referência de produção.

## 11. Automação e garantias previstas

Um futuro `EKM Gate` poderá automatizar regras verificáveis de estrutura,
presença declarada do parecer, rastreabilidade, imutabilidade e estados. Ele
permanece `Planned / Not Defined`; não alegar garantia automática sem
especificação, ferramenta e política implantadas. Julgamento semântico e
autenticidade do parecer permanecem humanos. A automação desse ponto de controle não implica
automação da autoria da especificação.

## 12. Regras específicas do projeto

`<REGISTRAR REFERÊNCIA DE PRODUÇÃO E RESTRIÇÕES PERMANENTES CONFIRMADAS>`
