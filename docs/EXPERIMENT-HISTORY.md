# Como chegamos ao modelo atual

## Contexto

A EKM surgiu durante experimentos de engenharia assistida por IA em projetos reais. A intenção inicial era aumentar produtividade mantendo o arquiteto humano responsável pelas decisões.

## 1. Especificações melhoraram a execução

Recortes delimitados fizeram o agente implementar, compilar, testar e relatar com menos expansão de escopo. Ficou claro que uma especificação suficientemente completa pode funcionar como unidade de delegação para um desenvolvedor humano ou agente.

## 2. Build e relatório não preservam intenção

Uma consolidação tecnicamente aprovada removeu conhecimento relevante de um documento de arquitetura. O relatório também não destacou adequadamente a mudança normativa. Isso mostrou que:

- código correto não garante conhecimento preservado;
- listar arquivos alterados não explica mudança semântica;
- documentos normativos precisam de proteção explícita.

## 3. O último commit não é sempre o baseline

Em uma reorganização de componentes, comparar somente com `HEAD` quase levou à conclusão errada de que alterações preexistentes haviam sido perdidas. A prova correta exigiu recuperar o estado real do worktree no início da tarefa.

Daí surgiu a regra: baseline é o estado observado, incluindo mudanças não commitadas.

## 4. Transações e lacunas tornaram o processo auditável

Foram introduzidos:

- `EKM-CHG-NNNN` para acompanhar mudanças;
- `EKM-GAP-NNNN` para representar conhecimento ausente;
- estados explícitos de abertura e encerramento;
- Definition of Done que reconcilia código, documentação e evidências.

Isso permitiu reabrir uma mudança quando a prova era insuficiente e encerrá-la novamente somente após nova auditoria.

## 5. Especificações precisam evoluir gradualmente

Funcionalidades não nascem em um único documento ou momento. Protocolos, commissioning, reset, reports, reutilização e correções surgiram em etapas, às vezes com regressão ou mudança de direção.

Por isso, a EKM adotou especificações incrementais e dois estados independentes: autoridade normativa e situação da implementação.

## 6. Adoção em legado exige outro ritmo

Ao iniciar a aplicação em uma biblioteca grande, ficou evidente que tentar documentar tudo seria caro e improdutivo. O modelo passou a usar:

- inventário em largura;
- aprofundamento por risco;
- perguntas humanas apenas sobre intenção;
- specification on touch;
- níveis graduais de cobertura até `Reconstructible`.

## 7. Implementação correta não valida uma inferência

No experimento de exemplos executáveis, o executor encontrou um build legado que usava `LED_BUILTIN` sem defini-lo. Ele escolheu uma definição coerente com `LED_PIN` e obteve build aprovado, mas essa alternativa não estava autorizada pela especificação.

O resultado mostrou que proibir contratos inventados não era suficiente: a lacuna precisa ser descoberta antes do código. A EKM passou a exigir Technical Readiness Review integral e bloqueio atômico quando qualquer requisito depender de inferência relevante.

## 8. Evolução após implementação exige linhagem

A reabertura da especificação dos exemplos mostrou que documentos ainda não integrados precisam poder voltar a revisão. Ao mesmo tempo, reescrever versões já entregues apagaria a intenção que governou a produção. O modelo passou a separar implementação, validação e entrega, congelando versões em `Done` e usando especificações relacionadas para evoluções posteriores.

Essa ampliação também revelou que garantias baseadas apenas em disciplina são frágeis. O `EKM Gate` foi registrado como direção futura, ainda sem arquitetura ou implantação definida.

## 9. Encontrar o primeiro bloqueio não comprova revisão integral

Em um experimento deliberado, uma especificação de exemplo para `AirConditionerCapability` presumiu a existência de uma API pública que não havia sido confirmada. O executor identificou corretamente a premissa falsa, declarou `Needs Clarification` e não implementou a API por inferência.

O bloqueio atômico funcionou, mas a revisão terminou após esse primeiro impedimento. Outras dimensões observáveis, como o estado normativo `Draft` e o ciclo de vida incompleto da capability, não foram registradas. A tarefa também foi marcada operacionalmente como concluída, embora a implementação estivesse bloqueada.

