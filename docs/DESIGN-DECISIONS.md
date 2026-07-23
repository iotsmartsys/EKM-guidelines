# Decisões de desenho da EKM

Este documento registra as razões das principais escolhas do modelo atual. Não substitui as diretrizes operacionais.

## DD-001 — Especificação como unidade de comportamento

**Decisão:** funcionalidades e contratos preserváveis devem ser representados por especificações incrementais.

**Motivo:** comportamentos surgem em momentos diferentes; um documento monolítico seria difícil de manter e incentivaria inferências.

## DD-002 — Não existe um único documento da verdade

**Decisão:** a verdade é distribuída por fontes com responsabilidades explícitas e conectadas por um mapa.

**Motivo:** comportamento, motivação, execução e evidência têm ciclos de vida e autoridades diferentes.

## DD-003 — Dossiê é visão geral, não substituto

**Decisão:** o dossiê facilita navegação e entendimento inicial, mas aponta para especificações especializadas.

**Motivo:** duplicar detalhes cria fontes concorrentes e divergência.

## DD-004 — Estados normativo e de implementação independentes

**Decisão:** cada especificação declara sua autoridade e, separadamente, a situação da implementação.

**Motivo:** uma especificação pode estar vigente sem estar implementada; uma implementação pode existir sem validação suficiente ou estar regredida.

## DD-005 — Transações e lacunas têm identidade própria

**Decisão:** mudanças usam `EKM-CHG-NNNN`; ausências de conhecimento usam `EKM-GAP-NNNN`.

**Motivo:** tarefas concluídas e conhecimento faltante precisam permanecer rastreáveis sem depender de conversas ou listas informais.

## DD-006 — Baseline é o worktree observado

**Decisão:** a comparação inclui alterações rastreadas, não rastreadas e preexistentes, não apenas `HEAD`.

**Motivo:** Git identifica commits, mas uma tarefa pode começar sobre trabalho ainda não consolidado.

## DD-007 — Relatório não é fonte normativa

**Decisão:** relatórios registram evidências e desvios, mas não criam ou alteram requisitos implicitamente.

**Motivo:** um relatório descreve uma execução específica e pode omitir consequências semânticas.

## DD-008 — Specification on touch

**Decisão:** ao modificar uma funcionalidade relevante ainda não especificada, seu domínio deve atingir ao menos `Specified`.

**Motivo:** documentar todo o legado de uma vez é caro; não documentar o que muda perpetua perda de conhecimento.

## DD-009 — `Active` exige autoridade humana ou inequívoca

**Decisão:** comportamento descoberto no código não deve virar requisito vigente apenas por inferência do agente.

**Motivo:** o código pode conter bugs, acidentes históricos, compatibilidade obsoleta ou experimentos.

## DD-010 — Autonomia proporcional à certeza

**Decisão:** agentes avançam autonomamente em descobertas e análises verificáveis. Em uma implementação regida por uma especificação atômica, qualquer requisito obrigatório dependente de julgamento bloqueia o recorte inteiro antes da primeira alteração.

**Motivo:** adoção e investigação podem ser incrementais, mas implementar parcialmente uma especificação incompleta rompe a unidade de delegação e permite decisões normativas silenciosas.

## DD-011 — Estrutura mínima antes de expansão

**Decisão:** começar com `AGENTS.md`, diretrizes, mapa, changelog, dossiê e especificações necessárias.

**Motivo:** padronização facilita adoção, mas arquivos sem autoridade ou uso claro criam burocracia.

## DD-012 — Technical Readiness Review obrigatória

**Decisão:** toda especificação deve receber resultado `Implementable` ou `Needs Clarification` antes de qualquer alteração de implementação.

**Motivo:** um build funcional pode esconder uma decisão inferida que não corresponde à intenção. Concentrar lacunas antes do código aumenta a confiabilidade e permite execução posterior verdadeiramente autônoma.

## DD-013 — Versões normativas em produção são imutáveis

**Decisão:** após `Done`, alterações de comportamento usam nova especificação relacionada, sem reescrever a versão integrada.

**Motivo:** reescrever uma especificação de produção destrói a correspondência histórica entre intenção, implementação e evidência.

## DD-014 — Garantias automatizadas são uma capacidade futura

**Decisão:** prever um `EKM Gate`, sem definir prematuramente sua arquitetura ou alegar garantia ainda inexistente.

**Motivo:** regras verificáveis não devem depender apenas de disciplina, mas a automação precisa nascer de requisitos e experimentos próprios e não substitui julgamento semântico humano.
