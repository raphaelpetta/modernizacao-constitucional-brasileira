# CF-CC-019 — Plano de integração e bases verificadas

**Estado:** protocolo operacional de reconciliação, sem mudança constitucional de mérito. **Corte:** 15/10/2026. **Base main:** `7c3bd80470899a09e31f25a6a3a47d7c9cca669c` (20 CF-NOR H, CF-GOV-019/CF-DEC-015). **Pesquisa experimental:** [PR #124](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/124) (54 CF-NOR H/15 módulos). **Objetivo:** eliminar erros de merge e colisão, não presumir aprovação política.

## Grafo real da pilha, conferido nos metadados dos PRs

```text
main ── #105 ── #106 ── #108 ── #109 ── #110 ── #111 ── #112 ── #113 ── #114
                                                                                 └── #115 ── #116 ── #117 ── #118 ── #119 ── #122 ── #123 ── #124

main ── #107 (M03 variantes A/B/C, fora da pilha)
main ── #101 (progressividade/governança, conflito com main após #121)
main ── #104 (central, filas/scripts/painéis, parcialmente independente)
main ── #121 (CF-GOV-019, **já mesclado**, SHA main 7c3bd804...)
main ── #59 (privacidade, CF-NOR 0030/0031 reservadas)
```

**Conferência:** bases e estados foram lidos dos PRs #105–#119 e #122–#124, além de #101/#104 e #121; a enumeração é **parentesco Git**, não autorização para mesclar em cascata. **Desvio material:** a pilha parte de `main` **anterior** ao merge de CF-GOV-019. Não mesclar topo #124 diretamente na main atual sem reconciliar o DAG, atualizar índice, fonte e política.

## Ganho de integração com risco controlado

1. **Primeira faixa (esta rodada):** trazer somente documentos operacionais não conflitantes de [#101](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/101) (progressividade, execução por camadas e plano diretor) e [#104](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/104) (núcleo da central e política de concorrência), adaptando o status e vinculando-os à [CF-GOV-019](../governanca/19_POLITICA_GANHO_MARGINAL_GLOBAL.md). Reconstruir `CF-DEC-014` operacional sem apagar `015`; nenhum script, painel gerado ou norma H transferida.
2. **Pendente em #101:** `catalogo/COBERTURA_FUNCIONAL.csv`, atualizações de `MODULOS.csv`, modelo de dossiê, script de validação e alteração residual de guias; os dados de cobertura são fotografias que precisam cotejo com main/stack.
3. **Pendente em #104:** scripts `controle_operacional.py` e `validar_operacao_local.sh`, workflow, testes, `FILA_TRABALHO.csv`, `PAINEL_GERADO.csv` e `QUADRO_PRODUTO.csv`. Não importar painel de 20 H como se fosse análise dos 54 da branch.
4. **Pilha normativa:** reproduzir validadores em checkout idêntico após sanar o bloqueio de execução ou em ambiente de teste com acesso; realizar auditorias jurídicas por R3 e integridade CF/1988/ADCT, detectar colisões de CF-NOR, conservar a distinção H/P/D e somente então considerar integração experimental.
5. **Variante M03 #107 e privacidade #59:** permanecem paralelas; cláusulas 0030/0031 reservadas e modelos institucionais A/B/C abertos. Não deduzir ratificação de texto H por merge técnico.

## Critérios de saída objetivos para integração normativa

- Conferir `main` e HEAD de PRs de origem; **bloquear se moverem** sem comparação de novo diff.
- Validar 54 fichas versus vista e `redacao/indice.csv`, checar remissões e duplicações, arquivo obrigatório, rota de trabalho; distinguir esse resultado de conformidade jurídica.
- Executar em checkout fiel `python scripts/validar_repositorio.py`, `python scripts/gerar_anteprojeto.py --check`, testes M05.02 e `test_redacao_integrada.py`; confrontar resultados. **Nenhum desses comandos rodou no GitHub Actions nos runs examinados.**
- Reconciliar central/GOV-019, remédios e garantias CF5, direitos políticos art14–17, federação, transição, orçamento e tribunal superior. Exigir análise crítica externa ou revisão especializada proporcional a R3; sem D material automática.
- Após integração, atualizar PRs/issue #103 e documentação de referência; PR original só pode ser fechado como substituído se o *delta* integral tiver destino comprovado.

## GANHO MARGINAL esperado × observado

A triagem privilegiou a redução do risco de perda de documentação, o diagnóstico da CI e a integração metodológica **em vez de produzir novas cláusulas CF-NOR**. A existência deste plano e a conferência de textos/PRs são verificáveis. A integração material das 54 H e o restabelecimento da CI **ainda não ocorreram**. Próximo trabalho de maior ganho: destravar a execução do runner e auditoria jurídica independente das hipóteses, não nova coleta de assuntos dispersos.

**FEITO:** DAG e riscos, plano seletivo; **PENDENTE:** validar a CI, importar scripts/painéis apenas após teste, reconciliação das 34 H adicionais; **PRÓXIMO:** ação material somente com evidência e bases atuais. **Interfaces:** central [#103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103), diagnóstico [#120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120), PRs #101/#104, CLF autônomo.
