# M06-IF-ELEI-004 — FEITO / PENDENTE / PRÓXIMO
**Corte 14/10/2026 · Issue M06 #55 · PR [#96](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/96), draft · branch `pesquisa/m06-interface-controle-eleitoral-20261014` · base main `2a770a8136f8ca4877e865be3e3b7745a6d4b168`**. Fontes M03 [PR85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85), M02 [PR95](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/95), M14 [PR91](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/91), CF-GOV [PR97](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/97), todos estudos em branches independentes NÃO integrados. **Estado F0–F5/F8 H/P/A/V; nenhuma D/F6/F7, CF-NOR, CLF, edição de main ou seleção de sistema.**

## FEITO
1. `M06-IF_ELEICOES_04_CONTROLE_SIMETRICO_A_B_C_ART60_v0.1.md` documenta exame equitativo **A (presidencialismo reformado)**, **B (parlamentarismo racionalizado)** e **C (semipresidencialismo premier-presidencial)**, extraindo A1–A5/B1–B6/C1–C5 do parecer M03.02.05 no PR85 e relacionando a art60§4 I–IV. B fora tratado separadamente na M06-IF-ELEI-003 (16 cláusulas H), **não transformar as contagens de 16 e 12 em ranking comparativo**.
2. `M06-IF_ELEICOES_04_MATRIZ_12_COMPARACOES_SIMETRICAS_A_B_C.csv`: **12 dimensões idênticas S01–S12**, três alternativas por linha, ataques comuns, diferença específica e prova exigida. **Todas as 12 ABERTAS** porque não existem textos constitucionais promulgados ou escolhas normativas de A/B/C.
3. `scripts/validar_m06_if_eleicoes_04_simetria.py`: verificador **estrutural** para reexecução, NÃO parecer jurídico. **QA independente efetivamente executada em JS buscando o CSV do GitHub:** PASS 12 linhas x 11 colunas, três opções sempre preenchidas, IDs únicos/ordenados, nenhuma célula vazia, 12 status ABERTA. Não afirmar que a CI executou especificamente Python sem log.
4. **Novos controles jurídicos:** (i) a ausência de voto popular direto para premier eleito pela Câmara NÃO implica automaticamente supressão de sufrágio direto de parlamentares, mas a **transformação/extinção do cargo presidencial eleito diretamente** suscita pergunta própria sobre art60§4 II, art77, 1993 e direitos de mandato, ainda A/V. (ii) A mantém legitimidade presidencial, porém decretos ilimitados e submissão do Judiciário ameaçam III/IV. (iii) C mantém eleição presidencial e precisa disciplina clara de competências, assinatura, defesa, diplomacia, orçamento e dissolução, sob pena de duplo governo. (iv) L2/L3 derrota de LOA é um impasse genérico a todas arquiteturas, não exclusividade de B. (v) STF ADI2.024 protege o núcleo essencial, sem chancelar A/B/C.
5. **Comparadores oficiais verificados:** França Constituição arts8,12,20,21,49/50 (Légifrance); Portugal Constituição arts133,186,187,195(2) (Assembleia da República/Tribunal Constitucional). Portugal admite demissão presidencial EXCEPCIONAL para normal funcionamento das instituições, não transcrever como livre demissão do PM em C da pesquisa. França tem art49(3) para lei financeira, **não copiar** para resolver orçamento no Brasil.
6. **Resultado metodológico:** GO para levar à M03 F6-00 as melhores objeções simétricas e buscar especificamente parecer de voto presidencial DIRETO/mandato transicional, competências de presidente C e controle de decretos A; NO-GO para escolher A/B/C em nome do usuário, promulgar ou escrever CF-NOR por “bora”.

## PENDENTE
- **M03:** decisão F6 expressa de modelo e texto real de poderes Executivo/Legislativo para permitir exame material de um dispositivo, não apenas rótulo A/B/C.
- **M02/M14:** possibilidade jurídica e limites de eventual supressão/reconfiguração da eleição PRESIDENCIAL direta no futuro sistema B e respeito ao mandato já eleito; CF16, EC111/2021 e CF57§4.
- **M06:** examinar art60§4 II especificamente frente ao cargo presidencial atual (art77), garantia de voto popular e plebiscito de 1993 sem declarar resposta do STF inexistente; MS preventivo só em PEC/ato real e legitimado congressista.
- **M03.01/M05:** governo em funções, orçamento, autorização legislativa, crédito e caixa nos 3 sistemas.
- **M04/M12:** preservação da federação, defesa, emergência e cadeia única de comando, especialmente em C.
- **Comparação institucional:** sem teste de texto real não há classificação de constitucionalidade definitiva, superioridade empírica, porcentagem de riscos ou obrigação jurídica definitiva de plebiscito R-CON1/2.

## PRÓXIMO
**Prioridade de maior informação:** parecer jurídico M02/M06 sobre **substituição da escolha presidencial direta** e direito de voto no contexto de reforma do sistema de governo; depois aplicação do art60 ao texto concreto selecionado em F6. Se não houver modelo escolhido, registrar pendência sem produzir novas variantes fictícias e sem decidir constitucionalidade de A/B/C. Comunicar corrigendas às issues M03/M02/M14.

## FONTES
- CF arts14,16,60§4,77 e 82: https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm
- STF ADI7350 voto periódico: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=57&abrirBase=CF
- STF art60 e núcleo essencial: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=60&abrirBase=CF
- França: https://www.legifrance.gouv.fr/loda/texte_lc/LEGITEXT000006071194/
- Portugal: https://www.parlamento.pt/Legislacao/Paginas/ConstituicaoRepublicaPortuguesa.aspx
- M03.02.05 (PR85) e M06-IF-ELEI-003 (PR96), ambos sem F6.