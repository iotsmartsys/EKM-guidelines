# Experimento — Modelo de coordenação por atores

**Status:** Experimental / In Progress

**Natureza:** protocolo experimental não normativo  
**Modelo EKM de referência:** 1.7
**Versão do protocolo:** 0.5

**Branch do experimento:** `modelo_de_coordenacao_por_atores`  
**Resultado:** piloto avançou até validação humana; auditoria de integridade e
integração ainda não executadas

## 1. Contexto

O modelo EKM 1.7 separa parecer humano da especificação, Technical Readiness
Review, autorização humana para implementação, execução e reconciliação, mas
não exige que as responsabilidades técnicas sejam exercidas por agentes
diferentes. A coordenação entre múltiplos agentes e a separação assistida de
responsabilidades permanecem questões em aberto.

Este experimento avaliará uma forma de trabalho coordenada por atores
especializados. Na primeira execução, os atores poderão ser simulados
manualmente em execuções separadas. O protocolo não altera o método de
referência vigente. Os templates ajustados nesta branch pertencem ao experimento
e não passam a reger projetos adotantes sem decisão explícita.

## 2. Pergunta experimental

A separação governada entre decisão humana, análise, implementação, revisão
técnica e auditoria da EKM aumenta a confiança e a velocidade da entrega,
mantendo custo operacional aceitável?

## 3. Hipóteses

### 3.1 Hipótese principal

A separação de responsabilidades, sob autoridade humana explícita, aumenta a
confiança da entrega e detecta desvios materiais sem transferir aos agentes a
decisão sobre intenção ou integração.

### 3.2 Hipóteses secundárias

- o Engenheiro Analista reduz ambiguidades e decisões ausentes que chegariam à
  implementação;
- o Engenheiro Tech Lead identifica divergências entre a especificação aprovada,
  o código e o relatório de implementação;
- o Validador de Integridade da EKM identifica violações metodológicas que uma
  revisão exclusivamente técnica não detectaria;
- handoffs explícitos produzem evidências localizáveis, auditáveis e
  reutilizáveis;
- o parecer humano anterior à análise impede que uma especificação produzida por
  agente adquira autoridade sobre a intenção;
- o valor incremental dos controles compensa o tempo, o contexto, os tokens e a
  coordenação adicionais.

### 3.3 Hipótese nula

O modelo não oferece ganho relevante sobre o processo vigente, seus atores
produzem principalmente observações duplicadas ou seu custo operacional supera
os benefícios observados.

## 4. Escopo

O experimento abrange:

- análise integral de uma especificação e do baseline aplicável;
- criação da especificação em branch exclusiva derivada de `main`;
- parecer humano de que a especificação representa a intenção conhecida;
- handoffs entre atores baseados em checkpoints commitados;
- autorização humana explícita para implementação;
- implementação da especificação aprovada;
- build e testes aplicáveis;
- revisão técnica independente;
- auditoria de integridade contra a EKM;
- validação funcional e decisão final humanas;
- medição dos resultados e retrospectiva.

O experimento não:

- modifica por si só o modelo EKM 1.7;
- exige que a especificação seja confeccionada por IA ou por qualquer forma
  específica de automação;
- autoriza implementação sem Technical Readiness Review e autorização humana;
- transfere decisões de produto ou arquitetura aos atores de IA;
- substitui testes, validação em hardware ou validação humana;
- torna `qa` ou `homolog` obrigatórias antes que seu processo de promoção seja
  especificado e validado;
- alega independência real quando os atores forem simulados pelo mesmo agente,
  modelo ou contexto;
- demonstra aplicabilidade universal a partir de uma única execução.

## 5. Baseline comparativo

Antes da execução, deve ser declarado o fluxo usado como baseline. A referência
preferencial é o processo vigente da EKM 1.7, com parecer humano da
especificação, Technical Readiness Review e implementação em execuções
separadas, mas sem a divisão completa entre os papéis especializados deste
protocolo.

Também devem ser registrados:

- projeto, repositório, branch, commit e estado real do worktree;
- commit de `main` do qual a branch exclusiva foi criada;
- versão da EKM e fontes normativas aplicáveis;
- tecnologia e tipo de mudança;
- complexidade e riscos conhecidos;
- dados históricos comparáveis, quando existirem;
- limitações que impeçam comparação direta.

Executar duas vezes a mesma mudança pode introduzir contaminação por aprendizado.
Quando não houver comparação pareada válida, a primeira execução será tratada
como piloto exploratório e não como comprovação de superioridade.

## 6. Contrato comum das etapas

Cada atuação deve declarar antes de começar:

1. papel exercido;
2. objetivo e escopo;
3. checkpoint de entrada;
4. fonte EKM e versão do contrato experimental aplicável;
5. compatibilidade ou normalização exigida desde o checkpoint anterior;
6. fontes obrigatórias;
7. estados esperados;
8. operações permitidas e proibidas;
9. artefato de saída;
10. resultado possível;
11. condição de bloqueio;
12. próximo gate.

