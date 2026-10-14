# M03.02.08 — Teste bienal de impasse: continuidade material de direitos, fiscalidade e eleições sem gatilho espúrio
**ID:** CF-M03.02-EST-008 · **Data de corte:** 14/10/2026 · **Issue:** [#84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84) · **PR:** [#85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85) (draft) · **main preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`.
**Estado:** H/P/A/V; F0–F5/F8 de pesquisa. F6 sem deliberação, F7 não iniciado; nenhum CF-NOR, nenhuma opção A/B/C ou quórum incorporados, nenhuma mudança na main/CLF. M03 lidera interfaces M02/M04/M05/M06/M07/M12/M14.
**Método:** cenários SEM dados monetários, ano civil definido, valores de dívida, classificação empírica ou previsão causal; análises CONDICIONAIS do desenho de futuras competências. Fonte brasileira vigente ≠ hipótese futura de autorização fiscal ≠ marco jurídico alemão/espanhol.

## 1. Resposta direta — o que os dois anos demonstram
Em uma Câmara fictícia de 100 lugares, rejeitar o orçamento durante **Y1 e Y2** não cria maioria para derrubar o gabinete por censura construtiva, não cria nem extingue a exigibilidade de uma obrigação por si, não assegura dinheiro em caixa e não é gatilho suficiente de eleição. Todas as versões FISC-A/B/C e ELE-1/ELE-2 precisam tratar explicitamente a possibilidade de uma crise fiscal duradoura sem eleição antecipada válida.

**L2/P2-derivação PRÉ-CONFIANÇA:** distribuição X46/Y44/Z10. Em R03 L2/P2 a proposta orçamentária perde por X46 contra Y+Z54 e a censura com candidato Y obtém somente Y44 contra X46 com abstenção de Z10. **IMPORTANTE:** a trajetória R03 original continua no t5 com voto formal de confiança derrotado por X46 contra Y+Z54; portanto é incoerente modelar dois anos do MESMO gabinete a partir do L2/P2 integral. Este ensaio **bifurca após t4 e omite expressamente t5–t6**: não há novo voto de confiança nos anos sintéticos Y1/Y2. No direito projetado, poderes de requerer confiança ainda estão abertos. Os números são hipóteses de voto, não realidade parlamentar brasileira.

**L3/P2:** distribuição A27/B23/C18/D14/E10/F8. A+C45, B+D+E47, F8 abstém. A investidura B2 hipotética anterior passou por SIM45/NÃO37/18 abstenções em segunda fase; censura alternativa B+D+E47 NÃO atinge maioria de membros (=51 nesta Câmara fictícia de 100). Orçamento é rejeitado por 45 a 47 com F8 abstendo em Y1 e Y2. Não existe questão voluntária de confiança no ramo L3/P2. **Nenhum eleitor é forçado a aceitar governo do outro bloco** só porque rejeitou lei orçamentária.

**Voto parlamentar** é uma variável política diferente de **qualificação jurídica de despesa**, **fonte orçamentária**, **disponibilidade financeira** e **limites de crédito**. Os resultados das 112 linhas não autorizam dizer “a Saúde recebeu recursos” nem “o hospital parou” sem dados de demanda, caixa e contabilidade real.

## 2. A arquitetura dos 112 testes multianuais
O arquivo `M03-02_08_MATRIZ_112_CONDICOES_FISCAIS.csv` contém:
- 2 legislaturas/ramificações × 8 categorias de obrigação/função × **7 recortes por regime/fase** = **112 condições**, sem percentuais ou números fiscais inventados;
- **FISC-A** em Y1 e Y2: autorização provisória funcional taxativa, inspirada no GG alemão art.111, exigindo base legal de cada obrigação e limitações de crédito;
- **FISC-B** em Y1 e Y2: prorrogação condicionada de dotações válidas anteriormente aprovadas, inspirada na CE espanhola art.134(4) e Lei 47/2003 art.38. Se NÃO existe orçamento novo em Y1, **Y2 não recebe por mágica um novo orçamento anual-base**: a referência válida permanece a última lei orçamentária realmente aprovada (Y0) com exclusão de projetos/obrigações que expiram; revisões/correções exigem competência e rito próprios. Não se assume “capitalização automática” das dotações;
- **FISC-C** em Y1-H1 (regime provisório tipo B), Y1-H2 (tipo A) e Y2-H2 (tipo A). A fase H1 **não reinicia automaticamente em Y2**, pois criar um novo período de prorrogação toda virada de exercício daria ao gabinete instrumento adicional para manipular prioridades; ambos os marcos e as durações concretas permanecem H. Nenhum “apagão” de obrigações no intervalo H1→H2 pode ser constitucionalmente aceito sem prova de direitos e fontes.

As oito categorias **separam funções que não devem ser tratadas como dotações equivalentes**:
1. **SERV_SAUDE:** continuidade de serviço de saúde legalmente instituído e obrigações exigíveis; dimensão material aumenta conforme demanda, custo e direitos, não por mera repetição de rubrica.
2. **SERV_EDUCACAO:** rede pública, pessoal legalmente contratado e prestações educacionais devidas; financiamento constitucional/material e novos alunos devem ser considerados.
3. **REP_CONSTIT:** receitas constitucionalmente partilhadas que pertencem ao ente federado, do tipo FPM. Sua natureza é diversa de concessão discricionária anual do Governo nacional; conferir bases de arrecadação e regras de distribuição/retensão previstas no direito aplicável. **Não inventar percentual do FPM** nem afirmar que todos os repasses federativos seguem a mesma lógica.
4. **REP_CONVENIO:** repasse de obrigação contratual/convênio efetivamente vigente, condições cumpridas e fonte válida; programa ou convênio extinto não se reanima por rotina fiscal.
5. **DIVIDA_SERVICO:** serviço de dívida já validamente contraída, devido; pagamento de obrigação existente não autoriza automaticamente empréstimo novo.
6. **DIVIDA_NOVA:** nova operação de crédito não pode ser presumida autorizada só porque falta orçamento; limites, espécie, competente e autorização fiscal exigem norma própria M05.
7. **PROG_EXTINTO:** programa vencido em Y0, sem obrigações remanescentes pressupostas; não reviver rubrica antiga, deixando as obrigações anteriores exigíveis para categoria própria se comprovadas.
8. **PROG_NOVO:** programa voluntário ainda sem lei ou dotação: governo não pode substituir deliberação parlamentar por interpretação extensiva de exceção fiscal.

### Quatro perguntas que cada linha do CSV obriga a responder
1. **Existe obrigação material exigível?** Ex.: atendimento, decisão judicial, folha e dívida regular, cujo cumprimento não se torna facultativo porque outra lei orçamentária não passou.
2. **Existe autorização orçamentária/transitória específica para executar?** Obrigações e dotações não são sinônimos; a Constituição projetada precisa disciplinar autorização provisória suficiente para deveres existentes.
3. **Existe fonte financeira e caixa?** Se caixa for insuficiente, a norma deve definir prioridades, cumprimento judicial, dívida e responsabilização; **não** se fabrica disponibilidade por vontade política.
4. **O custo pode recair sobre outro ente?** O poder federal não pode transferir encargo de saúde/educação a município sem respeitar competência, custeio e garantia de direitos. A CF atual **já contém art.167 §7º**, introduzido pela EC128/2022, sobre encargos legislativos de serviço público, com exceções textuais; ver a evolução da regra no futuro texto.

**Exemplo crítico de direito versus caixa:** hospital com obrigação legal válida em Y2: FISC-A pode autorizar provisoriamente despesa necessária, mas o hospital ainda carece de recursos disponíveis e regras de contratação/execução. FISC-B pode manter rubrica válida de Y0, porém valores fixos podem ser insuficientes para inflação, demanda ou direito legal superveniente. FISC-C na fase H2 assume os problemas de FISC-A. **Nenhuma solução de mera competência fiscal garante universalidade real de atendimento por si só.**

## 3. Controle de receita partilhada e repasses federativos
No direito positivo brasileiro, **CF arts.158/159** determinam participações e entregas de parcelas de receita a entes, e art.160 restringe retenções com exceções; tais relações não se reduzem a uma subvenção livre sujeita à simpatia do premiê ou presidente. Mesmo em orçamento federal não aprovado, a futura Constituição deve especificar que o executivo não pode **usar a crise fiscal como pretexto autônomo para bloquear titularidade de receita de estado/município**, preservadas as condições constitucionais próprias e a necessidade de arrecadação efetiva.

**Transferência de convênio/ajuste:** a existência de previsão fiscal antiga NÃO basta sem vínculo/condições legalmente eficazes; distinguir obrigação contratual ainda exigível de promessa política, autorização de crédito e liquidação contábil. Projetos plurianuais legitimamente comprometidos não podem ser simplesmente cancelados por continuação limitada, mas podem necessitar aprovação financeira válida.

**Encargos novos:** federalizar serviço ou exigir sua prestação municipal durante a prorrogação não dispensa fonte de custeio ou transferência; o M05 precisará dizer **se** restrição da EC128/2022 é preservada, ampliada, regulamentada e como será fiscalizada. Não reproduzir normas brasileiras sem avaliar se o futuro projeto as recepciona.

## 4. Dois exercícios seguidos e direitos fundamentais: contradições de cada FISC
| Teste | FISC-A | FISC-B | FISC-C |
|---|---|---|---|
| Obrigações materiais em Y1 | Continuação funcional condicionada à norma e caixa | Dotação prévia válida, mais dever de cumprir direitos | H1 como B; H2 como A |
| Obrigações em Y2 | Mesma regra legal, sem orçamento novo | Mesma base aprovada Y0, sem transformar Y1 em nova LOA | Prossegue H2; **não resetar H1** |
| Saúde/educação crescem | Lei pode cobrir dever novo sem automaticamente criar caixa/limite | Rubrica de Y0 pode subfinanciar e exigir ajuste por lei | Choque de transição H1→H2 e da insuficiência material |
| Receita repartida | Direito de ente separado de gasto discricionário | Idem, não depende do rótulo “prorrogação” | Idem |
| Convênios | Necessário provar obrigação existente | Necessário provar rubrica E obrigação vigentes | Cuidado com efeito da troca de fases |
| Programa extinto | Não reviver apenas por despesa provisória | Não prorrogar programa concluído conforme exclusão | Nenhuma fase autoriza ressuscitar |
| Novo empréstimo | Exige autorização legal específica, sem teto “25%” transplantado | Não surge por mero orçamento prorrogado | Não surge nem na troca H1→H2 |
| Política nova | Precisa lei e autorização | Não ganha poder da LOA antiga | Não é atalho emergencial generalizado |

**Escolha provisória de engenharia:** **FISC-A** possui maior clareza das categorias de obrigação, mas pode punir crescimento de demandas sem autorização/caixa; **FISC-B** preserva previsibilidade do planejamento aprovado mas pode congelar prioridades; **FISC-C** oferece transição, porém não tem vantagem demonstrada após Y2 e cria condição adicional para litígio/planejamento. **Nenhum vencedor estabelecido**. Antes de deliberação, M05 precisa mapear especificamente fontes e créditos (inclusive exigibilidade judicial e limites de endividamento), M04 consentimento territorial e M07 capacidade de execução.

## 5. ELE-1 × ELE-2 em ambas as legislaturas — 16 linhas
O arquivo `M03-02_08_MATRIZ_16_TESTES_ELEITORAIS.csv` utiliza 2 legislaturas × 2 alternativas eleitorais × 4 eventos distintos:
- **C1** dois orçamentos rejeitados: **NÃO** abre pleito em ELE-1 nem em ELE-2; a norma eleitoral cuida de eleição válida, não cria fundamento de dissolução;
- **C2** reforma estrutural 16 meses antes de **outro ramo** de falha de investidura: se **nova investidura fracassar** e Constituição futura autorizar dissolução, ELE-1 não cobre integralmente manipulação prévia; ELE-2 pode barrar norma da legislatura interessada, porém precisa exceção protetora de direitos. **C2 é hipotético ramo NOVO após renúncia ou formação frustrada**, NÃO consequência necessária de orçamento rejeitado nem continuação implícita de L2/P2 original;
- **C3** alteração fundamental após convocação decorrente de crise formal AUTÔNOMA: ELE-1 e ELE-2 bloqueariam aplicação ao pleito, salvo hipótese judicial estreita que restaure direito em condições operacionais possíveis;
- **C4** chefe de Estado tenta invocar veto fiscal para eleição: **NÃO** basta em ambas as regras; controle urgente da competência de dissolução, sem autorizar que tribunais decidam o mérito do orçamento.

**Condições de validade:** CF art.16 garante anterioridade de aplicação eleitoral no direito brasileiro vigente. ELE-1/ELE-2 não são normas brasileiras hoje; Comissão de Veneza CDL-AD(2024)027 é orientação persuasiva e não dispensa exame brasileiro. Quem proclama o resultado, quem certifica conflito entre versões de lei, exceção judicial e prazo de pleito seguem questões M02/M06/M14. O poder federal não pode usar emergência fiscal para reinventar a autoridade eleitoral.

## 6. Contraensaio de arquiteturas A e C
**A presidencial reformado:** igual legislatura fragmentada e igual orçamento rejeitado podem coexistir com presidente de mandato fixo. Uma oposição de 47 ou 54 deputados não pode dissolver Legislativo nem destituir o chefe de Estado por mera falta de lei; FISC-A/B/C e proteção de direitos continuam necessárias. **Mérito real:** evita eleição legislativa antecipada motivada por crise de gabinete. **Limite real:** não oferece substituição do presidente pelo surgimento de maioria programática parlamentar e mantém negociação fiscal conflituosa.

**B parlamentar racionalizado:** aceita gabinete minoritário enquanto não houver censura sucessora, sem confundir derrota fiscal com derrubada. Dissolução só se gatilho AUTÔNOMO de formação/confiança for satisfeito — ainda sem F6. **Mérito:** pode substituir governo por maioria sucessora quando surgir. **Limite:** persistência de gabinete com baixa capacidade legislativa, execução fiscal provisória por Y1/Y2 e necessidade de transparência/controle reforçados.

**C premier-presidencial:** responsabilidade do gabinete somente perante Parlamento; presidente popularmente eleito não tem competência presumida de demitir gabinete ou ordenar despesa, e não pode criar mecanismo paralelo de dissolução por orçamento. **Problema adicional:** conflito presidente/gabinete quanto a tutela de serviços, crédito ou emergência sem competência fiscal precisamente definida. Nenhum benefício incremental de C foi demonstrado neste ensaio.

## 7. Evidência jurídica e bibliografia de controle
1. **Constituição Federal/1988, texto atualizado:** arts.158–160 (receita pertencente a entes e entrega), arts.165–169 (orçamento, despesas, limites, autorização), art.16 (anterioridade), art.167 §7º. Texto consolidado da Câmara: https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html .
2. **EC128/2022, texto promulgado:** https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc128.htm .
3. **Alemanha, Lei Fundamental art.111, especialmente §2:** autorização funcional e crédito excepcional condicionado a insuficiência de receitas/reservas, em até um quarto da soma do orçamento anterior; **não** um teto uniforme de gastos, fonte oficial https://www.gesetze-im-internet.de/gg/art_111.html .
4. **Espanha, Lei Geral Orçamentária 47/2003 art.38:** prorrogação da LOA anterior até nova lei, excluídos programas/obrigações encerrados; adaptação orgânica de dotação; texto vigente no BOE https://www.boe.es/buscar/act.php?id=BOE-A-2003-21614 .
5. **Constituição espanhola art.134(4):** mesma prorrogação automática enquanto orçamento novo não aprovado, https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229 .
6. **Comissão de Veneza, CDL-AD(2024)027:** estabilidade de elementos eleitorais fundamentais; recomendações e exceções, https://www.coe.int/en/web/venice-commission/-/cdl-ad-2024-027-e . Direito comparado persuasivo, não interpretação vinculante de CF art.16.
7. **Dossiês M03.02 R03 e R07** versionados no mesmo PR85; classificações e hipóteses procedimentais NÃO são jurisprudência ou fatos brasileiros.

## 8. QA reproduzível, bloqueios e melhor objeção
**QA:** verificador estrutural específico `scripts/validar_m03_02_08_matrizes.py` a publicar junto com CSV; auditar 112 combinações únicas do produto cartesiano (2 legislaturas × 7 regime/fases × 8 categorias), 16 combinações eleitorais únicas (2 × 2 × 4), sequência temporal e citações de `L2/P2-derivação PRÉ-CONFIANÇA`. Um script de schema NÃO prova materialidade jurídica.

**Bloqueios para F6:** faltam pareceres especializados e dados reais M02/M04/M05/M06/M07/M12/M14; encargos, números e limites de dívida não quantificados; salvaguardas do orçamento multianual e do credor contra cortes sem fonte ainda não finalizadas; nenhuma competência da segunda Câmara aprovada.

**Melhor objeção contra nosso ensaio:** estabelecer autorização fiscal provisória para muitos exercícios pode tornar o Executivo funcionalmente independente da votação da Câmara, que continua incapaz de eleger sucessor; exigir reabertura eleitoral por derrota fiscal, porém, cria incentivo antidemocrático à fabricação de crises. **A tensão é real e não foi resolvida pelo teste**. É preciso escolher conscientemente que grau de impasse legislativo a democracia deverá admitir e quais deveres de publicidade, controle e processo fiscal podem limitar o dano.

## 9. Encaminhamento M03.02.09
Antes de nova redação, preparar matriz de **limites temporais e responsabilidade fiscal** para orçamento provisório repetido (quem revisa obrigações, quais saídas não envolvem eleição, como evitar renúncia do Legislativo à competência orçamentária), colher parecer M05/M04 e cruzar com tutela M06. Tratar F6-00 (A/B/C) e F6 fiscal como decisões diferentes. Não substituir prova orçamentária por número inventado ou por defesa abstrata de regime de governo.