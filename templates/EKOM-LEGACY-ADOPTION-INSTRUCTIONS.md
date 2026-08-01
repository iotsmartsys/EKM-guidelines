# Instrução — Adoção inicial do EKOM em repositório legado

Adote o EKOM 2.0 no repositório `<CAMINHO_DO_REPOSITORIO>`.

O Arquiteto autoriza nesta tarefa somente levantamento e fundação documental.
Não altere código, testes, dependências, build, automações ou configuração.

## Contrato da tarefa

1. Comece somente em uma branch derivada da `main`, nunca diretamente na
   `main`.
2. Comece somente com a árvore de trabalho limpa.
3. Leia as instruções locais e preserve documentação existente.
4. Produza uma fundação pequena e adaptada ao projeto.
5. Não declare como requisito uma intenção que não esteja comprovada.
6. Instale o `AGENTS.md` com roteamento para os perfis oficiais do EKOM.
7. Termine com commit, push e árvore de trabalho limpa.

Não copie branch, SHA, comandos de leitura ou mensagem de commit para os
documentos. O Git mantém essa trilha. A ordem não autoriza force push, merge,
tag, release ou deploy.

## Fundação recomendada

```text
AGENTS.md
docs/rfc/KNOWLEDGE-MAP.md
docs/rfc/EKOM-CHANGELOG.md
docs/specs/SYSTEM-DOSSIER.md
```

Crie `docs/rfc/EKOM-GUIDELINES.md` somente se o projeto não puder referenciar a
diretriz EKOM aplicável ou precisar de regras locais. Crie especificações
incrementais somente para decisões confirmadas ou domínios que serão tocados.

## Levantamento

Comece por árvore rasa, manifests, configurações e busca de símbolos. Localize:

- entradas, módulos e fronteiras;
- APIs e consumidores;
- fluxos principais;
- persistência e integrações;
- tratamento de falhas e segurança;
- build, testes, distribuição e documentação;
- código legado, obsoleto ou preparatório.

Aprofunde somente o necessário para sustentar conclusões úteis.

Classifique o conhecimento como:

- **fato observado:** comprovado no repositório;
- **decisão confirmada:** declarada pelo Arquiteto ou por fonte normativa;
- **inferência:** explicação provável ainda não confirmada;
- **lacuna:** conhecimento necessário ausente;
- **desvio:** diferença comprovada entre intenção e estado atual.

Não transforme inferência em decisão. Agrupe perguntas curtas apenas quando a
resposta mudar a interpretação ou o trabalho.

## Ativos

- `AGENTS.md`: porta de entrada curta para agentes.
- `KNOWLEDGE-MAP.md`: fontes, domínios, evidências e lacunas, sem duplicar
  especificações.
- `EKOM-CHANGELOG.md`: abra `EKOM-CHG-0001` e registre objetivo, decisões,
  lacunas, evidências materiais e resultado.
- `SYSTEM-DOSSIER.md`: visão factual do propósito, arquitetura, runtime, APIs,
  dados, integrações, qualidade e operação.
- especificações: somente contratos prioritários, em Rascunho [`Draft`] ou
  Proposta [`Proposed`] até existir decisão humana.

## Validação e conclusão

Antes de encerrar:

- confronte afirmações com fontes;
- valide caminhos e links;
- confira estados entre especificações, mapa e changelog;
- execute `git diff --check` ou equivalente;
- confirme que toda execução iniciada chegou a estado terminal e registre seu
  resultado ou limitação antes do commit, push e resposta conclusiva;
- declare validações não executadas;
- confirme que não houve mudança funcional.

A fundação está concluída quando o conhecimento necessário para o próximo
experimento é localizável, decisões e lacunas estão explícitas, os arquivos
estão consistentes e a entrega foi enviada por commit e push. Quantidade de
documentos não é medida de sucesso.
