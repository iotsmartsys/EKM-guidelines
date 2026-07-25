# EKM — Histórico de mudanças

Cada mudança relevante possui uma seção `EKM-CHG-NNNN`. A mesma transação
consolida os registros dos atores e gates. Não duplique a matriz da Technical
Readiness Review: mantenha-a na especificação e referencie-a aqui.

Quando o registro fizer parte do próprio commit de saída, o campo de SHA
permanece `Pending` e a Coordenação o completa no checkpoint da etapa seguinte.
Não altere retroativamente um commit apenas para fazê-lo referenciar a si mesmo.

## EKM-CHG-NNNN — `<TÍTULO>`

**Estado:** `Open | Blocked | Superseded | Closed`

**Data de abertura:** `<AAAA-MM-DD>`

**Especificação:** `<ID@VERSÃO E CAMINHO OU NÃO APLICÁVEL>`

## 1. Objetivo e escopo

**Objetivo:** `<RESULTADO PRETENDIDO>`

**Incluído:** `<ESCOPO AUTORIZADO>`

**Fora de escopo:** `<LIMITES>`

## 2. Baseline e branch

- Repositório: `<CAMINHO>`.
- Referência de origem: `main`.
- Commit de origem: `<SHA>`.
- Worktree de origem: `<LIMPO OU DIFERENÇAS REGISTRADAS>`.
- Branch da mudança: `<BRANCH EXCLUSIVA>`.
- Fontes normativas: `<LISTA>`.
- Lacunas preexistentes relevantes: `<LISTA OU NENHUMA>`.

### 2.1 Handoffs e contrato EKM aplicável

O apontamento pode ser dinâmico sem fixação por SHA. A Coordenação registra qual
contrato rege cada handoff e resolve incompatibilidades antes do ator seguinte.

| Etapa | Checkpoint de entrada | Estados esperados | Fonte e versão do contrato | Compatibilidade ou normalização | Resultado da admissão |
|---|---|---|---|---|---|
| `<PAPEL>` | `<SHA>` | `<ESTADOS>` | `<CAMINHO E VERSÃO>` | `<AÇÃO OU NENHUMA>` | `Accepted`, `Checkpoint Blocked` ou `Not Applicable` |

## 3. Autoria da especificação

- Autor: `<RESPONSÁVEL>`.
- Checkpoint de entrada: `<SHA E ESTADOS>`.
- Decisões humanas recebidas: `<LISTA>`.
- Fatos e fontes consultadas: `<LISTA>`.
- Lacunas indispensáveis: `<LISTA OU NENHUMA>`.
- Opções não solicitadas ou itens fora de escopo: `<LISTA OU NENHUMA>`.
- Estado produzido: `Proposed / Pending Review / Not Started / Not Ready`.
- Checkpoint de saída: `<SHA OU PENDENTE>`.

O Autor não preenche matriz de Technical Readiness Review nem alega
implementabilidade.

## 4. Engenheiro Analista

- Responsável: `<RESPONSÁVEL>`.
- Checkpoint de entrada: `<SHA E ESTADOS>`.
- Contrato EKM aplicável: `<FONTE E VERSÃO>`.
- Resultado do gate de admissão: `Accepted | Checkpoint Blocked | Pending`.
- Divergências de admissão:
  `<BRANCH, SHA, WORKTREE, ESTADOS, TRANSAÇÃO, CONTRATO OU NENHUMA>`.
- Resultado da Technical Readiness Review:
  `Implementable | Needs Clarification | Not Executed | Pending`.
- Registro integral:
  `<ESPECIFICAÇÃO, SEÇÃO 13 | RELATÓRIO READ-ONLY DE ADMISSÃO>`.
- Requisitos e dimensões analisados: `<LISTA OU INTERVALO>`.
- Natureza das lacunas:
  `<Normative | Baseline | Tooling | Evidence | None, COM REFERÊNCIAS>`.
- Classificação de dúvidas e decisões declaradas:
  `<Blocking | Non-blocking | Out of scope | Unrequested option, COM REFERÊNCIAS>`.
- Lacunas ou decisões necessárias: `<LISTA OU NENHUMA>`.
- Comandos e verificações executados: `<LISTA EXATA>`.
- Resultados e saídas relevantes: `<LISTA OU ARTEFATO>`.
- Operações Git e externas: `<LISTA OU NENHUMA>`.
- Artefatos temporários criados, alterados ou removidos:
  `<LISTA OU NENHUM>`.
- Reconciliação de saída:
  `<METADADOS, SEÇÃO 13, TRANSAÇÃO, GATE E WORKTREE>`.
- Checkpoint de saída: `<SHA OU PENDENTE>`.
- Gate seguinte:
  `<APROVAÇÃO HUMANA | RETORNO À AUTORIA | RETORNO À COORDENAÇÃO>`.

`Checkpoint Blocked` encerra a atuação antes da revisão. Nesse caso, o
Analista não altera `Technical readiness`, não preenche a matriz da revisão e
não normaliza artefatos de outro papel.

## 5. Aprovação humana para implementação

