# ADR-0006 — Contenção de escopo e pré-requisitos arquiteturais

**Estado:** Aceita

**Data:** 2026-08-11

**Versão resultante:** EKOM 3.4

## Contexto

Na especificação de deep sleep do `IoTSmartLink15.4`, uma funcionalidade pequena
de produto encontrou uma arquitetura sem lifecycle terminal, quiescência,
parada do executor ou arbitragem adequada. A análise de implementabilidade
devolveu sucessivas condições e a especificação funcional passou de 219 linhas
na versão experimental reduzida para 610 linhas quando promovida.

Nove relatórios de análise foram necessários. A especificação final tornou-se
coerente, mas absorveu uma evolução arquitetural com identidade própria:
lifecycle, quiescência, encerramento de componentes e coordenação de transições
terminais. O confronto de autoridade introduzido no EKOM 3.3 revelou fontes
afetadas, porém o método ainda oferecia ao Analista apenas prontidão ou retorno
genérico ao rascunho. Não havia classificação que separasse defeito funcional,
pré-requisito arquitetural, evidência ausente e impacto desconhecido.

## Decisão

Implementabilidade passa a significar executabilidade dentro da baseline
arquitetural e do recorte autorizados. Possibilidade técnica obtida mediante
redesenho transversal não torna uma especificação funcional pronta.

A análise usa uma taxonomia obrigatória:

1. Pronta [`Ready`];
2. Não pronta — defeito da especificação [`Not Ready — Specification Defect`];
3. Não pronta — pré-requisito arquitetural [`Not Ready — Architectural
   Prerequisite`];
4. Não pronta — evidência requerida [`Not Ready — Evidence Required`];
5. Não implementável — conflito de restrição [`Not Implementable — Constraint
   Conflict`];
6. Desconhecida — impacto não delimitado [`Unknown — Impact Not Delimited`].

`Prontidão condicionada` deixa de ser classificação final. Toda condição deve
ser identificada como bloqueante ou não bloqueante e roteada para uma classe.

Um pré-requisito arquitetural existe quando a capacidade necessária:

1. não está disponível na baseline;
2. pode ser especificada e validada independentemente da funcionalidade; e
3. altera materialmente arquitetura, componentes compartilhados, autoridades
   ou consumidores fora do recorte.

Nesse caso, a funcionalidade permanece bloqueada. O relatório recomenda análise
arquitetural abrangente e identifica a preparação necessária. O Arquiteto
decide se muda o desenho, aceita alteração local, autoriza ADR ou cria
especificação preparatória. A funcionalidade registra `Depends On`; a
preparação, `Enables`. A implementação funcional só é reconfrontada depois que
a baseline preparatória tiver sido implementada e validada.

## Gatilhos materiais

O teste de fronteira é obrigatório diante de novo lifecycle ou ownership,
ampliação material de API reutilizável, arbitragem transversal, mudança geral de
persistência, recuperação, protocolo ou segurança, impacto com a funcionalidade
desabilitada, consumidores desconhecidos ou retornos sucessivos que revelem
novos bloqueadores arquiteturais.

Um gatilho isolado não impõe automaticamente nova especificação. Materialidade,
independência da capacidade e raio de impacto governam a decisão.

## Proporcionalidade

Mudanças locais continuam na especificação funcional. Uma correção não exige
preparação apenas por tocar API ou mais de um arquivo. A separação ocorre quando
a capacidade tem contrato e validação próprios ou quando o impacto compartilhado
não está delimitado.

A análise arquitetural é primeiro um relatório. Ela pode concluir que a mudança
é local, que outro desenho preserva a baseline, que uma preparação é necessária
ou que o requisito é inviável. Somente o Arquiteto cria a decisão normativa.

## Consequências

- o Analista deixa de usar retorno genérico para naturezas distintas de
  bloqueio;
- o Autor preserva especificações funcionais pequenas sem esconder mudança
  arquitetural;
- o Implementador não usa autorização funcional para redesenhar componentes
  compartilhados;
- mapa e especificação registram dependência sem duplicar o contrato da
  preparação;
- projetos adotantes migram deliberadamente para a taxonomia do EKOM 3.4;
- trabalhos anteriores permanecem válidos sob a versão aplicada na época.

## Alternativas rejeitadas

- continuar usando `prontidão condicionada` foi rejeitado por não informar se a
  condição bloqueia implementação nem para onde ela deve ser roteada;
- tornar toda especificação inicialmente mais técnica foi rejeitado porque
  mistura contrato funcional com investigação e aumenta carga cognitiva;
- criar automaticamente uma preparação em qualquer mudança compartilhada foi
  rejeitado por gerar fragmentação e abstrações especulativas;
- permitir que o Implementador resolva a arquitetura localmente foi rejeitado
  porque consumidores e riscos podem estar fora do recorte autorizado.

## Critério de reavaliação

Simplificar a taxonomia se as classes não mudarem decisões ou apenas aumentarem
formulários. Fortalecer os gatilhos se novas funcionalidades continuarem
absorvendo evoluções arquiteturais ou se impactos fora do recorte forem
descobertos durante implementação.
