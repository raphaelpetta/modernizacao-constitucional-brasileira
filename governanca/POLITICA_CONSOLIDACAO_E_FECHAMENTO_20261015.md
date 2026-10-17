# Política de consolidação, auditoria e fechamento — CF

**Vigência operacional:** 15/10/2026, por determinação de coordenação do projeto. **Escopo:** M00–M14, pesquisa, redação, PRs e interfaces do projeto constitucional, sem vincular CLF. **Natureza:** complemento de [CF-GOV-019](19_POLITICA_GANHO_MARGINAL_GLOBAL.md), [CF-GOV-016](16_PROGRESSIVIDADE_DECISORIA.md), [CF-GOV-017](17_EXECUCAO_CAMADAS_E_AUDITORIA.md) e da [política de integração](../central/01_POLITICA_INTEGRACAO_E_CONCORRENCIA.md); prevalecem os controles de garantias e as decisões expressas. **Não aprova nenhuma CF-NOR, hipótese H, transição ou modelo de governo.**

## 1. Mudança de prioridade enquanto houver dívida de integração
A escolha da rodada compara **cobertura H**, **aprofundamento/contraprova V**, **integração técnica I** e **fechamento jurídico/decisório D**. Distinguir ganho *esperado* de resultado *comprovado* e indicar a alternativa preterida. **Integração e conclusão são trabalho substantivo**, mesmo quando não há nova CF-NOR. Não existem quotas rígidas de tempo, pontuação arbitrária ou proibição de explorar nova matéria urgente. Como orientação inicial revisável, preferir remover bloqueio real, auditar direito de alto risco e submeter questão madura a deliberação antes de acrescentar outra H de ganho menor.

**Gatilho da dívida:** três ou mais PRs substanciais dependentes, QA indispensável não executável ou diferença crescente entre a pilha H e a main exigem **triagem explícita de integração** na próxima seleção. Pode prosseguir trabalho independente que evite colisão e proteja garantias; novas pilhas sem critério de integração são excepcionalíssimas e motivadas. Manter no máximo duas frentes profundas ativas, como CF-GOV-019; PR pendente de revisão não é frente nova.

## 2. Protocolo de fechamento em quatro portas separadas
**G1 — Fonte e contexto.** Conferir a versão datada CF/1988/ADCT e, quando necessário, legislação/jurisprudência oficial, titulares, destinatários, exceções, transição, competências e extensão temporal. Registrar fonte não obtida, nunca fabricar completude.

**G2 — Validade documental e técnica.** Verificar ID/ordem, índice, texto canônico e vista regenerada no mesmo commit; reconciliar base Git e PRs paralelos; executar validadores reais ou registrar precisamente que não foram executados, com comandos e razões. Comparação literal, leitura de links e SHA não são CI verde nem auditoria jurídica.

**G3 — Controle jurídico proporcional.** R1: origem, consistência editorial, remissões e efeitos; R2: alcance, conflito interpretativo, exceções e teste de cenário; R3: matriz N:N da proteção vigente e seu destino, efeitos sistêmicos, melhor objeção, alternativas e contraprovas, jurisprudência crítica e, antes de fechamento material, revisão independente identificável. Não atribuir independência humana a autorrevisão de IA. Risco R3 não vira R1 por ser texto curto.

**G4 — Destino inequívoco.** `INTEGRADO_EXPERIMENTAL_H` somente após G1–G3 proporcionais, preservando H/P/A/V e lacunas; `APTO_A_DELIBERAR` quando comparação e incertezas residuais estiverem delimitadas; `RATIFICADO_D` só com manifestação expressa do usuário e registro de decisão. Opções bloqueadas ficam como variantes identificadas; nenhuma escolha por silêncio ou merge.

## 3. Ponto de parada e trilha de deliberação
Para cada controvérsia madura, elaborar **uma ficha curta**, preferencialmente atualizando dossiê existente: problema; alternativas reais (inclusive manutenção); melhor argumento contrário; direitos/competências protegidos; consequências e transição; evidência que mudaria preferência; recomendação **provisória**; pergunta decisória; registro de ratificação **pendente**. Saídas: `APTO_A_DELIBERAR`, `PREFERENCIA_PROVISORIA`, `PESQUISA_FOCAL`, `BLOQUEADO_POR_DEPENDENCIA`. Se investigação adicional não puder alterar escolha material ou proteção, remeter a questão à deliberação do usuário; não prolongar pesquisa por inércia. Questões estruturantes interdependentes não devem ser artificialmente decididas em pedaços.

## 3A. Critérios explícitos de fechamento progressivo e reabertura (PCCP)

**1. Fechamento técnico/documental:** origens, IDs, texto fonte/vista, versões Git e CI do mesmo SHA coerentes; pode ocorrer sem escolha material e sem D. Em risco R3, a etiqueta **não** declara adequação jurídica.

