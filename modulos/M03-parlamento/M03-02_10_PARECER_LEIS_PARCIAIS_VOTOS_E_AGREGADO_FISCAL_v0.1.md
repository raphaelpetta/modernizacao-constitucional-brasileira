# M03.02.10 — Votos fiscais parciais não substituem autorização, financiamento nem orçamento anual
**ID:** CF-M03.02-EST-010 · **Data de corte:** 14/10/2026 · **Issue:** #84 · **PR:** #85 (draft) · **main preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **Estado:** F0–F5/F8 pesquisas H/P/A/V, F6 NÃO decidido, F7 não iniciado. Nada CF-NOR/CF-DEC-D/CLF nem main.
**Propriedade:** M03, interfaces necessárias M03.01/M04/M05/M06/M07/M14 e, se houver dissolução, M02. O projeto Brasil alternativo não é decisão constitucional deste repositório.

## 1. Três perguntas distintas por medida
**P1 político:** Quantos deputados querem aprovar essa proposta específica? Uma derrota da LOA não é igual a derrota de toda despesa, e maioria favorável ao hospital não se converte em voto de confiança.
**P2 jurídico:** A autoridade competente pode apresentar, deliberar e aprovar o objeto com o procedimento/quórum correspondente? Voto simples não supera matéria de iniciativa reservada, competências federativas, vedações, condições e limites de endividamento.
**P3 material/financeiro:** Há obrigação válida, dotação/autorização provisória apropriada, recursos disponíveis NÃO DUPLICADOS, caixa, estimativa de impacto e execução possível? Uma votação positiva não cria dinheiro. Exige-se visão fiscal agregada, mesmo que leis especiais sejam votadas separadamente.

**Teste falsificável:** Se em L2 o orçamento inteiro perde por X46 contra Y+Z54, o partido Z pode, em outro ramo hipotético, votar com X em projeto de manutenção hospitalar: X+Z56 contra Y44. A mudança de voto depende da matéria e é apenas hipótese. Ela não implica aprovar o orçamento nem garantir a legalidade financeira da proposta. No L3/P2, A+C45 podem obter F8 numa lei hospitalar: SIM53 contra B+D+E47. Esse voto não vira apoio contínuo ao gabinete.

## 2. Quatro medidas modeladas e a ressalva das transferências federativas
**HOSP — crédito/lei de manutenção de hospital e obrigação exigível**: obrigação constitucional/legal, competência, instrumento apropriado e recurso disponíveis, controle material da saúde. Sem caixa, a prestação pode continuar em risco apesar de 53 ou 56 votos.
**ESCOLA — manutenção de escola/rede pública**: distinguir serviços obrigatórios de criação de programa novo; custeio, pessoal e aumento de demanda de Y1–Y3 exigem avaliação atualizada.
**CONVENIO — autorização fiscal complementar para convênio municipal vigente**: existe instrumento válido e condições cumpridas? Crédito/repasse não nasce apenas do voto. Não equiparar convênio condicionável a receitas constitucionalmente pertencentes a estados/municípios.
**DIVIDA_NOVA — contratar nova dívida para financiar despesa**: mesmo com 56/53/55 votos favoráveis, a competência, a finalidade constitucional, as autorizações próprias, limites e sustentabilidade continuam a exigir exame. Pagar dívida anterior e contratar nova dívida são coisas distintas.

**REP_CONSTIT — controle SEM votação constitutiva de nova titularidade**: parcelas de receita pertencentes aos entes segundo CF/1988 arts.158–160 não devem ser tratadas como programa facultativo a aprovar apenas se uma maioria apoiar o Governo. O desenho futuro da repartição cabe M04/M05, mas o teste contém uma salvaguarda: **não colocar em votação legislativa se município "merece" receber parcela já devida**, salvo matérias normativas distintas dentro de competência constitucional. Oito controles em CSV incluem, além disso, obrigação exigível, programa expirado e nova dívida nas duas legislaturas.

## 3. Votações: 24 contrafactuais matematicamente auditáveis
Matriz `M03-02_10_24_VOTACOES_LEIS_PARCIAIS.csv`: 2 legislaturas × 4 objetos × 3 **ramos alternativos por proposta**, e não uma sequência histórica de 24 votações. Os 100 assentos e 51 como maioria absoluta são apenas laboratório; este exercício usa **SIM>NÃO** como critério ilustrativo de apoio político à lei especial, não quórum constitucional aprovado. Não afirmar que a lei foi aprovada juridicamente porque SIM>NÃO.

