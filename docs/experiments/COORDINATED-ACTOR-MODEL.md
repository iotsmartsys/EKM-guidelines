# Experimento — Modelo de coordenação por atores

**Status:** Proposed  
**Natureza:** protocolo experimental não normativo  
**Modelo EKM de referência:** 1.6  
**Versão do protocolo:** 0.2

**Branch do experimento:** `modelo_de_coordenacao_por_atores`  
**Resultado:** ainda não executado

## 1. Contexto

O modelo EKM 1.6 separa Technical Readiness Review, aprovação humana,
implementação e reconciliação, mas não exige que essas responsabilidades sejam
exercidas por agentes diferentes. A coordenação entre múltiplos agentes e a
separação automatizada de responsabilidades permanecem questões em aberto.

Este experimento avaliará uma forma de trabalho coordenada por atores
especializados. Na primeira execução, os atores poderão ser simulados
manualmente em execuções separadas. O protocolo não altera o método vigente, os
templates ou as regras aplicáveis aos projetos adotantes.

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
implementação em execuções separadas, mas sem a divisão completa em quatro
atores.

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

## 6. Atores e contratos de responsabilidade

### 6.1 Arquiteto humano

Responsável por:

- definir objetivo, especificação e limites;
- declarar a referência de origem e aprovar a criação da branch da mudança;
- resolver decisões de produto e arquitetura;
- aprovar ou rejeitar a recomendação da Technical Readiness Review;
- autorizar explicitamente a implementação contra um baseline registrado;
- realizar ou coordenar a validação funcional e operacional;
- decidir por correção, repetição, integração ou encerramento;
- decidir futuramente se as evidências justificam mudança na EKM.

O protagonismo decisório permanece humano durante todo o experimento.

### 6.2 Coordenação do processo

A coordenação do processo é uma função operacional, não um novo papel de decisão
arquitetural. Na primeira execução, ela pode ser exercida pelo arquiteto humano.
Futuramente, poderá ser automatizada por um orquestrador.

Responsável por:

- registrar a referência e o commit de origem aprovados;
- criar a branch exclusiva da mudança a partir de `main`;
- verificar branch, commit, worktree e estados antes de cada atuação;
- preparar e registrar o checkpoint de entrada de cada ator;
- preservar a ordem dos gates e impedir início sobre checkpoint incompatível;
- registrar o commit resultante de cada etapa;
- executar operações Git somente quando explicitamente autorizadas;
- não converter uma saída de agente em aprovação humana implícita.

### 6.3 Engenheiro Analista

Responsável por executar a Technical Readiness Review integral definida pela EKM
1.6.

Deve:

- confrontar todos os requisitos e dimensões obrigatórias com o baseline;
- verificar clareza, consistência, testabilidade, contratos, dependências,
  condições de borda, compatibilidade e validações;
- produzir a matriz cumulativa da revisão;
- registrar todas as lacunas, mesmo após encontrar o primeiro bloqueio;
- emitir `Implementable` ou `Needs Clarification`;
- encerrar sem alterar artefatos de implementação.

Não pode autorizar a própria recomendação nem implementar a especificação.

### 6.4 Engenheiro Implementador

Responsável por executar exclusivamente a especificação aprovada.

Deve:

- reconfirmar especificação, branch, commit, worktree, revisão e transação antes
  da primeira alteração;
- interromper a execução caso surja uma decisão relevante não autorizada;
- implementar o recorte sem expansão silenciosa;
- executar builds, testes e validações aplicáveis;
- reconciliar código, automação, testes, documentação e diferenças do worktree;
- produzir relatório de implementação e decisões locais;
- declarar desvios, limitações, validações pendentes e operações externas.

O relatório registra evidências e não cria nem altera requisitos.

### 6.5 Engenheiro Tech Lead

Responsável por revisar a implementação contra:

- especificação aprovada;
- Technical Readiness Review;
- autorização e baseline registrados;
- diff completo;
- builds, testes e demais evidências;
- relatório do Engenheiro Implementador.

Deve avaliar aderência requisito a requisito, qualidade técnica, regressões,
suficiência das validações, mudanças não autorizadas e consistência do relatório.
Seu parecer deve indicar uma destas conclusões experimentais:

