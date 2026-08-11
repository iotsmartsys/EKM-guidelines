# ADR-0004 — Estrutura visual proporcional do mapa de conhecimento no EKOM 3.2

**Estado:** Aceita

**Data:** 2026-08-11

**Versão resultante:** EKOM 3.2

**Decisores:** Arquiteto humano

## Contexto

O EKOM exige mapa de conhecimento para localizar fontes, autoridade, domínios e
lacunas. Até a versão 3.1, porém, o template canônico contém somente tabelas.
Elas respondem onde está uma fonte e qual sua autoridade, mas não tornam
necessariamente visíveis hierarquia, composição, dependência ou conexão entre
alvos separados.

No experimento de variantes do IoTSmartLink15.4, uma árvore tornou explícitas
as fronteiras entre product firmware, board e componentes compartilhados. Um
diagrama pequeno conectou client ESP32-H2 e coordenador ESP32-C6 pelo protocolo
IEEE 802.15.4/ISSP, apesar de serem alvos físicos diferentes. Essa representação
orientou classificação e implementação sem transformar o mapa em contrato
duplicado.

Obrigar diagramas em qualquer repositório criaria custo sem ganho. Deixar o
formato inteiramente opcional, por outro lado, não garante que relações
materiais sejam visíveis quando o índice tabular for insuficiente.

## Decisão

O mapa EKOM passa a combinar três visões complementares:

1. **Índice de autoridade:** tabela obrigatória de fontes, estados e escopos.
2. **Árvore de conhecimento:** visão hierárquica obrigatória quando contenção,
   composição ou responsabilidade entre alvos, domínios ou componentes for
   material para localizar uma mudança.
3. **Diagrama de relações:** Mermaid pequeno obrigatório quando alvos ou
   domínios física ou operacionalmente separados se conectarem por protocolo,
   API, eventos, dados ou fluxo que não fique inequívoco na árvore.

A árvore é material, em particular, quando existir mais de um runtime target,
aplicativo, serviço ou firmware, ou quando três ou mais domínios/componentes
possuírem relação de contenção ou responsabilidade relevante.

O diagrama é material quando existir conexão entre dois ou mais alvos
implantáveis separadamente ou quando um fluxo cruzar três ou mais fronteiras de
domínio. Outros diagramas permanecem opcionais e devem existir somente quando
reduzirem esforço de compreensão.

Quando árvore ou diagrama não se aplicar, a seção correspondente permanece no
mapa com `Não se aplica` e uma justificativa curta. Isso torna a decisão de
omissão explícita sem exigir artefato decorativo.

Tabela, árvore e diagrama não duplicam contratos detalhados. O mapa usa nomes,
responsabilidades e relações estáveis e aponta para especificações, ADRs,
relatórios ou código que detêm o conteúdo especializado.

## Consequências

- humanos e agentes podem localizar tanto autoridade quanto estrutura e
  relações antes de varrer o repositório;
- sistemas com múltiplos alvos tornam visível a conexão ponta a ponta;
- classificação de regras entre produto, board, componente e plataforma deixa
  de depender apenas de texto linear;
- mudanças estruturais precisam reconciliar as visões afetadas do mapa;
- repositórios simples podem declarar as visões não aplicáveis;
- diagramas grandes, inventários de arquivo e duplicação de contrato continuam
  fora do objetivo do mapa.

## Compatibilidade e validação

A evolução é `minor`: preserva autoridade, workflow e roteamento do EKOM 3.1 e
amplia a capacidade normativa do mapa. Projetos adotantes migram
deliberadamente; mapas históricos não são reescritos automaticamente.

A guarda estrutural verifica a presença das três visões e aceita justificativa
explícita de não aplicabilidade. A qualidade semântica, o nível de detalhe e a
necessidade de visuais adicionais permanecem sob julgamento humano.
