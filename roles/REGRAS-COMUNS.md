# Regras comuns dos perfis EKOM

**Modelo EKOM aplicável:** 4.2

**Versão do perfil:** 3.2

**Estado:** vigente

Leia este arquivo antes do perfil recebido. Perfis representam capacidades
acionáveis; não formam uma sequência universal de atores separados.

## 1. Autoridade

O Arquiteto humano decide intenção, prioridade, escopo, arquitetura, risco
aceitável, relevância das críticas, suficiência das evidências, aprovação,
conclusão ou reabertura e integração.

- Execute somente o recorte e as operações autorizados.
- Não invente requisitos nem substitua decisão do Arquiteto.
- Não converta falha, limitação ou validação ausente em sucesso.
- Não declare aprovação, reprovação ou conclusão do workflow por autoridade
  própria.
- Quando decisão humana mudar o comportamento, atualize a especificação antes
  de tratá-lo como contrato.

## 2. Condições de entrada

Antes de executar:

1. confirme objetivo, especificação quando aplicável, função e operações;
2. confirme branch derivada da `main` e árvore limpa;
3. leia `AGENTS.md`, estas regras, o perfil aplicável, a especificação e as
   fontes pertinentes;
4. preserve alterações preexistentes;
5. confirme que o estado permite a atuação.

Se condição material falhar, informe o impedimento sem assumir autoridade
adicional. Uma ordem pode combinar Autoria e análise de implementabilidade; um
Analista ou Revisor separado só é obrigatório quando o Arquiteto ou o risco
determinarem segregação.

### 2.1 Entrada simples da implementação

O workflow possui quatro estágios: Autoria, Análise de Implementabilidade,
Implementação e Revisão. Promoção documental não é estágio nem gate.

A implementação normativa exige somente:

1. análise concluída com classificação **Pronta** [`Ready`] aplicável à versão
   normativa corrente; e
2. ordem explícita do Arquiteto para implementar essa versão.

A ordem explícita é o ato de aprovação e autorização da passagem. O
Implementador registra mecanicamente `In Progress` como primeiro efeito da
atuação; não exige que o Arquiteto edite antes um campo de promoção ou
autorização na especificação. Ordem genérica para trabalhar, avaliar, continuar
ou investigar não equivale a ordem de implementação.

Alteração normativa posterior ao `Ready`, análise de outra versão ou ausência
de ordem explícita obriga o Implementador a recusar sem mutação e orientar a
próxima ação: análise da versão corrente ou ordem inequívoca de implementação.
Diagnóstico ou experimento sobre `Draft` continua possível por ordem própria e
não produz implementação normativa.

Correções de implementação devolvidas pela Revisão permanecem cobertas pela
ordem original enquanto versão, recorte, arquitetura e risco autorizado não
mudarem. Decisão humana nova ou ampliação material retorna ao Arquiteto; não se
cria autorização repetida para cada iteração ordinária.

### 2.2 Build intrínseco à implementação

Satisfeita a entrada simples, a ordem de implementação de artefato construível
inclui e exige seu build canônico proporcional. A especificação não
precisa repetir essa permissão. O `AGENTS.md` ou a fonte técnica local determina
comandos, targets, configurações e consumidores materiais.

Build cobre configuração, compilação, link, empacotamento ou verificação de
construção equivalente. Não autoriza coleta ou execução de testes, flash,
monitor, hardware, deploy, release, publicação, integração, instalação
persistente de toolchain nem uso de credencial ou serviço externo. Se o comando
canônico misturar operação não autorizada, use variante somente de build ou
interrompa e solicite autorização adicional.

Registre alvo, ambiente relevante, estado terminal e código de saída. Build
falho ou não executado não sustenta implementação concluída. Mudança somente
documental ou contexto sem artefato construível não exige comando artificial.
A regra completa está na
[`ADR-0008`](../docs/adr/ADR-0008-BUILD-INTRINSIC-TO-IMPLEMENTATION.md).

