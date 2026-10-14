# M06.02 — Auditoria funcional dos remédios constitucionais e acesso à Justiça

**ID:** CF-M06-S002 · **Corte:** 14/10/2026 · **Status:** pesquisa F0–F5 especializada, testes F8 preliminares; **nenhuma deliberação F6/D e nenhum CF-NOR criado**.  
**Issue:** [#65](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/65). **PR de pesquisa:** [#62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62), draft, acumulando M06.01–02; a branch não pressupõe merge de M06.01. **Main de entrada:** `eaab37bcd5467d48db0cc0bda133c62ee7801ffe`. **CF-NOR-0007:** H, regra geral, não aprovada.  
**Interfaces:** M01 (direito e titularidade), M07/CLF T07.M03 (decisão administrativa), M09 (direitos sociais), M12 (liberdade e penal), M13 (CADH), M05 (custeio da Defensoria).

## 1. Questão de desenho (F0)

A eventual simplificação do texto deve proteger **funções de tutela**, não conservar necessariamente todo o nome/procedimento vigente. Para cada remédio, verificar os nove eixos:  
**(1)** pessoa legitimada individual e coletivamente; **(2)** direito protegido e exclusões de cabimento; **(3)** autoridade ou particular destinatário; **(4)** gratuidade, advogado, Defensoria e acessibilidade; **(5)** tutela urgente e preventiva; **(6)** prova e ônus/obtenção; **(7)** prazo e prioridade; **(8)** natureza dos efeitos e execução; **(9)** relação com devido processo e outras ações.

**Não presumir:** “tutela judicial efetiva” de CF-NOR-0007 H **não** estabelece automaticamente esses elementos. **Não concluir oposto:** a Constituição futura não é obrigada a imobilizar em seu texto cada prazo da legislação de 1965–2016. Requer prova de substituição funcional, não apenas semelhança verbal.

## 2. Inventário do direito brasileiro vigente (F1) — cinco instrumentos

### 2.1 Habeas corpus (CF art. 5º LXVIII; LXXVII)

**Objeto:** liberdade de locomoção ameaçada ou constrangida por ilegalidade/abuso de poder. A proteção comporta prevenção e reação, com urgência, e possui gratuidade constitucional. **Problema de proteção:** em cenário de prisão arbitrária, recurso ordinário lento, custas e formalidades de representação podem tornar o remédio inútil. Verificar em profundidade regimes de processamento e hipóteses específicas do CPP, jurisprudência de substitutividade, restrições e poderes do juiz antes de reproduzir fórmula geral.

**Não é** ação universal para qualquer direito nem instrumento de correção de dados cadastrais. A proteção constitucional material da locomoção deve coexistir com juiz natural, regras de flagrante/prisão, informação ao preso e proibições absolutas (M12).

### 2.2 Mandado de segurança individual/coletivo (CF art. 5º LXIX–LXX; Lei 12.016/2009)

**Objeto:** direito líquido e certo frente à ilegalidade/abuso de autoridade, não protegido por HC/HD. **Requisitos atuais ordinários:** comprovação pré-constituída, legitimados, prazo de 120 dias contado da ciência do ato impugnado (**lei**, art. 23), decisões urgentes e regime coletivo. **Não criar prazo constitucional imutável de 120 dias sem razão**; distinguir existência do remédio de regra processual de decadência.

**STF ADI 4.296, julgamento 09/06/2021:** o Plenário afastou parte das restrições legais a liminares em MS, inclusive vedação específica relativa a compensação de créditos tributários/liberação de mercadorias e exigência de oitiva prévia do representante público como condição de liminar coletiva. **Consequência de projeto:** não transformar “tutela prioritária” em direito sempre subordinado ao contraditório prévio, nem dispensar todo contraditório ulterior. Verificar integralidade do dispositivo/acórdão e efeitos temporais antes de copiar a técnica decisória.

**Melhor objeção:** decisões urgentes contra o Estado podem afetar orçamento e serviços, mas exigência absoluta de audiência prévia pode gerar dano irreversível. A arquitetura constitucional deve habilitar juízo concreto, não proibir liminar por categoria.

### 2.3 Mandado de injunção individual/coletivo (CF art. 5º LXXI; Lei 13.300/2016)

**Objeto:** inviabilidade do exercício de direitos, liberdades ou prerrogativas constitucionais por ausência de norma regulamentadora. A **Lei 13.300/2016**, especialmente arts. 8º e 9º, prevê reconhecimento da mora e condições para o exercício do direito, com distinções do alcance subjetivo/temporal; possui legitimidade coletiva própria nos arts. 12–13. **Não é mera condenação por omissão legislativa**, nem autoriza o Judiciário a substituir sem critério toda a política legislativa.

**Escolha aberta:** remédio especializado versus tutela geral de omissão, desde que preserve (i) acesso do titular, (ii) proteção intertemporal, (iii) possibilidade de exercício prático, (iv) respeito à competência legislativa e (v) tratamento coletivo. Exige coordenação M00/M03/M06.

### 2.4 Habeas data (CF art. 5º LXXII/LXXVII; Lei 9.507/1997)

**Objeto atual:** acesso e correção de informações pessoais em registros de entidades governamentais ou de caráter público. **Lei 9.507/1997**, art. 7º I–III, também prevê anotação de contestação ou explicação em determinado contexto. A lei exige prova da recusa ou demora administrativa no art. 8º, parágrafo único, com **prazos legais diferenciados** (10 dias de acesso e 15 dias nas outras hipóteses, quando ausente decisão, não prazo constitucional único de 10 dias). A via de habeas data é **gratuita** por CF/lei.

**Crítica operacional:** uma redação de proteção de dados sem remédio eficaz pode prometer acesso/correção, mas deixar o cidadão preso a ação comum onerosa; uma tutela exclusivamente de habeas data de 1997 pode ser insuficiente contra classificação automatizada/compartilhamento privado em escala. Examinar função do `CF-NOR-0031` (PR59 draft), da LGPD e de recursos administrativos sem presumir ampliação automática de todos os requisitos do HD a qualquer empresa.

### 2.5 Ação popular (CF art. 5º LXXIII; Lei 4.717/1965)

**Objeto:** ação proposta por cidadão com vistas a anular ato lesivo ao patrimônio público, moralidade administrativa, meio ambiente ou patrimônio histórico-cultural (conforme CF/1988). A garantia constitucional dispensa custas e ônus sucumbenciais **salvo comprovada má-fé**, assegurando controle cívico com risco processual diferenciado. A Lei 4.717/1965 disciplina legitimidade, pluralidade dos réus e participação do MP, execução e prazos.

**Tensão de reforma:** regime do cidadão-eleitor pode excluir residente não eleitor que sofra dano ambiental ou pessoas jurídicas; isso não demonstra sozinho que o instrumento deva ser abolido, pois tutela coletiva, Ministério Público, associações, Defensoria e controle administrativo podem coexistir, conforme funções. Estudar extensão futura da legitimidade e controle de litigância temerária sem criar barreiras econômicas generalizadas.

## 3. Remédios não são substitutos entre si

| Critério | HC | MS | MI | HD | Popular |
|---|---|---|---|---|---|
| Núcleo | Locomoção | Direito líquido/certo e autoridade | Omissão regulamentadora | Informação pessoal pública ou de caráter público | Controle cidadão de atos lesivos públicos |
| Proteção preventiva | Sim | Sim, justo receio | Omissão atual impeditiva, tutela concreta | Acesso/correção diante de negativa/demora | Pode requerer tutela para impedir consumação |
| Prova | Coação/ameaça e ilegalidade; rito especial | Documentação pré-constituída como modelo legal | Omissão e inviabilidade | Recusa/demora ou atendimento insuficiente | Lesão/ilegalidade e prova coletável |
| Titular/legitimidade | Amplo regime constitucional/processual a examinar | Individual e legitimados coletivos específicos | Individual e coletivo conforme lei | Pessoa de quem tratam os dados | Cidadão; demais vias coletivas coexistem |
| Custos | Gratuito constitucionalmente | Regime de custas/justiça gratuita em lei | Idem, com proteção de acesso | Gratuito constitucionalmente | Isenção constitucional salvo má-fé |
| Risco de substituição por ação comum | Prisão sem resposta rápida | Dano irreparável/prova documental | Direito permanece inexercível | Cadastro inacessível e segredo estatal | Desincentivo econômico a controle cidadão |
| Interfaces | M12/M06 | M07/M06 | M00/M03 | M01/M07 | M02/M07/M10 |

**Nota jurídica:** “prévia provocação administrativa” deve ser tratada para cada instituto separadamente, sem criar requisito de exaurimento universal do contencioso administrativo para o acesso à Justiça.

## 4. Confronto com CF-NOR-0007 e PR59 (H), cláusula por cláusula

`CF-NOR-0007` H assegura “apreciação judicial de lesão ou ameaça” e tutela “acessível, efetiva, tempestiva e adequada”, o que **incide como garantia geral útil**, mas falta especificar:
- proteção da liberdade ameaçada **sem taxas** e com resposta em tempo útil;
- mecanismos de contorno de provas em poder do Estado, onde cabível;
- solução efetiva para **omissão regulamentadora**;
- acesso/correção gratuita de dados e controle de atos estatais lesivos à coletividade;
- legitimação cívica e coletiva, proteção contra custos punitivos;
- coexistência com Defensoria/assistência jurídica integral e recurso interamericano.

`CF-NOR-0030–0031` (PR59 H **não na main**) investigam privacidade e dados, mas **não** substituem sem auditoria as garantias de sigilo, acesso, correção, liminares e reserva especial de comunicações. **Não inserir novas normas CF-NOR nesta pesquisa M06.02**: primeiro elaborar parecer jurídico para M01.13.

## 5. Alternativas institucionais e critérios de teste (F3–F5)

**Modelo A — manter cinco nomenclaturas constitucionalmente:** benefícios previsibilidade/controle e diversidade funcional; custos de complexidade e sobreposição de vias.  
**Modelo B — cláusula geral + remédio de liberdade gratuito + tutela rápida de ato estatal + tutela de omissão + dados + legitimidade popular/coletiva, com nomes técnicos adaptáveis:** potencial simplificação com conteúdo preservado e inovação futura; exige cláusulas de legitimidade, custos e tutelas suficientemente densas. **Hipótese preferida para teste, não deliberação.**  
**Modelo C — uma ação ordinária universal com todo regime em lei:** sofre risco elevado de captura orçamentária e procedimental por legislador hostil; só estudável com salvaguardas constitucionais equivalentes expressas, e a hipótese de equivalência não foi demonstrada.

**Indicadores reais ainda a coletar, não inventar:** tempo para concessão de liminares; cumprimento de ordens; origem territorial e classe econômica; uso de Defensoria; custo pericial/recursos; comportamento da litigância coletiva; acesso digital e barreiras de linguagem.

## 6. Testes adversariais e obrigações de prova (F8)

Acompanhar a `M06-02_MATRIZ_FUNCIONAL_REMEDIOS.csv` (linhas por instituição × função) e a `M06-02_TESTES_REMEDIOS.csv` (situações de legislador adversário). Cada cenário possui ação atual, consequência jurídico-material a preservar, substituto proposto, objeção mais forte, prova faltante e estado `A/V`.

**Casos especialmente sensíveis:**
1. Governante prende opositor e taxa o remédio de liberdade.
2. Governo vincula toda liminar coletiva à audiência prévia do próprio órgão causador do risco (ADI 4.296).
3. Poder Legislativo deixa de regulamentar direito, forçando a pessoa a esperar indefinidamente.
4. Órgão público nega acesso a dados pessoais e cria custo inicial para retificação.
5. Cidadão denuncia fraude orçamentária e é dissuadido por sucumbência automática.
6. Pessoa com deficiência não consegue manejar processo inacessível tecnicamente.
7. Medida de urgência protege uma pessoa, mas execução não ocorre em tempo útil.
8. Estado invoca proteção de dados para impedir transparência sobre irregularidades, exigindo conciliação entre privacidade e controle cívico.

## 7. Portas de segurança para futuras normas H

**A futura Constituição poderia** descrever garantias instrumentais por função, porém a conclusão de equivalência exige:
- direitos tutelados e legitimados explícitos;
- acesso acessível e economicamente viável;
- resposta preventiva e liminar contra dano irreversível, com contraditório apropriado;
- remédio para omissão e controle de dados;
- proteção coletiva contra lesões transindividuais;
- execução efetiva e transparência compatível com privacidade;
- competências e reserva de jurisdição nos lugares apropriados;
- não congelar todos os prazos atuais de lei ordinária (ex. 120 dias MS; 10/15 dias HD);
- interface com M06 de desenho judiciário e M12 de processo penal.

## 8. Referências oficiais específicas, limites e validação

- [Constituição compilada, arts. 5º XXXIV–LXXVIII, Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm).
- [Lei 12.016/2009, MS, arts. 1º, 21–23](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/lei/l12016.htm).
- [STF ADI 4.296, julgamento 09/06/2021](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=467335) — notícia oficial, ainda exigir exame do inteiro teor no ciclo de mérito.
- [Lei 13.300/2016, mandado de injunção](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/lei/l13300.htm).
- [Lei 9.507/1997, HD e requisitos diferenciados](https://planalto.gov.br/ccivil_03/leis/l9507.htm).
- [Lei 4.717/1965, ação popular](https://planalto.gov.br/ccivil_03/leis/l4717.htm).
- [STJ Tema 1.178, gratuidade, atualizado 13/08/2026](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1178&cod_tema_inicial=1178&novaConsulta=true&tipo_pesquisa=T).
- [CADH, arts. 8/25](https://www.oas.org/pt/cidh/mandato/Basicos/convencion.asp) e [África do Sul §38](https://www.justice.gov.za/legislation/constitution/chp02.html) — comparação funcional, **não** fonte de obrigatoriedade de formato brasileiro.

**Precisão de autoridade:** consulta ao texto legislativo e sínteses oficiais; ADI 4296 precisa de acórdão integral para testar todas consequências. Não assegurar que o regime legal atual ou seu título são constitucionalmente intangíveis. Sem coleta de séries CNJ nem experimentos empíricos neste subciclo.

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** inventário funcional dos cinco remédios, revisão de leis 1965–2016, contraste com `CF-NOR-0007` H e PR59, opções A/B/C, matrizes e testes de regressão, fontes oficiais.  
**PENDENTE:** acórdãos integrais, instrumentação empírica CNJ/Defensoria, jurisprudência interamericana, custos estimados, execução contra fazenda e regras de HC em todos os ritos, auditoria de outros instrumentos (ACP, ADPF, ações constitucionais abstratas) sem substituição automática. **Não F6/D.**  
**PRÓXIMO:** M06.03 candidato — tutela coletiva, Defensoria, execução de decisões e dados de Justiça; em paralelo emitir parecer M06 ao PR59 quanto a HD/privacidade. Reservar ID e issue na próxima rodada, relendo a main e demais frentes.

**Controle:** fonte normativa única em `redacao/` **não editada**; a pesquisa está no PR62, não na main. O status de CI deve ser verificado no SHA final.
