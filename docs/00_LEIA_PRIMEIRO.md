# Guia de implantação e uso

**Versão:** 0.1 · **Repositório:** https://github.com/raphaelpetta/modernizacao-constitucional-brasileira

## Para iniciar
1. Leia `governanca/04_ESTADO_ATUAL.md`, `governanca/03_DECISOES.md`, `governanca/02_METODOLOGIA.md` e `governanca/06_CONTINUIDADE_VERSIONAMENTO.md`.
2. Consulte `catalogo/MODULOS.csv` e `governanca/05_DEPENDENCIAS.md` para delimitar o tema.
3. Mantenha um **Projeto ChatGPT constitucional**, distinto do projeto legislativo; use `chatgpt/INSTRUCOES_PROJETO.md` nas instruções desse Projeto.
4. Em cada novo chat, solicite leitura do commit atual da `main` e dos dossiês pertinentes. Nunca assuma que um chat atualizou arquivos de outro.
5. Encerre sessões com `modelos/PACOTE_CONTINUIDADE.md` e registre no Git as conclusões persistentes, depois da revisão.

## Regras de decisão
O anteprojeto histórico e o guia-mestre são fontes de referência, não constituição proposta obrigatória. `D/P/H/A/V` distinguem diretriz ratificada, preferência, hipótese, aberto e verificação pendente. Apenas deliberação efetivamente confirmada eleva uma escolha substantiva a D. Mudança de governança operacional e mudança do conteúdo constitucional são fatos diferentes.

## Fluxo do GitHub
`main` = versão documental integrada; branches/pull requests = propostas em avaliação. Primeiro pesquisar e comparar; depois produzir dossiê/decisões/minuta. Reconciliar conflitos e atualizar `04_ESTADO_ATUAL.md` após integração. Se houver arquivo antigo carregado como fonte do Projeto ChatGPT, conferir sempre o remoto atualizado.

## Redação integrada e recuperação idêntica

A partir de M00.03, a redação exploratória reside em `redacao/propostas/CF-NOR-####.md` (fonte única) e `redacao/indice.csv` (posição, tipo, status). A leitura integrada fica em `redacao/anteprojeto-de-trabalho.md`, gerado por `python scripts/gerar_anteprojeto.py` e conferido em CI com `--check`. **Não editar a vista integrada manualmente.** Cada módulo deve usar [protocolo de técnica redacional](../governanca/11_TECNICA_DE_REDACAO_E_INTEGRACAO.md), preservar garantias e distinguir hipótese H de decisão D. Texto recuperado de chat anterior, arquivo antigo do Projeto e GitHub **não se sincronizam automaticamente**; conferir SHA da `main` antes de usar ou redigir qualquer trecho.

## Primeiros ciclos
M00.01: reserva constitucional, fontes, hierarquia e competências; M01.01: teoria geral de direitos e salvaguardas; rodada estrutural M03–M05 para mapear Parlamento, federação, tributos e capacidade fiscal; revisão transversal M06 e M14 para justiça e transição. Ver `governanca/08_ROTEIRO_INICIAL.md`.

## Referências antigas
O anteprojeto v0.1 contém 174 artigos permanentes, 13 títulos e 18 artigos de disposições transitórias; a numeração antiga não delimita a futura redação. Arquivos estão em `referencias/`. Para consulta exata do PDF, conservar também o original binário do pacote inicial, pois no GitHub foi incluída a extração textual.

## Verificação técnica

Executar `python scripts/validar_repositorio.py` antes da integração, além da revisão substantiva humana. O GitHub Actions confere estrutura em PRs; falha de estrutura bloqueia a conclusão técnica do ciclo. Referências normativas, jurisprudência e qualidade constitucional exigem verificação própria. Consultar `governanca/10_PROVENIENCIA_E_IDS.md` para campos mínimos de fonte, norma, decisão e proposta.
