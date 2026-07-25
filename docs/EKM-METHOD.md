# EKM — Gestão do Conhecimento de Engenharia

**Classe da fonte:** Normativa

**Estado da fonte:** Vigente

**Versão do documento:** 1.5

**Versão do modelo EKM:** 1.8

**Maturidade do modelo:** Experimental e utilizável

## 1. Objetivo

Estabelecer um modelo sustentável de governança e gestão do conhecimento de
engenharia para equipes humanas e assistentes de IA.

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
7. O estado de referência inclui a árvore de trabalho real, não apenas o último
   commit.
8. Documentação deve ser proporcional ao risco e ao valor do conhecimento.
9. A adoção em legado é incremental e orientada por prioridade.
10. O método deve reduzir retrabalho e custo de contexto, não criar burocracia sem finalidade.
11. Uma especificação que depende de inferência relevante não está pronta para implementação.
12. A confiabilidade da execução exige análise de implementabilidade antes do código.
13. Versões normativas integradas à produção são imutáveis.
14. Garantias verificáveis devem evoluir de disciplina para automação, sem atribuir à ferramenta julgamento semântico humano.
15. A EKM busca autonomia governada: decisões relevantes e responsabilidade
    final permanecem humanas.
16. Interações humanas de decisão, aprovação e validação são controles do
    método; somente coordenação operacional desnecessária deve ser reduzida.
17. A modalidade de autoria fica fora do contrato; a EKM não prevê automação da
    especificação.
18. Uma especificação somente segue para análise de implementabilidade após
    parecer humano explícito sobre sua intenção.

### 2.1 Linguagem normativa e vocabulário controlado

O português do Brasil é o idioma normativo canônico da EKM. Termos em outro
idioma não criam significado normativo por si próprios.

As palavras abaixo possuem força controlada:

- **DEVE** e **NÃO DEVE** expressam obrigação ou proibição;
- **PODE** expressa permissão; capacidade técnica deve ser descrita como
  “é capaz de”;
- **RECOMENDA-SE** expressa orientação não obrigatória;
- **NÃO SE APLICA** exige motivo e evidência que identifiquem a condição de
  dispensa.

Expressões como “quando aplicável”, “relevante”, “material”, “suficiente” e
“adequado” somente podem impor ou dispensar uma obrigação quando o critério, a
evidência ou a autoridade responsável estiverem declarados.

Nomes de ferramentas, comandos, arquivos, APIs, protocolos, padrões externos e
identificadores estáveis podem permanecer no idioma original, sempre
delimitados como código ou apresentados como alias. A prosa que explica sua
semântica permanece em português.

| Conceito canônico | Identificador ou alias legado |
|---|---|
| Revisão de implementabilidade | `Technical Readiness Review` |
| Ponto de controle | `gate` |
| Transferência de responsabilidade | `handoff` |
| Marco versionado | `checkpoint` |
| Estado de referência | `baseline` |
| Árvore de trabalho | `worktree` |
| Responsabilidade pelo documento ou registro | `ownership` |
| Somente leitura | `read-only` |
| Modelo reutilizável | `template` |
| Histórico de mudanças | `changelog` |
| Processo de construção | `build` |
| Publicação de versão | `release` |
| Implantação | `deploy` |
| Execução do sistema | `runtime` |
| Fluxo de promoção ou automação | `pipeline` |
| Relação de ganhos e perdas | `trade-off` |
| Critérios de prontidão para integração | `Definition of Ready for Integration` |
| Critérios de conclusão | `Definition of Done` |
| Líder Técnico | `Tech Lead` |

Os valores ingleses de estados e resultados permanecem aceitos como
identificadores legados no modelo 1.8. Documentos novos devem apresentar o
rótulo canônico em português e, quando necessário para compatibilidade, o
identificador legado entre colchetes ou código.

