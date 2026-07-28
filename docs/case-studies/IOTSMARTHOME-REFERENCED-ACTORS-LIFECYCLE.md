# Caso de estudo — ciclo completo com atores EKM referenciados

**Repositório:** `iotsmarthome`

**Especificação:** `AIOTSMARTHOME-MODULE-SETTINGS-RESET-001@0.1`

**Período:** julho de 2026

**Resultado:** integrado à `main`

## 1. Objetivo

Verificar se uma ordem curta, combinada com um `AGENTS.md` que seleciona regras
comuns e exatamente um perfil EKM, consegue dirigir atores e modelos diferentes
durante todo o ciclo de uma especificação.

O experimento também avaliou se a especificação, seus estados e o Git podem
funcionar como memória compartilhada sem exigir que cada agente carregue a
metodologia completa.

## 2. Modalidade

Cada atuação recebeu uma ordem no formato:

```text
Você é um <papel>, trabalhando na especificação <caminho>.
```

O `AGENTS.md` do projeto encaminhava essa ordem para:

1. regras comuns dos perfis;
2. exatamente um perfil correspondente ao papel;
3. a especificação indicada;
4. somente as fontes técnicas pertinentes.

As atuações foram sequenciais e usaram a mesma branch. Cada resultado material
foi entregue por commit e push.

## 3. Percurso

| Etapa | Resultado material |
|---|---|
| Autoria | especificação Proposta, Não iniciada, Não pronta e Pendente de revisão |
| Primeira ordem ao Implementador | recusa correta porque a especificação ainda não estava Implementável |
| Primeira análise | `Needs Clarification`; faltavam decisões sobre estado local e feedback visual |
| Decisão do Arquiteto | requisitos `MODULE-SETTINGS-RESET-013` a `016` resolveram as lacunas |
| Nova análise | `Implementable` |
| Implementação | botão, confirmação, delegação em camadas e `PUT` sem corpo; build aprovado |
| Revisão humana | Tech Lead revisou e aprovou o código |
| Validação humana | Arquiteto validou implementação e funcionalidade no dispositivo final |
| Promoção | `Active / Validated / Ready for Integration` |
| Publicação e integração | entrega `Done`, PR #39 integrado à `main` |

O merge foi registrado no repositório da aplicação pelo commit `96b9915`.

## 4. Atores e ambientes observados

- Claude Sonnet 5 executou as passagens de análise e a implementação.
- Google Antigravity com Gemini 3.6 Flash, configuração High, executou uma
  tentativa de promoção documental.
- Codex apoiou a avaliação do experimento, a correção dos perfis e a passagem
  final do Engenheiro Revisor.
- O Tech Lead humano revisou o código.
- O Arquiteto humano forneceu decisões, validou a funcionalidade, aprovou a
  implementação e confirmou publicação e integração.

O resultado não demonstra equivalência universal entre modelos. Demonstra que
atores heterogêneos conseguiram continuar o mesmo recorte por meio das fontes
versionadas.

## 5. Resultado funcional

A implementação entregue:

- adicionou `reset custom settings` em `ModuleSettingsEditView`;
- exigiu confirmação destrutiva;
- impediu chamada com `deviceId` vazio;
- delegou `ModuleSettingsEditView → ModuleViewModel → UpdateModuleService`;
- executou `PUT /{device_id}/settings/reset` sem corpo;
- tratou `204` como sucesso e preservou falhas;
- reutilizou o alerta existente;
- fechou a tela somente após o alerta de sucesso.

O build Debug sem assinatura foi aprovado. A funcionalidade foi validada no
dispositivo final e integrada à `main`.

## 6. Desvios observados

### 6.1 Árvore limpa reinterpretada

Uma atuação declarou a árvore limpa apenas em relação ao escopo, embora
existissem arquivos `.claude/` não versionados. A EKM não define limpeza
parcial: a árvore inteira deve estar limpa.

O caso mostrou que um agente pode reinterpretar uma regra explícita mesmo
quando localizou e leu o perfil correto.

### 6.2 Papel incompatível com a etapa

Uma promoção posterior à validação foi solicitada usando o papel Autor da
Especificação. O Gemini registrou `Approved / Implemented / Ready for
Integration`, embora a evidência humana sustentasse `Active / Validated / Ready
for Integration`.

O commit foi revertido sem reescrita de histórico. Os perfis foram ajustados
para que cada ator registre e promova o resultado da própria etapa. O
Engenheiro Revisor passou a registrar validação do Tech Lead e aprovação do
Arquiteto quando fornecidas explicitamente.

### 6.3 Acúmulo documental

A especificação e o changelog acumularam análises históricas extensas. A
evidência confirmou que o Git deve preservar a evolução técnica, enquanto as
fontes EKM devem privilegiar contrato vigente, decisões, lacunas, evidências
materiais e resultado.

## 7. Aprendizados

- O prompt mínimo foi suficiente quando o `AGENTS.md` selecionou regras fixas.
- O estado da especificação bloqueou corretamente implementação prematura.
- Agentes diferentes retomaram o trabalho sem compartilhar a conversa anterior.
- A autoridade do Arquiteto permaneceu necessária para intenção, produto,
  validação e integração.
- Commit e push por ator preservaram passagem auditável sem copiar a linhagem
  do Git para documentos.
- Cada ator deve promover os estados sustentados por sua própria atuação.
- Não é necessário criar um ator dedicado apenas à reconciliação.
- Perfis curtos e específicos reduziram a necessidade de carregar a metodologia
  completa, mas não garantem obediência universal.

## 8. Decisão

O Arquiteto aprovou o resultado do experimento e determinou que o modelo de
atores se torne o fluxo oficial da EKM.

A EKM 1.11 incorpora:

- ordem que identifica papel e especificação;
- regras comuns e um perfil específico por atuação;
- promoção de estados pelo ator responsável pela etapa;
- atualização do conhecimento afetado;
- commit, push e árvore limpa ao fim de cada tarefa;
- decisão final do Arquiteto sobre validação e integração.

Os controles de concorrência continuam fora do modelo.
