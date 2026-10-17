# CF — Reconciliação técnica da main PCCP com PR #139 (26 H experimentais)

**Corte:** 17/10/2026. **Natureza:** recibo de integração **em branch draft de pesquisa**, não homologação constitucional, parecer independente ou decisão material. **PR-alvo:** [#139](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/139). Estado do texto **26 H / 0 D** neste checkout, versus **20 H** previamente disponíveis na `main`. As **seis H** adicionais pertencem apenas a M07/M08/M10/M11 e permanecem em `redacao/propostas/` com auditoria `PENDENTE`. A pilha [PR #137](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/137) contém outro conjunto de 56 H e **não** é contagem aditiva.

## Dois históricos que precisavam coexistir

| Fonte Git de entrada | SHA | Resultado preservado |
|---|---|---|
| `main` atual após Q01 | `33ce01eb8f4fd48dbef0bdcf28613903fce68472` | Políticas PCCP, [CF-DEC-006](../governanca/03_DECISOES.md) como preferência provisória P-B, pauta única, contraprovas e 19 testes documentais PCCP |
| PR #139 antes da reconciliação | `c59e6bff14b057007cd080028f34bf220cf5c451` | 26 hipóteses H, vista e painel derivados, 6 fontes adicionais, matrizes auditáveis de risco e guardas próprias M07/M08/M10/M11 |
| Base histórica comum | `e968895556a9ba5276db63e94a6eeace5182a11c` | 20 H; ponto para provar delta sem sobrescrever governança recente |

**Método técnico:** produzir commit Git com **dois pais reais**, primeiro o antigo HEAD da branch #139 e segundo o HEAD atual da `main`. A árvore resultante recebe arquivos de governança/PCCP e testes da `main`, **além** dos 19 arquivos modificados/adicionados pela branch #139 relativamente à base comum, com **uma exceção reconciliada**: o workflow combina ambas as famílias de teste (não mantém somente uma delas). Adicionar uma guarda de coexistência do corpus de 26 H com a orientação P. A integração modifica **apenas a branch draft #139**; `main` não recebe as seis hipóteses e o PR continua aberto.

**Prova de não destruição:** inspeção dos blobs na entrada mostra **20/20 fontes CF-NOR da main idênticas à branch #139**; somam-se somente as seis novas fontes `0021`, `0022`, `0023`, `0025`, `0028`, `0029`. A árvore combina **mesmo** `redacao/indice.csv`, `redacao/anteprojeto-de-trabalho.md` e `central/PAINEL_GERADO.csv` derivados de 26 H; manter coerência pelo gerador/check. Não se aplicou alteração seletiva de texto à redação jurídica neste merge.

## Testes de regressão e portas

- **G1 PARCIAL:** dados e normas materiais das fontes CF/1988, ADCT e precedentes seguem nos respectivos dossiês [lote 01](LOTE_01_M07_M08_M10_MATRIZ_R3_20261016.md), [lote 02](LOTE_02_M11_ADCT68_R3_20261016.md), [transição](M14_ADCT68_FICHA_TRANSICAO_20261016.md) e [reconciliação](RECONCILIACAO_LOTES_01_02_20261016.md). Esta operação prova união de árvores Git, não equivalência N:N de direitos.
- **G2 a verificar no HEAD de reconciliação:** validar módulo/arquivos, anteprojeto `--check`, painel `--check`, executar **as duas famílias**: 19 testes PCCP da `main`; 25 testes adicionais do lote #139; 18 testes compartilhados; e cinco novas guardas de coexistência (**67 testes previstos**, ainda não reivindicados como aprovados neste registro).
- **G3/R3 PENDENTE:** revisão jurídica humana crítica e **independente** identificável ainda ausente quanto a **CF175** (concessões, delegação e direitos de usuários), **CF225** (EIA, fauna, culturas e proteção), **CF231** (domínio federal, direitos originários, consultas, terceiro e indenização) e **ADCT68** (propriedade/titulação quilombola, terceiros, custeio e transição). Continuam `R3_PENDENTE`; nenhuma aprovação jurídica é inferida de teste textual ou merge de branch.
- **G4 NÃO ATIVADO:** não houve pedido nem resposta de aprovação constitucional do usuário. **não ratificar** `H`, via de reforma, modelo de governo, direitos, competência ou transição. A preferência provisória P-B de `CF-DEC-006` continua **P**, sem D.

**Risco de integração residual:** eventual mudança futura da `main` exigirá verificação delta e testes reais novamente. PRs empilhados #137 e outras variantes ainda exigem reconciliação por arquivo, nunca sobrescrita cega. Não converter a branch consolidada em PR não draft ou realizar merge à `main` só porque a CI concluiu.

**Critério de saída técnica desta rodada:** um histórico combinado com dois pais Git, 26 H/0 D, preservação de 20 fontes antigas, workflow com testes documentais das duas linhas e checks G2 verdes no commit atualizado — **sem** resolver os bloqueios R3 materiais. **Próximo:** priorizar revisão independente ou lacuna concreta capaz de mudar conclusão; evitar repetição de fichas Q01 e não criar outro PR experimental redundante.
