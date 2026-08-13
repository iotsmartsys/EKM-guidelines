# ADR-0012 — Branch derivada da especificação

**Estado:** Aceita

**Data:** 2026-08-13

**Versão resultante:** EKOM 4.3

## Contexto

Durante a construção do piloto EKOM no n8n, a submissão para análise ainda
exigia `working_branch`. O campo transferia ao Arquiteto uma decisão operacional
de Git e permitia nomes divergentes para a mesma especificação. A automação
futura por commit também precisava de uma relação determinística entre branch e
fonte normativa.

## Decisão

Trabalho governado por uma especificação principal usa:

```text
docs/specs/<NomeDaEspecificacao>.md
             ↓
spec/<nome-da-especificacao>
```

O slug é o nome do arquivo sem `.md`, convertido para minúsculas. O nome do
arquivo usa segmentos alfanuméricos ASCII separados por hífen. A automação não
traduz, abrevia nem acrescenta sufixos.

Em mudança multi-especificação, a especificação coordenadora determina a
branch. Ausência de coordenadora ou colisão com outra transação ativa bloqueia a
automação e retorna ao Arquiteto.

## Consequências

- o Arquiteto não informa nem escolhe a branch durante a autoria;
- agentes e automações derivam o mesmo nome da fonte normativa;
- gatilhos podem observar `spec/**` e localizar a especificação correspondente;
- o caminho da especificação passa a ser suficiente para derivar a branch;
- renomear a especificação antes da entrega altera também a branch prevista;
- a convenção não autoriza criação, push, análise ou integração por si só.

## Alternativas consideradas

### Branch escolhida manualmente

Rejeitada porque repete decisão operacional, aumenta divergência e dificulta
gatilhos determinísticos.

### Branch derivada apenas do identificador da transação

Rejeitada como regra principal porque o identificador não localiza diretamente
a fonte normativa e mantém dois nomes independentes.

### Sufixo automático para colisões

Rejeitado porque oculta conflito de transação e reduz previsibilidade.

## Evidência e revisão

A regra foi solicitada e confirmada pelo Arquiteto durante o piloto n8n do
`IoTSmartLink15.4`. Sua eficácia será observada na submissão da especificação de
nível de bateria e na futura migração do gatilho manual para eventos de commit.
