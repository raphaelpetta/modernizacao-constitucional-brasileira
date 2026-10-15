# Produto constitucional de trabalho — como ler e auditar a minuta

**Corte:** 15/10/2026. **Status jurídico-político:** todas as fontes CF-NOR deste recorte são H (experimentais), nenhuma se torna decisão material D por estar num arquivo, branch ou PR. **Referência integrada:** main `fae101cdfa5a3af80182e9e56e8debb4ddfcaec9` com **20 H**. **Pilha experimental separada:** [PR #124](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/124), HEAD `b10a3e72f93a352b90003529283c51685a863dfb`, com **54 H** nos 15 módulos. Essas são **duas versões Git distintas**, não se somam (a pilha contém as 20 da main ancestral); há outras propostas independentes, como [PR #59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59) e [PR #107](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/107), **que não devem ser presumidas contidas na pilha**.

## Ler o que já está integrado

- **[Anteprojeto de trabalho na main](../redacao/anteprojeto-de-trabalho.md):** texto corrido das **20 H**, não Constituição integral, vigente ou ratificada.
- **[Índice canônico da main](../redacao/indice.csv):** status, ordem e fonte das normas que aparecem na vista integrada.
- **[Fontes canônicas](../redacao/propostas/):** fichas CF-NOR com texto normativo, evidências, objeções e pendências; a fonte não deve ser duplicada na central.
- **[Mapa funcional comparado](../catalogo/COBERTURA_FUNCIONAL.csv):** distingue **H na main**, **H na pilha PR #124** e **34 H adicionais ainda pendentes**, em cada M00–M14. O mapa é **inventário documental não exaustivo**, não percentagem de cobertura da Constituição.
- **[Protocolo global de ganho marginal](../governanca/19_POLITICA_GANHO_MARGINAL_GLOBAL.md):** próxima pesquisa deve demonstrar valor adicional relativo às alternativas; evitar sobreprodução e não sacrificar garantias.

## Ler o que está apenas em rascunho

A [ponta da pilha #124](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/redacao/cfcc018-m04-m07-m13-cobertura-20261015/redacao/anteprojeto-de-trabalho.md) compila **54 H**. Essa URL usa a *branch* explicitamente, para evitar parecer que todas as 54 estão na main. Os PRs #105–#124 foram empilhados segundo [o grafo de dependências](../central/02_PLANO_INTEGRACAO_PRS.md). Não escolher parlamentarismo/presidencialismo, tribunal constitucional, regime de voto ou conteúdo financeiro pela simples presença de hipótese na pilha.

**Fonte de verdade:** `redacao/indice.csv` + `redacao/propostas/CF-NOR-####.md` da **mesma revisão**. A vista `anteprojeto-de-trabalho.md` é gerada por `python scripts/gerar_anteprojeto.py` e verificada por `python scripts/gerar_anteprojeto.py --check`, não deve ser editada como fonte independente.

## Portas de qualidade — não confundir

1. **Estrutura documental:** validade de índices e links, unicidade de IDs/ordens, correspondência fonte–vista, testes de estrutura.
2. **Qualidade jurídico-constitucional:** preservar direitos CF/1988 e ADCT, competência, titular, exceções, direitos de minorias, instrumentos de tutela, jurisprudência e transição; não inferir equivalência pelo número de H.
3. **CI executada:** o workflow deve de fato provisionar runner e executar comandos. Em 15/10/2026, [run main 38790002189](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/38790002189) falhou **em duas tentativas sem steps ou runner**, inclusive após reexecução aceita; resultado **não significa que os testes Python passaram ou falharam**. Incidente [#120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120).
4. **Deliberação:** estado H/P/A/V **não equivale** a D. A decisão material requer aprovação específica e rastreável, independente da integração documental.

## Próxima ação de maior ganho marginal

A principal dívida de trabalho é **transformar proposta dispersa em texto validado com garantias explícitas**, começando por diagnosticar a CI e reconciliar scripts e controles remanescentes dos PRs [#101](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/101) e [#104](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/104) com a main já atualizada pela CF-GOV-019 e CF-CC-019. A partir daí, revisar criticamente as 34 H adicionais antes de eventual integração experimental.

**FEITO:** mapa separado main × pilha, ponto de entrada único, regras de leitura. **PENDENTE:** execução real do CI, revisão material R3, integração jurídica, variante A/B/C. **PRÓXIMO:** restaurar testes com provas, não alterar workflows por tentativa e erro. **Interface CLF:** soberania de cada repositório preservada.