O resultado mostrou que:

- bloqueio imediato da implementação e continuidade da análise são obrigações diferentes;
- revisão integral exige classificação cumulativa de todos os requisitos e dimensões;
- o executor não deve produzir e consumir sua própria autorização;
- `Implementable` deve aguardar aprovação humana;
- a reconfirmação do baseline protege a autorização contra mudanças posteriores.

O modelo 1.6 introduziu esses controles manualmente, sem exigir múltiplos agentes, CI/CD ou `EKM Gate`.

## 10. Papéis separados melhoram rastreabilidade, mas aumentam coordenação operacional

O primeiro piloto de coordenação por atores aplicou Autor da Especificação,
Engenheiro Analista, Engenheiro Implementador e Engenheiro Tech Lead a uma
mudança real no SmartHome-DeviceApi.

Os checkpoints tornaram os handoffs e desvios localizáveis. O Implementador
permaneceu no recorte aprovado, e o Tech Lead confirmou aderência estática sem
transformar uma falha de ambiente em falsa evidência operacional. O arquiteto
validou manualmente e aceitou o código e a funcionalidade.

O mesmo caso exigiu correções documentais, normalização do protocolo durante a
transação e intervenções frequentes da Coordenação. Restore indisponível e
ausência de banco isolado também impediram uma cadeia automatizada de
evidências.

O resultado parcial sustenta continuar o experimento, não incorporar o modelo
como obrigação. Validador de Integridade, integração e retrospectiva final ainda
precisam ser executados.

A avaliação inicial tratou a quantidade de interações humanas como possível
custo do modelo. A discussão posterior corrigiu essa expectativa: pareceres,
aprovações, validações e decisões finais são governança esperada. O custo a
reduzir é o de correções documentais, ambiguidades, preparação repetitiva e
tratamento operacional de handoffs.

Esse alinhamento motivou o modelo 1.7 e o protocolo 0.5: a especificação pode ser
humana, assistida ou produzida por agente, mas deve receber parecer humano
explícito antes da análise de implementabilidade.

Detalhes:
[`SMARTHOME-DEVICEAPI-COORDINATED-ACTORS.md`](case-studies/SMARTHOME-DEVICEAPI-COORDINATED-ACTORS.md).

## 11. Vocabulário misto também é risco operacional

A revisão do método e dos modelos encontrou três camadas misturadas sem
distinção suficiente: prosa normativa em português, termos técnicos externos e
identificadores de estados em inglês.

O piloto de atores tornou o problema observável. `Accepted` representava tanto
aceitação humana da intenção quanto admissão técnica de um marco; `Pending` e
`Blocked` também apareciam em contextos distintos. Termos como `gate`,
`handoff`, `checkpoint` e `Technical Readiness Review` eram usados como prosa
normativa sem vocabulário canônico.

O modelo 1.8 adotou português do Brasil como idioma normativo, definiu força
controlada para obrigações e permissões, introduziu rótulos contextuais em
português e preservou os valores ingleses como identificadores legados de
compatibilidade. O objetivo não é traduzir comandos ou APIs, mas garantir um
nome e um significado canônico para cada conceito.

## 12. Rastreabilidade redundante pode ocultar o valor do método

Ao preparar um novo experimento em um aplicativo Swift para iOS, iPadOS e
watchOS, a aplicação do protocolo 0.6 tornou visível um custo subestimado:
checkpoints, registros de SHA, pareceres intermediários, matrizes universais e
papéis obrigatórios repetiam informações ou decisões já disponíveis no Git e na
ordem do Arquiteto.

A revisão concluiu que:

- a autoridade do Arquiteto deve prevalecer explicitamente sobre os agentes;
- o prompt ou comando do Arquiteto já autoriza a etapa solicitada;
- o estado da especificação é suficiente para orientar a etapa seguinte;
- o Git deve preservar a linhagem sem ser transcrito para documentos;
- cada agente ainda deve entregar seu trabalho por commit e push;
- análise e revisão devem ser proporcionais ao risco;
- problemas não adotados não devem entrar preventivamente no fluxo.

