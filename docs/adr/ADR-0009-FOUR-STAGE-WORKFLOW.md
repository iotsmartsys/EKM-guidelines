# ADR-0009 — Workflow EKOM em quatro estágios

**Estado:** Aceita

**Data:** 2026-08-12

**Versão resultante:** EKOM 4.0

**Decisor:** Arquiteto humano

**Substitui:** ADR-0007 — Gates de implementação não são implícitos

## Contexto

O EKOM 3.5 tornou análise `Ready`, promoção documental para Pronta e
autorização da mesma versão três gates cumulativos. O controle impediu que uma
ordem ambígua executasse uma especificação ainda em `Draft`, mas passou a
exigir que o Arquiteto repetisse a mesma intenção em promoção, edição da fonte
normativa e nova ordem de implementação.

Em uso real, o agente recusou corretamente uma implementação já analisada e
considerada Pronta porque o campo documental de autorização permanecia
ausente. O comportamento provou a eficácia do bloqueio, mas também seu custo:
a distinção entre promoção e autorização não acrescentou uma nova decisão
humana, apenas uma passagem operacional. O fluxo chegou a ser percebido como
dez passos, apesar de o trabalho de engenharia possuir quatro funções
principais.

## Alternativas consideradas

- manter os três gates e melhorar prompts;
- tornar promoção e autorização automáticas, preservando cinco estados;
- reduzir o workflow a quatro estágios e tratar a ordem explícita como a
  autorização da transição correspondente.

## Decisão

O workflow oficial possui quatro estágios:

1. **Autoria da Especificação**;
2. **Análise de Implementabilidade**;
3. **Implementação**;
4. **Revisão**.

A passagem entre estágios ocorre por ordem explícita do Arquiteto. Não existe
uma etapa autônoma de promoção nem um campo documental de autorização que
precise ser preenchido antes de repetir a mesma ordem.

Para iniciar Implementação são suficientes:

1. análise `Ready` aplicável à versão normativa corrente; e
2. ordem explícita do Arquiteto para implementar essa versão.

A ordem é o ato de aprovação e autorização da transição. O Implementador
registra mecanicamente `In Progress` como primeiro efeito documental da
atuação, sem tratá-lo como precondição. Ordem genérica para “trabalhar”,
“avaliar” ou “continuar” não equivale a ordem de implementação.

Alteração normativa posterior ao `Ready` invalida a análise. Correções de
implementação dentro da mesma versão e do mesmo recorte permanecem cobertas
pela ordem original; não exigem nova autorização a cada retorno da Revisão.
Mudança de intenção, versão, recorte, arquitetura ou risco retorna ao
Arquiteto.

Análise não `Ready` retorna à Autoria. Pré-requisito arquitetural continua em
especificação preparatória. Build canônico continua intrínseco à Implementação.
Testes, hardware, deploy e operações externas são permissões operacionais,
quando aplicáveis, e não novos estágios do workflow.

A Revisão é o quarto estágio do fluxo. Ela confronta implementação, contrato e
evidências e pode devolver defeito de implementação ao estágio 3 ou defeito da
especificação ao estágio 1. Challenge adicional e independência continuam
proporcionais ao risco. Somente o Arquiteto determina `Done`, reabertura e
integração.

## Estados operacionais

Os estados resumem fatos e não criam passagens adicionais:

- `Draft`: em Autoria ou aguardando Análise;
- `Ready`: análise de implementabilidade sem bloqueador para a versão;
- `In Progress`: Implementação iniciada por ordem explícita;
- `Implemented`: implementação e builds obrigatórios encerrados;
- `Reviewed`: Revisão encerrada, com resultado e limitações registrados;
- `Done` ou `Reopened`: decisão exclusiva do Arquiteto.

Projetos podem manter estados técnicos adicionais, desde que não recriem
promoção ou autorização documental como gate intermediário.

## Consequências

- o Arquiteto decide uma vez em cada passagem, pela própria ordem;
- `Ready` substitui a promoção separada para Pronta;
- o Implementador ainda recusa especificação sem análise `Ready`, análise de
  outra versão ou ordem ambígua;
- a especificação deixa de carregar campos “Decisão do Arquiteto: Pronta” e
  “Autorização de implementação”; relatórios e Git preservam as transições;
- loops Autor–Analista e Implementador–Revisor podem continuar dentro de uma
  ordem previamente delimitada, parando apenas diante de decisão humana nova;
- a Revisão deixa de ser passagem opcional, mas sua profundidade, independência
  e evidências permanecem proporcionais ao risco;
- a mudança é incompatível com o modelo de estados 3.x e exige adoção
  deliberada como EKOM 4.0.

## Critério de reavaliação

Reavaliar se ordens explícitas voltarem a produzir implementação de versão não
analisada, se agentes não conseguirem correlacionar `Ready` à versão corrente,
ou se a redução não diminuir passagens humanas e tempo entre intenção e
entrega.
