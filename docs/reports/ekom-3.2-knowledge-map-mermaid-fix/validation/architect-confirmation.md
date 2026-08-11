# Relatório de validação — correção do Mermaid no mapa EKOM 3.2

**Classe da fonte:** Relatório

**Papel:** Consultor de Arquitetura com confirmação do Arquiteto

**Especificação:** Não se aplica; correção do template vigente da EKOM

**Revisão confrontada:** EKOM 3.2 vigente antes desta correção

**Estado:** Concluído

> Este relatório registra evidência observada e não promove estado por
> autoridade própria.

## Ordem e recorte

O Arquiteto relatou que o Mermaid de
`templates/docs/rfc/KNOWLEDGE-MAP.md` não renderizava no GitHub e autorizou a
correção, sua proteção proporcional e a integração na `main`. O recorte não
altera as regras, os estados nem a versão normativa da EKOM 3.2.

## Causa confirmada

Os placeholders `<...>` dentro dos rótulos Mermaid eram interpretados pelo
renderizador como marcação HTML. Os conteúdos eram removidos e a expressão
resultante continha rótulos vazios, causando erro de análise.

## Resultado material

- os rótulos exemplificativos usam texto simples, sem delimitadores HTML;
- a guarda documental rejeita placeholders em maiúsculas entre `<...>` dentro
  de blocos Mermaid;
- elementos Mermaid legítimos, como `<br/>`, permanecem admitidos;
- a documentação da guarda registra a nova verificação.

## Validações

- `git diff --check` aprovado;
- script da guarda compilável;
- roteamento documental EKOM aprovado;
- template vigente aprovado pela guarda;
- teste negativo confirmou a detecção do formato que causava a falha;
- busca não encontrou o formato inválido em outros blocos Mermaid normativos.

## Limitações e independência

Não houve migração de projetos adotantes nem alteração semântica do mapa. O
Consultor preparou e validou a correção e, portanto, não alega revisão
independente.

## Decisão do Arquiteto

O Arquiteto confirmou o registro e autorizou relatório, commit, publicação,
merge e integração na `main`. A EKOM permanece na versão 3.2.
