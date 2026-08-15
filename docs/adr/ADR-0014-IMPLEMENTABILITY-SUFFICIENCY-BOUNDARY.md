# ADR-0014 — Limite de prontidão por suficiência e controle contra omissão

**Estado:** Aceita

**Data:** 2026-08-15

**Versão resultante:** EKOM 4.5

**Decisor:** Arquiteto humano

**ADRs relacionadas:** ADR-0005, ADR-0006 e ADR-0013

## Contexto

No piloto da capability de bateria do `IoTSmartLink15.4`, análises sucessivas
trataram extensões aditivas, escolhas locais e evidências posteriores como
defeitos da especificação. O custo contrariou o objetivo de entregar mudanças
simples a médias em um dia de trabalho.

O primeiro refinamento experimental limitou a autoridade de fontes anteriores e
aplicou suficiência em vez de exaustão. Ele reduziu falsos bloqueios, mas uma
execução `Ready` omitiu um critério que exigia remediação explicitamente fora do
recorte. Conciliação sem cobertura suficiente poderia, portanto, esconder um
defeito real.

## Decisão

A análise de implementabilidade verifica se existe ao menos uma implementação
tecnicamente plausível e conforme dentro da baseline e do recorte. Não exige
solução interna completa, escolha antecipada entre alternativas locais ou
evidência produzível durante Implementação ou Revisão.

Uma fonte anterior só bloqueia quando o Analista demonstra cumulativamente:

1. requisito anterior explícito e aplicável ao mesmo comportamento;
2. requisito novo necessariamente incompatível;
3. inevitabilidade do conflito independentemente da escolha técnica; e
4. ausência de implementação conforme dentro do recorte.

Título, domínio, arquivo, classe, fachada, componente, dependência ou inventário
não ampliam autoridade. Listas são abertas por padrão, salvo declaração
inequívoca de exaustividade. Extensão aditiva presume-se não interferente.

Antes de `Ready`, a análise cobre requisitos, critérios e débitos relacionados,
dispõe cada bloqueador anterior aplicável e executa challenge limitado a
contradição interna, critério insatisfazível, remediação fora do recorte e
achado anterior omitido. Objetividade limita a redação, não a investigação.

O relatório formal possui no máximo 800 palavras, contém somente classificação,
bloqueadores objetivos, reconciliação anterior, controle resumido e até cinco
restrições indispensáveis ao handoff. Não reproduz requisitos, propõe correção,
antecipa implementação ou lista próximos passos. Cada execução cria arquivo
novo e imutável, identificado por UTC até segundos, revisão e ID da execução.
Parecer não persistido permanece consultivo.

## Consequências

- fontes anteriores deixam de congelar extensões por proximidade técnica;
- escolhas normais e validações posteriores avançam para o estágio que as pode
  resolver ou evidenciar;
- critério internamente incompatível ou dependente de remediação excluída
  continua bloqueante;
- relatórios menores preservam decisão e handoff sem transcrever investigação;
- controles de cobertura reduzem omissão, mas não garantem infalibilidade;
- a análise continua obrigatória e o Arquiteto continua decidindo suficiência,
  risco aceitável e passagem do workflow.

## Alternativas rejeitadas

- **Confronto exaustivo de toda fonte adjacente:** rejeitado por ampliar
  autoridade e custo sem demonstrar interferência material.
- **Confiar apenas em relatório curto:** rejeitado porque a primeira execução
  experimental omitiu um critério bloqueante.
- **Eliminar análise de implementabilidade:** rejeitado porque o caso confirmou
  valor na descoberta da contradição de `BATTERY-AC-007`.
- **Exigir prova de ausência de regressão:** rejeitado porque incentiva busca
  aberta por justificativa de bloqueio e prova negativa impraticável.

## Critério de reavaliação

Reavaliar se o limite produzir regressões materiais omitidas, se os controles
voltarem a gerar relatórios exaustivos, se o máximo de 800 palavras impedir
decisões compreensíveis ou se novos casos simples a médios não alcançarem
implementação e revisão em tempo proporcional.