Nenhum ator acumula silenciosamente a responsabilidade de outro. Uma ausência
nesse contrato bloqueia somente a etapa afetada e deve ser registrada na
transação `EKM-CHG`.

Os registros de aprovação, implementação, revisão técnica, integridade,
validação funcional e integração são consolidados na mesma transação. O histórico
Git preserva os handoffs. A especificação mantém apenas o comportamento
normativo e o registro da Technical Readiness Review.

## 7. Atores e contratos de responsabilidade

### 7.1 Arquiteto humano

**Entrada:** objetivo da mudança, decisões disponíveis e pareceres produzidos
pelos atores.

**Responsabilidades:**

- definir intenção, prioridade e limites;
- declarar a referência de origem e aprovar a criação da branch;
- resolver decisões de produto e arquitetura;
- emitir ou delegar a responsável humano o parecer sobre a especificação;
- aprovar ou rejeitar a recomendação da Technical Readiness Review;
- autorizar implementação contra checkpoint explícito;
- aceitar ou rejeitar recortes corretivos;
- realizar ou coordenar validação funcional e operacional;
- decidir por integração, repetição ou encerramento.

**Saída:** decisão explícita registrada na transação, com escopo, checkpoint,
data e responsável.

O protagonismo decisório permanece humano. Aprovação não pode ser inferida de
commit, silêncio, parecer técnico ou resultado de agente.

### 7.2 Coordenação do processo

A Coordenação é uma função de governança e orquestração, não uma nova autoridade
arquitetural. Pode ser exercida pelo arquiteto ou por outro coordenador
designado, com ou sem assistência de IA.

**Entrada:** decisão humana aplicável e último checkpoint válido.

**Responsabilidades:**

- registrar referência e commit de origem;
- criar a branch exclusiva da mudança a partir de `main`;
- verificar branch, commit, worktree e estados antes de cada atuação;
- declarar a fonte EKM e a versão do contrato experimental aplicável ao
  handoff, sem exigir fixação por commit nesta fase;
- detectar mudança do contrato desde o checkpoint anterior;
- normalizar artefatos incompatíveis por atuação autorizada ou bloquear o
  handoff, sem atribuir a normalização ao ator seguinte;
- preparar o checkpoint de entrada;
- preservar a ordem dos gates;
- formar o commit resultante de cada etapa quando autorizado;
- registrar operações Git e externas;
- impedir início sobre checkpoint incompatível;
- não converter saída de agente em aprovação implícita.
- distinguir participação humana decisória de intervenção operacional;
- não emitir em nome do arquiteto parecer, aprovação ou aceitação ausente.

**Saída:** checkpoint registrado na transação e worktree limpo para o próximo
ator.

**Bloqueio:** divergência entre branch, commit, worktree, estados, aprovação,
contrato aplicável ou artefatos obrigatórios.

### 7.3 Autor da Especificação

**Entrada:** intenção e decisões fornecidas pelo arquiteto, branch exclusiva,
transação `Open`, fontes EKM e baseline técnico disponível.

O Autor é uma função, não uma exigência de automação. Pode ser uma pessoa, uma
colaboração humano–IA ou um agente. O contrato de saída é o mesmo em qualquer
modalidade.

**Operações permitidas:**

- inspecionar fontes e código para obter fatos;
- elaborar ou corrigir requisitos, contratos, limites, aceite e validações;
- atualizar mapa e transação;
- registrar lacunas e decisões realmente necessárias.

**Operações proibidas:**

- alterar implementação;
- executar a Technical Readiness Review;
- preencher a matriz reservada ao Engenheiro Analista;
- transformar opção não solicitada em decisão bloqueante;
- tratar comportamento fora de escopo como lacuna obrigatória.

**Procedimento:**

1. separar fatos observados, decisões confirmadas, inferências e lacunas;
2. preencher as seções normativas do template;
3. assegurar rastreabilidade entre requisitos e critérios de aceite;
4. classificar explicitamente fora de escopo;
5. manter o registro da Technical Readiness Review como `Pending Review`;
6. encerrar a autoria sem alegar implementabilidade.

**Saída:** especificação `Proposed`, `Not Started`, `Not Ready` e
`Pending Review`, com parecer humano `Pending`, acompanhada de mapa e transação
atualizados.

**Bloqueio:** falta de decisão indispensável para definir o próprio contrato.
Opções não solicitadas, preferências e melhorias futuras não bloqueiam a autoria.

**Próximo gate:** parecer humano da especificação.

### 7.4 Parecer humano da especificação

Este é um gate humano, não um agente obrigatório adicional.

**Entrada:** especificação `Proposed`, parecer `Pending`, checkpoint da autoria,
transação `Open` e intenção conhecida.

**Responsabilidades humanas:**

- confirmar que objetivo, requisitos, limites e decisões representam a intenção;
- registrar responsável, data, checkpoint e ressalvas;
- solicitar revisão quando o documento não representar a intenção;
- não declarar viabilidade técnica sem a análise do Engenheiro Analista.

**Resultados:**

