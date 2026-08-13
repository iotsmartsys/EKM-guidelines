# ADR-0011 — Entrega Git intrínseca à atuação material

**Estado:** Aceita

**Data:** 2026-08-12

**Versão resultante:** EKOM 4.2

**Decisor:** Arquiteto humano

## Contexto

O EKOM exigia que uma atuação material produzisse commit e, “quando
autorizado”, push. O perfil do Consultor ainda introduzia uma confirmação final
entre o resultado pronto e sua entrega. Na prática, agentes concluíam o
trabalho, mas paravam com arquivos modificados ou commit apenas local à espera
de uma autorização que repetia a ordem inicial.

Essa parada não produzia nova decisão, evidência ou redução de risco. Também
contrariava a expectativa operacional do Arquiteto de que todo trabalho
material terminasse versionado, sincronizado e com árvore limpa.

## Decisão

Toda atuação autorizada que produza mudança material no repositório inclui sua
entrega Git normal:

1. preparar somente alterações pertencentes ao recorte;
2. criar um commit não vazio ao fim da etapa autorizada;
3. fazer push da branch de trabalho corrente;
4. terminar com árvore limpa.

A autorização inicial para produzir a mudança basta. A especificação não
precisa autorizar commit ou push, e o agente não cria um segundo gate de
confirmação apenas para esses atos.

Atuação somente leitura não cria commit. Uma proibição explícita do Arquiteto
prevalece. Se autenticação, rede ou política do remoto impedir o push, o agente
registra a falha com precisão e não apresenta a entrega como sincronizada. Se
alterações preexistentes não puderem ser isoladas com segurança, elas não são
absorvidas para obter uma árvore artificialmente limpa.

Commit e push da branch corrente não autorizam:

- force push ou reescrita de histórico;
- merge ou exclusão de branch;
- tag, release ou deploy;
- publicação em destino diferente do remoto normal da branch;
- inclusão de mudanças alheias ao recorte.

Essas operações mantêm autorização específica. Uma mudança parcial só é
entregue quando constitui resultado coerente e versionável; delta próprio
inválido ou incompleto é removido sem afetar trabalho preexistente.

## Consequências

- commit e push deixam de ser passos administrativos solicitados ao final;
- todos os perfis herdam o mesmo encerramento por meio das regras comuns;
- o Consultor deixa de exigir confirmação final redundante;
- especificações funcionais não repetem autorização de entrega Git;
- falhas de push permanecem visíveis e impedem alegar sincronização;
- integração e publicação continuam decisões distintas do Arquiteto.

## Critério de reavaliação

Reavaliar se a regra causar publicação indevida, mistura recorrente de deltas,
commits incoerentes ou se ambientes sem remoto tornarem o push intrínseco um
impedimento frequente. Medir também se desaparecem as paradas administrativas
com trabalho material pendente.
