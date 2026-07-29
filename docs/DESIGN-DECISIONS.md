# Decisões de desenho da EKM

Este documento registra as razões das principais escolhas do modelo atual. Não substitui as diretrizes operacionais.

## DD-001 — Especificação como unidade de comportamento

**Decisão:** funcionalidades e contratos preserváveis devem ser representados por especificações incrementais.

**Motivo:** comportamentos surgem em momentos diferentes; um documento monolítico seria difícil de manter e incentivaria inferências.

## DD-002 — Não existe um único documento da verdade

**Decisão:** a verdade é distribuída por fontes com responsabilidades explícitas e conectadas por um mapa.

**Motivo:** comportamento, motivação, execução e evidência têm ciclos de vida e autoridades diferentes.

## DD-003 — Dossiê é visão geral, não substituto

**Decisão:** o dossiê facilita navegação e entendimento inicial, mas aponta para especificações especializadas.

**Motivo:** duplicar detalhes cria fontes concorrentes e divergência.

## DD-004 — Estados normativo e de implementação independentes

**Decisão:** cada especificação declara sua autoridade e, separadamente, a situação da implementação.

**Motivo:** uma especificação pode estar vigente sem estar implementada; uma implementação pode existir sem validação suficiente ou estar regredida.

## DD-005 — Transações e lacunas têm identidade própria

**Decisão:** mudanças usam `EKM-CHG-NNNN`; ausências de conhecimento usam `EKM-GAP-NNNN`.

**Motivo:** tarefas concluídas e conhecimento faltante precisam permanecer rastreáveis sem depender de conversas ou listas informais.

## DD-006 — O estado de referência é a árvore de trabalho observada

**Estado:** substituída por DD-019 no modelo 1.9.

**Decisão:** a comparação inclui alterações rastreadas, não rastreadas e preexistentes, não apenas `HEAD`.

**Motivo:** Git identifica commits, mas uma tarefa pode começar sobre trabalho ainda não consolidado.

## DD-007 — Relatório não é fonte normativa

**Decisão:** relatórios registram evidências e desvios, mas não criam ou alteram requisitos implicitamente.

**Motivo:** um relatório descreve uma execução específica e pode omitir consequências semânticas.

## DD-008 — Specification on touch

**Decisão:** ao modificar uma funcionalidade relevante ainda não especificada, seu domínio deve atingir ao menos `Specified`.

**Motivo:** documentar todo o legado de uma vez é caro; não documentar o que muda perpetua perda de conhecimento.

## DD-009 — `Active` exige autoridade humana ou inequívoca

**Decisão:** comportamento descoberto no código não deve virar requisito vigente apenas por inferência do agente.

**Motivo:** o código pode conter bugs, acidentes históricos, compatibilidade obsoleta ou experimentos.

## DD-010 — Autonomia proporcional à certeza

**Decisão:** agentes avançam autonomamente em descobertas e análises verificáveis. Em uma implementação regida por uma especificação atômica, qualquer requisito obrigatório dependente de julgamento bloqueia o recorte inteiro antes da primeira alteração.

**Motivo:** adoção e investigação podem ser incrementais, mas implementar parcialmente uma especificação incompleta rompe a unidade de delegação e permite decisões normativas silenciosas.

## DD-011 — Estrutura mínima antes de expansão

**Decisão:** começar com `AGENTS.md`, mapa, histórico de mudanças, dossiê e
especificações necessárias. Uma diretriz local só é criada quando não existe
referência externa aplicável ou há regras próprias.

**Motivo:** padronização facilita adoção, mas arquivos sem autoridade ou uso claro criam burocracia.

## DD-012 — Revisão de implementabilidade obrigatória

**Decisão:** toda especificação deve receber resultado Implementável
[`Implementable`] ou Precisa de esclarecimento [`Needs Clarification`] antes de
qualquer alteração de implementação.

**Motivo:** um processo de construção funcional pode esconder uma decisão
inferida que não corresponde à intenção. Concentrar lacunas antes do código
aumenta a confiabilidade e permite execução posterior verdadeiramente autônoma.

## DD-013 — Versões normativas em produção são imutáveis

