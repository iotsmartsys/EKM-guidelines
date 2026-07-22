# Como chegamos ao modelo atual

## Contexto

A EKM surgiu durante experimentos de engenharia assistida por IA em projetos reais. A intenção inicial era aumentar produtividade mantendo o arquiteto humano responsável pelas decisões.

## 1. Especificações melhoraram a execução

Recortes delimitados fizeram o agente implementar, compilar, testar e relatar com menos expansão de escopo. Ficou claro que uma especificação suficientemente completa pode funcionar como unidade de delegação para um desenvolvedor humano ou agente.

## 2. Build e relatório não preservam intenção

Uma consolidação tecnicamente aprovada removeu conhecimento relevante de um documento de arquitetura. O relatório também não destacou adequadamente a mudança normativa. Isso mostrou que:

- código correto não garante conhecimento preservado;
- listar arquivos alterados não explica mudança semântica;
- documentos normativos precisam de proteção explícita.

## 3. O último commit não é sempre o baseline

Em uma reorganização de componentes, comparar somente com `HEAD` quase levou à conclusão errada de que alterações preexistentes haviam sido perdidas. A prova correta exigiu recuperar o estado real do worktree no início da tarefa.

Daí surgiu a regra: baseline é o estado observado, incluindo mudanças não commitadas.

## 4. Transações e lacunas tornaram o processo auditável

Foram introduzidos:

- `EKM-CHG-NNNN` para acompanhar mudanças;
- `EKM-GAP-NNNN` para representar conhecimento ausente;
- estados explícitos de abertura e encerramento;
- Definition of Done que reconcilia código, documentação e evidências.

Isso permitiu reabrir uma mudança quando a prova era insuficiente e encerrá-la novamente somente após nova auditoria.

## 5. Especificações precisam evoluir gradualmente

Funcionalidades não nascem em um único documento ou momento. Protocolos, commissioning, reset, reports, reutilização e correções surgiram em etapas, às vezes com regressão ou mudança de direção.

Por isso, a EKM adotou especificações incrementais e dois estados independentes: autoridade normativa e situação da implementação.

## 6. Adoção em legado exige outro ritmo

Ao iniciar a aplicação em uma biblioteca grande, ficou evidente que tentar documentar tudo seria caro e improdutivo. O modelo passou a usar:

- inventário em largura;
- aprofundamento por risco;
- perguntas humanas apenas sobre intenção;
- specification on touch;
- níveis graduais de cobertura até `Reconstructible`.

## Conclusão experimental

A hipótese atual é que agentes conseguem executar mudanças com mais autonomia quando o repositório contém especificações, regras de preservação, mapa de autoridade e histórico transacional. A autonomia continua limitada onde existe julgamento de produto ou arquitetura.

Este modelo ainda deve evoluir por meio de novas aplicações, auditorias e regressões observadas.
