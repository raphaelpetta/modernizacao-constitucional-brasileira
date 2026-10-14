# M14.01 — FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026 · **Responsável:** M14 · **Issue:** [#90](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/90) · **PR draft:** [#91](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/91) · **branch:** `pesquisa/m14-01-transicao-constitucional-20261014` · **main SHA de entrada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **M03 interface:** [PR85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85) draft, *não incorporado à main*.
**Status:** F0–F5/F8 pesquisa com estados H/P/A/V, F6/F7 **não realizados**. Nenhum texto CF-NOR, nenhuma decisão D, nenhuma integração à main, nenhuma edição CLF.

## FEITO
1. `M14-01_PARECER_AUTONOMO_VIABILIDADE_CONSTITUCIONAL_E_TRANSICAO_v0.1.md`: parecer funcional **independente M14** que testa e complementa a hipótese M03.02.13. Examina CF arts.1/14/16/18/25/29/49 XV/60/76–86/158–160/165–169, ADCT2/3, EC2/1992, STF ADI829/981/1722 e **MS22972 extinto sem resolução do mérito em 08/06/2018**. Distingue art60 derivado, revisão excepcional não reaberta e constituinte originário sem rito simplificado presumido.
2. **Divergência jurídica material identificada e explicitada**: doutrina de **Gussoli & Hachem (2022, Sequência, DOI 10.5007/2177-7055.2022.e91977)** aceita alteração do sistema por PEC, **mas defende novo plebiscito prévio como exigência constitucional por soberania**. O texto do ADCT2/1993 por si não impõe repetição genérica, e o STF **não** resolveu no MS22972 a necessidade de consulta/validade da PEC. Não afirmar dispensa definitiva nem obrigação judicialmente decidida. R-CON1/2/3 continuam abertos.
3. **Nova dimensão federativa**: STF, anotação art25, recomenda cautela com simetria e autonomia estadual; adoção do parlamentarismo federal não implica conversão automática de governos estaduais/municipais. FED1 federal somente, FED2 faculdade futura e FED3 imposição foram tratados com seus custos; P investigativa FED1 como menor ruptura, sem aprovação jurídica integral.
4. **Nova dimensão de mandatos**: TR-PROS prospectiva após eleição aplicável e preservação de titularidades é P prudencial; TR-IMEDIATA com redefinição do mandato presidencial em curso é hipótese de **alto risco** e exige justificação própria. Três arquiteturas A/B/C mantidas concorrentes.
5. `M14-01_MATRIZ_18_ROTAS_E_MANDATOS.csv`: **18** combinações (3 arquiteturas × 2 tempos × 3 alcances territoriais), sem calendário real fixado.
6. `M14-01_MATRIZ_12_TESTES_DE_TRANSICAO.csv`: **12** contraprovas constitucional-eleitorais/federativas, incluindo abuso do rito ADCT3, falsa afirmação de julgamento de mérito MS22972, governo cessante e cadeia de comando, tutela de receitas de entes.
7. `M14-01_PAUTA_12_PORTAS_F6.csv`: **12** pontos de decisão ainda ABERTOS, art60/plebiscito/mandatos/eleições/chefias/caretaker/federalismo/CLF.
8. `scripts/validar_m14_01_transicao.py`: verificador reproduzível de schemas, IDs e cruzamentos. **QA estrutural independente via JavaScript executado** lendo CSV no GitHub: PASS, 18/12/12, produto cartesiano completo, IDs únicos, campos não vazios e todas portas F6 ABERTAS. Script Python existe; não afirmar que workflow o executa sem confirmação direta.
9. Resposta à M03.02: concordância no princípio de não vacância e eficácia prospectiva, mas **revisão explícita** de (i) doutrina de consulta obrigatória prévia, (ii) federação e simetria, (iii) preservação de mandatos subnacionais; não aprovar a preferência de regime B nem importar quóruns de outra frente.

## PENDENTE — impedimentos e interfaces
- **M02 issue #14:** parecer sobre primeira eleição e aplicação CF16, nomeação/chefia B/C, consulta prévia e direito da oposição; reforma do calendário não presume extinção de mandato.
- **M03 issue #84/PR85:** que arquitetura, investidura e poderes de chefe Estado são base de projeto P/D; sem escolha material.
- **M04 issue #21:** alcance do princípio de simetria, autonomia estadual/municipal e receitas partilhadas; análise FED1/2/3.
- **M05 issue #25/M03.01 #18:** proposta LOA/crédito pelo caretaker limitado: FIN-CT1/2/3, competência, fonte, teto/dívida e repasses.
- **M06 issue #55 / PR62:** revisão jurídica art60 e soberania popular/consulta; tutela G3A/G3B, eleição, omissão, posse e controle de atos.
- **M07/M12:** serviços e autoridade civil única de defesa/emergência no marco T3.
- **Dado de realidade:** não existe análise empírica de custo de transição, prazo viável de T0–T4 nem parecer completo sobre primeira eleição/mudança de cargos.
- **Integração/governança:** PR91 draft até análise; verificar ci/mergeability e main antes de merge. Nenhum F6/D, CF-NOR, `redacao/indice.csv`, `governanca/03_DECISOES.md`, CLF ou main modificado por ratificação.
- **Atenção:** doutrina não é jurisprudência vinculante; extinção do MS22972 não constitui aprovação de parlamentarismo. Consulta popular, se vier a ser adotada, não cura cláusula pétrea ou quórum de PEC.

## PRÓXIMO — M14.01.02
**Questão operacional prioritária:** preparar **roteiro jurídico de validade do primeiro pleito e posse** sob TR-PROS, considerando (1) três cenários A/B/C com mandatos preservados, (2) R-CON1/R-CON2 e legitimidade da consulta, (3) revisão M02 de art16 e identificação da lei aplicável, (4) revisão M04 de FED1 e (5) restrições M03.01/M05 ao caretaker/LOA. Sem receber resposta intermodular, marcar V/A e não produzir CF-NOR. Revisar o próprio parecer se fontes superiores o contradisserem.

## PROVENIÊNCIA E FONTES
- STF ADCT3 https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=3&abrirBase=AD .
- STF MS22972 desistência https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=380829 .
- STF simetria art25 https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=25&abrirBase=CF .
- CF atualizada https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm .
- Gussoli/Hachem (2022) https://doi.org/10.5007/2177-7055.2022.e91977 .
- Espanha governo cessante https://www.boe.es/buscar/act.php?id=BOE-A-1997-25336 .
- Alemanha GG69 https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html .
- Governança CF-GOV-012/015 da main, PR85 draft, issue90.

## STATUS DE MERGE/CI
Após publicar o último arquivo do ciclo, verificar **PR #91**, workflow Actions/HEAD e comparação com main; resultados aqui só são verdadeiros para o SHA citado. **Sucesso CI estrutural não ratifica mérito jurídico.**