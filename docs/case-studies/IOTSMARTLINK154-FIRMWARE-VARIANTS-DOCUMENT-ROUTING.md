# Caso de estudo — variantes de firmware e roteamento documental

**Repositório:** IoTSmartLink15.4

**Período:** agosto de 2026

**Resultado funcional:** integrado e validado em hardware

## Objetivo observado

O experimento avaliou se mapa e árvore de conhecimento orientariam a evolução
de um único client para múltiplos product firmwares e boards selecionados pelo
`menuconfig`, preservando o coordenador e o protocolo compartilhado.

## Resultado sustentado

- mapa e especificação distinguiram client, coordenador, protocolo, product
  firmware, board e componentes reutilizáveis;
- uma segunda variante foi incorporada sem condicionais de produto dentro dos
  componentes, duplicação de runtime ou alteração do protocolo;
- a modelagem revelou que board representa um modelo físico com recursos e
  pinagem, não apenas o módulo ESP32;
- análises encontraram incompatibilidade de recursos, debounce irrealizável,
  concorrência em reports e comportamento terminal inadequado no boot;
- o resultado foi validado no hardware pelo Arquiteto.

## Custo e desvio documental

A especificação acumulou contrato, análises, relatórios de implementação,
revisão, decisões e encerramento até alcançar 1.573 linhas. No percurso até a
integração houve vinte commits exclusivamente documentais, cinco commits com
alteração funcional e dois merges.

O acúmulo não foi somente falha de execução. O template EKOM 3.0 reservava na
própria especificação seções para análise de implementabilidade, evidências da
implementação e decisão final, enquanto não fornecia diretórios ou templates de
relatório aos projetos adotantes.

## Avaliação

- **sustentada:** utilidade do mapa, das fronteiras e da especificação para
  reduzir decisões arquiteturais equivocadas;
- **sustentada:** aumento de qualidade e confiança proporcional por análise e
  hardware;
- **não comprovada:** aceleração do desenvolvimento, pois não houve baseline de
  tempo e o workflow documental foi fragmentado;
- **refutada no formato observado:** obtenção de contexto mínimo pela
  especificação final.

## Consequência para o método

O caso sustenta a [`ADR-0003`](../adr/ADR-0003-DOCUMENT-ROUTING-AND-EVIDENCE-SEPARATION.md):
contrato permanece na especificação; decisão arquitetural durável vai para ADR;
execução vai para relatório; mapa localiza; changelog resume a transação; Git
preserva a linhagem. A eficácia da correção ainda precisa ser confrontada em
uma nova mudança pequena e não é presumida por esta incorporação.

O valor específico da árvore e do diagrama sustenta também a
[`ADR-0004`](../adr/ADR-0004-KNOWLEDGE-MAP-VISUAL-STRUCTURE.md), sem tornar
visuais decorativos obrigatórios em repositórios simples.
