# Perfil EKOM — Autor da Especificação

**Versão do perfil:** 2.1

**Estado:** vigente

Leia primeiro [`REGRAS-COMUNS.md`](REGRAS-COMUNS.md).

## Responsabilidade

Transformar a intenção do Arquiteto em solução proposta, implementável e
verificável. A mesma atuação pode produzir a análise de implementabilidade
quando autorizada; segregação não é gate universal.

## Execução

- Consulte repositório, arquitetura, conhecimento e precedentes aplicáveis.
- Use IA para ampliar investigação, localizar impactos, restrições e
  incertezas sem transformar inferência em decisão.
- Registre objetivo, contexto, escopo, fora de escopo, requisitos, contratos,
  falhas e condições de borda.
- Diferencie fatos observados, decisões confirmadas, recomendações e pendências.
- Preserve arquitetura ou explicite padrão afetado, mudança, alcance e decisão
  do Arquiteto.
- Relacione requisitos a critérios que distingam sucesso, falha e ausência de
  evidência sem antecipar estrutura interna desnecessária.
- Identifique validações automatizáveis e evidências humanas, físicas ou de
  integração sem transformar teste em prova absoluta.
- Em objetivo multi-contexto, preserve contrato ponta a ponta e fontes locais
  responsáveis.

## Confronto de autoridade normativa

Antes de fechar a proposta ou recomendar prontidão:

1. identifique os comportamentos, contratos públicos, estados, ciclos de vida,
   nomes e fronteiras que a mudança toca;
2. use o mapa de conhecimento, o dossiê e as referências locais para localizar
   as especificações, ADRs e diretrizes que já governam esses elementos;
3. confronte a mudança com cada autoridade pertinente, inclusive itens de fora
   de escopo, invariantes e decisões de lifetime ou compatibilidade;
4. classifique a relação como preservação ou, conforme a convenção vigente,
   `New`, `Amends`, `Supersedes`, `Corrects` ou `Retires`;
5. declare na especificação a relação normativa e a fonte que governa cada
   extensão ou exceção; quando a decisão for transversal ou durável, acione o
   gatilho de ADR;
6. registre no relatório de análise a matriz detalhada de fontes afetadas,
   relação, conflito e ação requerida, sem inflar a especificação com narrativa
   de investigação;
7. mantenha como decisão pendente do Arquiteto toda relação ambígua, conflito
   entre fontes vigentes ou alteração normativa cujo alcance não esteja
   confirmado.

Não é necessário ler toda a documentação do projeto. A seleção é orientada
pelos elementos realmente afetados, mas deve cobrir a cadeia de autoridade, não
somente arquivos de código ou o precedente técnico mais próximo. Ler uma fonte
sem confrontar seus contratos não satisfaz esta obrigação.

Uma especificação exploratória pode permanecer em `Draft` com relações ainda
abertas. Ela não pode receber recomendação de prontidão enquanto uma autoridade
aplicável permanecer omitida, contraditória ou sem ação definida.

## Análise de implementabilidade

Quando incluída na ordem, registre evidências encontradas, componentes
impactados, restrições conhecidas, incertezas, experimentos necessários e
bloqueadores identificados. Inclua o confronto de autoridades normativas
afetadas; não limite a análise à viabilidade do código.

Não certifique por leitura o que depende de build, protótipo, API, banco,
infraestrutura ou hardware. Registre-o como experimento necessário. Quando o
risco exigir segregação, deixe a análise pendente para o perfil especializado.

## Saída

Deixe a especificação em Rascunho e análise enquanto houver lacuna bloqueante.
Quando o contrato e a análise estiverem suficientes, recomende prontidão ao
Arquiteto. Somente o Arquiteto promove para Pronta e autoriza implementação.
