# EKM — Histórico de mudanças

Cada mudança relevante possui uma seção `EKM-CHG-NNNN`. A mesma transação
consolida os registros dos atores e pontos de controle. Não duplique a matriz
da revisão de implementabilidade: mantenha-a na especificação e referencie-a
aqui.

Quando o registro fizer parte do próprio commit de saída, o campo de SHA
permanece “a registrar no próximo marco”, e a Coordenação o completa no marco
versionado da etapa seguinte.
Não altere retroativamente um commit apenas para fazê-lo referenciar a si mesmo.

## EKM-CHG-NNNN — `<TÍTULO>`

**Estado:** Aberta [`Open`] | Bloqueada [`Blocked`] | Substituída
[`Superseded`] | Fechada [`Closed`]

**Data de abertura:** `<AAAA-MM-DD>`

**Especificação:** `<ID@VERSÃO E CAMINHO OU NÃO APLICÁVEL>`

## 1. Objetivo e escopo

**Objetivo:** `<RESULTADO PRETENDIDO>`

**Incluído:** `<ESCOPO AUTORIZADO>`

**Fora de escopo:** `<LIMITES>`

## 2. Estado de referência e branch

- Repositório: `<CAMINHO>`.
- Referência de origem: `main`.
- Commit de origem: `<SHA>`.
- Árvore de trabalho de origem: `<LIMPA OU DIFERENÇAS REGISTRADAS>`.
- Branch da mudança: `<BRANCH EXCLUSIVA>`.
- Fontes normativas: `<LISTA>`.
- Lacunas preexistentes relevantes: `<LISTA OU NENHUMA>`.

### 2.1 Transferências de responsabilidade e contrato EKM aplicável

O apontamento pode ser dinâmico sem fixação por SHA. A Coordenação registra qual
contrato rege cada transferência e resolve incompatibilidades antes do ator
seguinte.

| Etapa | Marco versionado de entrada | Estados esperados | Parecer ou autorização humana aplicável | Fonte e versão do contrato | Compatibilidade ou normalização | Resultado da admissão |
|---|---|---|---|---|---|---|
| `<PAPEL>` | `<SHA>` | `<ESTADOS>` | `<RESULTADO E REFERÊNCIA OU NÃO APLICÁVEL>` | `<CAMINHO E VERSÃO>` | `<AÇÃO OU NENHUMA>` | Admitido [`Accepted`], Marco bloqueado [`Checkpoint Blocked`] ou Não aplicável [`Not Applicable`] |

## 3. Autoria da especificação

- Autor: `<RESPONSÁVEL>`.
- Marco versionado de entrada: `<SHA E ESTADOS>`.
- Decisões humanas recebidas: `<LISTA>`.
- Fatos e fontes consultadas: `<LISTA>`.
- Lacunas indispensáveis: `<LISTA OU NENHUMA>`.
- Opções não solicitadas ou itens fora de escopo: `<LISTA OU NENHUMA>`.
- Estado produzido: Proposta [`Proposed`] / Pendente de revisão
  [`Pending Review`] / Não iniciada [`Not Started`] / Não pronta [`Not Ready`].
- Parecer humano da especificação: Pendente [`Pending`].
- Marco versionado de saída: `<SHA OU A REGISTRAR NO PRÓXIMO MARCO>`.

O Autor não preenche matriz da revisão de implementabilidade nem alega
implementabilidade.

## 4. Parecer humano da especificação

- Resultado: Intenção aceita [`Accepted`] | Revisão necessária
  [`Revision Required`] | Pendente [`Pending`].
- Responsável humano: `<NOME>`.
- Data: `<AAAA-MM-DD>`.
- Especificação e versão: `<ID@VERSÃO>`.
- Marco versionado avaliado: `<BRANCH E SHA>`.
- Escopo do parecer:
  `<INTENÇÃO, REQUISITOS, LIMITES E DECISÕES ABRANGIDOS>`.
- Ressalvas: `<LISTA OU NENHUMA>`.
- Marco versionado de saída: `<SHA OU A REGISTRAR NO PRÓXIMO MARCO>`.

Intenção aceita [`Accepted`] confirma que a especificação representa a intenção conhecida e pode
seguir para análise técnica. Não declara implementabilidade nem autoriza
alteração de código. Commit, silêncio ou parecer de agente não substitui esta
decisão.

O registro é inicialmente declarativo. A EKM não alega verificar
automaticamente identidade, autenticidade ou autoridade.

## 5. Engenheiro Analista

