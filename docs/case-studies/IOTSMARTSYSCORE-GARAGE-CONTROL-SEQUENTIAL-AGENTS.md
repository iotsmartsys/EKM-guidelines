# Estudo de caso — Controle de garagem por agentes sequenciais

## Contexto

A `GarageControlCapability` do IoTSmartSysCore podia permanecer em `opening` ou
`closing` mesmo quando um fim de curso indicava uma posição física estável. A
especificação `IOTSSC-GARAGE-CONTROL@0.1` definiu vinte requisitos para separar
intenção de comando, movimento observado, posição confirmada e debounce dos
sensores.

O caso também foi escolhido para testar uma nova forma de entregar a EKM ao
executor: um prompt autocontido contendo somente as regras do Implementador e as
restrições técnicas aplicáveis.

## Problema metodológico

Experimentos anteriores mostraram que agentes variavam na capacidade de:

- localizar as fontes EKM;
- selecionar as regras pertinentes;
- manter estados e responsabilidades durante uma tarefa;
- distinguir implementação funcional de conformidade processual.

Prompts mais ricos haviam produzido melhor aderência. A hipótese deste caso era
que o agente poderia receber todo o contrato necessário em uma única instrução,
sem carregar a metodologia completa.

## Configuração

O repositório utilizou:

- `AGENTS.md` com invariantes permanentes;
- especificação em estado `Implementable`;
- prompt autocontido do Engenheiro Implementador;
- branch de trabalho derivada da `main`;
- commit e push como entrega material de cada parte;
- validação final reservada ao Arquiteto.

O prompt reuniu requisitos, escopo, arquitetura, referências, testes,
reconciliação documental e entrega Git.

## Execução heterogênea

A implementação ocorreu em duas partes.

O Copilot com Kimi K2.7 Code produziu a maior parte do código e dos testes. A
execução consumiu aproximadamente 80 mil tokens e foi interrompida quando os
créditos da conta se esgotaram. O trabalho parcial permaneceu versionado no
commit `234bd82`.

O Codex no ChatGPT retomou esse estado, completou e ajustou a implementação,
investigou as validações e reconciliou o conhecimento no commit `7968f8c`. Não
houve compartilhamento da conversa anterior entre os ambientes.

O build principal foi aprovado. A suíte de garagem compilou para ESP32-S3 com
configuração temporária, mas o environment automatizado canônico falhou antes da
compilação por uma configuração preexistente incompleta. A limitação foi
registrada sem falsa aprovação.

O Arquiteto executou os testes no dispositivo e confirmou aderência à
especificação. O commit `a9b18f4` promoveu a especificação para `Active`, a
implementação para `Validated` e a entrega para `Ready for Integration`.

## Resultado funcional

A implementação validada passou a contemplar:

- debounce independente dos sensores;
- prioridade da posição física estável;
- movimento comandado e movimento externo;
- reversão durante o percurso;
- sensores ausentes ou parciais;
- combinação contraditória como `unknown`;
- eventos somente em mudança lógica;
- configuração `sensorDebounceTimeMs` com default compatível de 50 ms.

`EKM-CHG-0007` e `EKM-GAP-0009` foram encerradas. A integração em `main`
permaneceu separada e não foi executada.

## Resultado metodológico

O caso demonstra que uma tarefa EKM pode sobreviver à troca de executor:

```text
especificação + estado + commit parcial
                    ↓
           próximo executor
```

Não foi necessário um ator de policiamento, checkpoint documental ou memória
conversacional comum. O primeiro resultado não precisou ser descartado quando a
execução terminou por falta de créditos.

A conformidade final foi composta:

- Kimi K2.7 Code produziu uma parte material e aproveitável;
- Codex completou o recorte e reconciliou as pendências;
- o Arquiteto comprovou o comportamento no dispositivo.

## Aprendizados

1. **O repositório pode ser a memória compartilhada.** Especificação, estados e
   Git permitiram retomada sem conversa comum.
2. **Conclusão da tarefa e capacidade do modelo são diferentes.** A primeira
   execução terminou por limite de créditos, não por evidência de incapacidade.
3. **Aderência não exige um único fornecedor.** O resultado final combinou
   ambientes e modelos diferentes.
4. **Evidência honesta preserva continuidade.** A falha do environment
   automatizado permaneceu registrada e não impediu validação posterior real.
5. **Custo também é resultado.** Aproximadamente 80 mil tokens tornam
   obrigatória a avaliação econômica da forma de instrução.
6. **A autoridade humana permaneceu produtiva.** O Arquiteto validou aquilo que
   o ambiente dos agentes não conseguiu comprovar.

## Limites

O caso não demonstra que qualquer modelo consegue cumprir qualquer tarefa EKM,
nem que o prompt autocontido é mais eficiente que a leitura dirigida. Também não
mede o custo total da cadeia e não resolve a configuração automatizada
preexistente.

Ele demonstra algo mais restrito e verificável: agentes heterogêneos puderam
executar sequencialmente partes da mesma especificação e chegar a uma
implementação validada, preservando estado, conhecimento e autoridade humana.

O registro cronológico está em
[`SELF-CONTAINED-IMPLEMENTER-RUN-001.md`](../experiments/SELF-CONTAINED-IMPLEMENTER-RUN-001.md).
