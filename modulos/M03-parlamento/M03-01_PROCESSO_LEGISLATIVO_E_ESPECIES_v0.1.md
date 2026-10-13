# M03.01 — Parlamento, procedimento de lei e espécies normativas: alternativas de arquitetura

**ID:** CF-M03.01-EST-001 | **Data de corte:** 13/10/2026 | **Etapas:** F0 delimitada; F1/F2/F3/F4/F5 parciais; F6 **sem ratificação**.
**Baseline CF:** `6e91df55d8801b1a14e0295b511f5e56dbb100eb` | **CLF:** `c04c78aa5dc42ae8f40da9641c6c4726709d046e`.
**Tarefa:** [issue #18](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/18).
**Interfaces:** M00 (fontes), M02 (eleições), M04 (federação), M05 (finanças), M06 (Justiça), M12 (exceção), M14 (reforma), CLF T01.M04.
**Registros-base:** [M00.02 — 74 fontes](../M00-fundamentos/M00-02_INVENTARIO_RESERVAS_CF1988.csv) e [18 registros ADCT](../M00-fundamentos/M00-02_ADCT_MATRIZ_TEMPORAL_v0.2.csv).
**Natureza:** dossiê de alternativas, **não minuta**, sem assumir presidencialismo/parlamentarismo, duas câmaras de configuração específica ou parâmetros do anteprojeto histórico.

## 1. O problema institucional

Como assegurar legislação democrática, tecnicamente inteligível, controlável e tempestiva, com proteção dos direitos, da oposição e da autonomia federativa, **sem criar um número excessivo de espécies de lei ou novos vetos que imobilizem o Parlamento**?

Há ao menos quatro perguntas que não podem ser resolvidas por uma escala única LC > LO > regulamento:

1. **Competência/âmbito:** legislação nacional, federal, estadual, distrital, municipal; execução e financiamento por quem?
2. **Iniciativa/agenda:** povo, parlamentares, governo, órgãos autônomos e instituições; reserva deve ser material e excepcional.
3. **Caminho de aprovação:** quais câmaras, quórum, consulta territorial, publicidade, tempos de deliberação, emendas e mediação?
4. **Efeito e controle:** lei ordinária, ato com força de lei, delegação limitada, regulamento, ato parlamentar de competência exclusiva, norma vinculante judicial; sanção/veto e fiscalização.

A eficiência deve ser comparada com: custo de veto, captura por incumbentes, proteção de minoria, capacidade administrativa, execução fiscal e qualidade deliberativa, **não somente rapidez de aprovação**.

## 2. Diagnóstico focalizado — direito brasileiro vigente

- **CF/1988 arts. 44–49:** Legislativo nacional bicameral, competências do Congresso e atos de competência exclusiva; cada casa tem atribuições específicas (arts. 51–52). Norma de âmbito nacional não equivale automaticamente a lei de interesse administrativo da União.
- **Arts. 59, 61 e 69:** catálogo formal de emenda, leis complementares e ordinárias, leis delegadas, medidas provisórias, decretos legislativos e resoluções; titularidade/iniciativa por matéria e exigência de maioria absoluta para LC. Essas regras não autorizam supor hierarquia material universal de LC sobre LO.
- **Arts. 62 e 68:** medidas provisórias e leis delegadas são veículos legislativos extraordinários de efeitos e controles distintos; não se confundem com decretos de execução (art. 84, IV) nem organização administrativa de competência constitucional (art. 84, VI).
- **Arts. 64–67:** tramitação bicameral, revisão, sanção/veto presidencial e tratamento de projeto rejeitado na sessão. A especificidade do Executivo atual depende do presidencialismo, podendo ser repensada em modelo de governo diferente.
- **Arts. 165–166:** iniciativa e disciplina orçamentária, emendas e limites de despesa; art. 113 do ADCT exige estimativa de impacto financeiro/orçamentário em determinadas propostas.
- **STF — Tema 917, ARE 878.911:** despesa pública decorrente de projeto parlamentar **não configura por si** invasão da iniciativa do Executivo; a reserva constitucional é relacionada a estrutura/atribuições de órgãos e regime de servidores. Casos recentes anotados pelo STF ilustram contenção de interpretação amplificadora da reserva.
- **STF — RE 377.457/Tema 71 e SV 62:** matéria ordinária veiculada formalmente em LC não adquire por esse simples fato proteção geral de LC.

**Fontes oficiais:** [CF/1988 compilada](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm); [STF, art. 61 e Tema 917](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=61&abrirBase=CF); [STF, Tema 917](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=4744414&numeroProcesso=878911&numeroTema=917); [STF, art. 59](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=59&abrirBase=CF). Consultados em 13/10/2026.

**Limites:** o diagnóstico não esgota regimentos das Casas, precedentes de medidas provisórias, iniciativa, veto, controle de emendas ou a experiência prática de coalizões e comissões. Ainda não há estudo empírico de taxas de aprovação, governabilidade e judicialização, nem reconstrução histórica da Constituinte de 1987–1988.

## 3. Comparação funcional: cinco arranjos

| Modelo comparado | Solução jurídica examinada | Benefício hipotético | Objeção brasileira/transferência |
|---|---|---|---|
| **Alemanha** | Lei Fundamental, arts. 76–78: governo, Bundestag e Bundesrat iniciam leis; participação territorial em toda lei, mas **consentimento obrigatório apenas em matérias enumeradas**, objeção superável em outras; mediação paritária no art. 77 | Diferenciar grau de veto conforme impacto federativo; mediação formal | Escolher matérias de consentimento é litigioso e pode bloquear orçamento/execução, sobretudo em coalizões adversárias |
| **África do Sul** | Constituição, arts. 75–76 e 78: percurso conforme projeto afetar ou não províncias, com poder de mediação; arts. 73 e 77 disciplinam iniciativa e money bills | Intensidade de deliberação territorial vinculada a matéria; classificação formal prévia de proposições | Controvérsia sobre “afeta províncias”, custos de classificação e instituições específicas do país |
| **Espanha** | Constituição, arts. 81–82, 86 e 90: lei orgânica reservada; delegação expressa de conteúdo/prazo; decreto-lei urgente com apreciação parlamentar em 30 dias; veto ou emenda do Senado reversível em termos constitucionais | Separação entre lei orgânica, delegação, urgência e bicameralismo de revisão | Lei orgânica pode ampliar judicialização; urgência normativa pode normalizar excepcionalidade |
| **França** | Constituição, arts. 38, 45–46: ordonnances com habilitação parlamentar e ratificação expressa; mediação intercasas e última palavra da Assembleia em determinadas hipóteses; leis orgânicas submetidas a controle prévio | Combinar desbloqueio parlamentar, garantia de procedimento e controle constitucional | Forte gestão da agenda pelo governo; relação com forma de governo é essencial, não neutralidade institucional |
| **Brasil/1988** | LC com reserva material, poderes do Senado, medidas provisórias, leis delegadas, sancionamento/veto; rito bicameral relativamente geral | Continuidade jurídica, controles conhecidos e representação das unidades federadas | Acúmulo de procedimentos, assimetria de agenda e litígios sobre reserva, distribuição de poder e urgência |

**Fontes primárias:**
- Alemanha: https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html (arts. 76–80); Bundestag https://www.bundestag.de/en/parliament/function/legislation/14legrat-245876 (consentimento versus objeção, explicação contextual).
- África do Sul: https://justice.gov.za/legislation/constitution/chp04.html (arts. 73–79); Departamento de Justiça https://www.justice.gov.za/legislation/legprocess.htm (classificação e tramitação).
- Espanha: https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229 (arts. 81, 82, 86 e 90, consolidação BOE atualizada em 20/05/2026).
- França: https://www.legifrance.gouv.fr/loda/texte_lc/LEGITEXT000006071194/ (arts. 38, 45, 46; consultar versão vigente e não versões históricas isoladas).
**Detalhe institucional sul-africano importante:** no art. 76(1), após insucesso da mediação, a Assembleia Nacional pode, em certas hipóteses, aprovar novamente o projeto com **dois terços de seus membros**, mesmo quando se trate de legislação que afeta províncias; portanto não há veto absoluto universal do Conselho. Fonte: https://justice.gov.za/legislation/constitution/chp04.html (art. 76(1)(e),(i),(j)). Essa superação qualificada é hipótese comparativa de equilíbrio entre autonomia e governabilidade, não solução ratificada para o Brasil.

**Cautela:** descrição de texto legal e explicação institucional não provam desempenho superior. Sem transplantar prazos, quóruns ou órgãos automaticamente.

## 4. Distinção decisiva — ESPÉCIE de lei versus PROCEDIMENTO da matéria

**Hipótese M03-H1:** a Constituição futura pode estabelecer **uma espécie parlamentar geral** com reservas constitucionais de iniciativa, aprovação bicameral e participação territorial especiais, conforme a matéria, sem multiplicar nomes de “leis reforçadas”.

A hipótese não exclui lei complementar materialmente reservada ou espécie institucional reforçada; exige justificar separadamente:
- qual garantia deixaria de existir se o procedimento fosse ordinário;
- por que a própria Constituição e controle judicial não bastariam;
- custo em tempo, veto e interpretação de cada nova classe;
- o que ocorre quando projeto combina matéria ordinária e de consentimento territorial;
- se os requisitos pertencem ao conteúdo inteiro da lei ou podem ser segregados por dispositivo.

**Contraexemplo:** uma lei de saúde nacional pode combinar direitos de pacientes, dados, organização de serviços locais e criação de despesa interfederativa. A classificação rígida de TODO o diploma como “lei institucional qualificada” pode dar veto extra a matérias comuns; a classificação apenas como lei comum pode contornar autonomia e financiamento territorial. Estudar fracionamento/separação de matérias, controle de emendas e rito da parte federativa.

**Não decidir que a futura Constituição terá Câmara alta, Conselho de Estados ou Conselho de Governos** antes do M03/M04; modelos bicamerais são cenários condicionais.

## 5. Três alternativas de estrutura (A/B/C) com melhor objeção

**A — Tipologia simples + procedimentos materiais.** Constituição, lei parlamentar geral e atos infralegais; iniciativa e participação federativa diferenciadas somente em hipóteses expressas. Leis institucionais podem exigir procedimento ou aprovação adicional sem constituir “classe hierárquica” global. **Vantagem:** inteligibilidade e menor contencioso sobre espécies. **Objeção:** salvaguarda insuficiente contra manipulação eleitoral e de órgãos de controle se maiorias ordinárias forem dominantes.

**B — Lei ordinária + lei complementar revisada.** Preservar LC em conjunto pequeno, taxativo, de justificativa democrática/federativa/institucional robusta, distinguindo competência, quórum, iniciativa e consequências de vício. **Vantagem:** transição menos disruptiva e jurisprudência conhecida. **Objeção:** reter quórum especial pode criar veto de minorias e dificuldade em codificar uma lei única de muitas matérias.

**C — Lei orgânica/estatutária delimitada.** Prever veículo reforçado ou rito com fiscalização específica para sistemas de competição e autonomia; comparar França/Espanha/Colômbia. **Vantagem:** possível proteção intermediária. **Objeção:** judicialização de fronteiras, bloqueio da oposição por necessidade de consenso e “segunda Constituição” opaca.

**Posição metodológica P, NÃO escolha constitucional:** utilizar A como **contrafactual de simplicidade**, B como **contrafactual de continuidade** e C como **contrafactual de proteção adicional**; submeter os três aos mesmos testes. A admissão de procedimentos diferenciados em A não transforma automaticamente toda lei em espécie qualificada.

## 6. Esboço condicional de processo legislativo (H) sem redação normativa

Sequência testável: **iniciativa admissível → classificação da matéria/competência → avaliação de impacto e transparência → comissões/participação → deliberação por maioria legitimada → revisão territorial diferenciada SE existir órgão → mediação com prazo e regra de impasse → controle de sanção/promulgação/publicação → impugnação constitucional e aplicação temporal**.

A cada etapa identificar **quem pode bloquear, por quanto tempo e quem resolve o impasse**, sem conceder monopólio de agenda ao Executivo por conveniência administrativa.

- **Iniciativa:** democrática como regra, institucionalmente reservada só por objeto; preservar participação popular e de oposição conforme o M02.
- **Orçamento:** diferenciar lei tributária, orçamento e alteração fiscal; não presumir que toda lei geradora de despesa necessite iniciativa governamental, contrariando a orientação do Tema 917 do STF.
- **Revisão territorial:** testar consentimento para alteração de autonomia/tributos partilhados, objeção superável para leis comuns e mecanismos de mediação antes do veto; alternativas sem bicameralismo devem oferecer proteção territorial substitutiva.
- **Comissão de mediação:** se houver duas câmaras, composição proporcional e representação territorial; checar transparência e possibilidade de acordo sem refazer tramitação inteira. Risco de barganha oculta e de contrabando legislativo.
- **Urgência:** estabelecer exceções materiais, fundamentação, prazo, revisão parlamentar e tutela judicial; não conceder urgência legislativa permanente a atos executivos.
- **Publicação/autenticidade:** ato não deve entrar em vigor sem publicidade e prova de versão, órgão, competência e procedimento; interface com CLF.

## 7. Testes adversariais: matriz separada

A [matriz de 12 cenários M03.01](M03-01_TESTES_PROCESSO_LEGISLATIVO.csv) e a [triagem simulada de 10 matérias](M03-01_TRIAGEM_MATERIAS_PROCEDIMENTOS.csv) documentam impasse bicameral, governo sem maioria, manipulação de espécie, iniciativa, urgência, lei mista, regimentos, orçamento, representação local, fiscalização judicial e interface CLF. Cada cenário confronta **desenho excessivamente permissivo** e **desenho excessivamente rígido**.

A pesquisa não determina regras de preferência do usuário: todas permanecem H/P/A/V.

## 8. Auditoria inicial de garantias e interfaces

- **M01/M02:** efeitos sobre legalidade, sufrágio, regras eleitorais e oposição; não permitir reforma oportunista por lei comum disfarçada.
- **M04/M05:** consentimento territorial para finanças compartilhadas, encargos e equalização; reconstituir calendário do ADCT antes de substituir transição.
- **M06:** independência judicial e iniciativa institucional, controle de espécie/competência e tempo de decisão; evitar transformar juiz em legislador cotidiano.
- **M12:** poderes emergenciais e proteção de direitos indeclináveis.
- **M14:** distinção de emenda constitucional e lei ordinária/qualificada, eficácia de tratados e mecanismos de transição.
- **CLF T01.M04:** corpus editorial único pode armazenar normas heterogêneas sem convertê-las em instrumento único; a aprovação de códigos reformadores exige competência e processo por matéria.
- **Forma de governo não resolvida:** iniciativa do Executivo, veto, sanção e dissolução mudam profundamente em parlamentarismo versus presidencialismo. Não codificar solução antes do módulo competente.

## 9. Próximo ciclo e porta de deliberação

**F1 aprofundamento:** jurisprudência completa sobre iniciativa, emendas parlamentares a projetos reservados, vetos, urgência, comissões, controle de tramitação e PECs; dados reais do Congresso (por origem, espécie, tempo e rejeição) com fontes e métodos.

**F2 histórico:** Constituinte de 1987–1988, reformas de medidas provisórias (EC 32/2001), normas de finanças e agenda legislativa; distinguir intenção da prática comprovada.

**F3 comparado:** replicar análise além de texto normativo, sobre frequência de veto/medição, transparência, bloqueio e revisão constitucional nos sistemas examinados.

**F4/F5 decisão comparada:** testar A, B e C no mesmo cenário de governo minoritário, duas câmaras divergentes, emergência, proteção territorial, baixa capacidade estatal e corrupção; parecer M04/M05 e M06; somente então submeter escolha material.

**F6:** nenhuma escolha ainda ratificada; não emitir CF-NOR. O merge deste dossiê documenta pesquisa e **não** aprova estrutura constitucional. 
