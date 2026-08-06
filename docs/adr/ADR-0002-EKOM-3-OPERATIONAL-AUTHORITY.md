# ADR-0002 — Autoridade operacional e workflow proporcional no EKOM 3.0

**Estado:** Aceita

**Data:** 2026-08-04

**Versão resultante:** EKOM 3.0

## Contexto

As versões anteriores trataram especificação, perfis separados e gates de
revisão como meios de aumentar continuidade e confiança. Os experimentos
produziram implementações geralmente funcionais e aceitáveis, muitas delas
corretas na primeira execução no ambiente real, integrando dispositivos, APIs,
bancos e serviços sem o Arquiteto assumir diretamente o desenvolvimento.

As intervenções humanas concentraram-se em esclarecer requisitos, avaliar
riscos, validar comportamento real e decidir conclusão. O conhecimento foi
preservado por especificações, relatórios, decisões, commits, conversas, logs e
evidências.

A maior dificuldade observada não esteve na implementação, mas na tentativa de
transferir validação e crítica arquitetural para outros agentes. Revisores
obrigatórios frequentemente ampliaram discussões sobre testes, riscos teóricos
e evidências sem ganho funcional proporcional. Agentes implementadores e
revisores podem compartilhar capacidades, contexto e vieses; multiplicidade de
agentes não garante independência.

Testes verdes também se mostraram evidência limitada. Em firmware e
integrações, execução em hardware, API, banco ou infraestrutura real pôde ser
evidência funcional mais forte. O estado público da engenharia assistida por IA
tampouco sustenta prometer engenharia autônoma de ponta a ponta sem supervisão
e autoridade humanas.

Essa última afirmação é uma inferência conservadora, não prova de
impossibilidade. Em consulta de 4 de agosto de 2026, a pesquisa de horizonte de
tarefas do [METR](https://metr.org/time-horizons/) ainda mede confiabilidade em
tarefas delimitadas e alerta que medições acima de 16 horas são pouco
confiáveis com a suíte atual. A análise da
[OpenAI sobre SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
mostra contaminação e testes que rejeitam soluções corretas; a auditoria
posterior do
[SWE-Bench Pro](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)
estima cerca de 30% de tarefas quebradas. Esses resultados demonstram progresso
e limites de medição em tarefas de código, não engenharia completa sem
supervisão humana.

## Hipóteses originais

- um Engenheiro Analista separado deveria anteceder toda implementação;
- todo workflow deveria terminar por Revisor separado;
- múltiplos agentes constituiriam revisão verdadeiramente independente;
- critérios e testes verdes poderiam fornecer prova suficiente de correção;
- a autonomia completa seria uma capacidade atual ou próxima do modelo.

## Observações sustentadas pelos experimentos

- a execução pode ser amplamente delegada;
- a especificação coordena participantes, estados e continuidade;
- o Arquiteto continua necessário como autoridade substantiva;
- soluções funcionais podem ser concluídas sem o Arquiteto desenvolver;
- validação no ambiente real tem alto valor, especialmente em firmware e
  integrações;
- IA amplia investigação, localização de impactos e execução;
- decisões e evidências versionadas preservam aprendizado entre agentes.

## Decisões

1. Adotar como definição operacional:

   > A EKOM é um modelo de orquestração de engenharia no qual a especificação
   > governa a execução dos agentes de IA, enquanto o Arquiteto mantém
   > autoridade sobre decisões, riscos, validação e conclusão do workflow.

2. Adotar como objetivo operacional permitir entrega especificada,
   implementada e documentada sem desenvolvimento direto pelo Arquiteto.
3. Reservar ao Arquiteto decisões arquiteturais, risco aceitável, relevância
   das críticas, suficiência das evidências, aprovação, conclusão e reabertura.
4. Manter análise de implementabilidade obrigatória, sem exigir ator separado.
5. Transformar Crítico/Revisor em capacidade consultiva e proporcional ao risco,
   sem autoridade própria de gate.
6. Tratar testes automatizados como evidências proporcionais, não prova
   absoluta nem narrativa universal de aceite.
7. Permitir que evidência do ambiente real tenha precedência funcional quando
   o contexto justificar, sem descartar regressão, segurança ou observabilidade.
8. Adotar ciclo iterativo de cinco estados: Rascunho e análise, Pronta,
   Implementação, Validação e Concluída; somente o Arquiteto conclui ou reabre.
9. Declarar o EKOM como modelo experimental cujo próprio desenho é confrontado
   por evidências materiais.
10. Manter autonomia completa como horizonte evolutivo, não promessa atual.

## Papéis revisados

- **Arquiteto:** autoridade final substantiva, não carimbador formal.
- **Autor:** consulta fontes existentes e pode incorporar a análise de
  implementabilidade, inclusive apoiado por IA.
- **Engenheiro Analista:** capacidade especializada opcional como ator separado.
- **Implementador:** executa, verifica, relata evidências, decisões locais,
  dúvidas, limitações e desvios.
- **Crítico/Revisor:** challenge consultivo, acionado por risco ou pelo
  Arquiteto; pode não encontrar risco adicional relevante.

## Hipóteses revisadas ou refutadas

- **Refutada como regra universal:** necessidade de Revisor separado em todo
  workflow.
- **Refutada:** equivalência entre múltiplos agentes e revisão independente.
- **Refutada:** testes verdes como prova suficiente de correção.
- **Refutada como regra universal:** Engenheiro Analista obrigatoriamente
  separado.
- **Não comprovada e retirada da capacidade atual:** autonomia completa.

## Consequências positivas

- menos handoffs e discussões sem ganho material;
- análise e challenge aplicados onde têm valor justificável;
- autoridade e responsabilidade humanas ficam inequívocas;
- evidências reais podem orientar aceitação sem desprezar testes;
- o modelo descreve com maior fidelidade o funcionamento observado.

## Limitações

- a suficiência das evidências continua dependendo de julgamento humano;
- resultado funcional não prova conformidade metodológica ou ausência de
  defeitos futuros;
- segregação ainda pode ser necessária em riscos específicos;
- evidência real pode ser cara, difícil de reproduzir ou incompleta;
- a revisão deriva dos experimentos registrados e não demonstra validade
  universal.

## Horizonte futuro

Novas formas de validação independente, redução comprovada de vieses e agentes
capazes de exercer julgamento confiável podem ampliar a autonomia. Qualquer
promoção depende de evidência material e nova decisão versionada.

## Versionamento e compatibilidade

A mudança é `major` pela convenção de
[`GOVERNANCE.md`](../GOVERNANCE.md): altera de forma incompatível o modelo de
atores, a autoridade de promoção e o workflow oficial. Projetos EKOM 2.1 não são
migrados automaticamente; seus registros permanecem válidos sob a versão em
que foram executados.
