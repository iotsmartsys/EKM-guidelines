# Especificação — `<FUNCIONALIDADE OU CONTRATO>`

**ID:** `<PROJETO-DOMÍNIO>`

**Classe da fonte:** Normativa

**Versão:** 0.1

**Estado normativo:** Proposta [`Proposed`]

**Estado da implementação:** Não iniciada [`Not Started`]

**Estado da entrega:** Não pronta [`Not Ready`]

**Revisão de implementabilidade:** Pendente de revisão [`Pending Review`]

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

### 7.1 Gate da implementação

- `<COMANDOS E EVIDÊNCIAS AUTOMATIZÁVEIS OBRIGATÓRIAS>`;
- `<CONDIÇÃO OBJETIVA DE SUCESSO, INCLUSIVE CASOS EXECUTADOS QUANDO APLICÁVEL>`;
- `<VALIDAÇÕES HUMANAS OU DE HARDWARE RESERVADAS À ETAPA POSTERIOR>`.

`Implemented` exige todos os critérios automatizáveis obrigatórios aprovados.
Critério falho, não executado ou não verificável mantém `In Progress`.

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

## 10. Revisão de implementabilidade

**Resultado:** Pendente de revisão [`Pending Review`] | Implementável
[`Implementable`] | Precisa de esclarecimento [`Needs Clarification`]

**Resumo da análise:** `<POR QUE A VERSÃO INTEGRAL PODE OU NÃO SER IMPLEMENTADA>`

**Decisões ausentes:** `<NENHUMA OU LISTA OBJETIVA>`

**Evidências consultadas:** `<FONTES MATERIAIS>`

A autoria deixa esta seção Pendente de revisão. Sob ordem do Arquiteto, o
Analista atualiza o resultado sem alterar a implementação. Uma lacuna bloqueante
permite concluir Precisa de esclarecimento, mas a análise formal ainda confronta
todos os elementos normativos da versão, sem exigir matriz universal ou leitura
indiscriminada do repositório.

## 11. Evidências da implementação

`<VALIDAÇÕES MATERIAIS, RESULTADOS E LIMITAÇÕES>`

Esta seção é preenchida durante a implementação. Metadados de commit, branch e
push permanecem no Git e não precisam ser copiados para a especificação.
