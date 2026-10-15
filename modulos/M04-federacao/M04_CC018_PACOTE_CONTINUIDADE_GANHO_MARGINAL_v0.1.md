# CF-CC-018 — Carteira de ganho marginal e continuidade

**Corte:** 15/10/2026. **Principal obrigação:** CF-GOV-019 [integrada à main](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/main/governanca/19_POLITICA_GANHO_MARGINAL_GLOBAL.md), sem ratificar escolhas de mérito. **Base stack:** PR [#123](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/123), commit `9541d25eb3d5ca04fb32933e9816508c78568ca0`, 51 H. **Main de entrada:** `7c3bd80470899a09e31f25a6a3a47d7c9cca669c`, 20 H. Esta branch adiciona **três H** e alcança 54 H; os projetos têm autonomia documental e não houve merge de normas nesta rodada.

## Preflight — três possibilidades concorrentes e ganho marginal

| Opção | Próximo resultado material plausível | Razão de escolher ou preterir |
|---|---|---|
| **H: M04, federação e competências** | preencher autonomia federativa, distinção competência administrativa comum vs. legislativa concorrente, interesse local dos Municípios; M04 só possuía H geral de competência/financiamento (0001) | **Escolhida**, lacuna R3 e texto distinto |
| **V: M07 serviço profissional e concurso** | preencher CF37 caput/II/V/IX, sem repetir H-0021 sobre petição e processo administrativo | **Escolhida**, efeitos institucionais verificáveis; Tema 1010 e Tema 784 |
| **V: M13 jurisdição penal internacional** | preencher CF5§4 que H-0036 assinalava explicitamente como ausente | **Escolhida**, complemento autônomo pequeno e constitucionalmente específico |
| **I: integração e CI da cadeia #105–#123, #101/#104** | retirar o maior bloqueio do *produto* e eliminar divergência entre 20 H na main e 54 H no stack | **Alternativa não executada nesta rodada**, mas já se torna a **principal candidata da próxima**, com ganho potencial superior a novo texto |

**Custo de oportunidade e critério de parada:** três normas H por funções descobertas e uma matriz crítica; após esse delta, **não iniciar quarta rodada contínua de novas CF-NOR** sem confrontar o ganho de corrigir CI, reconciliar PRs e elevar qualidade jurídica de textos já existentes. **Não** calcular completude pela contagem de 54 H; a maior parte das funções constitucionais ainda demanda confronto N:N.

## FEITO — três deltas canônicos, sem duplicação

1. `CF-NOR-0055` **M04 H/A** (ordem 0540): autonomia federal/estadual/distrital/municipal, competência executiva comum, legislação concorrente com normas gerais e suplementação, interesse local municipal; regra 0001 permanece centrada em competência–financiamento e não é duplicada.
2. `CF-NOR-0056` **M07 H/A** (0550): impessoalidade, concurso público, restrição de cargos em comissão e contratos temporários, prevenção de nepotismo e favorecimento. A H-0021 preserva processo administrativo, petição e inclusão digital — função diferente.
3. `CF-NOR-0057` **M13 H/A** (0560): submissão brasileira ao Tribunal Penal Internacional, complementaridade e cooperação legal. A H-0036 protege direitos de tratados/rito qualificado, não tinha reproduzido CF5§4.
4. `auditoria/CF_CC_018_MATRIZ_28_GARANTIAS.csv` identifica **28 destinos constitucionais** com `PARCIAL`, `NAO_COBERTO`, `APENAS_REMISSAO` ou `EM_OUTRA_FICHA_H`. Não contém declaração de equivalência integral.
5. `auditoria/CF_CC_018_MATRIZ_18_TESTES.csv`: **18 cenários** com status V/A, seis por frente. São desenhos adversariais e provas pontuais de texto vigente, não 18 decisões judiciais nem testes automatizados de comportamento institucional.
6. `redacao/indice.csv` e `redacao/anteprojeto-de-trabalho.md` sincronizados com 54 H; **nenhuma** CF-DEC nem regra de governo aprovada.

## PENDENTE e melhores objeções

- **M04:** a fórmula reduz repartição hoje minuciosa em arts.18–36; seria regressão afirmar que competência comum torna serviço livremente transferível ou que norma municipal prevalece sobre matéria privativa da União. Competências residuais, intervenção, regiões, proteção territorial e financiamento seguem abertos. Revisar art.167§7º, CF-NOR-0001/0002 e ADI6341.
- **M07:** concurso e cargos comissionados precisam convivência com cotas, igualdade, estabilidade, regras de nomeação (Tema 784), nepotismo em cargos políticos e poderes de cada ente, sem engessamento fiscal. Faltam CF37 III/IV, VI–XXII e art.41. A tese do Tema1010 não significa que toda função política ou confiança seja proibida.
- **M13:** TPI é jurisdição **complementar** (Estatuto de Roma art.1), não instância recursal nacional; falta regime de cooperação, competência legislativa e denúncia, reservas, efeitos processuais, jurisdição temporal e interfaces de M12. Não transformar submissão em adesão a qualquer tribunal penal estrangeiro.
- **Integração:** 34 H adicionais ao produto documental na main estão em PRs em cadeia, incluindo repositório principal com política CF-GOV-019 já atualizada; revisar divergência de bases, PR #59 privacidade e #101/#104 governança, preservar decisões P/A e corrigir CI [#120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120). Sem logs acessíveis não atribuir falha a texto nem declarar scripts aprovados.
- **Qualidade:** análise documental e cálculos da estrutura não equivalem a parecer humano jurídico independente, revisão de fontes integrais, auditoria da CF/1988 por dispositivo ou compatibilidade com ADCT. **Não executar merge de redação constitucional sem as portas de qualidade.**

## PRÓXIMO — comparação antes de repetir escrita

1. **Prioridade de integração:** definir plano **executável** para reconciliar PRs #101/#104 com a main CF-GOV-019 e os 34 H adicionais do stack #105–#124. Tentar diagnosticar CI por informações reais das duas anotações, se acessíveis; em caso contrário, executar validadores via checkout reproduzido ou identificar bloqueio autorizado e documentar caminho.
2. **M04/M07/M13 auditoria focada:** buscar provas que poderiam alterar texto, não simples nova rodada com H em todos os módulos; a matriz de 28 garantias define destinos e pendências.
3. **M14:** confrontar vigência, recepção, transferência de competências e continuidade institucional sem ratificar A/B/C e sem suprimir salvaguardas.

**Registro de ganho esperado x comprovado:** esperado: cobrir três funções não duplicadas; comprovado até o handoff: três fichas H e duas matrizes, mais sincronização canônica (verificar leitura remota separadamente). Status `NOVO` **no texto experimental**, `PENDENTE` na integração e validade material.

**Interfaces:** M00/M01/M03/M04/M05/M06/M07/M09/M11/M12/M13/M14; central CF #103, assuntos federativos M04 #21, M07 (issue vinculada a PR #102), M13 #93, CI #120. CLF mantém autonomia, qualquer proposta infraconstitucional será encaminhada em demanda própria.