- `Accepted`: segue para o Engenheiro Analista;
- `Revision Required`: retorna ao Autor da Especificação;
- `Pending`: nenhum handoff técnico é autorizado.

O parecer não altera sozinho `Technical readiness`, não autoriza código e não
substitui a aprovação humana posterior para implementação. Nesta fase, sua
evidência é declarativa; o protocolo não verifica automaticamente identidade,
autenticidade ou autoridade.

### 7.5 Engenheiro Analista

**Entrada:** especificação `Proposed`, parecer humano `Accepted`,
`Pending Review`, checkpoint limpo, transação `Open`, baseline técnico
correspondente e contrato EKM aplicável declarado pela Coordenação.

O Analista responde se o contrato aceito é passível de implementação e
verificação no baseline sem inferência relevante. Não decide se a funcionalidade
é desejável, não redefine intenção e não aprova a própria especificação.

**Gate de admissão:**

Antes da Technical Readiness Review, o Analista deve verificar:

1. repositório, branch e SHA;
2. worktree limpo;
3. ID e versão da especificação;
4. estados `Proposed / Pending Review / Not Started / Not Ready`;
5. parecer humano `Accepted`, com responsável, checkpoint e data;
6. transação `Open`;
7. presença dos artefatos da autoria;
8. fonte EKM e versão do contrato declaradas;
9. compatibilidade da especificação e da transação com esse contrato.

O gate produz um resultado próprio:

- `Accepted`: autoriza o início da Technical Readiness Review;
- `Checkpoint Blocked`: interrompe antes da revisão e retorna à Coordenação.

`Checkpoint Blocked` não é resultado da Technical Readiness Review. Nesse caso,
o Analista não altera o metadado `Technical readiness`, não preenche a matriz da
revisão e não tenta normalizar artefatos de outro papel. Seu relatório de
admissão é registrado pela Coordenação no formato compatível disponível.

**Operações permitidas:**

- inspecionar integralmente fontes normativas e implementação;
- preencher exclusivamente o registro da Technical Readiness Review;
- atualizar a transação com o resultado e as lacunas;
- executar verificações reproduzíveis necessárias para avaliar viabilidade;
- recomendar correções sem implementá-las.

**Operações proibidas:**

- alterar código, testes, build ou automações;
- reescrever requisitos para resolver decisões ausentes;
- normalizar silenciosamente artefato incompatível de outro papel;
- autorizar implementação;
- encerrar no primeiro bloqueio.

**Procedimento após `Accepted`:**

1. classificar todos os requisitos e dimensões obrigatórias;
2. classificar toda dúvida ou decisão já declarada na especificação como
   `Blocking`, `Non-blocking`, `Out of scope` ou `Unrequested option`;
3. identificar a natureza de cada lacuna como `Normative`, `Baseline`,
   `Tooling`, `Evidence` ou `None`;
4. confrontar testabilidade, contratos, persistência, segurança,
   compatibilidade, dependências e validações;
5. registrar evidência, impacto e decisão necessária;
6. emitir resultado binário da Technical Readiness Review;
7. reconciliar metadados, seção da revisão, transação e gate seguinte;
8. registrar comandos, resultados, operações e artefatos temporários.

**Saída após `Accepted`:** seção de Technical Readiness Review integral,
referência na transação e relatório operacional da etapa.

**Resultados da Technical Readiness Review:**

- `Implementable`: segue para autorização humana de implementação;
- `Needs Clarification`: retorna ao arquiteto e depois ao Autor da
  Especificação.

O resultado da revisão permanece binário. A natureza da lacuna explica sua
origem, mas não cria um terceiro resultado. O parecer deve deixar explícito
quando a decisão ausente pertence ao comportamento normativo, ao baseline, à
ferramenta ou à suficiência de evidência.

O resultado não altera sozinho o estado normativo nem autoriza implementação.

### 7.6 Engenheiro Implementador

**Entrada:** especificação `Approved` e `Implementable`, autorização humana
registrada, transação `Open`, checkpoint limpo e baseline reconfirmado.

**Operações permitidas:**

- alterar somente os ativos necessários à especificação;
- executar build, testes e validações autorizadas;
- tomar decisões mecânicas privadas sem efeito normativo;
- registrar evidências e decisões locais na transação.

**Operações proibidas:**

- ampliar escopo;
- inventar comportamento, contrato ou compatibilidade;
- corrigir falha preexistente fora do recorte sem autorização;
- declarar validação não executada;
- tratar relatório como alteração de requisito.

**Procedimento:**

1. reconfirmar o checkpoint;
2. rastrear requisito para alteração e evidência;
3. implementar atomicamente o recorte;
4. interromper diante de inferência relevante;
5. executar validações obrigatórias;
6. reconciliar todo o diff com o baseline;
7. registrar relatório na transação.

**Saída:** implementação, testes aplicáveis e relatório contendo requisitos,
arquivos, decisões locais, validações, resultados, desvios, pendências e
operações.

**Resultados:**

- `Implemented`: segue para Tech Lead;
- `Blocked`: retorna ao arquiteto sem alegar conclusão.

