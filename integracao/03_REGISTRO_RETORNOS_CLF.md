# Solicitações entre Constituição e CLF

**ID:** CF-INT-003 · **Estado:** triagem preliminar; nenhuma solução material aprovada.

| ID | Problema | IDs históricos CLF | Módulos constitucionais | Estado |
|---|---|---|---|---|
| CF-IC-001 | Espécies normativas, procedimentos e viabilidade do Código único | IC-2026-010; IC-2026-026 | M00;M03;M14 | IDENTIFICADO |
| CF-IC-002 | Competência federativa e autonomia financeira | IC-2026-006 | M04;M05;M09 | IDENTIFICADO |
| CF-IC-003 | Recepção, transição e continuidade institucional | IC-2026-027; IC-2026-034 | M14;M03;M06 | IDENTIFICADO |
| CF-IC-004 | Direitos territoriais, titularidades e pluralismo | IC-2026-023 | M11;M04;M06 | IDENTIFICADO |

Cada solicitação deve trazer commits e datas dos dois projetos, fontes, hipótese, impacto, alternativas e resposta separada. Identificar interface não significa aprovar reforma.

## Retorno da terceira rodada M00.01 (13/10/2026)

A pesquisa documentou que a interface `CF-IC-001` não se resolve apenas por unidade editorial: preservar reserva de lei, competência nacional/federal, classe normativa, procedimento, delegação e rastreabilidade material. Dossiê: `modulos/M00-fundamentos/M00-01_04B_RESERVA_DE_LEI_E_DELEGACAO.md` e cenário `CF-TEST-M00-011` da matriz. **Status: IDENTIFICADO/PESQUISA; nenhuma solução transferida ou ratificada no CLF.** Comunicar à frente T01.M04 após resposta dos módulos constitucionais M03/M04/M14 e revisão da versão atualizada do CLF.

## Retorno de M00.02 v0.2 para o CLF (13/10/2026)

