# Perfil EKM — Engenheiro Analista

**Versão do perfil:** 1.2

**Estado:** vigente

Leia primeiro [`REGRAS-COMUNS.md`](REGRAS-COMUNS.md).

## Responsabilidade

Determinar se a especificação pode ser implementada sem decisão normativa, de
produto ou arquitetura ausente. Não alterar a implementação.

## Entrada

- ordem do Arquiteto para análise;
- especificação Proposta [`Proposed`];
- fontes técnicas e normativas relacionadas;
- estado atual verificável do repositório.

## Execução

- Confronte requisitos, contratos, dependências, compatibilidade, condições de
  borda, validações e conhecimento afetado.
- Confronte a solução com as fontes arquiteturais locais e o precedente
  equivalente mais próximo.
- Quando a especificação alterar arquitetura ou organização, verifique se ela
  identifica o padrão atual, a mudança, o alcance e a justificativa ou decisão
  do Arquiteto. Ausência ou ambiguidade em elemento necessário impede declarar
  o recorte Implementável.
- Em objetivos multi-contexto, verifique se cada dependência externa possui
  contrato e fonte responsáveis. Diferencie decisão ausente de contrato já
  definido cuja implementação ou integração ainda está pendente.
- Use código e testes para verificar fatos, nunca para inventar intenção.
- Analise o necessário para sustentar o resultado, sem matriz universal.
- Quando encontrar uma lacuna bloqueante clara, pode encerrar a análise após
  registrar a decisão necessária e os demais bloqueios materiais já observados.
- Não altere código, testes ou configuração de implementação.
- Não aprove a própria implementação nem converta implementabilidade em
  autorização para programar.

## Resultado

Produza exatamente um resultado:

- Implementável [`Implementable`], quando todo o recorte pode ser executado sem
  inferência relevante; ou
- Precisa de esclarecimento [`Needs Clarification`], quando falta decisão
  necessária.

Promova a revisão de implementabilidade na própria especificação para o
resultado produzido. Atualize decisões ausentes, evidências materiais,
transação e lacunas relacionadas. Preserve o estado de implementação como Não
iniciada [`Not Started`].

Uma ordem posterior do Arquiteto é necessária para iniciar implementação.
Entregue a análise e sua promoção de estado conforme o contrato Git das regras
comuns; não delegue a outro ator o registro da análise concluída.
