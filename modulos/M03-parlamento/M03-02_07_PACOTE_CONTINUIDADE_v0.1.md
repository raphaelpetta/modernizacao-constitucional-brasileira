# M03.02.07 — FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026; **issue:** [#84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84); **PR:** [#85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85) (draft); **branch:** pesquisa/m03-02-governo-responsabilidade-20261014; **main preflight:** 2a770a8136f8ca4877e865be3e3b7745a6d4b168. **Propriedade:** M03; M02/M04/M05/M06/M07/M12/M14 recebem interfaces. **Estado:** F0–F5/F8 investigação, F6 NÃO deliberado, F7 NÃO iniciado, sem CF-NOR ou CF-DEC material, sem importação do Brasil alternativo.

## FEITO — apenas em PR draft, não main
1. Estudo `M03-02_07_ELEICOES_EXTRAORDINARIAS_E_ORCAMENTO_PROVISORIO_v0.1.md`: dois relógios independentes — eleição extraordinária e autorização fiscal durante o impasse. Direito vigente CF art.16 e art.167 §7º; Alemanha GG39, 63/67/68, 110/111; Espanha CE99/115/133/134(4) e Lei 47/2003 art.38; soft law Comissão de Veneza 2024–25. **Não transplantar 60 dias da Alemanha, 2 meses da Espanha ou 25% de crédito alemão como limites brasileiros aprovados.** O 25% alemão é crédito excepcional condicionado, não teto universal de despesa pública.
2. `M03-02_07_CALENDARIOS_ELEITORAIS.csv`: 15 marcos sequenciais em **CAL-N normal 5**, **CAL-X extraordinário 6**, **CAL-T inaugural 4**. Prazos/competências da Constituição proposta continuam H/A. Nota: normal + extraordinário são os **dois** calendários testados; inaugural é cenário separado de transição M14.
3. `M03-02_07_MATRIZ_CONTINUIDADE_FISCAL.csv`: **FISC-A** autorização taxativa, **FISC-B** prorrogação limitada, **FISC-C** híbrido; cada opção define recepção/receitas/despesas/programas expirados/crédito/fiscalização, mas **não** fornece custos reais.
4. `M03-02_07_OITO_ATAQUES_ELEICAO_ORCAMENTO.csv`: **8** cenários de governo que manipula circunscrições ou orçamento; oposição que bloqueia sem sucessor; programa expirado prorrogado; decisão judicial protetora de direitos durante campanha; emergência sem orçamento; chefe de Estado que dissolve apesar de censura/posse válida.
5. `scripts/validar_m03_02_07_matrizes.py`: validador reproduzível de quantidade/IDs/colunas e continuidade de fases. **Conferência independente JS realizada** lendo os 3 CSV diretamente do GitHub: PASS, 15 marcos (5+6+4), 3 modelos fiscais, 8 ataques, campos completos, IDs únicos. Isso **não** demonstra que GitHub Actions executou o Python nem prova direito ou custo.
6. Achado P: **ELE-1** blindagem da versão eleitoral válida depois de convocação (preservando anterioridade e exceções de direitos judicialmente exigíveis) merece prototipagem; **ELE-2** quarentena de reforma pela própria legislatura merece investigação contra manipulação antecipatória, mas pode congelar reformas legítimas; ELE-3 reserva reforçada idem. **FISC-C** candidato de stress test apenas, não superioridade demonstrada; FISC-A/B continuam alternativas sérias.
7. Não houve alteração de `redacao/`, `governanca/03_DECISOES.md`, repositório CLF ou main.

## FONTES — tipologia sem confusão
- Brasil: CF art.16, TSE e STF https://www.tse.jus.br/legislacao/codigo-eleitoral/constituicao-federal/constituicao-da-republica-federativa-do-brasil ; https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=16&abrirBase=CF .
- Brasil: EC128/2022 e art.167 §7º https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc128.htm .
- Alemanha: art.39 https://www.gesetze-im-internet.de/gg/art_39.html ; art.111 https://www.gesetze-im-internet.de/gg/art_111.html .
- Espanha: CE99/115/134(4) https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229&p=20260520&tn=1 ; legislação de orçamento https://www.boe.es/buscar/act.php?id=BOE-A-2003-21614 .
- Comissão de Veneza 2024 (declaração de estabilidade) https://www.coe.int/en/web/venice-commission/-/cdl-ad-2024-027-e e Code 2025 https://edoc.coe.int/en/elections/12110-code-of-good-practice-in-electoral-matters.html . Persuasão comparada, não direito brasileiro.
- Pesquisa interna existente: M00.01/04A, M04.01, M05.01/02 e anteriores M03.02.01–06. Sem base de dados fiscais harmonizada ou inferência de causalidade.

## PENDENTE / BLOQUEADORES REAIS
- **M02:** regras de antecipação da eleição e exceção de direitos, estabilidade do sistema eleitoral, método de certificação e quem convoca; a issue #14 ainda não equivale a parecer próprio concluído.
- **M05/M04:** definir precisamente receitas e despesas autorizadas, caixa, crédito, dívida, programas expirados, direitos sociais e repartição interfederativa, repasses e segunda Câmara; a pesquisa fiscal incorporada não equivale a parecer sobre governo em crise.
- **M06:** controle urgente de versão eleitoral, impugnação de dissolução e de gastos ilegais, tutela da nomeação G3A/B e fraude da certificação; nenhuma Corte constitucional nova aprovada.
- **M14:** issue #90, transição inaugural e preservação de mandatos; calendários não possuem dia/ano jurídico nacional escolhido.
- **M07/M12:** emergência/epidemia e gestão interina, continuidade dos serviços e comando legítimo da segurança; não criar poder extraordinário aberto.
- **Risco central irresoluto:** titular de governo minoritário pode sobreviver enquanto não se forma maioria para orçamento e censura; ELE-1 e FISC-A/B/C reduzem incentivos abusivos, **NÃO constroem maioria política**.
- **QA posterior:** ler main e HEAD do PR, CI real GitHub Actions, conflitos e versão das fontes; não inferir aprovação jurídica da CI.

## PRÓXIMO — M03.02.08, tarefa única executável
Aplicar ELE-1/ELE-2 e FISC-A/B/C **às legislaturas L2 e L3**, com condições observáveis de dois anos sem orçamento, continuidade de escola/hospital/repasses e dívida, decisão judicial de direito eleitoral no curso do pleito, e eleição extraordinária iniciada só após crise de formação (não derrota de orçamento). Conferir alternativas pelo prisma A presidencial e C premier-presidencial. Recolher críticas M02/M05/M06/M14 às opções exatas, corrigir efeitos de perda de direitos e manter F6-00 sem decisão final. **Saída:** matriz de casos, controles de competência, estimativa de custo somente se houver dados verificáveis, nota de preferência P/D bloqueada, handoff e QA. Sem CF-NOR e sem escolher artigo, prazo ou sistema por implicação.

## RASTRO DE INTEGRAÇÃO
Arquivos somente em branch PR #85, sem merge. Estado de CI e diff após último commit devem ser registrados posteriormente no relatório desta rodada ou comentário de PR. Merge documental não é ratificação.