**Decisão:** após `Done`, alterações de comportamento usam nova especificação relacionada, sem reescrever a versão integrada.

**Motivo:** reescrever uma especificação de produção destrói a correspondência histórica entre intenção, implementação e evidência.

## DD-014 — Garantias automatizadas são uma capacidade futura

**Estado:** preservada como decisão histórica; fora do escopo do modelo 1.9.

**Decisão:** prever um `EKM Gate`, sem definir prematuramente sua arquitetura ou alegar garantia ainda inexistente.

**Motivo:** regras verificáveis não devem depender apenas de disciplina, mas a automação precisa nascer de requisitos e experimentos próprios e não substitui julgamento semântico humano.

## DD-015 — Revisão não autoriza a própria implementação

**Estado:** parcialmente substituída por DD-018 e DD-020 no modelo 1.9.

**Decisão:** a revisão de implementabilidade é cumulativa, ocorre em execução
separada da implementação e produz uma recomendação submetida ao responsável
humano. Mesmo Implementável [`Implementable`] exige aprovação explícita e
reconfirmação do estado de referência antes da primeira alteração.

**Motivo:** o mesmo executor pode encontrar um bloqueio suficiente e interromper
prematuramente a investigação, deixando outras lacunas sem registro. Também
existe conflito de responsabilidade quando o agente produz e consome sua própria
autorização. A separação manual preserva o protagonismo humano sem exigir
prematuramente múltiplos agentes ou fluxo automatizado.

## DD-016 — Governança e parecer humano precedem implementabilidade

**Estado:** substituída por DD-018 no modelo 1.9.

**Decisão:** a EKM busca autonomia governada, não autonomia máxima. A modalidade
de confecção da especificação fica fora do contrato e sua automação não é
prevista como requisito ou capacidade do método. O artefato somente segue para
revisão de implementabilidade após parecer humano explícito de que representa a
intenção conhecida.

Esse parecer é diferente tanto do resultado técnico `Implementable` quanto da
autorização humana posterior para alterar o código. Inicialmente, seu registro é
declarativo e não implica verificação automatizada de identidade ou autoridade.

**Motivo:** o Engenheiro Analista deve avaliar se um contrato aceito é passível
de implementação, não decidir o que o produto deve fazer. Interação humana em
decisões, aprovações e validações é governança esperada; o que deve ser reduzido
é retrabalho e coordenação operacional sem valor decisório.

## DD-017 — Português canônico e identificadores legados explícitos

**Decisão:** o português do Brasil é o idioma normativo canônico da EKM.
Termos técnicos externos e identificadores legados podem ser preservados, mas
devem possuir significado canônico em português e aparecer delimitados como
identificadores.

Resultados sobre intenção, admissão, implementabilidade, autorização,
implementação e auditoria devem declarar seu contexto. Um mesmo identificador
legado não autoriza tratar decisões diferentes como equivalentes.

**Motivo:** a mistura não controlada de português e inglês, somada ao uso
contextualmente diferente de valores como `Accepted`, `Pending` e `Blocked`,
aumenta ambiguidade para pessoas, agentes e futuras automações. Traduzir
comandos, APIs ou identificadores de forma indiscriminada também reduziria a
precisão e quebraria compatibilidade. A separação entre rótulo normativo e
identificador preserva clareza e migração gradual.

## DD-018 — Autoridade do Arquiteto e ordem como autorização

**Decisão:** o Arquiteto humano sempre prevalece sobre decisões e recomendações
dos agentes. Cada tarefa é iniciada por ordem do Arquiteto, por prompt ou
pipeline, e essa ordem autoriza a etapa e o recorte solicitados. Não se exige um
segundo registro declarativo de aceite, identidade, data ou marco Git para
repetir a autorização.

A autoridade humana não reescreve fatos: falhas e limitações observadas
permanecem registradas. Se a decisão mudar o comportamento esperado, a
especificação é atualizada.

**Motivo:** o piloto mostrou que múltiplos pareceres documentais repetiam uma
decisão que já estava presente na própria ação do Arquiteto. Preservar a
autoridade sem duplicar sua ordem reduz carga cognitiva e mantém claro quem
decide.

## DD-019 — Git como trilha técnica e entrega obrigatória

