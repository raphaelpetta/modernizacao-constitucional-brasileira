# M03.03 R05-C — Conselho executivo C3: seleção, coalizões, cartel, quórum, urgência
**Corte:** 15/10/2026. Estado H/A/V, sem ratificação F6/D/F7, sem CF-NOR, CF-DEC nem CLF. Confronta C3 com I1, F1/F2, A e B, usando a MESMA base TSE histórica do R05-S. Material reprodutível: `M03-03_05_SIMULADOR_C3.js` e `M03-03_05_CENARIOS_C3_COLEGIALIDADE.csv`.

## 1. Duas fontes e a hipótese distinta do Conselho
- Fonte numérica: TSE, 513 deputados eleitos em 2022, tabela ajustada pelas novas totalizações até 20/07/2024. https://www.tse.jus.br/eleicoes/tabela-com-a-representatividade-dos-partidos-politicos-e-das-federacoes-na-camara-dos-deputados-e-no-senado-federal .
- Fonte conceitual: Stephen Gardbaum, *The case for plural executives in the age of strongmen*, I•CON 24(3), jul/2026, https://doi.org/10.1093/icon/moag084 . Executivo verdadeiramente plural exige poder superior compartilhado, não ministros subordinados a um primeiro-ministro que detém palavra final.
- Controle empírico: Ganghof 2026 AIG comparada, https://doi.org/10.1080/13510347.2026.2700743 ; seleção parlamentar e mandato protegido podem coexistir com colegialidade suíça ou concentração personalista, conforme partidos e competências.

C3 de teste: Conselho superior de cinco (número DIDÁTICO) responsável por decisões estratégicas; ministros exercem administração legal e executam diretivas válidas, mas não possuem governança política superior paralela; presidência rotativa sem poder geral de rever deliberação colegiada. Para políticas novas, exigir 4 presentes e 3 votos afirmativos; para nomeações sensíveis, alternativamente 4 votos E controle externo. Regras H, não norma constitucional escolhida.

## 2. Métodos alternativos de eleição de cinco conselheiros
**E1 — cinco escolhas separadas por maioria absoluta da Câmara:** maioria mínima 257 de 513. Uma coalizão ARITMÉTICA PL99+União59+PP47+Republicanos40+MDB42 = **287** poderia eleger cinco candidatos alinhados, se disciplinada e livre de exigência legal de diversidade, mesmo que os cargos sejam formalmente colegiados. Isso demonstra ausência de garantia institucional de pluralidade por votação simples; não afirma que esses partidos votariam unidos nem que escolheriam de fato cinco nomes idênticos em orientação.

**E2 — cinco cadeiras proporcionalmente distribuídas com D'Hondt segundo o PESO DAS BANCADAS HISTÓRICAS:** cálculo de quocientes sobre 513 cadeiras e 16 agrupamentos partidários com representação dá **PL 2, Federação Brasil 1, União 1, PP 1**. Nenhum partido tem 3, mas PL2+União1 forma maioria interna **3/5** se cooperarem, apesar de PL+União somarem apenas **158/513 ≈ 30,8%** dos deputados. Isso NÃO mede influência política real, apenas demonstra que pequena magnitude do órgão amplia efeitos de arredondamento e facilita maioria de agrupamentos internos diferentes da maioria legislativa. Alternativas proporcionais, como Sainte-Laguë e STV, podem distribuir as cinco cadeiras de maneira diferente; não houve comparação empírica de preferência de voto para esses sistemas.

**E3 — duas listas concorrentes de coalizão hipotética, 287 contra 226, cinco lugares D'Hondt:** resultado **3×2**. Mesmo assegurando duas posições minoritárias, os três representantes da maioria podem decidir ordinariamente se coesos. Para fiscalizar seus próprios atos ou nomear controladores, talvez seja necessário voto de quatro + instância independente; essa rigidez pode provocar veto estratégico e vacância prolongada. Não declarar representação partidária “garantida” apenas com cinco posições.

**E4 — composição escalonada:** eleição de uma vaga por ciclo/ano pode impedir tomada IMEDIATA de cinco lugares por uma única maioria, mas permite que uma maioria duradoura ocupe todos gradualmente, e pode conservar Conselho de legitimidade desatualizada após mudança popular. Seriam necessárias regras objetivas de duração, vacância, proteção de mandatos e sincronização com eleições; não foram simulados dados temporais brasileiros reais.

**E5 — escolha popular proporcional:** linha C2/Page-Shapiro-Talmon, *Electing the Executive Branch* (2020), https://arxiv.org/abs/2009.09734 ; torna mais exigente provar competição, coerência dos cinco cargos e responsabilidade de conselho. Sem dados de cédulas de aprovação/preferências para o eleitorado brasileiro, não validar artificialmente suposta proporção partidária direta.

## 3. Sete verificações reprodutíveis sobre “cartel” 3 de 5
| Caso | Situação | Presentes | Votos favoráveis | Regra | Resultado |
|---|---|---:|---:|---|---|
| C01 | 3 aliados e 2 contrários presentes | 5 | 3 | quórum 4; sim 3 | aprova |
| C02 | ausente um dos opositores | 4 | 3 | quórum 4; sim 3 | aprova |
| C03 | ausente um integrante do cartel | 4 | 2 | quórum 4; sim 3 | não aprova |
| C04 | ausentes os dois opositores | 3 | 3 | quórum 4; sim 3 | sem quórum |
| C05 | ausentes dois do cartel | 3 | 1 | quórum 4; sim 3 | sem quórum |
| C06 | nomeação sensível com 3 aliados | 5 | 3 | sim 4 | não aprova |
| C07 | nomeação com 3 aliados + 1 oposição | 5 | 4 | sim 4 | aprova |

