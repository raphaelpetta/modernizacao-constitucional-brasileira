# CF-IC-001 — Anexos normativos: três casos legislativos e auditoria literal do CLF

**ID:** CF-INT-009 · **Corte:** 13/10/2026 · **Estado:** PESQUISA H/Q, **nenhuma decisão constitucional ratificada**.  
**Fonte do CLF:** [PR #24](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/24), integrado na main pelo commit `12607cdd12c9ae677ea174cc5d54be133ccf7cd3`.  
**Baseline CF:** `abdfdc23cd698123faa362dcd90e1502ef9dbfed`.  
**Módulos destinatários:** M00.02 (fontes, lei e conteúdo normativo), M03.01 (veto, sanção, quóruns, procedimentos), M14 (transição), M01 (direitos), M04 (competências), M05 (orçamento).

## 1. Evidência direta da prática legislativa

**AN01 — VET 37/2026:** a Lei 15.459/2026 pretendia modificar o **anexo da Lei 7.405/1985** por seu art. 4º. A Mensagem 586/2026 vetou **art. 4º, art. 5º e anexo**; a lei promulgada identifica art. 4º e anexo como vetados. O Congresso registra dois dispositivos do veto `37.26.001` (caput art.4º) e `37.26.002` (caput art.5º), não uma lista de unidades autônomas dentro do anexo. Veto **não apreciado** no corte.  
Fontes: https://www.congressonacional.leg.br/materias/vetos/-/veto/detalhe/18469 ; https://presidencia.gov.br/ccivil_03/_ato2023-2026/2026/msg/vep/vep-586-26.htm ; https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15459.htm .

**AN02 — VET 35/2023:** vetou os **§§2º e 3º do art.21 da Lei 14.724/2023**, sobre substituição da tabela III do anexo IV da Lei10.486/2002 e atualizações posteriores. O Congresso derrubou ambos em **09/05/2024**; em **22/05/2024**, os dispositivos e **ANEXO VI com valores remuneratórios** foram promulgados, publicados em 23/05/2024. Isso confirma utilização legislativa de anexo com consequências normativas e processo posterior à derrubada do veto. **Não** demonstra poder do editor de substituir tabelas sem ato competente.  
Fontes: https://www.congressonacional.leg.br/pt_BR/materias/vetos/-/veto/detalhe/16069 ; https://www2.camara.leg.br/legin/fed/lei/2023/lei-14724-14-novembro-2023-794941-promulgacaodevetos-171874-pl.html .

**AN03 — VET 9/2026, LOA 2026:** a Lei15.346/2026 teve **dotações de Volumes IV e V** vetadas como itens discriminados por unidade, ação, fonte e valor. **É fato**, portanto, que o sistema orçamentário federal admite na prática veto **individualizado de dotações em anexos**. Mas **o orçamento possui objeto e rito constitucionais próprios (CF arts.165–166)**. Isso **não prova** que uma linha de tabela revogatória permanente de qualquer Código possa receber o mesmo tratamento.  
Fontes: https://www.congressonacional.leg.br/materias/vetos/-/veto/detalhe/18029 ; https://legis.senado.leg.br/norma/42528550 .

**Distinção probatória:** AN01–AN03 são **fontes legislativas primárias**, **não** acórdãos do STF decidindo constitucionalidade de veto a linha de anexo de Código. A pesquisa focal ainda não localizou tal precedente judicial diretamente aplicável; **não declarar inexistência universal de precedente**.

## 2. Cotejo dispositivo a dispositivo, sem promover equivalência jurídica fictícia

O CLF apresentou `modulos/T01/M04/AUDITORIA_LITERAL_DISPOSITIVOS_12.csv` com **24 espelhos literais** da **LC95/1998** e da **Lei9.784/1999**, `EVENTOS_ANEXOS_VETOS_12.csv` com **11 eventos legislativos** e `TESTES_CONTEXTUAIS_12.csv` com **18 contraprovas**. Controle automático exige `texto_fonte == texto_espelho_experimental` e mantém todos os registros de transposição **Q** quanto à equivalência jurídica e **NAO_PROMULGADO**.

**Razão decisiva:** literalidade **C0-T** não é equivalência jurídica **C0-J**. A Lei9.784 art.1º e §1º abrange funções administrativas do Legislativo e Judiciário federal, além da Administração federal direta e indireta; transferir seu art.2º para capítulo restrito a um Poder muda âmbito, ainda que a redação coincida. Os enunciados `dentre outros` (rol aberto), exceções legais e de sigilo, contraditório, provas, recursos e proibição de retroatividade de nova interpretação são juridicamente essenciais.

## 3. Consequências para eventual Constituição alternativa

- **M03.01:** investigar exatamente o status da **linha de anexo com conteúdo revogatório**, inclusive comparando (i) veto de art.4º que remete a anexo, (ii) veto dos §§2º–3º de lei de remuneração e promulgação posterior da tabela, e (iii) veto a dotações sob **rito constitucional orçamentário especial**.
- **M00.02:** determinar como anexos legislativos autênticos diferem de tabelas de concordância apenas editoriais, sem conferir poderes constitutivos de lei a operadores ou repositórios.
- **M14:** manter tabelas de efeitos intertemporais, veto e derrubada, direitos residuais e autenticidade de versões históricas; a revogação não deriva da simples presença de linha em planilha.
- **M01/M04/M05:** cotejo contextual deve respeitar direitos, competências federativas, iniciativa e reserva de lei, inclusive matérias de orçamento anual que **não integram automaticamente** legislação permanente do Código.
- **Interface `CF-IC-001`:** não decidir CP/CE nem a espécie de Código por força desses casos; dados são condições de modelagem, não decisão constituinte.

## 4. Encaminhamento sem homologação

**Via A/D:** dispositivos revogatórios legalmente enumerados, acompanhados por tabela explicativa de concordância sem efeito normativo — hipótese provisoriamente de menor risco. **Via B:** anexo normativo estático votado e publicado — possível matéria de pesquisa, porém **Q** quanto a unidade de veto e compatibilidade específica da legislação permanente; não equiparar linha de CSV a inciso constitucional.

A pesquisa reforça que a futura Constituição pode disciplinar a codificação, **mas precisa escolher um desenho de promulgação próprio**, sem silenciar sobre iniciativa, quórum, sanção/veto e versões. CLF `DEC-001` permanece finalidade; `DEC-016` **PENDENTE**. CF nenhuma solução aprovada.