O modelo 1.9 e o protocolo 0.7 removem a passagem documental obrigatória entre
papéis, preservando decisões, lacunas, evidências materiais e entrega
versionada. A hipótese do novo experimento é que essa dose menor de governança
permitirá testar e descartar ideias mais rapidamente sem perder
auditabilidade.

## 13. Resultado funcional e conformidade do agente são independentes

No experimento com o aplicativo Swift, o Arquiteto validou a implementação e
executou os testes integrados com resultado aprovado. Ao mesmo tempo, observou
que agentes usados pelo chat do VS Code não cumpriram integralmente a EKM ou
tomaram decisões incompatíveis com o método. Entre os executores experimentados,
somente o Codex apresentou conformidade consistente segundo a avaliação humana.

A boa assertividade do Codex também foi percebida em conversas novas. O
experimento, porém, não isolou modelo, ambiente agente, hierarquia de
instruções, ferramentas ou eventual contexto disponível. Portanto, não existe
evidência para atribuir o resultado a memória entre conversas ou ao contexto do
ChatGPT.

O achado impede duas equivalências indevidas:

- implementação funcionalmente aceita não comprova conformidade EKM;
- conformidade observada em um executor não comprova independência do método
  em relação a modelos e ambientes.

A consequência atual não é adicionar controles. É manter as regras essenciais
curtas, locais e verificáveis, para que não dependam de memória implícita nem
compitam desnecessariamente pela atenção do agente.

Detalhes:
[`IOTSMARTHOME-MULTI-AGENT-OBSERVATION.md`](case-studies/IOTSMARTHOME-MULTI-AGENT-OBSERVATION.md).

## 14. O fluxo precisa de uma origem comum e isolada

O primeiro piloto de coordenação por atores iniciou a mudança em uma branch
funcional derivada da `main`. Essa prática preservou a origem do trabalho e
isolou especificação, análise e implementação até a decisão de integração, mas
permanecia registrada apenas como característica daquela execução.

O Arquiteto decidiu adotá-la como regra geral. A EKM 1.10 e o protocolo 0.8
passaram a exigir que todo fluxo comece em uma branch de trabalho derivada da
`main`, nunca diretamente nela. A mesma branch pode atravessar as etapas do
recorte e não precisa incorporar avanços posteriores da `main`.

## 15. A execução pode sobreviver à troca de agente e modelo

A implementação da especificação `IOTSSC-GARAGE-CONTROL@0.1` foi conduzida em
duas partes sequenciais com uma instrução autocontida para o Implementador.

O Copilot com Kimi K2.7 Code produziu uma implementação parcial material e
versionada. A execução consumiu aproximadamente 80 mil tokens e foi interrompida
quando os créditos da conta se esgotaram. O Codex no ChatGPT retomou o trabalho,
completou o recorte e reconciliou as fontes EKM sem compartilhar a conversa do
primeiro ambiente.

O environment automatizado canônico permaneceu bloqueado por configuração
preexistente, e essa limitação não foi convertida em sucesso. Posteriormente, o
Arquiteto executou os testes no dispositivo, validou a implementação e promoveu
a especificação para `Active / Validated / Ready for Integration`.

O caso demonstra que especificação, estado e Git podem funcionar como memória
compartilhada entre executores heterogêneos. Também mostra que aderência técnica
e viabilidade econômica são dimensões independentes: o resultado foi
aproveitável, mas o consumo do primeiro executor foi material.

A evidência favorece continuar testando prompts autocontidos por etapa. Um
único caso não autoriza torná-los obrigatórios nem afirmar independência
universal de modelo.

Detalhes:

- [`SELF-CONTAINED-IMPLEMENTER-RUN-001.md`](experiments/SELF-CONTAINED-IMPLEMENTER-RUN-001.md);
- [`IOTSMARTSYSCORE-GARAGE-CONTROL-SEQUENTIAL-AGENTS.md`](case-studies/IOTSMARTSYSCORE-GARAGE-CONTROL-SEQUENTIAL-AGENTS.md).

## 16. Perfis referenciados sustentaram um ciclo completo

O experimento `AIOTSMARTHOME-MODULE-SETTINGS-RESET-001@0.1` percorreu autoria,
duas análises, decisão do Arquiteto, implementação, revisão do Tech Lead,
validação no dispositivo final, publicação e integração à `main`.