A matriz constitucional evoluiu de 53 para [74 registros de fontes do texto permanente](../modulos/M00-fundamentos/M00-02_INVENTARIO_RESERVAS_CF1988.csv) e [18 registros do ADCT](../modulos/M00-fundamentos/M00-02_ADCT_MATRIZ_TEMPORAL_v0.2.csv), com dependências fiscais até 2097. A [comparação de modelos](../modulos/M00-fundamentos/M00-02_ARQUITETURA_DE_FONTES_HIPOTESES_v0.2.md) distingue competência, espécie, procedimento, efeito, tempo e ato editorial. **Interface no CLF:** [issue #16 — T01.M04](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/16). Não alterar automaticamente a codificação nem importar qualquer arquitetura proposta como decisão.

## Pesquisa M03.01 e interface CLF — 13/10/2026

A revisão de alternativas do Parlamento e produção normativa foi aberta na [issue constitucional #18](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/18), com [dossiê](../modulos/M03-parlamento/M03-01_PROCESSO_LEGISLATIVO_E_ESPECIES_v0.1.md), [12 cenários de riscos](../modulos/M03-parlamento/M03-01_TESTES_PROCESSO_LEGISLATIVO.csv) e [10 exemplos de enquadramento material](../modulos/M03-parlamento/M03-01_TRIAGEM_MATERIAS_PROCEDIMENTOS.csv). Investiga lei comum, lei complementar, lei orgânica, mediação entre câmaras, iniciativa, urgência, impasse e despesas públicas. **Não há resultado normativo ratificado nem imposição ao CLF**. O T01.M04 deve exigir, para qualquer unidade editorial, proveniência e efeitos de cada parte sob sua espécie e competência constitucionais.

## Recepção de modelos de promulgação do Código uno — CF-IC-001 (13/10/2026)

O CLF T01.M04 produziu [seis modelos de promulgação, dois esboços constitucionais rivais e 18 testes](04_CODIGO_UNICO_MODELOS_PROMULGACAO_CLF.md) a partir do [PR CLF #18](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/18). O material foi **recebido apenas como hipótese de pesquisa**, para confrontação em M00.02/M03.01/M14, respeitando a matriz do próprio projeto constitucional de fontes, reservas e garantias.

**P3/CP:** procedimento coordenado que tentaria produzir texto positivo uno sem criar espécie nominal. **P4/CE:** espécie Código, com reserva material e iniciativas por componentes. Ambas **não aprovadas** e ainda têm pendências essenciais sobre forma do ato de integração, sanção/veto, bicameralismo, reedição C0 reservada, atualização e efeitos de promulgação incompleta. A existência dos arquivos **não transfere decisão jurídica** ao projeto CF. A linha `CF-IC-001` permanece `IDENTIFICADO/PESQUISA`.

## M04.01 — consentimento territorial e codificação (13/10/2026)

A pesquisa [M04.01](../modulos/M04-federacao/M04-01_CONSENTIMENTO_TERRITORIAL_E_IMPASSES_v0.1.md) identificou que a aprovação ou alteração de normas de **competência partilhada, partilha de receitas e obrigações locais** pode demandar participação institucional diferenciada no futuro sistema. A [triagem de 10 matérias](../modulos/M04-federacao/M04-01_TRIAGEM_CONSENTIMENTO.csv) e os [12 testes](../modulos/M04-federacao/M04-01_TESTES_IMPASSES.csv) não configuram escolha normativa. **CLF T01.M04:** preservar metadados por fonte/dispositivo sobre competência, procedimento, representação territorial, implementação financeira e transição; a reunião editorial não supre qualquer procedimento legislativo exigido. Interface ainda `PESQUISA` sem comando de alteração do Código.

## Teste CP/CE — simulação da origem à primeira alteração (13/10/2026)

O CLF [PR #19](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/19), integrado no commit `74aa56d2942d1499044fbf5256909692be904ece`, apresenta **72 estados** (CP/CE × componentes T/O/J × 12 fases) e **20 falhas adversariais**. [Nota de recebimento constitucional](05_SIMULACAO_CP_CE_VETO_E_ATUALIZACAO.md).

**Resultado limitado:** CP/P3 não definiu o ato jurídico de promulgação formalmente una; CE/P4 o nomeia, mas ainda **não** disciplina integralmente sanção/veto, bicameralismo, revogação dependente, controle e iniciativa não exercida. Vetos reais da **LC 236/2026** e o componente ordinário atual da **Lei 9.784/1999, art. 2º**, substituem exemplos históricos/desatualizados. A pesquisa M04.01 sobre consentimento territorial reforça exame de competência e participação federativa de cada componente. **CE/CP permanecem hipóteses H/A**, sem decisão constitucional ratificada.

## M05.01 — Encargos sem fonte e consolidação legislativa (13/10/2026)

O [dossiê M05.01](../modulos/M05-financas/M05-01_ENCARGOS_FINANCIAMENTO_EQUALIZACAO_v0.1.md) registra a **regra vigente do art. 167 §7º da CF/1988 (EC 128/2022)**, antes omitida no inventário, e diferencia previsão normativa de fonte, custeio plurianual, receita efetiva, transferência e execução. O [M00.02](../modulos/M00-fundamentos/M00-02_INVENTARIO_RESERVAS_CF1988.csv) recebeu entrada 75, corrigindo o registro anterior. A codificação CLF deve preservar a fonte original, as exceções, o conteúdo material e as referências ADCT/LRF e não tratar transferência de encargos como mera atualização editorial. **Interface em PESQUISA, sem reforma ou decisão ratificada**.

## Recepção V1/V2 — veto parcial e revogação dependente (13/10/2026)

O CLF [PR #20](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/20), integrado no commit `1d4fbd2ea3ba792b8c7137e9bb26b68a04b721e8`, fornece [dossiê V1/V2](06_VETO_E_REVOGACAO_DEPENDENTE_V1_V2.md), **24 cenários** e dois modelos normativos **não aprovados**. Distingue veto a dispositivo substitutivo, veto à cláusula revogatória e iniciativa judicial ausente. Caso real: [VET 48/2026](https://www.congressonacional.leg.br/pt_BR/materias/vetos/-/veto/detalhe/18651), que vetou trechos propostos para CTN art. 174 e a revogação do art. 44 §2º da Lei 9.430/1996; o veto permanecia **não apreciado** em 13/10/2026. **Não presumir relação causal entre os itens só porque constam do mesmo processo.**

**V1:** veto por unidades constitucionais com vínculo de eficácia pré-votado; alerta: a própria condição pode ser vetada. **V2:** veto de componente indivisível apenas como hipótese constitucional futura, com risco de veto estratégico. M03.01/M00.02/M14 devem avaliar sanção, veto, quórum, bicameralismo, iniciativa, direitos e continuidade, **coordenando-se com M04.01 e M05.01** sobre consentimento territorial e encargos financeiros. **CF-IC-001 permanece PESQUISA; nenhuma decisão normativa ratificada.**

## Teste V1: revogação e condição em unidade textual indivisa (13/10/2026)

A pesquisa [CLF PR #21](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/21), integrada no commit `189860ee90d24eb57c698c54b7a4bf04e090270d`, avaliou **4 minutas M0–M3 e 36 simulações** sobre art. 66 §2º da CF/1988, LC 95 e LINDB. [Dossiê CF-IC-001](07_V1_UNIDADE_DE_VETO.md). **M1/M2** (revogação e condição em artigo indiviso) mitigam veto isolado da condição, mas não o veto parcial ao substituto, nem resolvem derrubada tardia de veto, ausência de iniciativa judicial, não repristinação e promulgação una. **M0/M3** falham como modelos principais. M03.01/M14 devem testar remissões mínimas e datas de eficácia sem delegar poder normativo ao editor. Interface em PESQUISA, sem norma aprovada.

## Pesquisa empírica M05.02 e interface CLF (13/10/2026)

O [protocolo M05.02](../modulos/M05-financas/M05-02_PROTOCOLO_EMPIRICO_E_AUDITORIA_v0.1.md) estabelece controles de proveniência e competência para séries financeiras: identificador do ente, ano fiscal, fonte, espécie de transferência, estágio de execução, recebimento efetivo, retificação, metodologia e comparação temporal. A quebra de apresentação PAF em 2024 proíbe transposição ingênua de agregados antigos. **Interface apenas documental:** sem dados fiscais reais processados, sem alterar a CF ou impor regras novas ao CLF. O projeto legislativo deve preservar diferença entre repasses constitucionais gerais e transferências associadas a encargos legislativos concretos (CF art. 167 §7º).

## T01.M04 — concordância normativa e documental (ciclo 11, 13/10/2026)

A pesquisa [CLF PR #22](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/22) foi integrada à main CLF em `d9dadf0f11661cf7d1b040126fdf4700599b6f8b`. A nota [CF-INT-008](08_CLF_CONCORDANCIA_NORMATIVA_DOCUMENTAL.md) distingue N (ato legislativo promulgado), D (correspondência e provas sem efeito jurídico) e P (eventos publicados sem poder normativo). O CLF testou 12 nexos hipotéticos, 16 relações documentais e 20 cenários adversariais. A solução conservadora A/D usa artigos com revogação expressa e concordância explicativa; B, anexo normativo estático, continua **Q**, inclusive quanto à unidade de veto do art. 66 §2º e à enumeração exigida pelo art. 9º da LC95. Não se presume que linha de anexo seja unidade constitucional vetável. A opção de revogação por índice digital mutável foi rejeitada como hipótese. **CF-IC-001 PESQUISA, DEC-016 PENDENTE, nenhuma norma constitucional ratificada.**

## Recepção CLF ciclo 12: anexos normativos e cotejo textual (13/10/2026)

O [PR CLF #24](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/24), commit `12607cdd12c9ae677ea174cc5d54be133ccf7cd3`, trouxe três casos legislativos AN01 (veto art. 4º e anexo da Lei15.459/2026), AN02 (veto rejeitado e posterior promulgação de tabela no anexo da Lei14.724/2023) e AN03 (veto de dotações individualizadas da LOA2026, sob rito constitucional especial). [Devolutiva detalhada](09_ANEXOS_VETOS_AUDITORIA_LITERAL_CLF.md). Foram auditados 24 espelhos literais de LC95 e Lei9784, 11 eventos e 18 testes de contexto. A literalidade não prova C0 jurídico; nenhum texto novo foi promulgado. Veto de linha comum de tabela de revogações continua questão Q, sem analogia automática ao orçamento. CF-IC-001 segue pesquisa; CLF DEC-016 pendente.

## T07.M03 — primeiro piloto integral dos arts. 1º–2º da Lei 9.784/1999 (13/10/2026)

O CLF integrou o [PR #25](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/25), commit `fbc137173805a5d44d1b04a73c2a5c2fad1dd409`, com **21 unidades literais** (6 de art.1 e 15 de art.2), **16 dependências**, **30 contraprovas** e advertência contra revogar parcialmente arts. 1º–2º enquanto subsistem arts. 3º–70, sobretudo art. 69. [Devolutiva específica CF-IC-001](10_PILOTO_PROCESSO_ADMINISTRATIVO_CLF.md). O art. 1º, §1º, alcança outros Poderes da União em **função administrativa**; Súmula 633/STJ admite aplicação subsidiária estadual/municipal na ausência de norma local, não transformação automática em legislação nacional uniforme. `Esta Lei`→`este Código` pode ampliar indevidamente efeitos. **C0-T não é C0-J**, nenhum dispositivo promulgado ou revogado. `DEC-016` e `CF-IC-001` permanecem pendentes/em pesquisa.

## CLF T07.M03 — inventário integral por artigo e transcrição de arts. 3º–17 (13/10/2026)

O [CLF PR #27](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/27), integrado em `ed58554266a48b13f2f8a796c65651e268226a52`, acrescentou [devolutiva CF-IC-001](11_PILOTO_LEI9784_INVENTARIO_COMPLETO.md): **80 posições de artigo da Lei9.784** (49-C vetado integral), **16 eventos legislativos**, **50 vínculos relevantes** e **40 unidades literais dos arts.3º–17**. Com as 21 unidades já transcritas dos arts.1º–2º, há **61 unidades** em 17 artigos, todas `Q` em equivalência jurídica e **nenhuma promulgada**. STF SV5 demanda distinguir assistência facultativa no PAD de procedimentos especiais de defesa; regras de delegação dos arts.11–17 e veto da decisão coordenada preservam reservas constitucionais; competência federativa e subsidiariedade seguem testes. Inventário de 80 posições **não significa transcrição completa da lei**. `CF-IC-001` permanece PESQUISA; `DEC-016` do CLF pendente.

## CLF T07.M03 — ciclo 16: imparcialidade e intimações (14/10/2026)

O [CLF PR #28](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/28), commit `194bc08931fb24fdc7865e4790401baeef5f1b6d`, integrou **33 novas unidades literais** dos arts.18–28 da Lei9.784, **30 testes de veto, prazo, saneamento e defesa** e **20 dependências** (arts.26/27/28/41/49-D/59/66 e jurisprudência). **Acumulado textual: 94 unidades de 28 artigos**, sem certificação C0-J e sem norma promulgada. [Devolutiva detalhada](12_IMPARCIALIDADE_INTIMACAO_PROCESSO_CLF.md): STF/CF imparcialidade administrativa, STJ MS7.181/DF (suspeição ignorada) e Informativo Extraordinário 14/2024 (prejuízo real por intimação irregular); nenhuma tese permite eliminar intimação formal nem renúncia presumida do art.27. **CF-IC-001 PESQUISA; CLF DEC-016 PENDENTE**. O próximo cotejo será arts.29–47.

## CLF T07.M03 — ciclo 17: instrução, prova, pareceres, cautelares (14/10/2026)

**FEITO:** o [CLF PR #30](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/30) foi integrado à `main` no commit `e9f05f36f68d48db5b27dd0ea1ffab2e1626cc73`, com **28 unidades textuais** dos arts.29–47, **36 cenários adversariais** e **34 vínculos**. [Nota CF-IC-001](13_PROVAS_PARECERES_CAUTELARES_CLF.md) examina colaboração probatória oficial (29/36/37/38), participação e resposta (31/32/34), arquivamento sem confissão (39–41), diferença entre **parecer obrigatório vinculante e não vinculante** (42 §§1º/2º), laudos substitutivos (43), manifestação final (44), cautelar motivada em risco iminente com oitiva prévia diferida (45), privacidade (46) e competência para relatório/decisão (47). O conjunto T07.M03 soma **122 unidades textuais de 47 artigos**. **PENDENTE:** `C0-J` não provado, arts.48–70/intercalares não transpostos, `DEC-016` sem decisão. **PRÓXIMO:** arts.48–50, 49-A–G com vetos, depois 51–70; devolver interfaces M01/M03/M04/M06/M07/M14. `CF-IC-001` segue PESQUISA; nenhuma norma constitucional aprovada.

## CLF T07.M03 — ciclo 18: dever de decidir e decisão coordenada (14/10/2026)

**FEITO:** [CLF PR #33](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/33) integrado ao CLF (`9c84d9cc7e0c729b36b6fba2b81a59adec70f5e5`). A [devolutiva](14_DECISAO_COORDENADA_MOTIVACAO_CLF.md) examina dever de decidir (arts. 48–49), decisão coordenada (49-A a 49-G, exceto 49-C integralmente vetado), motivação (art. 50), seis registros históricos de vetos e a Súmula 674/STJ. **40 unidades textuais**, **36 simulações** e **30 vínculos**, com acumulado de **162 unidades** da Lei 9.784. **PENDENTE:** equivalência jurídica C0-J, conclusão dos arts. 51–70 e intercalares 64-A/B e 69-A, deliberação da forma do Código (DEC-016), qualquer decisão constitucional. **PRÓXIMO:** cotejo de recursos, decadência, especiais e transição. `CF-IC-001` continua pesquisa.
