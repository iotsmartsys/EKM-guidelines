# ADR-0013 — Débito técnico como conhecimento deliberadamente postergado

**Estado:** Aceita

**Data:** 2026-08-14

**Versão resultante:** EKOM 4.4

**Decisor:** Arquiteto humano

## Contexto

O EKOM já preservava lacunas de conhecimento, desvios, riscos residuais e
transações de mudança, mas não distinguia uma condição técnica conhecida cuja
correção fosse conscientemente postergada. Essa ausência permitia classificar
débito técnico como `EKOM-GAP`, embora `GAP` signifique conhecimento ausente, ou
deixá-lo apenas em relatório, comentário de código ou conversa sem guarda
persistente.

A necessidade foi observada durante o piloto EKOM no IoTSmartLink15.4. Ao
confrontar o caso, o Arquiteto decidiu que a condição conhecida, sua
consequência e a decisão de postergação precisam sobreviver sem transformar
toda crítica, defeito ou risco residual em débito técnico.

## Decisão

Débito técnico é uma condição técnica conhecida, com consequência identificada,
cuja correção foi conscientemente postergada pelo Arquiteto e que possui gatilho
de reavaliação ou critério objetivo de quitação.

O namespace canônico é `EKOM-DEBT-NNNN`. O mapa de conhecimento mantém o
registro persistente e navegável. Cada registro contém, no mínimo:

- condição atual e alcance afetado;
- evidência que comprova a condição;
- consequência ou risco material;
- decisão explícita de postergação do Arquiteto;
- gatilho de reavaliação ou critério de quitação;
- relações com especificações, ADRs, gaps e transações de mudança.

Os estados canônicos são:

- `Accepted`: postergação aceita explicitamente pelo Arquiteto;
- `In Remediation`: correção autorizada e vinculada a uma transação;
- `Repaid`: critério de quitação satisfeito e quitação determinada pelo
  Arquiteto;
- `Superseded`: registro substituído por outro débito ou decisão identificada.

Antes de `Accepted`, uma observação é achado, defeito, desvio, risco ou lacuna
aguardando classificação; agentes não criam aceitação tácita. Somente o
Arquiteto aceita postergação e determina `Repaid` ou `Superseded`. Agentes
preservam fatos, evidências e o estado operacional `In Remediation` quando
sustentado pela atuação autorizada.

Aceitar débito não altera a evidência nem torna conforme uma violação de
especificação vigente. A fonte normativa não é enfraquecida apenas para fazer o
estado atual parecer correto. A remediação usa `EKOM-CHG`, especificação e ADR
quando aplicáveis, percorre o workflow proporcional e produz evidência de
quitação.

Prazo, prioridade e estimativa podem ser registrados quando apoiarem decisão,
mas não são campos universais. O gatilho pode ser uma condição material, como
novo consumidor, mudança de plataforma, incidente, limite operacional ou
início de uma evolução relacionada.

## Consequências

- conhecimento ausente continua sendo `EKOM-GAP`, sem mistura com postergação
  consciente;
- defeito e desvio permanecem verdadeiros mesmo quando o risco de conviver com
  eles é aceito;
- relatórios preservam a descoberta, enquanto o mapa preserva o débito vigente;
- changelog e transações apontam débitos relacionados sem duplicar seu contrato;
- dívida arquitetural pode exigir ADR, mas dívida local não cria ADR por si só;
- não surge estágio novo no workflow nem backlog universal obrigatório;
- projetos sem débito aceito podem declarar a seção não aplicável ou mantê-la
  vazia.

## Alternativas rejeitadas

- **Usar somente `EKOM-GAP`:** rejeitada porque confunde desconhecimento com
  decisão consciente de postergação.
- **Registrar somente no relatório:** rejeitada porque relatório é histórico e
  não oferece guarda vigente nem critério de quitação.
- **Tratar todo defeito postergado como resolvido por risco aceito:** rejeitada
  porque autoridade humana não modifica evidência nem conformidade normativa.
- **Exigir prazo e prioridade para todo débito:** rejeitada por criar
  burocracia universal; gatilhos materiais frequentemente são mais úteis.

## Critério de reavaliação

Reavaliar se o registro produzir inventário sem decisões, se débitos forem
usados para contornar gates de implementação, se a distinção com defeito e
`GAP` continuar ambígua ou se os campos mínimos não sustentarem priorização e
quitação em casos reais.
