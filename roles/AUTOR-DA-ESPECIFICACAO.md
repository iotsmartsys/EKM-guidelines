# Perfil EKM — Autor da Especificação

**Versão do perfil:** 1.3

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
