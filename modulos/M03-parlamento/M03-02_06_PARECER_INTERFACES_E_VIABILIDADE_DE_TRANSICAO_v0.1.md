# M03.02.06 — Parecer de interfaces e viabilidade institucional de transição
**ID:** CF-M03.02-EST-006 · **Data:** 14/10/2026 · **Issue:** #84 · **PR:** #85 (draft) · **main preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **Proprietário:** M03 · **F0–F5/F8 pesquisa; F6 não deliberado, F7 não iniciado.**
**Regra:** parecer analítico emitido pelo M03 **sobre** documentação existente de M02/M04/M05/M06/M14; **NÃO é parecer formal emitido pelas respectivas frentes**. Nenhum código CF-NOR ou decisão CF-DEC é criado/alterado. Não importar a arquitetura do projeto Brasil alternativo.

## 1. O que ficou conhecido — fontes, limites e proveniência
**Preflight GitHub em 14/10/2026:**
- M02 e M14 **não têm pasta de dossiês integrada em `modulos/` na main lida**. M02.01 tem issue #14 e pesquisa preliminar no M00.01/04A; M14 depende de inventário temporal ADCT do M00.02. Não é legítimo chamar isso de revisão material completa de M02/M14.
- M05.01 e M05.02 **estão na main**, com proteção contra encargos sem custeio (CF/1988 art. 167 §7º) e pesquisa sobre distribuição municipal, mas **sem parecer específico sobre continuidade do orçamento nacional e funcionamento do governo cessante**. M05.02 registra dez fontes oficiais catalogadas, não dados municipais brutos harmonizados nem valores estimados de custo de reforma.
- M04.01 está na main; distingue representação territorial, competência material, execução, financiamento e mediação. NÃO decidiu composição/veto do futuro Senado/Conselho.
- M06.01–02 estão no **PR draft #62**, branch `pesquisa/m06-01-remedios-tutela-v01`, HEAD observado `50e4b81ac15992b4cd5f6314e1a562ccaf8652d1`. A pesquisa de acesso à Justiça e remédios (HC, MS, MI, HD, popular) **não** é parecer sobre impasse de confiança, nomeação ou dissolução; oferece critérios de tutela efetiva, urgência, autoridade coatora, prova e controle. Não ratificou Tribunal Constitucional apartado.
- A pesquisa M03.02 R01–R05 está somente neste **PR #85**, não na main; nenhuma escolha A/B/C é D. Os cenários de 100 cadeiras são artificiais, não previsão causal brasileira.
- A CF vigente e plebiscito 1993 devem ser analisados por suas fontes primárias, sem usar a constituição projetada como pressuposto do direito positivo.

Fontes versionadas:
* M00.01/04A: `modulos/M00-fundamentos/M00-01_04A_SALVAGUARDAS_ELEITORAIS.md` (main).
* M00.02/ADCT: `modulos/M00-fundamentos/M00-02_ADCT_MATRIZ_TEMPORAL_v0.2.csv` (main, 18 itens focalizados, NÃO exaustivos).
* M04.01: `modulos/M04-federacao/M04-01_CONSENTIMENTO_TERRITORIAL_E_IMPASSES_v0.1.md` (main).
* M05.01/02: `modulos/M05-financas/M05-01_ENCARGOS_FINANCIAMENTO_EQUALIZACAO_v0.1.md` e `M05-02_PROTOCOLO_EMPIRICO_E_AUDITORIA_v0.1.md` (main).
* M06 PR62: `modulos/M06-justica/M06-01_ACESSO_JUSTICA_E_REMEDIOS_v0.1.md` e `M06-02_DOSSIE_REMEDIOS_E_EQUIVALENCIA_v0.1.md` (PR62, não main).
* M03.02 R05: `M03-02_05_PARECER_COMPARATIVO_TRES_ARQUITETURAS_v0.1.md` (PR85, não main).

## 2. Interface M02: eleições, maioria governamental e risco de autobenefício
**Direito vigente verificável:** CF/1988 art.16 estabelece anterioridade de **aplicação** ao pleito para lei que altera processo eleitoral, não mera postergação de vigência; ADI 3.685 e RE 633.703 confirmam força da integridade competitiva em hipóteses específicas. Comissão de Veneza, Code of Good Practice 2025, sugere estabilidade de elementos fundamentais; não é norma vinculante brasileira. Fonte M00.01/04A e https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm .

