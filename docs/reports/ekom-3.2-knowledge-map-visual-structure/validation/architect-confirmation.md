# Relatório de validação — mapa visual EKOM 3.2

**Classe da fonte:** Relatório

**Papel:** Consultor de Arquitetura com confirmação do Arquiteto

**Especificação:** Não se aplica; evolução da governança EKOM

**Revisão confrontada:** EKOM 3.1 vigente antes desta evolução

**Estado:** Concluído

> Este relatório registra evidência observada e não promove estado por
> autoridade própria.

## Ordem e recorte

O Arquiteto determinou incorporar à EKOM normativa e à `main` oficial o mapa de
conhecimento com árvore e diagrama. O recorte abrange método, ADR, mapa
canônico, governança, adoção, roteadores, glossário, caso de estudo e guarda
estrutural. Não abrange migração de projetos adotantes.

## Decisões confirmadas

- índice tabular de autoridade é sempre obrigatório;
- árvore é obrigatória quando hierarquia, composição ou responsabilidade forem
  materiais;
- Mermaid é obrigatório quando alvos separados se conectarem por protocolo,
  API, evento ou dados, ou quando um fluxo cruzar três ou mais fronteiras;
- visão não aplicável permanece declarada com justificativa curta;
- visuais são pequenos e navegacionais e não duplicam contratos detalhados.

## Resultado material

O EKOM 3.2 incorpora a ADR-0004, a seção normativa de visões do mapa, o template
canônico com tabela, árvore e Mermaid, regras de manutenção e adoção, termos no
glossário e guarda estrutural ampliada.

O experimento do IoTSmartLink15.4 permanece a evidência inicial: a árvore
explicitou composição e responsabilidade, enquanto o diagrama conectou client
e coordenador pelo protocolo apesar da separação física.

## Validações

- integridade textual aprovada;
- script da guarda compilável;
- template completo do mapa aprovado;
- ADRs vigentes aprovadas pela guarda estrutural;
- referências de versão vigentes reconciliadas para EKOM 3.2.

## Limitações e independência

Projetos adotantes não foram migrados. A utilidade além do caso observado ainda
precisa ser confrontada; repositórios simples podem declarar árvore ou diagrama
não aplicáveis. O Consultor participou da formulação e não alega revisão
independente.

## Decisão do Arquiteto

O Arquiteto confirmou o registro, aprovou a formulação como EKOM 3.2 e autorizou
commit, publicação, merge e integração na `main` como versão oficial vigente.
Essa decisão não declara eficácia universal nem migra automaticamente projetos
adotantes.