| Câmara/ramo | Bloco SIM | Bloco NÃO | Apoio à medida, ilustrativo |
|---|---|---|---|
| L2/V1 | X+Z = 56 | Y = 44 | SIM>NÃO |
| L2/V2 | Y+Z = 54 | X = 46 | SIM>NÃO, mas iniciativa de oposição precisa exame |
| L2/V3 | X = 46 | Y+Z = 54 | NÃO |
| L3/V1 | A+C+F = 53 | B+D+E = 47 | SIM>NÃO |
| L3/V2 | B+D+E+F = 55 | A+C = 45 | SIM>NÃO, mas iniciativa de oposição precisa exame |
| L3/V3 | A+C = 45 | B+D+E+F = 55 | NÃO |

**Método de construção:** votos de todos os partidos somados pelas cadeiras da matriz R03, sem absentismo artificial, total sempre 100. V1/V2/V3 são **contrafactuais alternativos em cada proposta**, nunca inferir que uma mesma coligação se repetiria em quatro matérias ou por três exercícios. Nenhuma lei ou despesa teve resultado jurídico calculado. Em V2, especialmente, a oposição forma maioria numérica mas não se presume iniciativa válida para abrir crédito ou contratar dívida no regime vigente/futuro.

**Fonte das bancadas:** `M03-02_03_COMPOSICAO_LEGISLATURAS.csv`. **Ramo L2:** L2/P2 DERIVAÇÃO PRÉ-CONFIANÇA após t4; NÃO incluir t5–t6 originais, em que o gabinete X sofre derrota formal de confiança. **Ramo L3:** L3/P2 sem voto voluntário de confiança e sem sucessor eleito. Crise de LOA não dissolve/derruba por si.

## 4. Direito financeiro brasileiro e limites da analogia francesa
- **Lei 4.320/1964 arts.40–43:** suplementares reforçam dotação, especiais atendem despesa sem dotação específica, extraordinários atendem urgência/imprevisto nos pressupostos legais. Suplementares/especiais são autorizados por lei e requerem **recursos disponíveis**, com justificativa; os créditos adicionais pressupõem uma estrutura legal de orçamento e NÃO fornecem, só pela definição, autorização automática a Executivo sem LOA em qualquer hipótese. Fonte oficial Câmara consolidada: https://www2.camara.leg.br/legin/fed/lei/1960-1969/lei-4320-17-marco-1964-376590-normaatualizada-pl.html .
- **LRF LC 101/2000 arts.15–17:** para criação/expansão/aumento de determinadas despesas, estimativa de impacto orçamentário-financeiro, adequação e compatibilidade e origem de recursos para obrigação continuada conforme os pressupostos e exceções da própria lei. **Uma lei específica não é atalho para ignorar impacto**. Fonte: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm .
- **CF/1988 arts.165–169 e 167 V–VII, art.166:** reserva de orçamento, iniciativa/emendas em hipóteses próprias, créditos, proibição de autorização de crédito ilimitado; proteção federal/territorial e art.167 §7º (EC128/2022) sobre imposição de encargos legislativos de serviços públicos sem previsão de fonte/repasse, com exceções. Fontes: https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html e https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc128.htm .
- **França — LOLF art.45:** permite procedimentos especiais quando orçamento anual não está pronto, incluindo voto da primeira parte ou lei especial para continuidade da cobrança dos tributos existentes seguida de decretos para serviços votados, com discussão da LOA continuada. **Lei especial francesa NÃO significa que cada despesa isolada seja automaticamente votável com mera maioria ou que o Brasil precise reautorizar anual e especialmente impostos já exigíveis**. Fonte: https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044611965 . O Governo francês aplicou regime provisório em 2025 e 2026, mas suas regras próprias de crédito não equivalem às brasileiras: https://www.budget.gouv.fr/reperes/loi_de_finances/articles/loi-speciale-2026-en-attente .
- **Não presumir** lei fiscal parcial futura idêntica a crédito especial existente: a competência de iniciativa, especialidade, impacto plurianual e proteção de minorias devem ser aprovadas no futuro sistema; M03.01 e M05 devem emitir parecer.

