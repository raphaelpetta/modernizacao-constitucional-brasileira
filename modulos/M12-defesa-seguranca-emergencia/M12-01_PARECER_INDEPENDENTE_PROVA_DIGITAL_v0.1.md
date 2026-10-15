# M12.01 — Parecer independente sobre investigação digital, garantias de prova e Tema 977/STF

**ID:** CF-M12-S001 · **Corte:** 14/10/2026 · **Responsável funcional:** M12 (Defesa, segurança e emergência: polícia, investigação e inteligência). **Estado:** F0–F5, F8 conceitual, V/P/A, **sem decisão material D, sem CF-NOR e sem endosso de uma nova redação**.  
**Preflight:** CF main `b9dbdc540310ed5dc34fb1e5f314c46af343dc98`; [issue #80](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/80), agora reservada M12.01; pareceres M06 no [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62) e proposta experimental M01.13 no [PR #59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59). A autonomia significa **análise jurídica separada em branch M12**, não parecer formal subscrito por uma pessoa ou órgão externo.

## 1. A conclusão M12 é mais ampla que a crítica M06

Uma Constituição moderna precisa bloquear **três falhas diferentes** na prova digital:

1. **Legalidade da intervenção (L):** autoridade pode apreender o equipamento? identificar informação mínima em achado fortuito? preservar? pesquisar os dados? interceptar fluxo? De qual pessoa, objeto, motivo e durante quanto tempo, com qual fundamento legal, consentimento ou decisão judicial? **Uma cadeia de custódia perfeita não convalida uma devassa ilegal.**
2. **Confiabilidade e integridade (I):** a prova é autêntica, completa para o fim pertinente e tecnicamente auditável? É possível rastrear transformação, aquisição, extração, cópia, integridade, custódia e instrumentos empregados? **Uma apreensão lícita não demonstra automaticamente que os bytes apresentados não foram alterados.**
3. **Contraditório efetivo (C):** defesa e demais legitimados podem conhecer os dados usados, obter informação técnica suficiente para testá-los e suscitar nulidade/exclusão de prova, preservados dados de vítimas e terceiros? **A presença de um hash sem acesso processual útil não substitui contraditório.**

Três portões independentes **L/I/C**: nenhum deve ser substituído por outro. Inadmissibilidade jurídica da prova, nulidade processual por vício de integridade, direito à perícia e consequência de prejuízo **não possuem gatilhos idênticos**. Evitar constitucionalizar fórmula genérica "qualquer falha formal gera nulidade absoluta", ou a contrária "só haverá violação quando demonstrada adulteração" em hipóteses de acesso originariamente inconstitucional.

## 2. Fontes brasileiras, alcance e hierarquia

### STF Tema 977 — ARE 1.042.075, mérito plenário 25/06/2025

A **tese efetivamente aprovada** distingue:

- **CAP** — mera apreensão física do celular nos termos do CPP art. 6º/flagrante: não sujeita à reserva de jurisdição **por si**, mas legalidade do motivo e forma da apreensão subsiste;
- **IDF** — celular **encontrado fortuitamente**: acesso a dados **com fim exclusivo** de esclarecer autoria do fato supostamente criminoso ou identidade do proprietário, sem consentimento/decisão prévia, mediante **justificação posterior**; esta é **exceção limitada** e não licença para pesquisar outras infrações;
- **ACE** — aparelho apreendido segundo CPP art. 6º ou em flagrante: acesso investigativo a dados mediante consentimento **livre e expresso do titular** ou decisão judicial prévia individualizada com elementos concretos, proporcionalidade e abrangência delimitada. **Apreciação judicial prioritária, inclusive plantão**;
- **PRE** — providências necessárias à **preservação de dados e metadados** do celular apreendido **antes de autorização judicial**, com posterior justificação. O item 2 fala em `razões de referido acesso` mesmo tratando de preservação: registrar ambiguidade literal em vez de concluir que toda extração/perícia é acesso irrestrito autorizado. Pode exigir cópia técnica dos bits ou operação forense: não proibir ou autorizar de modo absoluto sem exame técnico;
- **TEMP** — eficácia **prospectiva** da tese, ressalvados pedidos formulados por defesas até o encerramento do julgamento.

**Escopo exato:** **aparelho de telefone celular em inquérito penal**, não qualquer serviço em nuvem, comunicação futura, busca administrativa ou reconhecimento facial. O andamento consultado **não certifica trânsito definitivo após eventuais embargos**; verificar novamente antes de ratificar texto constitucional, sem declarar que o precedente inteiro está suspenso por existir recurso. A tese plenária merece autoridade superior às formulações anteriores de votos-vista de julgamento **não final**.

Fontes [STF Tema 977](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=ARE&incidente=5173898&numeroProcesso=1042075&numeroTema=977) e [andamento com certidão plenária literal 25/06/2025](https://portal.stf.jus.br/processos/listarProcessos.asp?classe=ARE&numeroProcesso=1042075).

### Atualização STJ 2026 — cadeia de custódia e contraditório

**STJ, Jurisprudência em Teses 281, notícia 03/06/2026:** enfatiza cadeia de custódia, auditabilidade, **possibilidade de exame técnico independente** e uso possível de hash; e destaca que **dados estáticos de conexão** não são interceptação telefônica (regime Marco Civil da Internet, não simplesmente Lei 9.296/1996). A expressão `pode incluir hash` **não** equivale a impor um algoritmo específico por cláusula constitucional.

**STJ, AgRg no AgRg no HC 1.041.340/RS (5ª Turma, julgamento 15/04/2026, publicação 23/04/2026):** em cenário específico, manteve determinação de fornecimento à defesa da íntegra de extrações e documentação técnica para **exame assistido**, visando contraditório sobre integridade e admissibilidade; não é enunciado de direito universal de publicidade de dados particulares de terceiros sem filtros de sigilo.

**STJ, AgRg no HC 1.075.827/SP (5ª Turma, publicação 18/05/2026) e outros precedentes de 2026:** discutem exigência de prejuízo e limitações cognitivas do habeas corpus em controvérsia técnico-probatória; **mera irregularidade de método não prova adulteração nem produz automaticamente nulidade absoluta**. Há decisões que reconhecem necessidade de escrutínio técnico adicional e outras que exigem prova concreta de prejuízo. **Não** declarar que o STJ definiu uma tese única sobre toda aquisição forense ou ausência de hash. Apreciação de meio de prova, sigilo e direito à defesa é contexto-específica.

Fontes: [STJ edição 281](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/03062026-Nova-edicao-de-Jurisprudencia-em-Teses-traz-entendimentos-sobre-prova-digital-e-dados-estaticos-de-conexao.aspx), [STJ AgRg no AgRg no HC 1041340/RS](https://scon.stj.jus.br/SCON/pesquisar.jsp?b=ACOR&fr=veja&i=1&livre=%28%27AAHC%27+INPATH%28CLAS%29+AND+%271041340%27+INPATH%28NUM%29%29), [STJ AgRg no HC1075827/SP](https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?dt_publicacao=18%2F05%2F2026&num_registro=202600640991).

### Normas e direitos que não podem sumir

CF/1988 art. 5º X/XII (intimidade e comunicações), LVI (inadmissibilidade de provas ilícitas), LIV/LV (devido processo e contraditório), LVII (presunção de inocência), LXXVIII (duração razoável), LXXIX (proteção de dados). CPP arts. 6º, **157**, **158-A a 158-F**, 563; Lei9.296/1996 fluxo e Marco Civil Lei12.965/2014, arts.7 III, 10–11/22 para guarda/acesso a dados conforme hipóteses. Garantias de domicílio art. 5º XI e **Tema 280/STF** permanecem distintas da permissão de examinar conteúdo do celular encontrado depois.

**Competências do futuro texto:** M01 direito substantivo; **M12 reserva e funções investigativas/controle de polícia**, com parâmetros para urgências; M06 devido processo, remédios, supervisão jurisdicional, acesso útil a prova e exclusões; M07 agentes administrativos e tratamento de dados; M04 repartição federativa; CLF CPP/leis de comunicações. Especialidade M12 **não substitui** art. 5º X/XII, remédio HD de M06 nem Lei Penal reformada do CLF.

## 3. Parecer M12 próprio sobre P3-E x P3-R do M06

**P3-E (explicitar exceção mínima no texto constitucional):** tem coerência com a tese atual do Tema 977 e permite identificação fortuita mínima. **Risco estrutural:** criar permissão constitucional permanente com amplitude **maior do que a jurisprudência**, incluindo qualquer dispositivo e busca generalizada de conversas sob motivo artificial de "identificação". Exigir hipóteses **ativamente verificáveis**, fim exclusivo, registro de quais dados foram vistos, contenção e impugnação. A função pode ser descrita constitucionalmente e a implementação técnica ficar na lei; ainda precisaria definir o que configura **encontro fortuito**.

**P3-R (acesso sob reserva judicial universal salvo preservação técnica):** tutela informacional mais robusta que a exceção atual para identificação fortuita. **Não se pode apresentá-la como mera consolidação** do Tema 977, porque modifica deliberadamente os poderes atuais. **Objeção:** identificação de vítima/autor ou proprietário em cenário de urgência pode ser frustrada se não houver magistrado acessível; plantão e pedido emergencial são alternativas, com custos/necessidades a estudar. A urgência não pode ser usada para transformar consulta indiscriminada em regra.

**Terceira alternativa de redação constitucional a testar — P3-S (salvaguarda + exceção material estrita sem incorporar tecnologia):**

> A apreensão de equipamento não autoriza, por si, a investigação de seu conteúdo. O acesso estatal coercitivo a comunicações privadas ou a dados pessoais que revelem intensamente a vida privada exige consentimento livre e expresso do titular ou decisão judicial fundamentada, individualizada e delimitada nos casos legais, ressalvada exclusivamente a identificação mínima e justificada de autoria do fato ou do proprietário em encontro fortuito, em condições constitucionais precisas e sujeitas a revisão judicial.
>
> A lei disciplinará a preservação técnica necessária de dados e metadados de equipamento legalmente apreendido, com registro, finalidade de conservação, limitação de escopo, prazo, integridade e justificação posterior, **sem equipará-la à exploração investigativa do conteúdo**. Serão assegurados controle judicial tempestivo, acesso processual tecnicamente verificável pela defesa e proteção de terceiros, conforme as garantias gerais.

**Parecer M12 nesta fase:** P3-S é **candidata adicional** mais coerente se o usuário desejar manter funcionalmente a exceção atual, mas **NÃO superou os portões de equivalência**: (i) "dados que revelem intensamente" pode reduzir proteção de dados de conexão/metadados agregados; (ii) falta delimitação do encontro fortuito no nível constitucional, e o termo "nas condições constitucionais precisas" permanece remissão parcialmente vazia; (iii) acesso extrapenal não foi auditado; (iv) a expressão "apreensão legal" pede definição de legalidade da custódia; (v) revisão judicial de ato passado não convalida violação de reserva prévia quando exigida. **Não se recomenda converter P3-S em CF-NOR agora.**

**Hierarquia de segurança entre opções (apenas P):** entre Constituição que concede exceção em branco e P3-R, **P3-R protege melhor contra agente adversarial**; entre P3-E bem delimitada e P3-R, a escolha envolve equilíbrio institucional que não foi deliberado e necessidade de ouvir defesa, polícia técnica e magistratura. **Escolha aberta**, e nenhuma "melhor" opção automaticamente ratificada.

## 4. Quatro camadas de controle que devem coexistir

1. **Constituição A/G/E:** direito, reserva e exceção material mínima; proibição de busca geral arbitrária; devido processo e tutela.
2. **Lei processual/probatória:** pressupostos, autorização judicial, urgências e plantão, preservação técnica, relatórios, tratamento de terceiros, impugnação e sanções.
3. **Norma técnica e capacidade institucional:** documentação/cadeia de custódia, cópia forense, hashes apropriados, controle de versões, armazenamento seguro, rastreabilidade de operadores e auditoria externa. **Não** fixar software comercial, hash específico ou formulário em cláusula constitucional.
4. **Controle independente e contraditório:** magistrado, defesa, perícia independente, Ministério Público/Defensoria, supervisão de abuso, medidas de exclusão/indenização aplicáveis e remédios urgentes.

A **força probatória** não se confunde com a **licitude da fonte**. Desconformidade de registro técnico tampouco é igual a violação de reserva de jurisdição. O devido processo demanda decisão contextual, prova e possibilidade de contestação, sem descartar automaticamente material íntegro por formalidade trivial nem admitir devassa ilícita por ser tecnicamente perfeita.

## 5. Lacunas de pesquisa com responsabilidade definida

- **M12:** conceituar encontro fortuito como categoria fática/probatória, limite mínimo de identificação, relação com busca física e flagrante, retenção e exclusão de dados estranhos, proporcionalidade de coleta.
- **M06:** acesso útil da defesa a laudo/cópia forense quando necessário ao contraditório, sigilo de terceiros, impugnação de erros e consequências processuais da ilicitude, sem fórmula fixa de nulidade.
- **M07:** polícia/órgão executivo e autoridade de proteção de dados, deveres de registro, prestação de contas, integridade e accountability.
- **M01:** titularidade e proteção da privacidade/autodeterminação informacional, inclusive de vítima e terceiros não investigados.
- **M05:** infraestrutura pericial e plantões como custos estatais: **NÃO ESTIMADOS**; não presumir que exceção reduz gasto sem estimativa.
- **CLF:** disciplina infraconstitucional futura, não transpor artigos de CPP literalmente para CF.

**Matriz anexa:** `M12-01_MATRIZ_LEGALIDADE_INTEGRIDADE_CONTRADITORIO.csv`, com testes triplos L/I/C e respostas possíveis por variante. Valores são análises conceituais, **não cálculos de resultados judiciais**.

## 6. Portões de saída para eventual norma H

**K1** delimitação textual de encontro fortuito sem permissão geral; **K2** legalidade da apreensão independente da consulta; **K3** acesso condicionado a consentimento ou juiz com escopo; **K4** preservação técnica documentada distinta da devassa; **K5** não extrapolar celular penal para todas plataformas; **K6** contraditório e defesa auditáveis; **K7** tratamento distinto das consequências de ilegalidade, autenticidade e prejuízo; **K8** tutela em urgência/plantão; **K9** garantia específica de domicílio e sigilo; **K10** parecer M06/M07 e avaliação de custos; **K11** revisão atual do processo Tema977; **K12** prova de não regressão N:N e IDs de redação reservados. **Estado:** K1–K5 parcial, K6–K11 pendentes de prova adicional, K12 não iniciado; **sem autorização para H canônica ou D**.

## Referências
- STF [Tema 977](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=ARE&incidente=5173898&numeroProcesso=1042075&numeroTema=977) e [julgamento de mérito](https://portal.stf.jus.br/processos/listarProcessos.asp?classe=ARE&numeroProcesso=1042075).
- STJ [Jurisprudência em Teses 281 — 03/06/2026](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/03062026-Nova-edicao-de-Jurisprudencia-em-Teses-traz-entendimentos-sobre-prova-digital-e-dados-estaticos-de-conexao.aspx) e [AgRg no AgRg no HC 1041340/RS](https://scon.stj.jus.br/SCON/pesquisar.jsp?b=ACOR&fr=veja&i=1&livre=%28%27AAHC%27+INPATH%28CLAS%29+AND+%271041340%27+INPATH%28NUM%29%29).
- [CF/1988](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm), [CPP](https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm), [Lei9296](https://www.planalto.gov.br/ccivil_03/leis/l9296.htm), [Marco Civil](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm).

## FEITO / PENDENTE / PRÓXIMO
**FEITO:** primeiro parecer independente funcional M12.01, auditou distinção L/I/C, alternativas M06 P3-E/R e terceira P3-S com objeções, referências STF/STJ2026 e portões K1–K12. **PENDENTE:** acórdãos/votos completos em divergência, prova de custos e implantação, alternativas de exceção melhor redigidas, revisão cruzada M06/M07/M01 e teste jurídico-material de não regressão. **PRÓXIMO:** emitir revisão M12.01-R2 da excepcionalidade e dos dados estáticos/nuvem, coordenar com M01.13 sem promover H e registrar matriz N:N, depois deliberar entre P3-E/R/S. **QA:** CI estrutural, a conferir no SHA final, não certifica conteúdo ou decisões D.
