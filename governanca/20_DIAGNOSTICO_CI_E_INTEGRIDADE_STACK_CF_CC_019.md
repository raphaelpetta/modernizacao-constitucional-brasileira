# CF-CC-019 — Diagnóstico verificável da CI e conferência do stack

**Estado:** QA documental e triagem de infraestrutura; **NÃO** certifica Python ou validade jurídica. **Corte:** 15/10/2026. **Base main:** `7c3bd80470899a09e31f25a6a3a47d7c9cca669c`. **PRs afetados:** [#101](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/101), [#104](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/104), [#124](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/124), incident [#120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120).

## Evidência reprodutível: job conclui sem runner provisionado

| Origem | GitHub Actions run | Conclusão | Runner ID | Steps | Duração |
|---|---:|---|---:|---:|---:|
| PR #101 | [38716772220](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/38716772220) | failure | 0 | 0 | 2s |
| PR #104 | [38729692638](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/38729692638) | failure | 0 | 0 | 2s |
| **main** após CF-GOV-019 | [38771376862](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/38771376862) | failure | 0 | 0 | 2s |
| PR #124 (54 H) | [38786259984](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/38786259984) | failure | 0 | 0 | 2s |

**Fonte da constatação:** REST GitHub `/repos/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/{run_id}/jobs`, consultado no mesmo turno. Todos têm `runner_id:0`, `runner_name:""`, `steps:[]`, `labels:["ubuntu-latest"]` e duração de 2 s. **Inferência limitada:** nenhum comando do job foi registrado como executado; falha ocorreu **antes do provisionamento identificável do runner/execução de steps**. **Não é possível inferir causa raiz**: políticas de Actions, cota, faturamento, acesso à imagem de runner, suspensão/permissão, problema da plataforma ou outro erro pré-job exigem anotações/logs e configurações que não estão acessíveis. Não afirmar que existe uma causa específica.

O check-run do PR #124, ID `116598907942`, registra **duas anotações** de erro, mas a superfície de acesso disponível rejeita o endpoint `/check-runs/116598907942/annotations` e o log do job retorna `404 BlobNotFound`. A leitura da UI ou endpoint autorizado das anotações é a próxima fonte de evidência; **não** editar às cegas `.github/workflows/validar-estrutura.yml`.

## QA substantiva do gerador reproduzida de forma independente

- Conferidas **54/54 fontes `redacao/propostas/CF-NOR-####.md`** da branch `redacao/cfcc018-m04-m07-m13-cobertura-20261015`, de acordo com `redacao/indice.csv` ordenado e as 54 seções de `redacao/anteprojeto-de-trabalho.md`.
- Leitura individual remota em **três grupos de 18 fontes**; todos os blocos correspondem **exatamente** à seção esperada: `## ID — tema [status; tipo]`, eventual regra geral referida e texto entre `NORMA-INICIO`/`NORMA-FIM` normalizado somente pelas regras do gerador (`trim` dos limites). **Resultado: 54 conferidas; 0 divergências textuais por seção**.
- Verificação de cabeçalhos/índice/54 IDs e ordens distintos, 15 módulos e estado H ocorreu na CF-CC-018; esta rodada foi além ao ler **todas as fontes antigas**, não somente as três novas.
- A verificação das seções e a leitura do [gerador](../scripts/gerar_anteprojeto.py) em Python fundamentam a conferência, **mas não significam que o script Python tenha sido executado**. O validador completo `scripts/validar_repositorio.py` e as suites unittest tampouco foram executados. O ambiente externo não permitiu clonar o GitHub para Python diretamente.
- Arquivos do PR #101/#104 foram comparados por patch/conteúdo com a main: **#101 tem conflito por alterar arquivos de governança já modificados por CF-GOV-019**; **#104 é mesclável no servidor**, mas seus scripts, workflow e painéis não foram testados localmente e, portanto, não são importados nessa seleção documental.

## Checklist de diagnóstico pendente

1. Abrir [Actions run 38771376862](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/38771376862) na interface GitHub com permissão adequada. Ler as **duas anotações do check-run** e eventual banner de fila/conta/permissões; registrar transcrição e imagem/URL, sem divulgar segredos.
2. Verificar **Settings → Actions** e disponibilidade de runner `ubuntu-latest`, políticas da organização/repositório e limites da conta com permissão do administrador. Não concluir que falta de execução é causada por conteúdo das normas.
3. Resolver causa **comprovada**, reexecutar run e observar steps do `checkout` e `setup-python`. Se obtiver job em runner, confirmar Python 3.11 e os quatro comandos do workflow em `main` e, depois, na branch com 54 H.
4. Se CI permanecer indisponível, executar os mesmos comandos num checkout íntegro com hash e logs, e registrar limitação; isso fornece QA alternativa, mas **não** declara CI oficial verde.
5. Somente após validação técnica e auditoria jurídico-material R3, considerar integração experimental da pilha; nunca mudar H para D por um teste.

## Ganho marginal

**FEITO:** isolada condição pré-execução em PRs e `main`, descartada alegação infundada de falha demonstrada de Python, confirmada concordância de **54/54** seções; plano de reconciliação seletiva. **PENDENTE:** causa raiz/CI real e QA integral; auditoria de não regressão constitucional material. **PRÓXIMO:** recuperar anotações por interface autorizada e executar testes; priorizar conclusão dessa dependência ao invés de criar outras CF-NOR H.

## Reexecução controlada CF-CC-020 — 15/10/2026

Na `main` `fae101cdfa5a3af80182e9e56e8debb4ddfcaec9`, o [run 38790002189](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/38790002189) teve **primeira tentativa `failure`** antes de steps. A API de reexecução de jobs malsucedidos aceitou o pedido; a **tentativa 2 foi efetivamente concluída também em `failure`**, com novo job `116615081992`, `runner_id=0` e `steps=[]`. A reexecução **não corrigiu** a indisponibilidade e confirma persistência sob nova tentativa, não revela causa raiz ou qual das duas anotações aponta a falha. Workflow não alterado por tentativa e erro.

**Em paralelo:** [catálogo comparativo de cobertura](../catalogo/COBERTURA_FUNCIONAL.csv) é reconstruído da `main` (**20 H**) e do [PR #124](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/124) (**54 H**), não soma as duas fontes nem representa as branches paralelas #59/#107. Não declarar script Python verificado só porque as fichas normativas foram lidas remotamente. **PENDENTE prioritário:** acesso às anotações/permissões Actions e validação real dos scripts restantes dos PRs #101/#104.
