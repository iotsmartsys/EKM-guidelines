# Governança da EKM

## 1. Objetivo

Permitir que o método evolua com evidências sem apagar sua história nem
apresentar hipóteses como conclusões, preservando autoridade humana sobre
decisões relevantes.

Governança é um objetivo central da EKM. Ela delimita quem pode decidir, quem
pode executar, quais evidências sustentam cada transição e como exceções são
tratadas. O objetivo não é eliminar participação humana, mas acelerar a
engenharia com confiança, rastreabilidade e responsabilidade.

## 2. Estado atual

A EKM é experimental e utilizável. Não está concluída nem descartada. Cada versão representa o melhor modelo conhecido até aquele momento.

**Modelo vigente neste repositório:** 1.7.

## 3. Fontes deste repositório

| Fonte | Autoridade |
|---|---|
| `docs/EKM-CONCEPT.md` | Conceito e limites atuais |
| `docs/EKM-METHOD.md` | Método de referência vigente |
| `docs/DESIGN-DECISIONS.md` | Razões das decisões do método |
| `docs/LEGACY-ADOPTION.md` | Processo recomendado para legados |
| `templates/` | Ponto de partida operacional |
| `docs/case-studies/` | Evidências e aprendizados, não regras universais |

## 4. Critérios para evolução

Uma mudança na EKM deve indicar:

- problema observado;
- evidência ou experimento que o revelou;
- regra ou modelo afetado;
- impacto nos templates;
- compatibilidade com adoções anteriores;
- hipótese que ainda permanece aberta.

Preferências editoriais isoladas não justificam expansão do método.

## 5. Versionamento

Usar versionamento semântico para versões publicadas do guideline:

- **major:** mudança incompatível no modelo ou nos estados;
- **minor:** nova capacidade, regra ou template compatível;
- **patch:** esclarecimento ou correção sem mudança de comportamento.

Projetos adotantes não precisam atualizar automaticamente. A migração deve ser deliberada e registrar quais regras passaram a vigorar.

## 6. Experimentos

Estudos de caso devem separar:

- contexto;
- hipótese;
- execução;
- evidência;
- resultado;
- mudança introduzida no método;
- limitações da conclusão.

Resultados negativos são conhecimento válido e não devem ser omitidos.

## 7. Alterações nos modelos

Ao modificar um template:

1. atualizar a fonte conceitual ou decisão relacionada;
2. verificar consistência entre todos os modelos;
3. manter o template genérico;
4. não incorporar regras específicas de um projeto;
5. registrar impacto para usuários existentes.

## 8. Critério de qualidade

O sucesso da EKM não é medido pela quantidade de documentos. Deve ser avaliado por:

- confiança na entrega e qualidade das decisões;
- rastreabilidade de autoridade, responsabilidade e evidência;
- tempo entre intenção, especificação, validação e entrega;
- facilidade de localizar autoridade;
- redução de perguntas repetidas e inferências;
- preservação de contratos durante mudanças;
- qualidade e autonomia segura da execução;
- proporção entre participação humana decisória e coordenação operacional;
- custo de manutenção do próprio conhecimento.

Interações humanas planejadas de decisão, aprovação e validação não são
classificadas automaticamente como custo ou falha. O método deve distinguir
esses gates de retrabalho, ambiguidade e operação repetitiva.

Essas métricas ainda precisam ser experimentadas de forma mais sistemática.
