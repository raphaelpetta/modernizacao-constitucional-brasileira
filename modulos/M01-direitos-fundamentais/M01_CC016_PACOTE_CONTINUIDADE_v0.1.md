# CF-CC-016 — Continuidade da carteira de cobertura M01/M02/M06

**Data:** 15/10/2026. **Aplicação obrigatória:** [CF-GOV-019 — política de ganho marginal já integrada na main](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/main/governanca/19_POLITICA_GANHO_MARGINAL_GLOBAL.md). **Main verificada:** `7c3bd80470899a09e31f25a6a3a47d7c9cca669c` (**20 H**). **Stack:** PR #119, HEAD `948e0405e8fb74d4b0945f1c44007967b5d5b5c0` (**45 H**), novo trabalho nesta branch (**49 H, 15 módulos**). A branch é descendente do stack de trabalho criado **antes do merge CF-GOV-019 em main**. Ao integrar, preservar a política e reconciliar versões; **não forçar merge**.

## GANHO MARGINAL — preflight, comparação e resultado

**Candidatas H / V / I** documentadas em `modulos/M01-direitos-fundamentais/M01_CC016_PARECER_TRANSVERSAL_COBERTURA_v0.1.md`: (H) liberdades civis M01.14; (V) sufrágio M02 e proteção funcional de independência judicial M06; (I) integração de PRs/diagnóstico de CI #120. **Melhor alternativa preterida:** integrar #101/#104 e diagnosticar CI, relevante porém sob bloqueio de logs/anotações; essa ação deve continuar em coordenação independente. **Também preterido:** repetir M05 caixa, baixo ganho esperado sem evidência que altere projeto/decisão.

**Ganho esperado:** registrar direitos de três módulos pouco cobertos na branch canônica, **sem aprovar** desenho de governo/cortes, e identificar perigos concretos de compressão das garantias CF/1988. **Ganho comprovado:** quatro novas H e matriz 30 casos de continuidade/20 testes; periodicidade do voto e nulidade de decisão imotivada foram detectadas como ausências e **incluídas ainda nesta rodada**. Isso melhora rastreabilidade, mas não prova validade material, integralidade nem maturidade F6. **Classificação:** `NOVO` na cobertura H, `PARCIAL` no mérito jurídico. **Critério de parada executado:** não alongar com novo dossiê sobre os mesmos quatro núcleos; a próxima tarefa deve ser escolhida novamente por ganho marginal.

## FEITO
- `CF-NOR-0049` M01 liberdade de expressão, fonte/censura/direito de resposta;
- `CF-NOR-0050` M01 reunião e associação, aviso não licença e dissolve só por sentença transitada;
- `CF-NOR-0051` M02 sufrágio universal, voto direto, secreto **e periódico**, participações plebiscito/referendo/iniciativa;
- `CF-NOR-0052` M06 juiz natural, imparcialidade, independência, nulidade da falta de fundamentação, vitaliciedade carreira e autonomia financeira;
- `auditoria/CF_CC_016_MATRIZ_30_GARANTIAS.csv`: **30 funções verificadas como parcial/ausente/remissão/hipótese separada ou não decidida**, sem falsa equivalência;
- `auditoria/CF_CC_016_MATRIZ_20_TESTES.csv`: **20 cenários**, 8 M01, 6 M02, 6 M06;
- parecer transversal com fontes oficiais e críticas, `redacao/indice.csv` atualizado ordens `0480..0510` e `redacao/anteprojeto-de-trabalho.md` como vista derivada.

## QA observado
- Leitura GitHub remota de índice, fontes novas, vista e matrizes. **PASS:** 49/49 IDs e ordens únicos, 49 seções correspondentes, 49 estados H, 15 módulos M00–M14; corpo normativo de 0049–0052 reproduzido na respectiva seção; 30/30 funções e 20/20 testes sem IDs repetidos e com colunas consistentes.
- **Não executados** scripts Python `scripts/gerar_anteprojeto.py --check` e `scripts/validar_repositorio.py`; a CI da PR deverá ser lida quando aberta. Houve revisão jurídico-documental focal, **não parecer externo de especialistas** nem auditoria N:N exaustiva das CF 1988/ADCT.
- **Atenção aos PRs #59/#101/#104 e stack #105–#119:** 0030/0031 privacidade permanecem em PR #59; a nova faixa 0049–52 foi pesquisada no índice stack e nas referências GitHub antes de ocupar. Nenhuma CF-DEC substantiva alterada; `main` não muda por PR draft.

## PENDENTE / NÃO VERIFICADO
1. **M01:** liberdade religiosa/consciência/assistência espiritual/escusa (CF5 VI–VIII), locomoção, profissão, direitos informacionais, associação sindical, crítica à censura privada e moderação digital, direito de tutela e proteção de minorias.
2. **M02:** CF14 §§1–16, CF15/17, periodicidade e cláusula pétrea art60 §4 II (a periodicidade consta da H-0051, mas a rigidez constitucional ainda falta), consultas e elegibilidade, voto obrigatório/facultativo sem decisão.
3. **M06:** arquitetura 92–126, competências, órgão constitucional de cúpula, CNJ, vedação de vantagens/incompatibilidades, publicidade/sigilo estrito, custas, Defensoria, Ministério Público e proteção jurisdicional eficaz.
4. **M14:** transição, mandatos, via de reforma, preservação de garantias em configuração A/B/C e eventuais diferenças entre magistratura de carreira e Corte Constitucional com mandato.
5. **CI / PR:** teste documental e leitura de GitHub não asseguram execução Python nem possibilidade de merge; incidente #120 em aberto.

## PRÓXIMO — seleção deverá ser refeita pela política CF-GOV-019
**Opções concorrentes reais:**
- **M01.14 (ganho horizontal):** inventariar e propor proteção explícita de consciência, religião e objeção do art5 VI–VIII; mitigar regressão grave em liberdade de crença.
- **M02 (direitos políticos):** bloco de elegibilidade, regime do voto e autonomia partidária que permita comparar modelos A/B/C sem escolha de fórmula.
- **M06 (estrutura):** variantes condicionais de órgão de controle constitucional com teste de independência, acessibilidade e jurisdição sem confundir carreira com mandato.
- **Integração (#120/#101/#104):** resolver bloqueio de CI/anotações e dívida de PRs, com critério de fechamento técnico objetivo; não virar mais uma pesquisa infinita.

**RESPONSÁVEIS / INTERFACES:** M01 issue #54, M02 issue #14, M06 issue #55, M03 issue #84, M14 issue #90, central #103 e CI #120; CLF apenas por pedido bilateral caso texto mude competência material. **Nenhuma F6/D material ou escolha de sistema de governo.**