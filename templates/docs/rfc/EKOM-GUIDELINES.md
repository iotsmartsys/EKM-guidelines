# Diretrizes locais EKOM

Use este arquivo somente quando o projeto precisar de regras locais além da
diretriz externa aplicável.

**Versão do documento:** 3.0

**Versão do modelo EKOM:** 3.0

**Estado:** vigente

## 1. Definição e objetivo

O EKOM é um modelo de orquestração de engenharia no qual a especificação
governa a execução dos agentes de IA, enquanto o Arquiteto mantém autoridade
sobre decisões, riscos, validação e conclusão.

O objetivo é entregar uma solução especificada, implementada e documentada sem
que o Arquiteto precise desenvolver diretamente.

> **Specifications orchestrate. Code implements.**

## 2. Autoridade

Somente o Arquiteto decide arquitetura, risco aceitável, relevância das
críticas, suficiência das evidências, aprovação, conclusão ou reabertura e
integração. Agentes registram fatos e recomendações, não criam aprovação.

## 3. Workflow

```text
Rascunho e análise → Pronta → Implementação → Validação → Concluída
```

- lacuna de análise permanece ou retorna ao rascunho;
- restrição ou ambiguidade de implementação retorna ao rascunho/análise;
- defeito de validação retorna à implementação;
- problema na especificação retorna ao rascunho/análise;
- nova evidência pode motivar reabertura pelo Arquiteto.

Análise de implementabilidade é obrigatória, mas pode ser feita pelo Autor, com
apoio de IA, por agente especializado ou por especialista separado. Revisão é
challenge consultivo e proporcional ao risco, não gate universal.

## 4. Evidências

Testes automatizados são evidências, não prova absoluta. Não devem ser
alterados apenas para produzir verde nem usados autorreferencialmente pelo
Implementador. São especialmente úteis para regressões, regras complexas,
bordas, segurança e contratos estáveis.

Aceitação pode considerar código e diffs, builds, execução real, logs, testes,
hardware, APIs, bancos, infraestrutura, relatórios, decisões do Arquiteto e
defeitos posteriores. O Arquiteto decide suficiência e risco residual.

## 5. Preservação e Git

- Preserve arquitetura e precedente local salvo decisão explícita.
- Registre decisões, lacunas, limitações, desvios e evidências materiais.
- Não copie para documentos a linhagem já preservada pelo Git.
- Inicie em branch derivada da `main`; commit e push são exigidos quando
  autorizados; merge, tag, release e deploy exigem ordem específica.
- Não conclua com execução própria pendente ou estado desconhecido.

## 6. Regras específicas do projeto

`<REFERÊNCIA DE PRODUÇÃO, EVIDÊNCIAS PROPORCIONAIS E RESTRIÇÕES CONFIRMADAS>`
