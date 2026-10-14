# M03.02.05 — Pacote de continuidade (14/10/2026)
**Issue:** [#84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84) · **PR draft:** [#85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85) · **branch:** `pesquisa/m03-02-governo-responsabilidade-20261014` · **main inicial verificada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`.
**Propriedade:** M03. **Interfaces de decisão:** M02/M04/M05/M06/M12/M14; consulta M00/M03.01/M07 e CLF T01. **Status:** F0–F5/F8 parcial, F6 NÃO decidido, F7 NÃO iniciado, F6-00–13 abertos e dependentes. **Nenhuma CF-NOR, CF-DEC material ou escolha de sistema.**

## FEITO no branch (não integrado na main)
1. `M03-02_05_PARECER_COMPARATIVO_TRES_ARQUITETURAS_v0.1.md`: exame simultâneo e crítico de (A) presidencialismo reformado com mandato executivo independente; (B) parlamentarismo racionalizado, investidura escalonada como protótipo P, censura construtiva, orçamento R1/R4 e chefia de Estado não governante; (C) semipresidencialismo premier-presidencial com Presidente eleito e gabinete politicamente responsável só à Câmara, poderes residuais taxativos. Fontes oficiais e literatura empírica, objeções máximas e portas F6.
2. `M03-02_05_MATRIZ_PACOTES_A_B_C.csv`: **19 dimensões normativas**, atores, poder fiscal, controle, eleição, emergência, direito da oposição, federação e transição; status H/P/V por campo.
3. `M03-02_05_TESTES_COMPARATIVOS_A_B_C.csv`: **12 ataques normativos** aplicados simetricamente aos três pacotes, sem atribuir nota ou probabilidade artificial.
4. `M03-02_05_PAUTA_ESCALONADA_F6.csv`: **14 gates (F6-00–13)** com dependências e matérias não deliberadas; não transformar opções de roteiro em voto constitucional. Todas abertas, bloqueadas por gate anterior ou interface pendente.
5. Este pacote FEITO/PENDENTE/PRÓXIMO, com baseline e riscos.
6. Nenhuma edição em `governanca/03_DECISOES.md`, `redacao/indice.csv` e propostas CF-NOR; nenhuma edição no CLF ou na main.

## PREFERÊNCIA ANALÍTICA P, NÃO ESCOLHA D
B permanece candidato mais rico para **prototipagem**, porque testa substituição programática sem impeachment ou eleição necessariamente imediata. Entretanto L3/P2 demonstra defeito não resolvido: premier tolerado por minoria e protegido de censura construtiva permanece sem orçamento; R1/R4 só limitam dano. A mantém legitimidade popular executiva e possibilidade de coalizões legislativas, com rigidez de mandato como custo deliberado, não inferioridade presumida. C não demonstrou vantagem incremental suficiente para compensar duas legitimações concorrentes; não eliminar sem M02/M12. **A/B/C não classificados por ranking objetivo de desempenho.**

## FONTES E AUDITORIA
- Constituição brasileira atualizada, arts. 60, 76–86 e 165–169: https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html .
- Alemanha GG arts.63/67–69/111: https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html .
- Espanha CE 99,112–115,134(4): https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229&p=20260520 .
- Portugal CRP 186–195: https://www.parlamento.pt/Legislacao/Paginas/ConstituicaoRepublicaPortuguesa.aspx .
- França Constituição 1958: https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000571356/2025-03-22 .
- International IDEA, Non-executive Presidents (2017 revision): https://www.idea.int/publications/catalogue/non-executive-presidents-parliamentary-democracies .
- International IDEA, Electing Presidents 2019: https://www.idea.int/publications/catalogue/electing-presidents-presidential-and-semi-presidential-democracies .
- International IDEA, Removal of Presidents 2022: https://www.idea.int/publications/catalogue/removal-of-presidents .
- Cheibub/Przeworski/Saiegh 2004: https://doi.org/10.1017/S0007123404000195 .
- Figueiredo/Canello/Vieira 2012: https://www.scielo.br/j/dados/a/XhTh64tqZXbNLVjzJ7MQHLS/?lang=pt .
- Elgie 2011: https://doi.org/10.1093/acprof:oso/9780199585984.001.0001 .
- CSPD database 2024: https://link.springer.com/article/10.1057/s41304-024-00499-0 .
A literatura é observacional, histórico-comparativa ou jurídico-institucional; nenhum banco próprio 2026 de duração/eficiência de governos foi adquirido. Não deduzir causalidade nem atribuir percentuais. Modelos não são textos automaticamente compatíveis com a Constituição brasileira.

## PENDENTE — blockers
1. **M02 (essencial):** eleição de Presidente em C, chefe de Estado em B, investidura e eleições extraordinárias; relação com sistema partidário, minoria e direito da oposição. Não pressupor 600 cadeiras nem outras regras do projeto histórico.
2. **M04 (essencial):** Senado ou Conselho territorial, consentimento por matéria, orçamento, controle de encargos e preservação da autonomia municipal.
3. **M05 (essencial):** despesas provisórias, direitos sociais, orçamento plurianual/prorrogado, dívida, receitas e custos reais; nenhum parecer numérico fiscal aqui.
4. **M06 (essencial):** impeachment/remoção jurídica distinta de censura, judicialização limitada, fraude de nomeação/certificação, competência de Justiça em atos presidenciais e controle da maioria.
5. **M12 (essencial para C):** ordens civis e militares concorrentes, relação chefe de Estado/premier, urgência e exceção; não validar C sem resultado.
6. **M14 (essencial):** mandato presidencial atual e legislativo, futura eleição inaugural, interinidade, atos legais, recepção e eventual plebiscito/consulta sem presumir obrigação constitucional.
7. **História/dados:** indicadores reais de coalizão, execução, custos e direitos, populismo de agenda, crises, orçamento brasileiro recente e transição. Sem isso parecer de superioridade empírica é indevido.
8. **QA:** não foi feito novo merge/rebase; verificar no HEAD final GitHub Actions, conflitos e diferenças de main. CI estrutural não comprova julgamento jurídico nem adequação constitucional.
9. **F6:** nenhuma decisão ratificada; todas portas são ferramenta de coordenação e permitem objeções. M00/CLF não devem codificar espécies de lei com base nas hipóteses M03 ainda indefinidas.

## PRÓXIMO PASSO EXECUTÁVEL — M03.02.06
**Uma tarefa:** obter/reconstruir pareceres restritos de interface M02/M05/M06/M14 (e solicitar M04/M12 quando alterar competência/chefia), confrontar os três pacotes com desenho de calendário eleitoral e continuidade fiscal em cenário de transição, preparar *nota de pauta F6-00* ao usuário com três alternativas realmente competitivas e melhores objeções. Não converter preferência P em escolha D automaticamente.
**Insumos:** cinco dossiês M03.02, matrizes anteriores, documentação nas PRs relevantes, fontes primárias e CF/1988. **Critério de saída:** para cada arquitetura identificar quem elege, investe, destitui, dissolve, promulga, dirige defesa, executa orçamento, fiscaliza, transita, qual o remédio por abuso; identificar interfaces ainda bloqueadoras. Se pendências materiais não sanadas, manter pesquisa, sem CF-NOR.

## ESTADO E RASTRO
PR #85 continua draft e a main é a única fonte integrada. O SHA main lido no início foi 2a770a8136f8ca4877e865be3e3b7745a6d4b168; alterações de coordenação independentes permanecem em main, não sobrescrever. Comprovação final de estado CI/merge por consulta GitHub específica, não por este texto prévio.