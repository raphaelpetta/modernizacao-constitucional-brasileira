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
