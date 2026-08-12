# Especificação — `<FUNCIONALIDADE OU CONTRATO>`

**ID:** `<PROJETO-DOMÍNIO>`

**Classe da fonte:** Normativa

**Versão:** 0.1

**Estado do workflow:** Rascunho e análise [`Draft and Analysis`]

**Decisão do Arquiteto:** Em análise | Pronta para implementação | Em
validação | Concluída | Reaberta

**Análise de implementabilidade:** Pendente | `Ready` | `<OUTRA CLASSIFICAÇÃO>`

**Autorização de implementação desta versão:** Não concedida | Concedida

**Bloqueio arquitetural:** Nenhum | Bloqueada por `<ID OU CAPACIDADE>`

**Relações normativas e de dependência:**

- Nova [`New`] — somente quando não existir autoridade anterior para o
  comportamento; ou
- Altera [`Amends`] `<ID@VERSÃO>`;
- Substitui [`Supersedes`] `<ID@VERSÃO>`;
- Corrige [`Corrects`] `<ID@VERSÃO>`;
- Descontinua [`Retires`] `<ID@VERSÃO>`;
- Depende de [`Depends On`] `<ID@VERSÃO E ESTADO MATERIAL NECESSÁRIO>`; ou
- Habilita [`Enables`] `<ID@VERSÃO>`.

Declare uma linha por fonte afetada quando houver mais de uma relação. Uma
especificação nova em seu recorte ainda pode alterar contratos públicos, ciclos
de vida ou nomenclatura governados por outras fontes.

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

### 3.2 Limite de escopo funcional

**Capacidades arquiteturais pressupostas:** `<FONTES VIGENTES OU NENHUMA>`

**Preparação arquitetural separada:** `<ID E CONDIÇÃO DE RETOMADA OU NÃO
APLICÁVEL>`

Uma capacidade ausente que possa ser especificada e validada sem esta
funcionalidade e que altere materialmente componentes compartilhados,
autoridades ou consumidores não deve ser desenhada aqui. Mantenha a
funcionalidade bloqueada e registre somente `Depends On`; a preparação registra
`Enables` e seu próprio contrato.

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

**ADRs relacionadas:** `<CAMINHOS OU NENHUMA>`

**Autoridades confrontadas:** `<FONTES NORMATIVAS DOS COMPORTAMENTOS, APIS,
ESTADOS, CICLOS DE VIDA, NOMES E FRONTEIRAS AFETADOS; A MATRIZ DETALHADA
PERMANECE NO RELATÓRIO DE ANÁLISE>`

**Relatórios esperados:** análise | implementação | revisão, se acionada |
validação, conforme risco e recorte.

Análise, implementação, challenge e validação são registrados em relatórios
separados. A especificação pode referenciá-los e refletir decisões incorporadas
pelo Arquiteto, mas não recebe a narrativa dessas atuações.