## 5. Doze testes de integridade do conjunto fiscal
Matriz `M03-02_10_12_TESTES_COHERENCIA_FISCAL.csv`, 2 legislaturas × 3 ramos de voto × 2 hipóteses de custeio:
1. **SEM FONTE COMPROVADA:** SIM>NÃO não torna gasto legal sem financiamento verificável. Não aprovar despesa financiada por uma mesma rubrica já comprometida.
2. **FONTE INDIVIDUAL PRESUMIDA COMO H:** mesmo supondo que cada proposição possua cobertura individual, a alocação pode ser dupla e o conjunto pode contrariar limites globais, dívida e obrigações irrenunciáveis. **Não se inventa quantia nem se declara equilíbrio**.
3. **MAIORIA FORMAL INSUFICIENTE:** V2 pode ter maior apoio de deputados opositores, mas sem iniciativa constitucionalmente válida; DIVIDA_NOVA tem controles próprios em qualquer caso; V3 perde votação de apoio mas não extingue obrigação exigível.
4. **COERÊNCIA AGREGADA:** examinar fonte não duplicada, validade da LOA anterior, programas findos, limites reais de crédito, direito das pessoas/entes e vínculo entre políticas anuais. Se todas as leis especiais estiverem aprovadas, ainda assim não constituem a LOA total aprovada.
5. **CENTRALIDADE DO ORÇAMENTO ANUAL:** exigir reenvio e debate do agregado anual, tornar públicas autorizações especiais, cada uma com rastreabilidade de fonte/impacto, e proibir que Executivo use leis pequenas para governar estruturalmente sem controle.

## 6. Contraexemplos e objeções máximas
**S1 — maioria por objeto não significa coalizão de governo:** L3/V1 aprova hipoteticamente hospital com F, mas F pode rejeitar educação ou orçamento completo em ramo distinto. Não afirmar governabilidade geral.
**S2 — maioria da oposição sem competência de iniciativa:** L2/V2 e L3/V2 podem representar maioria para projeto de iniciativa governamental, MAS não para projeto que o Parlamento não possa iniciar ou ajustar. Requer M03.01 sobre direito de emenda, fonte e iniciativa, sem copiar regra federal vigente automaticamente para nova Constituição.
**S3 — saúde + educação + convênio somam mais do que fonte:** não inventar números; possibilidade lógica de **dupla contagem** de recurso e efeitos para municípios requer mapa de compromissos.
**S4 — dívida nova para “salvar serviços”:** aumenta restrição futura, pode infringir limites e regras materiais; voto favorável não valida operação.
**S5 — lei especial vira orçamento atomizado permanente:** o Governo pode esconder impacto conjunto, a Câmara aprovar itens populares e vetar receita, e fiscalização ficar incapaz de reconstituir prioridades. Resposta P possível: orçamento global anual obrigatório como prestação de contas/apresentação/votação procedimental, limite material nas leis parciais e catálogo público de créditos, **sem sanção automática de dissolução pela LOA rejeitada**.
**S6 — receita partilhada como chantagem:** titularidade constitucional de receita de entes, dadas as condições constitucionais, não é medida discricionária do gabinete nem deve ser submetida a plebiscito de popularidade do primeiro-ministro.

## 7. Protocolo de parecer e escolha
**P de engenharia, NÃO D:** manter P1 autorização mínima, P2 leis fiscais especiais sob fonte/competência, P3 debate anual e P4 controle objetivo, como quatro salvaguardas cumulativamente testáveis. R10 demonstra **possibilidade aritmética** de maiorias setoriais diferentes, e NÃO comprova ocorrência ou viabilidade financeira dessas votações. Uma Câmara fragmentada pode aprovar hospital sem aprovar LOA, mas também pode falhar nas quatro propostas e continuar responsabilizando politicamente Executivo.
**Porta F6 de orçamento parcial permanece BLOQUEADA:** M03.01 espécie e iniciativa; M05 cobertura, dívida, autorização fiscal multianual, custeio e dados; M04 consentimento e titularidade territorial; M06 tutela e controle; M07 execução; M14 transição. Sem essas respostas não há redação CF-NOR, quórum, data nem privilégio do pacote B sobre A/C.
**Próximo M03.02.11:** explorar como impedir o orçamento em fragmentos sem dar Executivo o poder de forçar confiança/dissolução: matriz de **reconciliação global de créditos específicos**, controle preventivo de fontes duplicadas e calendário parlamentar, junto a melhores objeções de M03.01/M05/M04.