# M03.02.10 — FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026 · **Issue:** [#84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84) · **PR:** [#85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85), draft · **branch:** `pesquisa/m03-02-governo-responsabilidade-20261014` · **main preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`.
**Propriedade:** M03. Interfaces M03.01/M04/M05/M06/M07/M14; eventual M02/M12. Estado F0–F5/F8 H/P/A/V; **F6 NÃO deliberada**, F7 não iniciado, nenhum CF-NOR, CF-DEC D, CLF, ou alteração da main.

## FEITO
1. `M03-02_10_PARECER_LEIS_PARCIAIS_VOTOS_E_AGREGADO_FISCAL_v0.1.md`: voto político (quantos deputados votam SIM), validade jurídico-formal (competência, iniciativa, tipo de lei, fonte e quórum), capacidade material (autorização, caixa, limites e direitos) são camadas distintas. Preservada distinção entre LOA negada e lei fiscal especial eventualmente apoiada.
2. `M03-02_10_24_VOTACOES_LEIS_PARCIAIS.csv`: **24 votos artificiais**, 2 legislaturas × 4 objetos HOSP, ESCOLA, CONVENIO vigente/exigível e DIVIDA_NOVA × três variantes V1 governo+pivô, V2 oposição+pivô, V3 governo contra oposição+pivô. L2: V1 56–44, V2 54–46, V3 46–54; L3: V1 53–47, V2 55–45, V3 45–55. **V1/V2/V3 são alternativas PARA CADA proposta, não sequência de quatro votações com coalizão estável**. Ninguém demonstrou legalidade de tramitação, resultado real ou suficiência financeira.
3. `M03-02_10_8_CONTROLES_DE_TITULARIDADE_E_CREDITO.csv`: 8 testes (2 câmaras × quatro invariantes) indicando que receita federal constitucionalmente repartida no direito vigente (CF158–160) NÃO depende de votação política constitutiva de nova titularidade; obrigação exigível não precisa lei nova para existir, mas pode precisar autorização fiscal; rubrica extinta não renasce por prorrogação; nova dívida exige autorização e controles próprios.
4. `M03-02_10_12_TESTES_COHERENCIA_FISCAL.csv`: **12 testes**, 2 câmaras × três ramos políticos × fontes não comprovadas ou hipoteticamente presumidas por medida. Mesmo havendo fonte hipotética individual, **não se demonstrou ausência de sobreposição do financiamento nem compatibilidade fiscal agregada**; V2 da oposição pode não ter iniciativa válida, dívida nova demanda fonte/limite. Não se inventaram quantias ou votos F6.
5. `scripts/validar_m03_02_10_matrizes.py`: verificador reproduzível da combinatória e da soma dos votos. **QA independente JS executada** diretamente sobre os CSV lidos no GitHub: PASS; [24, 8, 12] linhas; [20, 11, 12] campos, IDs exclusivos, todas partições de partido somam 100, somas L2/L3 corretas, maioria SIM>NÃO meramente ilustrativa, sem a transformar em lei válida. O Python foi incluído, NÃO atribuir execução dele ao CI sem verificar.
6. **Correção metodológica permanente:** L2/P2 original tem derrota formal de confiança no t5; o ramo de experiência L2 é derivação depois de t4 e antes de t5/t6. L3/P2 continua sem voto de confiança. Novo crédito não se pode converter em confiança. Nenhuma eleição decorre de lei fiscal derrotada.
7. **Fontes jurídicas e metodológicas:** Lei 4.320/1964 arts.40–43 (espécies e recursos), LC101/2000 arts.15–17 (impacto e custeio sob pressupostos), CF arts.165–169/167 V–VII e §7º, arts.158–160; França LOLF art.45 demonstra técnica de continuidade de finanças com lei especial, mas sem equivalência automática de seu tributo/crédito ao Brasil. Comparação não estabelece prioridade causal ou legitimidade legal das leis parciais.
8. Nenhuma edição da main, `redacao`, `governanca/03_DECISOES.md` ou repositório CLF.

## PENDENTE
- **M03.01:** parecer sobre espécie de lei fiscal especial em ausência de LOA aprovada, iniciativa e direito de emenda por matéria; maioria numérica de oposição não prova direito de iniciar nova despesa.
- **M05:** demonstrar disponibilidade de recursos, identificação sem dupla contagem, aumento de gastos e dívidas, compatibilidade global PPA/LDO ou instrumentos correspondentes, crédito extraordinário e execução de obrigações legalmente exigíveis, especialmente Y2/Y3.
- **M04:** participação territorial e continuidade de transferências constitucionalmente devidas, encargos sem custeio CF167§7 e distinção de convênios, controle de autonomia.
- **M06:** tutela de direito material com deficiência de caixa, controle de competência/forma, prestação de contas, proteção contra orçamento fatiado permanente e perda de igualdade entre credores.
- **M07/M14:** execução administrativa e primeira eleição/primeiro orçamento da reforma. Sem parâmetros e mandatos escolhidos.
- **Dados reais:** sem despesas, arrecadação, programação, obrigações ou séries temporais nacionais harmonizadas; **sem** valor de crédito, saldo ou projeção real. As 24 votações são experimentos matemáticos, NÃO fatos eleitorais.
- **F6:** decidir o papel relativo de orçamento agregado anual versus leis especiais exige o conjunto da arquitetura A/B/C e confirmação das interfaces; nenhum artigo ou posição constitucional foi ratificado.

## PRÓXIMO — M03.02.11
Organizar matriz de reconciliação global de autorizações fiscais especiais para impedir **dupla contagem** e **governo permanente por leis avulsas**:
- mapear proposta → obrigação → fonte não comprometida → custo plurianual → autorizações anteriores → compatibilidade agregada → publicação → rito parlamentar/competência → execução fiscal e caixa;
- casos (1) hospital+escola financiados pela mesma rubrica, (2) transferência municipal constitucional condicionada à LOA, (3) nova dívida de custeio para sustentar gabinete, (4) comissão de orçamento bloqueia votação completa apesar das leis especiais;
- incorporar críticas formais M03.01/M04/M05/M06 sem fingir que foram emitidas, e preparar alternativa P1–P4 coerente para uma porta F6 setorial posterior.
**Saída:** nova matriz de riscos, controles de autoria e contabilidade, melhor objeção e FEITO/PENDENTE/PRÓXIMO, ainda sem CF-NOR.

## RASTRO
Pesquisar no mesmo PR #85 draft. Consultar após commit final GitHub Actions, main e divergências; sucesso técnico de estrutura não implica parecer fiscal ou ratificação.