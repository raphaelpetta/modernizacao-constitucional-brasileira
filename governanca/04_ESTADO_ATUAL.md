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
M00: **PESQUISA EM CURSO**, subciclo M00.01 (F0 delimitada; F1 verificação normativa focalizada e F3 comparação inicial, ambas não exaustivas; F4/F5 triagem de problemas e alternativas em andamento). Dossiê inicial `modulos/M00-fundamentos/M00-01_RESERVA_CONSTITUCIONAL_E_FONTES.md`; pesquisa ampliada `modulos/M00-fundamentos/M00-01_PESQUISA_COMPARADA_E_CRITERIOS_v0.2.md` (integração PR #10, commit `fed09101315e0733390b911e186c50759bdee7d8`). Triagem adicional de 20 conjuntos da CF/1988, com [matriz e dossiê M00.01](../modulos/M00-fundamentos/M00-01_AUDITORIA_20_CASOS.md), sem juízo de cobertura exaustiva. Terceira rodada: [três filtros e testes adversariais](../modulos/M00-fundamentos/M00-01_04_ROTEIRO_DELIBERACAO.md), com frentes eleitoral, reserva normativa e proteção de direitos; **12 cenários documentados**, sem aprovação de opção constitucional. Questões de reserva legal, tipologia legislativa e hierarquia ainda como hipóteses; issue #4 segue aberta. M01–M02 e M05–M14: **PLANEJADO**; **M03 e M04: PESQUISA INICIADA**, questão #18, com [dossiê M03.01](../modulos/M03-parlamento/M03-01_PROCESSO_LEGISLATIVO_E_ESPECIES_v0.1.md), [12 testes adversariais](../modulos/M03-parlamento/M03-01_TESTES_PROCESSO_LEGISLATIVO.csv) e [10 casos de enquadramento de matérias](../modulos/M03-parlamento/M03-01_TRIAGEM_MATERIAS_PROCEDIMENTOS.csv). F0 delimitada; F1/F2/F3/F4/F5 parciais, sem deliberação. Nenhum módulo auditado nem texto constitucional material ratificado.

## Pesquisa M00.02 — reservas e delegações (13/10/2026)

Iniciado subciclo `M00.02` na [issue #15](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/15), com [dossiê de taxonomia e alternativas](../modulos/M00-fundamentos/M00-02_DOSSIE_FONTES_E_RESERVAS_v0.1.md) e [matriz inicial de 53 registros normativos](../modulos/M00-fundamentos/M00-02_INVENTARIO_RESERVAS_CF1988.csv). **Estado: TRIAGEM DOCUMENTAL, NÃO INVENTÁRIO EXAUSTIVO**. Matérias, reservas de LC/lei, competências, iniciativa e delegação classificadas para aprofundamento jurídico. **Atualização v0.2 em 13/10/2026:** [74 registros permanentes](../modulos/M00-fundamentos/M00-02_INVENTARIO_RESERVAS_CF1988.csv) (21 novos), [18 entradas ADCT com classificações temporais](../modulos/M00-fundamentos/M00-02_ADCT_MATRIZ_TEMPORAL_v0.2.csv) e [análise de modelos de fontes A–D](../modulos/M00-fundamentos/M00-02_ARQUITETURA_DE_FONTES_HIPOTESES_v0.2.md). Versão CF até EC 139/2026, sem escolha constitucional aprovada. Nova questão: efeitos de atos normativos próprios, resoluções do Senado, controle jurisdicional vinculante e transições até 2097. Ainda faltam o conjunto da CF/1988 e ADCT, atos infraconstitucionais de execução, efeitos temporais e jurisprudência completa. Nenhum desenho constitucional material foi homologado. O verificador estrutural confere IDs, módulos e campos básicos desse catálogo.

## Pesquisa M04.01 — consentimento e objeção territorial (13/10/2026)

Iniciado módulo **M04: PESQUISA**, questão [#21](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/21). [Dossiê de consentimento e impasses](../modulos/M04-federacao/M04-01_CONSENTIMENTO_TERRITORIAL_E_IMPASSES_v0.1.md), [12 testes adversariais](../modulos/M04-federacao/M04-01_TESTES_IMPASSES.csv) e [10 simulações de procedimento conforme matéria](../modulos/M04-federacao/M04-01_TRIAGEM_CONSENTIMENTO.csv). Comparação jurídica Alemanha (consentimento e objeção), África do Sul (classificação, mediação e superação), Suíça (consulta precoce) e França (mediação), com ADIs 1842 e 6341 e exemplo brasileiro do CGIBS/IBS. **F0 delimitada; F1–F5 parciais, sem escolha material.** T0 (consulta), T1 (objeção superável), T2 (consentimento forte) e T3 (reforma constitucional) são hipóteses de classificação; nenhum desenho de câmara territorial, representação municipal, quórum ou forma de governo foi ratificado. 

## Pesquisa M05.01 — encargo e equalização (13/10/2026)

M05 passou a **PESQUISA**. [Dossiê M05.01](../modulos/M05-financas/M05-01_ENCARGOS_FINANCIAMENTO_EQUALIZACAO_v0.1.md), [12 testes de estresse](../modulos/M05-financas/M05-01_TESTES_ENCARGOS.csv) e [6 hipóteses numéricas ilustrativas](../modulos/M05-financas/M05-01_SIMULACAO_ILUSTRATIVA.csv). **Correção material importante:** identificou-se omissão prévia do **art. 167 §7º da CF, introduzido pela EC 128/2022**, que já contém regra expressa contra transferência ou imposição por lei de encargos financeiros de serviços públicos sem fonte ou transferência correspondente, ressalvados casos textuais. Foi incluído como [registro 75 do inventário M00.02](../modulos/M00-fundamentos/M00-02_INVENTARIO_RESERVAS_CF1988.csv) e [adendo M04.01](../modulos/M04-federacao/M04-01_CONSENTIMENTO_TERRITORIAL_E_IMPASSES_v0.1.md). Fontes oficiais e casos STF ADI 7222/Tema 1132 analisados com ressalvas processuais. A pesquisa contábil comparada é preliminar; **não existem estimativas empíricas reais ou escolha normativa ratificada**.

## Pesquisa M05.02 — verificação das fontes e pipeline reproduzível (13/10/2026)

A [issue #29](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/29) avançou para **VERIFICAÇÃO DOCUMENTAL E INSTRUMENTAÇÃO DE ANÁLISE**, não coleta municipal concluída: [protocolo M05.02](../modulos/M05-financas/M05-02_PROTOCOLO_EMPIRICO_E_AUDITORIA_v0.1.md), [10 fontes oficiais catalogadas](../modulos/M05-financas/M05-02_CATALOGO_FONTES.csv), [esquema municipal vazio](../modelos/M05_02_ESQUEMA_NORMALIZADO.csv), [auditor descritivo](../scripts/m05_02_auditar_dados.py) e [testes sintéticos](../tests/test_m05_02_auditar_dados.py). Fontes Tesouro FINBRA, CKAN FPM/Fundeb, Boletim, SIOPS, SIOPE e IBGE foram conferidas por documentação e metadados; **CSVs oficiais não foram baixados/reconciliados**, portanto não há medidas fiscais reais, médias municipais ou estimativas de lacuna. O CI verifica esquema, IDs e comportamento sintético; não confundir isso com validação empírica ou escolha constitucional. Quebra metodológica do PAF em 2024 registrada. Estado de M05 permanece PESQUISA; conclusão substantiva da issue #29 segue aberta.

## Abertura de redação experimental integrada — M00.03 (13/10/2026)

Auditoria documental identificou que a metodologia F0–F8, os IDs `CF-NOR`, a classificação D/P/H/A/V, a auditoria de garantias e a continuidade Git estavam implantadas, **mas não existia ainda um texto integrado da nova Constituição**: `redacao/` continha somente README. Foi criada [issue #35 — M00.03](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/35) e [protocolo de técnica redacional](11_TECNICA_DE_REDACAO_E_INTEGRACAO.md) para funções G (geral), E (especialização), X (exceção), A (autônoma) e T (transitória), controle de não duplicação, especialidade e proteção contra supressões materiais. **Primeiro piloto de F7**: [anteprojeto-de-trabalho.md](../redacao/anteprojeto-de-trabalho.md) montado deterministicamente de [indice.csv](../redacao/indice.csv) e dois arquivos `CF-NOR` em [propostas](../redacao/propostas/). **Ambos H — hipóteses exploratórias sem aprovação**, nenhuma arquitetura de direitos, governo, justiça, competências ou texto constitucional completo ratificado. CI passou a verificar fonte integrada e detectar duplicação textual literal, NÃO antinomias semânticas.

## Próxima trilha
1. Validar o contrato metodológico e proveniência das antigas diretrizes.
2. Fazer M00: natureza constitucional, hierarquia, reservas, competências e direitos como estrutura do sistema.
3. Fazer M01: teoria geral de direitos, aplicabilidade, limitações e mecanismos de tutela.
4. Rodada curta de M03–M05: mapa de dependências do sistema político/federativo/fiscal, ainda sem fixar soluções.
5. Iniciar matriz sistemática CF/1988 × problemas × novas decisões, distinguindo mera ausência textual de regressão real.

## Revisões
Atualizar esta síntese ao final de integração substancial. Referências de versão devem apontar commits, nunca a mera memória da conversa.