**Achado novo:** exigir colegialidade 3/5, sem contrapesos, permite ao cartel de 3 decidir a agenda, nomear ministros e dominar atos ordinários. Exigir 4/5 em tudo dá poder de veto estrutural a quaisquer dois integrantes e pode atrasar ações constitucionalmente devidas. **Não existe quórum mágico de anticaptura.** A regra adequada depende da matéria, título legal, duração do mandato, independência do controle e consequência do impasse.

## 4. Testes de responsabilidade estratégica e continuidade
**Risco T1 — maioria estratégica de três nomeia o próprio juiz/auditor:** separar indicação, avaliação técnica, aprovação parlamentar com pluralidade e titularidade de destituição por justa causa com prova. Não permitir nomeação/destituição sem controle independente por conselho autor do fato fiscalizável.
**Risco T2 — 2×2 e um ausente durante desastre:** não há autorização de política NOVA sem voto mínimo. Ministro legalmente autorizado pratica socorro conservatório, uso de recursos já autorizados e atos inadiáveis, com motivação contemporânea, duração curta, fiscalização imediata. Exceção de guerra, intervenção e suspensão de direitos NÃO pode ser deduzida da rotina de socorro.
**Risco T3 — dois ausentes:** apenas 3 presentes. Administração segue atos ordinários já competentes; um presidente rotativo não passa a ter poderes políticos ilimitados. Exigir procedimento legítimo e tempestivo de suplência/eleição, não designação secreta por quem dirige gabinete.
**Risco T4 — ministro executa deliberação ilegal 3×2:** voto/ata sob sigilo proporcional, assinatura, ordem material e executor identificáveis a juiz/auditor; o voto vencido é prova, mas não imunidade automática. Garantia do devido processo individual.
**Risco T5 — LOA rejeitada por dois exercícios:** Conselho permanece sob mandato protegido e somente executa gastos autorizados e obrigações exigíveis nos termos constitucionalmente válidos; Conselheiros NÃO podem criar tributos ou autorizações por maioria interna. Continua bloqueio político fiscal.
**Risco T6 — colegiado capturado por um mesmo partido:** C3 pode concentrar substancialmente mais poder que Executivo unipessoal fiscalizado, se o colegiado controlar agenda, nomeações, defesa, orçamento e o próprio órgão de auditoria. Evitar associar “cinco pessoas” a “cinco poderes independentes”.
**Risco T7 — divisão entre ministros e Conselho:** a administração não pode ser segundo governo à sombra; ministros respondem por execução legal, Conselho por direção política válida, ambos por ilícitos próprios.

## 5. Confronto com executivos unipessoais e responsabilidade
**I1** (Presidente eleito por Parlamento sem censura) é fraco como solução anticaptura: mesmo mandato rígido de A, sem eleição popular presidencial. **F1** (Presidente eleito pelo Parlamento e removível por maioria negativa) admite troca política, mas sem maioria para substituição produz vacância; **F2** (censura construtiva presidencial) preserva sucessor mas reproduz bloqueio quando não há maioria positiva. **A** preserva titularidade clara e eleição direta, mas mandatário pode continuar bloqueado; **B** substitui governo ao haver sucessor, mas pode criar premiê dominante e necessita freios internos. C3 só melhora anticaptura se distribuição REAL de agenda e fiscalização reduzir coordenação de captura. A/B/F também podem receber limites de nomeação, urgência, prestação de contas e decisões colegiadas ministeriais, sem trocar forma de governo.

## 6. Três configurações para R06, sem preferência normativa de mérito
- **C3-P:** Conselho de cinco selecionado por regra proporcional verdadeira e mandato protegido; matérias ordinárias 3/5, nomeações sensíveis com requisito externo e/ou 4/5; ministro executivo vinculado, não premiê oculto.
- **C3-E:** mandatos escalonados e seleção pluripartidária sujeitos a regra de não substituição política arbitrária; salvaguarda temporal pode preservar dirigentes de maiorias passadas.
- **C3-R:** colegiado politicamente responsável à Câmara com moção de censura CONSTRUTIVA de um conselho sucessor completo ou parcialmente substituível (hipótese nova); testar risco de vacâncias múltiplas e supressão da autonomia colegiada.

**Portas jurídicas e administrativas:** M02 representação/voto/eleição dos conselheiros; M04 participação federativa; M05 proposta/execução fiscal; M06 nomeação e responsabilidade, oposição e publicidade; M07 competência ministerial; M12 cadeia de defesa e emergência; M14 transição/proteção de mandatos. Sem pareceres setoriais, PR #100 permanece apenas pesquisa.

**FEITO:** três métodos de eleição calculáveis + seleção escalonada e direta examinadas conceitualmente, D'Hondt 5 lugares baseado em bancadas, blocos 287/226, sete verificações de quórum e 7 riscos. **PENDENTE:** dados observacionais, preferências colegiadas reais, modelos federativos, impactos do ciclo orçamentário, autorização legal; CI final. **PRÓXIMO:** comparar C3-P/C3-E/C3-R e A/B/F sob exatamente as mesmas regras de nomeação, transparência, direito de oposição e orçamento, evitando atribuir ganhos de controle à colegialidade quando decorrem de controles independentes.
