# M03.02.11 — FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026 · **Issue M03:** [#84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84) · **PR draft:** [#85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85) · **branch:** `pesquisa/m03-02-governo-responsabilidade-20261014` · **main preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **estado:** F0–F5/F8, H/P/A/V, F6 NÃO deliberado e F7 NÃO iniciado. Nenhuma CF-NOR, CF-DEC D, CLF ou edição na main. **M03** lidera; M03.01/M04/M05/M06/M07/M14 dão interfaces.

## FEITO — somente branch de pesquisa
1. `M03-02_11_PARECER_RECONCILIACAO_GLOBAL_E_RESERVA_DE_ORCAMENTO_v0.1.md`: especifica sete portas de controle antes de declarar autorização fiscal realizável; distingue votos, iniciativa, materialidade, origem/compromisso/vinculação/exercício, dívida, caixa, direitos territoriais, dever de LOA agregada e fiscalização judicial estrita. Identifica contraprovas e encerra fase de proliferação de cenários fictícios como fim em si mesmo.
2. `M03-02_11_CATALOGO_11_FONTES_HIPOTETICAS.csv`: **11 fontes-IDs** abstratas com Y0–Y3, identidade, exercício, classes jurídica/territorial, vinculações e estado H; SEM valores financeiros. `UM_SLOT_INDIVISIVEL` é apenas marcador lógico de exclusividade, não R$, saldo ou crédito.
3. `M03-02_11_20_REIVINDICACOES_E_RESULTADOS.csv`: **20 pedidos** de créditos/obrigações H com cinco reservas técnicas condicionais, três bloqueios por fonte duplicada, um veto de vinculação, crédito sem autorização, fonte expirada, compromisso anterior, ano errado, dois estados pendentes por disponibilidade, um por fonte ausente, iniciativa, voto, materialidade e caso de receita constitucional de ente sem voto constitutivo. A ordem dos registros serve para DETECTAR sobreposição, não escolher que direito/prestação merece prioridade.
4. `M03-02_11_MATRIZ_12_TESTES_RECONCILIACAO.csv`: **12 ataques** a créditos avulsos, tutela de direitos, alteração indevida de fontes, dívida, entes e orçamento anual.
5. `M03-02_11_PORTAS_F6_RECONCILIACAO.csv`: **10 decisões F6-11-00..09**, todas ABERTAS, dependentes de interfaces reais.
6. `scripts/validar_m03_02_11_reconciliacao.py`: reprodutor determinístico de 20 resultados H mais verificação das quatro matrizes. **QA independente efetivamente executada em JavaScript** lendo os quatro CSV diretamente do GitHub: PASS; IDs únicos, colunas completas, 11/20/12/10 registros, cinco reservas técnicas, todas 20 decisões reproduzidas, 10 portas abertas. **Não afirmar execução do script Python no CI**, salvo execução comprovada em runner.
7. Direito brasileiro vigente: Lei 4.320/1964 art.43 §1º (fontes não comprometidas), LRF LC101/2000 arts.48 e 50 (transparência, vinculação/caixa individualizados), CF arts.158–160/165–169 e 167§7 (encargos de serviço público sem fonte/repasse EC128/2022). **Não vender técnica vigente como lacuna absoluta.**
8. Direito comparado: LOLF francesa art.45 é autorização especial de CONTINUIDADE DE ARRECADAÇÃO/TRAMITAÇÃO e decretos delimitados de `services votés`, com proposta anual sob debate; **NÃO há licença francesa genérica para votar cada despesa como lei especial.** P2 matéria por matéria é hipótese separada sob M03.01/M05.
9. Não alterada `governanca/03_DECISOES.md`, `redacao/indice.csv`, CF-NOR, CF main ou legislação CLF; nenhum F6 formal ou escolha de forma de governo.

## PENDENTE — críticas que nenhum script resolve
- **M05:** parecer jurídico-fiscal da autorização especial sob LOA inexistente; aderência a LRF e crédito na nova CF, demonstração de fonte livre/vinculação, agregação, disponibilidade de caixa, limites e financiamento de serviços exigíveis; base real de custos/receitas ainda ausente.
- **M03.01:** espécie de lei, iniciativa, emendas, quóruns, agenda, tramitação e compromisso de analisar LOA anual sem que lei parcial vire voto de confiança.
- **M04:** titularidade efetiva de receitas e direitos de estados/municípios, não tratar partilha constitucional como subvenção, encargos e veto territorial.
- **M06:** tutela contra omissão pública/ilegalidade de crédito e direito exigível sem juiz criar LOA, dinheiro ou prioridades em desfavor de outros titulares.
- **M07:** publicidade acessível, contratos, segregação de caixa, contabilidade de compromissos, atos emergenciais.
- **M14/M02:** transição para a primeira eleição e primeiro orçamento sob arquitetura A/B/C, mantendo art.16 e direitos ao mandato; M12 cadeia de comando em emergências se pertinente.
- **Risco político central:** gabinete sem maioria construtiva nem LOA nova pode continuar por anos; reconciliação apenas torna falhas observáveis e limita fraudes, **não cria maioria nem resolve comparação causal de sistemas de governo**.
- **CI/merge:** consultar status no HEAD final e divergência da main; aprovação estrutural de GitHub Actions não significa implementação efetiva, auditoria jurídica ou valores reais.
- **F6-00 A/B/C:** B segue preferência de **prototipagem P, não D**. A presidencial reformado é contrafactual forte, C premier-presidencial mantém a objeção da dupla legitimidade. Nunca passar hipótese em F6 por “bora” ou merge de documentação.

## PRÓXIMO — M03.02.12 (mudança de estratégia editorial)
**Não** criar dezenas de cenários fiscais repetidos sem dado novo. Produzir **auditoria de suficiência da pesquisa M03.02.01–11**, sintetizando:
(a) regras e salvaguardas verificadas, (b) melhores objeções não resolvidas de A/B/C, (c) interfaces M02/M03.01/M04/M05/M06/M12/M14 **efetivamente respondidas ou ainda sem parecer**,
(d) condições mínimas para nota final F6-00 de opção de arquitetura com A/B/C/não decidir; e
(e) matérias fiscais que deveriam permanecer em futura lei orgânica/CLF após escolha constitucional, sem constitucionalizar esquema técnico de planilha.
**Critério de saída:** documento crítico transparente ao usuário, compatível com H/P/A/V, com recomendação de onde interromper pesquisa; eventual deliberação de preferência P não vira ratificação D sem decisão expressa. Não mover status jurídico sem o rito de governança.

## Fontes de auditoria
- https://www.planalto.gov.br/ccivil_03/leis/l4320compilado.htm
- https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm
- https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044611965
- https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html

**Rastro:** toda R11 permanece em branch draft do PR #85; fonte integrada de verdade é apenas `main`. Enviar handoffs e atualizar PR; nenhuma decisão constitucional está pressuposta.