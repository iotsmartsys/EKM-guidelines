# Experimento — Modelo de coordenação por atores

**Status:** Experimental / In Progress

**Natureza:** protocolo experimental não normativo  
**Modelo EKM de referência:** 1.6  
**Versão do protocolo:** 0.3

**Branch do experimento:** `modelo_de_coordenacao_por_atores`  
**Resultado:** piloto iniciado; fluxo completo ainda não executado

## 1. Contexto

O modelo EKM 1.6 separa Technical Readiness Review, aprovação humana,
implementação e reconciliação, mas não exige que essas responsabilidades sejam
exercidas por agentes diferentes. A coordenação entre múltiplos agentes e a
separação automatizada de responsabilidades permanecem questões em aberto.

Este experimento avaliará uma forma de trabalho coordenada por atores
especializados. Na primeira execução, os atores poderão ser simulados
manualmente em execuções separadas. O protocolo não altera o método de
referência vigente. Os templates ajustados nesta branch pertencem ao experimento
e não passam a reger projetos adotantes sem decisão explícita.

## 2. Pergunta experimental

A separação coordenada entre análise, implementação, revisão técnica e auditoria
da EKM aumenta a aderência da implementação à especificação e reduz falhas ou
retrabalho, mantendo custo operacional aceitável?

## 3. Hipóteses

### 3.1 Hipótese principal

A separação de responsabilidades detecta, antes da validação funcional humana,
desvios materiais que não seriam detectados pelo fluxo vigente quando as
responsabilidades são concentradas.

### 3.2 Hipóteses secundárias

- o Engenheiro Analista reduz ambiguidades e decisões ausentes que chegariam à
  implementação;
- o Engenheiro Tech Lead identifica divergências entre a especificação aprovada,
  o código e o relatório de implementação;
- o Validador de Integridade da EKM identifica violações metodológicas que uma
  revisão exclusivamente técnica não detectaria;
- handoffs explícitos produzem evidências localizáveis, auditáveis e
  reutilizáveis;
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
- handoffs entre atores baseados em checkpoints commitados;
- aprovação humana explícita;
- implementação da especificação aprovada;
- build e testes aplicáveis;
- revisão técnica independente;
- auditoria de integridade contra a EKM;
- validação funcional e decisão final humanas;
- medição dos resultados e retrospectiva.

O experimento não:

- modifica o modelo EKM 1.6;
- autoriza implementação sem Technical Readiness Review e aprovação humana;
- transfere decisões de produto ou arquitetura aos atores de IA;
- substitui testes, validação em hardware ou validação humana;
- torna `qa` ou `homolog` obrigatórias antes que seu processo de promoção seja
  especificado e validado;
- alega independência real quando os atores forem simulados pelo mesmo agente,
  modelo ou contexto;
- demonstra aplicabilidade universal a partir de uma única execução.

## 5. Baseline comparativo

Antes da execução, deve ser declarado o fluxo usado como baseline. A referência
preferencial é o processo vigente da EKM 1.6, com Technical Readiness Review e
implementação em execuções separadas, mas sem a divisão completa entre os
papéis especializados deste protocolo.

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
4. fontes obrigatórias;
5. estados esperados;
6. operações permitidas e proibidas;
7. artefato de saída;
8. resultado possível;
9. condição de bloqueio;
10. próximo gate.

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
- aprovar ou rejeitar especificação e Technical Readiness Review;
- autorizar implementação contra checkpoint explícito;
- aceitar ou rejeitar recortes corretivos;
- realizar ou coordenar validação funcional e operacional;
- decidir por integração, repetição ou encerramento.

**Saída:** decisão explícita registrada na transação, com escopo, checkpoint,
data e responsável.

O protagonismo decisório permanece humano. Aprovação não pode ser inferida de
commit, silêncio, parecer técnico ou resultado de agente.

### 7.2 Coordenação do processo

A coordenação é uma função operacional, não um novo papel arquitetural. Pode ser
exercida pelo arquiteto e futuramente por um orquestrador.

**Entrada:** decisão humana aplicável e último checkpoint válido.

**Responsabilidades:**

