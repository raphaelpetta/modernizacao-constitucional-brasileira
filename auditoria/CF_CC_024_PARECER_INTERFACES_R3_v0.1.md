# CF-CC-024 — Auditoria de interfaces R3 das 54 hipóteses H

**Natureza:** verificação jurídico-funcional transversal, **não** minuta constitucional, decisão política ou certificação de equivalência à CF/1988. **Corte:** 15/10/2026. **Base normativa auditada:** [PR #124](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/124), commit `b10a3e72f93a352b90003529283c51685a863dfb`, 54 CF-NOR H em 15 módulos. **Main operacional de referência:** `866665bbfc84c0b37167cbdb8ef88e013a733287` (20 H; CF-GOV-019 e CF-CC-019/020 integradas). A branch de pesquisa deriva de uma versão anterior da main; rebase/reconciliação antes de qualquer merge. **CLF não alterado.**

## 1. Preflight sob a política CF-GOV-019

**Carteira concorrente**: (I) repetir diagnóstico da CI — ganho marginal momentaneamente **bloqueado**: jobs com `runner_id=0`, nenhuma etapa, duas anotações indisponíveis; issue [#120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120). (V) aprofundar uma ficha CF-NOR isolada — risco de melhora local redundante. (**Escolhida**) (A) testar INTERFACES entre garantias já redigidas, rigidez constitucional, Parlamento, cumprimento de direitos e tratados — não exigia novo conteúdo normativo e permite bloquear regressões **antes** de ratificar variantes.

**Ganho esperado:** evidenciar falhas que uma inspeção por módulo não percebe e oferecer portas concretas F6. **Ganho documental obtido:** matriz verificável de 16 testes em quatro interfaces e mapa preciso de consequências. **Não inferir** que os 16 testes representam 16 decisões judiciais, 16 antinomias demonstradas ou pesquisa empírica: são hipóteses adversariais classificadas. **Critério de parada:** não multiplicar casos enquanto não houver uma decisão de arquitetura ou proposta específica de resolução comprovadamente necessária.

## 2. Constatações objetivas e sua classificação

### A. Regra de reforma e núcleo inderrogável — M00 × M01 × M02 × M04 × M06 × M14

A leitura do [anteprojeto com 54 H](../redacao/anteprojeto-de-trabalho.md) revelou **ausência de dispositivo expresso** sobre limites materiais ao poder de reforma, como os atualmente previstos no [art. 60 §4º CF/1988](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm), que protege quatro categorias: federação, voto direto/secreto/universal/periódico, separação dos poderes e direitos e garantias individuais. Isso **não** significa que cada direito H desapareceu: a CF-NOR-0051 protege características do voto, a 0055 preserva entes autônomos, a 0052 enuncia independência judicial e a 0004 aplicação imediata. O que falta é **testar a resistência desses conteúdos a emendas tendentes a aboli-los**.

**Evidência textual específica:** busca por `reforma`, `cláusula pétrea` e `abolir` na vista normativa não retornou seções; `emenda` consta apenas na cláusula de tratados 0036 e na anterioridade eleitoral 0045, nenhuma descrevendo as quatro limitações materiais do art. 60 §4º. **Porta F6:** antes de qualquer alegação de anteprojeto completo, elaborar matriz do poder constituinte derivado, quóruns, temporalidade, sujeitos, limites e tutela. **Não criar ou votar uma cláusula pétrea por impulso operacional.** Casos I24-01–04.

### B. Remissões institucionais ainda dependem do modelo de Parlamento — M02 × M03 × M06 × M11 × M13 × M14

**Quatro hipóteses textuais mencionam o Congresso Nacional no corpo normativo:** CF-NOR-0025 (autorização para aproveitamento mineral/hídrico em terras indígenas), 0028 (removal excepcional e controle político), 0036 (tratados de direitos humanos aprovados por cada Casa), 0037 (representação partidária para MS coletivo). A referência **não é erro** se o projeto conservar a mesma estrutura parlamentar; é **dependência expressa**, não resolvida enquanto variantes de Senado/Câmara, sistema de governo e legitimados permanecem H/P.

**A cautela é material:** não substituir `Congresso` por termo genérico sem preservar consulta indígena qualificada, autorização democrática vinculante, acesso coletivo à justiça e quórum reforçado para direitos internacionais. Tampouco transformar a existência desses nomes numa ratificação tácita de bicameralismo. **Porta F6:** tabela de equivalência funcional em todos os modelos A/B/C realmente candidatos, com decisão específica das competências e mecanismos de transição M14. Casos I24-05–08.

### C. Exigibilidade social versus planejamento fiscal e repartição — M01 × M04 × M05 × M06 × M07 × M09 × M14

CF-NOR-0002 trata de encargos e fontes, 0048 de despesas provisórias na ausência de LOA, 0004 de aplicação imediata, 0007 de tutela judicial, 0022 de continuidade de serviços e 0055 de competências concorrentes/comuns. Esses textos **não são automaticamente incompatíveis**. A sua aplicação conjunta, porém, exige distinguir **(i) titular do direito, (ii) ente obrigado, (iii) custeio legítimo, (iv) cronograma de execução, (v) remédio judicial e (vi) urgência comprovada**.

O [STF Tema 698, RE 684612](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=4237089&numeroProcesso=684612&numeroTema=698) estabelece, sob grave deficiência/ausência do serviço, legitimidade de intervenção judicial e, **em regra**, determinação das finalidades com plano ou meios apresentados pela Administração, em vez de imposição pontual automática. Não equiparar o Tema 698 a autorização de gasto sem regime constitucional, nem à negativa de tutela por ausência de dotação. CF-NOR-0056 protege concurso/funções de carreira, mas não obriga concurso **como único remédio** para toda deficiência; o próprio Tema 698 considera outras soluções juridicamente possíveis.

**Ponto crítico adicional:** [art. 37 V vigente](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=37&abrirBase=CF) exige percentuais mínimos de servidores de carreira para cargos em comissão definidos em lei; CF-NOR-0056 não os transcreve expressamente. Isso é **lacuna de continuidade a decidir**, não permissão de eliminar esse controle. Casos I24-09–12; no conjunto, este é o **maior risco de execução**.

### D. Fontes internacionais e direitos de terceiros — M01 × M03 × M06 × M11 × M13

CF-NOR-0036 já distingue assinatura, aprovação e ratificação; 0057 prevê jurisdição complementar do Tribunal Penal Internacional, mas a cooperação doméstica e a denúncia continuam sem desenho. CF-NOR-0025 demanda consulta prévia e específica aos povos indígenas, que **não pode ser substituída** por mera audiência ambiental geral. CF-NOR-0053 assegura crença e objeção sem resolver, por si só, consentimento de pessoas incapazes e proteção de terceiros.

**Não há colisão textual demonstrada entre essas H.** Os casos testam onde direitos especiais poderiam ser esvaziados por aplicações genéricas de tratados, competências ou liberdade de crença. **Porta F6:** jurisdição e procedimento de cooperação, órgãos encarregados de atos internacionais, consulta própria e capacidade/consentimento nos conflitos de direitos. Casos I24-13–16.

## 3. Matriz de evidências e portas

[CSV rastreável de 16 casos](CF_CC_024_INTERFACES_R3_16_TESTES.csv) com ID, normas cruzadas, fonte positiva, situação adversarial, classe, constatação, risco e condição de saída.

| Classe | Casos | Interpretação correta |
|---|---:|---|
| **LACUNA_EXPRESSA** | 5 | Função específica sem disposição correspondente localizada; não equivale a colisão |
| **DEPENDENCIA_INSTITUCIONAL** | 5 | Texto só pode ser fechado após escolha ou desenho de arquitetura aplicável |
| **TENSÃO_A_RESOLVER** | 4 | Coaplicação precisa regras de competência, prova e tutela |
| **RISCO_DE_EXECUCAO** | 2 | Uma regra geral pode ser usada abusivamente contra especialidade ou vulneráveis |

**Situação:** todos os 16 casos estão `ABERTO`; não há código de decisão D, nenhum status `CONCLUIDO` e nenhum "CI green" presumido.

## 4. Pacote de continuidade e escolha da próxima rodada

**FEITO:** análise de 54 H como sistema, não como 54 fichas isoladas; bloqueios específicos dos arts. 60 §4º, 37 V, 231, garantias dos tratados e Tema 698; 16 cenários realmente diferenciados de casos anteriores CF-CC-014–018 (foco na coaplicação e arquitetura).

**PENDENTE:** conferir com o corpus da CF/1988/ADCT de modo integral e parecer humano; resolver escolhas substanciais A/B/C em F6 e a governança da reforma constitucional; alinhar M14 transição, M06 jurisdição, M04 competências, M07 servidores; validar scripts do [PR #128](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/128) em checkout completo e resolver [CI #120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120) quando houver acesso novo. **Não mexer no CLF** nem fechar PRs #101/#104 sem destino por arquivo.

**PRÓXIMO — alternativa marginalmente superior:** em vez de criar uma CF-NOR 0058 sem decisão, produzir **um quadro de requisitos de reforma constitucional e compatibilidade de modelos institucionais** (M00/M03/M14), com alternativas explícitas e proteção mínima das quatro categorias do art. 60 §4º; em paralelo, para a frente executiva M04/M05/M06/M09, testar **um único cenário sintético de proteção da saúde sem LOA e com encargos compartilhados** para descobrir se é preciso corrigir 0048/0002/0055. Priorizar aquele que prove maior possibilidade de alterar a decisão; não aprofundar outra vez este grupo sem resultado novo.

**Critério de aceite futuro:** uma função protegida, uma regra de competência e um remédio exequível identificáveis para cada cenário prioritário; nenhuma passagem H→D, nem merge por letra isolada. **Estado de integração:** branch experimental sobre PR #124, main não alterada.
