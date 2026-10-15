# M03.02.14 — FEITO / PENDENTE / PRÓXIMO
**Data:** 15/10/2026 · **M03 issue #84** · **PR [#85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85), draft** · **branch:** `pesquisa/m03-02-governo-responsabilidade-20261014` · **main conferida:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Interfaces independentes ainda não mescladas:** M02 PR95 (art.77/ADI5525), M06 PR96 (contraparecer de art60 e EC2/1992), M14 PR91 (transição) e governança PR97. Esta rodada é documentação de PESQUISA M03, sem aprovação autônoma dos outros módulos ou decisão D/F6/F7. Não mexeu CF-NOR, CLF, `governanca/03_DECISOES.md` ou main.

## FEITO
1. `M03-02_14_PARECER_COMPETENCIAS_CHEFIA_ESTADO_A_B_C_v0.1.md`: atribuição funcional de quem **decide materialmente, assina/representa formalmente, referenda, fiscaliza e exerce temporariamente** competências de Estado/Governo. Mantém A Presidência reformada, B-D Presidente CHEFE ESTADO direto, B-I CHEFE ESTADO indireto e C premier-presidencial. **B-D/B-I são comparações sobre UM mesmo modelo B não selecionado**, sem contagem de voto F6 e sem rascunho de PEC.
2. `M03-02_14_MATRIZ_16_ATOS_TITULARIDADE_A_BD_BI_C.csv`: **16 funções × 4 variações analíticas** = 64 enquadramentos H, TODOS status ABERTA. Abrange eleição titular, escolha candidato PM, investidura, nomeação, censura, ministros, Governo, veto, dissolução, decreto, LOA, dívida, tratados, defesa, emergência, primeira posse/mandatos. Regras de referenda e tutela explicitamente abertas.
3. `M03-02_14_MATRIZ_12_TRAVAS_ORIGEM_MANDATO_E_F6.csv`: 12 perguntas F6 **TODAS ABERTAS** com quem precisa emitir parecer, ato e risco. Especificamente: chefe Estado direto/indireto, conteúdo mandato, escolha PM, B1/B2/B3, G3A/B, refrendo inaugural, dissolução, caretakers LOA, diplomacia, defesa, federação, prazo primeira investidura e eventual consulta.
4. `scripts/validar_m03_02_14_competencias.py`: checagem estrutural disponível na branch, não valida legalidade nem executada manualmente nesta sessão. **QA independente JS efetivamente realizada, obtendo CSV da branch:** PASS 16/12 registros, 11/7 campos, 4 análises em cada ato, IDs ordenados/únicos, tudo ABERTA, zero vazios.
5. **Achados externos jurídicos primários:** Alemanha GG art58 (contrassinatura e exceções), art63 (voto de PM/possível escolha nomear/dissolver no último estágio), art67 censura construtiva e art65a comando ministro Defesa; Espanha CE64 (referenda Presidente do Congresso nomeação PM/dissolução art99), CE99/115 (investidura/dissoluções distintas); Portugal CRP195(2) (demissão EXCEPCIONAL presidencial Governo para funcionamento regular) não corresponde a livre demissão sob C; França CF art19 lista exceções à contrassinatura, arts8/12/20/21/49 têm regime próprio. **Fontes estrangeiras comparativas NÃO vigem no Brasil nem impõem quóruns ou prazos.**
6. **Correções das interfaces:** M02/M06 sustentam que PM escolhido pela Câmara eleita diretamente ≠ eleição presidencial ordinária direta art77; CF81§1 trata apenas de dupla vacância excepcional; ADI5525/5619 julgaram LEI ordinária, não PEC permanente. M06 verificou PGR contra tramitação no MS22972, mas STF encerrou sem mérito; EC2/1992 §1 previa vigência em 1/1/1995 após consulta 1993, exemplo HISTÓRICO de eficácia diferida não prazo mandatório hoje.

## PENDENTE
- **M02/M06:** parecer próprio sobre modo de escolha do chefe Estado B-D/B-I, poderes REAIS e núcleo do art60§4 II, efeitos das campanhas/mandatos, consulta R-CON1/2 controvertida.
- **M03:** deliberar A/B/C/D0 explicitamente em F6, depois origem da chefia, controles, quórum investidura B1/B2/B3, G3A ou G3B, referenda, veto e dissolução; não entender mera continuidade como voto sobre B.
- **M03.01/M05:** decidir CT-A/CT-B ou alternativa juridicamente válida para LOA/créditos durante governo em funções; nenhuma nova dívida sem fonte/autorização.
- **M12:** comando único de Forças Armadas e emergência sem ordens incompatíveis; dupla chefia mais perigosa em C.
- **M04/M14:** não alterar mandatos locais por simetria automática; preservar mandatos atuais, primeira Câmara instalada e efeitos prospectivos sem criar vácuo.
- **Governo e Direito:** nenhuma minuta de CF-NOR e nenhum calendário inaugural aprovado; quóruns, partidos, senado, cargos, chefias e poderes têm apenas enunciados funcionais H/P.
- **CI:** somente o resultado do workflow do último HEAD verificado poderá ser descrito como aprovado; QA JS de CSV não valida mérito jurídico.

## PRÓXIMO
**Parar de multiplicar novos cenários.** M03.02 já dispõe de quadro decisório suficiente para debater F6, **mas ainda não de aprovação independente** dos módulos responsáveis. Solicitar parecer material concentrado em 4 interfaces P01/P02 (voto e mandato), P06 (referenda inaugural), P08/P10 (fiscal e Defesa). Quando existir escolha material expressa, produzir articulado experimental com titulares competentes e submetê-lo a M02/M06/M14 **antes** de CF-NOR. Se a escolha continuar D0, registrar pendências sem presumir B-D nem B-I.

## Fontes
- Constituição alemã: https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html .
- Constituição espanhola: https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229 .
- Constituição portuguesa: https://www.parlamento.pt/Legislacao/Paginas/ConstituicaoRepublicaPortuguesa.aspx .
- Constituição francesa: https://www.legifrance.gouv.fr/loda/texte_lc/LEGITEXT000006071194/ .
- M06: PR96, M02: PR95, M14: PR91, M03: PR85. **Nenhuma destas pesquisas contém decisão F6.**