Claude Sonnet 5, Gemini 3.6 Flash High no Google Antigravity e Codex atuaram em
partes diferentes do percurso. O prompt mínimo identificava apenas papel e
especificação; o `AGENTS.md` encaminhava o agente para regras comuns e um perfil
fixo. A especificação, seus estados e o Git permitiram continuidade entre
ambientes sem compartilhar conversas.

O experimento também expôs dois desvios: uma interpretação parcial da exigência
de árvore limpa e uma promoção incorreta quando foi selecionado um papel
incompatível com a etapa. A correção não adicionou um reconciliador. Cada ator
passou a registrar e promover o resultado que sua própria atuação sustenta.

Após revisão do Tech Lead e aprovação do Arquiteto, a especificação atingiu
`Active / Validated / Done`; a mudança foi integrada pelo PR #39.

O Arquiteto aprovou a incorporação do modelo de atores ao fluxo oficial. A EKM
1.11 torna normativos os perfis, o roteamento por `AGENTS.md` e a promoção de
estado por etapa.

Detalhes:
[`IOTSMARTHOME-REFERENCED-ACTORS-LIFECYCLE.md`](case-studies/IOTSMARTHOME-REFERENCED-ACTORS-LIFECYCLE.md).

## 17. Uma especificação local revelou um objetivo multi-contexto

Durante a análise arquitetural da especificação
`AIOTSMARTHOME-SENSITIVE-DATA-REMOVAL-001@0.1`, a EKM tornou visível que remover
dados sensíveis do aplicativo não é uma implementação autônoma do
`iotsmarthome`.

O fluxo seguro depende de pelo menos três contextos de entrega:

- o provedor OAuth/OIDC precisa suportar autenticação interativa de usuário e o
  fluxo adequado para cliente nativo público;
- as APIs SmartHome precisam validar a autorização e fornecer configuração de
  runtime com escopo;
- o aplicativo precisa adotar sessão segura, recuperar a configuração
  autorizada e remover o bootstrap compartilhado legado.

O serviço OAuth existente já contém partes do contrato, como Authorization
Code, PKCE, discovery, renovação e revogação, mas isso não torna prontas a
experiência interativa, a proteção das APIs nem a integração do app. Promover a
especificação local como implementável ocultaria dependências externas; reunir
toda a implementação no documento do aplicativo misturaria fontes e
autoridades.

A descoberta mostrou uma função adicional do método: preservar um objetivo
arquitetural enquanto cada fonte responsável evolui por especificações e
evidências próprias. O Arquiteto aprovou a coordenação por uma especificação
ponta a ponta e especificações subordinadas nos contextos de entrega, sem criar
novo ator, orquestração ou rastreamento manual de commits entre repositórios.

A EKM 1.13 incorpora essa capacidade de forma proporcional. O caso de dados
sensíveis continua em andamento; portanto, a utilidade da coordenação
multi-contexto ainda deverá ser confrontada durante autoria, análise,
implementação e validação integrada dos recortes.

## 18. A colaboração arquitetural por IA precisa de papel institucional

A evolução da EKM e as decisões arquiteturais dos experimentos já eram
discutidas com IA, inclusive fora das quatro etapas funcionais. Essa
colaboração produzia resultados materiais, mas dependia de papéis ad hoc e não
possuía contrato próprio para delimitar operações, preservar a autoridade do
Arquiteto ou registrar a autorização humana.

O Arquiteto decidiu instituir o Consultor de Arquitetura como papel
transversal, subordinado e fora do pipeline. O papel pode apoiar também o Tech
Lead, mas somente o Arquiteto autoriza o recorte e confirma decisões
reservadas. A amplitude operacional não é permissão genérica e não sustenta
independência quando o Consultor já participou do mesmo recorte.

A EKM 1.14 exige que, antes do commit final, o Consultor apresente um registro
da ordem, operações, decisões, resultado e limitações e obtenha confirmação
explícita do Arquiteto. A exigência é uma hipótese de governança a ser
reavaliada pelo valor decisório e pelo custo, não uma afirmação de eficácia já
demonstrada.

## 19. Trabalho assíncrono pendente invalida conclusão antecipada

