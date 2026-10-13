# Estado operacional — leitura obrigatória no início de cada chat

**ID:** CF-GOV-004 · **Versão:** implantação v0.1 · **Data:** 13/10/2026.

## Objetivo
Constituição brasileira modernizada com liberdade de reconstrução e auditoria interdisciplinar. A CF/1988 é direito vigente; o anteprojeto de 2026 e o guia-mestre são registros históricos, não texto obrigatório.

## Estado verificado
- Repositório privado: https://github.com/raphaelpetta/modernizacao-constitucional-brasileira
- `main` = versão integrada. Cada chat deve registrar o SHA efetivamente lido.
- Guia-mestre histórico arquivado em `referencias/guia_mestre_constitucional_v0.1.md`.
- Texto do anteprojeto antigo arquivado em `referencias/anteprojeto_constitucional_v0.1_texto.md`; o PDF original permanece no pacote inicial para eventual depósito binário.
- Metodologia funcional, validação automática de estrutura e catálogo inicial de 15 módulos: proposta operacional de pesquisa, não divisão final do texto constitucional.
- CLF: https://github.com/raphaelpetta/codigo-legislacao-federal ; interface já documentada naquele repositório em `docs/09_INTERFACE_CONSTITUCIONAL.md`. A matriz de 34 interfaces refere-se à minuta constitucional v0.1, não ao projeto novo como definitivo.

## Não decidido
Sistema de governo, mecanismo eleitoral, desenho de Câmara alta, repartição fina de competências, finanças federativas, Justiça constitucional, conteúdo de reservas normativas, regimes territoriais, reforma constitucional e regras de transição. Todas as hipóteses antigas podem ser reexaminadas.

## Situação dos módulos
M00: **PESQUISA EM CURSO**, subciclo M00.01 (F0 delimitada; F1 verificação normativa focalizada e F3 comparação inicial, ambas não exaustivas; F4/F5 triagem de problemas e alternativas em andamento). Dossiê inicial `modulos/M00-fundamentos/M00-01_RESERVA_CONSTITUCIONAL_E_FONTES.md`; pesquisa ampliada `modulos/M00-fundamentos/M00-01_PESQUISA_COMPARADA_E_CRITERIOS_v0.2.md` (integração PR #10, commit `fed09101315e0733390b911e186c50759bdee7d8`). Triagem adicional de 20 conjuntos da CF/1988, com [matriz e dossiê M00.01](../modulos/M00-fundamentos/M00-01_AUDITORIA_20_CASOS.md), sem juízo de cobertura exaustiva. Terceira rodada: [três filtros e testes adversariais](../modulos/M00-fundamentos/M00-01_04_ROTEIRO_DELIBERACAO.md), com frentes eleitoral, reserva normativa e proteção de direitos; **12 cenários documentados**, sem aprovação de opção constitucional. Questões de reserva legal, tipologia legislativa e hierarquia ainda como hipóteses; issue #4 segue aberta. M01–M14: **PLANEJADO**. Nenhum módulo auditado nem texto constitucional material ratificado.

## Pesquisa M00.02 — reservas e delegações (13/10/2026)

Iniciado subciclo `M00.02` na [issue #15](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/15), com [dossiê de taxonomia e alternativas](../modulos/M00-fundamentos/M00-02_DOSSIE_FONTES_E_RESERVAS_v0.1.md) e [matriz inicial de 53 registros normativos](../modulos/M00-fundamentos/M00-02_INVENTARIO_RESERVAS_CF1988.csv). **Estado: TRIAGEM DOCUMENTAL, NÃO INVENTÁRIO EXAUSTIVO**. Matérias, reservas de LC/lei, competências, iniciativa e delegação classificadas para aprofundamento jurídico. **Atualização v0.2 em 13/10/2026:** [74 registros permanentes](../modulos/M00-fundamentos/M00-02_INVENTARIO_RESERVAS_CF1988.csv) (21 novos), [18 entradas ADCT com classificações temporais](../modulos/M00-fundamentos/M00-02_ADCT_MATRIZ_TEMPORAL_v0.2.csv) e [análise de modelos de fontes A–D](../modulos/M00-fundamentos/M00-02_ARQUITETURA_DE_FONTES_HIPOTESES_v0.2.md). Versão CF até EC 139/2026, sem escolha constitucional aprovada. Nova questão: efeitos de atos normativos próprios, resoluções do Senado, controle jurisdicional vinculante e transições até 2097. Ainda faltam o conjunto da CF/1988 e ADCT, atos infraconstitucionais de execução, efeitos temporais e jurisprudência completa. Nenhum desenho constitucional material foi homologado. O verificador estrutural confere IDs, módulos e campos básicos desse catálogo.

## Próxima trilha
1. Validar o contrato metodológico e proveniência das antigas diretrizes.
2. Fazer M00: natureza constitucional, hierarquia, reservas, competências e direitos como estrutura do sistema.
3. Fazer M01: teoria geral de direitos, aplicabilidade, limitações e mecanismos de tutela.
4. Rodada curta de M03–M05: mapa de dependências do sistema político/federativo/fiscal, ainda sem fixar soluções.
5. Iniciar matriz sistemática CF/1988 × problemas × novas decisões, distinguindo mera ausência textual de regressão real.

## Revisões
Atualizar esta síntese ao final de integração substancial. Referências de versão devem apontar commits, nunca a mera memória da conversa.
