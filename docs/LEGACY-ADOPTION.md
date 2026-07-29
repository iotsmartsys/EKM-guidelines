# Adoção da EKM em projetos legados

## 1. Princípio

A adoção começa com a menor fundação que permita localizar conhecimento,
registrar decisões e lacunas e executar o próximo experimento com segurança.
Não se documenta todo o legado antes de produzir valor.

## 2. Autoridade e tarefa

O Arquiteto define o repositório, o recorte e se a tarefa é apenas documental.
Essa ordem autoriza a etapa. O agente inicia o fluxo em uma branch derivada da
`main`, com árvore de trabalho limpa, e termina com commit, push e árvore limpa.

O projeto instala um `AGENTS.md` que aponta para os perfis oficiais da EKM
1.15. Depois da fundação, cada tarefa funcional identifica papel e
especificação. O agente lê regras comuns, exatamente um perfil e somente as
fontes pertinentes ao recorte.

## 3. Fundação recomendada

```text
AGENTS.md
docs/
├── rfc/
│   ├── KNOWLEDGE-MAP.md
│   └── EKM-CHANGELOG.md
└── specs/
    └── SYSTEM-DOSSIER.md
```

Uma diretriz local é criada apenas quando não há diretriz externa aplicável ou
existem regras próprias. Especificações são criadas para contratos confirmados
ou funcionalidades que serão tocadas.

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
