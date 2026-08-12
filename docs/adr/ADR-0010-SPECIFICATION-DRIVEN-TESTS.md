# ADR-0010 — Testes dirigidos pela especificação

**Estado:** Aceita

**Data:** 2026-08-12

**Versão resultante:** EKOM 4.1

**Decisor:** Arquiteto humano

## Contexto

O perfil do Implementador determinava atualizar “código, testes e conhecimento
afetado” e executar validações proporcionais ao risco. Mesmo com a execução de
testes condicionada a autorização própria, essa redação permitia ao
Implementador criar ou ampliar suítes por iniciativa técnica.

Em uma implementação real, a permissão produziu vários artefatos de teste. Eles
podiam ser relacionados ao comportamento, mas seu número e desenho passaram a
ser decididos durante a implementação. Isso aumenta código derivado,
manutenção, oráculos potencialmente arbitrários e conhecimento fora do mapa
normativo.

## Decisão

A ordem de implementação não autoriza por si só criar, ampliar, reestruturar ou
corrigir testes. Um teste integra o recorte somente quando a especificação
normativa corrente o exige explicitamente.

Para exigir teste, a especificação identifica:

- requisito ou critério de aceite sustentado;
- cenário e resultado observável;
- classe ou meio do teste, como host-native, target, integração ou hardware;
- artefato ou consumidor material, quando necessário para delimitar o alcance.

Uma menção genérica a qualidade, cobertura, regressão, validação proporcional
ou “adicionar testes” não autoriza criar testes. A especificação pode declarar
explicitamente que nenhum artefato de teste será produzido.

Testes existentes não são alterados apenas porque foram encontrados ou porque
uma API mudou. Se um teste fora do recorte deixar de compilar, o Implementador
registra o consumidor afetado e a limitação. Sua correção exige emenda da
especificação, seguida de nova análise quando a mudança for normativa.

Criar ou alterar um teste autorizado não autoriza executá-lo. Execução ou
coleta de testes, hardware, flash, monitor, deploy e operações externas
continuam dependentes de permissão operacional própria. A especificação define
a evidência desejada; a ordem operacional define se ela pode ser produzida
naquela atuação.

O Implementador realiza inspeção do próprio delta e o build canônico
intrínseco. Outras validações somente são implementadas quando exigidas pela
especificação e somente são executadas quando cobertas pelas permissões
vigentes. Ausência de permissão permanece `Not Executed` e não é convertida em
sucesso.

## Consequências

- o Autor decide se teste é parte do produto documental da mudança;
- o Analista confronta necessidade, alcance, meio e consumidores dos testes
  exigidos;
- o Implementador não inventa matriz, suíte ou cobertura;
- o Revisor não transforma preferência por testes em defeito quando a
  especificação não os contratou;
- build continua intrínseco e pode construir alvos existentes sem autorizar
  sua alteração ou execução;
- a especificação cresce apenas quando o risco justifica explicitamente uma
  evidência automatizada.

## Critério de reavaliação

Reavaliar se a regra causar regressões recorrentes por testes existentes não
reconciliados, se especificações passarem a listar testes sem relação com
critérios de aceite ou se o volume de código de teste continuar crescendo sem
decisão normativa rastreável.