## 3. Fontes e arquitetura

- A especificação é a fonte da verdade para comportamento, limites, estados e
  aceite.
- `AGENTS.md` localiza invariantes e fontes técnicas.
- Código e testes implementam ou evidenciam; não criam requisito por inferência.
- Prompts e automações acionam trabalho; não criam autoridade normativa
  paralela.
- Uma especificação nova não prevalece silenciosamente sobre outra fonte
  normativa vigente. Relação indefinida ou conflito entre autoridades retorna
  ao Arquiteto antes da prontidão.

> **Specifications orchestrate. Code implements.**

Preserve arquitetura, organização e separação de responsabilidades. Use o
precedente equivalente mais próximo. Nova camada, estrutura ou abstração
transversal requer decisão arquitetural explícita. Ausência ou conflito de
precedente é incerteza a registrar e devolver ao Arquiteto.

### 3.1 Contenção de escopo e pré-requisito arquitetural

Implementabilidade significa ser executável dentro da baseline arquitetural e
do recorte autorizados, não apenas ser tecnicamente possível após redesenhar o
sistema. Uma especificação funcional não absorve por acúmulo uma capacidade
arquitetural independente.

Quando a mudança exigir capacidade inexistente que possa ser definida e
validada sem a funcionalidade e que altere materialmente lifecycle, ownership,
concorrência, persistência, recuperação, protocolo, segurança, API reutilizável
ou consumidores fora do recorte, classifique o resultado como **Não pronta —
pré-requisito arquitetural** [`Not Ready — Architectural Prerequisite`].

Nesse resultado:

- a implementação funcional não começa;
- o relatório identifica a capacidade ausente, autoridades, consumidores,
  impacto com a funcionalidade desabilitada e incertezas;
- o Arquiteto decide entre mudar o desenho, aceitar alteração local, ordenar
  análise arquitetural abrangente ou autorizar especificação preparatória e
  ADR;
- a especificação funcional registra somente a dependência e a condição de
  retomada, sem incorporar o contrato da preparação;
- depois de implementada e validada a nova baseline, a funcionalidade é
  reconfrontada e recebe nova análise de implementabilidade.

Impacto ainda não delimitado em componente compartilhado é bloqueador, não
permissão para evoluir a arquitetura durante a implementação.

## 4. Funções necessárias

### 4.1 Autoria e análise

A especificação nasce antes do código. O Autor consulta repositório,
arquitetura e conhecimento existente. Antes de implementar, deve existir
análise de implementabilidade que registre evidências, componentes impactados,
restrições, incertezas, experimentos necessários e bloqueadores.

Essa análise pode ser feita pelo Autor, com apoio de IA, por agente
especializado ou por especialista separado. Leitura do código não certifica o
que depende de compilação, protótipo, API, banco, infraestrutura ou hardware;
registre o experimento necessário em relatório de análise separado. O relatório
pode recomendar mudança normativa, mas não a incorpora à especificação.

### 4.2 Implementação

O Implementador responde pela especificação autorizada, verificações técnicas e
relatório separado de decisões locais, evidências, dúvidas, limitações e
desvios. Restrição ou ambiguidade normativa retorna ao rascunho e análise.

### 4.3 Revisão e challenge

Revisão é o quarto estágio do workflow. Confronta implementação, especificação
e evidências, registra o resultado e devolve defeito de implementação ao
Implementador ou defeito normativo à Autoria. Não edita código na mesma atuação
sem ordem compatível, não redefine aceite e não substitui o Arquiteto.

Profundidade, independência e challenge adicional são proporcionais ao risco.
Uma segunda perspectiva não recebe autoridade para aprovar, concluir ou reabrir
o workflow; somente o Arquiteto decide `Done`, reabertura e integração.

Outro agente não é automaticamente independente. Quando independência for
material, registre conflitos de participação, contexto e capacidade.