**Desafio próprio de B e C:** eleições antecipadas podem ser convocadas com antecedência muito inferior ao prazo fixo de anterioridade, enquanto incumbentes poderiam alterar fórmula, circunscrições, propaganda, aliança e elegibilidade antes de dissolver. Não basta reproduzir “um ano” sem definir **qual regime eleitoral vale** em pleitos extraordinários. Hipóteses:
- **E-P1** aplicar em toda eleição antecipada as regras gerais vigentes na última eleição parlamentar, salvo correção exigida constitucional/judicialmente; evita mutação oportunista, mas pode congelar arranjo inadequado por mais tempo.
- **E-P2** mudanças ordinárias sujeitas a prazo de anterioridade e cláusula específica de **não aplicação ao primeiro pleito pós-dissolução** se votadas sob legislatura que se beneficia; exige disciplinar legislatura de referência e possíveis correções inadiáveis.
- **E-P3** órgão eleitoral com poderes técnicos de execução sem alterar matéria reservada à lei nem reescrever elementos essenciais; controle urgente de equidade e publicidade.

**M02 A (presidencialismo):** eleições presidenciais e parlamentares são institutos distintos, mandatos não se interrompem por simples derrota fiscal. Preservar isonomia, alternância, regras de impeachment separadas e fiscalização parlamentar.
**M02 B:** Câmara recebe voto de confiança; definir simultaneidade ou dissociação eleições legislativas, prazos, limites à dissolução e acesso de oposição à agenda, sem presumir lista partidária fechada/600 deputados.
**M02 C:** além do Parlamento, há presidente de eleição popular que pode alegar mandato próprio contra gabinete parlamentar; estudar eleições não coincidentes e coabitação. Nenhum arranjo eleitoral ratificado.

**Conclusão de interface:** é possível escolher B como objeto de estudo P; ainda NÃO está liberado fixar dissolução, data de pleito ou conteúdo de uma norma CF-NOR sem parecer específico M02.

## 3. Interface M05 + M04: orçamento e federalismo — continuidade não equivale a cheque em branco
**Fato jurídico importante, já estudado em M05.01:** EC 128/2022 incluiu **CF art.167 §7º**, vedando que lei imponha/transfira encargos financeiros de serviço público a ente federativo sem fonte orçamentária/financeira ou repasse dos recursos correspondentes, com exceções expressas. Isso NÃO significa suficiência, disponibilidade e previsibilidade plurianual efetivas. ADCT art.113 demanda estimativa financeira para hipóteses legais, não financiamento real garantido. Não alegar inexistência de proteção federal hoje.
Fontes: https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc128.htm ; https://www4.planalto.gov.br/legislacao/legis-federal/constituicao .

**Problema NÃO tratado nas entregas M05:** ausência de orçamento anual federal aprovado. Alemanha GG art.111 admite despesas provisórias taxativas e regras próprias de crédito; Espanha CE art.134(4) prorroga orçamento anterior, solução distinta. Ambas preservam direitos e obrigações mas não permitem concluir que uma simples cópia funcionaria sob a distribuição brasileira de competências, obrigações plurianuais, vinculações, emendas, precatórios, dívida e receitas. A autonomia estadual/municipal e o poder do Senado/Conselho no projeto exigem estudo M04 conjunto.

**Teste único FISC-01:** no ano de transição de A para B ou C, orçamento nacional foi proposto por titular executivo antigo, a nova Câmara não aprovou proposta do premier, e lei nova estabelece encargo sobre municípios. Deve ser possível identificar **separadamente**: competência para propor orçamento; órgão que vota; despesas juridicamente autorizadas durante o impasse; receita que continua arrecadável; despesas vinculadas/direitos exigíveis; proibição de obrigação municipal sem custeio; quem fiscaliza; quais poderes não podem ser inventados por ato executivo. Nenhuma maioria orçamentária é presumida.

**Três variantes normativas H:**
- **FISC-A** execução provisória de obrigações legais/serviços essenciais definidos e rubricas iniciadas, limites quantitativos e regras de financiamento expressos (contrafactual alemão), mais auditoria periódica.
- **FISC-B** prorrogação limitada do orçamento anterior, com exclusão de programas expirados, atualização conforme regra previamente votada e possibilidade de correções parlamentares (contrafactual espanhol).
- **FISC-C** híbrido temporal: janela curtíssima de prorrogação e, sem acordo, regime provisório taxativo; requer teste de incentivos e risco de contingenciamento inconstitucional. Não pressupor prazos ou indexadores arbitrários.

