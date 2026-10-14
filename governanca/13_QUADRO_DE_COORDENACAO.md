# Quadro de coordenação das frentes — fotografia verificada

**ID:** CF-GOV-013 · **Atualização:** 14/10/2026 · **Main de referência:** `c82d41b8313c79a7c7b7d93b3a69269eb86a99c3`.  
**ATENÇÃO:** fotografia, **não estado em tempo real**. Antes de decidir/mesclar, ler o SHA atual e a situação das issues/PRs, especialmente `redacao/indice.csv`. A numeração CF-NOR abaixo é a dessa referência, não uma reserva para outro ciclo.

## 1. Regra de leitura

- **Integrado na main:** existe como arquivo versionado, **não** aprova materialmente conteúdo constitucional.
- **PR draft:** pesquisa ou proposta ainda não incorporada.
- **H/P/A/V:** hipóteses/propostas/questões/verificações; **D:** apenas diretriz ratificada segundo `03_DECISOES.md`.
- **Próximo:** uma atividade verificável, não mera intenção. A cada mudança relevante registrar no `14_REGISTRO_DAS_RODADAS.md` ou handoff.

## 2. Frentes, entregas e próximos atos

| Frente | Estado na fotografia | Entrega verificada | Próximo trabalho prioritário | Dependências |
|---|---|---|---|---|
| **M00 — Teoria/fontes** | pesquisa `main` | M00.01 reserva constitucional; M00.02 fontes e reservas; M00.03 redação integrada, geração, CI | Completar inventário por dispositivo e preparar decisões sobre lei, delegação e tratados | M03/M04/M06/M13/M14 |
| **M01 — Parte geral** | H em `main` | CF-NOR 0003–0007; regime geral e 16 garantias em piloto | Reconciliar PR22, não presumir cobertura dos remédios | M00/M06/M09 |
| **M01 — Igualdade** | H em `main` | CF-NOR 0008–0011, dossiê/matriz de 16 garantias | Conciliar com M01.06 no PR22, testar lacunas CDPD/leis | M06/M09/M11/M13 |
| **M01 — Vida e bioética** | H em `main`, ciclo M01.11 em andamento | CF-NOR 0012–0017; M01.10 matriz de 20; índice atual já inclui **0018–0020** capacidade/diretivas/involuntariedade | Terminar auditoria específica M01.11 e revisar impacto CDPD/saúde/justiça | M05/M06/M09/M12 |
| **M01 — Privacidade/dados** | pesquisa PR22, proposta conflitante PR45 | M01.08 (28 testes; 18 registros digitais); #45 antigo 0012/0013 já ocupados | **Não mesclar #45**; reconstruir com IDs livres sobre main atual ou preparar texto novo após reserva | M06/M07/M12 |
| **M01 — Liberdades civis** | pendência M01.12 (nome a reservar) | lacunas identificadas pela auditoria transversal M01.09 | Abrir dossiê próprio sobre expressão, consciência, religião, informação, reunião, associação e circulação | M02/M06/M08/M12 |
| **M02 — Eleições** | planejado; issue #14 | salvaguardas preliminares M00 | Dossiê M02.01 sobre integridade e restrições oportunistas antes de fórmulas eleitorais | M03/M06/M14 |
| **M03 — Parlamento e governo** | pesquisa; issue #18 | M03.01 processo legislativo, 12 testes, 10 triagens | Cruzar iniciativa/veto com modelos CLF e camadas normativas M00 | M00/M04/M05/M14 |
| **M04 — Federação** | pesquisa; issue #21 | M04.01 participação territorial e tipos T0–T3, 12 testes/10 triagens | Confrontar competências e objeções com M03/M05, sem aprovar Câmara alta | M03/M05/M07/M14 |
| **M05 — Finanças** | pesquisa; issues #25/#29 | M05.01 encargo/equalização; M05.02 10 fontes, validador e testes sintéticos | Coletar, harmonizar e validar dados fiscais reais por município-ano antes de conclusão empírica | M04/M09/M05 |
| **M06 — Justiça e tutela** | sem dossiê próprio integrado | dependências e proteções processuais inventariadas em M01 | Abrir M06.01: remédios constitucionais, tutela coletiva, processo/controle constitucional e legalidade penal em interfaces | M01/M12/M13 |
| **M07 — Administração** | planejado | interfaces digitais, fiscais e CLF | Abrir estudo de boa administração e decisões administrativas/digitais; integrar CF-IC-001 | M01/M04/M06/CLF |
| **M08 — Economia** | planejado | direitos propriedade/mercado em matrizes M01 | Abrir pesquisa de propriedade, função social e prestação privada de serviços | M01/M04/M09 |
| **M09 — Direitos sociais e trabalho** | sem dossiê próprio integrado | garantias sociais/financiamento identificados M01/M05 | Abrir M09.01: mapa material arts. 6º–11 e 194–230, fontes de custeio e direitos exigíveis | M01/M04/M05/M06 |
| **M10 — Ambiente** | planejado | direito intergeracional listado | M10.01 ambiente/clima e deveres dos poderes e privados | M04/M08/M11 |
| **M11 — Povos** | planejado | direitos territoriais/capacidade coletiva inventariados | M11.01 proteção originária, consulta, autonomia e tutela | M01/M04/M06/M10 |
| **M12 — Segurança/emergência** | planejado | reservas de polícia e prisão inventariadas | M12.01 liberdade e força, necessidade, emergência e controle | M01/M06/M14 |
| **M13 — Internacional** | planejado | hierarquia e CDPD em estudos M00/M01 | M13.01 tratados, recepção, hierarquia e controle | M00/M01/M14 |
| **M14 — Reforma/transição** | planejado | efeitos ADCT/recepção já identificados | M14.01 proteção de direitos, reforma e etapas de implementação | todos |
| **CF ↔ CLF** | interface documentada `main` | CF-IC-001: Lei 9784 e devido processo; CLF T01.M04/T07.M03 | Triagem bilateral por competência, veto, processos e alcance territorial, sem transformar hipótese legal em CF decidida | M00/M03/M04/M06/M07/M14 |

