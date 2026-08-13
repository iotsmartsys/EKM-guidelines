# Diretrizes locais EKOM

Use este arquivo somente quando o projeto precisar de regras locais além da
diretriz externa aplicável.

**Versão do documento:** 4.2

**Versão do modelo EKOM:** 4.2

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
Autoria → Análise de Implementabilidade → Implementação → Revisão
Autoria bloqueada → preparação arquitetural validada → nova análise
```

- lacuna de análise permanece ou retorna ao rascunho;
- restrição ou ambiguidade de implementação retorna ao rascunho/análise;
- defeito técnico encontrado na Revisão retorna à Implementação;
- problema na especificação retorna ao rascunho/análise;
- nova evidência pode motivar reabertura pelo Arquiteto.
- capacidade arquitetural ausente, independente e transversal bloqueia a
  funcionalidade; análise e especificação preparatória são separadas por
  decisão do Arquiteto;
- análise classifica explicitamente defeito funcional, pré-requisito
  arquitetural, evidência requerida, conflito de restrição e impacto não
  delimitado; `prontidão condicionada` não é resultado final.
- implementação exige análise `Ready` da versão corrente e ordem explícita do
  Arquiteto para implementar essa versão. A ordem autoriza a passagem; não há
  promoção nem campo documental intermediário.
- implementação autorizada de artefato construível inclui build canônico e
  proporcional; a especificação não repete essa permissão. Testes, hardware e
  operações externas exigem autorização própria.

Análise de implementabilidade é obrigatória, mas pode ser feita pelo Autor, com
apoio de IA, por agente especializado ou por especialista separado. Revisão é
o quarto estágio; profundidade, independência e challenge são proporcionais ao
risco.

## 4. Evidências

Testes automatizados são evidências, não prova absoluta. Não devem ser
alterados apenas para produzir verde nem usados autorreferencialmente pelo
Implementador. São especialmente úteis para regressões, regras complexas,
bordas, segurança e contratos estáveis.

Criar, ampliar, reestruturar ou corrigir testes só integra o recorte quando a
especificação corrente o exige explicitamente e o vincula a requisito ou
critério de aceite. O Implementador não inventa suíte, matriz ou cobertura.
Criar teste não autoriza executá-lo; toda execução depende da permissão
operacional aplicável.

Aceitação pode considerar código e diffs, builds, execução real, logs, testes,
hardware, APIs, bancos, infraestrutura, relatórios, decisões do Arquiteto e
defeitos posteriores. O Arquiteto decide suficiência e risco residual.

Build falho ou não executado não sustenta implementação concluída. O relatório
registra alvo, ambiente relevante, estado terminal e código de saída.

## 5. Preservação e Git

- Preserve arquitetura e precedente local salvo decisão explícita.
- Especificação preserva contrato; ADR, decisão arquitetural durável;
  relatório, execução; mapa, localização; changelog, estado resumido.
- Análise, implementação, revisão e evidência operacional produzem registros
  separados;
  somente o Arquiteto incorpora seus achados em fontes normativas.
- Registre decisões, lacunas, limitações, desvios e evidências materiais na
  fonte correspondente.
- Reconcilie tabela, árvore e diagrama do mapa quando suas relações materiais
  mudarem; uma visão não aplicável exige justificativa curta.
- Não copie para documentos a linhagem já preservada pelo Git.
- Inicie em branch derivada da `main`. Toda mudança material autorizada inclui
  commit e push da branch corrente, sem confirmação final adicional, e termina
  com árvore limpa. Atuação somente leitura não cria commit.
- Force push, reescrita de histórico, merge, tag, release, deploy, exclusão de
  branch e publicação em outro destino exigem ordem específica.
- Não conclua com execução própria pendente ou estado desconhecido.

## 6. Regras específicas do projeto

`<REFERÊNCIA DE PRODUÇÃO, EVIDÊNCIAS PROPORCIONAIS E RESTRIÇÕES CONFIRMADAS>`
