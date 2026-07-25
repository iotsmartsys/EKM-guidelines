# Instrução — Adoção inicial da EKM em repositório legado

Use este documento como instrução inicial para um agente. Substitua os campos entre `<...>` antes da execução quando a informação estiver disponível.

---

## Missão

Adote a Engineering Knowledge Management (EKM) no repositório `<CAMINHO_DO_REPOSITORIO>`.

O objetivo desta etapa é descobrir, organizar e preservar o conhecimento vigente. Não implemente refatorações, correções ou novas funcionalidades, salvo autorização adicional explícita.

Produza os ativos mínimos:

```text
AGENTS.md
docs/rfc/EKM-GUIDELINES.md
docs/rfc/KNOWLEDGE-MAP.md
docs/rfc/EKM-CHANGELOG.md
docs/specs/SYSTEM-DOSSIER.md
docs/specs/<especificações prioritárias>.md
```

Use os modelos EKM disponíveis como base, adaptando-os ao projeto sem introduzir regras específicas de outro sistema.

## Restrições iniciais

- Não alterar código-fonte, testes, dependências, build, CI/CD, release ou configuração.
- Não executar commit, tag, push, branch, PR, deploy ou publicação.
- Não apagar, mover ou reescrever documentos existentes.
- Preservar toda a árvore de trabalho inicial.
- Não declarar como requisito uma intenção que não esteja comprovada.
- Não classificar especificação descoberta como `Active` sem fonte inequívoca ou aprovação humana.
- Otimizar leitura e uso de contexto; não despejar arquivos extensos sem necessidade.

## Fase 1 — Baseline

Registre:

- caminho do repositório;
- branch e commit atuais;
- estado completo da árvore de trabalho;
- instruções locais (`AGENTS.md` e equivalentes);
- documentação existente;
- linguagens, manifests e ferramentas principais.

O estado de referência é a árvore de trabalho observada, não somente `HEAD`.

## Fase 2 — Inventário econômico

Comece em largura usando árvore rasa, listagem de arquivos, arquivos de
manifesto, configurações e busca de símbolos. Localize:

1. entradas e executáveis;
2. módulos e fronteiras arquiteturais;
3. APIs públicas e consumidores;
4. principais fluxos de runtime;
5. persistência, formatos e migrações;
6. integrações e protocolos externos;
7. tratamento de erro, recuperação e segurança;
8. testes e validações em hardware, quando aplicável;
9. build, CI/CD, release e distribuição;
10. documentação e decisões existentes;
11. código legado, experimental ou preparatório.

Aprofunde somente arquivos necessários para comprovar cada conclusão.

## Fase 3 — Separação epistemológica

Classifique cada conclusão como:

- **Fato observado:** comprovado por código, configuração, teste ou documento vigente.
- **Decisão confirmada:** intenção informada por responsável humano ou fonte normativa inequívoca.
- **Inferência:** explicação provável que ainda exige confirmação.
- **Lacuna:** conhecimento necessário que não pode ser determinado com segurança.
- **Desvio:** diferença comprovada entre comportamento desejado e estado atual.

Não transforme inferências em decisões.

## Fase 4 — Perguntas ao responsável

Agrupe perguntas curtas apenas para pontos que mudam a interpretação do sistema, como:

- plataformas e versões ainda suportadas;
- APIs que exigem retrocompatibilidade;
- comportamento intencional versus limitação atual;
- código obsoleto versus preparação futura;
- integrações prioritárias;
- regressões históricas;
- processo desejado de release;
- regras de segurança ou persistência não comprováveis.

Continue autonomamente nos fatos independentes das respostas. Não bloqueie todo o levantamento por uma dúvida localizada.

## Fase 5 — Produção dos ativos

### `AGENTS.md`

Crie a porta de entrada curta e obrigatória. Ela deve ordenar a leitura das
fontes EKM, proteger o estado de referência e definir interrupções e relatório.

### `EKM-GUIDELINES.md`

Adapte as regras gerais da EKM ao repositório. Preserve estados, transações,
lacunas, proteção normativa, estado de referência e critérios de conclusão.

### `KNOWLEDGE-MAP.md`

Mapeie fontes, domínios, implementação principal, evidências, cobertura de adoção e lacunas. Não duplique especificações.

### `EKM-CHANGELOG.md`

Abra `EKM-CHG-0001` para a fundação. Registre estado de referência, ativos,
decisões, validações e resultado. Feche somente após auditoria.

### `SYSTEM-DOSSIER.md`

Produza uma visão executiva factual: propósito, escopo, arquitetura, runtime, API, dados, integrações, qualidade, operação e riscos. O dossiê é normativo apenas nas decisões explicitamente confirmadas; demais trechos devem indicar sua natureza.

### Especificações prioritárias

Crie somente as necessárias para registrar decisões já confirmadas ou contratos críticos. Use requisitos estáveis e estados independentes. Quando a intenção ainda depender de revisão, use `Draft` ou `Proposed`.

## Fase 6 — Cobertura e lacunas

Classifique cada domínio como:

```text
Unmapped → Inventoried → Mapped → Reviewed → Specified → Reconstructible
```

Registre uma `EKM-GAP-NNNN` para toda ausência que impeça evolução segura. Cada gap deve possuir critério objetivo de encerramento.

## Fase 7 — Auditoria final

Antes de encerrar:

- confronte afirmações com suas fontes;
- valide caminhos e links;
- confira estados entre especificações, mapa e changelog;
- verifique integridade textual (`git diff --check` ou equivalente);
- confirme que somente os ativos autorizados foram alterados;
- declare validações não executadas;
- mantenha divergências de implementação abertas, sem corrigi-las.

## Critério de interrupção

Interrompa somente a parte afetada e solicite decisão quando houver:

- conflito entre fontes normativas;
- necessidade de escolher comportamento de produto;
- possível remoção de compatibilidade ou conhecimento vigente;
- risco de alteração destrutiva;
- impossibilidade de distinguir bug, requisito e legado acidental;
- necessidade de ampliar o escopo autorizado.

## Relatório final obrigatório

Informe:

1. resultado executivo;
2. estado de referência usado;
3. ativos criados e modificados;
4. fatos e decisões registrados;
5. especificações e seus dois estados;
6. cobertura por domínio;
7. lacunas e desvios;
8. validações executadas e pendentes;
9. estado da transação EKM;
10. confirmação de ausência de mudanças funcionais;
11. operações Git ou externas realizadas.

Não apresente a quantidade de documentos como medida de sucesso. O resultado deve ser avaliado pela capacidade de localizar autoridade, reconhecer lacunas e evoluir o sistema sem inventar intenção.
