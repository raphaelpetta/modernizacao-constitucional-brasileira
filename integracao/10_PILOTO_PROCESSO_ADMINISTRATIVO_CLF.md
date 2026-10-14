# CF-IC-001 — Piloto T07.M03: âmbito e integridade da lei federal de processo administrativo

**ID:** CF-INT-010 · **Data:** 13/10/2026 · **Estado:** PESQUISA, sem deliberação constitucional ou codificação aprovada.  
**Fonte CLF:** [PR #25](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/25), **integrado** na main do CLF pelo commit `fbc137173805a5d44d1b04a73c2a5c2fad1dd409`.  
**Arquivos no CLF:** `modulos/T07/M03/PILOTO_13_ARTIGOS_1_2_LEI9784.md`, `CONCORDANCIA_INTEGRAL_ART1_ART2_13.csv`, `MAPA_DEPENDENCIAS_SISTEMICAS_13.csv`, `TESTES_VETO_CONTEXTO_TRANSICAO_13.csv`.  
**Módulos CF pertinentes:** M00.02 (fontes e hierarquias), M03.01 (iniciativa/veto), M04 (competências federativas), M01 (direitos e devido processo), M06 (função administrativa do Judiciário), M14 (transição e efeitos).

## 1. Resultado factual do piloto

O CLF fez transposição **textual experimental e integral** das unidades dos arts. 1º e 2º da Lei 9.784/1999:
- **art. 1º:** caput, §1º, §2º e seus três incisos (**6 unidades**);
- **art. 2º:** caput, parágrafo único e treze incisos (**15 unidades**).
Há **21 cópias literalmente correspondentes**, **16 dependências normativas** e **30 hipóteses adversariais**. Todas as cópias mantêm `equivalencia_juridica=Q`, `NAO_PROMULGADO`. **Não se afirma que a lei federal foi codificada ou revogada.**

Fonte oficial atualizada: https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html .

**Problema de alcance:** copiar `Esta Lei` para Código de 48 títulos pode estender indevidamente a definição do âmbito federal, as definições de órgão/entidade/autoridade e a aplicação aos **órgãos do Legislativo e Judiciário da União em função administrativa**. A substituição textual por `este Livro` é hipótese de nova redação **a auditar juridicamente**, não operação neutra validada. O contexto de arts. 3º–70, com disposições intercaladas, **ainda não foi incorporado**.

## 2. Dependências constitucionais reais

**Separação de Poderes e administração:** art. 1º, §1º, da Lei 9.784 alcança órgãos dos Poderes Legislativo e Judiciário **quando no desempenho de função administrativa**. A codificação futura não deve converter isso em autorização de regular a função legislativa/jurisdicional propriamente dita, nem eliminar garantias procedimentais dentro desses Poderes.

**Federalismo:** STJ **Súmula 633** permite aplicar subsidiariamente a Lei 9.784/1999 a estados/municípios **quando ausente lei local específica**, notadamente sobre decadência para revisão de atos. Tal orientação é jurisprudência de integração de lacunas, **não título de competência constitucional automaticamente delegado ao legislador federal**. A nova Constituição deve distinguir normas gerais nacionais que forem expressamente atribuídas à União, legislação de seus próprios processos administrativos, e eventual subsidiariedade interpretativa. Fonte: https://scon.stj.jus.br/SCON/sumstj/doc.jsp?b=SUMU&h=true&i=1&l=10&livre=SUMULA+INPATH%28TIPO%29+AND+633+INPATH%28NUM%29&ordenacao=-%40NUM&p=false .

**Relação entre lei geral e lei especial:** o **art. 69** reserva os processos administrativos específicos a normas próprias, sendo apenas subsidiária a Lei 9.784. Tirar arts. 1º e 2º da lei antiga, mantendo art. 69 e demais regras fora do CLF, torna o sistema possivelmente incoerente. Não converter remissões e regras de subsidiariedade em presunção editorial.

**Veto e transição:** sob CF/1988 art. 66, §2º, parágrafos e incisos podem ser vetados como unidades integrais. Um veto ao §1º ou §2º do art. 1º afeta alcance ou conceitos; veto ao parágrafo único ou incisos do art. 2º afeta direitos. **Revogação parcial da lei antiga fica bloqueada** enquanto não houver substituição jurídica suficiente, deliberação e condições de eficácia aprovadas.

**Direitos:** ampla defesa, contraditório, proporcionalidade, motivação, segurança jurídica, provas e recursos são aspectos centrais da disciplina. A atualização estrutural do Código não é licença para suprimi-los sob pretexto de condensação normativa.

## 3. Perguntas devolvidas aos módulos constitucionais

1. Como enunciar na nova Constituição **competência normativa da União sobre o seu processo administrativo**, garantindo autonomia dos entes federados e proteção mínima dos direitos procedimentais?
2. Como conciliar funções administrativas do Legislativo e Judiciário com suas autonomias de organização e iniciativa reservada, sem esvaziar a aplicação transversal de garantias?
3. O futuro Código precisa distinguir **normas gerais nacionais** (apenas se competência constitucional) de **normas federais de aplicação própria**?
4. A organização do Código em Livro tem consequência jurídica para `Esta Lei`, mesmo antes de transpor o **conjunto completo** dos arts. 3º–70? Como aprovar alterações referenciais sem expansão tácita de matéria?
5. Como condicionar eventuais revogações à efetiva promulgação do substituto **depois** de vetos parciais de garantias ou definições?
6. Qual regime de transição garante aplicação subsidiária a processos especiais e preserva efeitos para procedimentos em curso, atos praticados e jurisprudência consolidada?
7. A transposição fiel deveria prever teste explícito de **contexto**, além do teste de igualdade literal e quadro de proveniência, antes de receber selo `C0-J`?

## 4. Encaminhamento sem homologação

O CLF recebeu novo piloto temático **T07.M03**; o trabalho ainda não fornece versão completa da Lei 9.784 dentro do Código. Próxima etapa: inventariar arts. 3º–70, dispositivos intercalares e alterações de 2006/2009/2021, preservando vetos históricos, jurisprudência, âmbito federal e subsidiariedade. No projeto CF, usar os resultados como **teste adversarial de competências, direitos e processo legislativo**, não como aprovação de artigos constitucionais.

**Objetivo CLF DEC-001** preservado; **DEC-016** pendente; **CF-IC-001** permanece pesquisa.
