# M01.13 — Alternativas de redação para reservas de intrusão e tutela de dados

**ID:** CF-M01-S013-R1 · **Corte:** 14/10/2026 · **Estado:** **H/P/V, estudo editorial de alternativas NÃO ratificadas**. **Nenhuma nova ficha CF-NOR, nenhum ID reservado, nenhuma alteração ao texto de `CF-NOR-0030/0031`**. Estes trechos são **contramodelos independentes para deliberação**, não fonte canônica da Constituição; eventual redação aprovada como H deverá ser vertida a `redacao/propostas/`, após reserva e atualização por gerador.  
**Base:** CF main `5ac08b622d7552b7d3b37a695a3027b4b9d827d4`; [PR #59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59), H/draft, head de entrada `62161a6b9eb7dc62aad6efe4c914b1bd85fee411`; [issue #57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57). **Interface:** parecer M06 em [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62), `M06-02_PARECER_INTERFACE_PRIVACIDADE_PR59_v0.1.md`; M07, M12, M13; garantia geral `CF-NOR-0007` H.

## 1. Diagnóstico de não equivalência jurídica

**`CF-NOR-0030` atual no PR:** protege vida privada, domicílio e comunicações, mas **remete** ingresso e interceptação às "hipóteses e garantias específicas desta Constituição" que ainda não constam do anteprojeto. "Autorização judicial quando constitucionalmente exigida" não é norma especial substitutiva. **`CF-NOR-0031`:** direito autônomo de dados, contestação e autoridade independente; não contém remédio judicial gratuito funcionalmente comparável a art. 5º LXXII/LXXVII (habeas data).

**Parâmetros vigentes primários:**
- CF art. 5º **XI**: domicílio inviolável, consentimento, flagrante delito, desastre, socorro, determinação judicial **durante o dia**; **XII**: sigilo de correspondência/comunicações com exceção textual de comunicações telefônicas sob ordem judicial e finalidade penal; **X/LVI**: vida privada/prova ilícita; **LXXII/LXXVII/LXXIX**: habeas data, gratuidade e proteção de dados.
- **STF Tema 280 (RE 603616, 2015):** ingresso forçado sem mandado inclusive à noite só em fundada razão prévia para flagrante, posteriormente justificada, sob nulidade e responsabilidade. Não justificar entrada abusiva pela droga descoberta depois.
- **STF Tema 977 (ARE 1042075, Pleno 25/06/2025, acórdão publicado 24/09/2025):** apreensão física de celular ≠ acesso aos dados; se encontrado fortuitamente, há exceção estreita de acesso identificador sem prévia decisão, com justificativa posterior; aparelho regularmente apreendido/flagrante tem acesso aos dados condicionado a **consentimento livre e expresso ou ordem judicial fundamentada**, ressalvada hipótese delimitada; preservação de dados/metadados pode ocorrer antes da ordem sob requisitos; tese **prospectiva**, ressalvados pedidos defensivos anteriores ao fim do julgamento. **Não** afirmar ordem judicial necessária para toda e qualquer visualização, nem que apreensão autorize devassa.
- **Lei 9.296/1996**: interceptação do fluxo em comunicações telefônicas/informáticas/telemáticas, ordem judicial e lei; não é regime de toda consulta a arquivo local.
- **Lei 9.507/1997**, art. 7º (conhecimento/retificação/anotação) e art. 8º, parágrafo único (prova de recusa ou **10 dias** sem decisão para acesso, **15** para retificação/anotação). Prazos são **legais** e podem ser modernizados com garantias efetivas.
- **LGPD art. 20**: revisão de decisões **unicamente automatizadas** que afetem interesses; redação atual **não inclui direito universal a revisão por pessoa humana**; art. 18 e art. 22 tratam direitos e defesa individual/coletiva.

## 2. Três arquiteturas de redação (H, NÃO ADOTADAS)

### Modelo A — proteção explícita semelhante às reservas atuais, atualização digital complementar

**A1. Domicílio, E da cláusula 0030, trecho de trabalho:**

> É inviolável o domicílio. Ninguém nele poderá ingressar sem consentimento válido de quem o ocupa, salvo em situação de flagrante delito ou desastre, para prestar socorro, ou, durante o dia, por determinação judicial fundamentada. O ingresso forçado fundado em flagrante, sem ordem judicial, depende de razões concretas anteriores à diligência e de justificação posterior sujeita a controle judicial, sob responsabilidade e invalidade da prova obtida ilicitamente.

**A2. Comunicações, E da cláusula 0030, trecho de trabalho:**

> É protegido o sigilo das comunicações privadas, qualquer que seja o meio empregado. A interceptação de comunicações em curso dependerá de ordem judicial fundamentada, nos casos e pelo tempo previstos em lei para investigação criminal ou instrução processual penal, com controle da execução e proteção das informações não pertinentes. O acesso coercitivo a dados e mensagens armazenadas observará a garantia de intimidade, a reserva judicial aplicável e as exceções estritas constitucionalmente admitidas.

**A3. Tutela de dados, E do regime de M06 vinculado a 0031, trecho de trabalho:**

> Toda pessoa terá tutela judicial efetiva e gratuita para conhecer informações relativas a si constantes de registros governamentais ou de caráter público e para obter a sua retificação quando cabível, assegurados os meios de anotação de contestação nos casos da lei. O procedimento será célere, com requisitos razoáveis de prévia solicitação ao responsável, sem exigência de exaurimento administrativo nem prejuízo da proteção contra urgência irreversível.

**Vantagem:** manutenção explícita de direitos/limites de 1988 e de funções essenciais de HD; adiciona neutralidade técnica sem dar carta branca à lei. **Objeções:** risco de copiar ambiguidades históricas de comunicação em vez de fixar política digital coerente; menção à exceção "constitucionalmente admitida" pode continuar sem objeto; o rol "flagrante" também exige prova e justificação. O A2 precisará de complemento escrito sobre a exceção do Tema 977 — não deixar tudo implicitamente à lei.

### Modelo B — reserva por intensidade da intrusão, tecnologia-neutra e remédio funcional

**B1. Domicílio, trecho de trabalho:**

> O domicílio e os espaços em que se desenvolve a vida doméstica não poderão ser objeto de ingresso ou busca estatal contra a vontade de seus ocupantes, salvo mediante ordem judicial individualizada, executada nas condições constitucionais e legais, ou nos casos de socorro urgente, desastre ou flagrante comprovado por fundamentos objetivos e sujeito a imediata documentação e controle judicial posterior. A lei assegurará limites de finalidade, duração, escopo e integridade dos registros da diligência.

**B2. Comunicações, conteúdo e dados, trecho de trabalho:**

> São invioláveis a confidencialidade das comunicações privadas e a esfera informacional da pessoa. Medidas de interceptação do fluxo comunicacional e de investigação invasiva de conteúdos pessoais exigirão fundamento legal preciso, finalidade constitucionalmente legítima, delimitação individualizada, proporcionalidade estrita, decisão judicial prévia quando exigida por esta Constituição e fiscalização independente. Exceções de urgência ou de identificação estritamente necessárias somente poderão ocorrer em hipóteses constitucionais expressas, documentadas e revisáveis judicialmente, vedada a exploração geral sem autorização adequada.

**B3. Remédio funcional, trecho de trabalho:**

> É gratuita e célere a tutela judicial da pessoa para acesso, correção e, nas hipóteses da lei, anotação de contestação de dados pessoais em registros públicos ou de caráter público; serão admitidas medidas preventivas e urgentes para evitar danos graves, com proteção dos direitos de terceiros. O direito aos meios administrativos e judiciais adequados contra demais responsáveis pelo tratamento de dados pessoais permanece assegurado.

**Vantagem:** mais neutralidade técnica e distinção por finalidade/intensidade, sem congelar o CPP/LGPD. **Maior perigo:** "quando exigida" e "hipóteses expressas" ainda geram **remissões vazias** se não existir cláusula especial que defina precisamente **quais acessos** precisam de ordem e **quais exceções** se admitem. A referência a proteção "da esfera informacional" deve ser coordenada com `0031`, não repetida como um terceiro direito solto. O termo "imediata" em B1 não pode prejudicar socorro.

### Modelo C — cláusula geral + delegação ampla à lei (contramodelo adversarial)

> A privacidade, o domicílio e as comunicações serão protegidos na forma da lei, que estabelecerá as condições de acesso das autoridades e a tutela dos dados pessoais.

**Razão para não recomendar:** facilita substituição por permissões legais genéricas de invasão, interceptação ou taxação do acesso/correção de dados; nem preserva reserva judicial, hipóteses de exceção ou gratuidade de remédio. **Só poderia superar o teste** se outra disposição constitucional já determinasse tudo isso de modo materialmente equivalente, o que não se comprovou.

## 3. Alternativa modular recomendada para TESTAR, não para aprovar

**Modelo A como piso de segurança + neutralidade digital de B sob portões explícitos**, organizado como:
1. `CF-NOR-0030` **permanece** direito substantivo (A) sem incorporar ritos; acrescentar **uma especialização E** de domicílio e **outra E** de sigilo/interceptação com hipóteses e jurisdição, se a auditoria exigir;
2. `CF-NOR-0031` **permanece** direito autônomo de dados, com remédio de acesso/correção **E conduzido por M06** — alternativa de nome habeas data vs descrição de função aberta; regulamentação de prazos e formas pela lei;
3. `CF-NOR-0007` **continua** norma geral de tutela sem duplicar no texto do remédio todas as garantias gerais;
4. M12 define especiais de investigação e prova ilícita, M07 fiscalização/procedimentos, M04 competência, M14 recepção/transição.

**Nenhum ID CF-NOR novo foi reservado**: a rota editorial depende de consulta a `redacao/indice.csv`, PRs e `governanca/15_REGISTRO_RESERVAS_IDS.md` no dia de criação. A especialização E deve ser citada expressamente pela 0030 antes de afirmar equivalência.

## 4. Questões deliberativas separáveis

- **PRI01:** preservar rol explícito de ingresso (consentimento, flagrante, desastre, socorro, ordem diurna) ou reescrever em termos de intensidade e fundamentação sem reduzir proteção?
- **PRI02:** limitação tecnológica neutra à interceptação de fluxo na lei penal; efeitos sobre correspondência, dados armazenados e prova?
- **PRI03:** qual exceção constitucional estrita para identificação fortuita de aparelho e preservação sem ordem? Evitar transformar Tema 977 em liberação geral.
- **PRI04:** sanções e controle, nulidade de prova, responsabilidade do agente, documentação e contraditório ulterior.
- **PRI05:** manter termo habeas data vs remédio funcional; preservar gratuidade, titulares e natureza dos bancos (não estender automaticamente a qualquer empresa).
- **PRI06:** acesso/retificação/anotação e resposta urgente; limites do pedido administrativo; lei define prazos sem extinguir via judicial.
- **PRI07:** alocação de autoridade independente, autonomia/custeio, dados penais e segregação de poderes.
- **PRI08:** revisão de decisões automatizadas e direito inovador à revisão humana — deve ser escolha explícita, não confusão com LGPD vigente.

## 5. Critério de validação

O arquivo `M01-13_TESTES_ALTERNATIVAS_PRIVACIDADE.csv` registra **20 contraexemplos adversariais** com cobertura A/B/C e `PENDENTE`. Nenhum modelo obtém "equivalência material comprovada" nesta rodada. Antes de transformar alternativas em H oficial exigir **matriz N:N** CF/1988 → proposta e direitos processuais, leitura de jurisprudência STF 280 e 977 e revisão M06/M07/M12, legislação sobre busca domiciliar, comunicações e dados; conferir competência federativa/servidores e custos.

## Fontes oficiais consultadas

- [Constituição vigente, Planalto](https://www4.planalto.gov.br/legislacao/legis-federal/constituicao), art.5 X–XII, LVI, LXXII/LXXVII/LXXIX.
- [STF Tema 280, RE603616, tese e trânsito](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=280).
- [STF Tema 977, ARE1042075, julgamento 25/06/2025 e tese integral](https://portal.stf.jus.br/processos/listarProcessos.asp?classe=ARE&numeroProcesso=1042075).
- [Lei 9.296/1996, interceptação](https://www.planalto.gov.br/ccivil_03/leis/l9296.htm).
- [Lei 9.507/1997, habeas data](https://www4.planalto.gov.br/legislacao/portal-legis/legislacao-por-assunto-OLD/acesso-a-justica-e-processo-judicial/acoes-constitucionais/lei-no-9-507-de-12-de-novembro-de-1997).
- [LGPD Lei13.709/2018, arts.18/20/22](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).
- [Parecer funcional M06/PR62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62).

## Continuidade
**FEITO:** três famílias de redação A/B/C com 6 trechos de teste material, diferenciação de remédios, oito perguntas e 20 casos; texto CF-NOR0030/0031 original **não editado**. **PENDENTE:** certeza da melhor redação de reservas digitais, remissão expressa a exceções de acesso, controle pós-ingresso, jurisdição e HD, auditoria material por todos atores, decisão H oficial e eventual decisão D. **PRÓXIMO:** elaborar proposta reconciliada de *especialidades E* em colaboração M06/M12/M07, com matriz de concordância linha a linha, antes de reservar IDs. **Local:** material de pesquisa dentro do PR59 draft; nenhuma mudança à main.
