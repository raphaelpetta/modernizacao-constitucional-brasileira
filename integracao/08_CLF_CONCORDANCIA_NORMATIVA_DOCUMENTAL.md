# CF-IC-001 — Concordância documental e possível anexo normativo no Código único

**ID:** CF-INT-008 · **Data:** 13/10/2026 · **Status:** PESQUISA H/Q, sem deliberação constitucional ou incorporação normativa.  
**CF baseline:** `afe67ef7cbe0aa2931b555c2936e837bb9704990`. **CLF baseline:** `189860ee90d24eb57c698c54b7a4bf04e090270d`; estudo integrado na `main` CLF em `d9dadf0f11661cf7d1b040126fdf4700599b6f8b`, via [CLF PR #22](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/22).  
**Dependências:** M00.02 (fontes/reservas); M03.01 (iniciativa, veto, quórum e sanção); M14 (transição); M01 (direitos); M04/M05 (competência/encargos); CF-IC-001.  
**Escopo:** separar ato com força de lei e documentação oficial para evitar que a **unidade de consulta** seja confundida com a **unidade jurídico-formal** desejada.

## 1. Pergunta institucional específica

A futura Constituição precisa criar regra especial para incorporar **uma tabela normativa estática de revogações** a um Código formalmente uno? Ou uma codificação com **artigos legislativos expressos** e tabela **explicativa não normativa** poderia resolver grande parte do problema sem mudar o rol de unidades de veto?

Sob CF/1988, art. 66, §2º, o veto parcial incide apenas sobre texto integral de **artigo, parágrafo, inciso ou alínea**. **Não foi demonstrado** que uma linha de anexo normativo, isoladamente, possa ser tratada como unidade de veto dessas categorias. Ao contrário, há exemplos de legislação que altera/disciplina anexos, mas eles **não decidem** a técnica de veto de linhas de tabela sob a Constituição atual. A LC 95/1998, art. 9º, exige enumeração expressa de leis/dispositivos revogados, e art. 13, §1º, impõe continuidade na consolidação.

Fontes oficiais: Constituição https://www4.planalto.gov.br/legislacao/legis-federal/constituicao ; LC 95 https://www2.camara.leg.br/legin/fed/leicom/1998/leicomplementar-95-26-fevereiro-1998-363948-normaatualizada-pl.html .

## 2. Arquitetura em três camadas — hipótese de governança técnica

- **N — disposições normativas:** revogações, condições de vigência, transição e texto substitutivo somente se validamente **aprovados e promulgados**. Se um anexo tiver força normativa, deve ser estático, identificado e deliberado como parte de ato legislativo; não permitir atualização dinâmica por editor. Sua **unidade de veto ainda está Q**.
- **D — concordância documental:** tabela de origem/destino, classificação C0/C1/M/Q, relação 1:1, 1:N, N:1, motivo da exclusão, fontes, jurisprudência e versão **sem poder autônomo de mudar o direito**.
- **P — eventos públicos de autenticidade e vigência:** registros de promulgação, vetos, publicação e revisões. O dado publicado não equivale ao ato constitucional de criação/revogação.

**Definição constitucional a investigar:** se o órgão de codificação pode publicar versões oficiais com valor probatório sem substituir o ato promulgador; como sancionar a divulgação de texto editorial diverso do texto autêntico e como permitir retificação sem usurpação de competência.

## 3. Três modelos e falhas

**A/D — texto articulado + tabela explicativa:** artigos revogadores por grupos homogêneos, cada um com condição no mesmo enunciado indiviso (ciclo V1/M2), identificação exata de fonte e destino. Tabela de concordância explica e dá rastreabilidade. **Risco:** volume de artigos e vetos ao substituto parcialmente promulgado. **Hipótese preliminar mais conservadora.**

**B — anexo normativo estático vinculado a artigo:** possibilidade de enumerar centenas/milhares de revogações em tabela **expressamente aprovada junto com lei**, com identificação de unidade e condição. **Riscos essenciais não resolvidos:** como aplicar art. 66 §2º a linha/tabela; se satisfeito art. 9º da LC95; se linhas de regimes LO, LC e iniciativa reservada podem compartilhar ato; efeitos de veto/enmenda de parte do anexo; autenticidade e transição. **Não recomendar adoção sem parecer específico.**

**C — lei que revoga “o que constar no índice do portal”: REPROVADA como hipótese de desenho**, porque o índice mutável atribuiria indevidamente efeitos jurídicos a editores.

## 4. Direito comparado com diferenças jurídicas relevantes

**OLRC — EUA:** codificação positiva por título promulgado, com *disposition table*, *source credit table* e *revision notes* no relatório legislativo. São instrumentos de rastreabilidade, não autorização para um editor revogar lei federal por tabela dinâmica. https://uscode.house.gov/codification/legislation.html .

**Nova Zelândia:** `Legislation Act 2019` (versão de 04/09/2026), seções 30–39, 59–62, 78–91, incluindo **79A** sobre o estatuto de notas e informações publicadas; mostra por que o efeito dos materiais editoriais deve ser definido. https://www.legislation.govt.nz/act/public/2019/58/en/latest/sections/DLM7298272/ .

**Brasil:** Decreto 12.018/2024, art. 5º, revoga dispositivos que constavam em anexo de decreto anterior; **não** resolve possibilidade de veto separado a linhas de anexo legislativo. https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/decreto/d12018.htm .

## 5. Testes e perguntas devolvidas a M03.01/M00.02/M14

1. Qual é a menor unidade normativamente vetável na futura Constituição, se a forma legal admitir anexos com força de lei? Convém preservar art. 66 §2º por analogia, ou instituir regra explícita sem ampliar excessivamente o veto?
2. A enumeração revogatória em **anexo fechado e votado** satisfaz a clareza e a exigência de enumeração legislativa? Qual o papel de remissão em artigo de lei?
3. Se parte do anexo for vetada, como se preserva a dependência entre revogação R e substituto S **sem curadoria constitutiva de uma comissão**?
4. Como comprovar que a versão de tabela votada pelas duas Casas é idêntica à sancionada/promulgada, com rastro das emendas e vetos? Quem pode retificar erro real do ato promulgado?
5. Como manter classes materiais distintas de quórum/iniciativa e a unidade formal do Código CE/P4 — ainda uma hipótese?
6. Como registrar perda de validade, direitos adquiridos e efeitos residuais sem confundir metadados com disposição normativa?
7. Um cadastro com centenas de linhas pode mudar via meio eletrônico **sem** converter-se em emenda legislativa? **Sim, apenas se o conteúdo for puramente documental**; qualquer comando normativo precisa de ato competente.

**Estado decisório:** CF-IC-001 = PESQUISA; CLF DEC-001 = objetivo; DEC-016 = PENDENTE. A integração registra perguntas e riscos, **não** escolhe o veículo nem ratifica minuta.
