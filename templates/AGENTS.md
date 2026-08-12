# Instruções permanentes e roteamento EKOM

**Modelo EKOM:** 4.0

**Modalidade:** capacidades referenciadas e governança proporcional

**Estado:** vigente

## Autoridade

O Arquiteto humano tem autoridade final sobre intenção, prioridade, escopo,
arquitetura, risco aceitável, relevância das críticas, suficiência das
evidências, aprovação, conclusão ou reabertura e integração. A especificação é
a fonte da verdade para comportamento e governa a execução dos agentes.

## Fonte dos perfis

**Raiz do EKOM:** `<CAMINHO_ACESSIVEL_DO_EKOM>`

Antes de qualquer atuação EKOM:

1. leia integralmente `roles/REGRAS-COMUNS.md`;
2. leia o perfil correspondente à capacidade recebida;
3. leia a especificação indicada, quando aplicável;
4. leia somente as fontes técnicas pertinentes.

| Capacidade recebida | Perfil |
|---|---|
| Autor da Especificação | `roles/AUTOR-DA-ESPECIFICACAO.md` |
| Engenheiro Analista | `roles/ENGENHEIRO-ANALISTA.md` |
| Engenheiro Implementador | `roles/ENGENHEIRO-IMPLEMENTADOR.md` |
| Crítico ou Engenheiro Revisor | `roles/ENGENHEIRO-REVISOR.md` |
| Consultor de Arquitetura | `roles/CONSULTOR-DE-ARQUITETURA.md` |

Análise de implementabilidade é obrigatória antes da implementação, mas pode
ser feita pelo Autor, pelo Autor apoiado por IA, por agente especializado ou
por especialista separado. Revisão é o quarto estágio; profundidade,
independência e challenge adicional são proporcionais ao risco. A ordem pode
combinar autoria e análise, mas deve declarar segregação quando necessária.

Implementabilidade é avaliada dentro da baseline e do recorte. Capacidade
arquitetural ausente, independente e transversal bloqueia a funcionalidade e
exige decisão do Arquiteto sobre análise e especificação preparatória; não é
absorvida como detalhe da especificação funcional ou da implementação.

Implementação exige análise `Ready` da versão corrente e ordem explícita do
Arquiteto para implementar essa versão. A ordem aprova e autoriza a passagem;
não existe promoção ou campo documental intermediário. Análise ausente,
superada por mudança normativa ou ordem ambígua obriga recusa sem mutação.

Satisfeita essa entrada, a implementação de artefato construível inclui seu
build canônico proporcional. Build não exige cláusula na especificação e não
autoriza execução de testes, hardware, deploy ou outra operação externa.

## Fontes locais do projeto

- especificações: `<CAMINHO_DAS_ESPECIFICACOES>`;
- ADRs e RFCs: `<CAMINHO_DAS_DECISOES>`;
- relatórios: `<CAMINHO_DOS_RELATORIOS>`;
- transações e lacunas: `<CAMINHO_DO_CHANGELOG>`;
- mapa de conhecimento: `<CAMINHO_DO_MAPA>`;
- arquitetura e padrões: `<FONTES_TECNICAS_LOCAIS>`;
- comandos canônicos: `<BUILD_TESTES_E_VALIDACOES>`.

## Invariantes locais

- Preserve arquitetura, organização e separação de responsabilidades; desvio
  exige decisão arquitetural explícita.
- Testes são evidências, não prova absoluta; não os altere apenas para obter
  verde nem os use como argumento autorreferente.
- Build canônico dos entregáveis afetados integra a implementação; registre
  resultado terminal e não declare conclusão com build falho ou não executado.
- Agentes registram fatos, decisões locais, dúvidas, limitações e desvios.
- Análise, implementação, revisão e evidência operacional produzem registros
  separados;
  não são anexados à especificação.
- O mapa combina índice de autoridade, árvore hierárquica e Mermaid de relações
  conforme os gatilhos normativos da ADR-0004.
- Somente o Arquiteto incorpora achados em fontes normativas, aceita ADRs e
  decide estados; exceção mecânica exige arquivos e transformação explícitos.
- Somente o Arquiteto determina conclusão ou reabertura do workflow.
- `<REGRA_PERMANENTE_DO_PROJETO>`;
- `<RESTRICAO_DE_SEGURANCA_OU_PLATAFORMA>`;
- `<ARQUIVOS_OU_OPERACOES_PROIBIDAS>`.

> **Specifications orchestrate. Code implements.**
