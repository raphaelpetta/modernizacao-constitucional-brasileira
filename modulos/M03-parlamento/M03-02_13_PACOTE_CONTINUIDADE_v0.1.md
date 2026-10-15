# M03.02.13 — FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026 · **Issue de pesquisa:** [#84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84) · **PR:** [#85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85), aberto em draft · **branch:** `pesquisa/m03-02-governo-responsabilidade-20261014` · **main preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`.
**Governança:** H/P/A/V em F0–F5/F8; **F6 e F7 NÃO concluídos**. O M03 produziu parecer **de interface**, não em nome de M14/M02; CF-DEC-006 permanece H/P e M14 #90 não se tornou decisão ratificada. Nada em CF-NOR, `governanca/03_DECISOES.md`, `redacao/`, CLF ou main.

## FEITO
1. `M03-02_13_PARECER_INTERFACE_TRANSICAO_ELEITORAL_M14_M02_v0.1.md`: aprofundamento jurídico pós-auditoria R12, com direito brasileiro do art.60, art.16, ADCT arts.2 e **3**, EC2/1992, STF **ADI981 MC / ADI1722 MC**, primeira eleição e governo em funções; comparação estrita Alemanha GG69 e Espanha CE101/Ley50/1997 art.21. **NOVIDADE MATERIAL:** o procedimento de revisão constitucional do ADCT art.3º foi especial e único, controlável por cláusula pétrea; não há rito contemporâneo paralelo simplificado livremente reutilizável. Uma nova Constituição por poder originário e EC derivada têm fundamentos distintos. Plebiscito 21/04/1993 não cria imposição geral de consulta para reformas futuras nem prova compatibilidade jurídica da reforma por si.
2. `M03-02_13_MATRIZ_12_ETAPAS_T0_T3_A_B_C.csv`: **12 fases H**, 3 arquiteturas A/B/C × T0 validação/eficácia, T1 mandatos existentes, T2 eleição inaugural e formação, T3 posse e competências. Não define datas de pleito, extinção de mandato, chefe de Estado ou sucessão por inferência. CF art16 e M14 exigem validação dos prazos e regime inaugural.
3. `M03-02_13_MATRIZ_18_PODERES_CARETAKER.csv`: **18 itens H**, 3 arquiteturas × seis competências críticas: orçamento/crédito, nova dívida, nomeações, dissolução/confiança, defesa/emergência, serviços/repartição. Nenhuma arquitetura pode conceder ordens executivas concorrentes ou dívida nova em mera interinidade por silêncio.
4. **Tensão institucional nova:** a Espanha limita atos do governo cessante e impede sua apresentação de orçamento e projetos de lei (Ley50 art21). Se transplantada isoladamente, essa regra pode colidir com o dever de custear serviços quando nova investidura demora. Alternativas H, **não aprovadas**: CT-A autorização estritamente vinculada proposta pelo cessante com dever de demonstração fiscal, ou CT-B iniciativa parlamentar restrita com apoio técnico; ambas requerem parecer M03.01/M05 e salvaguardas M06.
5. `M03-02_13_DEZ_PORTAS_DE_TRANSICAO_F6.csv`: **10 portas F6 abertas**, sobre via de reforma, 1993, primeiro pleito, mandato, caretaker, CT-A/B, nomeação, defesa, receitas e hierarquia CF versus legislação.
6. `scripts/validar_m03_02_13_transicao.py`: validador de estrutura e completude; **QA independente efetivamente executada em JavaScript**, por leitura dos 3 CSV no GitHub: PASS, 12/18/10, todos os cruzamentos A/B/C × T0–T3 e × seis poderes, IDs únicos, nenhum campo vazio, status H/ABERTA. Isso NÃO certifica constitucionalidade, eleição, dinheiro ou execução do Python pelo CI.
7. Fontes verificadas por pesquisa jurídica externa e integrações de GitHub, com URLs/escopo no parecer. Não há aprovação autônoma M14 ou M02: só trabalho preliminar M03.

## PENDENTE — perguntas que dependem de outras frentes
- **M14 #90:** parecer independente art60/ADCT3/ADI981 e 1722, distinção EC/poder originário, consequência para mandatos, T0–T3 e consulta futura, primeira posse. Não criar nova revisão unicameral ou terminar mandato vigente por hipótese.
- **M02 #14:** aplicação CF16/ADI3685 no pleito inaugural, estabilidade de reformas e direitos, eficácia das leis anteriores, eleições extraordinárias e disputa judicial.
- **M03.01 #18 / M05 #25:** CT-A versus CT-B quando governo em funções está restringido e a LOA não foi aprovada; iniciativa, autorização fiscal, direitos exigíveis, serviço de dívida, caixa e nova dívida sem rito de emergência genérico.
- **M06 #55:** nomeação vinculada G3A/G3B (alternativas não decididas), direitos, controle de dissolução, tutela de atos de interinidade e de eleições sem tribunal decidir quem governa.
- **M12:** cadeia única de comando militar/emergência com presidente de voto direto C e premiê, controle dos atos de exceção.
- **M04/M07:** repasses de receita constitucional, contratos, cargos, capacidade administrativa e dever de serviço sem disputa de competência.
- **Não feito:** escolha de instrumento jurídico para adoção, data real, duração constitucional do governo em funções, texto de CF-NOR, análise conclusiva de art60 e decisão A/B/C. Não presumir obrigação de novo plebiscito nem possibilidade jurídica automática de alterar sistema por EC.
- **QA final:** verificar HEAD da branch, CI, mergeabilidade/divergência antes da próxima rodada. CI verde não valida o parecer jurídico.

## PRÓXIMO — R14 ou trabalho direcionado das interfaces
Priorizar respostas **efetivas e independentes** M14 e M02 sobre art60/pleito inaugural e de M03.01/M05 sobre CT-A/CT-B. A pesquisa M03 já definiu o problema jurídico com fontes; repetir muitos cenários fictícios sem respostas das frentes gera pouco valor. Um parecer M14 poderá concordar, corrigir ou refutar o dossiê, e a divergência deve ser incorporada. Se revisão indisponível, marcar A/V e **não criar CF-NOR nem D**. A preferência B continua P de prototipagem, A concorrente real, C exige poderes e comando sem dupla autoridade.

## FONTES
- CF art60/16: https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm
- ADCT3 STF ADI981/ADI1722: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=3&abrirBase=AD
- ADCT2 STF: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=2&abrirBase=AD
- EC2/1992: https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc02.htm
- Art16 anotado TSE: https://www.tse.jus.br/legislacao/codigo-eleitoral/constituicao-federal/constituicao-da-republica-federativa-do-brasil
- Alemanha GG69: https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html
- Espanha CE101 e Ley50 art21: https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229 ; https://www.boe.es/buscar/act.php?id=BOE-A-1997-25336 .
**Rastro:** tudo em PR draft #85 da branch de pesquisa. Merge documental, se vier, não ratifica novo Governo nem transição constitucional.