# M03.02.06 — FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026. **Issue M03:** [#84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84). **PR de pesquisa:** [#85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85), draft. **Branch:** `pesquisa/m03-02-governo-responsabilidade-20261014`. **Main preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Regime:** F0–F5 pesquisa, F6 e F7 **NÃO CONCLUÍDOS**; CF-NOR e CF-DEC material NÃO EDITADOS.
**Responsável funcional:** M03. **Interfaces:** M02/M04/M05/M06/M12/M14, apoio M00/M03.01/M07 e CLF quando houver rito legislativo.

## FEITO — persistentemente em branch, não na main
1. `M03-02_06_PARECER_INTERFACES_E_VIABILIDADE_DE_TRANSICAO_v0.1.md`: leitura direta de M00.01/04A (estabilidade eleitoral), M00.02/ADCT (18 itens não exaustivos), M04.01, M05.01 e M05.02, PR #62 M06.01–02 (acesso e remédios), CF/1988/ADCT/EC2/1992. Distingue fontes integradas e PRs, **e não atribui M02/M05/M06/M14 pareceres inexistentes**. Reconstitui T0–T3 de transição A/B/C, controle de nomeação/dissolução, integridade de eleições antecipadas, relação entre orçamento e financiamento local, riscos de presidências concorrentes.
2. `M03-02_06_MATRIZ_PARECERES_E_DEPENDENCIAS.csv`: **14 linhas** por interface e estado da pesquisa efetiva, comparando custos/controles nos pacotes A/B/C e indicando tarefas pendentes, sem inventar números.
3. `M03-02_06_NOTA_PRE_DELIBERACAO_F6_00_v0.1.md`: pauta de escolha P de protótipo A presidencial reformado/B parlamentar/C premier-presidencial/D continuar comparação, alternativas substantivas e suas melhores objeções, ratificação D explicitamente bloqueada.
4. **Handoffs reais em issues preexistentes**: comentário de M02 [#14](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/14), M05 [#25](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/25), M06 [#55](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/55), solicitando revisão delimitada sem alegar concordância.
5. **Abertura de demanda M14 [issue #90](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/90)** para transição, direitos, mandatos e eventual consulta popular; é abertura de pauta, **não início de pesquisa M14 nem decisão do sistema de governo**.
6. Verificação jurídica com fontes oficiais: CF art.60, art.16, ADCT art.2, EC2/1992 e TSE 1993; a consulta histórica prevista no ADCT **não institui por si novo plebiscito geral obrigatório**. Também exige análise material do limite da separação de poderes e do voto; nenhuma tese geral de validade constitucional da reforma foi ratificada.
7. Nenhum texto CF-NOR criado, sistema A/B/C ratificado ou alteração feita em `main`, `redacao/indice.csv`, `governanca/03_DECISOES.md`, ou repositório CLF.

## FONTES JURÍDICAS COMPROVADAS NESTA RODADA
- CF/1988: https://www4.planalto.gov.br/legislacao/legis-federal/constituicao e art.16/60/167§7.
- EC128/2022, art.167§7: https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc128.htm .
- STF, ADCT art.2, ADI829: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=2&abrirBase=AD .
- EC2/1992: https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc02.htm .
- TSE, plebiscito histórico: https://www.tse.jus.br/comunicacao/noticias/2013/Abril/plebiscito-sobre-forma-e-sistema-de-governo-completa-20-anos .
- Alemanha, GG63/67–69/111 https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html ; Espanha CE99/113–115/134(4) https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229 .
- Pesquisas internas citadas por arquivo, com versão na main/PR indicada no parecer. **Nenhuma base real de custos ou inferência causal acrescentada.**

## PENDENTE E NATUREZA DO BLOQUEIO
- **M02:** modelos de eleição antecipada, chefia de Estado e capacidade eleitoral; só pesquisa M00.01/04A e issue #14. Não há parecer M02.01 concluído.
- **M05/M04:** quem executa orçamento não aprovado, autoridade de dívida, tributos, fundos e encargos/consentimento territorial; M05.02 não tem base numérica harmonizada.
- **M06:** parecer próprio sobre tutela da mora e dissolução, responsabilidade e controle de chefia de Estado; PR62 trata predominantemente remédios e processo, não gabinete ou Corte nova.
- **M12:** defesa, emergência e autoridade civil única sob B/C; PR82 trata prova digital, NÃO competências executivas militares.
- **M14:** questão #90 nova, sem dossiê ainda; constitucionalidade/transição de mandatos T0–T3 e se há dever jurídico ou conveniência democrática de consultar a população. Não presumir aprovação por plebiscito de 1993.
- **Riscos centrais:** gabinete B2 investido com minoria e sem orçamento, censura construtiva sem sucessor; presidente C pode disputar legitimidade e comando; governo A pode enfrentar impasse de mandato fixo.
- **QA:** verificar na última versão o mergeability, o SHA de main, a CI e a estrutura das matrizes; testes de formato **não demonstram** validade jurídico-constitucional.
- **Não fez:** deliberação F6, proposta CF-NOR, alteração CLF ou integração na main.

## PRÓXIMA TAREFA PRIORITÁRIA — M03.02.07
**Pergunta:** sob B com B2/censura construtiva, e mantendo A/C como controles fortes, quais regras eleitorais para primeira eleição e eleição antecipada e quais regras fiscais de orçamento provisório podem ser propostas sem criar incentivos à crise?
**Insumos:** dossiês M03.02 R01–06, M00/04A, M05.01/02, M04.01, pareceres de M02 #14 / M05 #25 e M14 #90 (quando existirem).
**Saída verificável:** quadro de dois calendários de eleição antecipada versus legislatura normal, duas variantes FISC-A/FISC-B (e híbrido), matriz de 8 abusos orçamento-eleição e teste explícito de direitos, custos/fonte e estabilidade eleitoral. Depois pedir crítica M06 de G3A/B e M14 T0–T3.
**Condição de conclusão:** atores, prerrogativas, quóruns, regra aplicável no primeiro pleito, fonte fiscal, efeito e controle; sem decidir formato eleitoral global ou datas reais; nenhuma CF-NOR sem F6 material expressa.

## CONTROLE
Este registro é exclusivamente pesquisa em **PR draft #85**. O documento deve ser revisto contra a main e CI mais recentes antes de merge; merge de pesquisa não ratifica D.