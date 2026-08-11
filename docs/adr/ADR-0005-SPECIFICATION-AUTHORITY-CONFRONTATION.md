# ADR-0005 — Confronto de autoridade normativa durante a autoria

**Estado:** Aceita

**Data:** 2026-08-11

**Versão resultante:** EKOM 3.3

## Contexto

Na especificação de deep sleep do `IoTSmartLink15.4`, o Autor consultou
arquitetura, API pública, variantes e precedentes, mas não confrontou
sistematicamente os novos contratos com todas as autoridades afetadas. A
análise inicial tratou como detalhe técnico uma quiescência que incidia sobre o
fora de escopo e o lifetime de uma especificação Active, propôs ampliação de API
sem declarar a emenda correspondente e subestimou o alcance normativo de um
renome de product firmware.

Uma análise de verificação posterior encontrou os conflitos antes da
implementação, mas executou tardiamente uma atividade que deveria preceder a
recomendação de prontidão. O template de especificação já possuía `Relação
normativa`, porém o perfil do Autor não instruía como localizar e confrontar as
autoridades que alimentam esse campo.

## Decisão

Antes de recomendar prontidão, o Autor deve executar confronto de autoridade
normativa orientado pelos elementos afetados:

1. identificar comportamento, API, estado, ciclo de vida, persistência,
   compatibilidade, nome e fronteira tocados pela mudança;
2. localizar suas autoridades pelo mapa, dossiê, especificações e ADRs
   pertinentes;
3. classificar a relação como preservação, `New`, `Amends`, `Supersedes`,
   `Corrects` ou `Retires`;
4. declarar na especificação a relação vigente, a fonte governante e decisões
   ou exceções confirmadas;
5. registrar a matriz detalhada no relatório de análise;
6. devolver ao Arquiteto conflito, omissão ou alcance normativo ambíguo antes
   da prontidão.

O Engenheiro Analista reconfronta essas relações na análise de
implementabilidade. A verificação não se limita à viabilidade do código.

## Proporcionalidade

O confronto não exige leitura integral de toda a documentação nem matriz longa
para mudanças isoladas. A seleção parte do impacto material e segue a cadeia de
autoridade até que cada elemento afetado tenha uma fonte e uma relação
definidas. A especificação continua enxuta; investigação e matriz permanecem no
relatório.

Um primeiro `Draft` pode conter lacunas. A obrigação incide antes da
recomendação de prontidão, quando omissão ou contradição passaria a ser
consumida pelo Implementador como contrato suficiente.

## Alternativas consideradas

- confiar apenas na análise posterior foi rejeitado porque permite autoria
  recomendar prontidão sobre contratos concorrentes;
- exigir leitura de todo o acervo foi rejeitado por custo desproporcional e por
  reduzir foco;
- incorporar a matriz completa à especificação foi rejeitado porque mistura
  investigação histórica com contrato vigente e recria documentos extensos;
- tratar somente dependências de código foi rejeitado porque API, lifecycle,
  nomes e fora de escopo podem cruzar autoridades sem dependência nova.

## Consequências

- o perfil do Autor passa a orientar explicitamente a confecção da
  especificação em relação às fontes anteriores;
- a recomendação de prontidão passa a depender de relações normativas
  localizadas e reconciliadas;
- o relatório de análise recebe a matriz detalhada sem inflar a especificação;
- o Analista verifica tanto viabilidade técnica quanto consistência entre
  autoridades;
- projetos adotantes precisam atualizar o perfil referenciado e os templates
  ao migrar para EKOM 3.3;
- especificações e registros históricos de versões anteriores permanecem
  válidos sob o modelo em que foram produzidos.

## Critério de reavaliação

Simplificar a regra se ela induzir inventários extensos sem revelar conflitos.
Fortalecê-la se novas atuações continuarem recomendando prontidão com fontes
Active omitidas, relações indefinidas ou emendas silenciosas.
