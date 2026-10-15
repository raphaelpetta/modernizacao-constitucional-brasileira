# M12.01-R3 — Juízo jurídico-material P4-E × P4-R e mapa N:N de garantias

**Corte:** 14/10/2026 · **Fonte de verdade de trabalho:** PR [#82](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/82), branch `pesquisa/m12-01-investigacao-digital-tema977-v01`; **base main prévia** `c28f254a76fb14c0ea4c553ebdbd07f7822ad4e8`. **Estado:** avaliação crítica P, **NÃO decisão D**, sem qualquer alteração às fichas `CF-NOR-0030/0031` no PR [#59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59). Interfaces M01/M06/M07, CF art.5º, CPP e CLF. A [issue #80](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/80) segue como registro de subciclo.

## 1. Resultado — o que está efetivamente em disputa

**Eixo real:** constitucionalizar **uma autorização extrajudicial para consulta mínima de celular encontrado fortuitamente** (P4-E) versus exigir juiz também nessa situação (P4-R). A segunda opção **não viola** a jurisprudência vigente: constitui **nova política constitucional** mais restritiva ao Estado, não mera reprodução do Tema 977. A primeira **pode** preservar a função atual, mas transformaria uma exceção estreita definida judicialmente em **poder constitucional expresso**, mais difícil de restringir por interpretação futura. **Não escolher por mera economia de palavras.**

**Patamar comum:** (a) apreensão física ≠ leitura de dados; (b) ordem individualizada, necessária, proporcional e com escopo para acesso investigativo normal; (c) preservar tecnicamente ≠ explorar semanticamente conteúdo; (d) direito de defesa a material técnico quando indispensável ao contraditório, sujeito a controles de terceiros; (e) prova de origem ilícita não se valida por cópia perfeita; (f) nulidade/inidoneidade decorrente de deficiência técnica exige exame jurídico contextual; (g) controles de registros, tutelas e responsabilização; (h) interceptação de comunicações em curso fora da exceção fortuita e sob regime próprio.

### Quadro de juízo de mérito — sem notas arbitrárias

| Interesse constitucional | P4-E: exceção expressa | P4-R: juiz inclusive no fortuito | Ônus probatório da opção |
|---|---|---|---|
| Continuidade da exceção do **Tema 977** | Aproxima-se da hipótese estrita atual, se redigida sem expansão | Rompe conscientemente a exceção de acesso sem ordem | Acórdão, tese e motivos da mudança |
| Segurança da intimidade e dados | Requer proteção contra pretextos e «encontro fortuito» fabricado | Bloqueio ex ante mais forte | Controle de logs/ordens/impugnações |
| Identificar autor/proprietário rapidamente | Consulta mínima potencialmente imediata | Plantão judicial capaz de decidir em tempo útil | Tempo de resposta real e risco de perda de identificação |
| Prova e cadeia de custódia | Consulta identificadora pode contaminar outras evidências | Decisão judicial formal não assegura integridade sozinha | Logs, cópia técnica, acesso pericial e contraditório |
| Direitos de vítimas e terceiros | Contenção estrita, sem abrir conteúdos estranhos | Preserva dados, pode demorar identificação | Risco concreto, urgência e meios alternativos |
| Risco de legislação oportunista | Exceção constitucional pode ser ampliada por conceitos vagos | Regras mais resistentes a «necessidade» genérica | Formulação textual e fiscalização efetiva |
| Custos institucionais | Treinamento, logs, defesa e auditoria do ato ex post | Plantões, equipe judicial e comunicação segura com polícia | Orçamento e série de pedidos, **não obtidos** |
| Tecnologias futuras | Não transportar fortuito do **celular** para nuvem/biometria | Reserva geral pode exigir regime próprio para outros suportes | Pesquisa autônoma de metadados remotos |
| Implantação | Lei detalha consulta mínima com evidência verificável | Lei detalha plantão, prioridade e tutela urgente | M06/M07/M12/CLF + transição |
| Risco residual | Fronteira identificadora versus investigação de conteúdo | Burocratização da exceção sem pronto atendimento | Testes adversariais e desenho de capacidade |

### Recomendação **de trabalho**, não decisão do constituinte

**Adotar provisoriamente P4-R como *padrão de teste de não regressão da proteção individual***, porque exige fundamentação de magistrado antes da consulta, tem semântica mais simples contra abuso e **não petrifica a exceção jurisprudencial de 2025**. **Não promover P4-R a H** sem resposta à objeção decisiva: o sistema conseguirá identificar vítima, proprietário e autor com plantão realmente disponível no tempo necessário? A solução de mérito pode inverter-se se evidências de urgência mostrarem que uma exceção P4-E *estritamente limitada e verificável* evita danos desproporcionais. Segurança pública legítima e direitos de vítimas são valores constitucionalmente relevantes.

**Declaração de limite:** preferência condicional em pesquisa não é D, nem autorização de alterar o `redacao/indice.csv`. Os desenhos anteriores P3-S e P4-E permanecem preservados como contrafactuais documentados.

## 2. Matriz N:N: garantias, competências e implementação — não apenas direito à privacidade

| Fonte vigente | Núcleo protegido | Peça do projeto | Resultado P4 | Estado |
|---|---|---|---|---|
| CF5 X | Intimidade e vida privada | M01 `CF-NOR-0030` H, E-COM ainda P | P4-E/R protegem parcialmente; não resolvem honra/imagem/reparação | **Parcial** |
| CF5 XII | Correspondência e sigilo de comunicações, exceções específicas | M01 E-COM/M12 | Não colar regra do fluxo a arquivos locais; reserva penal exige texto próprio | **Pendente** |
| CF5 XI | Entrada domiciliar e suas exceções | E-DOM, M12, M06 | Entrada legal não autoriza acesso geral aos dados de dispositivo dentro da casa | **Pendente** |
| CF5 LXXIX | Proteção de dados inclusive digital | M01 `CF-NOR-0031` H, M07 | Ambos protegem exame investigativo; faltam dados de tráfego/remotos e competências | **Parcial** |
| CF5 XXXV | Controle jurisdicional efetivo | `CF-NOR-0007` H e M06 | P4-R depende plantão efetivo, P4-E exige revisão posterior útil | **Parcial** |
| CF5 LIV/LV | Devido processo e contraditório | M06 e M12 | L/I/C independentes, acesso técnico útil, tutela de terceiros | **Pendente** |
| CF5 LVI | Inadmissibilidade de provas ilícitas | M06/M12, CLF CPP157 | Integridade não convalida devassa de origem; regra de exclusão ainda sem ficha própria | **Bloqueio** |
| CF5 LXXVIII | Duração razoável e medidas urgentes | M06/M07 | Sem urgência judicial funcional, P4-R corre risco operacional | **Pendente** |
| CF5 LXXII/LXXVII | Habeas data e gratuidade | M06 E-HD | Acesso a dados públicos do titular **não** se confunde com busca penal de prova | **Outro instrumento pendente** |
| CPP6,157,158-A–F | Polícia, prova ilícita e cadeia de custódia | CLF penal/processual, M12/M06 | Lei e regulamentos definem métodos, autorização, documentação e perícia | **Implementação futura** |
| Marco Civil 7 III, 10 e 22 | Dados guardados por provedores/conexão | CLF/M07/M12 | Tema 977 do **celular** não autoriza acesso genérico a provedor | **Bloqueio de extrapolação** |
| STF Tema 977 | Exceção fortuita, acesso ordinário, preservação, modulação | M12 P4-E/R | P4-E aproxima regime atual; P4-R mudaria **poder investigatório**, sem apagar outros direitos | **Escolha A** |
| STF Tema 280 | Flagrante domiciliar exige razões anteriores e justificação posterior | M01 E-DOM/M12 | Não usar localização do celular para validar retroativamente ingresso ilegal | **Bloqueio independente** |
| STJ jurisprudência digital 2026 | Integridade, perícia em dúvida razoável, contraditório e prejuízo | M12/M06/CLF | Não universalizar ausência de hash = nulidade, nem aceitar cópia íntegra obtida ilicitamente | **Aferição contextual** |

**Conclusão da matriz:** nem P4-E nem P4-R demonstraram cobertura plena das garantias de 1988 ou eliminação das remissões pendentes; **não confundir preservação de direitos vigentes com preservação de toda faculdade de atuação policial atualmente admitida**. Mudança de faculdade pode ser constitucionalmente legítima por decisão consciente, mas deve ser anotada como tal.

## 3. Casos difíceis que impedem texto definitivo

**F1 — titular dos dados ≠ proprietário do suporte:** aparelho de empregador, vítima ou criança; consentimento do dono do hardware não necessariamente autoriza acessar dados privados de terceiros. Exigir hipótese, titularidade e competência para consentir; não resolver com expressão vaga "o titular".
**F2 — identificação que exige olhar contato mínimo:** a proibição absoluta de ler "qualquer conversa" em P4-E pode impedir identificação excepcional admitida pela tese. Melhor proibir exploração sem pertinência à identidade/fato e registrar o mínimo estritamente necessário, com controle. Norma penal detalha qual campo técnico.
**F3 — celular que cai durante prisão em flagrante:** classificar pela circunstância objetiva da descoberta, não pelo rótulo escolhido pela autoridade. P4-E necessita distinção verificável contra abuso; P4-R independe dela para reserva de acesso.
**F4 — preservação pode copiar setores da memória:** leitura técnica para gerar imagem/hash ≠ análise semântica livre, mas qualquer operação pode processar dados; exigir finalidade, mínima aquisição necessária, registro e guarda.
**F5 — intimação e plantão:** P4-R só pode ser escolhida com projeção de custos e plantões penais, inclusive em pequenas comarcas e regiões remotas; **não há dados empíricos verificados neste ciclo**.
**F6 — segredo profissional, vítimas e terceiros:** controle de conteúdo apreendido e acesso da defesa por meio assistido são simultaneamente necessários; não autorizar publicação geral de material privado.
**F7 — modulação Tema 977:** efeitos prospectivos da tese vigente e exceção para pedidos defensivos até julgamento são fatos de direito atual; futura Constituição precisa regime próprio de aplicação no tempo, não "revoga retroativamente" decisões por implicação.

## 4. Decisão pendente explicitada para deliberação futura

1. **D-OP1 (aberta):** exceção constitucional mínima do celular fortuito (P4-E), ou juiz como padrão universal no fortuito (P4-R)?
2. **D-OP2 (aberta):** qual é o limite tecnológico e pessoal da proteção, e a lei pode definir técnicas sem criar uma nova exceção material?
3. **D-OP3 (aberta):** regime de controle posterior da preservação e remédios efetivos com tutela judicial e contraditório?
4. **D-OP4 (aberta):** como instituir plantão/capacidade de perícia e custear supervisão, sem transformar urgência em acesso discricionário?
5. **D-OP5 (aberta):** compatibilidade com provas ilícitas, prazo transicional e proteção de terceiros?

**Porta de entrada em `CF-NOR` futura:** fechar deliberações materialmente essenciais, obter parecer M01/M06/M07, teste N:N e preflight de ID, então produzir uma só ficha H por norma E em `redacao/propostas/`, reexecutando gerador e CI. Até lá, não alterar PR59.

## 5. Evidências primárias e limites

- [STF Tema 977 — tese e andamentos oficiais](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=ARE&incidente=5173898&numeroProcesso=1042075&numeroTema=977), ata do Pleno 25/06/2025 e acórdão publicado 24/09/2025, item 2 contém redação ambígua "referido acesso" no contexto de preservação. **Não tratar parecer/voto anterior como tese final**.
- [STF Tema 280](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=280), entrada domiciliar.
- [CF/1988](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm), [CPP](https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm), [Marco Civil](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm).
- [STJ Jurisprudência em Teses 281](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/03062026-Nova-edicao-de-Jurisprudencia-em-Teses-traz-entendimentos-sobre-prova-digital-e-dados-estaticos-de-conexao.aspx) e decisões discutidas em `M12-01_REDLINE_P4_EXCECAO_E_CADEIA_CUSTODIA_v0.1.md`. Acórdãos e eventuais embargos posteriores ainda exigem verificação antes de D. **Este dossiê não comprova custo real ou resultado de operação policial.**

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** comparação de mérito sem ranking numérico, matriz N:N de 14 fontes/funções, sete falhas de borda e registro das cinco deliberações abertas; preferência de teste P4-R **expressamente não vinculante**. **PENDENTE:** revisão independente M01/M06/M07 e custo/tempo de plantão, detalhamento de terceiro/fortuito/preservação e prova, nenhum D/CF-NOR. **PRÓXIMO:** solicitar M06/M07 avaliação dirigida F1–F7, fechar questões materialmente necessárias com usuário e testar viabilidade de plantão antes de qualquer ficha E H; atualizar PR82 e issue80. **QA:** verificar CI após gravação; CI estrutural não certifica juízo de mérito.