**Parecer M03 sobre M05, NÃO chancela M05:** R1 conciliação transparente + R4 continuidade fiscal limitada são necessários independentemente de A/B/C; nenhuma dessas regras gera uma maioria. M05 ainda deve especificar autorizador de dívida/crédito, controles judiciais e administrativos, encargos compartilhados, prorrogação repetida e fontes de financiamento. M04 deve decidir quais matérias exigem consentimento do órgão territorial sem dar à segunda Câmara competência implícita para censurar gabinete.

## 4. Interface M06: remédios e controle da investidura/dissolução
M06 PR62 pesquisa efetividade de tutela, urgência, prova, competência, custos e acesso à Justiça. **NÃO** define qual será a futura Corte Constitucional nem a via adequada para controlar nomeação ministerial, dissolução, emergência e fraude parlamentar. M03 propõe objeto de parecer específico, sem fingir que M06 o emitiu:

1. **NOMEAÇÃO:** após investidura validamente certificada (confrontar falsificação de ata), a chefia de Estado deve exercer ato juridicamente vinculado? **G3A** tutela judicial de omissão ou **G3B** efeito supletivo ex constitutione após prazo — duas hipóteses H. Tribunal examinaria quórum, competência, autenticidade e prazo, NÃO programa partidário.
2. **DISSOLUÇÃO:** não bastam motivações políticas alegadas; identificar hipóteses taxativas (falha de formação; confiança derrotada com janela para sucessor) e restrições durante censura. Controle pode incidir em vício de competência/procedimento/finalidade de forma limitada sem juiz arbitrar orçamento.
3. **RESPONSABILIDADE:** impeachment por infração constitucional grave não deve servir de censura parlamentar comum; ao mesmo tempo, a reforma não pode blindar atos ilícitos de presidente, premier ou maioria.
4. **REVISÃO EFETIVA:** urgência, legitimidade institucional da Câmara/minoria, publicidade, acesso a provas, execução e proteção contra instrumentalização estratégica do próprio contencioso. Poder judiciário não pode escolher gabinete mediante mérito de programa; coibiria fraude documental/competencial.
5. **SEGUNDA CHEFIA C:** presidente popularmente eleito não pode demitir gabinete por discordância, sob pena de migrar para subtipo de dupla responsabilidade; controle precisa ser congruente com M06 e M12.

Não emitir "parecer favorável M06": há apenas **questões recebidas** pelo M03 a encaminhar para essa frente. Fonte jurídica comparativa para controle estrito: BVerfG 25/08/2005, 2 BvE 4/05 e 7/05, julgou controle finalístico limitado da dissolução por confiança, sem transformar juízes em árbitros da boa-fé política. https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/2005/08/es20050825_2bve000405en.html .

## 5. Interface M14: transição, legitimidade e plebiscito histórico
**Fato brasileiro confirmado:** ADCT art.2º instituiu **plebiscito específico** sobre forma e sistema de governo; EC 2/1992 antecipou-o para **21/04/1993**, e Lei 8.624/1993 disciplinou-o. O resultado preservou República/presidencialismo. Esse ato NÃO estabelece por seu próprio texto dever permanente de nova consulta para toda proposta futura. Tampouco significa que uma reforma contemporânea tenha automaticamente legitimidade constitucional sem exame da CF art.60 e seus limites. Fontes: https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=2&abrirBase=AD ; https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc02.htm ; https://www.tse.jus.br/comunicacao/noticias/2013/Abril/plebiscito-sobre-forma-e-sistema-de-governo-completa-20-anos ; https://www4.planalto.gov.br/legislacao/legis-federal/constituicao .

**Cautela jurídica obrigatória:** CF/1988 art.60 §4 protege, entre outros, sufrágio direto, secreto, universal e periódico e separação dos Poderes. O presidencialismo não está nominalmente no rol do §4; disso **não** se segue aprovação automática de qualquer desenho parlamentar, porque a análise de tendência à abolição de garantias e separação substancial, legitimidade da alteração e regime de direitos é específica. A ADI 829 reconheceu sujeição de emenda constitucional a controle por cláusulas pétreas (contexto EC 2/1992). Não tratar eventual plebiscito futuro como juridicamente obrigatório ou proibido **sem parecer próprio**. Não confundir Constituição inteiramente nova por poder constituinte originário com uma EC submetida ao art.60 da Constituição atual.

