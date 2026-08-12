# Diretrizes locais EKOM

Use este arquivo somente quando o projeto precisar de regras locais além da
diretriz externa aplicável.

**Versão do documento:** 3.5

**Versão do modelo EKOM:** 3.5

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
Rascunho bloqueado → preparação arquitetural validada → nova análise
```

- lacuna de análise permanece ou retorna ao rascunho;
- restrição ou ambiguidade de implementação retorna ao rascunho/análise;
- defeito de validação retorna à implementação;
- problema na especificação retorna ao rascunho/análise;
- nova evidência pode motivar reabertura pelo Arquiteto.
- capacidade arquitetural ausente, independente e transversal bloqueia a
  funcionalidade; análise e especificação preparatória são separadas por
  decisão do Arquiteto;
- análise classifica explicitamente defeito funcional, pré-requisito
  arquitetural, evidência requerida, conflito de restrição e impacto não
  delimitado; `prontidão condicionada` não é resultado final.
- implementação exige cumulativamente análise `Ready`, promoção registrada para
  Pronta e autorização da mesma versão. Ordem de implementação não satisfaz
  gate ausente; o Implementador recusa sem mutação e orienta a próxima etapa.

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
- Especificação preserva contrato; ADR, decisão arquitetural durável;
  relatório, execução; mapa, localização; changelog, estado resumido.
- Análise, implementação, challenge e validação produzem relatórios separados;
  somente o Arquiteto incorpora seus achados em fontes normativas.
- Registre decisões, lacunas, limitações, desvios e evidências materiais na
  fonte correspondente.
- Reconcilie tabela, árvore e diagrama do mapa quando suas relações materiais
  mudarem; uma visão não aplicável exige justificativa curta.
- Não copie para documentos a linhagem já preservada pelo Git.
- Inicie em branch derivada da `main`; commit e push são exigidos quando
  autorizados; merge, tag, release e deploy exigem ordem específica.
- Não conclua com execução própria pendente ou estado desconhecido.

## 6. Regras específicas do projeto

`<REFERÊNCIA DE PRODUÇÃO, EVIDÊNCIAS PROPORCIONAIS E RESTRIÇÕES CONFIRMADAS>`