- Responsável: `<RESPONSÁVEL>`.
- Marco versionado de entrada: `<SHA E ESTADOS>`.
- Contrato EKM aplicável: `<FONTE E VERSÃO>`.
- Resultado do ponto de controle de admissão: Admitido [`Accepted`] | Marco
  bloqueado [`Checkpoint Blocked`] | Pendente [`Pending`].
- Divergências de admissão:
  `<BRANCH, SHA, ÁRVORE DE TRABALHO, ESTADOS, TRANSAÇÃO, CONTRATO OU NENHUMA>`.
- Resultado da revisão de implementabilidade:
  Implementável [`Implementable`] | Precisa de esclarecimento
  [`Needs Clarification`] | Não executada [`Not Executed`] | Pendente
  [`Pending`].
- Registro integral:
  `<ESPECIFICAÇÃO, SEÇÃO 14 | RELATÓRIO SOMENTE LEITURA DE ADMISSÃO>`.
- Requisitos e dimensões analisados: `<LISTA OU INTERVALO>`.
- Natureza das lacunas:
  `<NORMATIVA [Normative] | ESTADO DE REFERÊNCIA [Baseline] | FERRAMENTAS [Tooling] | EVIDÊNCIA [Evidence] | NENHUMA [None], COM REFERÊNCIAS>`.
- Classificação de dúvidas e decisões declaradas:
  `<BLOQUEANTE [Blocking] | NÃO BLOQUEANTE [Non-blocking] | FORA DE ESCOPO [Out of scope] | OPÇÃO NÃO SOLICITADA [Unrequested option], COM REFERÊNCIAS>`.
- Lacunas ou decisões necessárias: `<LISTA OU NENHUMA>`.
- Comandos e verificações executados: `<LISTA EXATA>`.
- Resultados e saídas relevantes: `<LISTA OU ARTEFATO>`.
- Operações Git e externas: `<LISTA OU NENHUMA>`.
- Artefatos temporários criados, alterados ou removidos:
  `<LISTA OU NENHUM>`.
- Reconciliação de saída:
  `<METADADOS, SEÇÃO 14, TRANSAÇÃO, PONTO DE CONTROLE E ÁRVORE DE TRABALHO>`.
- Marco versionado de saída: `<SHA OU A REGISTRAR NO PRÓXIMO MARCO>`.
- Próximo ponto de controle:
  `<APROVAÇÃO HUMANA | RETORNO À AUTORIA | RETORNO À COORDENAÇÃO>`.

Marco bloqueado [`Checkpoint Blocked`] encerra a atuação antes da revisão.
Nesse caso, o Analista não altera a revisão de implementabilidade, não preenche
a matriz da revisão e
não normaliza artefatos de outro papel.

## 6. Aprovação humana para implementação

- Resultado: Autorizada [`Approved`] | Rejeitada [`Rejected`] | Pendente
  [`Pending`].
- Responsável: `<NOME>`.
- Data: `<AAAA-MM-DD>`.
- Especificação e versão: `<ID@VERSÃO>`.
- Revisão de implementabilidade aprovada: `<MARCO VERSIONADO>`.
- Estado de referência abrangido: `<BRANCH E SHA>`.
- Limites ou ressalvas: `<LISTA OU NENHUMA>`.
- Marco versionado aprovado para implementação:
  `<SHA OU A REGISTRAR NO PRÓXIMO MARCO>`.

Commit, silêncio ou parecer de agente não substitui esta decisão.

## 7. Engenheiro Implementador

- Responsável: `<RESPONSÁVEL>`.
- Marco versionado de entrada: `<SHA E ESTADOS>`.
- Reconfirmação do estado de referência: `<EVIDÊNCIA>`.
- Resultado: Implementada [`Implemented`] | Implementação bloqueada [`Blocked`]
  | Pendente [`Pending`].
- Requisitos implementados: `<LISTA>`.
- Arquivos alterados: `<LISTA>`.
- Rastreabilidade requisito → alteração → evidência:

| Requisito | Alteração | Evidência |
|---|---|---|
| `<ID>` | `<ARQUIVO/SÍMBOLO>` | `<TESTE/CONSTRUÇÃO/INSPEÇÃO>` |

- Decisões mecânicas locais: `<LISTA OU NENHUMA>`.
- Validações executadas e resultados: `<LISTA>`.
- Validações pendentes: `<LISTA OU NENHUMA>`.
- Desvios ou bloqueios: `<LISTA OU NENHUMA>`.
- Operações Git e externas: `<LISTA OU NENHUMA>`.
- Marco versionado de saída: `<SHA OU A REGISTRAR NO PRÓXIMO MARCO>`.

