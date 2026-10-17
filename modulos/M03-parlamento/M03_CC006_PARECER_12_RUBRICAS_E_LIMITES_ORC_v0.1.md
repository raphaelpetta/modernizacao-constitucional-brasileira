# CF-CC-006 — teste institucional por 12 rubricas, fontes e liquidez

**Data:** 15/10/2026. **Estado:** P/A/V em pesquisa, sem norma CF-NOR, F6/D ou simulação financeira do orçamento brasileiro. **Branch:** PR #107. **Fonte de hipóteses:** `M03_CC004_TRES_ALTERNATIVAS_ORC_E_INV_v0.1.md`, protótipos A/B/C do M03; [CF-NOR-0002 H](../../redacao/propostas/CF-NOR-0002.md) M05; regras constitucionais vigentes arts. 165–169; M07 CF-NOR-0021 H; [CLF T07 PR #45](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/45) e #49 apenas experimentais.

## Resultado crítico

O problema do orçamento não aprovado não é resolvido por uma opção entre presidencialismo e parlamentarismo. Quatro filtros devem ser **aplicados individualmente a toda rubrica**: (1) obrigação ou autorização legal material; (2) título orçamentário ou autorização fiscal extraordinária válida; (3) fonte e competência federativa; (4) execução, liquidação e disponibilidade financeira. A existência de um não presume os outros. O regime de continuidade hipotético ORC-A/B/C exige regra prospectiva constitucional e legal, **não** aplicação implícita de LOA pretérita.

A [matriz de doze tipos de rubrica](M03_CC006_DOZE_RUBRICAS_ORC_SEM_LOA.csv) diferencia folha, benefícios, contratos essenciais, repasses, emendas, créditos extraordinários, programas novos, infraestrutura digital, defesa civil, obras, dívida e tutela judicial social. São **tipos hipotéticos, não rubricas de dado nacional**; sem montantes, empenhos ou orçamentos reais analisados.

## Avaliação falsificável das três ORC

| Critério | ORC-A — continuidade legal anterior | ORC-B — autorização transitória deliberada | ORC-C — piso constitucional fechado |
|---|---|---|---|
| Falta de autorização anterior suficiente | **FAIL possível** | depende da aprovação transitória | **FAIL possível** se piso não detalhado |
| Parlamento sem maioria por dois exercícios | não oferece solução política necessária | **FAIL sob bloqueio** | permite continuidade estrita se lei válida/limites prévios |
| Programa/tributo/dívida novos | sem competência por continuidade | sem presunção de aprovação | vedação de autorização fiscal em branco |
| Repasses federativos com fonte legal | classificação por obrigação e título | incluir norma transitória se exigida | delimitar no piso objetivo e art. 167 §7 |
| Controle da execução | demonstrativos e órgãos legais | votação e fiscalização da autorização | controle reforçado dos gatilhos, finalidade e prazo |

**Resultado geral:** nenhuma opção satisfaz os cinco critérios em todos os doze casos com a informação disponível. Não afirmar que ORC-C é superior só porque preserva despesas essenciais, nem que ORC-B oferece solução para paralisia parlamentar. A preferência só pode surgir com texto delimitado, dados e comparação de efeitos.

## Três interfaces que devem produzir devolutiva de fato

1. **M05 (custeio):** para cada rubrica, especificar base legal, órgão competente, dotação, fonte, liquidação, prazo e fluxo de caixa; art. 167 §7 não se confunde com título automático de despesas de um Governo provisório.
2. **M06 (controle):** juiz pode impor dever concreto e fiscalizar legalidade, inclusive omissão grave, mas **não aprova sozinho LOA** ou forma maioria parlamentar; delimitar tutela de contas e orçamento com respeito às competências.
3. **M07/CLF T07/T43 (continuidade digital):** indisponibilidade do canal não suprime direito de petição/defesa; no PR #45 a pesquisa identificou diferença entre envio, recebimento, consulta e ciência, porém sem prova completa do caso Ibama. Exigir prova de opção, destinatário, logs, norma temporal aplicável e mecanismo de correção de prazo. Falha de ciência não cria poder de gasto ilimitado.

**FEITO:** matriz de 12 classes e teste ORC-A/B/C por critério; **PENDENTE:** amostra financeira real, leis e orçamentos de referência, revisão M05/M06, jurisprudência e consentimento institucional. **PRÓXIMO:** preencher pelo menos duas rubricas com fonte jurídica e financeira verificáveis antes de declarar alternativa de orçamento mais madura, sem F6/D e sem copiar decisão da CLF.
