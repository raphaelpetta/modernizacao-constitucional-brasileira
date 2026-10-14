# M12.01 — Pacote obrigatório de continuidade (14/10/2026)

**Base de entrada:** main `b9dbdc540310ed5dc34fb1e5f314c46af343dc98`. **Issue:** [#80](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/80), M12.01 formalmente reservada. **Branch:** `pesquisa/m12-01-investigacao-digital-tema977-v01`. **Estado:** pesquisa independente V/P/A; não decisões D, não CF-NOR. **Referência cruzada:** [PR59 M01.13](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59), [PR62 M06.02](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62).

## FEITO
- Parecer próprio `M12-01_PARECER_INDEPENDENTE_PROVA_DIGITAL_v0.1.md`, fundado nas funções constitucionais de investigação de M12 (polícias, segurança, inteligência), sem presumir aprovação por M01/M06/M07.
- Três controles independentes: **L** legalidade da obtenção/interceptação; **I** integridade e mesmidade técnico-pericial; **C** contraditório e acesso útil à prova. Cada um pode falhar separadamente.
- Direito vigente: STF Tema977 (CAP, IDF, ACE, PRE e modulação), CF5 X/XII/LVI/LV/LXXIX; STJ **Jurisprudência em Teses 281, 03/06/2026** (dados estáticos de conexão != interceptação; integridade auditável) e **AgRg no AgRg no HC1041340/RS, Quinta Turma, abril/2026**, direito de defesa a exame técnico adequado em caso concreto. Distinção entre ilicitude, quebra de integridade, nulidade e prejuízo, sem regra absoluta falsa.
- Revisão independente das variantes P3-E/P3-R do M06 e **terceira opção P3-S** (exceção material mínima sujeita a limites e preservação técnica; ainda com remissões incompletas e riscos apontados). Não há escolha material.
- Matriz `M12-01_MATRIZ_LEGALIDADE_INTEGRIDADE_CONTRADITORIO.csv` com **24 cenários** jurídicos conceituais, não decisões empíricas ou dados de polícia.
- Não criados novos IDs CF-NOR, não editado PR59 nem dispositivos H. O catálogo identifica M12 com Defesa/segurança/emergência e investigação, mas o parecer é estudo, não acórdão ou consulta externa.

## PENDENTE
- Parecer cruzado M06/M07 e M01 sobre L/I/C, e decisão material se a Constituição admite exceção identificadora atual ou prefere reserva mais estrita; **a redação atual de P3-S não supera integralmente os portões de segurança**.
- Inteiro teor/votos de decisões que divirjam quanto a acesso técnico e documentação da prova; eventual evolução de embargos Tema977; delimitação legal de preservação forense sem exploração ilícita.
- Tratamento de nuvem, metadados de provedores, acesso penal x administrativo, custo de perícia, direito das vítimas e proteção de dados de terceiros; cadeia de custódia em CLF e medidas de acesso da defesa.
- Verificação QA estrutural deste PR no HEAD final. CI estrutural NÃO comprova exatidão jurídica ou equivalência constitucional.

## PRÓXIMO
**Prioridade:** confrontar a variante P3-S e P3-E com o parecer M06, **corrigir de forma expressa o perímetro do encontro fortuito** e as técnicas de preservação sem ampliar acesso; exigir revisão do M07 quanto a dados administrativos e da M06 quanto ao contraditório antes de texto H. Construir concordância N:N entre CF5 X/XII/LV/LVI/LXXIX, Tema977 e minuta E-COM. Só preparar CF-NOR com reserva e decisão material explícita.

**Coordenação:** issue #80, PR draft M12 e links ao PR59/PR62; main de saída a confirmar na integração documental separada. 


## Atualização após abertura do PR de pesquisa
**FEITO:** [PR #82](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/82) aberto como draft, abrangendo parecer próprio de M12.01 e matriz de 24 cenários. **PENDENTE:** opinião cruzada M01/M06/M07, acórdãos e custos, nenhuma hipótese ratificada D. **PRÓXIMO:** devolver resultados à issue #80 e PRs #59/#62, respeitando o bloqueio de E-COM e a fonte normativa única. CI do último SHA a verificar.

## M12.01-R2 — Redline P4 e STJ 2026 (14/10/2026)

**FEITO:** `M12-01_REDLINE_P4_EXCECAO_E_CADEIA_CUSTODIA_v0.1.md` criou duas alternativas de revisão detalhadas: **P4-E** (exceção identificadora do celular encontrado fortuitamente, estrita em sujeito/fato/finalidade, com registro e revisão) e **P4-R** (exige ordem judicial até para essa finalidade, como opção material mais restritiva). `M12-01_TESTES_REDLINE_P4.csv` = **18 ataques**. Pesquisa STJ: JTes281 03/06/2026, Informativo879 AgRg HC1014212/ES (dúvida razoável exige perícia), RHC237288/AM (15/09/2026, publicação 21/09/2026) sobre necessidade de indício concreto e contraditório; proíbe conclusões opostas falsas de nulidade automática por todo vício e validação de prova ilícita por integridade perfeita. **Nenhuma ficha CF-NOR criada, nenhuma opção D**.
**PENDENTE:** colisão do conceito de encontro fortuito com flagrante, perícia de conservação de conteúdo e sigilo de terceiro, revisão cruzada M06/M07/M01, acórdãos integrais e infraestrutura plantão, não regressão N:N.
**PRÓXIMO:** registrar feedback ao PR59/62, reunir M06/M07 em redação P5 sem circularidade e submeter a deliberação consciente E/R antes de qualquer reserva de ID. CI HEAD a conferir; PR82 permanece draft.