**Quatro marcos temporais condicionais, sem data real definida:**
- **T0 norma aprovadora:** promulgação/entrada em vigor de regras permanentes e transitoriedade especial; preservar art.16 CF vigente para matéria eleitoral enquanto incidir; examinar quais procedimentos e legitimidades originam a reforma.
- **T1 governo anterior:** até marco constitucional prospectivo, presidente e ministros exercem competências e mantêm responsabilidades sob regras vigentes; não declarar cessação antecipada sem regra expressa e análise de mandatos/direitos.
- **T2 eleição parlamentar inaugural:** definir qual câmara eleita sob quais regras e data receberá poderes de investidura, qual lei eleitoral será aplicável, quem nomeia/interinamente preside e se haverá eleição presidencial separada (C) ou chefe Estado não executivo (B).
- **T3 posse de novo gabinete/chefia de Estado:** atribuição de competências e de cadeias de comando desde hora certa, sem vazio administrativo ou presidências concorrentes; continuidade de obrigações, contratos, orçamento e direitos, fiscalização de nomeação e prevenção de rejeição indevida.

**A (presidencialismo reformado):** transição comparativamente menos estrutural, mas alterações de mandatos, competências, orçamento e urgência não são automaticamente neutras. **B (parlamentarismo):** desdobramento Estado/Governo, primeira investidura, gabinete cessante, chefia de Estado e eleição precisam norma transitória própria. **C (premier-presidencial):** além de B, sincronização de duas eleições e duas legitimidades e delimitação do comando civil, com transição potencialmente mais complexa.

**Não feito:** linha do tempo jurídica de mandatos concretos, aprovação de consulta popular, regra de eleição de chefe de Estado e avaliação de compatibilidade da reforma proposta com cláusulas pétreas. M14 continua necessitando frente própria.

## 6. Conclusão de interface — quais escolhas se podem levar a debate agora?
- **Porta F6-00, DELIBERÁVEL COMO ORIENTAÇÃO DE PESQUISA P:** após cinco rodadas, pode-se submeter A presidencial reformado, B parlamentar racionalizado e C premier-presidencial para escolher **um protótipo provisório**. Isto não é ratificação constitucional definitiva. O mesmo formulário/ata deve permitir "continuar comparação sem preferência".
- **F6 material definitiva ainda bloqueada:** ausência de pareceres específicos de M02 (regras eleitorais/pleito extraordinário), M05/M04 (orçamento/financiamento), M06 (sucessão, controles), M12 (chefias militares), M14 (transição/mandatos) e análise empírica atual. A documentação de M06 PR62 não substitui revisão institucional M06 desta questão.
- **Preferência de pesquisa do M03 permanece B**, sem atribuir maior sobrevivência democrática, eficácia legislativa ou proteção de direitos por mera adoção nominal de parlamentarismo. A e C devem permanecer competitivas com objeções e vantagens concretas.
- **Problema incontornável:** gabinete B2 com minoria tolerada e protegido por censura construtiva pode permanecer sem orçamento; R1/R4 evitam danos e bloqueio artificial de serviços, mas não criam apoio político. R2/R3 dão risco de chantagem eleitoral.
- **Nenhuma aprovação de quórum, datas, composição, chefe de Estado, normas CF-NOR ou reforma do CLF.** O nível de certeza obtido é jurídico-comparativo para pautar decisão, não prova causal do melhor regime.

## 7. Pedido de interface operacional para próxima rodada (F6-00)
**M02:** 2 páginas: elegibilidade, estabilidade de regras em eleições extraordinárias, quem certifica investidura e direito da oposição nos três pacotes.
**M05/M04:** tabela quem propõe/vota/executa orçamento sem aprovação, despesas/taxação/dívida admissíveis, encargos territoriais e limites de veto em A/B/C.
**M06:** ato de nomeação G3A/G3B, competência para tutela urgente, controle restrito de dissolução e separação de responsabilidade jurídica e confiança.
**M12:** única autoridade de comando militar, segurança e emergência nos modelos B/C, com prevenção de ordens concorrentes.
**M14:** sequência T0–T3 com direitos adquiridos, mandatos e regras de eleições inaugurais; avaliação art.60/ADI829/plebiscito histórico; não produzir afirmação peremptória sobre consulta obrigatória.
**Entregável integrado:** nota curta de decisão P sobre protótipo A/B/C, mantendo ressalvas F6 e sem transformação automática em decisão D.