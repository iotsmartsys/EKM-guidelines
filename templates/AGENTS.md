# Instruções permanentes e roteamento EKOM

**Modelo EKOM:** 3.1

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
por especialista separado. Challenge/revisão é consultivo e acionado pelo
Arquiteto ou pelo risco; não é gate universal. A ordem pode combinar autoria e
análise, mas deve declarar segregação quando ela for necessária.

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
- Agentes registram fatos, decisões locais, dúvidas, limitações e desvios.
- Análise, implementação, challenge e validação produzem relatórios separados;
  não são anexados à especificação.
- Somente o Arquiteto incorpora achados em fontes normativas, aceita ADRs e
  promove estados; exceção mecânica exige arquivos e transformação explícitos.
- Somente o Arquiteto determina conclusão ou reabertura do workflow.
- `<REGRA_PERMANENTE_DO_PROJETO>`;
- `<RESTRICAO_DE_SEGURANCA_OU_PLATAFORMA>`;
- `<ARQUIVOS_OU_OPERACOES_PROIBIDAS>`.

> **Specifications orchestrate. Code implements.**
