# EKM — Engineering Knowledge Management

**Tipo:** Diretriz de referência

**Status:** Active

**Versão:** 1.2

**Modelo EKM:** 1.5

## 1. Objetivo

Estabelecer um modelo sustentável de gestão do conhecimento de engenharia para equipes humanas e assistentes de IA.

Um repositório aderente deve preservar conhecimento suficiente para que uma equipe competente consiga:

- compreender o propósito e os comportamentos do sistema;
- modificar o sistema sem remover contratos inadvertidamente;
- auditar a conformidade entre intenção e implementação;
- recuperar decisões e regressões relevantes;
- reconstruir uma implementação funcionalmente equivalente sem depender da implementação atual como única fonte.

Reconstruibilidade não significa reproduzir o mesmo código ou binário.

## 2. Princípios

1. Conhecimento permanente pertence ao repositório, não à conversa.
2. A especificação é a unidade principal do comportamento esperado.
3. Código e testes não substituem a intenção normativa.
4. Relatórios registram evidências, mas não criam requisitos implicitamente.
5. Nenhum agente deve inventar decisões ausentes.
6. Mudanças de código e de conhecimento formam uma única transação de engenharia.
7. O baseline inclui o worktree real, não apenas o último commit.
8. Documentação deve ser proporcional ao risco e ao valor do conhecimento.
9. A adoção em legado é incremental e orientada por prioridade.
10. O método deve reduzir retrabalho e custo de contexto, não criar burocracia sem finalidade.
11. Uma especificação que depende de inferência relevante não está pronta para implementação.
12. A confiabilidade da execução exige análise de implementabilidade antes do código.
13. Versões normativas integradas à produção são imutáveis.
14. Garantias verificáveis devem evoluir de disciplina para automação, sem atribuir à ferramenta julgamento semântico humano.

## 3. Classes de fonte

### Normativa

Define obrigação vigente: especificações, contratos, arquitetura, RFCs, ADRs e diretrizes ativas.

### Histórica

Preserva decisões e estados anteriores. Não governa a implementação atual.

### Operacional

Define procedimentos de build, release, deploy, recuperação ou manutenção.

### Evidência ou relatório

Registra uma execução, teste, auditoria, incidente ou experimento.

### Informativa

Explica conceitos sem impor obrigação.

## 4. Hierarquia e conflito

```text
Princípios e decisões vigentes
→ arquitetura e contratos
→ especificações ativas
→ critérios de aceite e testes
→ implementação atual
→ relatórios, histórico e conversas
```

A hierarquia auxilia a localizar autoridade, mas não autoriza ignorar contradições. Diante de conflito normativo, o agente deve registrar a divergência, interromper o trecho afetado e solicitar decisão humana.

## 5. Especificações incrementais

Um sistema é formado por funcionalidades definidas e modificadas em momentos diferentes. A EKM não exige uma especificação monolítica.

Cada especificação deve declarar, quando aplicável:

- identificador e título;
- estado normativo e estado da implementação;
- objetivo, contexto e escopo;
- comportamento esperado;
- requisitos identificáveis;
- invariantes e contratos;
- estados, falhas e condições de borda;
- fora de escopo;
- critérios de aceite e validações;
- relações com outras fontes;
- desvios e lacunas conhecidos.

### Estado normativo

- `Draft`: em elaboração.
- `Proposed`: pronta para decisão.
- `Approved`: aprovada, ainda não necessariamente vigente.
- `Active`: fonte vigente.
- `Superseded`: substituída por fonte indicada.
- `Withdrawn`: retirada antes de vigorar.
- `Archived`: preservada apenas historicamente.

### Estado da implementação

- `Not Started`: não iniciada.
- `In Progress`: parcial.
- `Implemented`: concluída, mas sem toda a evidência exigida.
- `Validated`: critérios comprovados.
- `Regressed`: deixou de atender ao comportamento antes comprovado.
- `Blocked`: depende de decisão ou condição externa.
- `Retired`: removida intencionalmente.

### Estado da entrega

- `Not Ready`: ainda não satisfaz integração.
- `Ready for Integration`: implementação, validações e conhecimento podem seguir para integração.
- `Done`: a versão normativa e sua implementação foram integradas à referência de produção declarada pelo projeto.

Os estados normativo, de implementação e de entrega são independentes. `Implemented`, `Validated` e `Done` não são sinônimos.

### Imutabilidade em produção

Antes de `Done`, uma especificação pode ser revisada e retornar a estados anteriores. Após `Done`, sua identidade de ID e versão é imutável. Mudanças posteriores exigem nova especificação relacionada como `Amends`, `Supersedes`, `Corrects` ou `Retires`.

O mapa e o changelog registram eventos posteriores e determinam a composição normativa vigente sem reescrever a versão integrada. Cada projeto deve declarar sua referência de produção; ela não deve ser inferida pelo executor.

