# Adoção do EKOM em projetos legados

## 1. Princípio

A adoção começa com a menor fundação que permita localizar conhecimento,
registrar decisões e lacunas e executar o próximo experimento com segurança.
Não se documenta todo o legado antes de produzir valor.

## 2. Autoridade e tarefa

O Arquiteto define o repositório, o recorte e se a tarefa é apenas documental.
Essa ordem autoriza a etapa. O agente inicia o fluxo em uma branch derivada da
`main`, com árvore de trabalho limpa, e termina com commit, push e árvore limpa.

O projeto instala um `AGENTS.md` que aponta para os perfis oficiais do EKOM
5.0. Depois da fundação, cada tarefa funcional identifica papel e
especificação. O agente lê regras comuns, exatamente um perfil e somente as
fontes pertinentes ao recorte.

A especificação aplicável torna-se a fonte única da verdade para o
comportamento e o principal objeto que orquestra a tarefa. Código, testes,
automações e relatórios permanecem fontes derivadas.

## 3. Fundação recomendada

```text
AGENTS.md
docs/
├── adr/
├── reports/
├── rfc/
│   ├── REPOSITORY-ENGINEERING-CONTRACT.md
│   ├── REPOSITORY-READINESS.md
│   ├── KNOWLEDGE-MAP.md
│   └── EKOM-CHANGELOG.md
└── specs/
    └── SYSTEM-DOSSIER.md
```

Uma diretriz local é criada apenas quando não há diretriz externa aplicável ou
existem regras próprias. Especificações são criadas para contratos confirmados
ou funcionalidades que serão tocadas.

O mapa preserva um índice de autoridade e acrescenta árvore ou Mermaid quando
hierarquia ou conexão entre alvos for material. Visão não aplicável permanece
declarada com justificativa curta.

O `AGENTS.md` deve substituir todos os placeholders do template por caminhos,
fontes técnicas, validações e invariantes reais do projeto antes do primeiro
trabalho regido pelos perfis.

## 4. Levantamento econômico

1. Localizar instruções, manifests, entradas e documentação.
2. Mapear módulos, APIs, dados, integrações, build, testes e distribuição.
3. Separar fato observado, decisão confirmada, inferência, lacuna e desvio.
4. Perguntar ao Arquiteto somente o que muda a interpretação ou a execução.
5. Aprofundar por risco e proximidade do trabalho.

O Git preserva o estado versionado e a linhagem. Não se copiam SHAs, branches ou
listas de comandos para o changelog.

## 5. Cobertura

| Nível | Significado |
|---|---|
| Não mapeado [`Unmapped`] | domínio ainda não localizado |
| Inventariado [`Inventoried`] | entradas e arquivos principais identificados |
| Mapeado [`Mapped`] | fluxos e dependências principais compreendidos |
| Revisado [`Reviewed`] | contratos e riscos confrontados com evidências |
| Especificado [`Specified`] | fonte normativa confirmada |
| Reconstruível [`Reconstructible`] | comportamento pode ser recuperado sem inferência relevante |

Use *specification on touch*: aprofunde o domínio quando ele for alterado.

## 6. Conclusão

A fundação termina quando:

- o próximo trabalho pode localizar suas fontes;
- decisões confirmadas e lacunas relevantes estão explícitas;
- arquitetura, integrações e meios de validação essenciais estão mapeados;
- não houve alteração funcional fora do recorte;
- os ativos estão consistentes;
- a tarefa foi entregue por commit e push.

Auditoria independente, matriz ampla e documentação integral do sistema não são
condições universais de conclusão.

## Qualificação do repositório — EKOM 5.0

Antes de implementar, confirme contrato de engenharia aprovado por
Arquiteto/responsável técnico humano e Repository Readiness válida cobrindo
todo o recorte e suas dependências materiais. `Not Ready` bloqueia;
`Conditionally Ready` permite apenas escopos explicitamente `Ready` e habilitados
por decisão humana. Ausência, insuficiência, aprovação pendente ou avaliação
superada impede mutação de implementação, inclusive na via curta do Consultor.
Levantamento, proposta e documentação autorizados podem preparar a qualificação.

O `Ready` da análise de uma especificação não substitui essa condição de adoção.
Não repita aprovação vigente a cada tarefa. A IA pode sugerir contrato a partir
do código, mas somente o humano pode aprová-lo como norma.

Aplique especificação da tarefa → contrato aprovado → precedentes oficiais →
código existente → preferência do implementador. Especificação não revoga regra
arquitetural silenciosamente: exceção exige decisão humana com regra, motivo,
alcance e validade. Precedente contraditório não se torna norma.


## Qualificação na fundação

Produza `docs/rfc/REPOSITORY-ENGINEERING-CONTRACT.md` como Draft/Proposed,
separe observações de inferências e deixe aprovação pendente até decisão humana.
Use o template `REPOSITORY-READINESS-REPORT-TEMPLATE.md` para registrar cobertura,
evidências, lacunas e desvios em `docs/reports/repository-readiness/`.
Mantenha `docs/rfc/REPOSITORY-READINESS.md` com estado inicial Not Ready e referências
à revisão, avaliação e decisão humana; cadastre ambos no mapa de conhecimento.
Uma norma local existente pode ser referenciada pelo contrato, com versão e alcance.

A fundação documental pode ser entregue com aprovação pendente e implementação
bloqueada. Só anuncie adoção habilitada após qualificação válida no alcance;
não transforme a ordem de instalar EKOM em aprovação do contrato inferido.
