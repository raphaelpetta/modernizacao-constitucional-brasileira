# PCCP-Q01 — cinco fichas funcionais condicionais PB-T01/T02/T05/T09/T11

**Corte:** 17/10/2026. **Classificação:** pesquisa e especificação de interfaces `V/A/H-documental`, **sem norma CF-NOR**, sem proposta de política ratificada e sem decisão constitucional `D`. Origem: [CF-DEC-006 — P-B exclusivamente provisória](../../governanca/03_DECISOES.md); [roteiro de 12 contraprovas, com âncoras ao PR #107](M03_PCCP_Q01_12_CONTRAPROVAS_20261016.md); [funil F6](../../central/04_FUNIL_DECISOES_F6.csv). **Estado dos cinco casos:** `ESPECIFICACAO_CONDICIONAL` + `R3_PENDENTE`.

**Pergunta deste artefato:** para cada evento hipotético, identificar separadamente **gatilho, sujeito competente no direito vigente, função hipotética a localizar em eventual texto novo, rito, decisão controlável, efeito transitório, evidência faltante e condição de parada**. Onde houver variante, descrevê-la como **campo aberto**: nenhuma distribuição futura de competências está escolhida ou validada.

## Fontes positivas, com alcance delimitado

- [Câmara dos Deputados — Constituição de 1988 atualizada até EC 139/2026](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html), inclusive ADCT. Conferir a redação **vigente** antes de qualquer emenda proposta; este projeto não modifica o direito vigente.
- [STF — ADI 3.685/DF](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=3685), julgamento 22/03/2006: anterioridade do art. 16 aplicada ao alcance temporal da EC 52/2006. **Não** julga uma PEC de parlamentarismo.
- [STF — ADI 5.525 e art. 81 da CF](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=81&abrirBase=CF): disciplina do processo eleitoral em vacância; **não** resolve admissibilidade de nova eleição presidencial indireta **ordinária**.
- [PR #107, HEAD `33790b7c493bb839d39a35831d3571895a6bf5c8`](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/33790b7c493bb839d39a35831d3571895a6bf5c8/modulos/M03-parlamento/M03_CC002_PROTOTIPOS_CONSTITUCIONAIS_A_B_C_v0.1.md): fonte **experimental externa** dos enunciados B-01…B-06, A-01…A-05, C-01…C-05.
- [PR #130, HEAD `ff6ea0c74d4c33347b201cf2acf7b317db11c49a`](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/ff6ea0c74d4c33347b201cf2acf7b317db11c49a/modulos/M03-parlamento/M03_CC025_EQUIVALENCIA_FUNCIONAL_ABCP123_v0.1.md): estudo experimental **não ratificado** de atribuições parlamentares P1/P2/P3 e quatro remissões.

## PB-T01 — investidura inconclusa e governo de continuidade

| Campo funcional | Informação documentada ou questão verificável |
|---|---|
| **GATILHO** | Assembleia/Câmara recém-instalada não conclui a votação de investidura na primeira tentativa, em hipótese de protótipo B-01 |
| **ATORES_VIGENTES** | Na CF/1988 não há investidura parlamentar ordinária do Presidente nem cargo constitucional de Primeiro-Ministro; arts. 76–84 tratam do Executivo presidencial e os arts. 44–52 do Congresso |
| **FUNCAO_CONDICIONAL** | Identificar Câmara que decide a investidura; autoridade que certifica resultado; eventual chefe de Estado que formaliza nomeação; governo de continuidade sob competência delimitada |
| **RITO_CONDICIONAL** | Registrar iniciativa, candidatura, quórum, primeira tentativa, novas tentativas, condição objetiva de fracasso, motivação e publicidade; B1/B2 do PR #107 permanecem **alternativas de texto**, não regras aprovadas |
| **CONTROLE** | Acesso à fiscalização parlamentar e à jurisdição quanto à regularidade de rito, sem tribunal escolher maioria ou Primeiro-Ministro; atos da autoridade interina sujeitos a limites e prestação de contas |
| **EFEITO_TRANSITORIO** | Nenhum ocupante pode ser investido por Câmara ainda não instalada; manter continuidade de atos com título vigente até marco jurídico válido; datas, mandatos e sucessões seguem sem decisão |
| **PROVA_FALTANTE** | Texto da sequência completa, capacidade e impedimentos da autoridade interina, número/prazo das tentativas e remédios com legitimados; matriz M03/M06/M14 |
| **CONDICAO_DE_PARADA** | Se os elementos não estiverem especificados, marcar `LACUNA_DE_RITO`, manter B-01 em H e não inferir admissibilidade nem ratificação |

**Rastreio:** PB-T01 ⇄ PROT-M03-B-01, B-05 e A-01/A-04 (identificação textual, não julgamento de políticas).

## PB-T02 — investidura obtida sem aprovação da LOA

| Campo funcional | Informação documentada ou questão verificável |
|---|---|
| **GATILHO** | Investidura hipotética válida, mas ausência de aprovação da lei orçamentária anual no momento pertinente |
| **ATORES_VIGENTES** | Executivo propõe PPA/LDO/LOA sob CF art. 165; Congresso exerce atribuições de apreciação e fiscalização orçamentária; execução depende da autorização e vedações constitucionais, especialmente art. 167 |
| **FUNCAO_CONDICIONAL** | Identificar quem propõe, quem aprova, quem executa, quem fiscaliza e quem presta contas em cada cenário; confiança política e autorização de despesa são atos distintos |
| **RITO_CONDICIONAL** | Enumerar separadamente obrigação exigível, título de despesa, dotação/crédito, fonte de financiamento, disponibilidade de caixa, prazo e prestação de contas; não presumir regime automático de duodécimos ou crédito não previsto |
| **CONTROLE** | Parlamento e controle externo verificam autorização e execução; tutela judicial de direito exigível não cria por si crédito nem transforma recursos vinculados em caixa livre |
| **EFEITO_TRANSITORIO** | Regras financeiras e competências de autoridade anterior subsistem até alteração jurídica válida; não transformar a primeira investidura em autorização geral de gasto |
| **PROVA_FALTANTE** | Dispositivo constitucional concreto e norma de LDO do ente/ano, atos orçamentários e identificação de fonte real; cotejar [CF-CC-028](../../auditoria/CF_CC_028_CASO_UNICO_SAUDE_LOA_FEDERACAO_v0.1.md) sem usar valores sintéticos como dados reais |
| **CONDICAO_DE_PARADA** | Sem título, fonte, disponibilização e regime jurídico verificáveis, `LACUNA_FINANCEIRA`; nenhum juízo de execução ou fechamento material |

**Rastreio:** PB-T02 ⇄ PROT-M03-B-04, B-06; A-05/C-04 como referências do material documental.

## PB-T05 — ordens incompatíveis em emergência e defesa

| Campo funcional | Informação documentada ou questão verificável |
|---|---|
| **GATILHO** | Duas autoridades hipotéticas pretendem emitir ordens inconciliáveis sobre defesa, emergência ou segurança |
| **ATORES_VIGENTES** | Na CF/1988, arts. 84, 136–141 e 142 distribuem competências presidenciais, procedimentos excepcionais, participação dos conselhos e controle do Congresso; art. 49 IV prevê atribuições legislativas sobre estados excepcionais |
| **FUNCAO_CONDICIONAL** | Exigir mapa por **ato jurídico**, diferenciando declaração, proposta, referenda, execução, controle político, revisão judicial, prestação de contas e resposta por excesso; não presumir poderes residuais de cargo hipotético |
| **RITO_CONDICIONAL** | Documentar objeto e pressuposto, autoridade iniciadora, forma/assinatura, participação de órgão consultivo, comunicação ao Legislativo, prazo, extensão territorial e medidas coercitivas admissíveis |
| **CONTROLE** | Controle constitucional dos limites materiais dos direitos e legalidade, deliberação/fiscalização parlamentar pertinente, publicidade proporcional, responsabilização e remédios de urgência |
| **EFEITO_TRANSITORIO** | Autoridades constitucionais **vigentes** conservam títulos até implementação juridicamente válida; nova distribuição de defesa não pode ser aplicada antes da investidura dos novos órgãos |
| **PROVA_FALTANTE** | Texto de atribuições de cada ato de intervenção, defesa e sítio; sobreposição de comando, prazo e substituição; revisão M03/M06/M12 e impactos CF art. 5º |
| **CONDICAO_DE_PARADA** | Sem mapa ato→órgão→controle→efeito e sem avaliação do piso constitucional, `LACUNA_DE_COMPETENCIA`; nenhum poder de emergência novo está aprovado |

**Rastreio:** PB-T05 ⇄ PROT-M03-B-02, B-06 e INV-04; C-03/C-04 são referências documentais distintas, não hipóteses implicitamente adotadas.

## PB-T09 — modalidade de escolha da chefia de Estado

| Campo funcional | Informação documentada ou questão verificável |
|---|---|
| **GATILHO** | Uma futura redação hipotética propõe alterar o procedimento de escolha ordinária da chefia de Estado |
| **ATORES_VIGENTES** | Eleitorado escolhe Presidente por sufrágio sob CF arts. 14 e 77; eleição congressual excepcional em dupla vacância está delimitada no art. 81 §1º; art. 60 §4º II protege voto direto, secreto, universal e periódico |
| **FUNCAO_CONDICIONAL** | Documentar poderes efetivos da chefia de Estado, fonte de legitimidade, responsáveis por eleição e investidura, duração, substituição e eventual relação com o gabinete. `B-D` e `B-I` **não estão decididas** |
| **RITO_CONDICIONAL** | Separar modalidade eleitoral, conteúdo real do voto, iniciativa/rito da eventual emenda, direito político, calendário e anterioridade; não tratar consulta como substituição de controle do art. 60 |
| **CONTROLE** | Exame jurídico concreto de compatibilidade dos direitos de voto e garantias individuais, legitimados e momentos adequados de tutela; STF ADI 3.685 e ADI 5.525 possuem objetos próprios e não autorizam inferência automática |
| **EFEITO_TRANSITORIO** | Não alterar mandatos, pleitos, diplomação ou posse atuais por simulação; M02/M14 devem indicar quando cada ato ingressaria em vigor e se incide art. 16 |
| **PROVA_FALTANTE** | PEC ou texto constitucional integral proposto, catálogo de competências do cargo, juízo jurídico da alternativa sobre arts. 16 e 60 §4º, proteção da representação e revisão independente identificável |
| **CONDICAO_DE_PARADA** | Sem texto concreto e matriz jurídico-eleitoral, `LACUNA_DE_ADMISSIBILIDADE`; não concluir pela validade nem invalidade categórica da hipótese |

**Rastreio:** PB-T09 ⇄ PROT-M03-B-02 e INV-05; A-01/C-01 são apenas artefatos condicionais de outras famílias.

## PB-T11 — remissões constitucionais quando mudam as Casas

| Campo funcional | Informação documentada ou questão verificável |
|---|---|
| **GATILHO** | Projeto condicional prevê mudar número, composição ou atribuições de Casas parlamentares |
| **ATORES_VIGENTES** | Congresso sob arts. 44–52; Câmara e Senado possuem atribuições textuais distintas; mudança de nome de órgão não transfere por si quórum ou prerrogativa |
| **FUNCAO_CONDICIONAL** | Identificar para **cada competência vigente** o órgão hipotético iniciador, revisor, autorizador, controlador e legitimado; P1/P2/P3 permanecem campos do PR #130, sem adoção |
| **RITO_CONDICIONAL** | Para cada função, registrar a quantidade de deliberações, forma de representação federativa, quórum, iniciativa, consulta, publicidade, controle e salvaguarda de oposição |
| **CONTROLE** | Preservar garantia material, participação das comunidades e tutela judicial; vedar inferência automática de equivalência entre um voto unicameral e o rito constitucional de duas Casas |
| **EFEITO_TRANSITORIO** | Remissões a Congresso/Câmara/Senado precisam de regra de continuidade para atos pendentes e competências até instalação de nova estrutura; não atribuir ato a órgão inexistente |
| **PROVA_FALTANTE** | Matriz N:N de cada artigo vigente, mapa de competência por variante, processo legislativo especial e parecer jurídico R3 independente |
| **CONDICAO_DE_PARADA** | Sem destinatário, rito e garantia funcional para cada remissão, `LACUNA_DE_REPRESENTACAO`; não redigir remissão genérica a “órgão competente” |

**Quatro funções com parâmetro vigente próprio:**

| FUNCAO_VIGENTE | Fonte constitucional atual | Elementos que futura hipótese deve explicitar (sem declarar equivalência) |
|---|---|---|
| `TRATADOS_DH` | CF art. 5º §3º | Aprovação em **cada Casa**, dois turnos e três quintos, para equivalência a emenda; qualquer estrutura diferente precisa de exame material específico |
| `TERRAS_INDIGENAS_RECURSOS` | CF art. 49 XVI e art. 231 §3º | Autorização do Congresso para aproveitamento de recursos hídricos/pesquisa e lavra em terras indígenas, comunidades ouvidas e participação nos resultados |
| `REMOCAO_INDIGENA` | CF art. 231 §5º | Vedação geral, hipóteses constitucionais excepcionais e deliberação legislativa conforme texto vigente; retorno imediatamente que cesse risco |
| `MS_COLETIVO_PARTIDO` | CF art. 5º LXX a | Partido político com representação no Congresso pode impetrar mandado de segurança coletivo; preservar legitimidade processual funcional |

**Rastreio:** PB-T11 ⇄ INV-01, INV-03, PROT-M03-B-06; [PR #130](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/130) contém a análise documental por P1/P2/P3, mas não constitui decisão do projeto.

## Checagem transversal e resultado limitado

| Caso | Estrutura de fato-ato-órgão-rito-controle-efeito | Dado/ato específico faltante | Situação após esta rodada |
|---|---|---|---|
| PB-T01 | Identificado como campos de documento, sem preencher escolha | Investidura, tentativas, quóruns, títulos de continuidade | `ESPECIFICACAO_CONDICIONAL` / `R3_PENDENTE` |
| PB-T02 | Identificado como campos de documento, sem autorizar gasto | Norma financeira do ente/ano e fonte real | `ESPECIFICACAO_CONDICIONAL` / `R3_PENDENTE` |
| PB-T05 | Identificado como campos de documento, sem alterar comando | Catálogo de atos excepcionais e controles | `ESPECIFICACAO_CONDICIONAL` / `R3_PENDENTE` |
| PB-T09 | Identificado como campos de documento, sem escolher eleição | Projeto/PEC e direitos eleitorais concretamente afetados | `ESPECIFICACAO_CONDICIONAL` / `R3_PENDENTE` |
| PB-T11 | Identificado como campos de documento, sem fechar Parlamento | Remissões N:N e garantia efetiva por órgão | `ESPECIFICACAO_CONDICIONAL` / `R3_PENDENTE` |

**Resultado realmente obtido:** cinco quadros funcionais com campos e referências documentadas, quatro remissões parlamentares rastreáveis e condições claras para distinguir **ausência de dado**, **contraprova pendente** e **ratificação D não autorizada**. Não há aqui avaliação de desempenho, comparação ou escolha de política constitucional. Não há parecer humano R3, solução de impasses, novo artigo CF-NOR ou fechamento material.

**FEITO:** tornar reproduzível a verificação a solicitar para cada situação, preservando o direito vigente. **PENDENTE:** atos, quóruns, direitos afetados, fontes orçamentárias, variantes integrais M02/M03/M04/M05/M06/M12/M14, controle intermodular e parecer jurídico independente G3. **PRÓXIMO:** cruzar as cinco fichas com os demais sete casos do roteiro, mediante evidência material nova; encaminhar deliberação D somente com objeto jurídico completo, G1–G4 aplicáveis e ratificação expressa.
