# Controle de nomes de ciclos e reserva de identificadores

**ID:** CF-GOV-015 · **Data base:** 14/10/2026 · **Estado:** procedimento de coordenação.  
**Regra geral:** nenhum subciclo Mxx.yy ou identificador `CF-NOR-####` deve ser declarado livre **sem conferir simultaneamente** `redacao/indice.csv` na `main`, PRs/branches de redação abertos e este registro. A reserva deve ser publicada em issue/registro versionado e vinculada a função e responsável funcional. **Uma reserva não é norma, artigo definitivo nem decisão D.**

## 1. Unicidade e atribuição

1. O ID é **estável após integração**; não renumerar automaticamente porque outra matéria ficou à frente na ordem. O índice possui campo `ordem` próprio. Números não são artigos constitucionais.
2. **Reserva de PR:** qualquer nova ficha de redação de direitos registra seu ID proposto no corpo do PR e na issue-mãe; antes do merge revisar novamente `main` e PRs. Não basta atualizar a própria branch.
3. **Conflito material:** dois textos diferentes com mesmo ID constituem bloqueio; **nunca resolver com a escolha arbitrária do último commit**. Preservar ambos no histórico e criar nova branch do último SHA com IDs distintos.
4. Atribuição de subciclos: uma frente de pesquisa e outra de redação podem usar códigos diferentes; se a pesquisa e redação falarem de mesmo conteúdo, explicitar `ORIGEM` e `VERSAO` sem assumir equivalência.
5. Os IDs `CF-DEC-####` seguem `03_DECISOES.md` e não podem ser convertidos de status por PR de mero texto.
6. Ferramentas automatizadas verificam unicidade **dentro do índice**, mas **não** reivindicações externas em PRs até que exista validador específico; a leitura das PRs é obrigatória.

## 2. Fotografia de reservas existentes

**Main lida durante início da coordenação, SHA `c82d41b8313c79a7c7b7d93b3a69269eb86a99c3`:**

| Faixa/ID | Uso existente | Situação |
|---|---|---|
| 0001–0002 | Financiamento, encargos M04/M05 | Já na `main` H |
| 0003–0007 | Regime geral M01 | Já na `main` H |
| 0008–0011 | Igualdade M01.09 | Já na `main` H |
| 0012–0017 | Dignidade, vida, integridade, consentimento e pesquisa M01.10 | Já na `main` H |
| 0018–0020 | Capacidade, diretivas e medidas involuntárias M01.11 | Já na `main` H, verificação dinâmica obrigatória |
| 0012–0013 no PR #45 | **Colisão**: privacidade e proteção de dados propostos sob IDs já utilizados na `main` | **INVALIDADO PARA MERGE**; nunca reaproveitar os números nesta proposta |

**Próximo `CF-NOR` não é automaticamente 0021:** verificar outros PRs, issues de reserva e commit atual. É aceitável usar IDs não contíguos, se justificados e documentados, para reduzir concorrência. O campo `ordem` organiza apresentação editorial independentemente do ID.

## 3. Subciclos ocupados e propostos

| Chave | Escopo | Controle |
|---|---|---|
| M01.01–M01.09 | Pesquisa acumulada no PR #22 | Histórico de pesquisa; M01.09 também foi usado em piloto de igualdade na main, portanto distinguir `M01.09-PESQUISA` de `M01.09-REDACAO` no arquivo |
| M01.10 | Dignidade, vida e integridade | Issue #43, material H integrado |
| M01.11 | Capacidade/diretivas/medidas involuntárias | Issue #47, material H em andamento/integrado conforme SHA |
| **M01.12** | Liberdades civis: expressão, religião/consciência, reunião, associação, circulação, informação | **Reserva funcional proposta por este projeto de coordenação**, criar issue dedicada antes de pesquisa |
| **M06.01** | Tutela judicial, remédios, garantias do processo e controle constitucional | Reserva funcional proposta, criar issue |
| **M09.01** | Direitos sociais e do trabalho, sua materialidade e financiamento | Reserva funcional proposta, criar issue |
| **M02.01** | Integridade eleitoral | Já existe issue #14, não reabrir sob novo nome |
| **M03.01, M04.01, M05.01, M05.02** | Frentes em pesquisa | Issues #18, #21, #25, #29: não duplicar |

