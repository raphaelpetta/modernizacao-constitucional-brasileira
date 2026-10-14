# Pacote de continuidade — CF-M01.12-F0F5-001

**Data:** 14/10/2026 · **Escopo:** internação/intervenção involuntárias e cuidados comunitários.  
**SHA CF de entrada:** `50b498885e17fa1709e66b0861f40e5387b4f4b0`. **SHA de saída:** conferir `main` após eventual merge; não presumir.  
**Branch:** `pesquisa/m01-12-coercao-raps-f0f5-v01`. **Issue:** [#49](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/49). **PR:** conferir descrição/estado no GitHub quando aberto.  
**Fontes principais:** Lei 10.216/2001, Lei 11.343/2006 art. 23-A/Lei 13.840/2019, CDPD e LBI (todos em Planalto); STJ Informativo 533 (2014, resumo); OMS/OHCHR 2023 e Comitê CDPD (orientação); Ministério da Saúde Relatório de Gestão 2025 pp.73–74. URLs e diferenças de força jurídica no dossiê.

## FEITO
1. Preflight confirmou código **M01.12 já atribuído à issue #49** e liberdades **M01.14 issue #54**; sem nova renomeação. Conferidos main, PRs drafts, reservas e `CF-NOR-0001–0020`.
2. Produzido [dossiê jurídico-comparado F0–F5](M01-12_COERCAO_EM_SAUDE_RAPS_ALTERNATIVAS_v0.1.md), com quatro alternativas A–D, distinção de seis regimes e objeções.
3. Produzida [matriz de 22 cenários de risco](M01-12_MATRIZ_TESTES_E_CONFLITOS.csv), todos analíticos/hipotéticos e não dados de vítimas.
4. Transcritos [dados oficiais federais RAPS 2025](M01-12_RAPS_2025_FONTE_OFICIAL.csv): 3.070 CAPS, 1.042 residenciais agregados SRT+UA e 2.169 leitos de hospitais gerais, total heterogêneo 6.281; dados extraídos em 31/12/2025. Checadas somas das cinco regiões em cada categoria. **Não medem cobertura ou taxa de coerção.**
5. Nenhuma norma CF-NOR criada; nenhum status H→D. Existing `CF-NOR-0020` não autoriza por si só intervenção involuntária.

## PENDENTE / NÃO VERIFICADO
- Revisão longitudinal/atual (pós-LBI) de STF/STJ e de interpretação da CDPD, além de precedentes estaduais e efeitos da Lei 13.840.
- Dados de número, motivo, duração, reinternação, desfecho, processo/advogado e fiscalização de internações involuntárias por ente.
- Cadastro real de equipes, ocupação e acesso CAPS/RAPS, territorialização/população, cuidado comunitário e orçamento executado; custos e transição não calculados.
- Ausculta real de pessoas afetadas, familiares, profissionais, Defensoria, gestores e movimentos; não apresentar hipótese como opinião de tais grupos.
- Parecer M06 sobre habeas corpus, tutela e revisão; M09/M05 sobre capacidade, serviços e financiamento; interface CLF.
- Não há validação de superioridade causal ou escolha normativa A–D.

## DECISÕES E CLASSIFICAÇÃO
- **D operacional já vigente no projeto:** regra CF-GOV-012 de preflight/handoff, preservada, sem regra concorrente.
- **H:** alternativas A/B/C/D em análise e eventuais propostas futuras; nenhuma escolhida.
- **A:** admissão material de internação não consentida, extensão de cláusula constitucional, desenho de revisão obrigatória, direitos de crianças, epidemiologia.
- **V:** atualidade de jurisprudência, cobertura empírica, efeitos financeiros, implementação local e evidência de danos/benefícios.

## PRÓXIMO (uma tarefa concreta)
**M01.12.02 — auditoria de controle de internações e capacidade territorial da RAPS**, na **mesma issue #49**: identificar fonte administrativa pública agregada/anônima de internações involuntárias e revisões, construir critérios de acesso/ausência dos dados e cruzar com CNES, financiamento SISMAC/FNS e RAPS 2025; revisar decisões judiciais pós-LBI e solicitar parecer M06. Entregar matriz com unidade ente/ano e incertezas, sem deduzir causalidade do agregado.

## COORDENAÇÃO E QA
- M01 condutor; M06 (remédios, defesa e controle); M09 (serviços), M05 (repasses), M12 (liberdade/coerção), M13 (direito da CDPD), M14 (transição), M07 (sigilo de dados).
- `redacao/indice.csv`, propostas e o texto integrado **não foram alterados**; 20 H na main de entrada, PR #59 usa 0030/0031 apenas em draft.
- O GitHub Actions/QA de **esta branch** deve ser consultado após criar PR; não declarar CI aprovado antes do relatório da execução.
- O protocolo e o conteúdo jurídico ainda exigem revisão humana, mesmo com validação CSV e links corretos.