Na análise da especificação `OAUTH-END-USER-AUTHORIZATION-001`, um Engenheiro
Analista executado no Antigravity com Gemini 3.6 Flash High promoveu a prontidão,
atualizou conhecimento, criou commit, realizou push e emitiu relatório de
conclusão enquanto duas tarefas de build ainda estavam em execução. Após o
relatório, uma delas continuava pendente.

O desvio mostrou que iniciar um comando não comprova seu resultado e que uma
resposta conclusiva pode competir com ferramentas assíncronas do próprio
agente. A evidência de build e teste não era terminal no instante em que foi
registrada, mesmo que a análise de implementabilidade pudesse permanecer
tecnicamente correta por outras fontes.

O Arquiteto decidiu tornar universal um gate local de encerramento. A EKM 1.16
exige que cada agente confirme estado terminal e resultado de tudo que iniciou
antes de promover estado, aprovar evidência, criar o commit final, fazer push ou
emitir conclusão. A regra não cria orquestração entre atores e não impede o
agente de continuar trabalho útil enquanto aguarda.

## 20. Primeira calibração da adequação de um ator EKM

O mesmo ciclo de `OAUTH-END-USER-AUTHORIZATION-001` foi usado como primeira
amostra histórica da métrica experimental. A avaliação considera o perfil
Gemini 3.6 Flash High no Antigravity, atuando como Engenheiro Analista sob a EKM
1.15.

| Dimensão | Nota | Fundamentação |
|---|---:|---|
| Autoridade, papel e escopo | 19/20 | preservou o papel documental, não alterou implementação e aguardou ordem posterior; houve linguagem que aproximou proposta de fato existente |
| Correção técnica do resultado | 15/20 | `Implementable` permaneceu defensável e a arquitetura foi confrontada, mas o baseline de testes não foi incorporado ao handoff |
| Evidências e validações | 7/25 | builds aprovados foram registrados, porém a conclusão antecedeu tasks e a falha terminal de `dotnet test` foi omitida |
| Estados e conhecimento EKM | 10/20 | a especificação preservou `Proposed / Not Started / Not Ready / Implementable`, mas o mapa colocou `Implementable` na coluna normativa e a limitação não foi reconciliada |
| Git e encerramento | 9/15 | branch, resultado material e árvore foram tratados, mas commit, push e relatório ocorreram antes do estado terminal de todas as execuções |
| **Total** | **60/100** | **Não aceitável [`Not Acceptable`]** |

O encerramento com tasks pendentes seria eliminatório sob a EKM 1.17. Como a
execução ocorreu sob a 1.15, o achado é calibração histórica, não violação ou
suspensão retroativa. Uma única amostra também não qualifica nem desqualifica
universalmente o modelo; o perfil permanece Candidato [`Candidate`] e requer
novas execuções supervisionadas.

A amostra mostrou utilidade inicial da métrica ao separar uma conclusão técnica
provavelmente correta de uma cadeia de evidências e estados que exigia correção.

## 21. Carregamento explícito da EKM no Claude Code

A mesma análise de `OAUTH-END-USER-AUTHORIZATION-001` foi repetida três vezes
com Claude Sonnet 5 na extensão Claude Code para VS Code. As duas primeiras
execuções usaram o prompt mínimo e o roteamento local baseado somente em
`AGENTS.md`. A terceira adicionou um `CLAUDE.md` que encaminhava explicitamente
o ambiente para `AGENTS.md`, regras comuns e perfil do Engenheiro Analista.

| Execução | Perfil observado | Nota bruta | Eliminatório | Classificação |
|---|---|---:|---|---|
| 1 | Sonnet 5 + Claude Code/VS Code, sem adaptador EKM | 61/100 | árvore não reconciliada e conclusão sem commit/push | Reprovada [`Failed`] |
| 2 | Sonnet 5 + Claude Code/VS Code, sem adaptador EKM | 67/100 | árvore não reconciliada e conclusão sem commit/push | Reprovada [`Failed`] |
| 3 | Sonnet 5 + Claude Code/VS Code, com `CLAUDE.md` | 89/100 | nenhum | Aceitável [`Acceptable`] |