## 3. Repositórios/PRs em coordenação

- **CF:** https://github.com/raphaelpetta/modernizacao-constitucional-brasileira .
- **CLF:** https://github.com/raphaelpetta/codigo-legislacao-federal .
- **#19 CF:** PR draft com dois arquivos iniciais de M01.01 em base antiga. **Supersessão de escopo provável, não equivalência documental comprovada**; preservar pesquisa útil antes de encerrar.
- **#22 CF:** PR draft, 29 arquivos de pesquisa M01.01–M01.09; contém protocolo de comparações e 96 conjuntos em fotografia **anterior às H 0008–0020**; revisão incremental necessária.
- **#45 CF:** PR draft de privacidade/dados com IDs **0012–0013 já utilizados na main**. **BLOQUEADO PARA MERGE**; original deve ficar registrado, recriação sobre `main` com ID próprio.
- **#44 CF:** fechado sem merge por primeira colisão de numeração.
- **M01.10 #43 e M01.11 #47:** frentes já identificadas, não reutilizar seus nomes para liberdades civis.
- **M06/M09:** sem issues dedicadas na fotografia, abertura prioritária com escopo cruzado.

## 4. Conflitos de interface que exigem uma só decisão

| Dúvida | Módulo de condução | Revisores funcionais | Bloqueia o quê |
|---|---|---|---|
| Reservas de lei e delegação | M00 | M03/M06/M13 | reservas substantivas de poderes e direitos |
| Liberdades e legalidade penal | M01 + M12 | M06 | restrições, sanções e garantias especiais |
| Remédios judiciais | M06 | M01/M09/M11 | afirmar equivalência de tutela geral |
| Proteção digital e fiscalização | M01 (direito) / M07 (autoridade) | M06/M08/M12 | aprovar CF-NOR proteção de dados completo |
| Encargos, competência e receita | M04/M05 | M03/M09 | definir distribuição fiscal |
| Prestação social sem fonte | M09/M05 | M04/M06 | concluir execução e exigibilidade |
| Mudança da CF com CLF | M00/M03/M14 | CLF T01.M04/T07.M03 | alterar vigência e revogação |
| Propostas repetidas e IDs | coordenação M00.03 | todos autores afetados | qualquer merge editorial colidente |

## 5. Decisões e qualidade

Nenhuma norma `CF-NOR-0001–0020` da fotografia recebeu status `D`. O registro de decisões mantém diretrizes gerais e as decisões históricas do guia com proveniência diferenciada. Não deliberar forma de governo, eleições, Câmara alta, Justiça ou tributação apenas porque estudos já existem.

**Próxima atualização deste quadro:** após saneamento de PR #45 e abertura M06/M09, ou quando a main mudar estruturalmente. Toda nova rodada deve fazer handoff mesmo se este quadro ainda não tiver sido editado.