**Decisão:** o Git é a fonte da linhagem técnica. SHA, branch de origem, mensagem
de commit e checkpoints não são campos obrigatórios em documentos EKM.

Cada tarefa de agente deve começar com árvore limpa, produzir resultado material
e terminar com commit, push e árvore limpa. Falha no push significa que a etapa
não foi entregue. A ordem normal não autoriza force push, reescrita de
histórico, merge, tag, release ou deploy.

**Motivo:** copiar metadados do Git para o changelog não agrega entendimento
humano e cria divergência e manutenção manual. Em contrapartida, commit e push
são necessários para que o resultado do agente exista de forma versionada e
possa alimentar a próxima etapa.

## DD-020 — Governança proporcional e estado como passagem

**Decisão:** a especificação contém o estado necessário para a etapa seguinte.
O changelog registra apenas decisões, lacunas, evidências materiais e resultado.
Matrizes extensas, revisão técnica independente e auditoria de integridade são
usadas somente quando o Arquiteto considerar que agregam confiança ao recorte.

Ao encontrar uma lacuna bloqueante clara, a análise pode encerrar sem buscar uma
classificação exaustiva. Itens materiais já descobertos devem ser agrupados.

**Motivo:** o protocolo anterior tornou cada transferência auditável, mas
introduziu formulários, checkpoints, papéis universais e repetição sem benefício
proporcional. A dose inicial deve proteger conhecimento e decisão enquanto
permite experimentar, entregar e descartar hipóteses rapidamente.

## DD-021 — Pipeline somente como ordem lógica

**Decisão:** o fluxo atual é uma sequência de etapas comandadas pelo Arquiteto.
O modelo 1.9 não incorpora concorrência, locks, filas ou mecanismos de
orquestração, e esses conceitos não participam dos experimentos atuais.

**Motivo:** não se deve adicionar ao processo uma preocupação ainda não adotada.
Antecipá-la criaria regras e custo antes de existir evidência de utilidade.

## DD-022 — Fluxo iniciado em branch derivada da `main`

**Decisão:** todo fluxo de trabalho deve começar em uma branch de trabalho
derivada da `main`, nunca diretamente na `main`. A mesma branch pode atravessar
as etapas autorizadas do recorte; não se exige uma branch nova por atuação.

**Motivo:** usar a `main` como origem comum torna explícito o baseline de
produção, preserva a linhagem da mudança e mantém o trabalho isolado até a
decisão humana de integração, sem duplicar metadados do Git nos documentos EKM.

## DD-023 — Modelo de atores como fluxo oficial

**Decisão:** a EKM 1.11 organiza cada tarefa por um papel explicitamente
selecionado na ordem do Arquiteto. O agente lê as regras comuns, exatamente um
perfil correspondente, a especificação indicada e somente as fontes técnicas
pertinentes.

Os atores oficiais são Autor da Especificação, Engenheiro Analista, Engenheiro
Implementador e Engenheiro Revisor. Cada ator atualiza o conhecimento afetado,
promove somente os estados sustentados por sua etapa e entrega o resultado por
commit e push. Não existe um ator adicional destinado apenas a reconciliar ou
versionar o trabalho dos demais.

O Engenheiro Revisor pode registrar validação do Tech Lead, aprovação do
Arquiteto e confirmação de integração quando essas decisões já tiverem sido
fornecidas explicitamente. Ele não produz aprovação própria nem substitui a
autoridade humana.

**Motivo:** o ciclo completo no aplicativo iotsmarthome demonstrou que prompts
curtos e perfis referenciados conseguem dirigir agentes e modelos diferentes,
preservando continuidade por meio da especificação, dos estados e do Git. O
mesmo caso mostrou que papéis incompatíveis e regras genéricas favorecem
promoções incorretas e reinterpretações. Tornar responsabilidades e passagens
explícitas aumenta aderência sem criar um ator burocrático de reconciliação.

## DD-024 — O Autor investiga e propõe sem revisar a própria implementabilidade

**Decisão:** o Autor da Especificação pode analisar um problema complexo,
inspecionar fontes técnicas, comparar alternativas e propor uma solução
arquitetural e implementável. Não é criado um papel adicional de coautoria.