- Resultado: `Approved | Rejected | Pending`.
- Responsável: `<NOME>`.
- Data: `<AAAA-MM-DD>`.
- Especificação e versão: `<ID@VERSÃO>`.
- Technical Readiness Review aprovada: `<CHECKPOINT>`.
- Baseline abrangido: `<BRANCH E SHA>`.
- Limites ou ressalvas: `<LISTA OU NENHUMA>`.
- Checkpoint aprovado para implementação: `<SHA OU PENDENTE>`.

Commit, silêncio ou parecer de agente não substitui esta decisão.

## 6. Engenheiro Implementador

- Responsável: `<RESPONSÁVEL>`.
- Checkpoint de entrada: `<SHA E ESTADOS>`.
- Reconfirmação do baseline: `<EVIDÊNCIA>`.
- Resultado: `Implemented | Blocked | Pending`.
- Requisitos implementados: `<LISTA>`.
- Arquivos alterados: `<LISTA>`.
- Rastreabilidade requisito → alteração → evidência:

| Requisito | Alteração | Evidência |
|---|---|---|
| `<ID>` | `<ARQUIVO/SÍMBOLO>` | `<TESTE/BUILD/INSPEÇÃO>` |

- Decisões mecânicas locais: `<LISTA OU NENHUMA>`.
- Validações executadas e resultados: `<LISTA>`.
- Validações pendentes: `<LISTA OU NENHUMA>`.
- Desvios ou bloqueios: `<LISTA OU NENHUMA>`.
- Operações Git e externas: `<LISTA OU NENHUMA>`.
- Checkpoint de saída: `<SHA OU PENDENTE>`.

O relatório registra a execução e não cria requisitos.

## 7. Engenheiro Tech Lead

- Responsável: `<RESPONSÁVEL>`.
- Checkpoint de entrada: `<SHA E ESTADOS>`.
- Validações repetidas: `<LISTA E RESULTADOS>`.
- Parecer: `Aprovada | Correção necessária | Decisão do arquiteto necessária | Não verificável | Pending`.

| Requisito ou dimensão | Resultado | Evidência | Severidade | Ação necessária |
|---|---|---|---|---|
| `<ID/ASPECTO>` | `<CONFORME/DESVIO/RISCO/NÃO VERIFICÁVEL>` | `<EVIDÊNCIA>` | `<BLOQUEANTE/ALTA/MÉDIA/BAIXA>` | `<AÇÃO OU NENHUMA>` |

- Consistência do relatório do Implementador: `<RESULTADO>`.
- Mudanças não autorizadas: `<LISTA OU NENHUMA>`.
- Recorte corretivo: `<ESCOPO OU NÃO APLICÁVEL>`.
- Checkpoint de saída: `<SHA OU PENDENTE>`.

O Tech Lead não corrige a implementação nem cria requisitos.

## 8. Validador de Integridade da EKM

- Responsável: `<RESPONSÁVEL>`.
- Checkpoint de entrada: `<SHA E ESTADOS>`.

| Controle EKM | Resultado | Evidência | Impacto |
|---|---|---|---|
| `<CONTROLE>` | `Compliant | Non-compliant | Not verifiable | Blocked` | `<EVIDÊNCIA>` | `<IMPACTO>` |

- Conclusão geral: `Conforme | Conforme com ressalvas | Não conforme | Não verificável | Blocked | Pending`.
- Não conformidades: `<LISTA OU NENHUMA>`.
- Evidências ausentes: `<LISTA OU NENHUMA>`.
- Checkpoint de saída: `<SHA OU PENDENTE>`.

O Validador audita o processo. Não repete a Technical Readiness Review, não
substitui o Tech Lead e não corrige artefatos.

## 9. Validação funcional e operacional

- Responsável humano: `<NOME>`.
- Ambiente: `<AMBIENTE>`.
- Checkpoint ou artefato validado: `<REFERÊNCIA>`.
- Procedimento executado: `<LISTA>`.
- Resultado: `Validated | Rejected | Pending`.
- Evidências: `<LISTA>`.
- Desvios: `<LISTA OU NENHUMA>`.
- Estado recomendado: `<READY FOR INTEGRATION OU RETORNO CORRETIVO>`.

## 10. Integração e encerramento

- Referência de produção: `main`.
- Autorização para integrar: `<RESPONSÁVEL, DATA E REFERÊNCIA>`.
- Commit, PR ou merge de integração: `<REFERÊNCIA OU PENDENTE>`.
- Especificação integrada: `<ID@VERSÃO OU NÃO APLICÁVEL>`.
- Estado normativo: `<ACTIVE OU OUTRO>`.
- Estado da implementação: `<VALIDATED OU OUTRO>`.
- Estado da entrega: `<DONE OU OUTRO>`.
- Mapa e lacunas reconciliados: `<EVIDÊNCIA>`.
- Operações externas e deploy: `<LISTA OU NENHUMA>`.
- Estado final da transação: `Closed | Open | Blocked`.
- Critério e evidência de encerramento: `<DESCRIÇÃO>`.

Sem integração comprovada na referência de produção, uma mudança funcional não
pode declarar `Done` nem fechar a transação.

## 11. Pendências, desvios e histórico corretivo

`<GAPS, DESVIOS, RETORNOS ENTRE GATES E CHECKPOINTS SUBSEQUENTES>`

Mudanças de governança, investigação ou fundação podem marcar etapas funcionais
como `Not Applicable`, desde que possuam critério próprio, aprovado e
explicitamente registrado.