## Adendo verificado de saneamento (14/10/2026; main base `d346f71140656263216cdeb137a775e2b3fc73a9`)

**Prevalece sobre fotografias anteriores nas matérias específicas indicadas**; ainda assim, conferir GitHub em tempo real antes de novas operações.

- **Governança:** [PR #51](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/51) foi integrado (commit `80f5e05d3ce772c856ecf20e6b3231b0c7989e37`). Protocolo de FEITO/PENDENTE/PRÓXIMO passou a valer nos canais e templates.
- **Catálogo antigo M01:** [PR #58](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/58) integrado (commit `d346f71140656263216cdeb137a775e2b3fc73a9`), com cópia histórica integral dos arquivos do PR #19 e [concordância M01](../modulos/M01-direitos-fundamentais/M01-00_CONCORDANCIA_PR19_PR22_PR45.md); **PR #19 fechado sem merge**, não houve perda de fonte.
- **Pesquisa corrente:** PR #22 **permanece draft** (29 arquivos). Sua revisão jurídica, confronto incremental com `CF-NOR` H e eventual integração ainda são **pendências**, não fatos concluídos.
- **Privacidade e dados:** antigo PR #45 **fechado sem merge por colisão**. Nova [issue #57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57) e [PR #59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59) em **draft** apresentam `CF-NOR-0030` e `0031` H, reservados; CI estrutural **success** no head `62161a6b9eb7dc62aad6efe4c914b1bd85fee411`, PR clean na leitura. Ainda não mergeado nem auditado materialmente.
- **Issues de frentes abertas:** [#53 coordenação](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/53), [#54 M01.12 liberdades](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/54), [#55 M06.01 tutela e remédios](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/55), [#56 M09.01 direitos sociais](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/56), [#57 M01.13 privacidade](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57). Ter issue aberta **não é pesquisa F1–F5 concluída**.
- **CLF:** [PR #29](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/29) integrado (commit `7d0db6a63131b8d976b008adbb6d37e34c5c105f`), padronizando continuidade, sem ratificação legislativa.

**Próximo marco prioritário:** auditar PR #22 à luz das H realmente na main e abrir o primeiro dossiê efetivo M06.01/M09.01; o PR #59 deve receber revisão material antes de qualquer merge. Evitar chamar questões abertas de decisões.

## Adendo de execução — 14/10/2026: auditoria M01 e abertura efetiva M06/M09

**SHA da main relida:** `10374bf79927131d000710954d408ac98fbc1b49` (integrações CF–CLF avançaram em paralelo; nenhum dispositivo constitucional foi modificado nesta rodada).

| Frente | Feito no PR, não ainda na main | Pendente | Próximo |
|---|---|---|---|
| **M01.09 auditoria jurídica/integrativa** | [PR #22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22), agora **31 arquivos**: dossiê incremental + correspondência N:N dos **96 grupos** do inventário original com 20 propostas H e PR59. Classificação provisória: **7 parcial específico, 68 geral não equivalente, 16 sem especial na main, 5 somente em PR59**. | Revisão jurídica granular por conjunto, testes de não regressão e integração dos pareceres de M06/M09; **nenhuma equivalência material certificada** | Revisar blocos de garantias de processo e trabalho com M06.01/M09.01 |
| **M06 Justiça, tutela e remédios** | [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62), **draft**, 3 arquivos: dossiê, 20 testes e continuidade; CI estrutural success | Avaliação de HC, MS, MI, HD e popular por instituto, custos e dados CNJ; M06 sem texto H | M06.02 candidato, detalhe de legitimidade, prova, custas e execução |
| **M09 Sociais e trabalho** | [PR #63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63), **draft**, 3 arquivos: dossiê, 24 testes e continuidade; CI estrutural success | Art. 7º inciso a inciso e efeitos financeiros; dados reais M05, entes e transição; M09 sem texto H | M09.02 candidato, direitos trabalhistas e materialidade M09.03 |
| **Privacidade M01.13** | [PR #59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59) permanece proposta redacional H 0030/0031, não na main | Revisão das reservas de domicílio/comunicações e tutela de dados pela nova M06.01 | Parecer cruzado M06/M07/M12 antes de eventual merge |
| **CF ↔ CLF** | main CF recebeu estudo sobre provas/pareceres/cautelares T07.M03 via CF-IC-001 no commit `10374bf7` | Confrontar processo administrativo de CF, M06 e CLF antes de redigir regras gerais de boa administração | Interface M07 e M06 sobre devido processo administrativo |

**Nota:** status documental `PESQUISA` de M06/M09 refere-se a trabalhos em **PR draft**, não integração à main, nem decisão material. **Atualizar este quadro apenas em marcos relevantes**.

## Adendo — 14/10/2026: M06.02/M09.02 e reconciliação de M01.12

**Main de referência inicial:** `eaab37bcd5467d48db0cc0bda133c62ee7801ffe`. **Atenção:** estes trabalhos de pesquisa constam em branches/PRs draft, NÃO foram incorporados à main; consultar HEAD antes do merge.

| Frente | FEITO em PR (não na main) | PENDENTE | PRÓXIMO |
|---|---|---|---|
| **M06.02 — remédios** ([issue #65](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/65)) | [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62) agora abrange M06.01–02; dossiê, **12 funções de tutela** e **22 testes especializados** adicionais; fonte ADI4296, leis HC/MS/MI/HD/popular, gratuidade. GitHub Actions success em `5ae0238d9e0eb3dfbc42a179267d35bfe3abfe26`. | Inteiro teor de acórdãos, números CNJ/Defensoria, prova de equivalência, crítica ao PR59 de dados, M07/CLF. | Emitir parecer M06 ao PR59; avaliar M06.03 de tutela coletiva/execução. |
| **M09.02 — trabalho** ([issue #66](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/66)) | [PR #63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63) agora abrange M09.01–02; **35 registros art7** (34 incisos + PU), **11 funções arts8–11**, **24 testes especializados** adicionais, OIT/STF Tema1046. CI success em `41d381c569e42ce7e974fb8018de86badf9c6710`. | CLT/ADCT e dados reais de custos/horas, representatividade sindical e limites à negociação, M05; não existe CF-NOR M09. | M09.03 negociação/sindicatos/greve, M09.04 pisos/jornada com dados M05. |
| **M01.12 / M01.14** | **Colisão de ciclo resolvida administrativamente:** a [issue #49](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/49), mais antiga, mantém `M01.12` para coerção em saúde; a [issue #54](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/54) de liberdades civis foi reidentificada **M01.14**, preservando escopo e histórico. | F1–F5 de ambas as frentes, sem normas novas. | Iniciar as pesquisas pela issue responsável correspondente. |

**Classificação:** consulta a fontes primárias, testes adversariais documentais, **nenhuma decisão material D**. A atualização de nomenclatura M01 é operacional, não revisão de direitos constitucionais. A integridade dos arquivos foi testada, **não** sua exatidão jurídica integral.

## Adendo M01.12 — pesquisa inicial em coerção e RAPS (14/10/2026; entrada main `50b49888`)

**Correção de identificadores já efetuada anteriormente pela coordenação, não repetida neste ciclo:** [#49](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/49) permanece **M01.12 (coerção e saúde mental)**, [#54](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/54) é **M01.14 (liberdades)** e #57 é M01.13 (privacidade). 

**FEITO em PR de pesquisa, sem CF-NOR nova:** [dossiê M01.12](../modulos/M01-direitos-fundamentais/M01-12_COERCAO_EM_SAUDE_RAPS_ALTERNATIVAS_v0.1.md), [22 cenários](../modulos/M01-direitos-fundamentais/M01-12_MATRIZ_TESTES_E_CONFLITOS.csv), [RAPS 2025 oficial com transcrição agregada e soma auditada](../modulos/M01-direitos-fundamentais/M01-12_RAPS_2025_FONTE_OFICIAL.csv) e [continuidade](../modulos/M01-direitos-fundamentais/M01-12_PACOTE_CONTINUIDADE_v0.1.md). A Lei 10.216/2001 e o art. 23-A da Lei 11.343/2006 têm **garantias/setores distintos**. O dado oficial de 6.281 soma categorias heterogêneas (CAPS + SRT/UA + leitos) e NÃO é medida de internações coercitivas.

**PENDENTE:** jurisprudência contemporânea pós-LBI; defesa e revisão periódica, indicadores municipais de coerção/atendimento, custos e fiscalização, opinião de afetados, pareceres M06/M09/M05. **PRÓXIMO:** M01.12.02, pilotar indicadores territoriais agregados e critérios de devido processo sob a mesma issue #49. Nenhuma escolha A/B/C/D ou norma H ratificada. A versão deste quadro é fotografia, consultar PR e main reais antes de trabalhar.

## Adendo — 14/10/2026: parecer M06 para privacidade e pesquisa M09.03 sindical

**Base mais recente da main lida:** `8cc7e0b572d77e4f8889243afa06d1e01a062394`, commit concorrente sobre **CF–CLF: decisão coordenada/motivação (CF-IC-001)**. **Não envolve ratificação de normas CF-NOR.** Quadro é fotografia datada, ler main e PRs novamente em rodada posterior.

| Frente | FEITO (com localização) | PENDENTE | PRÓXIMO |
|---|---|---|---|
| **M06 ↔ M01.13 privacidade/dados** | [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62), **draft** com 9 arquivos, incluiu `M06-02_PARECER_INTERFACE_PRIVACIDADE_PR59_v0.1.md` e CSV de **16 testes**. Parecer aponta **10 critérios** de reservas art5 XI/XII, habeas data art5 LXXII/LXXVII, dados estatais, algoritmos/autoridade, baseado em CF/LGPD/Lei9507, sem equivalência certificada. [PR #59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59) e [issue #57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57) receberam feedback sem editar CF-NOR 0030/0031 H. CI estrutural success no PR62 head `e3c49cd2361d4da82e7d8c4895b7c1d60cba8cf2`. | Normas H especiais de reserva de domicílio/interceptação, remédio de dados e revisão M07/M12; precedentes integrais e prova de tutela equivalente | M01.13/M06/M07/M12 devem cotejar modelos de salvaguarda e decidir onde pesquisar a especialização, **sem merge/ratificação prematuros** |
| **M09.03 sindicatos/negociação/greve** | [Issue #68](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/68) e [PR #63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63), **draft** com 12 arquivos, novo dossiê, **14 escolhas** SIND01–14 e **20 testes**. STF Temas 935/1046/531; OIT C98 ratificada, C87 não; Lei7783; comparação A/B/C. CI success no head `7852866f7db4a542f810d6ec67e5ab08ec19c4e8`. | Microdados de sindicalização e financiamento, votação/representação por setor, jurisprudência integral e atualização recursal do Tema935; M02/M05/M06/M08/M13/CLF | Simular **unicidade democratizada vs pluralismo representativo**, custeio/oposição e transição com participação de M05/M02 |
| **CF–CLF** | main avançou para `8cc7e0b5`, recebendo na integração CF-IC-001 estudo sobre decisão coordenada/motivação do processo administrativo do CLF, com 40 unidades experimentais, vetos, testes e dependências, segundo mensagem de commit | Compatibilidade com tutela M06 e processo administrativo M07 | Encaminhar estudo ao M07/M06, sem importar alterações do CLF como escolhas constitucionais D |

**Controle:** PRs #22/#59/#62/#63 seguem draft e não integrados na main; nenhuma `CF-NOR` material ratificada. Resultados de teste são estruturais, e cenários são testes conceituais, não evidência empírica.

## Entrega M01.12.02 — fiscalização e fontes territoriais (14/10/2026)

**FEITO em PR documental:** [dossiê](../modulos/M01-direitos-fundamentais/M01-12_02_AUDITORIA_FISCALIZACAO_E_RAPS_v0.1.md); [15 fontes oficiais](../modulos/M01-direitos-fundamentais/M01-12_02_CATALOGO_BASES_E_CONTROLES.csv); [14 indicadores](../modulos/M01-direitos-fundamentais/M01-12_02_DICIONARIO_INDICADORES.csv); [5 valores de uma portaria CAPS 2025](../modulos/M01-direitos-fundamentais/M01-12_02_AMOSTRA_PORTARIA_CAPS_2025.csv). SIAPI/MPMG, MSM 2.0/MPRJ e MPSP podem subsidiar notificação/alta, mas não foi obtida base abrangente; RAPS/CNES/SIH e SISMAC têm funções diferentes. STJ 2.228.271/ES é **processual**; CNJ 487 restringe-se ao escopo **penal/segurança**. Nenhuma CF-NOR ou decisão material D, manter PR22/59/62/63 em draft até verificação de status real.

**PENDENTE:** agregados de notificações e sua cobertura, acesso de pessoas a revisão/defesa, série de uso da RAPS, repasses efetivos, dados atualizados de mérito STJ/STF, auditoria jurídica pós-LBI, interlocução com pessoas afetadas. **PRÓXIMO:** M01.12.03 **na issue #49**, com pedido institucional agregado adequado à LGPD, harmonização do CNES e parecer M06/M09/M05, antes de qualquer cláusula adicional. SHA da main e PR devem ser conferidos na abertura da próxima rodada.