O relatório registra a execução e não cria requisitos.

## 8. Engenheiro Líder Técnico (`Tech Lead`)

- Responsável: `<RESPONSÁVEL>`.
- Marco versionado de entrada: `<SHA E ESTADOS>`.
- Validações repetidas: `<LISTA E RESULTADOS>`.
- Parecer: Implementação aprovada | Correção necessária | Decisão do arquiteto necessária |
  Não verificável [`Not verifiable`] | Pendente [`Pending`].

| Requisito ou dimensão | Resultado | Evidência | Severidade | Ação necessária |
|---|---|---|---|---|
| `<ID/ASPECTO>` | `<CONFORME/DESVIO/RISCO/NÃO VERIFICÁVEL>` | `<EVIDÊNCIA>` | `<BLOQUEANTE/ALTA/MÉDIA/BAIXA>` | `<AÇÃO OU NENHUMA>` |

- Consistência do relatório do Implementador: `<RESULTADO>`.
- Mudanças não autorizadas: `<LISTA OU NENHUMA>`.
- Recorte corretivo: `<ESCOPO OU NÃO APLICÁVEL>`.
- Marco versionado de saída: `<SHA OU A REGISTRAR NO PRÓXIMO MARCO>`.

O Líder Técnico não corrige a implementação nem cria requisitos.

## 9. Validador de Integridade da EKM

- Responsável: `<RESPONSÁVEL>`.
- Marco versionado de entrada: `<SHA E ESTADOS>`.

| Controle EKM | Resultado | Evidência | Impacto |
|---|---|---|---|
| `<CONTROLE>` | Conforme [`Compliant`], Não conforme [`Non-compliant`], Não verificável [`Not verifiable`], Auditoria bloqueada [`Blocked`] ou Não aplicável [`Not Applicable`] | `<EVIDÊNCIA E VERSÃO DO CONTRATO>` | `<IMPACTO>` |

- Conclusão geral: Conforme | Conforme com ressalvas | Não conforme | Não
  verificável [`Not verifiable`] | Auditoria bloqueada [`Blocked`] | Pendente
  [`Pending`].
- Não conformidades: `<LISTA OU NENHUMA>`.
- Evidências ausentes: `<LISTA OU NENHUMA>`.
- Marco versionado de saída: `<SHA OU A REGISTRAR NO PRÓXIMO MARCO>`.

O Validador audita o processo. Não repete a revisão de implementabilidade, não
substitui o Líder Técnico e não corrige artefatos.

## 10. Validação funcional e operacional

- Responsável humano: `<NOME>`.
- Ambiente: `<AMBIENTE>`.
- Marco versionado ou artefato validado: `<REFERÊNCIA>`.
- Procedimento executado: `<LISTA>`.
- Resultado: Validada [`Validated`] | Rejeitada [`Rejected`] | Pendente
  [`Pending`].
- Evidências: `<LISTA>`.
- Desvios: `<LISTA OU NENHUMA>`.
- Estado recomendado: `<PRONTA PARA INTEGRAÇÃO [Ready for Integration] OU RETORNO CORRETIVO>`.

## 11. Integração e encerramento

- Referência de produção: `main`.
- Autorização para integrar: `<RESPONSÁVEL, DATA E REFERÊNCIA>`.
- Commit, PR ou merge de integração: `<REFERÊNCIA OU A REGISTRAR>`.
- Especificação integrada: `<ID@VERSÃO OU NÃO APLICÁVEL>`.
- Estado normativo: `<VIGENTE [Active] OU OUTRO>`.
- Estado da implementação: `<VALIDADA [Validated] OU OUTRO>`.
- Estado da entrega: `<CONCLUÍDA [Done] OU OUTRO>`.
- Mapa e lacunas reconciliados: `<EVIDÊNCIA>`.
- Operações externas e implantação: `<LISTA OU NENHUMA>`.
- Estado final da transação: Fechada [`Closed`] | Aberta [`Open`] | Bloqueada
  [`Blocked`].
- Critério e evidência de encerramento: `<DESCRIÇÃO>`.

Sem integração comprovada na referência de produção, uma mudança funcional não
pode declarar Concluída [`Done`] nem fechar a transação.

## 12. Pendências, desvios e histórico corretivo

`<LACUNAS, DESVIOS, RETORNOS ENTRE PONTOS DE CONTROLE E MARCOS VERSIONADOS SUBSEQUENTES>`

Mudanças de governança, investigação ou fundação podem marcar etapas funcionais
como Não aplicável [`Not Applicable`], desde que possuam critério próprio,
aprovado e
explicitamente registrado.
