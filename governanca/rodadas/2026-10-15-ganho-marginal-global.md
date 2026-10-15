# CF-COORD-20261015-GM — implantação da avaliação de ganho marginal

**Natureza:** marco transversal operacional H→D somente **para governança de execução** conforme pedido explícito do usuário em 15/10/2026; nenhuma ratificação de cláusulas constitucionais. **Base lida:** `main` `2a770a8136f8ca4877e865be3e3b7745a6d4b168`; PRs de governança concorrentes [#101](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/101), [#104](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/104) ainda draft; [PRs normativos até #119](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/119), com stack experimental de 45 H e main de 20 H. **Corte:** 15/10/2026.

## FEITO

- Documento **CF-GOV-019** `governanca/19_POLITICA_GANHO_MARGINAL_GLOBAL.md` com definição, método prospectivo, triagem de carteira, custos de oportunidade, regra de saturação, critérios de exceção e métricas qualitativas não arbitrárias.
- Propagação transversal para `README.md`, `chatgpt/INSTRUCOES_PROJETO.md`, `governanca/02_METODOLOGIA.md` e `governanca/12_PROTOCOLO_RODADAS_E_SINCRONIZACAO.md`.
- Novo campo obrigatório no `modelos/PACOTE_CONTINUIDADE.md` (candidatas H/V/I, escolha e alternativa preterida, benefício esperado/observado, saturação e critério de parada).
- `governanca/03_DECISOES.md` contém **CF-DEC-015 D (operacional)**, explicitamente distinguida de F6 constitucional; CF-DEC-014 permanece em PR #101 e **não foi ocupada**.
- Exemplo negativo concreto: CF-CC-012–015, quatro rodadas sucessivas em caixa/LOA M05; concluir que a **próxima pesquisa no mesmo recorte deve demonstrar potencial concreto de alteração de norma/decisão**, não continuar só por inércia.

## Comparação de alternativas (preflight desta própria rodada)

**Candidata H:** novo recorte jurídico de M01/M02/M06, ganho real futuro alto, mas não atende imediatamente a ordem de implantar **regra global**. **Candidata V:** continuar M05 com RGF municipal, ganho marginal baixo sem vínculo de dados a decisão. **Candidata I (escolhida):** formalizar política global nos pontos de entrada de toda rodada, ganho transversal alto e manutenção documental limitada. **Alternativa preterida:** apenas comentar issue central sem arquivo persistido — valor menor por falta de aplicação operacional global.

**Ganho esperado:** impedir quatro ou mais ciclos sucessivos no mesmo núcleo sem justificação e elevar visibilidade de lacunas de direitos em outros módulos. **Ganho de fato comprovado:** registros documentais e instruções vinculados na branch; comportamento futuro e redução de retrabalho **ainda não observados**. Não inventar percentuais, horas economizadas ou provas de melhora institucional.

## PENDENTE

- Concluir QA textual de links locais, integridade das modificações, resultado efetivo de Actions e efeitos colaterais dos PRs #101/#104.
- Eventual merge na `main` depende do estado real de revisão e reconciliação; comentário em conversa e branch não equivalem a `main`.
- A fila/central do PR #104 contém regra parcial de rotação, e o PR #101 contém CF-GOV-017/018 e CF-DEC-014; preservar regras complementares **sem repetir** trechos ou rebaixar garantias. Validar que nenhuma orientação anterior seja perdida.

## PRÓXIMO

**Primeira rodada sob CF-GOV-019:** avaliar três candidatas M01 (liberdades e sua tutela), M02/M03 (direitos políticos/governo) e M06 (arquitetura judicial), com M14 como interface; justificar seleção por lacuna e risco, não pela sequência da última investigação. M05/LOA em **PAUSADO_POR_DEPENDENCIA** (com ressalva de que direitos e deveres jurídicos materiais seguem abertos).

## COORDENAÇÃO / DEPENDÊNCIAS

Central [#103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103); conflito/PR #101, #104; CI geral [#120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120). Nenhuma mudança automática no CLF. **Condição de saída:** política acessível por links a partir das instruções, metodologia, protocolo, modelo de handoff e README, com estado CI declarado e D operacional documentada.