| Contexto | Rótulos canônicos e identificadores legados |
|---|---|
| Parecer humano da intenção | Intenção aceita [`Accepted`], revisão necessária [`Revision Required`], pendente [`Pending`] |
| Admissão de uma etapa | Admitido [`Accepted`], marco bloqueado [`Checkpoint Blocked`], pendente [`Pending`] |
| Revisão de implementabilidade | Implementável [`Implementable`], precisa de esclarecimento [`Needs Clarification`] |
| Autorização para implementar | Autorizada [`Approved`], rejeitada [`Rejected`], pendente [`Pending`] |
| Auditoria | Conforme [`Compliant`], não conforme [`Non-compliant`], não verificável [`Not verifiable`], bloqueada [`Blocked`], não aplicável [`Not Applicable`] |

Um resultado deve ser escrito com seu contexto. Não use isoladamente
`Accepted`, `Pending` ou `Blocked` quando houver mais de uma interpretação
possível. “Pendente” representa uma decisão ainda não emitida; revisão não
iniciada deve ser registrada como “não executada”, e referência que só poderá
ser preenchida no marco seguinte deve ser registrada como “a registrar no
próximo marco”.

## 3. Classes de fonte

### Normativa

Define obrigação vigente: especificações, contratos, arquitetura, RFCs, ADRs e diretrizes ativas.

### Histórica

Preserva decisões e estados anteriores. Não governa a implementação atual.

### Operacional

Define procedimentos de construção, publicação de versão, implantação,
recuperação ou manutenção.

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

A modalidade de confecção fica fora do contrato da EKM. O método não prevê nem
exige automação da autoria; governa o conteúdo, a autoridade e os pontos de
controle do
artefato resultante.

### Estado normativo

- Rascunho [`Draft`]: em elaboração.
- Proposta [`Proposed`]: pronta para decisão.
- Aprovada [`Approved`]: aprovada, ainda não necessariamente vigente.
- Vigente [`Active`]: fonte vigente.
- Substituída [`Superseded`]: substituída por fonte indicada.
- Retirada [`Withdrawn`]: retirada antes de vigorar.
- Arquivada [`Archived`]: preservada apenas historicamente.

### Estado da implementação

- Não iniciada [`Not Started`].
- Em andamento [`In Progress`]: parcial.
- Implementada [`Implemented`]: concluída, mas sem toda a evidência exigida.
- Validada [`Validated`]: critérios comprovados.
- Regredida [`Regressed`]: deixou de atender ao comportamento antes comprovado.
- Bloqueada [`Blocked`]: depende de decisão ou condição externa.
- Descontinuada [`Retired`]: removida intencionalmente.

### Estado da entrega

- Não pronta [`Not Ready`]: ainda não satisfaz integração.
- Pronta para integração [`Ready for Integration`]: implementação, validações e conhecimento podem seguir para integração.
- Concluída [`Done`]: a versão normativa e sua implementação foram integradas à referência de produção declarada pelo projeto.

Os estados normativo, de implementação e de entrega são independentes.
Implementada [`Implemented`], Validada [`Validated`] e Concluída [`Done`] não
são sinônimos.

### Parecer humano da especificação

Ao concluir a autoria, a especificação fica Proposta [`Proposed`] e registra o parecer
humano como Pendente [`Pending`]. Antes da revisão de implementabilidade, o
arquiteto ou outro
responsável humano autorizado deve emitir:

- Intenção aceita [`Accepted`]: a especificação representa a intenção conhecida e pode seguir
  para análise técnica;
- Revisão necessária [`Revision Required`]: a especificação retorna à autoria;
- Pendente [`Pending`]: nenhuma decisão foi emitida.

O parecer deve registrar responsável, data, marco versionado e ressalvas. Ele não
declara implementabilidade nem autoriza alteração de código.

Esse controle é inicialmente declarativo. A EKM exige evidência explícita, não
permite que um agente presuma ou fabrique a decisão e não alega verificar
automaticamente identidade, autenticidade ou autoridade.

### Imutabilidade em produção

Antes de Concluída [`Done`], uma especificação pode ser revisada e retornar a
estados anteriores. Após Concluída, sua identidade de ID e versão é imutável.
Mudanças posteriores exigem nova especificação relacionada pelos identificadores
`Amends`, `Supersedes`, `Corrects` ou `Retires`.

O mapa e o histórico de mudanças registram eventos posteriores e determinam a
composição normativa vigente sem reescrever a versão integrada. Cada projeto
deve declarar sua referência de produção; ela não deve ser inferida pelo
executor.

