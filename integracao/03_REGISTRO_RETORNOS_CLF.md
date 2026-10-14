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
