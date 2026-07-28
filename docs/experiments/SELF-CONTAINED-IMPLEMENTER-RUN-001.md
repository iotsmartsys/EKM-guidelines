# Execução experimental — instrução autocontida e agentes sequenciais

**Estado:** concluída

**Data:** 26/07/2026

**Modelo EKM no projeto:** 1.9

**Modelo EKM na consolidação da evidência:** 1.10

**Projeto:** IoTSmartSysCore

**Especificação:** `IOTSSC-GARAGE-CONTROL@0.1`

**Branch:** `fix/estado_do_garage_control_incosistente`

## 1. Hipóteses

1. Um prompt autocontido, com as regras EKM e técnicas pertinentes ao
   Implementador, pode reduzir a dependência de o agente localizar e interpretar
   a metodologia completa.
2. Agentes e modelos diferentes podem executar partes sequenciais da mesma
   implementação quando especificação, estado e trabalho parcial permanecem
   versionados no repositório.
3. A troca de executor não precisa de memória conversacional compartilhada nem
   de um ator adicional de coordenação.

## 2. Preparação

O `AGENTS.md` do IoTSmartSysCore foi reduzido às invariantes permanentes do
repositório. A instrução específica do Implementador reuniu em uma única
invocação:

- autoridade e etapa;
- estado de entrada;
- objetivo, escopo e fora de escopo;
- requisitos `GAR-001` a `GAR-020`;
- restrições de arquitetura e implementação;
- referências técnicas;
- testes e validações;
- reconciliação EKM;
- commit, push e estado final esperado.

O prompt aplicado está preservado no projeto como
`docs/experiments/GARAGE-CONTROL-STATE-IMPLEMENTER-PROMPT.md`. O modelo
reutilizável correspondente está em
[`templates/prompts/ENGENHEIRO-IMPLEMENTADOR.md`](../../templates/prompts/ENGENHEIRO-IMPLEMENTADOR.md).

## 3. Execução

### 3.1 Primeira parte — Copilot com Kimi K2.7 Code

O Copilot, usando o modelo Kimi K2.7 Code, implementou a primeira parte do
recorte e produziu resultado versionado no commit `234bd82`.

O resultado continha a maior parte da máquina de estados, mocks e testes. O
consumo informado foi de aproximadamente 80 mil tokens. A execução ultrapassou
o limite de créditos da conta antes de concluir validações, reconciliação do
conhecimento e entrega final.

A interrupção foi causada pelo limite de recursos. Portanto, esta execução não
permite concluir que o modelo se recusou ou seria incapaz de completar as
obrigações restantes.

### 3.2 Segunda parte — Codex no ChatGPT

O Codex retomou o trabalho versionado sem compartilhar a conversa anterior do
Copilot. Ele concluiu e ajustou código, testes e fontes EKM no commit `7968f8c`.

Resultados registrados:

- `git diff --check`: aprovado;
- build `esp32_dev`: aprovado;
- suíte `test_garage_control_state`: compilação para ESP32-S3 aprovada com
  configuração temporária equivalente;
- `pio test -e esp32s3_test`: bloqueado antes da compilação por
  `UndefinedEnvPlatformError`, pois o environment preexistente estendia
  `env:base32` sem plataforma;
- testes automatizados não declarados como executados;
- validação física ainda pendente naquele momento.

O agente preservou a limitação e manteve corretamente a especificação em
`In Progress / Not Ready`.

### 3.3 Validação do Arquiteto

O Arquiteto executou testes no dispositivo e declarou que a implementação
atendeu às expectativas da especificação.

O conhecimento foi reconciliado no commit `a9b18f4`:

- estado normativo: `Active`;
- implementação: `Validated`;
- entrega: `Ready for Integration`;
- `EKM-CHG-0007`: `Closed`;
- `EKM-GAP-0009`: `Closed`.

A limitação histórica do environment automatizado permaneceu registrada.
Nenhum merge em `main`, release ou deploy foi realizado.

## 4. Resultado

As três hipóteses receberam evidência favorável neste caso:

- o prompt autocontido forneceu ao Implementador o recorte normativo e técnico
  sem exigir releitura da metodologia completa;
- o trabalho parcial do primeiro executor foi aproveitado pelo segundo;
- especificação, estado declarado e Git foram suficientes para transferir a
  execução entre ambientes sem contexto conversacional compartilhado;
- o Arquiteto preservou a autoridade sobre a validação e a decisão de
  integração;
- a entrega final foi validada funcionalmente contra a especificação.

O fluxo observado foi:

```text
Copilot + Kimi K2.7 Code
→ implementação parcial versionada
→ interrupção por limite de créditos
→ Codex retoma e conclui
→ Arquiteto testa e valida no dispositivo
→ conhecimento e estados reconciliados
```

Essa sequência não constitui execução concorrente. As partes ocorreram
sequencialmente sobre a mesma branch de trabalho.

## 5. Custo e eficiência

O consumo aproximado de 80 mil tokens na primeira parte é evidência material de
custo. O experimento não mediu os tokens do Codex nem possui baseline equivalente
sem EKM, por isso não permite atribuir o consumo ao prompt ou concluir ganho
líquido de produtividade.

O resultado mostra que efetividade técnica e viabilidade econômica precisam ser
avaliadas separadamente.

## 6. Limites

- uma especificação, um repositório e uma cadeia de executores;
- nenhuma comparação controlada entre prompt autocontido e leitura dirigida;
- consumo do primeiro executor aproximado e custo do segundo não medido;
- interrupção externa impediu avaliar a conclusão integral pelo Kimi K2.7 Code;
- o environment automatizado canônico permaneceu defeituoso;
- a integração em `main` não fez parte da execução;
- o caso não demonstra independência universal de modelo ou ambiente.

## 7. Conclusão experimental

A EKM sustentou uma implementação funcionalmente validada mesmo com troca
sequencial de agente e modelo durante a tarefa. A continuidade não dependeu de
memória compartilhada: intenção, estado e resultado parcial permaneceram em
artefatos versionados.

O caso justifica continuar experimentando instruções autocontidas por etapa,
mas ainda não justifica torná-las obrigatórias ou declarar superioridade sobre
a leitura dirigida.