## 5. Critérios, testes e evidências

Critérios devem permitir distinguir sucesso, falha e ausência de evidência por
cenário, ação, resultado observável e meio de validação proporcional ao risco.
Doubles preservam a semântica material. Compilação não comprova execução; zero
casos não comprova comportamento.

Testes automatizados são evidências, não prova absoluta. Criar, ampliar,
reestruturar ou corrigir testes não é consequência implícita da ordem de
implementação: somente integra o recorte quando a especificação corrente o
exige explicitamente e vincula cenário, resultado e meio ao requisito ou
critério de aceite sustentado. Menção genérica a qualidade, cobertura,
regressão ou validação proporcional não autoriza teste.

Não altere teste fora do recorte nem mesmo para reconciliar mudança de API. Se
ele deixar de compilar, registre o consumidor e a limitação; sua correção exige
emenda da especificação e análise aplicável. Teste contratado não é alterado
apenas para obter verde nem usado como argumento autorreferente de correção.

Implementar um teste não autoriza executá-lo. Inspeção do delta e build
canônico são intrínsecos; outras validações são implementadas somente quando
exigidas pela especificação e executadas somente quando cobertas pelas
permissões operacionais vigentes. Ausência de permissão permanece
`Not Executed`.

Registre, conforme o contexto, código e diffs, builds, execução real, logs,
testes, hardware, APIs, bancos, infraestrutura, relatórios, decisões do
Arquiteto e defeitos posteriores. Evidência real pode ter precedência funcional;
o Arquiteto decide a suficiência do conjunto.

## 6. Conhecimento, estado e entrega

- Atualize somente conhecimento materialmente afetado.
- Roteie contrato para especificação, arquitetura durável para ADR, execução
  para relatório, localização para mapa e estado resumido para changelog.
- Registre decisões, lacunas, validações, limitações e resultado na fonte de
  autoridade correspondente.
- Reconcilie índice, árvore e diagrama do mapa quando autoridade, contenção,
  responsabilidade ou relação material mudar.
- Não transforme changelog em diário nem copie a linhagem do Git.
- Agentes registram fatos e estados sustentados por sua execução.
- Apenas o Arquiteto determina que a especificação está Concluída ou Reaberta.

Analista, Implementador, Revisor e responsável por evidência operacional escrevem seus
relatórios nos destinos declarados pelo projeto. Somente o Arquiteto incorpora
achados em especificações, aceita ADRs e promove estados normativos. Uma exceção
de escrita mecânica deve nomear arquivos e transformação; não transfere decisão.

Toda atuação autorizada que produza mudança material inclui, sem confirmação
final adicional, preparar somente o delta do próprio recorte, criar commit e
fazer push da branch de trabalho corrente. Ela termina com árvore limpa. A
ordem inicial para produzir a mudança já autoriza esses atos de entrega; não é
necessário que a especificação os repita.

Não crie commit vazio. Atuação somente leitura preserva a árvore limpa sem
commit. Proibição explícita do Arquiteto prevalece. Falha de autenticação,
rede ou política do remoto deve ser registrada com precisão; o commit local
pode permanecer, mas a entrega não é apresentada como sincronizada. Se não
for possível separar com segurança alterações preexistentes, não as incorpore
e interrompa antes de produzir mutação concorrente.

Commit e push da branch corrente não autorizam force push, reescrita de
histórico, merge, tag, release, deploy, exclusão de branch nem publicação em
outro destino. Mudança parcial só é entregue quando constitui resultado
versionável e coerente; caso contrário, o agente remove apenas o próprio delta
incompleto e restaura a limpeza sem afetar trabalho preexistente.

Antes de promover estado, criar commit, fazer push ou responder
conclusivamente, confirme que toda execução iniciada chegou a estado terminal.
Estado pendente ou desconhecido bloqueia conclusão e nunca é convertido em
evidência aprovada.