**Gatilho:** a abertura de uma issue com título e escopo definitivo consolida uma reserva; se outra issue já existir na hora, reconciliar e não duplicar.

## 4. Antes de criar qualquer norma ou ciclo

- [ ] Confirmar SHA atual e índice na `main`.
- [ ] Consultar `governanca/13_QUADRO_DE_COORDENACAO.md` e este registro.
- [ ] Consultar PRs e issues abertos, não só arquivos da main.
- [ ] Registrar vínculo de ID, matéria, issue/PR, módulo e dependências.
- [ ] Conferir status H/P/D e autoridade para alterar.
- [ ] No fechamento, atualizar **Feito / Pendente / Próximo** e registrar eventual alteração de reserva.

Se o estado do GitHub mudar antes da criação do arquivo ou merge, repetir o preflight. O protocolo **reduz**, mas não elimina atomicamente, corridas entre branches independentes: neste caso prevalece a verificação de conflitos no momento de integrar.

## Adendo de reserva — 14/10/2026

A [issue #57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57) reservou formalmente **CF-NOR-0030** para privacidade e **CF-NOR-0031** para dados pessoais; textos H foram propostos no [PR #59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59), **ainda draft e não integrados à main** na fotografia `d346f71140656263216cdeb137a775e2b3fc73a9`. As ordens editoriais candidatas são 0210/0220, independentes dos IDs. 

**Não disponíveis para outro PR enquanto a issue #57 estiver ativa:** 0030, 0031. **Não liberados para privacidade/dados:** 0012 e 0013, ocupados por dignidade e vida na main. Consultar PRs e índice novamente antes de integrar; a reserva documental não é travamento atômico do GitHub.

Subciclos iniciados no tracker: **M01.12 [#54](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/54)**, **M06.01 [#55](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/55)**, **M09.01 [#56](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/56)**, **M01.13 [#57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57)**. Isto reserva escopo, não aprova texto nem conclui pesquisa.

## Adendo de reserva e colisão resolvida em 14/10/2026

**M06.02 = [issue #65](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/65)**: dossiê de remédios HC/MS/MI/HD/ação popular no PR62. **M09.02 = [issue #66](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/66)**: art7 I–XXXIV/PU e arts8–11 no PR63. Ambos pesquisa sem CF-NOR nova.

**Correção de reserva M01 feita após identificar colisão real:**
- `M01.12` = [issue #49](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/49), já anteriormente reservada para internações e tratamentos involuntários, rede comunitária/saúde mental;
- `M01.13` = [issue #57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57), privacidade/dados, PR59 H 0030/0031;
- `M01.14` = [issue #54](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/54), **renomeada** de M01.12 para liberdades de expressão/religião/reunião/associação. O conteúdo da issue e seu histórico foram preservados.
A entrada histórica acima que aponta `M01.12` como código de liberdades civis ficou **superada apenas nesse aspecto**. Não usar simultaneamente o mesmo código em dois estudos; links por número de issue permanecem estáveis.

**Próximos códigos M06.03, M09.03, M09.04 são apenas sugestões, ainda NÃO reservas**, até novo preflight em main/issues/PRs. A política de source-of-truth de `redacao/indice.csv` e controle de IDs CF-NOR continua inalterada.

## Reserva adicional — M09.03 e interface M06/privacidade, 14/10/2026

**M09.03** oficialmente vinculada à [issue #68](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/68), dossiê e CSVs no [PR #63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63); **nenhuma CF-NOR reservada/criada**. Não reutilizar M09.03 para capítulo previdenciário ou pisos sem exame da issue. **M06.02** incluiu parecer de interface com privacidade no [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62); **não** foi ocupado o código M06.03 (tutela coletiva futura permanece sugestão pendente, não reserva). CF-NOR 0030/0031 seguem reservadas no PR59 H/draft, jamais afirmar integração à main.


## Reserva de subciclo M12.01 — 14/10/2026
A [issue #80](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/80) registra **M12.01 — investigação digital e Tema 977**, com estudo independente no [PR #82](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/82), draft. M12 abrange polícias/investigação segundo `catalogo/MODULOS.csv`. A reserva é de **subciclo**, não de ficha `CF-NOR` nem decisão constitucional. **FEITO:** designação e parecer; **PENDENTE:** interoperabilidade M01/M06/M07; **PRÓXIMO:** revisão conjunta sem ocupar novos IDs até deliberação.
