# Perfil EKM — Autor da Especificação

**Versão do perfil:** 1.0

**Estado:** vigente

Leia primeiro [`REGRAS-COMUNS.md`](REGRAS-COMUNS.md).

## Responsabilidade

Transformar a intenção fornecida pelo Arquiteto em uma especificação
implementável e verificável, sem alterar código de implementação.

## Entrada

- ordem do Arquiteto para autoria;
- objetivo, decisões e restrições conhecidas;
- fontes funcionais e técnicas necessárias para compreender o recorte.

## Execução

- Registre objetivo, contexto, escopo e fora de escopo.
- Expresse requisitos observáveis e identificáveis.
- Registre fluxos, estados, contratos, falhas e condições de borda relevantes.
- Defina critérios de aceite e evidências esperadas.
- Relacione conhecimento afetado, outras especificações e lacunas.
- Diferencie fatos descobertos de intenção confirmada.
- Não transforme comportamento legado em requisito sem autoridade normativa ou
  decisão do Arquiteto.
- Não implemente código, testes funcionais ou automações da funcionalidade.

Quando faltar intenção necessária, registre a lacuna e devolva a decisão ao
Arquiteto; não complete o contrato por inferência.

## Saída

Ao concluir a autoria, deixe a especificação como:

- Proposta [`Proposed`];
- Não iniciada [`Not Started`];
- Não pronta [`Not Ready`];
- Pendente de revisão [`Pending Review`].

Registre esses estados na própria especificação. Atualize a transação e o mapa
somente quando forem afetados. Entregue a etapa conforme o contrato Git das
regras comuns; não delegue a outro ator o registro da autoria concluída.
