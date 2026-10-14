# M10.01-R11 — Parecer de proveniência e prontidão documental das seis fichas

**ID:** CF-M10.01-S011 · **Data de corte:** 14/10/2026 · **Issue:** #88 · **PR:** #89 (draft).  
**Main inicial:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`; **PR89 HEAD inicial:** `f7380504410ec972546cbe143fe2ad7167aea643`.  
**Objeto:** verificar se a pesquisa **já existente** em outros módulos realmente responde às fichas F01–F06 da R10. **Nenhuma D nova, CF-NOR, reserva de ID ou modificação em `redacao/`, `main` ou CLF.**

## 1. Como a verificação foi realizada

Foram consultados: diretórios relevantes da `main`, lista de PRs abertos; o [PR #22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22) M01 (HEAD `f76910cb8c222d5c15a77147a50ec4c0b3362778`); o [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62) M06 (HEAD `50e4b81ac15992b4cd5f6314e1a562ccaf8652d1`); a `main` acima; issues M04 #21 e M06 #65 e comentários; além dos **reviews e comentários do PR89**, que retornaram **zero revisões formais e zero comentários de código** no momento da coleta. Os nove comentários da issue #88 eram registros de andamento da própria frente M10, **não respostas externas específicas às fichas da R10**.

**Distinção metodológica:**
- **Fonte positiva:** CF/1988, LC140, legislação e decisões conforme seus limites. Não constitui parecer editorial.
- **Cobertura documental parcial:** outro módulo examinou uma função relacionada **com fonte, arquivo e SHA demonstráveis**.
- **Resposta intermodular específica:** seria documento que confrontasse literalmente `F01–F06` ou a redação `A-TEXTO/B-TEXTO`, esclarecesse pontos normativos e explicitasse limites. **Nenhuma resposta desse tipo foi localizada no universo GitHub efetivamente consultado.**
- **Ausência na amostra:** não equivale a afirmar inexistência absoluta de qualquer discussão oral, texto externo ou arquivo não pesquisado. A ausência de diretório no caminho testado não prova que todo o conhecimento relativo ao módulo esteja ausente do projeto.

A matriz `M10-01_R11_QUADRO_RESPOSTAS_INTERMODULARES.csv` identifica **18 observações, três por ficha**, separando contribuição existente, lacuna e fonte GitHub **ancorada ao commit de leitura**.

## 2. Achados por ficha e consequência documental

### F01 — direito/dever intergeracional

- **M01/PR22, prova positiva:** o dossiê M01.09 reconhece expressamente o conteúdo setorial ambiental — prevenção, participação, responsabilidade e proteção intergeracional — que deve ser relacionado a M10. Isso é **reconhecimento transversal do assunto**, não aprovação do enunciado A-01/B-01 nem demonstração de tutela.
- **M06/PR62:** matriz F09_COLAB e F12_EXECUCAO aborda, em geral, tutela difusa/estrutural e execução. Não contém parecer voltado à legitimidade de pretensões das futuras gerações.
- **M05/main:** fontes e encargos relacionados à execução estatal em geral, sem definição de obrigação climática específica.

**Evidência ainda necessária:** sujeito titular/legitimado, dever concreto, conexão de competência/financiamento e remédio de lesão intertemporal. **Estado F01:** `PARCIAL_DOCUMENTAL + A/V`, sem resposta específica ou D.

### F02 — EIA prévio e publicidade

- **M00/main, L-02:** existe **teste adversarial sobre delegação de metodologia técnico-ambiental** à agência com elementos essenciais em lei. É uma contribuição material à separação `garantia constitucional × procedimento técnico`, mas não fixa a interpretação do art.225 §1º IV nem altera seus gatilhos.
- **M06/PR62:** aborda ação popular e tutela coletiva genérica; falta enquadramento específico da ACP ambiental e revisão do EIA A-04/B-03.
- **M07/M08:** não foi localizado dossiê especializado pertinente nos diretórios/PRs examinados.

**Lacuna exigida:** confirmação de anterioridade/publicidade para risco significativo, prova técnica, procedimento, ente licenciador e meio de controle sem transpor o prazo legal de 45 dias para a CF. **Estado F02:** `PARCIAL_DOCUMENTAL + A/V`.

### F03 — competência, licenciamento, fiscalização

- **M04/main, M04.01:** separa competência normativa, execução, cooperação, custeio e controle, mas o escopo é participação territorial/impasse legislativo, **não** distribuição operativa da licença/auto/fiscalização sob [LC140 arts.13–17](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp140.htm).
- **M05/main, M05.01:** demonstra que CF art.167 §7º já exige fonte ou transferência para encargos de prestação de serviço público impostos por lei, com exceções; isso não prova custeio específico do licenciamento ambiental nem incide automaticamente sobre todo dever ecológico anterior.
- **M07:** parecer de administração ambiental específico não localizado.

**Lacuna exigida:** mapear competência comum CF23, concorrente CF24, local CF30, supletividade de LC140 e [STF ADI4757](https://portal.stf.jus.br/processos/detalhe.asp?incidente=4224704), sem generalizar órgãos licenciadores simultâneos. **Estado F03:** `PARCIAL_DOCUMENTAL + A/V`.

### F04 — ação popular, ACP, execução

Este é o achado de precisão da R11: o **PR62 vai além de mera declaração de remédios genéricos**, embora não responda integralmente à ficha.

- [M06.02, §2.5 (PR62)](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/50e4b81ac15992b4cd5f6314e1a562ccaf8652d1/modulos/M06-justica/M06-02_DOSSIE_REMEDIOS_E_EQUIVALENCIA_v0.1.md#L42-L47) enumera ação popular ambiental, cidadão e isenção de custas e sucumbência salvo má-fé.
- [M06.02, matriz F07_POPULAR, F09_COLAB e F12_EXECUCAO](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/50e4b81ac15992b4cd5f6314e1a562ccaf8652d1/modulos/M06-justica/M06-02_MATRIZ_FUNCIONAL_REMEDIOS.csv) registra funções distintas de controle popular, tutela transindividual e cumprimento judicial. **Contribuição funcional parcial real.**
- [CF-NOR-0007 H da main](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/2a770a8136f8ca4877e865be3e3b7745a6d4b168/redacao/propostas/CF-NOR-0007.md) assegura inafastabilidade e tutela geral, **não** demonstra a continuidade das condições específicas da ação popular/ACP.
- [Lei 7.347/1985 compilada](https://www.planalto.gov.br/ccivil_03/leis/l7347compilada.htm) arts.1,3–5 é base legal da ACP; seus legitimados e procedimentos não são idênticos aos da ação popular.

**Lacuna exigida:** revisão M06 específica de `A-TEXTO-10`, `B-TEXTO-02/08`, legitimidade associativa/Defensoria/MP, urgência, prova ambiental, custas e execução. **Estado F04:** `PARCIAL_ESPECIFICA_POPULAR + PARCIAL_FUNCOES_COLETIVAS + V`, sem parecer conclusivo.

### F05 — direitos territoriais e consulta

- **M01/PR22:** encaminha direitos originários, autogoverno, consulta e legitimidade própria ao M11, **não** define hierarquia convencional nem aplicação ao licenciamento.
- **M00/main, M00.02:** registra categorias gerais de tratados e requisitos de aprovação/recepção; não é parecer sobre a Convenção 169.
- **M11/M13:** nenhum diretório específico encontrado nas localizações da main consultadas e nenhum PR aberto dedicado a esses módulos na fotografia. É **limite verificável da busca**, não afirmação global sobre todas as fontes do projeto.

**C0:** [CF art.231](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm), [Convenção OIT169, Anexo LXXII do Decreto10.088/2019](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10088.htm), [Lei15.300/2025 art.4§2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm). A lei distingue audiência pública de consulta quando aplicável.

**Lacuna exigida:** incidência por grupo/afetação, representação, oportunidade, hierarquia do tratado, efeitos processuais e relação com manifestação de órgão envolvido. Não presumir veto universal, inexistência de consulta ou que homologação define a existência do direito originário. **Estado F05:** `PARCIAL_HIERARQUIA_ABSTRATA + SEM_PARECER_ESPECIALIZADO_NA_AMOSTRA + V`.

### F06 — regimes especiais e transição

- **M00/main, ADCT:** há matriz efetiva de fases 2026/2027/2033 para o sistema IBS/CBS. O conteúdo **não examina** a literalidade do art.225 §1º VIII.
- **M05/main:** identifica transição EC132, encargo fiscal e faseamento em âmbito geral, **sem parecer específico** sobre biocombustíveis/hidrogênio e a LC214 art.175.
- **M03/M04:** pesquisas institucionais possuem outros objetos. Nenhum parecer setorial M08/M11/M14 foi localizado no preflight.

A [EC132/2023, art.23](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm) distingue o momento de vigência do **art.3º (2027)** e **art.4º (2033)**; o regime do art.225 §1º VIII tem sucessão textual que foi inventariada especificamente pela R8. Isso continua **dado jurídico documental**, não parecer fiscal aplicado nem decisão sobre a futura redação.

A planilha `M10-01_R11_AUDITORIA_RESERVAS_ESPECIAIS.csv` separa **seis grupos de funções** (regime fiscal; biomas patrimônios nacionais; terras estaduais indisponíveis; localização nuclear por lei federal; fauna/proteção animal e ressalva cultural; interfaces economia/cultura/povos). **A-RES/B-RES da R9 NÃO são cláusulas normativas.** Sem transposição textual ou deliberação, a continuidade funcional permanece sem certificação.

**Estado F06:** `PARCIAL_MAPA_TEMPORAL + PARCIAL_FISCAL_GERAL + SEM_REVISAO_SETORIAL_NA_AMOSTRA + V`.

## 3. Síntese da prontidão sem pontuações

| Ficha | Contribuição existente que é possível citar | Resposta específica revisando a ficha/textos R9 | Estado documental |
|---|---|---|---|
| F01 | M01 transversal e M06 coletiva geral | Não localizada | A/V |
| F02 | M00 teste de delegação e M06 popular geral | Não localizada | A/V |
| F03 | M04 competências em geral; M05 fonte de encargos | Não localizada | A/V |
| F04 | M06 ação popular ambiental + tutela coletiva e execução | Não localizada | A/V |
| F05 | M01 identificação de direito originário/consulta; M00 tratados abstratos | Não localizada | A/V |
| F06 | M00 ADCT e M05 fiscalidade geral | Não localizada | A/V |

**Nota sobre 'não localizada':** esta matriz não constitui nota de avaliação do mérito ou índice comparativo de desempenho institucional. É apenas verificação sobre documentos/PRs abertos e linhas efetivamente lidas. Ausência de resposta específica **não** autoriza apagar a garantia vigente nem antecipar decisão material F6.

## 4. Portas G0–G5 e atos de continuidade

- **G0:** preflight `main`, PR/issue, commits fixados e arquivos existentes: realizado na abertura.
- **G1:** normas primárias e alguns estudos cruzados: identificados; decisão de mérito superveniente nas ADIs7913/7916/7919 e ADC102 não foi certificada por inteiro teor acessível nesta verificação; notícia de pauta não é decisão.
- **G2:** existência de parecer literal das fichas F01–F06 pelos módulos destinatários: **não encontrada nesta amostra**; todos os registros A/V continuam abertos.
- **G3:** não há aprovação constitucional específica; CF-DEC-004 D(guia) não ratifica A/B ou F01–F06.
- **G4:** A/B são texto **experimental** e contêm reservas sem efeito normativo; nenhuma auditoria final contra `CF-NOR` M10 candidata.
- **G5:** PR89 permanece draft; CI estrutural não substitui revisão jurídica/decisão.

**FEITO:** 18 fontes/vínculos documentais por SHA, seis grupos de reserva auditados, precisão da contribuição do PR62, busca de comentários/reviews efetivos.  
**PENDENTE:** validações específicas M01/M04/M05/M06/M07/M08/M11/M13/M14, decisão de conteúdo, vigência judicial verificável, regras transitórias e equivalência contra redação futura.  
**PRÓXIMO — M10.01-R12:** **encaminhar perguntas técnicas curtas e delimitadas aos canais de coordenação existentes**, sem duplicar questões/subciclos ou criar normas; por exemplo, solicitar a M06 uma colação F04 versus ACP/ação popular, a M04 uma resposta F03 por operação e a M05 exame do art.225 §1º VIII por redação temporal. Onde não houver frente iniciada, registrar a dependência junto à coordenação, sem atribuir anuência. Não criar uma nova série de matrizes sem nova evidência.

**Integridade:** nenhuma alteração `redacao/`, `indice.csv`, CLF, `governanca/03_DECISOES` ou main. PR89 aberto em draft.
