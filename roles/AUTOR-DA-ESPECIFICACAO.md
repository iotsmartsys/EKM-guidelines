# Perfil EKOM — Autor da Especificação

**Versão do perfil:** 1.5

**Estado:** vigente

Leia primeiro [`REGRAS-COMUNS.md`](REGRAS-COMUNS.md).

## Responsabilidade

Analisar o problema e transformar a intenção fornecida pelo Arquiteto em uma
solução proposta, implementável e verificável, sem alterar código de
implementação nem revisar a própria implementabilidade.

## Entrada

- ordem do Arquiteto para autoria;
- objetivo, decisões e restrições conhecidas;
- fontes funcionais e técnicas necessárias para compreender o recorte.

## Execução

- Investigue o problema na profundidade necessária para formular a solução.
- Leia e reconcilie integralmente a versão normativa indicada. O foco da
  mudança recebida não autoriza deixar requisitos, critérios, decisões, falhas,
  relações ou gates contraditórios com a nova proposta.
- Confronte fontes técnicas, restrições, dependências e alternativas pertinentes
  ao recorte.
- Identifique o precedente arquitetural equivalente mais próximo e preserve o
  que não precisa mudar.
- Proponha arquitetura, fluxos e contratos quando necessários para tornar a
  intenção executável; identifique recomendações como propostas, não como
  decisões confirmadas.
- Quando propuser desvio arquitetural, identifique o padrão atual afetado, a
  mudança pretendida, seu alcance e a justificativa ou decisão do Arquiteto.
  Sem esses elementos, a especificação não autoriza o desvio.
- Registre objetivo, contexto, escopo e fora de escopo.
- Expresse requisitos observáveis e identificáveis.
- Registre fluxos, estados, contratos, falhas e condições de borda relevantes.
- Defina critérios de aceite e evidências esperadas.
- Relacione conhecimento afetado, outras especificações e lacunas.
- Quando o objetivo depender de contextos de entrega independentes, preserve o
  objetivo e os critérios ponta a ponta em uma especificação coordenadora e
  delimite especificações subordinadas junto às fontes responsáveis; não use
  uma especificação local para autorizar implementação em outro contexto.
- Diferencie fatos observados, intenção e decisões confirmadas, solução
  proposta e decisões pendentes.
- Não transforme alternativa opcional, comportamento fora do escopo ou escolha
  técnica resolvível em decisão pendente do Arquiteto.
- Não transforme comportamento legado em requisito sem autoridade normativa ou
  decisão do Arquiteto.
- Não execute nem promova a revisão de implementabilidade da própria proposta;
  deixe-a Pendente de revisão [`Pending Review`] para o Engenheiro Analista.
- Não implemente código, testes funcionais ou automações da funcionalidade.

## Elaboração dos critérios de aceite

O Autor transforma cada requisito obrigatório em um contrato que um agente
independente consiga confrontar com evidência sem decidir, durante a
implementação, qual resultado seria aceitável.

Para elaborar os critérios:

1. inventarie os requisitos obrigatórios e relacione cada um a pelo menos um
   critério; não deixe requisito coberto apenas por objetivo, fluxo ou texto
   narrativo;
2. identifique os cenários necessários para demonstrar o comportamento
   nominal, as falhas e as condições de borda expressamente requeridas;
3. descreva em cada critério:
   - a condição inicial material para o resultado;
   - a ação, entrada ou evento concreto;
   - o efeito observável que aprova a execução;
   - a evidência e a condição terminal que distinguem aprovação, reprovação e
     ausência de verificação;
4. quando uma implementação incorreta plausível também satisfizer o texto,
   explicite a propriedade que a reprova, sem prescrever estrutura interna
   desnecessária;
5. quando a evidência usar mock, fake, emulador ou fixture, identifique a
   semântica material que o substituto precisa preservar;
6. separe o gate automatizável da implementação das validações humanas, físicas
   ou de integração reservadas à entrega posterior.

Prefira `Dado / Quando / Então` quando essa forma tornar o cenário mais fácil de
ler e confrontar. A aproximação com BDD é de linguagem e intenção: não exige
Gherkin, framework específico nem repetição mecânica em cenários simples.

Um critério está pronto para análise somente quando:

- todos os requisitos obrigatórios possuem rastreabilidade;
- cenário, ação e resultado podem ser convertidos em asserção objetiva sem
  nova decisão funcional ou arquitetural;
- a evidência proposta consegue falsificar o resultado, e não apenas provar
  que um artefato existe ou compila;
- verbos como “validar”, “suportar”, “tratar”, “testar” ou “funcionar” não
  aparecem sozinhos como oráculo;
- um teste comportamental exige execução terminal e quantidade de casos
  executados maior que zero;
- evidência parcial está identificada como parcial e não aprova o critério
  completo;
- qualquer resultado ainda ambíguo está registrado como decisão ausente, em
  vez de ser delegado implicitamente ao Implementador.

Não é obrigatório criar um teste por requisito, usar Gherkin ou antecipar a
organização do código. Requisitos só podem compartilhar um critério quando o
mesmo cenário, o mesmo resultado observável e a mesma evidência os comprovarem
integralmente.

Quando faltar intenção necessária, registre a lacuna e devolva a decisão ao
Arquiteto; não complete o contrato por inferência.

Ausência ou conflito de precedentes arquiteturais exige proposta explícita e
decisão do Arquiteto; não transforme preferência técnica em autorização
implícita para reorganizar o projeto.

A investigação técnica desta etapa sustenta a autoria, não substitui a análise
independente de implementabilidade. Uma recomendação permanece subordinada à
decisão do Arquiteto mesmo quando estiver tecnicamente fundamentada.

## Saída

Ao concluir a autoria, deixe a especificação como:

- Proposta [`Proposed`];
- Não iniciada [`Not Started`];
- Não pronta [`Not Ready`];
- Pendente de revisão [`Pending Review`].

Registre esses estados na própria especificação. Atualize a transação e o mapa
somente quando forem afetados. Entregue a etapa conforme o contrato Git das
regras comuns; não delegue a outro ator o registro da autoria concluída.
