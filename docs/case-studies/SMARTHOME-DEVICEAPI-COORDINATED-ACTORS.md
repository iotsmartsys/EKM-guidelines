# Estudo de caso — Reset de device settings por atores coordenados

## Contexto

O SmartHome-DeviceApi precisava expor um endpoint idempotente para remover os
settings específicos de um device, preservando settings globais, herdados e
padrão. A mudança foi usada como primeira execução do protocolo experimental de
coordenação por atores da EKM.

O fluxo foi dividido entre Autor da Especificação, Engenheiro Analista,
Engenheiro Implementador e Engenheiro Tech Lead, com gates e decisões explícitas
da Coordenação e do arquiteto.

A execução ocorreu sob as versões 0.2 a 0.4 do protocolo e foi posteriormente
reavaliada conforme o alinhamento de governança da versão 0.5.

## Hipótese

A separação de responsabilidades e os handoffs por commit deveriam aumentar a
aderência à especificação, tornar desvios localizáveis e impedir que um mesmo
ator produzisse e consumisse sua própria autorização.

## Execução observada

A execução avançou até:

1. autoria da especificação;
2. primeira análise com resultado `Needs Clarification`;
3. correção e normalização para o protocolo 0.4;
4. nova análise com resultado `Implementable`;
5. aprovação humana para implementação;
6. implementação e relatório;
7. revisão do Tech Lead com parecer `Não verificável`;
8. validação manual e aceitação do código e da funcionalidade pelo arquiteto.

O Validador de Integridade da EKM, a integração e o encerramento ainda não foram
executados.

O contrato executado ainda não exigia parecer humano formal da especificação
antes do Analista. A intenção foi fornecida e refinada pelo arquiteto, mas não
há registro equivalente ao novo gate `Accepted` associado a um checkpoint.

## Evidências favoráveis

- A branch exclusiva e os checkpoints preservaram a origem e cada handoff.
- A análise encontrou problemas de baseline e de processo antes da
  implementação.
- A repetição do Analista confirmou suporte aos dez requisitos funcionais.
- O Implementador permaneceu no escopo aprovado e alterou somente os componentes
  necessários.
- O Tech Lead confirmou estaticamente os dez requisitos e não encontrou mudança
  não autorizada.
- O Tech Lead não declarou validação operacional inexistente quando restore e
  banco isolado estavam indisponíveis.
- A validação humana confirmou a implementação e a funcionalidade.
- A autorização para implementação e a validação funcional exerceram a
  governança humana esperada.

## Fricções e evidências negativas

- A autoria inicial e as revisões deixaram inconsistências de estado e
  transação que exigiram intervenção da Coordenação.
- O protocolo evoluiu durante a transação, exigindo normalização explícita.
- O resultado binário da análise misturou inicialmente clareza normativa com
  limitação operacional.
- Tentativas de build falharam no restore e não geraram evidência reproduzível
  de compilação pós-implementação.
- Não havia banco isolado autorizado para testes destrutivos pelos agentes.
- Um artefato de telemetria do tooling C# apareceu dentro do worktree e foi
  inicialmente percebido como resíduo de build.
- A validação manual aceita pelo arquiteto ainda precisa ser reconciliada no
  registro transacional.
- O parecer humano da especificação não existia como gate formal no contrato
  aplicado e não pode ser criado retroativamente.
- O custo de coordenação e correção documental foi relevante para uma mudança
  funcional pequena.

## Resultado parcial

O resultado técnico é positivo: a funcionalidade foi especificada,
implementada, revisada estaticamente, validada manualmente e aceita pelo
arquiteto.

O resultado metodológico é promissor, mas ainda inconclusivo. A separação de
papéis melhorou rastreabilidade, controle de escopo e honestidade das evidências.
Ao mesmo tempo, o caso revelou sobrecarga de coordenação operacional,
inconsistências documentais e dependência de um ambiente de execução adequado.

A confiança foi favorecida por checkpoints, revisão independente e decisão
humana. O efeito sobre velocidade ainda não pode ser concluído, porque tempo
ativo, custo de contexto e duração das intervenções não foram medidos de forma
sistemática.

A quantidade de decisões humanas não é tratada como falha. Pareceres,
aprovações, validação funcional e decisão de integração são controles esperados;
o alvo de redução é retrabalho e operação repetitiva.

## Conclusão provisória

O experimento justifica continuar avaliando o modelo, mas ainda não justifica
torná-lo obrigatório na EKM. A próxima avaliação deve observar se o Validador de
Integridade acrescenta informação relevante e se o fluxo pode ser simplificado
sem perder separação de responsabilidades e rastreabilidade.

O caso também reforça que validação humana não é uma falha do método. Ela é um
gate deliberado quando a decisão final ou o ambiente operacional permanecem sob
responsabilidade do arquiteto. O ponto a melhorar é transformar essa validação
em evidência versionada e reproduzível sempre que possível.

## Limitações

- uma única funcionalidade e um único repositório;
- protocolo alterado durante a execução;
- ausência, no contrato executado, do parecer humano formal anterior à análise;
- agentes sem identificação versionada de modelo, custo e tempo ativo;
- build e validação funcional não reproduzidos no ambiente dos agentes;
- auditoria de integridade e integração ainda pendentes.

O registro cronológico e os checkpoints estão em
[`COORDINATED-ACTOR-MODEL-RUN-001.md`](../experiments/COORDINATED-ACTOR-MODEL-RUN-001.md).