Na terceira execução, o relatório mostrou leitura de `AGENTS.md`,
`REGRAS-COMUNS.md`, `ENGENHEIRO-ANALISTA.md`, especificação, changelog e mapa.
O agente começou com árvore limpa, usou o estado canônico `Needs
Clarification`, atualizou as três fontes afetadas, criou commit, realizou push
e terminou com árvore limpa.

A pontuação da execução adaptada foi:

| Dimensão | Nota | Fundamentação |
|---|---:|---|
| Autoridade, papel e escopo | 20/20 | carregou o papel correto, preservou o recorte documental e não alterou implementação |
| Correção técnica do resultado | 11/20 | o confronto factual foi forte, mas tratou como decisões arquiteturais três pontos que também admitem interpretação como escolhas normais de implementação |
| Evidências e validações | 23/25 | apresentou fontes e limitações materiais; builds e testes foram corretamente declarados fora do recorte documental |
| Estados e conhecimento EKM | 20/20 | sincronizou especificação, changelog e mapa com estados independentes e vocabulário canônico |
| Git e encerramento | 15/15 | commit, push, sincronização e árvore final limpa foram verificados |
| **Total** | **89/100** | **Aceitável [`Acceptable`]** |

O contraste sustenta a hipótese de que o carregamento das instruções é parte
material do perfil executor. Ele não demonstra que toda melhora decorreu
exclusivamente do adaptador, mas torna improvável atribuir as duas falhas
anteriores somente ao modelo.

Por decisão do Arquiteto, o perfil adaptado é provisoriamente aceitável para
uso com revisão. Ele permanece Candidato [`Candidate`]: possui somente uma
execução avaliada nessa configuração e ainda não satisfaz a amostra mínima em
dois contextos exigida para Aceito [`Accepted`]. O perfil sem adaptador
permanece Não aceitável para atuação autônoma.

## 22. Critérios listados não garantem um oráculo executável

A implementação experimental de
`IOTSSC-BINARY-COMMAND-STATE@0.1` no IoTSmartSysCore foi executada por Claude
Sonnet 5 no Claude Code com o adaptador EKM que havia produzido resultado
Aceitável no experimento anterior. O agente respeitou o fluxo documental,
implementou a fronteira de storage, criou testes, compilou o runtime, registrou
limitações, criou commit e realizou push.

A revisão do Tech Lead, porém, encontrou falso sucesso funcional:

- o caminho comum presumido não alcançava o override de LED;
- a válvula passava em mock que aceitava diretamente um vocabulário rejeitado
  pelo adapter real;
- corrupção havia sido reduzida a tamanho ou versão incompatível;
- falhas NVS exigidas não possuíam injeção separada;
- a compilação dos testes reportava zero casos executados, mas ainda sustentou
  a promoção para `Implemented`.

A especificação possuía requisitos e uma tabela de evidências, inclusive
menções aos tipos concretos e às falhas. O problema não foi ausência total de
critérios, mas falta de oráculos explícitos que permitissem ao executor
reprovar a própria solução. “Testes com valve”, “testes de corrupção” e
“injeção de falhas” admitiram evidências estruturalmente presentes, mas
semanticamente insuficientes.

O Arquiteto decidiu experimentar uma regra menor que “mais testes” ou uma
matriz universal: cada requisito obrigatório deve tornar observáveis cenário,
ação, resultado e evidência suficiente para distinguir aprovação, reprovação e
ausência de execução. Doubles preservam a semântica material substituída, e
compilação não comprova teste comportamental executado.

A EKM 1.18 incorpora a regra em caráter vigente. O caso ainda não demonstra
que ela evita o mesmo desvio; a especificação será restaurada ao estado anterior
à implementação, receberá critérios assertáveis e será submetida a uma nova
execução para comparação.

## Conclusão experimental

Os experimentos sustentam que agentes conseguem executar mudanças com autonomia
governada quando o repositório contém especificações, estados, perfis de
responsabilidade e histórico versionado. Julgamento de intenção, produto,
arquitetura, validação e integração permanece humano.

A incorporação do modelo de atores à EKM 1.11 encerra sua condição de hipótese
experimental. Sua eficácia universal não é presumida: novas aplicações,
regressões e custos observados continuam orientando a evolução do método.