Essa decisão rejeita um coautor dentro do fluxo funcional. Ela não impede um
papel institucional de apoio ao Arquiteto fora desse fluxo, posteriormente
definido por `DD-026`.

O Autor separa fatos observados, intenção e decisões confirmadas, solução
proposta e decisões pendentes. Recomendações permanecem subordinadas ao
Arquiteto. A própria autoria não produz `Implementable`: a revisão de
implementabilidade continua pertencendo a uma atuação independente do
Engenheiro Analista.

**Alternativas consideradas:**

- criar um Coautor ou Especialista de Solução formal foi rejeitado porque
  duplicaria a responsabilidade do Autor e acrescentaria passagem operacional;
- limitar o Autor à transcrição de requisitos foi rejeitado porque problemas
  transversais exigem investigação e desenho antes de formarem um contrato
  implementável;
- permitir que o Autor aprovasse a própria implementabilidade foi rejeitado
  porque eliminaria a verificação independente e misturaria produção e
  autorização do contrato;
- tratar o Autor como Autor/Analista foi rejeitado porque tornaria ambíguo qual
  atuação sustenta `Implementable`.

**Motivo:** o perfil anterior já exigia uma especificação implementável, mas
não explicitava que a investigação e a proposição de solução pertenciam à
autoria. Essa ambiguidade permitia tanto uma autoria superficial quanto a
criação de decisões pendentes artificiais para escolhas opcionais. Um
experimento anterior registrou sobreposição parcial da autoria com a revisão de
implementabilidade e lacunas artificiais; o início do experimento de remoção de
dados sensíveis tornou explícita a hipótese de que a autoria de um problema
transversal precisa formular uma solução, não apenas reproduzir a intenção
inicial.

Essa primeira autoria ainda não foi avaliada pelo Arquiteto e não constitui
evidência de sucesso da decisão. Ela motivou o esclarecimento normativo que será
confrontado nas etapas seguintes.

**Riscos para reavaliação:**

- o Autor pode apresentar recomendação como decisão confirmada;
- pode devolver escolhas técnicas resolvíveis como falsas decisões do
  Arquiteto;
- pode produzir proposta enviesada que o Analista apenas ratifique;
- a separação conceitual pode não ser suficiente para preservar independência
  quando agentes compartilham contexto.

A decisão deve ser reavaliada se os experimentos mostrarem autoaprovação,
aumento de decisões artificiais, perda de independência da análise ou
necessidade recorrente de um especialista com responsabilidade realmente
distinta. A motivação e estes critérios permanecem neste registro de desenho,
fora das fontes carregadas pelos atores em uma tarefa funcional normal; o
perfil contém somente a regra operacional necessária.

## DD-025 — Objetivos multi-contexto usam coordenação por especificações

**Decisão:** quando um objetivo depende de fontes e implementações mantidas em
repositórios, serviços, aplicativos ou infraestruturas independentes, a EKM usa
uma especificação coordenadora para o resultado ponta a ponta e especificações
subordinadas executáveis em cada contexto de entrega.

A especificação coordenadora registra decisões arquiteturais, relações,
dependências e critérios de integração. Cada especificação subordinada
permanece junto às fontes que governam sua implementação, percorre o fluxo
normal de atores e promove somente os próprios estados. A conclusão de um
recorte não promove automaticamente os demais nem comprova o objetivo
coordenado; este exige evidência de integração dos recortes obrigatórios.

As relações registram identificadores, fontes responsáveis, dependências e
estados materiais. Não duplicam especificações externas nem transcrevem a
linhagem preservada pelo Git.

**Motivo:** a análise da remoção de dados sensíveis do `iotsmarthome` mostrou
que o resultado depende primeiro de mudanças no provedor OAuth/OIDC, nas APIs
protegidas e no contrato de configuração, além da posterior migração do
aplicativo. Tratar tudo como uma única especificação local permitiria que um
ator do app inferisse contratos externos ou declarasse um resultado impossível
de validar naquele repositório. Tratar cada mudança isoladamente, sem uma fonte
coordenadora, perderia o objetivo arquitetural que dá sentido aos recortes.

**Alternativas consideradas:**

