# M09.02 — Auditoria constitucional do trabalho: art. 7º e representação coletiva

**ID:** CF-M09-S002 · **Data de corte:** 14/10/2026 · **Estado:** pesquisa F0–F5, testes F8 preliminares, **sem ratificação F6/D**.  
**Base da main:** `eaab37bcd5467d48db0cc0bda133c62ee7801ffe`; branch de pesquisa e [PR #63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63) draft. **Issue:** [#66](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/66). Continuidade de M09.01, [issue #56](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/56). Nenhuma fonte canônica `redacao/` editada.

## 1. Pergunta constitucional, sem solução pré-ratificada

É possível **consolidar** os 34 incisos e parágrafo único do art. 7º, além das 11 proteções funcionais dos arts. 8º–11, numa estrutura mais simples que:
(a) preserve direitos materiais já conquistados e sua efetividade;
(b) não transforme proteção mínima em autonomia negociadora fictícia; 
(c) permita reforma de arranjos financeiros, benefícios e tecnologias mediante prova de equivalente ou melhor proteção;
(d) respeite participação de pessoas vulneráveis, liberdade sindical, empregadores e autonomia privada?
O objetivo não é reproduzir 35+11 dispositivos em outro título nem afirmar que tudo pode ser relegado à lei.

**Instrumentos desta rodada:** [matriz dos 34 incisos + parágrafo único](M09-02_MATRIZ_ART7_INCISOS.csv) (**35 linhas**), [matriz dos arts. 8º–11](M09-02_MATRIZ_ART8_A_11.csv) (**11 linhas**) e [testes adversariais](M09-02_TESTES_TRABALHO.csv). Em todas as linhas o código `equivalencia_ao_anteprojeto = NAO_DEMONSTRADA` é intencional: o piloto `CF-NOR-0004` H não contém esses patamares.

## 2. Classificação: conteúdo material, modelo de implementação e contingências

A matriz utiliza:
- **Q** — **quantitativo explícito atual** (8/44 horas, 6 horas revezamento, 50% extraordinária, 1/3 férias, 120 dias maternidade, 30 dias aviso prévio, idades 14/16/18, prazos prescricionais, mínimo salário etc.). O *número* é parte do direito vigente e não simples preferência administrativa. Pode ser discutido e modernizado constitucionalmente, mas com proposta expressa, análise técnica, proteção comparada e transição.
- **A** — conteúdo material mínimo **autônomo** (não discriminação, segurança, proteção salarial, acidente, maternidade e cuidado etc.), inclusive onde a CF remete sua operação à legislação.
- **F** — mecanismo de custeio/proteção financeira (FGTS, seguro-desemprego, salário-família, benefícios, previdência).
- **I** — proteção de organização/participação coletiva (organização, convenções, resultados, segurança).
- **S** — reserva ou salvaguarda específica; **L** — disciplina infraconstitucional passível de reforma sem esvaziar núcleo.

Estas classes **não têm correspondência automática** aos tipos editoriais G/E/A/X/T da fonte única. Quando o futuro projeto redigir, converter função em norma A/E somente com autorização e índice canônico, não repetir o direito por classificações.

### 2.1 Proteções quantitativas que exigem deliberação expressa

**Art. 7º XIII–XVII** reúne jornada normal **até 8h por dia e 44h por semana**, redução/compensação nas condições constitucionais; **6h** em turnos ininterruptos de revezamento salvo negociação coletiva; descanso semanal remunerado; hora extraordinária com acréscimo **mínimo de 50%**; férias anuais acrescidas de **pelo menos 1/3**. Na CF vigente, são garantias distintas: tempo máximo, descanso efetivo, remuneração por sobretrabalho e negociação.

**Arts. 7º XVIII, XXI e XXXIII** preveem **120 dias** de licença à gestante sem prejuízo emprego/salário, aviso prévio mínimo de **30 dias** proporcional e vedação de trabalho em geral para menores de **16**, exceto aprendiz a partir de **14**, e proibições de trabalho noturno, perigoso ou insalubre abaixo de **18**. Limites diferentes protegem situações diferentes; não confundir com mero objetivo abstrato de emprego digno.

**Art. 7º XXIX:** prescrição quinquenal dos créditos durante relação, até **2 anos** após a extinção do contrato. É proteção/contenção intertemporal, não mero prazo de qualquer regulamento. A eventual reforma precisa avaliar acesso a prova, assimetria e segurança jurídica antes de constitucionalizar ou deslocar a matéria.

**Art. 7º IV, VII, VIII:** piso salarial mínimo nacional, piso dos variáveis e 13º salário. Não se deve assumir que um “direito genérico a salário adequado” produz automaticamente os mesmos efeitos econômicos/jurídicos. Tampouco que cada modelo monetário atual é irreformável: estudar salário real, proteção familiar, inflação e efeitos distributivos (M05) antes de propor troca.

**Art. 7º parágrafo único/EC 72/2013:** trabalhadores domésticos têm rol próprio e integração previdenciária. Uma nova fórmula universal de proteção **poderia ser superior**, mas só se cobrir efetivamente os riscos e as diferenças setoriais; não presumir extensão automática apenas pela palavra “todos”.

### 2.2 Direitos que exigem salvaguardas mesmo com detalhamento legal

- Proteção contra dispensa arbitrária (I), seguro-desemprego e FGTS (II–III): distinguir resultado de proteção econômica dos instrumentos que o realizam; compensação, custeio, transição e negociação. Conferir regra de ADCT sobre indenização de dispensa antes de propor supressão ou transição.
- Salário/proteção de retenção dolosa (V–X) e prestações familiares, lucros (XI–XII). **A Constituição vigente qualifica a retenção dolosa salarial como crime** no inciso X; eventual redesenho pertence também M12 (legalidade penal), não texto laboral genérico.
- Ambiente de trabalho seguro (XXII), adicionais por risco (XXIII) e seguro/reparação de acidentes (XXVIII) são **complementares, não permutáveis**: adicional pecuniário não é licença para expor trabalhadores a risco evitável; indenização após o dano não substitui prevenção.
- Proteção em face de automação (XXVII): avaliar perda de ocupações, discriminação algorítmica, treinamento, transição e responsabilização, sem pressupor constitucionalizar uma tecnologia ou inviabilizar digitalização.
- Vedação de discriminação e proteção de deficiência (XXX–XXXII) exige igualdade setorial e acesso a remédios mesmo com `CF-NOR-0008–0011` H no catálogo geral.

### 2.3 Arts. 8º–11: organização, liberdade sindical e assimetrias

**Art. 8º I:** autonomia sem licença governamental, proteção contra intervenção. **Art. 8º II:** unicidade sindical (uma organização por categoria/base territorial de tamanho mínimo), opção institucional vigente que **não se confunde** com o núcleo da liberdade sindical. **Arts. 8º III–VIII:** representação, custeio, liberdade de não filiação, participação na negociação, aposentado filiado e proteção da liderança contra dispensa.

**Art. 9º:** greve é direito, mas a proteção de necessidades inadiáveis em serviços essenciais exige lei e controle, sem equiparar todo serviço prestado por particulares a um setor onde a paralisação é sempre proibida. **Art. 10:** participação de trabalhadores/empregadores em órgãos públicos pertinentes. **Art. 11:** representante eleito nas empresas com mais de **200 empregados** — comparar a finalidade de representação direta com o número, que pode ser circunstancial.

**OIT, status de ratificação em 14/10/2026:** o sistema oficial **NORMLEX** inclui as Convenções **87 (liberdade sindical) e 187 (marco promocional de segurança e saúde)** entre os instrumentos fundamentais **não ratificados pelo Brasil**. Não declarar que são tratados formalmente incorporados e vinculantes no Brasil. A **Declaração da OIT de 1998, emendada em 2022**, estabelece os cinco princípios e direitos fundamentais do trabalho também para membros que não ratificaram instrumentos associados; distinguir compromisso por filiação e vigência interna de tratado específico. **Verificar separadamente ratificações de Convenções 98, 100, 111, 138 e 155 ao utilizá-las.**

A unicidade sindical constitucional atual é uma das controvérsias mais importantes: modernizar o modelo com pluralismo não significa eliminar representação eficaz nem supor que toda fragmentação fortalece trabalhadores. Examinar coerência de negociação, poder de mercado, financiamentos e antirretaliação.

## 3. STF Tema 1.046: negociação coletiva e limite material

A tese do STF (ARE 1.121.633) admite negociações setoriais com limitações ou afastamentos de certos direitos independentemente da explicitação de vantagens compensatórias específicas, **desde que respeitados direitos absolutamente indisponíveis**. Não é autorização irrestrita para renunciar a saúde/segurança, trabalho infantil proibido, antidiscriminação, integridade e limites materialmente protegidos.

**Questões para o desenho futuro:**
1. Quais direitos materiais são indisponíveis e o que pode ser ajustado coletivamente?
2. A autonomia sindical sem genuína representatividade pode legitimar renúncia forçada?
3. Que mecanismos de aferição democrática, transparência e impugnação protegeriam minorias de uma categoria?
4. Como articular direitos do trabalhador individual, legitimidade sindical, empregadores e a dignidade/integridade do M01?
5. Se a Constituição futura alterar o patamar obrigatório, quais transições resguardariam relações existentes?

**Não** transplantar a tese atual como regra nova ratificada; investigar primeiro com decisões integrais e evolução posterior.

## 4. Direito comparado: diferenças úteis e limites (F2–F3)

**Portugal — CRP art. 59:** proteção de salário igual, condições dignas, conciliação trabalho-família, saúde, descanso, limite de jornada, férias remuneradas, assistência por desemprego involuntário e reparação por acidente. Modelo com **núcleo material explícito** sem reproduzir em todos os casos o mesmo detalhamento numérico brasileiro. Questão: que aspectos exigem quantitativos constitucionais para serem efetivos em cenários de governo/empregador hostil?

**África do Sul — Constituição §23:** direito a práticas laborais justas, sindicatos, greve e negociação coletiva, inclusive organizações de empregadores, sob limites gerais §36; desenho que protege **funções institucionais**, cabendo muitas especificidades à legislação. Potencial fragilidade: fórmula geral pode permitir grande divergência de resultados se proteção legislativa/efetividade de execução for fraca.

**OIT — cinco princípios fundamentais desde 2022:** liberdade sindical e negociação coletiva, eliminação do trabalho forçado, erradicação do trabalho infantil, não discriminação e ambiente de trabalho seguro/saudável; norma de direito internacional e compromisso de filiação, **não um capítulo constitucional pronto**.

**História brasileira:** mudanças no alcance dos direitos de trabalhadores rurais, domésticos e avulsos, proteção a maternidade, idade mínima, segurança no trabalho e organização sindical. A EC 72/2013 e a EC 20/1998 demonstram que a Constituição é já um sistema de direitos materialmente atualizado, não só folha de princípios; aferir custos e limitações da proteção existente.

## 5. Três arquiteturas concorrentes e pontos adversariais

| Opção | Forma | Vantagem | Objeção |
|---|---|---|---|
| A — conservar lista extensiva semelhante à CF/1988 | Direitos quantitativos e institucionais enumerados artigo/inciso por artigo/inciso | Continuidade verificável contra regressão rápida | Dificuldade de alterar arranjos e problemas de coesão |
| B — cláusula forte de direitos laborais, com pisos e garantias especiais claramente identificados | Núcleos materiais (renda, jornada, repouso, maternidade, antidiscriminação, segurança, coletiva, execução) + regras específicas para garantias que precisam de número/procedimento | Simplifica linguagem sem deixar tudo para lei | Se pisos não forem explicitados ou substituídos com eficácia, simplificação vira regressão |
| C — direito geral ao trabalho digno, proteção remanescente toda por lei e negociação | Grande discricionariedade pública/privada | Adaptação rápida e texto curto | Fragilidade diante de crise, captura sindical ou do legislador, desigualdade de barganha |

**Hipótese P para avaliar:** B pode ser superior a A/C **somente após matriz de continuidade por inciso** e auditoria quantitativa e institucional. Não foi aprovada como desenho. **Não propor ainda CF-NOR**.

## 6. Portões de qualidade para futura decisão

- Nenhum quantitativo atual será apagado sem identificar o direito e proteger resultado comparável ou melhor; uma média salarial geral não basta para demonstrar ganho para grupos vulneráveis.
- **Não equiparar** proteção do salário, segurança no trabalho e compensação financeira: direitos de prevenção e proteção pós-dano coexistem.
- Direito sindical positivo e negativo; órgão de representação sem interferência, proteção contra retaliação e negociação real, com controle de assimetria.
- Proteção de trabalhadores domésticos, rurais, avulsos, informais e em plataformas; **não** afirmar que art. 7º hoje cobre indistintamente todas as formas sem lei e interpretação.
- M09 define conteúdo material; M05 avalia fontes/efeitos fiscais, M08 relações econômicas, M06 acesso/execução, M01 igualdade. Substituição que afete M04/M05/M06 requer estudos, não aprovação isolada M09.
- Jurisprudência sobre validade de negociação e interpretações de indisponibilidade, status real dos tratados OIT, legislação trabalhista federal em 2026, dados PNAD/CAGED/RAIS e custos são **portas obrigatórias antes de proposta definitiva**.
- Critérios de avaliação: cobertura, salário real, desigualdade por gênero/raça/deficiência, informalidade, segurança, desemprego, passivo trabalhista, acesso à Justiça, contribuição/custeio e diferenças regionais. Dados reais **não foram tratados nesta rodada**.

## 7. Perguntas M09.02 abertas

**TRAB01** piso protetivo quantitativo X regra geral e lei; **TRAB02** jornada e descanso; **TRAB03** proteção contra dispensa e fundos; **TRAB04** maternidade/paternidade/parentalidade e custeio; **TRAB05** segurança e risco; **TRAB06** sindicatos, pluralismo/unicidade, representação; **TRAB07** negociação coletiva e absolutamente indisponíveis; **TRAB08** domésticos, avulsos, plataformas e informalidade; **TRAB09** trabalho infantil, discriminação e deficiência; **TRAB10** automação e transição; **TRAB11** prescrição, ações e tutela; **TRAB12** competências, financiamento, ADCT e transição.

## 8. Fontes oficiais e certeza

- [Constituição compilada art. 7º I–XXXIV, parágrafo único, 8º–11, Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm).
- [Emenda Constitucional 72/2013, direitos domésticos](https://planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc72.htm).
- [STF Tema 1.046 — tese e trâmite, ARE1121633](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=ARE&incidente=5415427&numeroProcesso=1121633&numeroTema=1046.).
- [OIT, declaração de princípios 1998 alterada 2022](https://www.ilo.org/declaration/info/WCMS_716594/lang--en/index.htm).
- [NORMLEX/OIT — convenções fundamentais NÃO ratificadas Brasil (C87/C187)](https://normlex.ilo.org/dyn/nrmlx_en/f?p=NORMLEXPUB%3A11210%3A0%3A%3ANO%3A%3AP11210_COUNTRY_ID%3A102571), corte 14/10/2026.
- [Constituição Portugal art. 59](https://www.parlamento.pt/legislacao/paginas/constituicaorepublicaportuguesa.aspx).
- [Constituição África do Sul §23](https://www.justice.gov.za/legislation/constitution/chp02.html).

**Âmbito da validação:** textos constitucionais, parâmetros judiciais de tema específico e compromissos OIT checados em fontes primárias. *Não* certificados impactos econômicos, custos fiscais, status de cada lei vigente trabalhista nem acórdãos integrais. Dados sociais de pesquisa M05 permanecem por obter.

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** dossiê M09.02, matriz de 35 unidades art.7º, matriz de 11 funções arts.8º–11, cenários adversariais e cotejo comparado e STF Tema1046/OIT. **PENDENTE:** consolidação por leis (CLT, domésticos, previdência e plataformas), ADCT, revisão de direitos quantitativos com dados reais, transparência sindical e conceito de disponibilidade; não há CF-NOR nova ou decisão D. **PRÓXIMO:** estudo M09.03 da arquitetura constitucional de negociação coletiva, sindicatos e greve (coord. M01/M06) e M09.04 de quantidades/finanças trabalhistas com dados M05, após reservar IDs e verificar novas pesquisas.  
**Status de PR/CI:** verificar último HEAD antes de descrever conclusão; este trabalho permanece em PR63 draft até revisão jurídica e de fontes.
