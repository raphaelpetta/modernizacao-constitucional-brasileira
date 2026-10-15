# M03 — Garantia parlamentar transversal: investigação minoritária e limites dos poderes

**Estado H/V, sem deliberação institucional.** Fonte experimental CF-NOR-0047 no stack CF-CC-011. **Base main:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`; base branch #116 `abf450fd5491b8310e1e02b88102c370dcaeac45`.

## Hipótese e problema

As crises de governabilidade não podem converter maioria governista em monopólio da fiscalização. A proteção de um terço da Casa, objeto definido e prazo certo é um mecanismo que funciona **independentemente de o chefe de Governo precisar ou não de confiança parlamentar**. Preserva a possibilidade de comissão parlamentar mesmo quando Presidente e maioria são aliados ou quando há gabinete parlamentar de coalizão.

O art. 58 §3º da CF/1988 estabelece quórum de 1/3, investigação sobre fato determinado e prazo certo, poderes de investigação próprios das autoridades judiciais e remessa ao Ministério Público. [Texto Câmara](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html). A leitura contramajoritária foi confirmada na [jurisprudência do STF, MS 24.831/24.847](https://stf.jus.br/arquivo/informativo/documento/informativo572.htm); limites de reserva de jurisdição e defesa constam de [STF art. 5º](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=5&abrirBase=CF) e [STF art. 58](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=58&abrirBase=CF).

## Alternativas confrontadas

| Arquitetura | Como a garantia atua | O que NÃO decide |
|---|---|---|
| A — presidencialismo reformado | CPI fiscaliza Presidente e Ministério sem necessidade de desconfiança | Impeachment e poder de veto continuam autônomos |
| B — parlamentarismo racionalizado | CPI fiscaliza mesmo gabinete investido pela maioria | Não altera censura construtiva, confiança ou investidura |
| C — premier-presidencialismo | CPI alcança governo e atos presidenciais conforme competências constitucionais | Não define referenda, defesa e coexistência das chefias |
| S1/C3 e outros | Fiscalização protegida onde haja Legislativo representativo | Não pressupõe duas Casas ou órgão único de governo |

**Melhor objeção:** constitucionalizar quórum de 1/3 inflexível pode gerar multiplicidade de inquéritos, impor custos e expor dados. É objeção concreta, mas substituir direito da minoria por autorização majoritária eliminaria seu valor quando mais necessário. Testar tempo, objeto, sanções ao abuso, financiamento, transparência e proteção de dados antes de ratificar.

## Riscos não resolvidos e remissões

- **Art. 58 §2º:** demais poderes de comissões, convocações e audiências não foram reconstruídos; a expressão geral de fiscalização não equivale a essa lista.
- **Casas:** art. 58 §3º admite CPI conjunta da Câmara e do Senado; a formulação H não define se haverá segundo órgão legislativo federal. Garantia conjunta precisa de redação condicionada se o bicameralismo for mantido.
- **Poderes de investigação:** preservado o núcleo investigativo, mas não foi delimitado, caso a caso, acesso a sigilos, dados sensíveis, prisão em flagrante, mandados, sanções por omissão ou respeito ao segredo de justiça.
- **Transição:** CPI de mandato anterior, convocação de ministros, eficácia das investigações e comissões em mudança institucional precisam norma M14.
- **M05/M07/M06:** fiscalização financeira, transparência executiva, Poder Judiciário e controle de constitucionalidade continuam separados.

## Adversarial e sequência

A [matriz de 16 testes](../../auditoria/CF_CC_011_MATRIZ_16_TESTES_M02_M03.csv) contém oito casos M03 e oito casos M02. Nenhum julgamento novo foi atribuído ao STF. Os resultados são perguntas e requisitos a submeter a revisão.

**FEITO:** delimitação normativa da fiscalização minoritária sem mudar CF-DEC-006 (governo), CF-DEC-007 (Senado) ou CF-DEC-008 (justiça); primeira H funcional M03. **PENDENTE:** contraditório sobre direitos investigados, arquitetura das Casas, poderes financeiros e CPI conjunta. **PRÓXIMO:** pacotes condicionais de orçamento/confiança/censura, sem decisão A/B/C, com testes M05/M06/M14. **Dependências:** M01/M02/M04/M05/M06/M07/M12/M14; revisão do [PR #107](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/107).