- registrar referência e commit de origem;
- criar a branch exclusiva da mudança a partir de `main`;
- verificar branch, commit, worktree e estados antes de cada atuação;
- preparar o checkpoint de entrada;
- preservar a ordem dos gates;
- formar o commit resultante de cada etapa quando autorizado;
- registrar operações Git e externas;
- impedir início sobre checkpoint incompatível;
- não converter saída de agente em aprovação implícita.

**Saída:** checkpoint registrado na transação e worktree limpo para o próximo
ator.

**Bloqueio:** divergência entre branch, commit, worktree, estados, aprovação ou
artefatos obrigatórios.

### 7.3 Autor da Especificação

**Entrada:** intenção e decisões fornecidas pelo arquiteto, branch exclusiva,
transação `Open`, fontes EKM e baseline técnico disponível.

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
`Pending Review`, acompanhada de mapa e transação atualizados.

**Bloqueio:** falta de decisão indispensável para definir o próprio contrato.
Opções não solicitadas, preferências e melhorias futuras não bloqueiam a autoria.

**Próximo gate:** Engenheiro Analista.

### 7.4 Engenheiro Analista

**Entrada:** especificação `Proposed`, `Pending Review`, checkpoint limpo,
transação `Open` e baseline técnico correspondente.

**Operações permitidas:**

- inspecionar integralmente fontes normativas e implementação;
- preencher exclusivamente o registro da Technical Readiness Review;
- atualizar a transação com o resultado e as lacunas;
- recomendar correções sem implementá-las.

**Operações proibidas:**

- alterar código, testes, build ou automações;
- reescrever requisitos para resolver decisões ausentes;
- autorizar implementação;
- encerrar no primeiro bloqueio.

**Procedimento:**

1. validar o checkpoint;
2. classificar todos os requisitos e dimensões obrigatórias;
3. distinguir lacuna indispensável, item fora de escopo e opção não requerida;
4. confrontar testabilidade, contratos, persistência, segurança,
   compatibilidade, dependências e validações;
5. registrar evidência, impacto e decisão necessária;
6. emitir resultado binário.

**Saída:** seção de Technical Readiness Review integral e referência na
transação.

**Resultados:**

- `Implementable`: segue para aprovação humana;
- `Needs Clarification`: retorna ao arquiteto e depois ao Autor da
  Especificação.

O resultado não altera sozinho o estado normativo nem autoriza implementação.

### 7.5 Engenheiro Implementador

**Entrada:** especificação `Approved` e `Implementable`, aprovação humana
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

### 7.6 Engenheiro Tech Lead

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

### 7.7 Validador de Integridade da EKM

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
3. verificar Technical Readiness Review, aprovação e reconfirmação;
4. verificar rastreabilidade, proteção normativa e reconciliação;
5. conferir estados, desvios, pendências e operações;
6. classificar cada controle como `Compliant`, `Non-compliant`,
   `Not verifiable` ou `Blocked`;
7. derivar a conclusão geral sem ocultar itens individuais.

**Saída:** relatório de integridade read-only. A Coordenação o registra na
transação sem alterar seu conteúdo semântico e forma o checkpoint seguinte.

**Conclusões gerais:**

- `Conforme`;
- `Conforme com ressalvas`;
- `Não conforme`;
- `Não verificável`;
- `Blocked`.

**Próximo gate:** validação funcional humana quando não houver bloqueio.

### 7.8 Validação funcional, integração e encerramento

**Entrada:** implementação aprovada tecnicamente, processo auditado e
checkpoint limpo.

**Responsabilidade humana:**

- executar ou coordenar validações funcionais e operacionais;
- registrar ambiente, procedimento, resultado e evidência;
- decidir sobre `Validated` e `Ready for Integration`;
- autorizar integração;
- comprovar chegada à referência de produção;
- reconciliar especificação, mapa, transação e estados após o merge.

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
Especificação `Proposed / Pending Review` e transação EKM
          ↓
Checkpoint commitado da especificação
          ↓
Engenheiro Analista
          ↓
Technical Readiness Review integral
    ├─ Needs Clarification → decisão/correção humana → nova revisão integral
    └─ Implementable
          ↓
