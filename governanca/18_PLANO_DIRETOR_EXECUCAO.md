# Plano diretor operacional integrado CF–CLF (camada de coordenação)

**ID:** CF-GOV-018 · **Data:** 15/10/2026 · **Status:** proposta de governança em PR; não altera decisões materiais. **Versão de interface:** COORD-CFCLF-20261015-01.

## Mandato e fronteiras
Coordenar *sequenciamento, metodologia, bloqueios e qualidade* sem fundir as fontes de estado normativo: decisões da CF continuam no repositório CF e decisões do CLF no repositório CLF. Direito vigente só é descrito por fontes oficiais verificadas; CF futura é hipótese; corpus CLF é proposta. A coordenação não é uma instância constituinte. Repositório permanente de cada produto continua sendo sua `main`, após revisão. Branch/PR constituem entregas **pendentes de integração**.

## Modelo de execução
- **Cobertura guiada por riscos:** comparar lacunas relevantes (CF: funções, direitos, órgãos e transição; CLF: fontes/dispositivos, vigência e destinos) antes de aprofundar outra vez matéria já densamente pesquisada.
- **Entrega preferida por ciclo:** uma unidade substantiva concluível; várias se rigor permitir. Somente criar matrizes/testes se responderem a pergunta jurídica determinada. Se não houver trabalho novo seguro, relatar bloqueio e selecionar outro escopo.
- **Fila resiliente:** manter três opções executáveis independentes; um impedimento tem dono, teste de saída, data de reavaliação. Problema técnico recorrente não justifica vários ciclos perdidos.
- **Limite inicial de WIP:** duas frentes substantivas CF, duas CLF, uma interface transversal; frentes bloqueadas não ocupam vaga. Isto é parâmetro de trabalho revisável, não proibição de pesquisa.
- **Dois estágios de integração:** pesquisa e análise documental materialmente revisadas podem entrar na `main` sem ratificar escolha normativa; cláusula e solução material permanecem H/P/A/V/DEC pendentes. Não efetuar merge normativo ou mudar D/CONFIRMADA sem anuência explícita.

## Política de priorização argumentada
Selecione a tarefa com maior potencial de: 1) eliminar lacuna de cobertura; 2) desbloquear outras frentes; 3) produzir corpus/testo integral condicional; 4) reduzir risco de perda de garantias; 5) diminuir divergências entre PRs. Levar em conta custo da próxima entrega e viabilidade técnica. **Não usar score numérico como substituto da fundamentação.** Uma tarefa pode ser ultrapassada quando outra se tornar urgente por risco novo.

## Fila inicial de trabalhos independentes (revalidar em cada execução)
1. **CF M03:** em PR #99/#100, extrair incertezas decisivamente relevantes entre variantes de sistema de governo e assinalar invariantes transversais M02/M04/M06/M14. Entrega: quadro de escolha madura ou investigação focal; sem D.
2. **CF cobertura:** ampliar mapa de funções e garantias da CF/1988/ADCT, sobretudo M07/M08 e direitos especiais de M01, sem converter cobertura parcial em “completa”.
3. **CLF T07:** no PR #45/#39, avançar auditoria jurídico-material de efeitos, especialidades e concordância dos recortes documentais de Lei 9.784; não presumir 215 unidades homologadas.
4. **CLF T01.M04/DEC-016:** prosseguir desenho de corpus único e matriz independente de positivação, com interfaces M00/M03/M14, sem decidir forma de promulgação.
5. **CLF expansão:** recortes em T25/T24/T29/T43 com fontes e controle de especialidades, sem duplicar arquivos dos PRs existentes.
6. **Interface:** matriz CF M07/M06 ↔ CLF T07/T43 (boa administração, intimações digitais, tutela e competência).

## Registro e indicadores
Cada entrega persiste em PR/branch com `FEITO/PENDENTE/PRÓXIMO`, recorte, fontes, data, SHA, risco, status de direito vigente/hipótese e estado dos testes; quando acesso falhar, não declarar escrita. Resumo operacional atual pode ficar em issue/arquivo próprio; preservar quadros históricos extensos, sem lhes impor atualização a cada ciclo.

A cada **14 dias** avaliar: tarefas realmente concluídas, parcelas do universo conhecido cobertas com fonte, interfaces resolvidas, direitos/garantias com destino verificável, pendências materiais que bloqueiam ratificação, retrabalho e ciclos consumidos em erro técnico. Não publicar percentual de completude com denominador não verificado. Reavaliar prioridades e prazos somente depois de observar produtividade.

## Garantias de integridade
Preservação N:N de garantias; sanções/competências/finanças/eleições/tutela com exame R3; fonte oficial temporalmente situada; não confundir CI estrutural com validade, avaliação de um agente com revisão independente ou decisão em chat com aprovação material. Toda reforma relevante acompanha alternativa de manutenção, objeções, efeitos e transição.

## Integração com o CLF
Regra correspondente do CLF: [plano diretor operacional CLF](https://github.com/raphaelpetta/codigo-legislacao-federal/blob/main/docs/21_PLANO_DIRETOR_EXECUCAO.md), com mesma versão de interface **após integração**. Divergências futuras exigem issue de interface em ambos os repositórios. A coordenação pode recomendar; não altera unilateralmente registros CLF.

## Estado da implantação
Arquivo apresentado em branch de governança; **não** declara ter migrado PRs de pesquisa, preenchido inventário completo, alterado tarefa agendada, concluído auditoria ou homologado dispositivos. Atividades e referências dos PRs são fotografias verificáveis no momento da proposta; consultar HEAD e estado atuais antes de qualquer execução.