**2. Estabilização material:** decisão expressa do usuário em [03_DECISOES.md](03_DECISOES.md) com questão, data, fonte, alternativas, melhor objeção, alcance **e exclusões**, condicionantes e interfaces. Em R3, antes de D material exige parecer/revisão independente humana identificável, controle não regressivo N:N e efeitos sistêmicos proporcionais; não é aceitável ratificação automática ou fictícia.

**3. Fechamento normativo local:** texto de dispositivo ou conjunto funcional com decisão de redação, relação N:N de direito vigente e proteções, efeitos, exceções, órgão responsável, implementação, custos pertinentes e ponte transitória revisados. Toda remissão a questão aberta mantém indicação de reserva, sem proclamar fechamento integral.

**4. Fechamento sistêmico:** revisar **em conjunto** decisões e dispositivos ligados por eleições/governo/parlamento, tutela/direitos, federalismo/custeio, tratados e transição; conflito novo bloqueia apenas a parte afetada. Uma D orientadora anterior não supera ressalva sistêmica posterior.

**5. Fechamento global:** matriz funcional CF/1988/ADCT e regimes de transição sem omissão crítica, versões integradas, interfaces CLF identificadas (sem transposição automática), auditoria jurídica intermodular independente R3, contraprovas, aprovação expressa de escolhas materiais e texto final gerado validado. A CF vigente não é modificada pelo projeto.

**Reabertura motivada:** fato/julgado superveniente material, falha comprovada, regressão de garantia, incompatibilidade entre D, consequência não antecipada ou revisão expressa do usuário. Guardar a decisão anterior como `SUBSTITUIDA` e justificar impacto e novos testes. Não reabrir por mera alternativa retórica. **Nenhum percentual de completude geral** decorre de 20, 26 ou 56 H.

**Saída deliberativa:** usar rótulos operacionais com motivo em [pauta única](../central/03_PAUTA_DELIBERACAO_PROGRESSIVA.md); declarar separadamente se a questão admite **orientação P** ou **ratificação material D**. Falta de revisão R3 independente não proíbe pesquisar, redigir H, auditar ou coletar orientação P, mas **bloqueia estabilização D/fechamento material**.

## 4. Métricas de resultado e antirredundância
Reportar, **se mensuráveis no checkout indicado**, (a) H na main versus H apenas em PR, sem soma dupla; (b) funções e direitos **efetivamente mapeados**, com denominador de recorte declarado; (c) verificações G1/G2/G3 cumpridas, pendentes ou não aplicáveis **por recorte**; (d) PRs empilhados/bloqueados e antiguidade; (e) questões aptas à decisão, submetidas e ratificadas; (f) conflitos e garantias resolvidos. **Não inventar percentual constitucional global** nem usar módulos com H como completude funcional.

Uma única fonte versionada rege cada dado; `redacao/indice.csv` e `redacao/propostas/` regem o texto H, a vista é derivada; dashboards devem ser regenerados e validados, nunca editados para aparentar progresso. Não repetir relato em várias planilhas/pareceres quando link + delta e handoff existente bastam. Registrar somente alterações de estado verificadas.

## 5. Resposta ao bloqueio de CI
A [issue #120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120) documenta falhas de runner **antes de executar steps**; causa não identificada. Prioridade técnica: obter as duas anotações no GitHub, verificar Actions/runner/permissões, reproduzir em checkout fiel `python scripts/validar_repositorio.py`, `python -m unittest` e `python scripts/gerar_anteprojeto.py --check` e corrigir **somente a causa demonstrada**. Um novo `failure` sem steps não prova defeito das hipóteses normativas nem satisfaz QA. Enquanto houver bloqueio, exceções documentais estritas só após comprovação alternativa proporcional; não promover texto R3, novos scripts ou dados gerados sob pretexto de CI indisponível.

## 6. Aplicação inicial verificável e próximo checkpoint
**Fotografia de entrada em 15/10/2026:** main com **20 H**, pilha [PR #124](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/124) com **54 H no total** (34 adicionais, não aditivas à main); [PR #125](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/125) integrou governança seletiva; [PR #126](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/126) propõe cobertura/guia; [#101](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/101) e [#104](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/104) conservam resíduos, e #59/#107 são paralelos. **Não** contar estas informações como estado atual sem nova leitura.

**Próximas candidatas em ordem condicionada ao ganho marginal:** (I) diagnosticar CI #120 e reconciliar dados/scripts residuais #101/#104; (I/V) preparar a reconciliação do stack 54 H com main e variantes paralelas, por lotes juridicamente auditáveis e sem promoção a D; (D/V) selecionar questão já madura e produzir ficha de deliberação com garantias e alternativas; (H) nova cláusula só quando superar claramente esses retornos. Cada ciclo termina com `FEITO / PENDENTE / PRÓXIMO`, Git SHA e testes efetivos. Reavaliar a regra após dois ciclos com entregas e bloqueios reais, não somente com novos documentos.

**Interface CLF:** transmitir apenas demandas específicas à [central CLF #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48); não importar norma, decisão ou cronograma do CLF para CF.
