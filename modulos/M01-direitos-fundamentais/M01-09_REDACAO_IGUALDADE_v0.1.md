# M01.09 — Igualdade substantiva, antidiscriminação e especialidades constitucionais

**ID:** CF-M01.09-F7-001 · **Corte:** 13/10/2026 · **Estado:** F7 experimental, normas H, F6 não homologada.  
**Main de partida:** `35703d9fec8a30579faa0d8dad079e149923f8bf`.  
**Pesquisa paralela (não integrada à main):** [PR #22 — M01.01–M01.08](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22), head `f913120e8f5598dee90bec749a80a7705e7639e5`. A subfrente **M01.08 desse PR refere-se à privacidade e automação**. Por isso, a redação de igualdade passa a ser **M01.09**, evitando colisão de identificadores.  
**Interfaces:** M00, M02, M03, M04, M05, M06, M07, M08, M09, M11, M12, M13 e M14; Código da Legislação Federal apenas pela interface competente.  
**Local da redação:** [índice CF-NOR](../../redacao/indice.csv), [anteprojeto de trabalho gerado](../../redacao/anteprojeto-de-trabalho.md), [matriz de 16 garantias](M01-09_MATRIZ_IGUALDADE_E_GARANTIAS.csv).

## 1. Problema e contexto da pesquisa (F0–F1)

A CF/1988 já contempla **igualdade formal e material** (arts. 3º III–IV e 5º), proteção contra discriminação e diversas garantias setoriais. A **Convenção sobre os Direitos das Pessoas com Deficiência (CDPD)**, incorporada conforme art. 5º §3º da CF (Decreto 6.949/2009), define discriminação em razão da deficiência de modo a incluir a **recusa de adaptação razoável**; a LBI (Lei 13.146/2015) a concretiza. Assim, não se pode classificar esse dever como novidade ainda inexistente no Brasil.

A **Lei 15.142/2025** revogou a **Lei 12.990/2014** e estabelece **30%** de reserva de vagas nos concursos e seleções federais abrangidos, com regras próprias e transição. O percentual é decisão legislativa vigente setorial, **não patamar fixado neste piloto constitucional**. O STF considerou constitucional a política de cotas universitárias na **ADPF 186**; a **ADC 41** tratou da lei federal antiga e não deve ser transposta indistintamente para a lei de 2025. **ADI 5357:** a Corte manteve a obrigatoriedade de educação inclusiva também nas escolas particulares; o direito ao ajuste não se dissolve em liberdade empresarial abstrata.

**Fontes normativas/jurisprudenciais principais:**
- [CF/1988, Câmara — texto consolidado](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html);
- [CDPD, Decreto 6.949/2009, arts. 2º e 5º](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/decreto/d6949.htm);
- [Lei Brasileira de Inclusão — 13.146/2015, arts. 3º e 4º](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm);
- [Lei 15.142/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15142.htm);
- [STF, ADI 5357](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=5357);
- [STF, ADPF 186](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADPF&numProcesso=186).

**F2 histórico:** a ampliação da igualdade formal à material e à inclusão decorre de debates constitucionais, movimentos de pessoas afetadas e interpretação judicial, não de simples redação "mais moderna". A extensão histórica e seus efeitos causais ainda necessitam aprofundamento.

## 2. Direito comparado funcional, sem transplante direto (F3)

A [Constituição da África do Sul, seção 9](https://www.justice.gov.za/legislation/constitution/chp02.html) distingue igualdade perante a lei, realização efetiva, medidas afirmativas, discriminação direta/indireta e tutela entre particulares. Serve como arquitetura comparativa; **não prova** que um catálogo idêntico seja a melhor solução para o Brasil nem autoriza importar presunções de injustiça sem exame dos tipos de procedimento.

A CDPD impõe garantia material constitucionalmente incorporada que precede a reforma proposta e vale a todos os entes federativos. Deve ser cotejada como **piso de continuidade**, não como invenção brasileira do novo anteprojeto.

## 3. Alternativas de redação e quatro cláusulas de teste (F4–F7)

A pesquisa M01.06 no PR #22 comparou: **EQ-A conciso**, **EQ-B substantivo**, **EQ-C contramodelo excessivamente rígido**. O piloto usa abordagem inspirada em EQ-B apenas como **hipótese H de teste**, mantendo EQ-A e EQ-C como controles negativos e sem ratificação.

| ID | Tipo G/E | Função distinta | Principal risco |
|---|---|---|---|
| `CF-NOR-0008` | G | Igualdade jurídica/material com dever estatal de enfrentar obstáculos discriminatórios | Generalidade e judicialização de escolhas distributivas |
| `CF-NOR-0009` | E → 0008 | Distinção direta/indireta, justificação de efeitos e deveres pertinentes | Inferência indevida de discriminação por estatística, conflito com autonomia legítima |
| `CF-NOR-0010` | E → 0009 | Adaptação razoável e acessibilidade de pessoas com deficiência, preservando CDPD | Alegação genérica de ônus indevido e invisibilização de acessibilidade sistêmica |
| `CF-NOR-0011` | E → 0008 | Legitimidade de medidas afirmativas materialmente justificadas, sem percentuais fixos | Captura, critérios inadequados e ausência de controle distributivo |

**Especialidade funcional:** 0009 define direito/dever distinto de 0008, 0010 protege uma garantia específica já constitucional e 0011 distingue igualdade material de tratamento uniforme. Não se afirma que a enumeração G/E seja a única arquitetura correta: as quatro normas podem ser fundidas, reformuladas ou rejeitadas após testes.

**Crítica de redação:** `CF-NOR-0009` adota motivos de discriminação em cláusula aberta, ainda sem lista enumerada de categorias protegidas. A matriz exige verificar se essa escolha proporciona inteligibilidade, segurança e proteção material suficiente diante dos arts. 3º e 5º atuais. `CF-NOR-0010` usa o conceito de ônus desproporcional para ajuste individual, **não** licença para negar direitos de acesso universal. `CF-NOR-0011` prevê revisão conforme objetivos sem data terminal automática.

## 4. Casos adversariais e não regressão (F5)

A [matriz M01.09](M01-09_MATRIZ_IGUALDADE_E_GARANTIAS.csv) relaciona **16 conjuntos de garantias e cenários**. Entre outros:

1. Regra neutra de contratação produz exclusão estatisticamente importante mas possui finalidade funcional legítima; examinar prova e alternativas plausíveis.
2. Escola particular nega assistência necessária a aluno com deficiência alegando custos sem exame; conservar CDPD, LBI e ADI 5357.
3. Empresa invoca liberdade de associação para discriminar sem vínculo funcional com sua finalidade; examinar autonomia privada e proteção.
4. Comissão de heteroidentificação rejeita autodeclaração sem motivação/contestação; preservar contraditório e devido processo.
5. Governo extingue toda política afirmativa por interpretação de igualdade como tratamento idêntico; confrontar ADPF 186 e igualdade material.
6. Autoridade exige prova penal baseada exclusivamente em disparidade estatística; preservar legalidade, presunção de inocência e contraditório.
7. Governo interpreta a obrigação de adaptação individual como substituto do dever de acessibilidade universal; separar deveres.
8. Código único reduz direitos territoriais de indígenas/quilombolas a enunciado abstrato de igualdade; proibir equivalência presumida.

**Observações decisórias:** critérios de distribuição de ônus probatório civil/administrativo, sanções específicas, regras de cotas e classificação de beneficiários exigem estudos setoriais e M06; não codificar automaticamente em norma geral de proibição. Os direitos penais não são flexibilizados pela nova cláusula de discriminação.

## 5. Auditoria de continuidade: escopo e pendências

O piloto **não cobre** diretamente criminalização de racismo (CF art. 5º XLII), autonomia indígena e consulta territorial, direitos laborais de igualdade, procedimento penal, proteção de dados em provas, direitos de crianças e garantias setoriais de educação e saúde. O estado da matriz é `INDETERMINADO`, `PARCIAL_E_INDETERMINADO`, `NAO_EQUIVALENTE` ou `NAO_COBERTO`; nenhum resultado é `EQUIVALENCIA_DEMONSTRADA`.

**Melhor objeção geral:** inserir muitas regras em M01 pode repeti-las nos capítulos especiais; inserir poucas pode ocultar diferenças reais de proteção. O procedimento M00.03 exige revisão N:N de regra geral e especialidade por conteúdo e não apenas eliminação de frases.

## 6. Caminho subsequente (sem autorização decisória implícita)

- Conciliar o PR de pesquisa [#22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22) com a `main` **por arquivos de pesquisa M01**, sem sobrescrever `governanca/`, `redacao/` ou interfaces de pesquisas posteriores. O PR permanece draft até revisão própria.
- Consolidar propostas sobre vida, autonomia e integridade pessoal a partir do M01.07 de pesquisa, e privacidade/dados a partir do M01.08 de pesquisa — nomes M01.09 (presente redação) e outros subciclos posteriores sem colisão.
- Solicitar revisão jurídica M06/M09/M11/M13 antes de promover qualquer disposição de H para D.
- Realizar testes materiais, funcionais e empíricos suficientes antes de declarar equivalência à CF/1988 ou escolher desenho vinculante para a nova Constituição.

**Não houve ratificação de percentuais, categorias rígidas, condições de voto, categorias penais ou dever de término obrigatório de cotas.** Quatro normas experimentais H entram apenas no texto de trabalho.
