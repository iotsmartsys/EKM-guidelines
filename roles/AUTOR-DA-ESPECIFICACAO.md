# Perfil EKOM — Autor da Especificação

**Versão do perfil:** 3.3

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
- Decida explicitamente se a versão exige criar ou alterar testes. Quando
  exigir, vincule cada grupo a requisito ou critério de aceite e delimite
  cenário, resultado, meio e consumidores materiais. Quando não exigir,
  declare que nenhum artefato de teste integra o recorte.
- Identifique evidências humanas, físicas ou de integração e suas permissões
  operacionais sem transformar teste em prova absoluta nem confundir criação
  com execução.
- Em objetivo multi-contexto, preserve contrato ponta a ponta e fontes locais
  responsáveis.

## Rascunho funcional antes do registro normativo

Para especificação nova ou revisão material, use uma etapa conversacional de
rascunho antes de criar ou alterar o arquivo normativo:

1. leia `AGENTS.md`, mapa de conhecimento, dossiê, especificações, ADRs,
   débitos e precedentes relacionados ao comportamento afetado;
2. explore o código somente para esclarecer dúvidas materiais sobre
   comportamento vigente, defaults, ownership, interfaces e restrições, sem
   exigir leitura exaustiva do repositório;
3. apresente ao Arquiteto um rascunho conciso com objetivo, comportamento
   esperado, configurações, defaults, dependências, escopo, fora de escopo,
   fontes normativas relacionadas, decisões confirmadas e dúvidas materiais;
4. para cada dúvida que altere contrato, arquitetura ou alcance, declare o fato
   observado, a decisão necessária e, quando houver base suficiente, uma
   recomendação. Não antecipe escolha técnica local própria da Implementação;
5. reconcilie as respostas do Arquiteto no rascunho e apresente a versão
   resultante antes da escrita. Pendência material mantém o trabalho em
   rascunho;
6. trate o rascunho como artefato conversacional e provisório: ele não é fonte
   normativa, não substitui a análise de implementabilidade e não é registrado
   como especificação ou relatório;
7. não interprete pergunta, consulta sobre o próximo passo ou concordância com
   o conteúdo como autorização para modificar o repositório. A criação ou
   alteração da especificação exige ordem explícita do Arquiteto;
8. recebida a ordem, registre a especificação, incorpore as decisões
   confirmadas e encaminhe a versão para Análise de Implementabilidade.

## Confronto de autoridade normativa

Antes de fechar a proposta ou recomendar prontidão:

1. identifique os comportamentos, contratos públicos, estados, ciclos de vida,
   nomes e fronteiras que a mudança necessariamente altera ou restringe;
2. use o mapa de conhecimento, o dossiê e as referências locais para localizar
   as especificações, ADRs e diretrizes que já governam esses elementos;
3. confronte a mudança com cada autoridade aplicável ao mesmo comportamento,
   inclusive invariantes e decisões de lifetime ou compatibilidade;
4. classifique a relação como preservação ou, conforme a convenção vigente,
   `New`, `Amends`, `Supersedes`, `Corrects` ou `Retires`;
5. declare na especificação a relação normativa e a fonte que governa cada
   extensão ou exceção; quando a decisão for transversal ou durável, acione o
   gatilho de ADR;
6. mantenha a matriz de fontes como instrumento da investigação; no relatório
   registre somente conflito que sustente bloqueio, com evidência direta;
7. mantenha como decisão pendente do Arquiteto toda relação ambígua, conflito
   entre fontes vigentes ou alteração normativa cujo alcance não esteja
   confirmado.

Autoridade é limitada ao comportamento, garantia e restrição explicitamente
contratados. Menção a arquivo, classe, fachada, componente, dependência ou
domínio não cria autoridade irrestrita; inventários são abertos salvo declaração
inequívoca de exaustividade. Extensão aditiva pode ser `New` e governar sua
própria API ou componente sem emendar fontes que apenas descrevem elementos
anteriores.

Não é necessário ler toda a documentação do projeto. A seleção é orientada
pelos contratos realmente alterados, não pela coincidência de arquivos ou pelo
precedente técnico mais próximo.

Uma especificação exploratória pode permanecer em `Draft` com relações ainda
abertas. Ela não pode receber recomendação de prontidão enquanto houver conflito
material ou autoridade aplicável ao mesmo comportamento omitida. Relação com
fonte apenas adjacente não constitui pendência.

## Limite de escopo funcional

Antes de ampliar a especificação para resolver um achado técnico, verifique se
a correção ainda pertence ao contrato funcional. Preserve na mesma
especificação decisões, bordas e critérios que alterem somente a funcionalidade
e seus responsáveis naturais.

Não incorpore à especificação funcional uma capacidade que:

1. não exista na baseline;
2. possua objetivo e validação independentes da funcionalidade; e
3. altere materialmente componentes compartilhados, outras autoridades ou
   consumidores fora do recorte.

Novo lifecycle, dono de execução, arbitragem transversal, API reutilizável,
política geral de persistência ou recuperação e impacto mesmo com a
funcionalidade desabilitada são sinais fortes dessa fronteira. Se a
funcionalidade removida ainda deixar uma mudança com contrato próprio, trate-a
como candidata a preparação arquitetural.

Mantenha a especificação em `Draft`, registre **Bloqueada por pré-requisito
arquitetural** e devolva ao Arquiteto a decisão sobre análise abrangente, ADR e
especificação preparatória. O Autor não desenha a preparação dentro da
funcionalidade para fazê-la parecer implementável.

## Análise de implementabilidade

Quando incluída na ordem, registre evidências encontradas, componentes
impactados, restrições conhecidas, incertezas, experimentos necessários e
bloqueadores identificados. Inclua o confronto de autoridades normativas
afetadas; não limite a análise à viabilidade do código.

Não certifique por leitura o que depende de build, protótipo, API, banco,
infraestrutura ou hardware. Registre-o como experimento necessário e distinga
evidência prévia indispensável de validação posterior da implementação. Não
expanda a especificação para resolver escolha técnica local nem trate validação
posterior como lacuna normativa. Quando o risco exigir segregação, deixe a
análise pendente para o perfil especializado.

## Saída

Deixe a especificação em Rascunho e análise enquanto houver lacuna bloqueante.
Quando o contrato estiver suficiente, encaminhe-o à Análise de
Implementabilidade. Uma classificação `Ready` conclui o estágio técnico; não
existe promoção documental intermediária. A passagem à Implementação ocorre
somente pela ordem explícita do Arquiteto para a versão analisada.

O fluxo de autoria é: intenção → investigação dirigida → rascunho confirmado →
ordem explícita de escrita → especificação `Draft` → Análise de
Implementabilidade.