## 6. Revisão de implementabilidade e atomicidade

Depois do parecer humano de Intenção aceita [`Accepted`] e antes de qualquer alteração de
implementação, o revisor deve analisar integralmente a especificação, as fontes
relacionadas e o estado de referência. Deve verificar se o contrato aceito é passível de
implementação sem inferência relevante, confrontando consistência,
testabilidade, contratos, dependências, condições de borda, compatibilidade,
validações e mudanças necessárias não autorizadas.

A revisão não decide se a funcionalidade é desejável, não redefine intenção e
não aprova a própria especificação.

O resultado é binário:

- Implementável [`Implementable`]: o recorte inteiro pode ser executado sem inferência relevante;
- Precisa de esclarecimento [`Needs Clarification`]: ao menos um requisito obrigatório depende de decisão ausente, contraditória ou ambígua.

Inferência relevante é uma escolha capaz de alterar comportamento observável, produto, arquitetura, API, protocolo, persistência, concorrência, segurança, compatibilidade, configuração operacional ou critério de aceite.

### 6.1 Completude cumulativa

Encontrar uma lacuna bloqueia imediatamente qualquer intenção de implementação,
mas não encerra a revisão de implementabilidade. O revisor deve continuar até
classificar todos os requisitos e dimensões obrigatórias do recorte.

A revisão deve verificar, além dos requisitos identificáveis:

- precondições confrontadas com o estado de referência;
- estados normativo, de implementação e de entrega;
- APIs e ciclo de vida;
- dependências e configuração;
- compatibilidade e regressões;
- viabilidade das validações e critérios de aceite.

O resultado deve ser sustentado por uma matriz com:

| Campo | Valores ou conteúdo |
|---|---|
| Requisito ou dimensão | Identificador ou aspecto transversal |
| Resultado | Suportado [`Supported`], Lacuna [`Gap`], Conflito [`Conflict`] ou Não aplicável [`Not Applicable`] |
| Evidência | Fato verificável do estado de referência |
| Lacuna ou impacto | Consequência técnica ou normativa |
| Decisão necessária | Decisão humana pendente ou Nenhuma [`None`] |

Nenhum requisito pode ficar sem classificação. Uma revisão encerrada no primeiro bloqueio não é integral.

### 6.2 Separação entre revisão, aprovação e implementação

A revisão de implementabilidade e a implementação devem ocorrer em execuções
separadas, ainda que sejam realizadas pelo mesmo agente.

A execução da revisão deve registrar especificação, branch, commit e estado real
da árvore de trabalho, produzir a matriz completa e encerrar sem alterar
implementação, inclusive quando o resultado for Implementável [`Implementable`].

Implementável [`Implementable`] significa apto para aprovação humana; não
constitui autorização autônoma. A implementação somente pode começar após
aprovação explícita do responsável para a revisão e o estado de referência
registrados.

Antes da primeira alteração, o executor deve reconfirmar que:

- a especificação não sofreu mudança material;
- o parecer humano de Intenção aceita [`Accepted`] permanece aplicável ao marco
  versionado;
- branch, commit e árvore de trabalho permanecem compatíveis com o estado de
  referência revisado;
- a revisão aprovada permanece Implementável [`Implementable`];
- a transação aplicável está Aberta [`Open`].

Mudança material invalida parecer, revisão e autorização. Exige novo parecer
humano e nova revisão integral. Precisa de esclarecimento
[`Needs Clarification`] deve ser reportado como bloqueio, nunca como
implementação concluída.

Esses controles são manuais no modelo 1.8 e não dependem de múltiplos agentes,
CI/CD ou `EKM Gate`.

Quando o resultado for Precisa de esclarecimento [`Needs Clarification`]:

1. nenhum item da especificação nem artefato de implementação é alterado;
2. o executor registra requisito, evidência, lacuna, decisão ausente, impacto das alternativas e ajuste recomendado;
3. o responsável corrige ou aprova a correção da especificação;
4. um novo parecer humano de Intenção aceita [`Accepted`] confirma a intenção
   do marco versionado
   corrigido;
