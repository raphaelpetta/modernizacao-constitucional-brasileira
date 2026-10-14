# CF-IC-001 — Inventário completo por artigo e primeiros 17 artigos da Lei 9.784/1999

**ID:** CF-INT-011 · **Corte:** 13/10/2026 · **Situação:** pesquisa e auditoria de integração; **nenhuma decisão constitucional ratificada**.  
**Origem CLF:** [PR #27](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/27), integrado na `main` no commit `ed58554266a48b13f2f8a796c65651e268226a52`.  
**Versão CF de referência:** `0ac5607c3a11680b17a7d35868c6db797f448334`.  
**Módulos pertinentes:** M00.02, M01, M03.01, M04, M06, M07 e M14.

## 1. O que foi alcançado de fato

O CLF expandiu seu módulo T07.M03 com:
- **80 posições de artigo** da Lei 9.784/1999 consolidadas em inventário de referência, incluindo os arts.1º–70 e 49-A–49-G, 64-A/64-B, 69-A; o **art. 49-C inteiro foi vetado**, restando **79 posições com texto positivo** segundo a consolidação consultada.
- Vetos parciais **49-A §§2º/3º, 49-G §2º, 69-A inciso III e §§3º/4º**, e histórico legislativo de acréscimos de 2006/2009/2021.
- **16 registros** de publicação e alteração, **50 remissões ou nexos críticos** — amostra, não mapa exaustivo de referências.
- **40 unidades textuais integralmente espelhadas dos arts.3º–17**, inclusive incisos e parágrafos; com o piloto anterior arts.1º–2º, **61 unidades** de **17 artigos** transcritas textualmente. Todas `C0-T` literais, **`Q` em equivalência jurídica**, sem norma promulgada e sem revogação.
- Processo de QA que obriga distinguir `49-C vetado`, demais vetos parciais, origem, titular e status normativo; o CI testa dados, **não** julga constitucionalidade ou equivalência de efeitos.

**Ressalva essencial:** o inventário **é integral no nível de artigo**, não de todos os incisos e parágrafos da lei. Os arts.18–70 ainda dependem de transcrição completa. Não anunciar `Lei 9.784 totalmente codificada`.

Fonte oficial: https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html .

## 2. Perguntas constitucionais que surgiram da transposição literal

### M01 e M06: direitos de defesa e reserva de assistência

O art.3º IV da Lei 9.784 dispõe sobre acompanhamento **facultativo** por advogado, ressalvada exigência **por lei**. **Súmula Vinculante 5 do STF** estabelece que a ausência de defesa técnica por advogado **não viola, por si, a Constituição no processo administrativo disciplinar**. Não transpor isso como afirmação de que nenhuma modalidade administrativa jamais exige defesa técnica, nem invalidar direitos específicos assegurados por outra lei/Constituição. O STF distinguiu essa súmula de procedimento disciplinar por falta grave em execução penal na **Rcl 9.339**.

Fonte STF: https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26&sumula=1199 ; https://noticias.stf.jus.br/postsnoticias/cassada-decisao-que-validou-sindicancia-para-apurar-falta-de-apenado-sem-defesa-tecnica/ .

### M00/M03/M06: competência, delegação e limites indelegáveis

Arts.11–17 diferenciam competência própria, delegação **parcial**, **três proibições** de delegação (ato normativo, recurso e competência exclusiva), publicidade formal, avocação **excepcional e temporária**. Eventual Constituição alternativa com administração independente, autônoma e digital não pode usar uma cláusula geral de coordenação para cancelar essas reservas sem deliberação de mérito.

Especialmente importante: a **decisão coordenada** de 2021 (art.49-A) mantém responsabilidade de cada órgão e **exclui** licitações, processos sancionatórios e órgãos de Poderes distintos (§6º). A supressão editorial dessas exceções seria `M`, não consolidação `C0`.

### M01/M04: legitimidade e federalismo

O art.9º protege interessados com situações individuais, coletivas e difusas e é **referido expressamente no art.49-B**; o art.26 é referido no 49-D. Assim, renumeração e condensação de categorias precisam preservar legitimidade e defesa.

Art.1º §1º da Lei 9.784 alcança os Poderes Legislativo e Judiciário da União apenas em **função administrativa**. Art.69 mantém procedimentos especiais como lei própria subsidiada; a **Súmula 633/STJ** admite aplicação subsidiária da Lei federal a estados e municípios quando falta regra local específica, particularmente sobre decadência administrativa. **Não** inferir competência automática da União sobre todo processo administrativo subnacional.

Fonte STJ: https://scon.stj.jus.br/SCON/sumstj/doc.jsp?b=SUMU&h=true&i=1&l=10&livre=SUMULA+INPATH%28TIPO%29+AND+633+INPATH%28NUM%29&ordenacao=-%40NUM&p=false .

### M14: vetos, transição e direitos adquiridos

A numeração do art.49-C aparece no cadastro legislativo, mas o **texto foi vetado integralmente**. Outras unidades foram vetadas nos arts.49-A/G e 69-A. Um índice de codificação que ressuscite essas unidades produziria incorreção normativa.

O novo Código deve preservar efeitos residuais e datas dos acréscimos legislativos de 2006, 2009 e 2021. **Art.70 da Lei9.784 é fórmula histórica de vigência de 1999**, que não poderia ser automaticamente importada como vigência futura do CLF.

## 3. Consequências metodológicas

1. **Fotografia integral no nível de artigo** é pré-condição, mas não aprovação da transposição jurídica.
2. Toda **inclusão de incisos, parágrafos, alterações, vetos e correspondências semânticas** exigirá origem, versão, competência, alcance e direitos explicitados, mantendo distinção entre `C0-T`, `C0-J`, `C1`, `M`, `Q`.
3. `Esta Lei` não se reescreve automaticamente como `este Código`; somente um Livro com âmbito juridicamente delimitado e completo poderá sustentar eventual alteração contextual, após revisão.
4. A primeira regra revogatória válida dependerá de todo regime efetivamente substituído, entrada em vigor, condições de veto e proteção de direito intertemporal. A revogação de art.1º–2º isolada segue bloqueada.
5. O projeto CF deve utilizar esses casos na redação M01/M03/M04/M06/M14 **como testes adversariais**, sem importar automaticamente dispositivos federais como artigo constitucional.

**Estado de decisões:** CF-IC-001 = PESQUISA. `DEC-001` = objetivo de Código Federal juridicamente uno; `DEC-016` = PENDENTE sobre veículo de promulgação. **Não há anteprojeto constitucional ou CLF homologado por esta nota.**
