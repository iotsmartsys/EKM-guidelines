# Relatório de validação — roteamento documental EKOM 3.1

**Classe da fonte:** Relatório

**Papel:** Consultor de Arquitetura com confirmação do Arquiteto

**Especificação:** Não se aplica; evolução da governança EKOM

**Revisão confrontada:** EKOM 3.0 vigente antes desta evolução

**Estado:** Concluído

> Este relatório registra evidência observada e não promove estado por
> autoridade própria.

## Ordem e recorte

O Arquiteto autorizou operacionalizar ADRs e relatórios separados antes de
migrar a especificação de variantes. O recorte abrange método, governança,
decisão arquitetural, roteamento, templates, adoção e guarda estrutural. Não
abrange migração de documentos em projetos adotantes.

## Decisões confirmadas

- especificação preserva contrato vigente;
- ADR registra decisão arquitetural transversal ou durável;
- relatório registra análise, implementação, challenge ou validação;
- mapa localiza autoridade, relações e lacunas;
- changelog resume a transação e referencia fontes materiais;
- Git preserva autoria, diferenças e linhagem;
- somente o Arquiteto incorpora achados em fontes normativas, aceita ADRs e
  promove estados;
- migração histórica ocorre somente depois da criação dos destinos e mediante
  autorização própria.

## Resultado material

O EKOM 3.1 operacionaliza a separação por meio da ADR-0003, regras comuns,
roteador de projetos, template de especificação sem relatórios embutidos,
templates próprios de ADR e dos quatro tipos de relatório, adoção legada e
guarda estrutural proporcional.

O caso de estudo das variantes de firmware registra a evidência que motivou a
mudança e distingue hipóteses sustentadas, não comprovadas e refutadas.

## Validações

- integridade textual aprovada;
- guarda estrutural aprovada sobre as fontes e templates EKOM 3.1;
- a guarda identificou as cinco seções de relatório atualmente embutidas na
  especificação legada de variantes, demonstrando o caso negativo esperado;
- referências de versão vigentes reconciliadas para EKOM 3.1.

## Limitações e independência

A especificação de variantes e o projeto IoTSmartLink15.4 não foram migrados.
A eficácia do novo roteamento ainda deve ser confrontada em uma mudança pequena.
O Consultor participou da formulação e não alega revisão independente.

## Decisão do Arquiteto

O Arquiteto confirmou que o registro representa a decisão, aprovou a formulação
como EKOM 3.1 e autorizou commit, publicação e integração na `main` como versão
vigente. Essa decisão não declara eficácia universal nem migra automaticamente
projetos adotantes.