- ampliar a especificação do aplicativo para autorizar mudanças em todos os
  repositórios foi rejeitado por misturar fontes, autoridades e ciclos de
  integração independentes;
- criar um novo Coordenador como ator obrigatório foi rejeitado porque o
  Arquiteto já dirige as atuações e as especificações podem preservar as
  relações materiais;
- usar apenas uma lista informal de tarefas foi rejeitado porque não preserva
  contratos, decisões nem critérios de conclusão ponta a ponta;
- exigir sincronização automática, locks ou estado distribuído foi rejeitado
  por antecipar mecanismos ainda não adotados.

**Aplicação proporcional:** a estrutura só é usada quando existe dependência
material entre contextos de entrega. Uma mudança inteiramente local continua
com uma única especificação e o fluxo normal.

**Critérios de reavaliação:** reavaliar se a coordenação duplicar conhecimento,
criar manutenção manual sem apoiar decisões, tornar ambígua a autoridade dos
estados ou não permitir verificar a integração ponta a ponta.

## DD-026 — Consultor de Arquitetura como apoio institucional subordinado

**Decisão:** a EKM institui o Consultor de Arquitetura como papel de IA que
apoia o Arquiteto e o Tech Lead em atividades transversais. O Arquiteto
permanece o ator principal e a única autoridade final sobre intenção,
arquitetura, risco, autorização, validação e integração.

O Consultor pode investigar, propor e executar documentação, código, testes,
configuração, análise, revisão ou coordenação somente dentro de ordem explícita
do Arquiteto. O papel não concede permissão implícita para qualquer dessas
operações e não transforma a IA em aprovadora das próprias recomendações.

Antes do commit final, o Consultor apresenta e recebe confirmação explícita do
Arquiteto sobre um registro que identifica ordem, recorte, operações, decisões
confirmadas, resultado e limitações. Essa confirmação não equivale a aprovação
técnica, validação ou integração, salvo quando o Arquiteto atribuir
explicitamente esse significado.

**Relação com decisões anteriores:**

- `DD-018` continua válida para os atores funcionais; o registro adicional do
  Consultor é uma exceção proporcional à amplitude de sua atuação;
- `DD-023` continua definindo somente quatro atores no pipeline;
- `DD-024` continua rejeitando um coautor dentro da autoria funcional;
- `DD-025` continua coordenando objetivos multi-contexto por especificações,
  sem transformar o Consultor em orquestrador ou fonte global de estado.

**Salvaguardas:**

- cada ordem identifica resultado, repositório, recorte e operações;
- ampliações materiais exigem nova confirmação antes da ação;
- decisões propostas só se tornam confirmadas por manifestação do Arquiteto;
- o Tech Lead não delega autoridade reservada sem delegação explícita;
- participação anterior impede alegação posterior de independência no mesmo
  recorte;
- ações destrutivas, merge, release e deploy mantêm autorização específica;
- o registro final é confirmado antes do commit e preservado na fonte
  materialmente apropriada.

**Alternativas consideradas:**

- manter a colaboração arquitetural apenas informal foi rejeitado porque
  decisões e autorizações ficariam dependentes da conversa;
- tornar o Consultor um quinto ator sequencial foi rejeitado porque apoio
  transversal não corresponde a uma etapa única;
- conceder autorização ampla por definição do papel foi rejeitado porque
  inverteria a autoridade e ampliaria silenciosamente o escopo;
- obrigar o Consultor a trocar de papel para toda contribuição foi rejeitado
  porque impediria coautoria de governança e arquitetura, embora promoções
  formais continuem pertencendo aos atores;
- dispensar o registro final foi rejeitado porque a amplitude do papel exige
  tornar localizável o que o Arquiteto efetivamente autorizou e confirmou.

**Motivo:** decisões de arquitetura, evolução da EKM e apoio ao Tech Lead já
são discutidos com IA, mas o modelo não possuía um papel institucional para
essa colaboração. Ordens ad hoc tornavam ambíguos o recorte permitido, a
autoridade humana preservada e o valor probatório da participação da IA.

