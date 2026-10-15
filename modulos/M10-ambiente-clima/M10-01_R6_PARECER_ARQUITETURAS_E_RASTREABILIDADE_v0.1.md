# M10.01-R6 — Pré-auditoria de não regressão funcional: arquiteturas constitucionais hipotéticas

**ID:** CF-M10.01-S006 · **Data de corte:** 14/10/2026 · **Fases:** F1/F3/F4/F5 (hipóteses de organização, sem decisão F6 nem redação F7).  
**Issue:** #88 · **PR:** #89, draft · **Base CF main da rodada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **HEAD PR de entrada:** `5b323ac3ec9c68da76a46a557209360de1f89272`.  
**Arquivos desta rodada:** `M10-01_R6_MATRIZ_NAO_REGRESSAO_HIPOTETICA.csv` (35 vínculos funcionais × 2 arquiteturas), `M10-01_R6_TESTES_DUAS_ARQUITETURAS.csv` (12 hipóteses), este parecer e pacote de continuidade. **Nenhuma CF-NOR, decisão D, minuta no índice, modificação do CLF ou merge em main.**

## 1. Objeto e ressalva de prova

A Constituição brasileira vigente impõe garantias ambientais em diversas partes, especialmente nos arts. 5º, 23, 24, 30, 129, 145, 170, 186, 216, 225 e 231. O art. 225 contém direitos, deveres, reservas de lei, procedimentos, bens ambientais específicos, regras tributárias e competências excepcionais. **A posição de uma função no texto não determina automaticamente seus efeitos jurídicos**, pois extensão, titularidade, execução, remédios e regimes legais também importam.

Esta rodada **não pode demonstrar não regressão substantiva** sem texto candidato. Desenvolve uma **matriz de requisitos de rastreabilidade**: para cada função vigente, identifica onde uma arquitetura a situaria, a remissão necessária, instrumentos legais e objeções que uma redação futura teria de enfrentar.

