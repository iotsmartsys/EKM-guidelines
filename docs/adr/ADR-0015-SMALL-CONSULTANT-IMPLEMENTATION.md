# ADR-0015 — Implementação pequena pelo Consultor sem especificação

**Estado:** Aceita

**Data:** 2026-08-31

**Versão resultante:** EKOM 4.7

**Decisor:** Arquiteto humano

**ADRs relacionadas:** ADR-0006, ADR-0009, ADR-0011 e ADR-0012

## Contexto

O workflow governado por especificação protege mudanças funcionais e
arquiteturais, mas impõe custo desproporcional a implementações pequenas,
locais e de baixo risco que o Arquiteto já delimitou. O Consultor de Arquitetura
já possui capacidade de implementação sob ordem expressa, sem possuir
autoridade própria para ampliar escopo, arquitetura ou risco.

Permitir uma via curta exige preservar três guardas: a exceção deve nascer de
decisão inequívoca do Arquiteto, não pode absorver trabalho materialmente maior
e deve deixar a linhagem Git e o conhecimento do projeto atualizados.

## Decisão

O Consultor de Arquitetura pode implementar sem especificação e sem análise
`Ready` somente quando o Arquiteto:

1. determinar explicitamente que a alteração é pequena;
2. ordenar expressamente sua implementação sem especificação; e
3. delimitar objetivo, recorte e operações autorizadas.

A via curta é aplicável apenas a alteração local, de baixo risco e
compreensível sem criar novo contrato funcional. Ela é vedada quando a mudança
exigir ou revelar arquitetura, contrato público, persistência ou migração de
dados, segurança ou autorização, protocolo, concorrência, operação externa,
múltiplos componentes ou consumidores, impacto material não delimitado ou
qualquer ampliação material de escopo ou risco.

Se a alteração não for pequena, ou deixar de sê-lo durante a investigação, o
Consultor não implementa o recorte ampliado e não parcela artificialmente o
trabalho. Ele registra as evidências materiais e devolve ao Arquiteto a
necessidade do workflow governado por especificação.

Quando estiver na `main`, o Consultor cria uma branch derivada da `main` antes
da primeira mutação. Ao final da implementação, atualiza obrigatoriamente o mapa
de conhecimento com o elemento ou relação afetada e a fonte vigente. O mapa
localiza o conhecimento; não assume o contrato que seria de uma especificação.

Continuam aplicáveis preservação arquitetural, validação proporcional, entrega
Git intrínseca e permissões próprias para testes, hardware, deploy, release e
demais operações externas.

## Consequências

- implementações pequenas expressamente delimitadas podem evitar a criação de
  especificação e análise formais;
- a exceção pertence ao Consultor e não se torna permissão genérica dos demais
  perfis;
- o Arquiteto determina a elegibilidade inicial, mas o Consultor deve parar se
  fatos da execução demonstrarem ampliação material;
- a branch separa a mudança da `main` e o mapa preserva sua localização no
  conhecimento vigente;
- mudanças grandes permanecem no workflow governado por especificação.

## Alternativas rejeitadas

- **Exigir especificação para toda implementação:** rejeitada por impor custo
  desproporcional a mudanças pequenas explicitamente controladas.
- **Aceitar a classificação do agente:** rejeitada porque transfere ao Consultor
  autoridade reservada ao Arquiteto.
- **Permitir que um trabalho grande seja dividido em pequenos commits:**
  rejeitada porque tamanho da entrega Git não reduz escopo, risco ou impacto.
- **Atualizar somente o Git:** rejeitada porque a via sem especificação precisa
  preservar uma entrada navegável no conhecimento do projeto.

## Critério de reavaliação

Reavaliar se a via curta ocultar mudanças funcionais ou arquiteturais, se a
classificação de tamanho se mostrar ambígua em casos recorrentes, se o mapa
passar a duplicar contratos ou se o custo de atualizar o conhecimento superar
o ganho observado nas implementações pequenas.
