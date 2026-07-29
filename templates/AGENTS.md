# Instruções permanentes e roteamento EKM

**Modelo EKM:** 1.17

**Modalidade:** atores com perfis referenciados

**Estado:** vigente

## Autoridade

O Arquiteto humano tem autoridade final sobre intenção, prioridade, escopo,
arquitetura, risco, autorização, validação e integração. A ordem recebida por
prompt ou pipeline identifica papel, especificação e recorte autorizado.

## Fonte dos perfis

**Raiz da EKM:** `<CAMINHO_ACESSIVEL_DA_EKM>`

Antes de qualquer atuação EKM:

1. leia integralmente
   `<CAMINHO_ACESSIVEL_DA_EKM>/roles/REGRAS-COMUNS.md`;
2. leia integralmente somente o perfil correspondente ao papel recebido;
3. leia a especificação indicada, quando aplicável;
4. leia apenas as fontes técnicas pertinentes ao recorte.

| Papel recebido | Perfil |
|---|---|
| Autor da Especificação | `roles/AUTOR-DA-ESPECIFICACAO.md` |
| Engenheiro Analista | `roles/ENGENHEIRO-ANALISTA.md` |
| Engenheiro Implementador | `roles/ENGENHEIRO-IMPLEMENTADOR.md` |
| Engenheiro Revisor | `roles/ENGENHEIRO-REVISOR.md` |
| Consultor de Arquitetura | `roles/CONSULTOR-DE-ARQUITETURA.md` |

Não carregue perfis de outros papéis nem a metodologia EKM completa. Se a ordem
não identificar papel, resultado e recorte, ou se a fonte não estiver
acessível, não inicie a tarefa; informe o impedimento ao Arquiteto. A
especificação é obrigatória no ciclo funcional; o Consultor pode receber
Não se aplica [`Not Applicable`] em governança ou apoio fora desse ciclo.

## Fontes locais do projeto

- especificações: `<CAMINHO_DAS_ESPECIFICACOES>`;
- decisões e evidências: `<CAMINHO_DO_CHANGELOG>`;
- mapa de conhecimento: `<CAMINHO_DO_MAPA>`;
- arquitetura e padrões: `<FONTES_TECNICAS_LOCAIS>`;
- comandos canônicos: `<BUILD_TESTES_E_VALIDACOES>`.

## Invariantes locais

- Preserve arquitetura, organização e separação de responsabilidades vigentes;
  use as fontes técnicas acima e o precedente equivalente mais próximo. Desvio
  exige autorização arquitetural explícita na especificação.
- `<REGRA_PERMANENTE_DO_PROJETO>`;
- `<RESTRICAO_DE_SEGURANCA_OU_PLATAFORMA>`;
- `<ARQUIVOS_OU_OPERACOES_PROIBIDAS>`.

As regras comuns e o perfil selecionado definem condições de entrada, promoção
de estados, evidência, Git e encerramento. Regras específicas da tarefa
pertencem à especificação ou à ordem do Arquiteto, não a este arquivo.