**Critérios de reavaliação:** reduzir ou retirar o papel se o registro final
virar formalidade sem apoiar decisão, se surgir autorização genérica, se o
Consultor obscurecer a responsabilidade dos atores, se a confirmação humana
for confundida com validação ou se a participação transversal comprometer
revisões independentes.

### Registro inaugural da atuação

**Estado da confirmação final:** Confirmada pelo Arquiteto.

O Arquiteto confirmou o registro inaugural e autorizou o commit e o push do
resultado preparado. A confirmação não declarou eficácia comprovada, validação
experimental, integração à `main`, release ou deploy.

- **Papel exercido:** Consultor de Arquitetura e par do Arquiteto na autoria da
  EKM.
- **Ordem autorizada:** criar um papel institucional de IA para apoiar
  transversalmente o Arquiteto e o Tech Lead, preservando o Arquiteto como ator
  principal.
- **Repositório e recorte:** `EKM-guidelines`; método, perfil, regras comuns,
  roteamento, templates, histórico, decisão de desenho e caso de estudo em
  andamento.
- **Operações autorizadas:** investigar as fontes vigentes, propor o contrato,
  editar documentação e templates, validar a consistência e, após confirmação
  final, criar commit e realizar push.
- **Decisões explicitamente recebidas:** o Consultor pode atuar em todas as
  naturezas de atividade quando solicitado pelo Arquiteto; cada atuação depende
  de autorização e confirmação explícitas; a autorização deve ficar registrada
  ao final; o Arquiteto continua sendo o ator principal.
- **Resultado material preparado:** EKM 1.14 com perfil
  `CONSULTOR-DE-ARQUITETURA`, comando reutilizável, salvaguardas de autoridade e
  independência, atualização das fontes vigentes e registro no caso de estudo.
- **Validações e limitações:** consistência textual, referências e versões
  verificadas; nenhuma eficácia do papel foi ainda demonstrada; esta atuação
  participou da solução e não pode constituir revisão independente dela.
- **Significado solicitado para a confirmação final:** confirmar que este
  registro representa a autorização e as decisões do Arquiteto e autorizar o
  commit e o push do resultado preparado. A confirmação não declara eficácia,
  validação experimental, integração à `main`, release ou deploy.

## DD-027 — Preservação arquitetural local com evolução explícita

**Decisão:** a EKM estabelece como comportamento padrão que implementações
preservem a arquitetura, a organização e a separação de responsabilidades do
repositório, usando o precedente equivalente mais próximo. Um agente não cria
nova camada, pasta estrutural, abstração transversal ou padrão arquitetural por
preferência própria.

Uma especificação Implementável pode autorizar evolução arquitetural quando a
mudança for consciente e delimitada. Para isso, ela identifica:

1. o padrão, a restrição ou o precedente atual afetado;
2. a mudança pretendida;
3. o alcance da mudança;
4. a justificativa ou decisão do Arquiteto que a sustenta.

Ausência de orientação, necessidade técnica inferida, oportunidade de melhoria
ou redação genérica não constituem autorização. Ausência ou conflito de
precedentes devolve a decisão ao Arquiteto.

**Aplicação por ator:**

- o Autor localiza o precedente e torna qualquer desvio explícito;
- o Analista verifica se a mudança pode ser executada sem inferência
  arquitetural;
- o Implementador preserva o precedente ou executa somente o desvio
  delimitado;
- o Revisor confronta organização, responsabilidades e autorização do desvio.

**Aplicação proporcional:** a EKM central define o comportamento, mas a
arquitetura concreta permanece no repositório. O `AGENTS.md` apenas localiza as
fontes técnicas e declara invariantes locais. Não é criado um documento
arquitetural obrigatório; a especificação detalha os quatro elementos somente
quando existir desvio.

**Alternativas consideradas:**

- congelar todo padrão existente foi rejeitado porque transformaria legado em
  norma e impediria evolução intencional;
- permitir que o agente reorganize o projeto quando julgar tecnicamente melhor
  foi rejeitado porque transfere decisão arquitetural e amplia escopo;
- exigir aprovação externa para todo novo arquivo foi rejeitado por adicionar
  custo sem distinguir manutenção comum de mudança estrutural;
- criar um manual arquitetural universal na EKM foi rejeitado porque padrões
  pertencem ao contexto de cada repositório.