Aprovação humana explícita
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
- identificador e estado da transação `EKM-CHG`;
- artefatos e pareceres obrigatórios das etapas anteriores;
- aprovação humana aplicável.

O ator deve validar o checkpoint antes de atuar. Branch, commit, worktree,
estado ou evidência incompatível com o gate esperado bloqueia a operação e deve
ser reportado.

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

| Gate concluído | Estado normativo | Technical readiness | Implementação | Entrega | Responsável pelo registro |
|---|---|---|---|---|---|
| Autoria em andamento | `Draft` | `Pending Review` | `Not Started` | `Not Ready` | Autor da Especificação |
| Autoria concluída | `Proposed` | `Pending Review` | `Not Started` | `Not Ready` | Autor da Especificação |
| Análise aprovada | `Proposed` | `Implementable` | `Not Started` | `Not Ready` | Engenheiro Analista |
| Aprovação humana | `Approved` | `Implementable` | `Not Started` | `Not Ready` | Coordenação após decisão humana |
| Implementação concluída | `Approved` | `Implementable` | `Implemented` | `Not Ready` | Engenheiro Implementador |
| Tech Lead aprovado | `Approved` | `Implementable` | `Implemented` | `Not Ready` | Tech Lead registra parecer; não avança implementação |
| Integridade conforme | `Approved` | `Implementable` | `Implemented` | `Not Ready` | Validador registra conformidade; não avança implementação |
| Validação funcional aprovada | `Approved` | `Implementable` | `Validated` | `Ready for Integration` | Coordenação após decisão humana |
| Integração comprovada em `main` | `Active` | `Implementable` | `Validated` | `Done` | Coordenação após integração |

Resultado negativo não avança automaticamente estado. O parecer deve indicar o
gate de retorno. Somente a coordenação aplica transição dependente de decisão
humana ou integração.

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

- `Needs Clarification`: retorna ao arquiteto e ao Autor da Especificação. A
  correção produz novo checkpoint `Proposed / Pending Review` e invalida a
  revisão anterior.
- `Blocked` durante implementação: nenhum item pode ser apresentado como
  implementação concluída. Se o bloqueio exigir mudança normativa, o fluxo
  retorna à autoria; se for operacional, retorna ao arquiteto.
- `Correção necessária` do Tech Lead: quando o contrato permanece inalterado,
  retorna ao Implementador com recorte aprovado. Quando exige novo requisito ou
  decisão, retorna à autoria, análise e aprovação humana.
- `Não conforme`, `Não verificável` ou `Blocked` no Validador: retorna ao gate
  que originou a violação ou a ausência de evidência. O relatório original
  permanece preservado e uma nova validação é executada após o checkpoint
  corretivo.
- validação funcional reprovada: retorna ao arquiteto. Correção aderente ao
  contrato volta ao Implementador; mudança de comportamento volta à autoria.

Qualquer mudança material na especificação invalida Technical Readiness Review,
aprovação e checkpoints posteriores. Nenhum retorno apaga parecer ou evidência
anterior.

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
- intervenções humanas.

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
3. especificação submetida;
4. referência `main`, commit de origem e baseline inicial;
5. evidência de criação da branch exclusiva;
6. checkpoint de entrada e commit resultante de cada etapa;
7. parecer e matriz do Engenheiro Analista;
8. decisões e aprovação do arquiteto;
9. reconfirmação anterior à implementação;
10. relatório do Engenheiro Implementador;
11. diff completo, builds, testes e validações;
12. parecer do Engenheiro Tech Lead;
13. relatório do Validador de Integridade da EKM;
14. validação funcional e operacional;
15. registro de ciclos corretivos;
16. métricas e retrospectiva consolidada;
17. decisão experimental.

Ausência de uma evidência deve ser registrada; não pode ser convertida em
resultado positivo por inferência.

## 11. Métricas

### 11.1 Qualidade e aderência

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
- intervenções e decisões humanas;
- esforço de preparação e auditoria das evidências.

### 11.4 Efeito sobre o arquiteto

- decisões que exigiram participação humana;
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
  autoria e Technical Readiness Review da especificação de reset de settings no
  SmartHome-DeviceApi.

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
