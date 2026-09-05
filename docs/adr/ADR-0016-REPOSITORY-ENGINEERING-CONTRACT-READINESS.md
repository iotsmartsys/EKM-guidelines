# ADR-0016 — Contrato de engenharia e qualificação para adoção

**Estado:** Aceita

**Data:** 2026-09-05

**Versão resultante:** EKOM 5.0

**Decisor:** Arquiteto humano

**ADRs relacionadas:** ADR-0009, ADR-0014 e ADR-0015

## Contexto

Buscar precedentes não determina qual arquitetura o responsável técnico deseja.
Padrões coexistentes e código legado permitem inferências incompatíveis. O
Arquiteto determinou incorporar regras explícitas como pré-requisito de adoção.
A eficácia desse controle ainda precisa de experimento; não se presume resultado.

## Decisão

Adotar [Repository Engineering Contract e Repository Readiness](../REPOSITORY-READINESS.md)
como norma de qualificação do repositório. A precedência é especificação da
tarefa, contrato aprovado, precedentes oficiais, código existente e preferência
do implementador. Conflitos normativos exigem decisão humana explícita.
A IA propõe; somente Arquiteto/responsável técnico humano aprova como norma.

Repository Readiness usa Not Ready, Conditionally Ready e Ready, sem alterar
as classificações da análise da especificação. Implementação é bloqueada sem
contrato aprovado e qualificação válida no recorte. A via curta do Consultor
não dispensa qualificação. A ADR-0009 continua regendo a passagem entre estágios
dentro de um repositório habilitado; a ADR-0015 conserva sua dispensa limitada.

## Consequências

- arquitetura, organização e estilo passam a ser fornecidos ao executor;
- adoção documental e habilitação para implementação tornam-se distintas;
- surge custo de formular e aprovar regras e avaliar conformidade, proporcional
  ao escopo; áreas justificadamente não aplicáveis não exigem conteúdo artificial;
- perfis, roteadores, templates e roteiro experimental tornam o controle acionável;
- a mudança é major porque repositórios antes utilizáveis sem qualificação
  deixam de ser elegíveis ao migrar para 5.0; história não é reescrita;
- guardas documentais não garantem obediência dos agentes nem autenticam humanos.

## Alternativas rejeitadas

- Inferir norma dos precedentes: mantém a ambiguidade original.
- Aprovação automática pela IA: transfere autoridade técnica ao proponente.
- Exigir conformidade integral de todo legado: impede adoção proporcional;
  escopos independentes podem ser habilitados explicitamente.

## Critério de reavaliação

Medir bloqueios corretos e indevidos, desvios arquiteturais, tempo de preparação
e intervenção humana no experimento; ajustar o controle por evidência.
