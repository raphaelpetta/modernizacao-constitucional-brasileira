# Registro das rodadas e handoffs transversais

**ID:** CF-GOV-014 · **Política:** log **append-only lógico** de atividades de coordenação e marcos entre módulos. Subciclos materiais continuam a produzir pacote de continuidade próprio. Versões antigas ficam no histórico do Git; corrigir entrada por adendo com indicação, sem reescrever fatos passados.  
**Não é uma fila executada automaticamente:** a atividade só está concluída se o SHA/PR/link apontado realmente sustenta o resultado.

| Rodada | Data | Base lida | Entrega concluída ou em PR | O que permanece aberto | Próximo ato recomendado | Estado |
|---|---|---|---|---|---|---|
| CF-COORD-20261014-01 | 14/10/2026 | CF main `c82d41b8313c79a7c7b7d93b3a69269eb86a99c3`; CLF main `fbc137173805a5d44d1b04a73c2a5c2fad1dd409` (corte inicial) | Protocolo obrigatório CF-GOV-012, quadro CF-GOV-013, esta linha e registro de identificadores CF-GOV-015 criados em branch de governança; sincronização de instruções e checklist do PR ainda depende de concluir este PR | Conferência de concorrência/merge, PR #19 e #22, colisão PR #45, liberdades civis, abertura de M06/M09 e interface CLF | Após CI e merge de governança: sanear os PRs e abrir issues M06.01/M09.01/M01.12; atualizar estado com SHAs reais | EM_EXECUCAO |

## Modelo de nova entrada

`CF-COORD-AAAAMMDD-NN` | data e SHA exato da main | **FEITO** (com arquivo/PR/commit e distinção entre integrado e draft) | **PENDENTE** (incluindo CI/decisões V) | **PRÓXIMO** (tarefa executável e dependências) | situação.

Este log não substitui os pacotes de continuidade completos e não deve catalogar cada microcommit. Atualizar ao concluir **marcos transversais**, novas frentes, merges, bloqueios e mudanças relevantes de planejamento.  
**Controle de consistência:** se uma entrada disser "mergeado" e o PR ainda estiver aberto, corrigir antes de reportar ao usuário.

## Marco de encerramento parcial da coordenação — CF-COORD-20261014-02

**Data:** 14/10/2026. **Baseline final conferida CF:** `d346f71140656263216cdeb137a775e2b3fc73a9`; **CLF:** `7d0db6a63131b8d976b008adbb6d37e34c5c105f`. Estes hashes são fotografia após merges de governança/arquivo; podem evoluir.

**FEITO:** (a) regra transversal implantada na CF, PR #51 mergeado (`80f5e05d`); (b) igual regra implantada no CLF, PR #29 mergeado (`7d0db6a6`); (c) questões #53–57 abertas com escopos dedicados; (d) PR #58 mergeado (`d346f711`), fontes PR #19 arquivadas e PR #19 fechado sem merge; (e) PR #45 fechado sem merge por colisão, novo PR #59 H 0030/0031 aberto draft com CI estrutural success; (f) PR #22 continua draft, preservado para revisão crítica.

**PENDENTE:** atualização completa e jurídica da matriz N:N diante de `CF-NOR-0008–0020`, revisão das 29 pesquisas do PR #22 antes de merge, revisão M06/M07/M12 das novas cláusulas digitais, efetiva pesquisa F1–F5 M06.01/M09.01/M01.12, integração CF–CLF por casos concretos. Nenhuma norma H foi promovida a D, nem o usuário ratificou escolha material.

**PRÓXIMO:** iniciar pela **reconciliação jurídica incremental do PR #22** com as normas H atuais e preparar dossiês M06.01/M09.01, sem multiplicar identificadores ou quebrar fonte única. **Acompanhamento:** issue #53 e quadro `13_QUADRO_DE_COORDENACAO.md`.

**QA:** CF PR #51, #58 e #59 passaram na verificação estrutural de seus SHAs; CLF PR #29 teve CI estrutural success. Isso não certifica direito vigente, eficácia empírica, equivalência jurídica ou texto ratificado.

## CF-COORD-20261014-03 — Reconciliação e abertura de Justiça/Sociais