5. a análise integral é repetida;
6. somente o novo resultado Implementável [`Implementable`], seguido de aprovação humana
   explícita e reconfirmação do estado de referência, autoriza a execução.

Implementação parcial exige divisão explícita e aprovada da especificação. Decisões mecânicas privadas continuam permitidas apenas quando comprovadamente equivalentes e sem impacto normativo.

Durante Precisa de esclarecimento [`Needs Clarification`], somente registros EKM
e a correção normativa explicitamente aprovada podem ser alterados.

## 7. Transações e lacunas

Mudanças relevantes usam identificadores `EKM-CHG-NNNN`. Lacunas usam `EKM-GAP-NNNN`.

Estados permitidos:

- Aberta [`Open`];
- Bloqueada [`Blocked`];
- Substituída [`Superseded`];
- Fechada [`Closed`].

Uma transação deve registrar estado de referência, objetivo, requisitos, fontes
afetadas, parecer humano da especificação, resultado da revisão de
implementabilidade,
autorização para implementação, evidências, desvios e encerramento. Uma lacuna
somente é fechada quando seu critério explícito de encerramento é comprovado.

## 8. Proteção do conhecimento

- Não remover decisões vigentes.
- Não substituir documentos normativos por resumos.
- Não condensar conteúdo de modo a perder obrigação, contexto, risco ou relação
  de ganhos e perdas.
- Não tratar limpeza editorial como autorização para mudança normativa.
- Marcar substituição e preservar a relação histórica.
- Declarar semanticamente toda mudança normativa no relatório.
- Obter autorização humana para remover conhecimento vigente.

## 9. Baseline e reconciliação

Antes de alterar o repositório, registre:

- branch e commit;
- arquivos modificados, novos e não rastreados;
- processos de construção e testes relevantes conhecidos;
- fontes normativas vigentes.

No encerramento, reconcilie separadamente:

1. código;
2. construção e automação;
3. testes e evidências;
4. documentação normativa;
5. todas as diferenças em relação à árvore de trabalho inicial.

## 10. Critérios de prontidão para integração e conclusão

Pronta para integração [`Ready for Integration`] exige requisitos atendidos,
validações obrigatórias aprovadas, implementação e conhecimento reconciliados,
ausência de bloqueios e evidência auditável.

Concluída [`Done`] exige ainda integração da versão normativa e da implementação
à referência de produção declarada. Pendência obrigatória impede ambos os
estados.

## 11. Critérios de conclusão da transação EKM

Uma mudança só pode ser encerrada quando:

- o parecer humano da especificação foi registrado antes da revisão de
  implementabilidade;
- uma revisão de implementabilidade válida e uma autorização humana explícita
  precederam a primeira alteração de implementação;
- requisitos foram rastreados;
- implementação e conhecimento estão reconciliados;
- decisões não foram removidas silenciosamente;
- validações foram executadas ou declaradas pendentes;
- mapa e lacunas refletem o estado real;
- o relatório permite auditoria;
- operações Git e externas foram declaradas.

Build aprovado, isoladamente, não comprova conformidade EKM.

Mudanças funcionais sob o modelo 1.8 somente encerram a transação em Concluída
[`Done`].
Investigações e governança podem possuir critério aprovado próprio sem declarar
entrega funcional.

## 12. Automação e garantias previstas

A EKM prevê um futuro ponto de controle EKM (`EKM Gate`) para verificar automaticamente regras
comprováveis antes da integração, reduzindo dependência de disciplina
individual. São candidatos: estrutura e metadados, presença declarada do
parecer humano, relações normativas, imutabilidade em produção, evidência de
implementabilidade, rastreabilidade, estados e reconciliação.

O ponto de controle permanece planejado e não definido
[`Planned / Not Defined`]. Arquitetura, esquema, ferramenta,
política de bloqueio e implantação ainda exigem especificação própria e
experimentos. Nenhum projeto pode alegar garantia automatizada apenas por adotar
estas diretrizes. Completude semântica, intenção e autenticidade do parecer
permanecem responsabilidade humana. A EKM não prevê automação obrigatória para
a confecção da especificação.

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
