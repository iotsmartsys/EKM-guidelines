# Relatório de análise — `<MUDANÇA>`

**Classe da fonte:** Relatório

**Papel:** Engenheiro Analista | Autor apoiado por IA | Especialista

**Especificação:** `<CAMINHO E VERSÃO>`

**Revisão confrontada:** `<COMMIT, VERSÃO OU ÁRVORE OBSERVADA>`

**Estado:** Em elaboração | Concluído

> Este relatório registra uma atuação e não altera fontes normativas.

## Confronto de autoridades normativas

| Elemento afetado | Fonte vigente | Relação proposta | Conflito ou ação requerida |
|---|---|---|---|
| `<COMPORTAMENTO, API, ESTADO, LIFECYCLE, NOME OU FRONTEIRA>` | `<SPEC, ADR OU DIRETRIZ>` | Preserva | `Nenhuma` |

Use `New`, `Amends`, `Supersedes`, `Corrects` ou `Retires` quando aplicável.
Relação ambígua ou autoridade omitida só impede prontidão quando envolve o mesmo
comportamento e sobreposição material de contratos. Fonte adjacente e extensão
aditiva não exigem emenda. Conflito vigente aplicável permanece bloqueante.

## Resultado

**Classificação principal:** selecione exatamente uma:

- Pronta [`Ready`];
- Não pronta — defeito da especificação [`Not Ready — Specification Defect`];
- Não pronta — pré-requisito arquitetural [`Not Ready — Architectural
  Prerequisite`];
- Não pronta — evidência requerida [`Not Ready — Evidence Required`];
- Não implementável — conflito de restrição [`Not Implementable — Constraint
  Conflict`];
- Desconhecida — impacto não delimitado [`Unknown — Impact Not Delimited`].

**Condições bloqueantes:** `<ITENS OU NENHUMA>`

**Condições não bloqueantes:** `<ITENS OU NENHUMA>`

Não use `prontidão condicionada` como classificação. Classifique cada condição
e informe a ação correspondente. Escolhas técnicas locais e evidências que
serão produzidas durante Implementação ou Revisão não bloqueiam por si sós.

**Teste de suficiência:** `<EXISTE AO MENOS UMA IMPLEMENTAÇÃO TECNICAMENTE
PLAUSÍVEL E CONFORME DENTRO DA BASELINE E DO RECORTE? EVIDÊNCIA OBJETIVA>`

**Razão de cada bloqueio:** `<IMPOSSIBILIDADE OU CONFLITO | DECISÃO NORMATIVA
AUSENTE | PRÉ-REQUISITO ARQUITETURAL | IMPACTO MATERIAL NÃO DELIMITADO |
EVIDÊNCIA PRÉVIA INDISPENSÁVEL | NENHUMA>`

**Quando houver bloqueio por fonte anterior, cadeia causal cumulativa:**
`<REQUISITO ANTERIOR EXPLÍCITO E APLICÁVEL → REQUISITO NOVO NECESSARIAMENTE
INCOMPATÍVEL → CONFLITO INEVITÁVEL → AUSÊNCIA DE IMPLEMENTAÇÃO CONFORME NO
RECORTE, OU NÃO APLICÁVEL>`

## Reconciliação dos achados anteriores

| Achado anterior | Disposição | Regra e evidência |
|---|---|---|
| `<BLOQUEADOR DO RELATÓRIO ANTERIOR>` | `Mantido | Descartado | Não bloqueante` | `<FONTE E FUNDAMENTO>` |

Todo bloqueador anterior aplicável deve aparecer. `Ready` não é válido com
achado sem disposição.

## Controle de cobertura

- **Requisitos confrontados:** `<N>/<TOTAL>`
- **Critérios de aceite confrontados:** `<N>/<TOTAL>`
- **Débitos relacionados confrontados:** `<N>/<TOTAL>`
- **Lacunas de cobertura:** `<ITENS OU NENHUMA>`

## Challenge de `Ready`

**Executado:** `Sim | Não aplicável porque a classificação não é Ready`

**Contradição interna:** `<RESULTADO>`

**Critério insatisfazível ou fora do recorte:** `<RESULTADO>`

**Remediação postergada exigida:** `<RESULTADO>`

**Bloqueador anterior sem disposição:** `<RESULTADO>`

## Fronteira da especificação

**Baseline confrontada:** `<ARQUITETURA, VERSÃO E ESTADO>`

**A correção pertence somente à funcionalidade e seus donos naturais?**
`Sim | Não | Desconhecido`, com evidência.

**Capacidade arquitetural ausente:** `<DESCRIÇÃO OU NENHUMA>`

**Pode ser especificada e validada sem a funcionalidade?**
`Sim | Não | Não aplicável`, com justificativa.

**Componentes e consumidores compartilhados:** `<IDENTIFICADOS>`

**Consumidores ou impactos não delimitados:** `<ITENS OU NENHUM>`

**Impacto com a funcionalidade desabilitada:** `<IMPACTO OU NENHUM>`

**Relação recomendada:** `Nenhuma | Depends On | Enables | ADR e especificação
preparatória`, subordinada à decisão do Arquiteto.

**Condição para nova análise:** `<MARCO MATERIAL OU NÃO APLICÁVEL>`

## Evidências encontradas

`<FONTES MATERIAIS E FATOS>`

## Impactos e restrições

`<COMPONENTES, CONTRATOS E LIMITES>`

## Incertezas e experimentos necessários

`<ITENS, INDICANDO BLOQUEANTE PRÉVIO OU EVIDÊNCIA POSTERIOR, OU NENHUM>`

## Restrições materiais não bloqueantes

`<ATÉ CINCO ITENS NECESSÁRIOS AO HANDOFF, OU NENHUMA>`

## Bloqueadores e decisões requeridas

`<ITENS RESERVADOS AO ARQUITETO OU NENHUM>`

Se a classificação for **Não pronta — pré-requisito arquitetural**, declare
por que a capacidade não é uma correção local, recomende análise arquitetural
abrangente e não incorpore a preparação à especificação funcional.

## Limitações da análise

`<ESCOPO NÃO CONFRONTADO, INDEPENDÊNCIA E EVIDÊNCIA AUSENTE>`
