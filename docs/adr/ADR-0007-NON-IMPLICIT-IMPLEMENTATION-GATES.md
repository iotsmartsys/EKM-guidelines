# ADR-0007 — Gates de implementação não são implícitos

**Estado:** Substituída

**Substituída por:** ADR-0009 — Workflow EKOM em quatro estágios

**Data:** 2026-08-11

**Versão resultante:** EKOM 3.5

## Contexto

Depois de redigida a v0.11 de deep sleep do `IoTSmartLink15.4`, ainda em
`Draft` e sem análise de implementabilidade, o Arquiteto ordenou “implementar o
recorte da v0.11” para observar o comportamento do agente. O executor reconheceu
os dois fatos, mas respondeu que a ordem prevalecia, que registraria o desvio no
relatório e seguiria para o código.

O perfil vigente já dizia que a entrada exigia especificação Pronta e
autorização. Porém, a separação entre autoridade humana, ordem operacional,
análise e promoção não era expressa de forma suficientemente negativa. O agente
interpretou a autoridade do Arquiteto como dispensa implícita dos gates e usou o
relatório como mecanismo de regularização posterior.

O Arquiteto interrompeu a execução e desfez todas as alterações. Nenhuma
implementação da v0.11 foi aceita como resultado.

## Decisão

A implementação normativa exige três gates cumulativos e verificáveis:

1. análise de implementabilidade concluída com classificação `Ready`;
2. versão promovida pelo Arquiteto e registrada como Pronta para implementação;
3. autorização explícita para implementar a mesma versão.

Uma ordem de implementação satisfaz somente o terceiro gate. Ela não promove
implicitamente a especificação, não substitui a análise e não autoriza o
Implementador a registrar o desvio e prosseguir.

Na ausência de qualquer gate, o Implementador recusa antes de investigação
orientada à solução e antes de qualquer mutação. Sua resposta identifica cada
gate presente ou ausente e orienta a próxima etapa correta. Não altera código,
testes, configuração, dependências, build ou relatório de implementação.

Autoridade humana continua final: o Arquiteto pode ordenar análise, incorporar
achados, promover estado e autorizar execução. A autoridade decide essas ações;
não converte uma ação ainda não registrada em fato consumível pelo próximo
perfil.

Diagnóstico ou experimento sobre `Draft` continua possível somente por ordem
distinta que o nomeie explicitamente. Essa atuação não pode alegar implementação
da especificação, mudar estado de implementação ou ser consumida como entrega
normativa.

## Resposta canônica mínima

```text
Implementação não iniciada: condição de entrada ausente.
Análise Ready: presente | ausente
Especificação Pronta: presente | ausente
Autorização da versão: presente | ausente
Próxima etapa: análise | promoção | autorização
```

O texto pode ser adaptado ao projeto, mas a recusa, a ausência de mutação e a
orientação dos gates são obrigatórias.

## Consequências

- ordem e promoção deixam de ser interpretáveis como equivalentes;
- relatório não funciona como autorização retroativa;
- o Implementador verifica estado antes de investigar como codificar;
- solicitações acidentais de implementação sobre `Draft` retornam ao fluxo
  correto sem produzir trabalho descartável;
- experimentos permanecem possíveis, mas recebem identidade e limites próprios;
- projetos adotantes migram deliberadamente para EKOM 3.5.

## Alternativas rejeitadas

- confiar apenas na frase “não inicie” foi rejeitado porque o caso mostrou
  interpretação contrária;
- aceitar que toda ordem do Arquiteto promova estado foi rejeitado porque apaga
  a análise obrigatória e torna a especificação incapaz de governar o fluxo;
- permitir implementação com relatório de desvio foi rejeitado porque transforma
  gate em aviso sem efeito;
- proibir diagnóstico em `Draft` foi rejeitado porque investigação explícita
  ainda pode produzir evidência útil sem representar implementação normativa.

## Critério de reavaliação

Reavaliar se agentes continuarem iniciando implementação diante de gate ausente
ou, no extremo oposto, recusarem diagnósticos e experimentos explicitamente
autorizados por confundi-los com implementação normativa.
