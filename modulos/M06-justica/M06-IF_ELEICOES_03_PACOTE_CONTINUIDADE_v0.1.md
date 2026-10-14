# M06-IF-ELEI-003 — FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026 · **Issue M06:** #55 · **PR draft M06:** [#96](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/96), branch `pesquisa/m06-interface-controle-eleitoral-20261014` · **base main:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Interfaces:** M03 #84 / PR85 (alternativa B é P de pesquisa, NÃO D), M14 #90 / PR91, M02 #14 / PR95, M04 #21, M05 #25, M12; CF-GOV-016 PR97. Todas branches de pesquisa **não integradas**.
**Estado:** F0–F5/F8, H/P/A/V; nenhuma decisão D/F6, F7 CF-NOR, alteração `governanca/03_DECISOES.md`, `main` ou CLF.

## FEITO
1. `M06-IF_ELEICOES_03_PARECER_ARTICULADO_TESTE_PARLAMENTARISMO_B_ART60_v0.1.md`: primeira análise concreta, porém **somente semântica e funcional H**, de 16 pontos da hipótese **B parlamentarismo racionalizado** da M03.02.05 B1–B6, confrontados com art.60§4 I–IV, ADI 2.024 (núcleo essencial e não congelamento literal), ADI 7.350 (periodicidade eleitoral), MS20.257/34.722/37.721/38.596 da M06-IF-ELEI-002. **NÃO é texto de PEC nem CF-NOR.**
2. `M06-IF_ELEICOES_03_MATRIZ_16_CLAUSULAS_B_H_ART60.csv`: 16 BH-01..BH-16, com fontes M03, melhor defesa, pior redação, indícios materiais e prova F6 pendente. **Triagem = 5 DEFENSAVEL_CONDICIONAL, 9 ALTO_RISCO_SE_ABUSIVO, 2 INDETERMINADO_SEM_TEXTO.** Não equivale a votos, probabilidades, julgamento de constitucionalidade ou aprovação da alternativa B. Toda cláusula F6 ABERTA.
3. `M06-IF_ELEICOES_03_MATRIZ_8_CONTRAEXEMPLOS_NUCLEO.csv`: oito abusos X01..X08, em especial veto discricionário de chefe Estado à investidura, dissolução por LOA, juiz condicionado ao gabinete, retirada autonomia municipal/estadual, transformação de presidente eleito em chefe simbólico durante mandato, gasto caretaker sem base, estado de exceção sem fim e bloqueio de minoritário sob censura construtiva. Oito classificados H, diferenciando **risco pétreo se efetivamente textual/comprovado** de risco político sem abolição evidente.
4. `M06-IF_ELEICOES_03_CHECKLIST_10_PROVAS_ANTES_DA_PEC.csv`: dez K01–K10 **todas ABERTAS**; primeira Câmara, título presidencial, consulta R-CON1/2, art16, direitos oposição, Judiciário independente, receitas federativas, defesa e orçamento.
5. `scripts/validar_m06_if_eleicoes_03_pec_b.py`: QA estrutural reproduzível. **Auditoria JS INDEPENDENTE realmente executada diretamente sobre conteúdo dos três CSV no GitHub: PASS** 16/8/10, dimensões 10/9/7, IDs completos, nenhuma célula vazia e 16 cláusulas F6/10 portas ainda ABERTAS. Python criado, mas não alegar execução individual dele no workflow sem prova.
6. **Resultado jurídico de maior valor:** a hipótese B **não pode ser refutada meramente por envolver Governo dependente de Câmara**, nem validada por supor que art60§4 protege só nomes de cargos. A cláusula pétrea protege o **núcleo essencial** de federação, voto, separação e direitos. **Riscos mais agudos aparecem na transição retroativa de mandato presidencial, poder de dissolução eleitoral, tutela de juiz/câmaras, financiamento sem Parlamento e autonomia dos entes**; a censura construtiva e B2, em isolamento, suscitam inicialmente dilemas de governabilidade, sem prova de supressão inequívoca do núcleo. STF **não julgou PEC parlamentarista concreta** aqui nem conferiu obrigatoriedade/dispensa definitiva de consulta (MS22.972 extinto sem mérito).

## PENDENTE
- **M03:** só há cláusulas funcionais H, sem redação constitucional real, seleção material, quóruns, prazos e chefia de Estado definida. Sem texto, MS parlamentar contra ato legislativo não tem réu ou ato coator concreto. Não pedir julgamento ex ante de toda forma de governo.
- **M02/M14:** art16, primeira eleição, EC111 (5/1/2027 presidencial) e CF57§4 (Câmara nova a partir de 1/2), preservação do mandato eleito; TR-PROS P, não D.
- **M04/M05/M12:** autonomia e receitas, caretaker/LOA/caixa, defesa e emergência, sem soluções F6.
- **M06:** critérios de legitimidade/cabimento do MS para PEC real versus controle posterior da EC, efeitos de eventual núcleo suprimido, texto novo da jurisdição, eventual plebiscito obrigatório R-CON1/2 controvertido.
- **A/C continuam abertos e não são inferiores por conclusão do M06:** só B foi triada por ser protótipo P preexistente na M03.05; não houve escolha do usuário.
- **CI/mergeabilidade:** conferir SHA final, workflow efetivo e PR draft; sucesso CI não demonstra constitucionalidade do modelo.

## PRÓXIMO
**M03 F6-00, SOMENTE SE houver manifestação expressa substantiva:** escolher protótipo A, B ou C de **pesquisa**, ou manter todos, ou escolher definitivamente em D F6 mediante resposta dos módulos; então formular um texto **concreto de cada competência** para teste material M06/M02/M14. **Se nenhuma deliberação for emitida, próxima pesquisa deve procurar um novo impasse factual/documental e não repetir matrizes hipotéticas**. Não produzir CF-NOR por simples “bora”.

## FONTES
- STF CF art60 §4 ADI2024, ADI7350: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=60&abrirBase=CF
- STF MS preventivo de PEC: ver M06-IF-ELEI-002 e seu catálogo 10 precedentes, PR96.
- CF art16: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=16&abrirBase=CF
- CF texto: https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm
- EC111: https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc111.htm
- Lei 9709: https://www.planalto.gov.br/ccivil_03/leis/l9709.htm
- M03.02.05 B1–B6 e M03.02.12 — PR85 draft, nenhum F6.