**Data:** 14/10/2026; **CF main de entrada `df689704613ab389bdbef4228857f162e66ae8cd`**, relida durante a rodada em `10374bf79927131d000710954d408ac98fbc1b49`; **nenhuma promoção H→D**.

**FEITO:** M01 dossiê de auditoria incremental e matriz 96×`CF-NOR-0001–0020` H e PR59 incluídos na branch do [PR #22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22) (31 arquivos), sem editar `redacao/`. Criados PRs de pesquisa [#62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62) — M06.01, 20 casos — e [#63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63) — M09.01, 24 casos. Ambos com dossiê, CSV, pacote e CI estrutural success. Atualizadas [issues #55](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/55) e [#56](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/56). Fonte legal oficial: CF/1988 EC139/2026; STF Temas 548,698,6,1234 (incluindo atualização 2026) e STJ Tema 1178.

**PENDENTE:** CI final do PR22 no último SHA, auditoria legal e empírica granular dos 96 grupos, revisão do PR59 por M06/M07/M12, estudos aprofundados M06/M09 e M05; PR22/59/62/63 draft, sem merge. Dispositivos `CF-NOR` vigentes no projeto permanecem H; **nenhuma deliberação material D**.

**PRÓXIMO:** primeiro estudo aprofundado de remédios judiciais e direitos trabalhistas/prestações sociais, com critérios de custas, legitimidade, prazo, financiamento e tutela; depois revisão crítica do PR22 em blocos jurídicos. A coordenação CF–CLF de provas/pareceres/cautelares deve ser encaminhada ao M06/M07.

## Marco CF-COORD-20261014-04 — remédios, direito do trabalho e colisão de ciclos

**Data:** 14/10/2026. **Base de entrada CF main:** `eaab37bcd5467d48db0cc0bda133c62ee7801ffe`. **Branches de pesquisa:** M06 PR62 e M09 PR63, sem merge.

**FEITO:** (i) M06.02, [issue #65](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/65): 1 dossiê, 12 funções, 22 cenários adversariais e handoff no PR62, CI estrutural success no `5ae0238d`; (ii) M09.02, [issue #66](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/66): 1 dossiê, 35 registros de art7, 11 funções arts8–11, 24 cenários e handoff no PR63, CI estrutural success no `41d381c5`; (iii) corrigida **colisão M01.12**: issue #49 coerção mantém M01.12, issue #54 liberdades renomeada M01.14.

**PENDENTE:** auditoria material de fontes e mérito, dados empíricos CNJ/Defensoria/mercado de trabalho, integração com M01 e CLF, parecer de proteção de dados PR59, M05 financiamento, ratificação constitucional. **PR62/63 permanecem em draft; pesquisas ainda não integradas à main.**

**PRÓXIMO:** parecer M06 ao PR59 sobre HD/acesso/tutela urgente e aprofundamento da negociação sindical M09.03; estudo quantitativo M09.04 com M05. Reservar identificadores antes de novas fichas. **Estado jurídico:** sem F6/D; nenhuma `CF-NOR` editada.

**Fontes-chave verificadas:** STF ADI4296 e Tema1046; STJ Tema1178; Constituição 1988 art5 e 7–11; Leis 12.016/2009, 13.300/2016, 9.507/1997, 4.717/1965; OIT NORMLEX 2026 e Declaração 1998/2022.

## CF-M01-20261014-12 — coerção e capacidade da RAPS (pesquisa inicial)

**Data:** 14/10/2026. **Main de entrada:** `50b498885e17fa1709e66b0861f40e5387b4f4b0`. **Issue:** #49 (M01.12); branch `pesquisa/m01-12-coercao-raps-f0f5-v01`. **Main de saída e PR/CI:** ver conferência de encerramento; não presumir merge prévio.

**FEITO:** preflight verificou que a colisão com M01.14 havia sido **resolvida por outra frente**; mantidos IDs, sem duplicação. Pesquisas sobre Lei 10.216, Lei 11.343 art. 23-A/Lei 13.840, LBI/CDPD, STJ Informativo 533 (precedente antigo), OMS/OHCHR e Comitê CDPD (orientações), dados nacionais/regionais RAPS 2025; dossiê M01.12, 22 cenários, 6 linhas oficiais agregadas e handoff. Nenhum CF-NOR novo nem ratificação D.

**PENDENTE:** revisão de jurisprudência posterior à LBI, dados individuais/agregados de internações e fiscalização, acesso territorial real, custos, pareceres M06/M09/M05, revisão humana de conclusões. **PRÓXIMO:** M01.12.02 na issue #49, indicadores e controles de internação, não novo ciclo colidente. **QA:** script de estrutura verificará esquemas e soma das regiões, mas não validade jurídica nem causalidade clínica. [Continuidade M01.12](../modulos/M01-direitos-fundamentais/M01-12_PACOTE_CONTINUIDADE_v0.1.md).

## CF-COORD-20261014-05 — Parecer dados/remédios e sindicalismo/greve

**Data:** 14/10/2026. **Base de entrada:** CF main `50b498885e17fa1709e66b0861f40e5387b4f4b0`; **main conferida ao preparar registro:** `8cc7e0b572d77e4f8889243afa06d1e01a062394` (avanço paralelo da interface CF–CLF). Pesquisas em PRs draft, sem merge editorial nesta rodada.

**FEITO:** (i) parecer M06 à redação H privacidade/dados PR59, `M06-02_PARECER_INTERFACE_PRIVACIDADE_PR59_v0.1.md`, 16 testes e 10 critérios, arquivos no PR62; PR59 e issue #57 receberam vínculo. (ii) [Issue #68](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/68) M09.03 aberta, dossiê, matriz de 14 escolhas e 20 testes + handoff no PR63. (iii) fontes atuais: CF/LGPD/Lei9507/ADI6387/6649 e STF Temas935 (ED nov2025, atos 2026),1046,531; OIT C87 não, C98 ratificada; Lei7783. (iv) **PR62 9 arquivos e PR63 12**, ambos CI estrutural success nos HEADs `e3c49cd2` e `7852866f`, sem conflitos. Não editados `redacao/propostas` nem a `main` em pesquisa.

**PENDENTE:** reservas especiais de domicílio/comunicações, remédio constitucional de dados, parecer M07/M12, acórdãos integrais, estatísticas e custos reais M05, decisão sobre unicidade versus pluralismo, atualização final dos recursos Tema935. PR22/59/62/63 seguem draft; H não é D.

**PRÓXIMO:** testar alternativas H de garantias especiais de privacidade e habeas data (sem duplicar M01/M06) e comparar integralmente A unicidade democratizada vs B pluralismo sindical representativo com custo/transição M05; verificar compatibilidade dos procedimentos administrativos CF–CLF com M06/M07.

**Validação:** CI de estrutura não constitui exame jurídico, resultado empírico ou ratificação.

## CF-M01-20261014-12-02 — Dados de fiscalização, RAPS e precedente processual

**Entrada:** `5ac08b622d7552b7d3b37a695a3027b4b9d827d4`. **Issue:** #49 M01.12, código reservado e sem colisão; **branch:** `pesquisa/m01-12-02-indicadores-fiscalizacao-v01`. **PR e SHA de saída:** verificar GitHub após integração, sem afirmação antecipada de aprovação.

**FEITO:** pesquisados MPMG SIAPI, MPRJ MSM 2.0 e MPSP, SIH, CNES, RAPS, SISMAC, portaria CAPS 2025, CNJ Res. 487 e STJ REsp 2.228.271 (competência, não autorização material); dossiê, 15 fontes, 14 indicadores, 5 valores autorizados e testes automatizados de integridade. A soma de cinco CAPS é R$ 331.468 mensal e R$ 3.977.616 anualizada, **não pagamentos efetivos**. Não houve coleta de bases institucionais nominais nem dados regionais de coerção comprovados.

**PENDENTE:** pedidos agregados não enviados, resposta de órgãos públicos, séries territoriais baixadas, comprovação de revisão por juiz/Defensoria, cobertura dos notificadores, recursos pagos, resultados clínicos, prova de equivalência jurídica.

**PRÓXIMO:** M01.12.03 sob issue #49, dados agregados e pareceres transversais M06/M09/M05, com proteção a dados sensíveis. **Nenhuma CF-NOR nova e nenhuma decisão F6/D.**

## CF-COORD-20261014-06 — alternativas M01.13 e simulações M09.03

**Data de corte:** 14/10/2026. **Base inicialmente consultada:** CF main `5ac08b622d7552b7d3b37a695a3027b4b9d827d4`; **releitura final antes do quadro:** main `48166d04ff85634dfd70caa2de549ed866e6591e` (pesquisa M01.12.02 integrada por outra frente). **Não se editou** `redacao/` nem documentos M01.12 nesta rodada.

**FEITO:** [PR #59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59), draft, recebeu 3 arquivos: modelos A/B/C de cláusulas especiais para domicílio, interceptação, aparelho e remédio gratuito de dados; 20 casos adversariais, pacote; STF Temas280/977 de 2015/2025 verificados com limites/exceções. `CF-NOR-0030` e `0031` H **não foram editadas**. [PR #63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63), draft, recebeu modelos institucionais A unicidade auditável e B pluralismo representativo, contramodelo C, 16 casos paramétricos e handoff; França/México comparados; IBGE PNAD 2024 8,9% filiação **não mede representação/negociação**. Ambos passaram CI estrutural nos heads `fecd6d46` e `d344293b`, limpos na verificação; [issues #57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57) e [#68](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/68) receberam continuidade.

**PENDENTE:** integração de pesquisa (PR59/63 ainda draft), revisão jurídico-material e complementos E de domicílio, comunicações e habeas data; proteção diante de acesso a celular segundo distinções Tema977; revisão M06/M07/M12; dados de custos, filiação/representatividade sindical e atualização Tema935; nenhuma aprovação material D.

**PRÓXIMO:** (1) M01.13/M06/M07/M12 elaborar variante reconciliada de reservas e tutela de dados com exame de direitos de terceiros, manter unificada a fonte `redacao/` quando vier a existir ficha H; (2) M09/M02/M05 submeter modelos A/B a análise setorial/financeira, garantir liberdade de organização, mandatos e participação de não filiados. Revalidar SHA, PR e ID ao começar.

**QA:** GitHub Actions verifica estrutura e caminhos, não eficácia jurídica, direito vigente futuro, votação sindical real ou dados empíricos. Nenhuma norma existente promovida de H para D.

## CF-COORD-20261014-07 — Minuta DOM/COM/HD e teste setorial A/B

**Data:** 14/10/2026. **Main consultada:** `e648bd71227f407f2b46207e9c8d546a255254d2`; PR59/63 atualizados em branches próprias e ainda draft, sem alteração da `redacao/` canônica na main.

**FEITO:** (1) [PR59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59): dossiê P de três especialidades propostas E-DOM/E-COM/E-HD, matriz de 24 garantias CF e 24 cenários, handoff; Tema280/977, CF art5, Leis9296/9507 e LGPD, CI success HEAD `222aed01c02df926e2fd139fe0abb5428b08bb9b`. Nenhuma `CF-NOR` criada nem `0030/0031` modificada. (2) [PR63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63): oito perfis sindicais A/B, 24 casos, dicionário de 17 dados/fontes/ausências e pacote; IBGE PNAD2024, MTE CNES/Mediador e comunicado 169 entidades, CI success `da79467a3c6bb0f205864dfe1bd89534c54bd6c5`. (3) Criada [issue #76](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/76) de interface M02/M05 — representação eleitoral/custos de certificação; issues #57 e #68 atualizadas.

**PENDENTE:** equivalência material à CF/1988 (domicílio, sigilo, HD), revisão do trecho digital de exceções com M06/M07/M12, acórdãos integrais; votos, cobertura de acordos, custeio real de sindicatos e órgão público, execução por setor, direitos de minorias e transição de modelos; nenhuma decisão material D.

**PRÓXIMO:** revisar exceções digitais de E-COM e montar Parecer M06/M12 sobre HD/fluxo/armazenamento; estudar indústria e domésticos como pilotos A/B com denominadores de participação e custo M05, sem inventar coeficientes fiscais.

**Qualidade:** os 48 registros de matrizes para M01 e os 49 registros de M09 (8+24+17) são **classificações/testes de documentação**, não pessoas, direitos revogados ou estatística de eficácia. CI apenas estrutural, pesquisas draft.
