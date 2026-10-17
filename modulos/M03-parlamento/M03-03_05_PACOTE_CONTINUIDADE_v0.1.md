# M03.03 R05 — FEITO / PENDENTE / PRÓXIMO
**Corte:** 15/10/2026 · PR #100 draft, branch `pesquisa/m03-03-espaco-de-arquiteturas-20261015`; nenhuma aprovação F6/D/F7, CF-NOR, CF-DEC, CLF nem integração à main.

## FEITO
1. **Base TSE auditável** (`M03-03_05_DADOS_TSE_2022_BASE.csv`): 513 cadeiras de eleição 2022 após totalizações até 20/07/2024; 109.491.000 votos nominais+legenda em tabelas de 2023 com agrupamentos e ressalvas de temporalidade. 17 grupos, somas conferidas (inclui agregado residual sem cadeira). Fonte URLs dentro dos dois pareceres.
2. **S1 com AV sintético**, `M03-03_05_SIMULADOR_S1.js` e `M03-03_05_CENARIOS_S1_TSE_2022.csv`: oito cenários, eliminando legendas até PL/Federação Brasil, com preferências posteriores INVENTADAS e documentadas; sensibilidade do governante sob Parlamento fixo, caso de borda 81×81 de colégio mesmo com maioria preferencial final, três hipóteses de reparo de arredondamento, alternativas SF1/SF3/contramodelo SF2 e proteção fiscal federativa. Relatório `M03-03_05_PARECER_S1_COM_DADOS_TSE_v0.1.md`.
3. **C3 com simulação de composição e quórum**, `M03-03_05_SIMULADOR_C3.js` e `M03-03_05_CENARIOS_C3_COLEGIALIDADE.csv`: eleição separada por maioria em que coalizão 287 poderia indicar 5/5; D'Hondt sobre peso histórico parlamentar produz PL2/FedBrasil1/União1/PP1; possibilidade de PL+União 3/5 com 158/513; lista agregada 287×226 D'Hondt produz 3×2; sete testes de quórum e de nomeação sensível. Variantes escalonadas e escolha popular estudadas SEM dados reais de preferência. Relatório `M03-03_05_PARECER_C3_SELECAO_QUORUM_v0.1.md`.
4. **Síntese adversarial** `M03-03_05_SINTESE_COMPARATIVA_E_PORTAS_R06_v0.1.md`: controles A/B/F/I1, sete proposições validadas ou abertas, critérios de refutação e próxima rodada R06.
5. **QA matemático interno independente:** somas 513 e 109.491.000, fechamento de todas transferências, limite das cadeiras de confiança, existência de empate sob q=0,485, soma da coalizão 287 e cálculo de D'Hondt PL2/Fed1/União1/PP1. **Reexecutar scripts Node em CI próprio ainda não é passo realizado por GitHub Actions ordinária**; ela testa estrutura do repositório, não estes ensaios.

## PENDENTE
- Aferir execução formal dos dois scripts no ambiente Node e comparar saídas ao CSV gerado; a validação interna por implementação equivalente NÃO substitui um job automatizado de regressão.
- M02: desenho nacional/UF do voto ordinal e colégio, federações, ranking incompleto, votos inválidos, vacâncias, partidos sem assento, resolução de empate, voto igual. Preferências secundárias brasileiras **inexistem na apuração histórica**.
- M04: Senado e proteção territorial diante de representação legislativa/colégio especial.
- M05: custos e autorização fiscal (continuidades SF1 e SF3) com Tesouro, Siga Brasil e dados subnacionais. Nenhuma solução permite gasto sem fonte.
- M06/M07/M12: proteger controladores e oposição contra cartel 3/5, decisões/assinaturas colegiais, defesa e delegação estreita.
- M14/M02/M06: CF arts. 16, 60§4º II, rito de reforma/consulta, mandatos e transição prospectiva.
- Evidência observacional comparada e simulações com normas eleitorais reais da distribuição por UF. O M03 não dispõe de previsão empírica de estabilidade ou desempenho.

## PRÓXIMO
**R06-S:** três formas territoriais (voto nacional extra, derivação estadual, compensação de cadeiras), incluindo prova de proporção e cédula realizável; testar correção de empate nas preferências finais e auditabilidade.
**R06-C:** C3 proporcional, escalonado e colegiado politicamente censurável sob mesmos atos; examinar requisitos de independência de tribunais/auditoria e custo de quóruns alternativos, sem premiê informal.
**R06-M:** pedir pareceres autônomos dos 7 módulos de interface e organizar proposta de resolução fiscal sem falsear dados. Somente depois de auditar se S1/C3 adicionam benefício frente A/B/F considerar preferência investigativa P. **Não transformar autorização da pesquisa em aprovação de modelo D.**

## CI
Status de CI deverá ser consultado para o commit HEAD final da R05; falha breve sem logs verificada na R04 (documentada no pacote anterior) não certifica falha de conteúdo nem permite dizer que passou. Não fazer merge sem revisão.
