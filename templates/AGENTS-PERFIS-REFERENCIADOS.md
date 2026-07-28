# Instruções permanentes e roteamento EKM

**Modalidade:** perfis fixos referenciados

**Estado:** incorporado ao template oficial da EKM 1.11

O template canônico vigente é [`AGENTS.md`](AGENTS.md). Este arquivo permanece
como referência histórica compatível com o protocolo experimental 0.2.

## Autoridade

O Arquiteto humano tem autoridade final sobre intenção, prioridade, escopo,
arquitetura, risco, autorização, validação e integração. A ordem recebida por
prompt ou pipeline define o papel e o recorte autorizado.

## Fonte dos perfis

**Raiz local da EKM:** `<CAMINHO_LOCAL_DA_EKM>`

Quando a ordem identificar um papel EKM, antes de qualquer ação:

1. leia integralmente
   `<CAMINHO_LOCAL_DA_EKM>/roles/REGRAS-COMUNS.md`;
2. leia integralmente somente o perfil correspondente na tabela abaixo;
3. leia a especificação indicada na ordem;
4. leia apenas as fontes técnicas pertinentes ao recorte.

| Papel recebido | Perfil |
|---|---|
| Autor da Especificação | `roles/AUTOR-DA-ESPECIFICACAO.md` |
| Engenheiro Analista | `roles/ENGENHEIRO-ANALISTA.md` |
| Engenheiro Implementador | `roles/ENGENHEIRO-IMPLEMENTADOR.md` |
| Engenheiro Revisor | `roles/ENGENHEIRO-REVISOR.md` |

Não carregue perfis de outros papéis nem a metodologia EKM completa. Se a ordem
não identificar um papel ou a fonte não estiver acessível, não inicie a tarefa;
informe o impedimento ao Arquiteto.

## Fontes locais do projeto

- especificações: `<CAMINHO_DAS_ESPECIFICACOES>`;
- decisões e evidências: `<CAMINHO_DO_CHANGELOG>`;
- mapa de conhecimento: `<CAMINHO_DO_MAPA>`;
- arquitetura e padrões: `<FONTES_TECNICAS_LOCAIS>`;
- comandos canônicos: `<BUILD_TESTES_E_VALIDACOES>`.

## Invariantes locais

- `<REGRA PERMANENTE DO PROJETO>`;
- `<RESTRICAO DE SEGURANCA OU PLATAFORMA>`;
- `<ARQUIVOS OU OPERACOES PROIBIDAS>`.

As regras comuns e o perfil selecionado definem condições de entrada, evidência,
Git e encerramento. Regras específicas da tarefa pertencem à especificação ou à
ordem do Arquiteto, não a este arquivo.
