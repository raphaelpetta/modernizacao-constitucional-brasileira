# M00.02 — Reservas de lei, fontes normativas e delegações na CF/1988

**ID:** CF-M00.02-EST-001 | **Pesquisa:** F0 delimitado; F1 triagem documental de 53 registros; F2/F3/F4 ainda parciais.  
**Data de corte da pesquisa:** 13/10/2026. **Git de entrada:** CF `be6bcbb60b33cc0680f7e867dbdd689811f237f7`; CLF `64ede4acc03d3e51d8815a1c1635b11e138430d1`.  
**Tarefa:** [M00.02 #15](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/15).  
**Arquivo pesquisável:** [M00-02_INVENTARIO_RESERVAS_CF1988.csv](M00-02_INVENTARIO_RESERVAS_CF1988.csv).  
**Estado das escolhas:** todas as soluções futuras são H/P/A/V; **nenhuma espécie, reserva ou hierarquia da Constituição futura está ratificada**.

## 1. Objeto, fontes e o que foi realmente pesquisado

A questão não é listar todas as vezes que a expressão “na forma da lei” aparece. O objetivo é mapear **qual função jurídica** a Constituição de 1988 reserva à lei ou a outros atos, quem decide, que controles se aplicam e se existe possibilidade de delegação.

**Fonte primária principal:** [Constituição Federal atualizada da Câmara dos Deputados](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html), conferida em 13/10/2026, incluindo emendas que alteraram a federação, o sistema tributário e as finanças. Conferência cruzada pelo [Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm). A fonte atualizada contém dispositivos do **ADCT** e regras de produção futura de efeitos: a existência de texto novo não significa vigência simultânea uniforme de todo o regime.

**Fontes complementares verificadas:**
- STF, [Súmula Vinculante 62 e RE 377.457/Tema 71](https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26&sumula=9347): possibilidade de revogar por lei ordinária disciplina materialmente ordinária inserida em diploma formalmente complementar. **Não inferir** hierarquia universal LC > LO.
- [LC 95/1998, arts. 13–15](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp95compilado.htm): consolidação legislativa preservando alcance dos dispositivos, com procedimentos próprios e limites; não legitima reforma material sob rótulo de transposição fiel.
- [Suíça, Constituição art. 164](https://www.fedlex.admin.ch/eli/cc/1999/404/de): regula disposições normativas importantes por lei formal e delegação sob limite constitucional; versão e redação devem ser datadas no estudo comparado aprofundado.
- [Alemanha, Lei Fundamental art. 80](https://www.gesetze-im-internet.de/gg/art_80.html): habilitação para ato regulamentar deve especificar conteúdo, finalidade e alcance, e o regulamento aponta sua base legal.

**Limites de cobertura:** os 53 registros são amostra dirigida de cláusulas e conjuntos de cláusulas, não 53 leis existentes, não 53 reservas únicas em sentido dogmático e não inventário integral da Constituição. Vários agrupam incisos, outros distinguem no mesmo artigo duas reservas; faltam numerosas remissões setoriais, jurisprudência por dispositivo, ADCT completo, atos normativos autônomos, resoluções parlamentares, direito internacional e regramentos de iniciativa fora dos exemplos. Nenhuma linha significa que a lei exigida já tenha sido editada ou corretamente recebida.

## 2. Taxonomia funcional a testar

| Classe | Função | Exemplos do CSV | Problema a resolver |
|---|---|---|---|
| Reserva material de espécie | Exige LC, lei específica ou lei para assunto definido | arts. 93; 121; 146; 163; 198 §3º | Quando há proteção constitucional justificada para elevar procedimento? |
| Reserva de iniciativa | Exige proposição por órgão determinado | arts. 61 §1º; 93; 165 | Quando protege independência e quando concentra poder de agenda? |
| Distribuição territorial de competência | Atribui competência legislativa ou estabelece cooperação | arts. 22 parágrafo único; 23 parágrafo único; 24; 25 §3º | Uma lei “nacional” precisa ser autorizada por quais dispositivos? |
| Delegação legislativa constitucional | Permite produção de ato com força de lei sob processo especial | arts. 62 e 68 | Como controlar urgência e limites materiais sem normalizar exceção? |
| Delegação/regulação técnica | Permite ajustes operacionais ou variáveis dentro de lei | arts. 84 IV (pesquisa seguinte); 153 §1º | Como delimitar poderes sem travar atualização técnica? |
| Reserva de disciplina ordinária | Pressupõe lei para regulação executiva/social ou serviços | arts. 37 IX; 175; 182 | Quanto da matéria deve ser diretamente garantido na Constituição? |
| Reserva de vinculação material/procedimental | Protege receitas, repartição e financiamento | arts. 161; 165 §9º; 198 §3º | Quais parâmetros não podem ser perdidos em uma lei comum? |

**Nota:** rótulos são instrumentos documentais, não categorias constitucionais reconhecidas universalmente. Uma cláusula pode pertencer a mais de uma classe, e `lei` sem qualificativo não autoriza assumir automaticamente a espécie federal ordinária.

## 3. Seis descobertas com consequências sistêmicas

### 3.1. Reserva de LC não exprime hierarquia geral

Os arts. 59 e 69 distinguem espécies e quórum de lei complementar; a **Súmula Vinculante 62** mostra que matéria meramente ordinária não se torna materialmente complementar só porque inserida numa LC. Isso exige codificar (a) matéria, (b) espécie, (c) iniciativa e (d) órgão e competência, **separadamente**. Não basta criar um catálogo com “nível da lei”.

**Problema candidato CF-PROB-M00-0005 (IDENTIFICADO, não demonstrado como antinomia):** falta de modelo simples e inequívoco para explicitar a função de cada espécie em uma Constituição modernizada.

### 3.2. Mesmo nome de lei cumpre funções muito diferentes

O art. 22, parágrafo único, permite a LC **autorizar os estados** a legislar questões específicas da competência privativa da União; o art. 23, parágrafo único, prevê **leis complementares de cooperação**; o art. 93 reserva LC do **Estatuto da Magistratura**, com iniciativa do STF. Estas reservas não têm a mesma razão de existir. Aboli-las ou convertê-las em lei comum exige três análises institucionais independentes.

**Problema CF-PROB-M00-0006 (HIPÓTESE):** reserva formal uniforme pode esconder funções federativas, institucionais e de garantia distintas.

### 3.3. Regulamentação executiva e legislação delegada não são equivalentes

O art. 68 prevê **lei delegada** mediante resolução do Congresso, com matérias excluídas; o art. 62 prevê medidas provisórias com força de lei e requisitos/vedações próprios; o art. 84, IV, estabelece competência regulamentar para fiel execução das leis. Misturá-los sob o rótulo “poder regulamentar” apaga diferenças de origem, controle e efeitos.

**Problema CF-PROB-M00-0007 (HIPÓTESE):** como enunciar delegações e o limite das decisões essenciais sem delegação legislativa em branco?

### 3.4. A legalidade tributária tem flexibilizações cuidadosamente localizadas

O art. 150, I, impõe reserva de lei para exigir ou aumentar tributos; o art. 153, §1º, permite a alteração de alíquotas de impostos específicos por ato executivo, **condicionada à lei**; o art. 153, VIII, e §6º, distingue LC de instituição e lei ordinária para alíquotas do imposto seletivo. O art. 156-A, §5º, acrescenta extensa reserva de LC ao IBS, associada à reforma da EC 132/2023.

Conclusão restrita: reserva legal e adaptabilidade podem coexistir, mas **não** se conclui daí que toda matéria técnica possa passar ao Executivo. Transição fiscal e garantias de receita exigem estudo M05.

### 3.5. Orçamento e serviços sociais expõem a relação entre lei e execução

Os arts. 163 e 165 §9º reservam LC para matéria financeira estruturante; o art. 165 exige **leis de iniciativa do Executivo** para PPA, LDO e LOA; o art. 198 §3º contém LC para critérios de financiamento interfederativo da saúde. São casos em que espécie normativa, iniciativa, controle parlamentar e direito material convivem.

**Implicação para M01/M05/M09:** não retirar restrições financeiras do texto constitucional sem verificar se o sistema alternativo mantém capacidade real de prestação, tutela e equalização.

### 3.6. “Código único” e “lei única” são escolhas diferentes

O art. 59, parágrafo único, atribui a uma LC a disciplina da elaboração e consolidação; os arts. 13–15 da LC 95/1998 cuidam da consolidação de leis; a CF vigente distribui competências e espécies especiais. Portanto, **o CLF como corpus organizado é conceitualmente distinto de um só diploma legal com força normativa homogênea para todas as matérias**.

A matriz do CLF e as demandas IC-2026-010/026 devem ser examinadas com esse requisito. Se a nova Constituição pretender modificar essas reservas para permitir espécie única, será necessária decisão expressa sobre limites materiais, processo, competências dos entes e preservação de garantias — hipótese ainda aberta.

## 4. Alternativas institucionais sem decisão

**Modelo A — diferenciação mínima:** Constituição, lei parlamentar geral com reservas materiais e exigências específicas de iniciativa, além de regulamentos vinculados à lei. *Pró:* simplicidade. *Contra:* pode deixar sem barreira suficiente matérias sujeitas a autointeresse legislativo e conflito federativo.

**Modelo B — aperfeiçoamento seletivo do brasileiro:** manter distinção de lei ordinária e complementar **somente para matérias reservadas taxativa e funcionalmente**, tornar claras iniciativa, competência, execução e efeitos; delegação delimitada. *Pró:* continuidade. *Contra:* conflitos de enquadramento e veto minoritário persistem.

**Modelo C — lei orgânica/estatutária reforçada:** reservar determinados sistemas eleitorais/institucionais a quórum ou procedimento especial, possivelmente com controle específico. *Pró:* blindagem intermediária. *Contra:* risco de complexidade, bloqueio e judicialização; não confundir proteção de oposição com direito de veto permanente.

**Modelo D — código unificado com diferenciação interna:** examinar como legislação codificada com partes formalmente diferenciadas poderia ser aprovada e atualizada respeitando reservas materiais, procedimentais e territoriais. *Pró:* acessibilidade e coerência. *Contra:* “um diploma” com partes de espécies diferentes carece de construção constitucional muito precisa; um único documento editorial não equivale a único ato normativo.

**Nenhuma alternativa foi escolhida.** As possibilidades de combinar simplicidade e proteção serão testadas pelo M03/M04/M05/M06, com contraditório argumentativo.

## 5. Testes adversariais imediatos

1. **Competência:** União edita lei federal comum regulando integralmente serviço local contra autonomia municipal; conferir se matéria, normas gerais ou cooperação autorizam a intervenção.
2. **Iniciativa:** maioria parlamentar impõe reorganização de órgão judicial cujo projeto era reservado institucionalmente; proteção contra interferência ou impedimento de reforma democrática?
3. **Delegação:** Executivo institui sanção sem hipótese/teto legal determinado, alegando interesse técnico; conferir exigências legais, direitos e contestação.
4. **Tributação:** Executivo amplia incidência de tributo chamando a medida de ajuste de alíquota autorizado; a exceção constitucional alcança somente os parâmetros efetivamente permitidos.
5. **Saúde:** lei comum altera critérios de financiamento que a Constituição reservou a LC, comprometendo equalização; distinguir vício de espécie e consequência material.
6. **Código:** regra infraconstitucional é transposta para ato único cujo processo não satisfaz reserva original; exigir concordância, evidência de equivalência e rastreabilidade de espécie/competência.
7. **Legislador em causa própria:** regras eleitorais são alteradas pelo incumbente; critérios de transparência e estabilidade merecem proteção além da simples escolha da classe de lei.

## 6. Próximo incremento verificável

**F1-B:** ampliar para um levantamento sistemático artigo a artigo da CF/1988 (incluindo ADCT), localizar cada ocorrência e capturar instrumento, competência, iniciativa, remissão e eventuais efeitos temporais, sem interpretar todo “na forma da lei” como reserva exclusiva a lei ordinária. Em segundo passo identificar leis de execução efetivamente promulgadas e alterações.

**F2/F3:** investigar Constituintes, emendas e precedentes sobre os porquês de reservar LC em campos diferentes; cotejar a Suíça (lei formal para regras importantes), Alemanha (limites da delegação), modelos latinos e custos políticos. **Não há estudo causal de impacto realizado.**

**F4/F5:** cruzar inventário com a matriz dos 20 conjuntos CF/1988 e registrar reais conflitos de implementação; testar objeções de proteção de minorias, veto e judicialização.

**F6:** preparar recomendações separadas por função de reserva, sem ratificar espécies até que M03/M04/M05/M06 validem as interfaces.

**Nível de confiança:** localização das 53 referências **conferida no texto atualizado**, mas sua interpretação jurídica, recepção, aplicabilidade temporal ou relação com atos regulamentadores **nem sempre verificada**. Por isso o status é **TRIAGEM_DOCUMENTAL**, não INVENTARIO_COMPLETO, AUDITADO ou INTEGRADO como regime jurídico.

**Nenhuma decisão material adotada nesta rodada.**