### 7.7 Engenheiro Tech Lead

**Entrada:** checkpoint da implementação, especificação aprovada, Technical
Readiness Review, autorização humana, diff completo, relatório e evidências.

**Operações permitidas:** leituras, inspeções e repetição de validações
reproduzíveis já autorizadas.

**Operações proibidas:**

- corrigir diretamente a implementação;
- criar novo requisito;
- substituir preferência técnica por obrigação;
- declarar evidência não reproduzida como própria.

**Procedimento:**

1. validar o checkpoint e o escopo do diff;
2. revisar requisito por requisito;
3. avaliar qualidade, regressões, compatibilidade e suficiência dos testes;
4. confrontar o relatório com as mudanças reais;
5. classificar cada achado como desvio, risco, decisão necessária ou
   recomendação não bloqueante;
6. produzir parecer e, quando necessário, recorte corretivo.

**Saída:** parecer registrado na transação com matriz requisito, evidência,
resultado, severidade e correção requerida.

**Resultados:**

- `Aprovada`: segue para Validador de Integridade;
- `Correção necessária`: retorna ao arquiteto e, após autorização, ao
  Implementador;
- `Decisão do arquiteto necessária`: retorna ao arquiteto;
- `Não verificável`: retorna ao arquiteto com a evidência ausente.

### 7.8 Validador de Integridade da EKM

**Entrada:** checkpoint aprovado pelo Tech Lead e todos os artefatos da
transação.

**Operações permitidas:** auditoria read-only do processo, fontes, checkpoints e
evidências.

**Operações proibidas:**

- repetir a Technical Readiness Review como Engenheiro Analista;
- reavaliar preferência técnica já aderente à especificação;
- corrigir código ou documentos;
- redefinir requisitos;
- substituir evidência ausente por inferência.

**Procedimento:**

1. validar a sequência dos checkpoints;
2. verificar separação dos papéis;
3. verificar parecer humano da especificação, Technical Readiness Review,
   aprovação para implementação e reconfirmação;
4. verificar rastreabilidade, proteção normativa e reconciliação;
5. conferir estados, desvios, pendências e operações;
6. classificar cada controle como `Compliant`, `Non-compliant`,
   `Not verifiable`, `Blocked` ou `Not Applicable`;
7. derivar a conclusão geral sem ocultar itens individuais.

Cada handoff é auditado contra o contrato declarado quando ocorreu. Controle
introduzido posteriormente recebe `Not Applicable`, com a versão que justifica
a classificação, e não produz não conformidade retroativa.

**Saída:** relatório de integridade read-only. A Coordenação o registra na
transação sem alterar seu conteúdo semântico e forma o checkpoint seguinte.

**Conclusões gerais:**

- `Conforme`;
- `Conforme com ressalvas`;
- `Não conforme`;
- `Não verificável`;
- `Blocked`.

`Conforme` exige que todos os controles aplicáveis estejam `Compliant`;
controles `Not Applicable` não alteram a conclusão.

**Próximo gate:** validação funcional humana quando não houver bloqueio.

### 7.9 Validação funcional humana, integração e encerramento

**Entrada:** implementação aprovada tecnicamente, processo auditado e
checkpoint limpo.

**Responsabilidade humana:**

- executar ou coordenar validações funcionais e operacionais;
- registrar ambiente, procedimento, resultado e evidência;
- decidir sobre `Validated` e `Ready for Integration`;
- autorizar integração;
- comprovar chegada à referência de produção;
- reconciliar especificação, mapa, transação e estados após o merge.

A validação funcional humana é um gate esperado de governança. Sua existência
não representa falta de autonomia do modelo. A Coordenação deve registrar
ambiente, procedimento, resultado e evidência sem transformar a decisão em
saída de agente.

**Resultados:**

- validação aprovada: `Validated / Ready for Integration`;
- validação reprovada: retorno ao arquiteto para recorte corretivo;
- integração comprovada em `main`: `Active / Validated / Done`, com fechamento
  da transação;
- integração ausente: transação permanece `Open`.

## 8. Fluxo e gates

```text
Objetivo e referência `main` definidos pelo arquiteto
          ↓
Preparação da mudança e registro do baseline
          ↓
Branch exclusiva derivada de `main`
          ↓
Autor da Especificação
          ↓
Especificação `Proposed / Pending Review`, parecer humano `Pending`
          ↓
Checkpoint commitado da autoria
          ↓
Parecer humano da especificação
    ├─ Revision Required → Autor da Especificação
    └─ Accepted
          ↓
Checkpoint do parecer humano
          ↓
Engenheiro Analista
          ↓
Gate de admissão
    ├─ Checkpoint Blocked → Coordenação → normalização ou novo handoff
    └─ Accepted
          ↓
Technical Readiness Review integral
    ├─ Needs Clarification → decisão/correção humana → nova revisão integral
    └─ Implementable
          ↓
Autorização humana explícita para implementação
          ↓
Checkpoint aprovado para implementação
          ↓
Engenheiro Implementador
          ↓
Reconfirmação do baseline → implementação → build/testes → relatório
          ↓
Checkpoint da implementação
          ↓
Engenheiro Tech Lead
    ├─ correção ou decisão necessária → arquiteto → novo ciclo autorizado
    └─ Aprovada
          ↓
Checkpoint da revisão técnica
          ↓
Validador de Integridade da EKM
    ├─ Não conforme, Não verificável ou Blocked → arquiteto
    └─ Conforme ou Conforme com ressalvas
          ↓
Validação funcional/operacional humana
          ↓
Ready for Integration
          ↓
Integração em `main` e reconciliação
          ↓
Active / Validated / Done e transação fechada
          ↓
Retrospectiva e decisão experimental
```

