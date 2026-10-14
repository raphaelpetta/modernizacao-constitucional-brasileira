# M11.01-R4 — Parecer de requisitos cumulativos para recursos minerais e hídricos em terras indígenas

**Sessão:** CF-M11.01-S004 · **Data de corte:** 14/10/2026 · **Issue M11:** [#92](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/92) · **PR #94:** draft.  
**Main no preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **HEAD PR94 de entrada:** `6b1334f74761960411a802e180a846ceef9cea12`.  
**Objeto:** pesquisa F1–F5 sobre **autorizações, participação, consulta, outorga, estudo ambiental e reparação**, sem proferir decisão material F6/D, selecionar arquitetura A/B ou criar `CF-NOR`.

## 1. Regra vigente por ato, titular e tempo

A [Constituição compilada](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm) contém regime cumulativo de atos **juridicamente diferentes**:

| Nível | Texto e conteúdo vigente | Função e ator | O que NÃO supre |
|---|---|---|---|
| **Bens e direito de uso** | CF art.20 VIII (potenciais hidráulicos), IX (minerais/subsolo), XI (terras tradicionalmente ocupadas); arts.176 caput e 231 caput/§2 | União como titular dos bens constitucionalmente indicados; povo com posse permanente e usufruto constitucional das riquezas do solo, rios e lagos, em regime próprio | Propriedade da União não implica disponibilidade irrestrita do território, e o usufruto não dispensa regras especiais de subsolo |
| **Autorização parlamentar** | CF art.49, XVI e 231 §3 | **Congresso Nacional** autoriza a exploração/aproveitamento hídrico e pesquisa/lavra mineral **em terras indígenas**; é ato distinto de licença administrativa | Não dispensa ouvir comunidades, concessão/outorga ou EIA |
| **Oitiva constitucional especial** | CF art.231 §3 | Comunidades indígenas afetadas devem ser **ouvidas** no processo de autorização; não é mera audiência ao público em geral | Não autoriza por si a pesquisa/lavra; não implica veto universal automaticamente |
| **Participação econômica específica** | CF art.231 §3, parte final | Comunidades têm participação **nos resultados da lavra, na forma da lei** | Não é sinônimo de receita bruta, de multa, de reparação ambiental ou de compensação de outro instituto |
| **Regime de exploração e autorização/concessão federal** | CF art.176 caput/§1 | Recursos minerais/potenciais hidráulicos pertencem à União; o regime federal de autorização/concessão deve ter **condições específicas por lei** para terras indígenas | Não se substitui por autorização de Câmara/Congresso nem por simples escolha de cooperativa |
| **Consulta e salvaguardas convencionais** | [Convenção OIT169 arts.6–7 e 15](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10088.htm), Anexo LXXII Decreto10088/2019 | Consulta apropriada aos povos diretamente afetados por medidas legislativas/administrativas; art15 disciplina recursos e participação/indenização nos pressupostos próprios | Audiência ambiental genérica/parecer de órgão não comprovam consulta; hierarquia interna permanece **M13.01 #93** |
| **EIA/licenciamento ambiental** | CF225 §1 IV/§§2–3, [Lei15.190/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm) e [Lei15.300/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm) conforme modalidade | Prévio EIA publicizado para significativa degradação e demais atos/licenças legalmente exigíveis; reparação e sanções independentes | Não substitui Congresso, consulta nem condições especiais da CF |
| **Controle e tutela** | CF arts.5 XXXV,129 V/III, 231/232 e 225; decisões aplicáveis | Comunidades, organizações, MP e legitimados conforme via própria; poder de fiscalização | Nem aprovação administrativa nem compensação afastam controle judicial e recuperação ambiental |

**Atenção ao art.176 §4 (aproveitamento de renováveis de capacidade reduzida):** a dispensa ali indicada de **autorização/concessão ordinárias** não pode ser lida automaticamente como derrogação do regime especial de CF231 §3/CF49 XVI. Conflitos de âmbito e exceções requerem confronto do texto completo, sem inferir licença para empreendimento indígena.

**Atenção ao art.231 §7 c/c art.174 §§3–4:** as garantias gerais de estímulo a garimpo/cooperativismo desses dispositivos **não se aplicam, por força da regra especial**, às terras indígenas. Uma cooperativa estabelecida sob condições judiciais Cinta Larga em MI7516 não transforma a regra geral de garimpo em direito automático nacional.

## 2. Fato judicial de 2026 que altera materialmente a pesquisa

O [MI 7.516, processo STF](https://portal.stf.jus.br/processos/detalhe.asp?incidente=7420379), teve cautelar em 06/02/2026 e **referendo em 13/08/2026**, certificado pelo Plenário. [Notícia oficial STF do referendo](https://noticias.stf.jus.br/postsnoticias/congresso-tem-24-meses-para-editar-lei-sobre-mineracao-em-terras-indigenas-decide-stf/). A decisão reconheceu omissão do Legislativo, impôs **prazo de 24 meses** para lei nacional sobre mineração indígena e fixou condições provisórias **relacionadas à Terra Cinta Larga**, cuja destinação concreta depende de atos futuros, sem liberar exploração automaticamente.

Os **oito blocos** de [`M11-01_R4_FICHA_MI7516_REGIME_CINTA_LARGA_v0.1.md`](M11-01_R4_FICHA_MI7516_REGIME_CINTA_LARGA_v0.1.md) separam desintrusão de atividade ilegal, consulta, 1% condicional da terra demarcada, preferência/cooperativa/autorizações, **50% calculado sobre o valor devido aos entes e órgãos descritos na decisão**, destinação financeira, EIA/manejo e reparação.

**Cautela de jurisdição e hierarquia de normas:**
- **24 meses, 1% e fórmula de 50%** derivam da cautelar no **MI**, não são parte literal da CF231 nem de uma lei ordinária nacional vigente.
- A **área de até 1%**, se autorizada a exploração, é **condição provisória Cinta Larga** e não limite para terras indígenas de qualquer povo.
- A fração financeira **não significa 50% do faturamento bruto da mina**; exige identificar precisamente o montante judicial usado como base.
- A criação de **cooperativa** e a **preferência** do povo não dispensam Congresso, outorga da União, consulta e EIA; o próprio [STF declarou que o julgamento não autoriza mineração imediatamente](https://noticias.stf.jus.br/postsnoticias/congresso-tem-24-meses-para-editar-lei-sobre-mineracao-em-terras-indigenas-decide-stf/).
- Não concluir que o regime provisório de **mineração** em Cinta Larga se estenda a **hidrelétricas** ou a minas em outras terras.
- Em **02/06/2026**, STF determinou plano para retirada de **garimpo ilegal** daquela região; a proteção contra ilícito é distinta de autorização futura condicionada.

**Objeto distinto:** o [ARE 1.425.370](https://noticias.stf.jus.br/postsnoticias/stf-avanca-no-processo-de-escuta-do-povo-cinta-larga-sobre-mineracao/) discutiu coleta de manifestação dos Cinta Larga também sobre atividades no **entorno** do território. Escuta para fins de instrução processual, decisão judicial do caso, consulta convencional e autorização constitucional não são conceitos intercambiáveis. O próprio STF descreveu em 12/06/2026 a preparação dessa escuta como insumo à decisão, não autorização automaticamente produzida.

## 3. Distinção de consulta e autorização conforme tipo de decisão

**Consulta convencional — OIT169 arts.6 e 15:** o art.6 trata de medidas legislativas/administrativas suscetíveis de afetar diretamente os povos abrangidos; o art.15(2) acrescenta procedimentos de consulta antes de prospecção/exploração pelo Estado titular de minerais/subsolo e participação/indenização nos pressupostos. O dever de boa-fé e representação apropriada não é idêntico a consulta popular geral.

**Oitiva constitucional do art231 §3:** é requisito especial no âmbito de autorização congressual de aproveitamento hídrico e pesquisa/lavra em terra indígena. A forma de sua interação com a consulta convencional e o resultado das manifestações deve ser verificada **por procedimento real e campo de incidência**, sem afirmar uma audiência formal suficiente por si ou consentimento com efeito vinculante universal.

**Autorização do Congresso — art49 XVI:** é ato de competência constitucional especializada, não autorização econômica ilimitada; não serve de licença ambiental ou de autorização de domínio territorial da União para ignorar usufruto tradicional.

**Atos administrativos:** a outorga mineral/energética e a licença ambiental têm competências e finalidades diferentes; podem exigir estudos e manifestações próprias. Ausência de uma dessas etapas não é sanada pela conclusão de outra.

**Participação econômica vs. reparação:** CF231 §3 aponta participação nos resultados **da lavra**, OIT169 art15 inclui benefícios quando possível e indenização equitativa por dano; CF225 §§2–3 mantém restauração e sanções/reparação em regime próprio. **Não criar equivalência contábil entre participação nos resultados, compensação financeira por recurso, tributo, dano moral e obrigação de recuperar o meio ambiente.**

## 4. Testes concretos hipotéticos e confronto com textos M10

A [matriz R4 de 17 funções](M11-01_R4_MATRIZ_CUMULATIVIDADE_RECURSOS_NATURAIS.csv) discrimina fontes **constitucionais**, **convencionais**, **legais** e **judiciais específicas** e cita os alvos A/B da M10. Os [12 casos adversariais R4](M11-01_R4_TESTES_CUMULATIVIDADE_E_REGIME_MI.csv) incluem licenciamento isolado de hidrelétrica, decisão congressional sem consulta, cooperativa sem outorga, garimpo ilegal Cinta Larga, percentuais judiciais indevidamente generalizados, mina externa com impacto direto e participação financeira usada erroneamente como quitação de dano.

Em [M10 R9](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/89), os trechos **`A-TEXTO-11` e `B-TEXTO-04/B-TEXTO-10`** fazem **remissões genéricas a direitos originários e consulta**, sem transpor literalmente autorização parlamentar CF49 XVI, oitiva especial, participação econômica CF231 §3, condições de bens e outorga CF176 ou capacidade postulatória CF232. O M10 A-04/B-03 reproduz hipótese de EIA, e A-07/A-08 e B-06/B-07 referem recuperação, **mas esses deveres não suprimem nem substituem os direitos territoriais**.

O **MI7516 não deve ser escrito literalmente na Constituição experimental** como lei fiscal universal; sua existência serve de **caso adversarial de transição** a distinguir norma, decisão, titular e extensão, sujeito a revisão se houver nova decisão ou lei.

## 5. Questões jurídicas abertas e resposta parcial à M10 F05

1. **M13.01 [#93](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/93):** hierarquia e incorporação da OIT169 e eventuais efeitos da relação com legislação minerária; **nenhum parecer emitido nesta rodada**.
2. **M03:** técnica para autorizar pelo Congresso e relação com nova distribuição de competências constitucionais; art49 XVI e art231 §3 exigem auditoria simultânea na CF alternativa.
3. **M05:** estrutura de participação financeira na lavra e fórmula **judicial Cinta Larga**, sem confundir com repartições financeiras ambientais comuns; seu campo é intermodular.
4. **M10/M07:** EIA, modalidades de licença e fiscalização, discussão atual da Lei15.190/2025; não atribuir resultado às ADIs7913/7916/7919 e ADC102 sem decisão de mérito verificada.
5. **M06/CLF:** direitos processuais, controle de omissão e combate a mineração ilegal, proteção e reparação.
6. **M11:** titularidade, organização/representatividade e direitos próprios, não previsão de um empreendimento concreto.

**Resultado:** a ficha F05 da M10 já recebeu parecer **parcial** da M11 (R1–R3); a R4 acrescenta critérios específicos sobre recursos e notícia judicial **confirmada** do MI7516 com seu objeto restrito. **Não demonstra equivalência completa** dos dois textos experimentais, não ratifica modelo A/B e não altera as decisões em aberto.

**FEITO:** as categorias cumulativas, MI7516, 17 funções e 12 testes. **PENDENTE:** parecer de hierarquia M13, revisão de Congresso M03, efeitos de eventual lei/decisão superveniente e prova de casos reais. **PRÓXIMO:** completar a interface F05 do M10 com a distinção da autorização congressual, consulta, participação e licença, e encaminhar a M03/M05 a separação de responsabilidades sem gerar nova ficha canônica.
