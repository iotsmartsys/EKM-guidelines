# Prompt opcional — Revisão de integridade da EKM

**Estado:** Experimental

Use somente quando o Arquiteto solicitar uma revisão independente. Esta não é
uma etapa obrigatória do fluxo EKM 1.18.

```text
Revise a integridade EKM da mudança <EKM-CHG-NNNN> no repositório
<CAMINHO_DO_REPOSITORIO>.

O Arquiteto autoriza somente revisão e atualização do registro de evidência.
Não altere código, testes, especificação ou decisões.

1. Comece em uma branch derivada da `main`, nunca diretamente na `main`.
2. Comece com a árvore de trabalho limpa.
3. Leia AGENTS.md, a especificação e a transação relacionadas.
4. Verifique:
   - aderência da implementação aos requisitos;
   - preservação das fontes normativas;
   - coerência dos estados;
   - presença das evidências materiais exigidas;
   - lacunas ou desvios não declarados.
5. Classifique cada achado como Conforme, Não conforme ou Não verificável.
6. Não invente evidência nem transforme risco aceito em validação aprovada.
7. Registre apenas achados materiais.
8. Antes de promover estado, criar o commit final, fazer push ou responder,
   confirme que toda execução iniciada chegou a estado terminal e registre seu
   resultado ou limitação.
9. Termine com commit, push e árvore de trabalho limpa.

Não copie SHA, branch ou histórico de comandos para o documento. O Git já
preserva esses dados.
```

O resultado é uma recomendação ao Arquiteto, que mantém a autoridade sobre
aceite e integração.