Nenhum parecer posterior corrige retroativamente um gate ausente. Se uma etapa
obrigatória não tiver ocorrido no momento devido, o desvio deve permanecer
registrado como evidência do experimento.

### 8.1 Branch exclusiva da mudança

Toda especificação funcional submetida a este experimento deve ser criada em
uma nova branch exclusiva, derivada obrigatoriamente de `main`.

Antes da primeira alteração da especificação, devem existir:

- referência explícita a `main` como origem;
- commit de origem registrado;
- estado real do worktree de origem registrado;
- branch da mudança criada;
- transação `EKM-CHG` identificada e `Open`.

A branch contém o ciclo completo da mudança: especificação, revisões, decisões,
implementação, correções, relatórios e evidências. Criá-la não aprova a
especificação nem autoriza implementação.

Correções identificadas depois da implementação devem retornar à branch da
mudança e percorrer novamente os gates afetados. Alterações diretas nas branches
de promoção não substituem esse ciclo.

Quando um repositório ainda não possuir a fundação EKM, sua adoção documental
deve ocorrer como mudança precedente e separada. A fundação deve alcançar
`main` antes que a branch da primeira especificação funcional seja derivada.

### 8.2 Checkpoint de entrada dos atores

Toda etapa ou operação de agente deve começar a partir de um commit explícito. O
checkpoint de entrada contém:

- repositório e branch;
- SHA completo do commit;
- confirmação de worktree limpo;
- ID e versão da especificação;
- estado normativo;
- estado da implementação;
- estado da entrega;
- resultado da Technical Readiness Review;
- parecer humano da especificação;
- identificador e estado da transação `EKM-CHG`;
- caminho da fonte EKM e versão do contrato experimental aplicável;
- compatibilidade, migração ou normalização desde o checkpoint anterior;
- artefatos e pareceres obrigatórios das etapas anteriores;
- parecer ou autorização humana aplicável.

O ator deve validar o checkpoint antes de atuar. Branch, commit, worktree,
estado ou evidência incompatível com o gate esperado bloqueia a operação e deve
ser reportado.

O apontamento dinâmico para a EKM não exige fixação ou validação por SHA nesta
fase. Ainda assim, a Coordenação deve declarar a versão do contrato usada no
handoff e tratar incompatibilidades introduzidas desde o checkpoint anterior.
Essa declaração registra semântica de processo, não integridade criptográfica.

Essa exigência não substitui a regra EKM de observar o worktree real. O worktree
continua sendo verificado, mas qualquer diferença não commitada no início de um
handoff constitui violação do checkpoint.

### 8.3 Saída e formação do próximo checkpoint

A saída de um ator não autoriza automaticamente a etapa seguinte. O ciclo de
handoff é:

```text
checkpoint de entrada
        ↓
operação do ator
        ↓
artefatos, alterações e relatório
        ↓
revisão ou aprovação aplicável
        ↓
novo commit de checkpoint
        ↓
próximo ator
```

O commit de checkpoint deve preservar a saída da etapa anterior e o estado
atual da especificação. O próximo ator recebe esse commit como entrada
imutável.

Quando a etapa exigir decisão humana, o checkpoint seguinte somente pode ser
formado depois que a decisão estiver registrada. A existência de um commit não
é, isoladamente, evidência de aprovação.

### 8.4 Estados e ownership

| Gate concluído | Estado normativo | Parecer humano da especificação | Technical readiness | Implementação | Entrega | Responsável pelo registro |
|---|---|---|---|---|---|---|
| Autoria em andamento | `Draft` | `Pending` | `Pending Review` | `Not Started` | `Not Ready` | Autor da Especificação |
| Autoria concluída | `Proposed` | `Pending` | `Pending Review` | `Not Started` | `Not Ready` | Autor da Especificação |
| Intenção aceita | `Proposed` | `Accepted` | `Pending Review` | `Not Started` | `Not Ready` | Coordenação após parecer humano |
| Análise aprovada | `Proposed` | `Accepted` | `Implementable` | `Not Started` | `Not Ready` | Engenheiro Analista |
| Aprovação para implementação | `Approved` | `Accepted` | `Implementable` | `Not Started` | `Not Ready` | Coordenação após decisão humana |
| Implementação concluída | `Approved` | `Accepted` | `Implementable` | `Implemented` | `Not Ready` | Engenheiro Implementador |
| Tech Lead aprovado | `Approved` | `Accepted` | `Implementable` | `Implemented` | `Not Ready` | Tech Lead registra parecer; não avança implementação |
| Integridade conforme | `Approved` | `Accepted` | `Implementable` | `Implemented` | `Not Ready` | Validador registra conformidade; não avança implementação |
| Validação funcional aprovada | `Approved` | `Accepted` | `Implementable` | `Validated` | `Ready for Integration` | Coordenação após decisão humana |
| Integração comprovada em `main` | `Active` | `Accepted` | `Implementable` | `Validated` | `Done` | Coordenação após integração |