**Motivo:** uma regra curta e localizável reduz a criação incidental de
estruturas desconhecidas e a mistura de responsabilidades, preservando uma
válvula de escape para mudanças conscientemente conduzidas pela especificação.

**Caráter experimental:** a regra será inicialmente observada no ciclo da
especificação `OAUTH-END-USER-AUTHORIZATION-001`. Ela ainda não comprova
redução de retrabalho ou aumento de aderência entre modelos. A adoção da EKM
1.15 nesse repositório permanece uma mudança local separada.

**Critérios de reavaliação:** simplificar, retirar ou especializar a regra se
ela congelar código inadequado, gerar consultas frequentes sem valor, permitir
interpretações divergentes de “precedente equivalente” ou não reduzir desvios
arquiteturais materiais.

**Estado da decisão:** confirmada pelo Arquiteto para incorporação à EKM 1.15.

### Registro da atuação

**Estado da confirmação final:** Confirmada pelo Arquiteto.

- **Papel exercido:** Consultor de Arquitetura e par do Arquiteto.
- **Ordem autorizada:** incorporar à EKM a preservação arquitetural local com
  uma exceção consciente e explícita pela especificação.
- **Repositório e recorte:** `EKM-guidelines`; método, regras comuns, perfis dos
  quatro atores, templates, governança, conceito e decisão de desenho.
- **Operações autorizadas:** editar as fontes afetadas, validar consistência,
  criar commit e realizar push.
- **Decisões confirmadas:** preservar arquitetura, organização e separação de
  responsabilidades por padrão; autorizar desvios somente quando a
  especificação identificar padrão atual, mudança, alcance e justificativa ou
  decisão do Arquiteto.
- **Resultado material:** EKM 1.15 preparada sem novo documento obrigatório,
  com responsabilidades distribuídas pelos atores e observação inicial
  prevista no ciclo `OAUTH-END-USER-AUTHORIZATION-001`.
- **Validações e limitações:** consistência textual e de versões verificada;
  eficácia ainda não demonstrada. O Consultor participou da criação e não pode
  atuar como revisor independente dessa regra.
- **Significado da confirmação:** o Arquiteto confirmou que o registro
  representa a discussão e autorizou commit e push. A confirmação não declara
  eficácia experimental, validação funcional, integração à `main`, release ou
  deploy.

## DD-028 — Conclusão exige estado terminal das execuções iniciadas

**Decisão:** nenhum agente pode promover estado, registrar validação como
aprovada, criar o commit final, realizar push ou emitir resposta conclusiva
enquanto tarefa, comando, processo, build, teste, upload ou execução delegada
que tenha iniciado permanecer em estado não terminal ou desconhecido.

Antes do encerramento, o agente identifica essas execuções, confirma o estado
terminal e captura resultado, código de saída ou limitação material. Trabalho
inconclusivo não se converte em sucesso por cancelamento, abandono ou emissão de
relatório.

**Evidência:** na análise de `OAUTH-END-USER-AUTHORIZATION-001`, um agente
promoveu a especificação, criou commit, realizou push e declarou conclusão
enquanto duas tarefas de build ainda executavam; uma permanecia pendente após o
relatório.

**Proporcionalidade:** o controle é local ao trabalho iniciado pelo próprio
agente. Ele permite continuar outras ações autorizadas durante a espera e não
introduz fila, lock, orquestrador ou sincronização entre atores.

**Alternativas rejeitadas:**

- confiar que a ferramenta cancelará tarefas ao concluir foi rejeitado porque
  não preserva resultado nem código de saída;
- exigir espera imediata após cada comando foi rejeitado porque impediria
  paralelismo útil;
- aplicar a regra somente a builds foi rejeitado porque testes, uploads e
  execuções delegadas produzem o mesmo risco de evidência prematura.

**Critérios de reavaliação:** simplificar a enumeração de estados ou operações
se ambientes diferentes não conseguirem aplicá-la de forma consistente;
especializar a regra se ela bloquear trabalho sem relação com evidência ou
entrega.

**Estado da decisão:** confirmada pelo Arquiteto para incorporação à EKM 1.16.
