# EKM — Engineering Knowledge Management

**Tipo:** Diretriz de referência

**Status:** Active

**Versão:** 1.0

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

Os dois estados são independentes.

## 6. Transações e lacunas

Mudanças relevantes usam identificadores `EKM-CHG-NNNN`. Lacunas usam `EKM-GAP-NNNN`.

Estados permitidos:

- `Open`;
- `Blocked`;
- `Superseded`;
- `Closed`.

Uma transação deve registrar baseline, objetivo, requisitos, fontes afetadas, evidências, desvios e encerramento. Uma lacuna somente é fechada quando seu critério explícito de encerramento é comprovado.

## 7. Proteção do conhecimento

- Não remover decisões vigentes.
- Não substituir documentos normativos por resumos.
- Não condensar conteúdo de modo a perder obrigação, contexto, risco ou trade-off.
- Não tratar limpeza editorial como autorização para mudança normativa.
- Marcar substituição e preservar a relação histórica.
- Declarar semanticamente toda mudança normativa no relatório.
- Obter autorização humana para remover conhecimento vigente.

## 8. Baseline e reconciliação

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

## 9. Definition of Done EKM

Uma mudança só pode ser encerrada quando:

- requisitos foram rastreados;
- implementação e conhecimento estão reconciliados;
- decisões não foram removidas silenciosamente;
- validações foram executadas ou declaradas pendentes;
- mapa e lacunas refletem o estado real;
- o relatório permite auditoria;
- operações Git e externas foram declaradas.

Build aprovado, isoladamente, não comprova conformidade EKM.

## 10. Conjunto mínimo recomendado

```text
AGENTS.md
docs/rfc/EKM-GUIDELINES.md
docs/rfc/KNOWLEDGE-MAP.md
docs/rfc/EKM-CHANGELOG.md
docs/specs/SYSTEM-DOSSIER.md
docs/specs/<especificações funcionais>.md
```

O conjunto pode crescer, mas cada novo ativo deve ter finalidade e autoridade claras.