Resultado negativo não avança automaticamente estado. O parecer deve indicar o
gate de retorno. Somente a coordenação aplica transição dependente de decisão
humana ou integração.

O gate de admissão não altera estados. `Accepted` apenas permite iniciar a
revisão; `Checkpoint Blocked` preserva os estados recebidos.

### 8.5 Promoção prevista

O pipeline pretendido para adoção futura é:

```text
main
  ↓
branch exclusiva da especificação e desenvolvimento
  ↓
qa
  ↓
homolog
  ↓
main
```

Neste estágio, apenas a criação da branch exclusiva a partir de `main` e os
checkpoints dentro dela são exigidos pelo experimento.

As branches `qa` e `homolog` são capacidades previstas, mas ainda não
obrigatórias. Sua implementação futura deverá especificar, experimentar e
aprovar ao menos:

- se são permanentes, compartilhadas ou isoladas por mudança;
- unidade de promoção: commit, merge, release ou artefato;
- tratamento de mudanças concorrentes;
- critérios de entrada e saída;
- validações e aprovações de cada ambiente;
- rastreabilidade entre commits, artefatos e deploys;
- estratégia de correção, reversão e nova promoção.

Enquanto essa definição não existir, nenhum projeto pode alegar conformidade
com um pipeline EKM de `qa` e `homolog` apenas pela existência dessas branches.
O estado `Done` continua condicionado à integração comprovada na referência de
produção declarada.

### 8.6 Ciclos de retorno

- `Checkpoint Blocked`: retorna à Coordenação sem executar a etapa. A causa é
  corrigida por atuação autorizada do papel responsável, e um novo checkpoint
  é formado antes de repetir o gate de admissão;
- `Needs Clarification`: retorna ao arquiteto e ao Autor da Especificação. A
  correção produz novo checkpoint `Proposed / Pending Review`, exige novo
  parecer humano e invalida a revisão anterior.
- `Revision Required` no parecer humano: retorna à autoria antes da Technical
  Readiness Review. A correção exige novo parecer sobre o checkpoint resultante.
- `Blocked` durante implementação: nenhum item pode ser apresentado como
  implementação concluída. Se o bloqueio exigir mudança normativa, o fluxo
  retorna à autoria; se for operacional, retorna ao arquiteto.
- `Correção necessária` do Tech Lead: quando o contrato permanece inalterado,
  retorna ao Implementador com recorte aprovado. Quando exige novo requisito ou
  decisão, retorna à autoria, análise e autorização humana.
- `Não conforme`, `Não verificável` ou `Blocked` no Validador: retorna ao gate
  que originou a violação ou a ausência de evidência. O relatório original
  permanece preservado e uma nova validação é executada após o checkpoint
  corretivo.
- validação funcional reprovada: retorna ao arquiteto. Correção aderente ao
  contrato volta ao Implementador; mudança de comportamento volta à autoria.

Qualquer mudança material na especificação invalida o parecer humano da
especificação, a Technical Readiness Review, a autorização para implementação e
os checkpoints posteriores. Nenhum retorno apaga parecer ou evidência anterior.

## 9. Isolamento e simulação manual

Cada atuação deve ocorrer em execução identificável e produzir um artefato
imutável de handoff. Para cada execução, registrar:

- ator;
- responsável pela simulação;
- agente e modelo, quando aplicável;
- data e identificador da sessão;
- checkpoint de entrada;
- entradas disponibilizadas;
- contexto deliberadamente omitido;
- saída produzida;
- consumo de tempo e tokens, quando disponível;
- participação humana, distinguindo gates decisórios e intervenções
  operacionais.

Aplicam-se os seguintes controles:

- um ator recebe somente as entradas previstas para sua responsabilidade;
- conclusões de um ator não podem ser silenciosamente reescritas por outro;
- correções geram nova versão ou adendo rastreável;
- o Implementador não recebe raciocínios privados do Analista, apenas seu
  artefato formal aprovado;
- o Tech Lead e o Validador registram achados próprios e distinguem achados
  novos de repetições;
- o uso do mesmo agente, modelo ou sessão deve ser declarado como limitação;
- o mesmo contexto não deve ser apresentado como evidência de independência.

## 10. Evidências obrigatórias

Uma execução deve preservar:

1. versão deste protocolo;
2. fonte EKM declarada pelo projeto e consultada em cada etapa; nesta fase, o
   apontamento pode ser dinâmico e não exige fixação por commit;
3. versão do contrato experimental declarada em cada handoff;
4. compatibilidade, migração ou normalização aplicada;
5. especificação submetida;
6. referência `main`, commit de origem e baseline inicial;
7. evidência de criação da branch exclusiva;
8. checkpoint de entrada e commit resultante de cada etapa;
9. parecer humano da especificação;
10. resultado do gate de admissão do Engenheiro Analista;
11. parecer, matrizes e evidências operacionais do Engenheiro Analista;
12. aprovação humana para implementação;
13. reconfirmação anterior à implementação;
14. relatório do Engenheiro Implementador;
15. diff completo, builds, testes e validações;
16. parecer do Engenheiro Tech Lead;
17. relatório do Validador de Integridade da EKM;
18. validação funcional e operacional humana;
19. decisão humana de integração;
20. registro de ciclos corretivos;
21. métricas e retrospectiva consolidada;
22. decisão experimental.

Ausência de uma evidência deve ser registrada; não pode ser convertida em
resultado positivo por inferência.

## 11. Métricas

### 11.1 Confiança, qualidade e aderência

- confiança declarada pelo arquiteto e evidências que a sustentam;
- requisitos atendidos, parcialmente atendidos e não atendidos;
- ambiguidades, conflitos e lacunas encontrados antes do código;
- mudanças não autorizadas;
- regressões e defeitos encontrados antes e depois da validação humana;
- falhas escapadas para validação funcional ou integração;
- suficiência e reprodutibilidade das validações.

### 11.2 Valor incremental por ator

Cada achado deve ser classificado como:

- `Exclusivo`: ainda não registrado por outro ator;
- `Confirmatório`: confirma, com evidência própria, achado anterior;
- `Duplicado`: repete achado sem evidência ou consequência adicional;
- `Falso positivo`: não se sustenta após análise;
- `Fora de escopo`: não pertence à responsabilidade do ator.

Também devem ser registrados a severidade, o momento da detecção e o retrabalho
evitado ou provocado.

### 11.3 Custo operacional

- tempo por ator e tempo total;
- tokens ou custo estimado, quando disponíveis;
- volume de contexto e artefatos transferidos;
- quantidade de handoffs;
- quantidade de checkpoints formados ou rejeitados;
- violações de branch, commit, worktree ou estado encontradas nos handoffs;
- quantidade de ciclos corretivos;
- gates e decisões humanas planejadas;
- intervenções operacionais humanas não planejadas;
- esforço de preparação e auditoria das evidências.

### 11.4 Efeito sobre o arquiteto

- decisões humanas previstas efetivamente exercidas;
- tempo dedicado a decisões versus atividades operacionais;
- perguntas repetidas;
- confiança e facilidade de localizar a evidência;
- aprendizado reutilizável produzido pelo experimento.

## 12. Interpretação dos resultados

A primeira execução será um piloto do protocolo. Ela poderá:

- confirmar que os contratos e handoffs são executáveis;
- revelar sobreposição, lacunas ou conflitos entre papéis;
- indicar métricas inviáveis ou ausentes;
- produzir evidência preliminar de benefício ou custo.

Participação humana em pareceres, aprovações, validação funcional e decisão de
integração é resultado esperado da governança. Sua quantidade não constitui,
isoladamente, resultado negativo. A avaliação deve observar confiança, tempo de
entrega e proporção entre decisão de valor e coordenação operacional.

Ela não será suficiente, isoladamente, para incorporar o modelo ao método
vigente.

O modelo será candidato a novos experimentos quando houver achados materiais
exclusivos ou confirmação independente relevante, com custo observável e
compatível com o risco da mudança.

O modelo deverá ser ajustado quando houver benefício, mas também duplicação
excessiva, responsabilidades conflitantes, isolamento insuficiente ou custo
desproporcional.

A formulação experimentada poderá ser descartada quando não produzir valor
incremental material, provocar mais falhas ou retrabalho do que evita, ou exigir
coordenação incompatível com o benefício observado. Descartar a formulação não
autoriza omitir as evidências negativas.

Qualquer proposta de incorporação à EKM exige repetição em casos suficientemente
diversos, comparação com baseline e uma mudança governada separadamente.

## 13. Registro da execução

Cada execução deve ser registrada em documento separado, sem alterar este
protocolo retroativamente. O registro deve conter:

1. contexto;
2. hipótese avaliada;
3. baseline;
4. branch da mudança e commit de origem em `main`;
5. checkpoints e estados da especificação;
6. atores, modelos e isolamento;
7. cronologia e artefatos;
8. achados por gate;
9. métricas;
10. resultado técnico;
11. resultado de integridade EKM;
12. limitações;
13. retrospectiva;
14. decisão: repetir, ajustar, propor adoção ou descartar.

Mudanças futuras neste protocolo devem possuir motivação e histórico próprios.

Execuções registradas:

- [`COORDINATED-ACTOR-MODEL-RUN-001.md`](COORDINATED-ACTOR-MODEL-RUN-001.md):
  execução do reset de settings no SmartHome-DeviceApi até a validação manual
  e aceitação humanas.

Estudo de caso:

- [`SMARTHOME-DEVICEAPI-COORDINATED-ACTORS.md`](../case-studies/SMARTHOME-DEVICEAPI-COORDINATED-ACTORS.md):
  resultado técnico e metodológico parcial da Execução 001.

## 14. Evidência que motivou a versão 0.3

A primeira atuação isolada do Autor da Especificação ocorreu no
SmartHome-DeviceApi e produziu o checkpoint
`eb5ed262dfa830f62aa936bb02ce7420780fdd3d`.

O agente:

- criou corretamente branch derivada de `main`, transação, especificação, mapa
  e commit documental;
- preservou o escopo e não alterou implementação;
- registrou o contrato funcional fornecido;
- preencheu parcialmente a Technical Readiness Review apesar de declarar que
  não a executou;
- tratou opções não solicitadas e um item fora de escopo como decisões
  pendentes;
- não declarou uma transação anterior que permanecia aberta e desatualizada
  após merge.

Essas evidências mostraram que descrição de responsabilidade sem contrato de
etapa e ownership de saída não era suficiente. A versão 0.3 introduziu:

- contrato comum para todas as etapas;
- Autor da Especificação como atuação explícita;
- ownership entre especificação, review e transação;
- estados e gates de handoff;
- registros mínimos de cada ator na mesma `EKM-CHG`;
- Validador de Integridade separado do Engenheiro Analista e do Tech Lead;
- ciclos de retorno e reconciliação pós-integração.

A evidência provém de uma única autoria e não comprova ainda a eficácia do fluxo
completo. Na publicação da versão 0.3, Engenheiro Analista, Implementador, Tech
Lead, Validador e integração permaneciam por experimentar. A primeira atuação
posterior do Engenheiro Analista está preservada no registro da Execução 001.

## 15. Evidência que motivou a versão 0.4

O Engenheiro Analista da Execução 001 produziu o checkpoint
`a3cbb556d3388d2987da1e87b46c20c97945ff65` após consultar o protocolo 0.3.

A atuação:

- analisou cumulativamente os requisitos funcionais;
- preservou a separação entre revisão e implementação;
- identificou uma falha preexistente que impedia as validações obrigatórias;
- aceitou como válido um checkpoint ainda em `Draft`;
- não tratou a incompatibilidade entre os artefatos 0.2 e o contrato 0.3;
- não classificou decisões artificiais deixadas pela autoria;
- deixou inconsistência entre o resultado da revisão e o encerramento da
  transação;
- não registrou integralmente comandos, resultados e artefatos temporários.

O protocolo havia mudado entre os checkpoints do Autor e do Analista. Como a
fonte EKM é dinâmica e não exige fixação por commit nesta fase, a execução
também revelou ausência de responsabilidade explícita para compatibilidade de
transações em andamento.

A versão 0.4 introduziu experimentalmente:

- declaração do contrato EKM aplicável em cada handoff;
- responsabilidade da Coordenação por compatibilidade e normalização;
- gate de admissão do Engenheiro Analista;
- `Checkpoint Blocked` separado do resultado da Technical Readiness Review;
- classificação da natureza das lacunas;
- classificação obrigatória de dúvidas e decisões já declaradas;
- reconciliação de saída e evidência operacional do Analista;
- controles correspondentes nos templates e na auditoria.

O resultado da Technical Readiness Review permanece binário no protocolo 0.4.
As mudanças foram repetidas uma vez no mesmo caso, conforme o registro da
Execução 001, mas ainda precisam ser observadas em casos diferentes antes de
qualquer proposta de incorporação ao método de referência.

## 16. Alinhamento de governança e versão 0.5

A avaliação parcial da Execução 001 tratou inicialmente a quantidade de
intervenções humanas como possível limitação do modelo. A discussão posterior
identificou que essa interpretação contrariava a premissa da EKM.

O objetivo próximo não é extinguir interação humana nem transferir
responsabilidade final aos agentes. O modelo deve priorizar:

1. governança das decisões e responsabilidades;
2. confiança e rastreabilidade da entrega;
3. velocidade e capacidade de execução;
4. preservação do conhecimento;
5. redução de coordenação operacional desnecessária.

A versão 0.5:

- torna explícita a autonomia governada;
- permite autoria humana, assistida ou por agente, sem exigir automação;
- introduz parecer humano da especificação antes da análise técnica;
- restringe o Analista à avaliação de implementabilidade;
- separa parecer da intenção, autorização para implementar, validação funcional
  e decisão de integração;
- caracteriza a Coordenação como função de governança e orquestração;
- distingue gates humanos planejados de intervenção operacional e retrabalho.

A Execução 001 ocorreu sob contratos anteriores e não pode receber
retroativamente um gate que não existia. Sua reavaliação registra a ausência de
parecer humano formal anterior à análise como evidência histórica, não como
violação retroativa.