- `Aprovada`;
- `Correção necessária`;
- `Decisão do arquiteto necessária`;
- `Não verificável com as evidências disponíveis`.

O Tech Lead não corrige diretamente a implementação. Quando necessário, produz
um recorte corretivo ou devolve uma decisão ao arquiteto.

### 6.6 Validador de Integridade da EKM

Responsável por auditar se o processo e seus atores cumpriram a versão declarada
da EKM e este protocolo.

Deve verificar:

- separação e limites dos papéis;
- validade da Technical Readiness Review;
- aprovação humana e reconfirmação do baseline;
- atomicidade e ausência de inferência relevante;
- rastreabilidade entre requisitos, mudanças e evidências;
- proteção do conhecimento normativo;
- reconciliação e estados da transação;
- declaração de desvios, pendências e operações;
- suficiência das evidências para as alegações realizadas.

Seu parecer deve indicar uma destas conclusões experimentais:

- `Conforme`;
- `Conforme com ressalvas`;
- `Não conforme`;
- `Não verificável com as evidências disponíveis`.

Essas conclusões pertencem ao protocolo e não alteram a semântica normativa da
EKM 1.6. O Validador não redefine a especificação, não substitui a revisão
técnica e não escolhe preferências de implementação que a EKM não regulamente.

## 7. Fluxo e gates

```text
Objetivo e referência `main` definidos pelo arquiteto
          ↓
Preparação da mudança e registro do baseline
          ↓
Branch exclusiva derivada de `main`
          ↓
Especificação e transação EKM
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
    ├─ ressalva, não conformidade ou ausência de prova → arquiteto
    └─ Conforme
          ↓
Validação funcional/operacional humana
          ↓
Retrospectiva e decisão experimental
```

Nenhum parecer posterior corrige retroativamente um gate ausente. Se uma etapa
obrigatória não tiver ocorrido no momento devido, o desvio deve permanecer
registrado como evidência do experimento.

### 7.1 Branch exclusiva da mudança

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

### 7.2 Checkpoint de entrada dos atores

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

### 7.3 Saída e formação do próximo checkpoint

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

### 7.4 Promoção prevista

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

## 8. Isolamento e simulação manual

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

## 9. Evidências obrigatórias

Uma execução deve preservar:

1. versão deste protocolo;
2. versão congelada da EKM utilizada;
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

## 10. Métricas

### 10.1 Qualidade e aderência

- requisitos atendidos, parcialmente atendidos e não atendidos;
- ambiguidades, conflitos e lacunas encontrados antes do código;
- mudanças não autorizadas;
- regressões e defeitos encontrados antes e depois da validação humana;
- falhas escapadas para validação funcional ou integração;
- suficiência e reprodutibilidade das validações.

### 10.2 Valor incremental por ator

Cada achado deve ser classificado como:

- `Exclusivo`: ainda não registrado por outro ator;
- `Confirmatório`: confirma, com evidência própria, achado anterior;
- `Duplicado`: repete achado sem evidência ou consequência adicional;
- `Falso positivo`: não se sustenta após análise;
- `Fora de escopo`: não pertence à responsabilidade do ator.

Também devem ser registrados a severidade, o momento da detecção e o retrabalho
evitado ou provocado.

### 10.3 Custo operacional

- tempo por ator e tempo total;
- tokens ou custo estimado, quando disponíveis;
- volume de contexto e artefatos transferidos;
- quantidade de handoffs;
- quantidade de checkpoints formados ou rejeitados;
- violações de branch, commit, worktree ou estado encontradas nos handoffs;
- quantidade de ciclos corretivos;
- intervenções e decisões humanas;
- esforço de preparação e auditoria das evidências.

### 10.4 Efeito sobre o arquiteto

- decisões que exigiram participação humana;
- tempo dedicado a decisões versus atividades operacionais;
- perguntas repetidas;
- confiança e facilidade de localizar a evidência;
- aprendizado reutilizável produzido pelo experimento.

## 11. Interpretação dos resultados

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

## 12. Registro da execução

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
