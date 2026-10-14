# M03.02 — Rodada 04: FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026. **Issue:** [#84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84). **PR:** [#85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85) (draft). **Main de entrada:** \`2a770a8136f8ca4877e865be3e3b7745a6d4b168\`; **branch:** \`pesquisa/m03-02-governo-responsabilidade-20261014\`. **Responsável:** M03, interfaces M00/M02/M04/M05/M06/M07/M12/M14. **Estado:** pesquisa H/P/A/V, F6 não deliberado, F7 não iniciado. Não existe decisão D ou CF-NOR nesta rodada.

## FEITO (somente branch/PR)
1. Dossiê \`M03-02_04_TESTES_INCENTIVOS_E_DISSOLUCAO_ESTRATEGICA_v0.1.md\`: G1 governo fabrica rejeição orçamentária, G2 oposição bloqueia sem maioria sucessora, G3 chefe de Estado bloqueia nomeação de sucessor validamente escolhido; integra cenários L2/L3 auditados na rodada 03, alternativas R1–R4, G3A/G3B/G3C, contramodelo presidencial A e parecer de risco de dissolução.
2. \`M03-02_04_MATRIZ_15_TESTES_DE_CAPTURA.csv\`: 15 registros com ator, gatilho, incentivo adversarial, remédio, competência, prazos **pendentes** e objeções. QA de estrutura via leitura dos arquivos GitHub: **15 linhas**, **13 campos**, IDs únicos; G1 quatro, G2 quatro, G3 sete testes, consistente.
3. \`M03-02_04_PORTAS_DE_DELIBERACAO_F6.csv\`: **12 pontos de opção material EM_ABERTO**, cobrindo forma de governo, investidura, censura, confiança, orçamento, dissolução, governo minoritário, nomeação do chefe de Estado, federalismo, fiscalidade, controle judicial e transição. QA documental via leitura: 12 IDs únicos, 7 campos, 12 status EM_ABERTO.
4. **Conclusões H**: mera contagem de orçamentos rejeitados é passível de fabricação tanto pelo Governo como pela oposição; R1 conciliação + R4 custeio fiscal restrito preservam serviços e transparência, mas não são garantia de maioria; R2 pode desconstituir censura construtiva; R3 automático por bloqueio fiscal é vulnerável; nomeação de sucessor pela chefia de Estado deve ter mecanismo vinculante e contingência contra mora, a definir (G3A/G3B).
5. **Nenhuma** alteração em \`redacao/\`, \`CF-NOR\`, \`governanca/03_DECISOES.md\` ou repositório CLF. Pesquisa não equivale a texto da Constituição.

## FONTES PRIMÁRIAS EFETIVAMENTE REVISADAS
- Alemanha Grundgesetz, arts. 63, 67, 68, 111: https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html ; https://www.gesetze-im-internet.de/gg/art_111.html .
- Tribunal Constitucional Federal alemão, **2 BvE 4/05 / 7/05**, decisão 25/08/2005, exame da dissolução por confiança com requisitos finalísticos e fiscalização judicial limitada: https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/2005/08/es20050825_2bve000405en.html . A decisão manteve a dissolução; não proibiu genericamente votos estratégicos.
- Espanha, Constituição BOE vigente conforme página de 20/05/2026, arts. 62, 64, 99, 113–115, 134(4): https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229&p=20260520&tn=1 .
- Bélgica, Constituição traduzida oficialmente em **2021**, arts. 46/96, apenas fonte comparativa historicamente identificada e dependente de reconferência de atualizações: https://www.dekamer.be/kvvcr/pdf_sections/publications/constitution/grondwetuk.pdf .
- Reino Unido, Dissolution and Calling of Parliament Act 2022, ss. 1–4, contraste sobre prerrogativa e não-justiciabilidade: https://www.legislation.gov.uk/ukpga/2022/11 .
Os textos são fontes jurídicas, não dataset do desempenho institucional. Não se inferem probabilidades reais nem classificação moral de votos.

## PENDENTE / LIMITES
- M02: partidos/eleições antecipadas, direito da oposição e limites a mudanças oportunistas; validar legitimidade de procedimentos de investidura.
- M04/M05: competência de segunda Câmara e regime financeiro, obrigações de Estados/municípios, continuidade de direitos e fiscalidade em orçamento não aprovado; custo de prorrogação indefinida não calculado.
- M06: revisão da nomeação vinculada, tutela por omissão, responsabilidade civil/política do Chefe de Estado, autenticidade das atas, competência judicial restrita e abuso de prerrogativa.
- M07/M12: limites do gabinete interino, comando militar e emergência se o chefe de Estado recusa sucessão.
- M14: regras de dissolução repetida, eleições extraordinárias, transição de mandatos e eficácia de investidura supletiva.
- Pesquisa histórica e base causal comparada robusta: não obtidas. Bélgica texto oficial utilizado de 2021 (status atual ainda a reconfirmar). A análise do regime britânico não inclui controle constitucional completo.
- A divergência anterior entre main e PR limita conclusões sobre integração. Verificar estado real do CI do último HEAD e da main antes de merge; mesmo CI success apenas valida os testes implementados, não toda a constitucionalidade.

## PRÓXIMO PASSO M03.02.05 — parecer de arquitetura e porta deliberativa
**Pergunta:** se o Parlamento pode manter um gabinete minoritário incapaz de aprovar políticas, qual sistema A/B/C e quais instrumentos R1–R4 e G3A/G3B devem ser submetidos à decisão F6, com alternativas e melhores objeções reais?
**Insumos:** quatro dossiês M03.02, matrizes de alternativas/votações/captura, legislação e precedentes verificados, estudos M02/M04/M05/M06/M14 ainda a obter.
**Critério de saída:** documento curto com 2–3 pacotes institucionais coerentes, ator/quórum/rito/prazo/financiamento/controle/transição e parecer de não regressão, distinguindo fatos, hipóteses, preferências e escolhas que dependem de aprovação expressa. Se não houver parecer mínimo das interfaces, permanecer na pesquisa e não produzir CF-NOR.
**Alternativas em pauta:** A presidencial reformado; B parlamentarismo com B2+censura construtiva e R1/R4; C premier-presidencial com competências presidenciais estritas. R2/R3 apenas acompanhadas de crítica de captura; G3A e G3B sem opção aprovada.

## CONTROLE DE VERSIONAMENTO
Toda entrega permanece no **PR #85 draft**. Nenhuma mudança na main ou no CLF foi feita nesta rodada. Não presumir integração, deliberação D, CI verde final ou parecer cruzado antes de verificar.