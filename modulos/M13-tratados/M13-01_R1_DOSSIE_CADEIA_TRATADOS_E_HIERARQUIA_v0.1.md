# M13.01-R1 — Dossiê de incorporação, hierarquia, eficácia e controle de tratados

**Identificação:** CF-M13.01-S001 · **Corte:** 14/10/2026 · **Issue própria:** [#93](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/93) · **Branch:** `pesquisa/m13-01-tratados-hierarquia-20261014`.  
**Main de entrada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Nível:** F0 escopo já reservado; F1–F5 pesquisa jurídica inicial, **sem F6/D, CF-NOR F7, alteração de `redacao/`, `main` ou CLF**.

## 1. Problema técnico e critérios de separação

A redação de um texto constitucional hipotético não autoriza tratar **assinatura**, **aprovação legislativa**, **ratificação internacional**, **vigência externa**, **promulgação/publicação interna**, **posição hierárquica** e **aplicabilidade judicial da obrigação específica** como um único ato.

| Momento | Quem atua | Pergunta verificável | Erro a evitar |
|---|---|---|---|
| Negociação/assinatura | Executivo/representantes habilitados | Brasil assinou? quais condições e reservas? | assinatura = tratado aprovado ou vigente |
| Aprovação parlamentar | Congresso, CF49 I | Qual decreto legislativo e **qual rito**? | todo decreto legislativo = rito art5 §3 |
| Ratificação ou adesão | Executivo no plano externo (CF84 VIII) | Quando e com qual depositário? | data de aprovação = data de ratificação |
| Vigência internacional para o Brasil | Cláusula de entrada em vigor do tratado | Qual data para **o Brasil**, diferente da vigência global? | aplicar data mundial automaticamente |
| Promulgação/publicidade doméstica | Decreto presidencial de promulgação, contexto da jurisprudência brasileira | Qual decreto publica o texto e qual foi substituído por consolidação? | revogar **decreto promulgador** = denunciar o tratado |
| Hierarquia no direito interno | CF5 §§2–3 + jurisprudência STF | Direitos humanos? aprovação pelo rito qualificado? decisão que caracterizou o instrumento? | CDPD, OIT169 e Paris têm **exatamente** o mesmo grau por assinatura |
| Incidência e controle | Autoridades/Judiciário sob competências legais | O comando é suficientemente concreto? existe requisito de regulamentação/fato e remédio? | supralegalidade = veto universal ou autorização administrativa automática |

**Fontes constitucionais:** [CF arts. 4º, 5º §§2º–3º, 49 I, 84 VIII, 102 III b, 105 III a e 109 III](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm). A estrutura de controle de constitucionalidade não se confunde com a análise concreta de compatibilidade da **lei infraconstitucional com tratado supralegal**; cabimento/processo de cada ação devem ser examinados, não presumidos.

## 2. Quatro instrumentos com trajetórias diferentes

### 2.1 Convenção 169 da OIT — direitos indígenas e tribais

**Linha documental positiva:** Convenção adotada 27/06/1989; **Decreto Legislativo 143 de 20/06/2002** a aprova pelo **rito ordinário**, **ratificação depositada 25/07/2002**, **vigência internacional para o Brasil 25/07/2003**, **Decreto 5.051 de 19/04/2004** a promulga; **Decreto 10.088/2019, Anexo LXXII**, consolida o decreto promulgador e mantém o tratado no repertório nacional.

- [Decreto 5.051/2004, preâmbulo com todas as datas](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/decreto/d5051.htm).
- [Decreto 10.088/2019, Anexo LXXII, publicação atualizada Câmara](https://www2.camara.leg.br/legin/fed/decret/2019/decreto-10088-5-novembro-2019-789348-normaatualizada-pe.html).
- [Senado, DL143/2002](https://legis.senado.leg.br/norma/588321).

**Classificação hierárquica fundamentada:** a Convenção 169 versa direitos humanos de povos indígenas/tribais e **não foi aprovada pelo rito de equivalência de emenda do art5 §3** (adicionado somente em 2004). A **orientação geral do STF** no RE466.343/HC87.585 e na [Súmula Vinculante25/jurisprudência do STF](https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26&sumula=1268) atribui **status supralegal, inferior à CF e superior às leis ordinárias**, aos tratados de direitos humanos incorporados sem o rito art5 §3. **Conclusão técnica de enquadramento:** `SUPRALEGAL_PELA_ORIENTACAO_GERAL_STF`; **não dizer que um julgamento específico do STF declarou automaticamente cada artigo da C169 supralegal em toda espécie de ação**, nem que a sua ratificação ocorreu pelo rito qualificado.

**Conteúdo e incidência:** [C169 arts. 1º, 6º, 7º, 15, 16 e 34](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10088.htm): campo de povos indígenas/tribais; medidas legislativas/administrativas **suscetíveis de afetá-los diretamente**; consulta por instituições representativas e boa-fé, objetivo de acordo/consentimento; participação em planos/programas; recursos naturais e hipóteses específicas de transferência/deslocamento. Não converter todas as cláusulas em **veto irrestrito** nem reduzir consulta a audiência pública.

**Interface nacional:** [CF231 §3 e 232](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm) preserva **oitiva e autorização parlamentar** para aproveitamento hídrico/mineral **em terra indígena**, participação na lavra e legitimidade judicial própria. A [Lei 15.300/2025 art4 §2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm) estabelece que a audiência no regime **LAE não substitui a consulta devida**. A [Lei 15.190/2025 arts42–45](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm) disciplina manifestação de órgãos intervenientes com critérios próprios — **não é definição exaustiva da titularidade convencional**.

**Limites:** hierarquia não decide por si **afetação direta**, representatividade, oportunidades de influência, relação de consulta com órgãos estaduais/municipais, ou remédio judicial de toda controvérsia. Essas matérias têm estudos especializados em [M11 PR94](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/94), [M10 PR89](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/89), [M06 PR62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62).

### 2.2 Convenção sobre os Direitos das Pessoas com Deficiência (CDPD) e Protocolo

**DL186 de 09/07/2008** diz expressamente que aprova ambos **nos termos do art5 §3 da CF**; **depósito em 01/08/2008**; **Decreto 6.949 de 25/08/2009** os promulga. A equivalência de emenda é sustentada pelo **procedimento documental efetivamente cumprido**, não pelo simples assunto 'direitos humanos'.

- [DL186/2008, art1](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/congresso/dlg186-2008.htm).
- [Decreto6949/2009](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/decreto/d6949.htm).

**Distinção de conteúdo:** a CDPD art4(3) dispõe sobre consulta/participação de **pessoas com deficiência por organizações representativas** nas matérias que as afetam. **Esse rito não é o mesmo** da Convenção169 art6, embora compartilhem preocupações de representação e participação; não transportar requisitos de um tratado ao campo de titularidade do outro.

### 2.3 Acordo de Paris — tratado ambiental e proteção de direitos humanos no STF

**DL140 de 16/08/2016**, ratificação depositada **21/09/2016**, vigência externa para Brasil **04/11/2016**, promulgação pelo **Decreto 9.073/2017**, publicados os termos oficiais:
[Senado, DL140/2016](https://legis.senado.gov.br/norma/588274/publicacao/15642126); [Decreto9073/2017](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/decreto/d9073.htm).

Na **ADPF708, julgamento de 04/07/2022**, o STF vinculou o dever estatal climático à proteção de direitos fundamentais e tratados ambientais, reconhecendo estatuto **supralegal** a obrigações ambientais que compreendeu como instrumentos de direitos humanos, no contexto do **Acordo de Paris** e do Fundo Clima. [STF Informativo 1061 (2022)](https://www.stf.jus.br/arquivo/informativo/documento/informativo1061.htm); [STF jurisprudência da CF225, ADPF708](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=225&abrirBase=CF).
**Limite de certeza:** o portal do Informativo devolveu HTTP403 para abertura integral nesta busca, mas resumo indexado e página oficial de jurisprudência identificam o julgamento. A análise **não transforma cada instrumento ambiental, técnico, comercial ou climático indistintamente em emenda constitucional** nem transfere todas as obrigações do Acordo para um direito individual autoexecutável de determinado pedido.

### 2.4 Convenção Americana de Direitos Humanos (CADH) — paradigma jurisprudencial

**Cadeia formal específica:** [Decreto Legislativo 27 de 26/05/1992](https://www2.camara.leg.br/legin/fed/decleg/1992/decretolegislativo-27-26-maio-1992-358314-publicacaooriginal-1-pl.html), [carta de adesão depositada em 25/09/1992 e vigência para o Brasil nessa data, Decreto 678/1992](https://legis.senado.leg.br/norma/388856/publicacao/15635063). Aprovação **ordinária**, sem rito CF5 §3 (posterior, de 2004). A adesão inclui declaração interpretativa brasileira indicada no art. 2º do decreto; não estender a declaração a obrigações distintas não abrangidas por seu texto.

[STF RE466.343/HC87.585, julgamento plenário dezembro/2008](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=100258&ori=1) e [Súmula Vinculante25](https://portal.stf.jus.br/jurisprudencia/sumariosumulas.asp?base=26&sumula=1268): a vedação de prisão civil do depositário infiel é exemplo de que tratado de direitos humanos incorporado pelo **rito ordinário** pode bloquear aplicação de normas **infraconstitucionais** incompatíveis sem revogar a CF. Esse resultado **não é equivalência constitucional do tratado**; a posição é **supralegal**. É precedente geral útil para analisar C169, mas precisa de cotejo por matéria.

## 3. Regimes hierárquicos — classificação e teste de prova

| Categoria | Prova de ingresso | Parâmetro de hierarquia | Contraste concreto |
|---|---|---|---|
| Tratado de DH aprovado pelo **art5 §3** | decretos legislativos com quórum/turnos de EC; ratificação e promulgação | **equivalência às emendas constitucionais** | **CDPD** — DL186/2008 |
| Tratado de DH **sem** art5 §3 | aprovação ordinária, ratificação, promulgação | **supralegal** sob orientação STF consolidada | **C169**, classificada pela matéria e rito; **CADH** no precedente |
| Tratado **ambiental** com direitos humanos reconhecidos no julgamento | rito, objeto e **precedente aplicável** | posição **supralegal** reconhecida no julgamento pertinente | **Acordo de Paris / ADPF708**; não generalizar a todos |
| Tratado comum (sem qualificação de DH no precedente) | atos de incorporação por instrumento | **paridade ordinária em regra tradicional do STF**, sujeita a exceções e regime especial | exigir instrumento concreto; não afirmar enquadramento de toda convenção técnica sem exame |

**Não igualar supralegalidade a supremacia sobre a Constituição.** Tampouco supor que a aprovação por decreto legislativo em si converte tratados em simples 'decretos administrativos': decreto legislativo, tratado e decreto de promulgação têm **funções distintas**, e a hierarquia decorre da CF e do tipo de obrigação/rito.

## 4. Conflito entre lei doméstica e tratado: raciocínio funcional

Exemplo **hipotético**: norma nacional determina que audiência pública geral **sempre substitui** consulta de povo sujeito à Convenção169. O exame exige: (1) se o instrumento e a comunidade são abrangidos; (2) se há **medida legislativa/administrativa suscetível de afetação direta**; (3) se a consulta devida, tal como regulada pelas fontes aplicáveis, foi prestada por representante e meio adequados; (4) se a lei conflita de fato com comando supralegal; (5) procedimento e tutela judicial compatíveis. A [Lei15.300 art4 §2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm) já contém a distinção de não substituição para LAE.

**Consequência metodológica:** um juiz não precisa declarar que a Convenção169 tem formalmente status de EC para avaliar uma incompatibilidade legal com norma supralegal; mas **isso não determina automaticamente que qualquer omissão de consulta anule todo ato, sem ponderar o tipo de tutela e seus pressupostos**. A forma processual e efeitos ficam sob M06.

## 5. Controle de convencionalidade e limites de efeito

- **Controle interpretativo:** ler legislação e práticas administrativas em relação às obrigações convencionais aplicáveis, quando possível, sem ignorar texto/competência.
- **Conflito normativo:** qual comando nacional contradiz o tratado, qual é a posição normativa deste e quais efeitos jurídicos são postulados? A invalidação/contenção de eficácia de lei em caso concreto difere de decisão de inconstitucionalidade concentrada.
- **Prova e tutela:** a **legitimação própria do art232 CF** e os instrumentos do M06 (ACP, MI, controle abstrato, medidas urgentes) têm ritos e legitimados diferentes; supralegalidade **não cria sozinha nova espécie de ação judicial**.
- **Fonte internacional:** obrigações de tratados, decisões/relatórios internacionais e recomendações de órgãos de supervisão **não são automaticamente intercambiáveis**, devendo ser individualizados com natureza e força respectivas.
- **Federalismo/competência:** obrigação internacional assumida pelo Brasil não determina por si qual órgão interno **licencia** ou quem pode impor responsabilidade administrativa; remeter a M04/M07/M10 e ao instrumento normativo específico.

## 6. Pontos abertos para a arquitetura hipotética da CF e relação com M00

A [`CF-NOR-0007` H](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/2a770a8136f8ca4877e865be3e3b7745a6d4b168/redacao/propostas/CF-NOR-0007.md) protege genericamente acesso ao Judiciário, **sem enunciar hierarquia, incorporação, controle de convencionalidade, remédios especiais CF232 ou execução**. O [M00](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/tree/main/modulos/M00-fundamentos) pesquisa arquitetura de normas/hierarquia e reserva de lei. A M13-R1 **não pode declarar equivalência final** sem texto constitucional candidato e decisão F6.

Em particular, o eventual reposicionamento de função do **art5 §§2–3** ou do **art49 I/84 VIII** é **questão aberta**, não opção selecionada por esta pesquisa. Uma futura auditoria deve verificar se mecanismos de aprovação, publicidade, posição de tratados de DH, tutela e regime de transição são preservados, alterados ou substituídos com prova literal, sem usar texto ambiental M10 como cláusula universal sobre fontes.

## 7. Produtos conectados

- `M13-01_R1_MATRIZ_CADEIAS_TRATADOS_E_HIERARQUIA.csv`: **4 instrumentos × 6 funções = 24 linhas** com aprovações/ratificações/promulgação/hierarquia/controle/prova.
- `M13-01_R1_TESTES_ADVERSARIAIS_TRATADOS.csv`: **12 hipóteses** (C169/CDPD/Paris/CADH, conflito legal, consulta, fontes e decisões).
- `M13-01_R1_PARECER_INTERFACE_F05_M10_M11_v0.1.md`: resposta material **M13 parcial** sobre hierarquia à F05 da M10 e questões M11, sem alterar pareceres desses módulos.
- `M13-01_R1_PACOTE_CONTINUIDADE_v0.1.md`: FEITO/PENDENTE/PRÓXIMO, QA e passagem para R2.

**FEITO:** distinção dos atos e fundamentação documental por instrumento; **PENDENTE:** outros acordos/denúncia/controvérsias e detalhes processuais, recepção numa eventual CF não aprovada; **PRÓXIMO:** investigação de conflitos materiais específicos entre C169, a Lei15190/2025 e a LAE Lei15300/2025 à luz da hierarquia, com cenário de consulta e remédio identificado, sem projeto normativo F7.