Fontes principais:
- [Constituição compilada brasileira — Câmara dos Deputados](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html), consultada 14/10/2026; [Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm).
- [LC 140/2011](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp140.htm), [Lei 15.190/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm), [Lei 15.300/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm), [Decreto 10.088/2019 — OIT169 Anexo LXXII](https://www2.camara.leg.br/legin/fed/decret/2019/decreto-10088-5-novembro-2019-789348-normaatualizada-pe.html).
- [STF ADI 4757](https://portal.stf.jus.br/processos/detalhe.asp?incidente=4224704), [STF ADI 6808](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=486116&ori=1), [STF ADPF 651](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=486085&ori=1), [STF ADPF 708](https://portal.stf.jus.br/processos/detalhe.asp?incidente=5951856), STF Temas 999 e 1194 já catalogados na R3.
- [Alemanha, Lei Fundamental art. 20a](https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html); [Tribunal Constitucional Federal alemão, 24/03/2021, 1 BvR 2656/18 e conexos](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/2021/03/rs20210324_1bvr265618en.html); [França, Carta Constitucional do Meio Ambiente (2005)](https://www.legifrance.gouv.fr/contenu/menu/droit-national-en-vigueur/constitution/charte-de-l-environnement).

**Leitura das fontes comparadas sem transplantar teses:** Alemanha, art. 20a, refere-se a fundamentos naturais e gerações futuras, interpretados em relação a liberdades intertemporais no julgamento de 2021. A Carta francesa contém direitos e deveres ambientais, precaução (art.5) e acesso à informação/participação (art.7). São instrumentos jurídicos estrangeiros com regimes próprios e não validam uma arquitetura brasileira em particular.

## 2. Baseline C0: função vigente, sem inferência de reforma

C0 denota apenas **manutenção do arranjo normativo atualmente encontrado** como parâmetro documental de controle, não alternativa escolhida e não juízo sobre suficiência. Inclui:
- direitos/deveres ambientais materiais e intergeracionais, EIA prévio para potencial significativa degradação, restauração, áreas protegidas, biodiversidade, educação e controle de riscos;
- distribuição federativa atual (CF 23–24–30 e LC140), com fiscalização comum e licenciamento por um ente definido legalmente;
- direitos de acesso à informação, ação popular, tutela coletiva segundo legitimados legais, direitos indígenas e consulta conforme regime aplicável;
- regras especiais muitas vezes omitidas em sínteses: §1º VIII do art.225 (incentivos fiscais com aplicação temporal), §§4–7 (biomas nacionais, terras estaduais, localização nuclear, prática cultural com animais);
- regimes legais LAC/LOC/LAE, planos de adaptação e mecanismos de carbono **como instrumentos infraconstitucionais**, não garantias constitucionais literais; jurisprudência do STF/STJ com seus próprios objetos.

## 3. Arquitetura A — núcleo ambiental concentrado com interfaces explícitas

**Esquema de localização, não texto proposto:**

| Bloco de trabalho hipotético | Conteúdo a auditar | Interface obrigatória |
|---|---|---|
| A1 — titularidade e tempo | Direito difuso, deveres e gerações presentes/futuras; dimensão climática em abstrato | M01/M06 |
| A2 — proteção ecológica | Processos, biodiversidade/genética, áreas protegidas, fauna/flora, educação ambiental | M08/M09/M11 |
| A3 — prevenção e procedimento | Controle de riscos, EIA para significativa degradação e publicidade; participação/precaução em relação a atos | M01/M06/M07 |
| A4 — restauração e responsabilidade | Recuperação mineral, reparação distinta de sanções e remédios cabíveis | M06/M08/M12 |
| A5 — clima e governança | Deveres de implementação e adaptação; instrumentos legais e controle de omissões em seus pressupostos | M05/M06/M13 |
| A6 — regimes constitucionais específicos | Tributação do art.225 §1 VIII, patrimônios nacionais, terras estaduais, localização nuclear, exceção cultural; **todas sujeitas a decisão material** | M03/M04/M05/M08/M11/M14 |
| A7 — remissões federativas | Competência ambiental material/legislativa e autonomia municipal remetidas com precisão ao desenho M04 | M04/M07 |
| A8 — remissões a direitos e tutela | Informação, ação popular, tutela coletiva, direitos territoriais e garantias processuais | M01/M06/M11/M13 |
| A9 — reserva legal técnica | Regulação do órgão licenciador, modalidades, estudos adicionais, prazos, plano e procedimento, nos limites de garantias/competências | M04/M06/M07/M08/M12/CLF |

**Operação hipotética:** o leitor localiza no núcleo ambiental os direitos/deveres ecológicos expressos; para competências e tutela utiliza remissões a outros módulos. Um bloco identificado por nome **não é cláusula**, e `A6` é placeholder de questões materiais sem resultado. A mera existência de A7/A8 não demonstra que a função da CF atual continuaria com o mesmo titular, ônus ou remédio.

## 4. Arquitetura B — distribuição por função constitucional com ligação ambiental

| Bloco de trabalho hipotético | Conteúdo a auditar | Interface obrigatória |
|---|---|---|
| B1 — direitos fundamentais | Direito a equilíbrio ecológico, tempo intergeracional, informação e legitimidade quando constitucional | M01 |
| B2 — garantias de procedimento/participação | EIA nos casos de significativa degradação, publicidade, participação e precaução dentro das garantias que vierem a ser deliberadas | M01/M06/M07 |
| B3 — Federação e administração | Competência ambiental administrativa e legislativa, supletividade por lei complementar, proteção urbana; localização nuclear se deliberada | M04/M07/M03 |
| B4 — economia, propriedade, finanças | Defesa do ambiente na economia, função da propriedade e tratamento tributário geral e específico, com aplicação temporal | M05/M08/M14 |
| B5 — Justiça e responsabilidade | Tutela coletiva, sanções e reparação, medidas e execução; limites penais | M06/M12 |
| B6 — território e cultura | Direitos indígenas e consulta, espaços/biomas protegidos, patrimônio, proteção animal/cultural e terras públicas | M11/M13/M08 |
| B7 — deveres estatais e serviços ecológicos | Processos ecológicos, biodiversidade, risco, educação, clima e adaptação | M07/M08/M09 |
| B9 — legislação de execução | Licenciamento único, LAC/LOC/LAE, prazos, condicionantes e regime de estudos/consulta das normas aplicáveis | M04/M07/M08/M11/M12/CLF |

**Operação hipotética:** um caso de licenciamento pode acionar simultaneamente garantias do capítulo de direitos, competência federativa, tutela processual e direitos territoriais. A ligação entre capítulos exigiria remissões e definições que ainda não existem. A arquitetura B **não dispensa** enunciar com precisão os comandos hoje expressos no art.225; apenas os distribui em blocos conceituais.

## 5. Matriz de rastreabilidade: significado dos marcadores

A planilha de trabalho `M10-01_R6_MATRIZ_NAO_REGRESSAO_HIPOTETICA.csv` contém **35 funções e vínculos**, incluindo as 29 entradas da R5 acrescidas das seis funções C0 que seriam frequentemente colapsadas numa síntese.

- **EXPL:** bloco conceitual designado para receber comando explícito **se futuramente deliberado**; não certifica texto nem equivalência.
- **REF:** função situada por remissão/interface; nenhum enunciado ou conteúdo no módulo de destino foi aprovado nesta rodada.
- **LEGAL:** questão disciplinada em lei vigente; nome da modalidade de licença não precisa ser tratado como dispositivo constitucional por esta análise.
- **MIX:** conteúdo constitucional e legal/jurisprudencial coexistem, devendo ser separados antes de qualquer alegação de preservação.
- **DEC:** função constitucional **atual** cuja continuidade, modificação ou transição é uma **decisão material aberta** (especialmente tributação de combustíveis, biomas, terras estaduais, nuclear e prática cultural animal). Não indica descarte, manutenção ou superioridade de tratamento.

Uma mudança de `EXPL` para `REF` ou `DEC` na matriz é marcador da **necessidade de texto e deliberação**, não constatação de inconstitucionalidade de arquitetura inexistente. Uma futura matriz real deverá conter o ID CF-NOR, texto exato, disciplina legal residual e teste de tutela.

### Exemplos de rastreio N:N

| Função atual | Arquitetura A | Arquitetura B | Verificação requerida |
|---|---|---|---|
| EIA com publicidade para significativa degradação | A3 | B2 | Sujeito, risco gatilho, anterioridade, publicidade e controle |
| Proteção ambiental comum e licença por um ente | A7 + A9/LC140 | B3 + B9/LC140 | Separar competência administrativa, fiscalização, órgão licenciante e mora |
| Reparação independentemente de sanção | A4 + A8 | B5 | Dever material, sujeitos, remédios e regime penal/civil distinto |
| Consulta indígena e audiência pública | A8 + A3 | B6 + B2 | Titulares do direito, Convenção169, momento e objeto |
| Regra fiscal específica CF225 §1 VIII | A6 (DEC) | B4 (DEC) | Vigência EC132, regulação LC e deliberação material separada |
| Restauração/proteção áreas | A2 | B6/B7 | Reserva legal e integridade de atributos |
| Proteção da futura geração | A1 + A5 | B1 + B7 | Conteúdo temporal e tutela sem impor meta quantitativa inexistente |

## 6. Testes de borda

`M10-01_R6_TESTES_DUAS_ARQUITETURAS.csv` apresenta **12 casos inventados**; cada linha relaciona fonte atual, percurso A, percurso B, norma administrativa residual, remédio processual abstrato, melhor objeção e ponto de prova:
1. dispensa indevida de EIA com potencial significativo;
2. empreendimento interestadual com fiscalização múltipla;
3. audiência geral sem consulta a povo indígena afetado;
4. multa de mineração sem recuperação de dano;
5. abandono de plano climático e controle de omissão;
6. alteração administrativa de espaço especialmente protegido;
7. diminuição de participação ambiental em colegiado;
8. transformação de regra fiscal especial em princípio genérico;
9. usina nuclear sem localização fixada por lei federal;
10. LOC e alegação de anistia penal/civil universal;
11. modificação de prazos e canais de publicidade/participação;
12. aparente colisão proteção animal e manifestação cultural.

**Leitura dos resultados:** ambos os esquemas exigem remissões e decisões para esses casos; a linha `percurso_a/percurso_b` é um **roteiro documental de verificação**, não uma previsão sobre efetividade ou comportamento judicial. Não há pontuação nem avaliação de probabilidade de sucesso.

## 7. Dependências, status de STF e delimitação de fontes

**Intermodulares**:
- M01/M06: direito à informação, tutela judicial, participação, efeito vinculante do STF e garantias processuais;
- M04/M07: competência legislativa/administração, licenciamento único, cooperação supletiva, poder de fiscalização e motivação;
- M05/M14: §1 VIII do art.225 e o faseamento da EC132, orçamento, recursos e regras transitórias;
- M08/M11: ecossistemas, propriedade, povos, patrimônio e exceção cultural; consulta em especial;
- M12/CLF: art.26§5 da Lei15190 e crime art.60 Lei9605, sem interferência em minuta criminal;
- M13: posição e alcance da Convenção169 e direito internacional ambiental.

**STF — legislação de 2025:** [ADI 7913](https://portal.stf.jus.br/processos/detalhe.asp?incidente=7468448) e [ADI 7916](https://portal.stf.jus.br/processos/detalhe.asp?incidente=7473191) têm andamentos indexados em 14/09/2026 de petições/reconsideração/conclusão. [ADI 7919](https://portal.stf.jus.br/processos/detalhe.asp?incidente=7474918) apresenta indexação de petições em 02–04/09; [ADC 102](https://portal.stf.jus.br/processos/detalhe.asp?incidente=7554475) estava relacionada à pauta de agosto. **A consulta direta aos autos nesta rodada produziu bloqueios HTTP 403 e os índices não certificam o último evento em 14/10/2026**. Não alegar acórdão definitivo, cautelar vigente ou inexistência desses atos sem certidão/decisão verificável. Não afirmar que todos estão simplesmente parados desde agosto.

**Comparado:** decisão climática alemã de 2021 usa art.20a e liberdades intertemporais; a Carta francesa de 2005 enuncia responsabilidade e precaução com medidas proporcionadas. Nenhuma é uma reprodução da CF brasileira, e a inserção de formulações equivalentes em qualquer arquitetura seria **decisão material nova**, fora da R6.

## 8. Limitações e passagem de fase

1. **Sem texto candidato**, não há como declarar preservação, regressão, ampliação ou equivalência da garantia; existe apenas mapa do que verificar.
2. **Sem dados de desempenho**, a organização textual não fundamenta previsão de custo, benefício, eficácia ambiental, agilidade ou resultado político.
3. **Sem julgamento primário atualizado**, a litigância de licenciamento não fornece tese de mérito conclusiva.
4. **Sem parecer intermodular**, nenhuma remissão A7/A8/B3/B5/B6 pode ser considerada efetivamente integrada à CF.
5. **Sem decisão F6**, as categorias DEC permanecem abertas; estudos de técnica A e B não introduzem escolhas constituintes.

**FEITO:** C0 como referência; duas arquiteturas hipotéticas A/B; 35 entradas de rastreabilidade; 12 cenários; fontes oficiais brasileiras e dois referenciais comparados; identificação das decisões materiais pendentes.

**PENDENTE:** posição dos revisores M01/M04/M05/M06/M07/M08/M11/M12/M13/M14; status primário dos quatro processos; cronologia EC132; escolha expressa, se houver, de matéria ou arquitetura; redação concreta; auditoria jurídica de equivalência.

**PRÓXIMO — M10.01-R7:** preparar **protocolo intermodular de perguntas discriminadas**, sem criar normas novas, delimitando quais funções materiais devem ser decididas por M10 e quais já pertencem aos capítulos M01/M04/M05/M06/M08/M11/M13. Se houver material suficiente, organizar cenários editoriais com dependências resolvidas e depois submeter escolhas materiais por decisão explícita F6; somente após isso qualquer redação ganha ID CF-NOR.

**Controle de integridade:** PR89 permanece draft; C0, A e B são esquemas analíticos, não capítulos de anteprojeto, não votados e não promulgados; CF main e CLF intactos.
