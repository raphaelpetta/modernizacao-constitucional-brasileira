# M06-IF-ELEI-002 — FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026 · **Issue responsável:** M06 #55 · **PR draft:** #96, branch `pesquisa/m06-interface-controle-eleitoral-20261014`; **main preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Interfaces:** M02 #14 PR95, M14 #90 PR91, M03 #84 PR85, CF-GOV-016 PR97 — todos drafts, nenhum desses materiais foi integrado à main.
**Fase:** pesquisa jurídica H/P/A/V, F6/D/F7 NÃO concluídos, sem CF-NOR, CLF ou alteração de main. Este é segundo estudo de interface M06, não M06.03 formal, não confundir PR96 com PR62 de remédios M06.01/02.
## FEITO
1. `M06-IF_ELEICOES_02_PARECER_ESPECIFICO_PEC_ART60_PAR4_STF_v0.1.md`: **resolver lacuna substantiva identificada na reconciliação**: há jurisprudência colegiada específica de mandado de segurança de parlamentar contra PEC supostamente tendente a abolir cláusulas pétreas. O MS20.257 (Plenário 1980) admitiu a via mas indeferiu segurança; o MS24.667 AgR (Plenário 2003) delimita legitimação parlamentar; MS34.722 AgR (Plenário 2019) aplica limites formais, circunstanciais e materiais art60; MS37.721 AgR (Turma 2022) confirma cabimento em tese de MS material preventivo contra PEC de imunidade parlamentar; MS38.596 (Plenário 2024) exige afronta inequívoca para impedir discussão parlamentar e **denegou segurança** sobre PEC206/2019 de educação, preservando controle de norma promulgada. **Distinguir cabimento, concessão cautelar, mérito e homologação de constitucionalidade**.
2. **Razão jurídica:** o art60§4 diz que proposta tendente a abolir núcleo protegido **não será objeto de deliberação**, hipótese qualificada em que vício se materializa na própria tramitação; isso difere de controle material preventivo genérico de PL (MS32.033) e da ADI de emenda já promulgada. Não cabe converter Lei/regimento em cláusula pétrea apenas por discordância (MS34.722) nem atribuir legitimação MS parlamentar a qualquer cidadão.
3. **Efeito de tempo:** MS21.648, MS22.487 e decisão posterior do MS34.448 mostram que a promulgação pode retirar legitimidade/objeto do MS de parlamentar, que **não se transforma em ADI**. Não afirmar que ajuizamento preventivo valida ou invalida a futura emenda; após promulgação aplicar cabimento novo e legitimados art103.
4. **Dissenso identificado:** parecer PGR no MS32.036/2014 tentou rever cabimento de controle preventivo material, **não é decisão do STF**; cautela MS32.036/37 sobre PEC33 teve **liminar negada** sem referida aprovação colegiada do mérito. MS34.448/507 decisões individuais não substituir acórdãos 2019/2022/2024.
5. `M06-IF_ELEICOES_02_MATRIZ_10_PRECEDENTES_PEC.csv`: dez entradas, colegialidade, questão, holding, resultado e **tipo de evidência** oficial/republicada, para não confundir Plenário, Turma e liminar.
6. `M06-IF_ELEICOES_02_CHECKLIST_8_PORTAS_CABIMENTO_MS.csv`: oito barreiras de cabimento ainda ABERTAS para **PEC concreta** e autoridade/ato existentes; não aprovar consulta plebiscitária, roteiro de posse, poderes de chefe Estado ou CF-NOR.
7. `scripts/validar_m06_if_eleicoes_02_pec.py` versionado. **QA independente realmente EXECUTADA em JavaScript**, buscando e decodificando CSV direto do GitHub: PASS, 10/8, 11/8 colunas, cinco precedentes-chave presentes, oito portas ABERTAS e nenhum campo vazio. Não afirmar execução individual do script Python pela CI sem prova.
8. Fontes utilizadas preferencialmente ementas STF no LexML, portal de jurisprudência anotada e comunicados oficiais STF; acórdãos mais novos de 2019/2022/2024 conferidos por ementas/inteiros teores republicados com atribuição, **não inventar URL ou afirmar conferência de PDF STF original**.

## PENDENTE
- **Texto da PEC A/B/C e normas eleitorais**: ainda não existe proposta constitucional concreta em F6; não declarar incompatibilidade material da troca de governo ou plebiscito obrigatório. STF MS22.972 foi extinto sem mérito e consulta R-CON1/R-CON2 continua controvertida.
- **Cabimento no futuro sistema judicial**: se Constituição alternativa modificar legitimados, remédios ou revisão judicial, deverá ser deliberado em M06/M03, sem supor automaticamente atual STF, Turma ou art103.
- **Verificação aprofundada**: inteiro teor oficial STF dos MS34.722, MS37.721 e MS38.596 quando se redigir peça ou parecer normativo final; o resumo foi verificado em republicações e portal STF, mas não se pode fingir acórdão oficial PDF acessado.
- **M14/M02**: o parecer de controle preventivo não substitui análise de consulta Lei9709, art16 e primeira investidura.
- **Governança**: checar CI/HEAD após commits; este PR96 continua draft e não altera PR97 ou PR95/91 diretamente. O documento anterior M06-IF-ELEI-001 deve receber NOTA DE ADITAMENTO referindo nova jurisprudência, sem sobrescrever o raciocínio original.

## PRÓXIMO
1. Devolver à issue M06 #55 a correção: **não falta precedente específico**; falta **texto concreto A/B/C e prova de inequívoca violação de núcleo material**, com oito portas ainda abertas.
2. Encaminhar ao CF-GOV-016 PR97/issue M14 #90 correção de status da tensão “PEC sem precedente”: deve mudar para **resolvido quanto ao CABIMENTO** e **não resolvido quanto ao mérito de reforma hipotética**; não alterar PR97 sem integração própria.
3. Se houver formulação F6 do sistema de governo, fazer exame artigo a artigo de limitações art60 e direitos de voto, em vez de fabricar mais casos. Não usar MS de parlamentar para buscar aprovação prévia do texto inteiro do projeto.

## FONTES DE REFERÊNCIA
- STF temático: https://portal.stf.jus.br/publicacaotematica/vertema.asp?lei=5235
- LexML MS20.257: https://www.lexml.gov.br/urn/urn:lex:br:supremo.tribunal.federal;plenario:acordao;ms:1980-10-08;20257-1450184
- LexML MS24.667: https://www.lexml.gov.br/urn/urn:lex:br:supremo.tribunal.federal;plenario:acordao;ms:2003-12-04;24667-3573536
- STF 2016 MS34.448: https://noticias.stf.jus.br/postsnoticias/ministro-barroso-mantem-tramitacao-da-pec-dos-gastos-publicos-na-camara-dos-deputados/
- MS34.722 ementa republicada: https://www.jusbrasil.com.br/jurisprudencia/stf/768218522
- MS37.721 republicação: https://www.jusbrasil.com.br/jurisprudencia/stf/1652522800/inteiro-teor-1652522801
- MS38.596 ementa de acórdão no clipping órgão público: https://escolasuperior.rr.def.br/wp-content/uploads/2025/04/CLIPPING_DEZ_2024.pdf .