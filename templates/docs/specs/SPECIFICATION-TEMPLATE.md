# Especificação — `<FUNCIONALIDADE OU CONTRATO>`

**ID:** `<PROJETO-DOMÍNIO>`

**Classe da fonte:** Normativa

**Versão:** 0.1

**Estado do workflow:** Rascunho e análise [`Draft and Analysis`]

**Decisão do Arquiteto:** Em análise | Pronta para implementação | Em
validação | Concluída | Reaberta

**Relação normativa:** Nova [`New`] | Altera [`Amends`] `<ID@VERSÃO>` |
Substitui [`Supersedes`] `<ID@VERSÃO>` | Corrige [`Corrects`] `<ID@VERSÃO>` |
Descontinua [`Retires`] `<ID@VERSÃO>`

## 1. Objetivo e contexto

`<RESULTADO OBSERVÁVEL E POR QUE ELE É NECESSÁRIO>`

## 2. Escopo

`<COMPORTAMENTOS ABRANGIDOS>`

## 3. Fora de escopo

`<LIMITES EXPLÍCITOS>`

### 3.1 Arquitetura e organização

**Precedente aplicável:** `<FONTE E COMPONENTE EQUIVALENTE MAIS PRÓXIMO>`

**Elementos preservados:** `<ARQUITETURA, ORGANIZAÇÃO E RESPONSABILIDADES QUE
NÃO DEVEM MUDAR>`

**Desvio arquitetural explícito:** Nenhum | `<PADRÃO ATUAL AFETADO; MUDANÇA
PRETENDIDA; ALCANCE; JUSTIFICATIVA OU DECISÃO DO ARQUITETO>`

A ausência de desvio explícito determina preservação do precedente aplicável.

## 4. Requisitos

- **`<PREFIXO>-001`:** `<REQUISITO VERIFICÁVEL>`.
- **`<PREFIXO>-002`:** `<REQUISITO VERIFICÁVEL>`.

## 5. Fluxos, estados e contratos

`<FLUXOS, TRANSIÇÕES, APIS, FORMATOS, PERSISTÊNCIA E INVARIANTES RELEVANTES>`

## 6. Falhas e condições de borda

`<COMPORTAMENTO ESPERADO DIANTE DE ERROS>`

## 7. Critérios de aceite e validações

### `<AC-001>` — `<COMPORTAMENTO OBSERVÁVEL>`

**Cobre:** `<REQUISITO(S)>`

- **Dado que** `<CONDIÇÃO INICIAL MATERIAL>`;
- **Quando** `<AÇÃO, ENTRADA OU EVENTO>`;
- **Então** `<RESULTADO OBSERVÁVEL QUE APROVA O CENÁRIO>`;
- **Evidência:** `<TESTE, INSPEÇÃO OU VALIDAÇÃO TERMINAL>`.

Cada requisito obrigatório deve poder ser classificado como aprovado,
reprovado ou não verificável sem o executor inventar o oráculo. `Dado / Quando /
Então` aproxima o contrato da linguagem BDD, mas não exige Gherkin nem uma
ferramenta específica. Em recortes simples, texto equivalente é suficiente.

Agrupe requisitos somente quando o mesmo cenário, resultado e evidência
comprovarem todos. Evidência parcial deve ser identificada como parcial e não
aprova o critério completo. Doubles preservam as semânticas materiais
substituídas. Compilação não comprova execução; zero casos executados não
constitui aprovação de comportamento.

### 7.1 Evidências planejadas

- `<TESTES, BUILDS E OUTRAS EVIDÊNCIAS PROPORCIONAIS>`;
- `<CONDIÇÃO OBJETIVA DE SUCESSO, INCLUSIVE CASOS EXECUTADOS QUANDO APLICÁVEL>`;
- `<VALIDAÇÕES HUMANAS OU DE HARDWARE RESERVADAS À ETAPA POSTERIOR>`.

Testes automatizados são evidências, não prova absoluta. Não devem ser alterados
apenas para produzir verde. O conjunto e o risco residual são avaliados pelo
Arquiteto.

## 8. Conhecimento afetado

`<FONTES QUE DEVEM MUDAR OU SER PRESERVADAS>`

## 9. Relações, decisões e lacunas

**Fatos observados:** `<EVIDÊNCIAS QUE LIMITAM OU SUSTENTAM A PROPOSTA>`

**Intenção e decisões confirmadas:** `<ORDEM E DECISÕES DO ARQUITETO>`

**Solução proposta:** `<RECOMENDAÇÕES DO AUTOR AINDA SUBORDINADAS AO ARQUITETO>`

**Decisões pendentes:** `<SOMENTE ESCOLHAS NECESSÁRIAS QUE EXIGEM AUTORIDADE
HUMANA, OU NENHUMA>`

**Relações:** `<OUTRAS ESPECIFICAÇÕES E EKOM-GAP RELACIONADAS; QUANDO O
OBJETIVO FOR MULTI-CONTEXTO, IDENTIFIQUE A FONTE RESPONSÁVEL, A DEPENDÊNCIA E O
ESTADO MATERIAL NECESSÁRIO SEM DUPLICAR O CONTEÚDO EXTERNO>`

## 10. Análise de implementabilidade

**Executor da função:** Autor | Autor apoiado por IA | Agente especializado |
Especialista separado

**Recomendação:** Prontidão | Retorno ao rascunho/análise

**Evidências encontradas:** `<FONTES MATERIAIS DO REPOSITÓRIO>`

**Componentes impactados:** `<LISTA OBJETIVA>`

**Restrições conhecidas:** `<LISTA OBJETIVA>`

**Incertezas:** `<LISTA OBJETIVA OU NENHUMA>`

**Experimentos necessários:** `<BUILD, PROTÓTIPO, API, BANCO, HARDWARE OU
NENHUM>`

**Bloqueadores:** `<LISTA OBJETIVA OU NENHUM>`

**Decisões ausentes:** `<NENHUMA OU LISTA OBJETIVA>`

A análise é obrigatória antes da implementação; ator separado não é. Somente o
Arquiteto considera a especificação Pronta e autoriza execução.

## 11. Evidências da implementação

`<VALIDAÇÕES MATERIAIS, RESULTADOS E LIMITAÇÕES>`

Esta seção é preenchida durante a implementação. Metadados de commit, branch e
push permanecem no Git e não precisam ser copiados para a especificação.

## 12. Validação e decisão do Arquiteto

**Evidências confrontadas:** `<CONJUNTO MATERIAL>`

**Challenge consultivo, se acionado:** `<ACHADOS, AUSÊNCIA DE RISCO ADICIONAL
RELEVANTE OU NÃO SOLICITADO>`

**Risco residual:** `<RISCO E TRATAMENTO>`

**Decisão:** Retornar à implementação | Retornar ao rascunho/análise |
Concluir | Reabrir

Somente o Arquiteto determina conclusão ou reabertura.
