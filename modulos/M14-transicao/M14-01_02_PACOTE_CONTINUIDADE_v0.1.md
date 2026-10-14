# M14.01.02 — FEITO / PENDENTE / PRÓXIMO
**Corte:** 14/10/2026 · **responsável:** M14 · **issue:** [#90](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/90) · **PR:** [#91](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/91), draft · **branch:** `pesquisa/m14-01-transicao-constitucional-20261014`. **Main baseline confirmada no preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. M03 em PR85 draft é **interface**, não alteração direta nem ratificação.
**Estágio:** F0–F5/F8 — pesquisa H/P/A/V. F6 não aprovado, F7 não iniciado. Nenhuma CF-NOR, decisão D, calendário de pleito, alteração de mandato ou regra de Governo aprovada. `main` e CLF não tocados.

## FEITO
1. `M14-01_02_PARECER_PRIMEIRO_PLEITO_E_POSSE_ASSIMETRICA_v0.1.md`: parecer jurídico autônomo sobre consulta prévia, emenda e eleição inaugural, analisando explicitamente **desencontro entre início do mandato presidencial em 5 DE JANEIRO do ano seguinte à eleição (CF art82, EC111/2021) e sessões preparatórias de posse da Câmara/Senado A PARTIR DE 1º DE FEVEREIRO do primeiro ano da legislatura (CF art57 §4)**. Governo parlamentar B não pode ser considerado investido em janeiro por uma Câmara ainda não instalada. Não supor número fixo de dias de hiato, mandato presidencial encurtado nem novo quórum B2 ratificado.
2. Lei9.709/1998 arts.2–3: **plebiscito ocorre ANTES do ato**, referendo depois; decreto legislativo de convocação nacional mediante **proposta de pelo menos um terço dos membros de qualquer Casa**, sem confundir quórum de iniciativa com aprovação do decreto ou quórum art60 da emenda. **Gussoli/Hachem 2022** defendem necessidade jurídica de consulta prévia, STF MS22.972 extinguiu-se sem mérito. R-CON1/2 permanecem abertas; 1993 é precedente histórico, não regra perpétua expressa.
3. CF art16 e precedentes **ADI3.685** (anterioridade aplicável a EC e coligações) e **RE633.703 Tema387** (Lei Ficha Limpa não aplicável em 2010) confirmam que vigência formal ≠ aplicação no pleito. Não presumir incidência para qualquer norma administrativa; M02 deve qualificar alteração de processo eleitoral e proteger igualdade.
4. `M14-01_02_MATRIZ_18_TRILHAS_DE_CONSULTA_E_POSSE.csv`: **18 ramos H**, 3 arquiteturas A/B/C × 2 rotas R-CON1/2 × 3 soluções J1 eficácia diferida/J2 sincronização prospectiva/J3 caretaker legal. Alternativas concorrentes, não cronograma factual, sem datas inventadas.
5. `M14-01_02_MATRIZ_12_CONTRAPROVAS_DO_PLEITO_INAUGURAL.csv`: **12 ataques H**, incluindo presidente eleito e Câmara ainda não instalada, plebiscito confundido com PEC, iniciativa do decreto legislativo, nova lei eleitoral extemporânea, primeira investidura inválida, dupla cadeia militar, fiscalidade/receita e simetria federativa.
6. `M14-01_02_CHECKLIST_10_BLOQUEIOS_DE_POSSE.csv`: **10 condições G01–G10 todas ABERTAS**: rito de reforma, consulta, lei eleitoral e CF16, mandato, Câmara legítima, chefia de Estado, caretaker, finanças, defesa e federação.
7. `scripts/validar_m14_01_02_primeira_posse.py`: reexecução local de checagem combinatória, **sem mérito jurídico**. **QA independente realmente executada por JavaScript**, lendo os três CSV do GitHub: PASS, 18/12/10 registros, 14/8/6 campos respectivamente, IDs únicos, 18 combinações completas, todos G ABERTOS, zero campos vazios. Não afirmar que Python rodou na Actions sem prova.
8. **Síntese de engenharia ainda P:** TR-PROS e FED1 como menor ruptura; **J1/J2/J3 e R-CON1/R-CON2 continuam alternativas H**. **J1 pode exigir aguardar ciclo eleitoral posterior inteiro** para não encerrar mandato executivo legitimamente iniciado apenas um mês antes da instalação parlamentar. Nenhum calendário real estabelecido.

## PENDENTE
- **M02 issue #14:** definir quais alterações de processo eleitoral ficam sob CF16 e ADI3685/RE633703; diploma/posse, prazo mínimo operacional de primeira eleição, sistema eleitoral futuro e efeitos de consulta/popular art14/49 XV. Não atribuir aprovação a M02.
- **M03 issue #84 / PR85:** decidir como nomear premier e chefia Estado, quais quóruns B1/B2/B3, censura e confiança, e como manter Governo até primeira investidura sem novas ordens militares/finanças.
- **M14/M06 issue #55:** exame art60, mandato presidencial em curso, validade de consulta R-CON1/2, controle de omissão e conflito de posse.
- **M05/M03.01 issues #25/#18:** orçamento/LOA durante eventual hiato e poderes FIN-CT1/2/3 com obrigatoriedade de fonte e autorização financeira.
- **M04 issue #21 e M12:** não conversão automática de mandatos subnacionais, cadeia única civil/militar. M07 contratos, serviços, interoperabilidade.
- **Sem norma:** não há texto vigente novo, PEC validada, acordo para consulta prévia, autorização de encurtar mandatos, quórum de investidura ou calendário aprovado. Todas soluções são condicionais.
- **Qualidade:** QA estrutural não comprova constitucionalidade, sufrágio real, legitimidade da consulta, competência de financiamento ou previsibilidade de transição.
- **Integração:** verificar HEAD/CI/mergeability e SHA de main depois do último commit; PR permanece draft e sem aprovação F6. Qualquer adendo de governança também é só proposta na branch.

## PRÓXIMO — M14.01.03
**Prioridade executável:** solicitar resposta escrita de M02 para (i) art16 e lei aplicável à primeira eleição, (ii) procedimento/igualdade de campanha para plebiscito e quórum correto de iniciativa, (iii) confirmação eleitoral de títulos na assimetria 5 janeiro / 1 fevereiro. Confrontar com M03/M05 para primeira investidura e LOA do interino e M06 para mandato e tutela. **Critério:** uma matriz objetiva de provas com pareceres externos explícitos, não mera multiplicação de cenários H. Se ainda não respondidos, suspender CF-NOR e manter portas A/V.

## FONTES
- Constituição/1988 vigente CF57§4,82,16,60: https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html
- EC111/2021: https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc111.htm
- Lei9709/1998 art2/3: https://www.tse.jus.br/legislacao/codigo-eleitoral/leis-ordinarias/lei-nb0-9.709-de-18-de-novembro-de-1998
- STF ADI3685: https://noticias.stf.jus.br/postsnoticias/supremo-mantem-verticalizacao-para-as-eleicoes-de-2006/
- STF Tema387: https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=4003780&numeroProcesso=633703&numeroTema=387
- Consultas/controvérsia: https://doi.org/10.5007/2177-7055.2022.e91977 ; https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=380829 .

**STATUS:** documentos exclusivamente na branch PR91 até integração; a CI não é decisão jurídica.