## 6. Technical Readiness Review e atomicidade

Antes de qualquer alteração de implementação, o executor deve analisar integralmente a especificação, as fontes relacionadas e o baseline. Deve verificar clareza, consistência, testabilidade, contratos, dependências, condições de borda, compatibilidade, validações e mudanças necessárias não autorizadas.

O resultado é binário:

- `Implementable`: o recorte inteiro pode ser executado sem inferência relevante;
- `Needs Clarification`: ao menos um requisito obrigatório depende de decisão ausente, contraditória ou ambígua.

Inferência relevante é uma escolha capaz de alterar comportamento observável, produto, arquitetura, API, protocolo, persistência, concorrência, segurança, compatibilidade, configuração operacional ou critério de aceite.

Em `Needs Clarification`:

1. nenhum item da especificação nem artefato de implementação é alterado;
2. o executor registra requisito, evidência, lacuna, decisão ausente, impacto das alternativas e ajuste recomendado;
3. o responsável corrige ou aprova a correção da especificação;
4. a análise integral é repetida;
5. somente o novo resultado `Implementable` autoriza a execução.

Implementação parcial exige divisão explícita e aprovada da especificação. Decisões mecânicas privadas continuam permitidas apenas quando comprovadamente equivalentes e sem impacto normativo.

Durante `Needs Clarification`, somente registros EKM e a correção normativa explicitamente aprovada podem ser alterados.

## 7. Transações e lacunas

Mudanças relevantes usam identificadores `EKM-CHG-NNNN`. Lacunas usam `EKM-GAP-NNNN`.

Estados permitidos:

- `Open`;
- `Blocked`;
- `Superseded`;
- `Closed`.

Uma transação deve registrar baseline, objetivo, requisitos, fontes afetadas, resultado da Technical Readiness Review, evidências, desvios e encerramento. Uma lacuna somente é fechada quando seu critério explícito de encerramento é comprovado.

## 8. Proteção do conhecimento

- Não remover decisões vigentes.
- Não substituir documentos normativos por resumos.
- Não condensar conteúdo de modo a perder obrigação, contexto, risco ou trade-off.
- Não tratar limpeza editorial como autorização para mudança normativa.
- Marcar substituição e preservar a relação histórica.
- Declarar semanticamente toda mudança normativa no relatório.
- Obter autorização humana para remover conhecimento vigente.

## 9. Baseline e reconciliação

Antes de alterar o repositório, registre:

- branch e commit;
- arquivos modificados, novos e não rastreados;
- builds e testes relevantes conhecidos;
- fontes normativas vigentes.

No encerramento, reconcilie separadamente:

1. código;
2. build e automação;
3. testes e evidências;
4. documentação normativa;
5. todas as diferenças em relação ao worktree inicial.

## 10. Definition of Ready for Integration e Done

`Ready for Integration` exige requisitos atendidos, validações obrigatórias aprovadas, implementação e conhecimento reconciliados, ausência de bloqueios e evidência auditável.

`Done` exige ainda integração da versão normativa e da implementação à referência de produção declarada. Pendência obrigatória impede ambos os estados.

## 11. Definition of Done da transação EKM

Uma mudança só pode ser encerrada quando:

- uma Technical Readiness Review válida autorizou a implementação antes da primeira alteração de implementação;
- requisitos foram rastreados;
- implementação e conhecimento estão reconciliados;
- decisões não foram removidas silenciosamente;
- validações foram executadas ou declaradas pendentes;
- mapa e lacunas refletem o estado real;
- o relatório permite auditoria;
- operações Git e externas foram declaradas.

Build aprovado, isoladamente, não comprova conformidade EKM.

Mudanças funcionais sob o modelo 1.5 somente encerram a transação em `Done`. Investigações e governança podem possuir critério aprovado próprio sem declarar entrega funcional.

## 12. Automação e garantias previstas

A EKM prevê um futuro `EKM Gate` para verificar automaticamente regras comprováveis antes da integração, reduzindo dependência de disciplina individual. São candidatos: estrutura e metadados, relações normativas, imutabilidade em produção, evidência de Technical Readiness, rastreabilidade, estados e reconciliação.

O Gate permanece `Planned / Not Defined`. Arquitetura, schema, ferramenta, política de bloqueio e implantação ainda exigem especificação própria e experimentos. Nenhum projeto pode alegar garantia automatizada apenas por adotar estas diretrizes. Completude semântica e intenção permanecem responsabilidade humana.

## 13. Conjunto mínimo recomendado

```text
AGENTS.md
docs/rfc/EKM-GUIDELINES.md
docs/rfc/KNOWLEDGE-MAP.md
docs/rfc/EKM-CHANGELOG.md
docs/specs/SYSTEM-DOSSIER.md
docs/specs/<especificações funcionais>.md
```

O conjunto pode crescer, mas cada novo ativo deve ter finalidade e autoridade claras.
