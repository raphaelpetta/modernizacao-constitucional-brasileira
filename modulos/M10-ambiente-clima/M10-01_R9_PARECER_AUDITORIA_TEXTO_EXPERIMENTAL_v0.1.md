# M10.01-R9 — Parecer de auditoria de texto experimental A/B

**Sessão:** CF-M10.01-S009 · **Corte:** 14/10/2026 · **Issue:** #88 · **PR:** #89 (draft).  
**CF main baseline da rodada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **PR HEAD de entrada:** `97b2b552e357d20632982fd2cf8dd8d3c055ef38`.  
**Estado:** experimento jurídico-editorial **H de pesquisa**, não F6, não F7 canônico; nenhuma decisão D, nova CF-NOR, alteração de `redacao/`, `indice.csv`, `main` ou CLF.

**Entregas auditadas:**
1. `M10-01_R9_ESBOCO_A_NUCLEO_CONCENTRADO_v0.1.md`: **12 cláusulas fictícias A-TEXTO** e **5 reservas especiais A-RES**;
2. `M10-01_R9_ESBOCO_B_PROTECAO_DISTRIBUIDA_v0.1.md`: **14 cláusulas fictícias B-TEXTO** e **9 reservas B-RES**, situadas em blocos funcionais (direitos, procedimento, Federação, economia, Justiça, territórios e deveres);
3. `M10-01_R9_MATRIZ_TEXTO_NN.csv`: **38 registros** de direito vigente, texto A/B e ressalva, com vínculos muitos-para-muitos;
4. `M10-01_R9_TESTES_TEXTO_CONCRETO.csv`: **14 casos fictícios** aplicados diretamente às duas redações.

## 1. A natureza do contraste

As arquiteturas A e B são **dois modos hipotéticos de localizar cláusulas**, não modelos constitucionalmente aprovados e não opções submetidas a votação. O texto foi criado deliberadamente *fora* de `redacao/propostas/` e não recebeu identificador `CF-NOR-####`. A matriz associa cada fonte ao(s) trecho(s) correspondente(s), inclusive quando só há **reserva sem texto**.

Fontes primárias centrais:
- [Constituição Federal atualizada — Câmara dos Deputados, art.225](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html): direito intergeracional, §1 I–VIII, §§2–7, e interfaces CF5/23/24/30/129/145/170/186/216/231;
- [LC140/2011, arts13–17](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp140.htm): licenciamento por um ente e supletividade/não licença tácita;
- [Lei7347/1985 compilada, arts3–5](https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7347-24-julho-1985-356939-normaatualizada-pl.html): ACP preventiva, reparatória e legitimação;
- [Lei15300/2025, art4 §2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm): audiência da LAE não substitui consulta prévia quando devida;
- [EC132/2023, arts1/3/4/23](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm): faseamento da regra fiscal do art225 §1 VIII (reconhecimento específico na R8);
- [OIT169, Anexo LXXII do Decreto10088/2019](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10088.htm): consulta em seu campo de incidência.

O status das ações ADI7913/7916/7919/ADC102 permanece **V** para eventual decisão final superveniente no corte: esta rodada não localizou acesso direto primário conclusivo ao inteiro teor que permita certificação; não atribuir resultado ao simples pautamento de 12/08/2026.

## 2. Rastreabilidade e lacunas encontradas diretamente no texto

### 2.1 Direito ao ambiente, gerações e dever de proteção

- A-TEXTO-01 e B-TEXTO-01 explicitam titulares e devedores sob palavras próximas ao caput do art.225.
- A-TEXTO-02 / B-TEXTO-11 enunciam processos ecológicos, manejo, biodiversidade e fiscalização genética; a compatibilidade com conhecimento tradicional e direitos coletivos exige M11.
- **V:** a remissão a futuras gerações não demonstra automaticamente qual ação, legitimado, requisito probatório ou tutela temporal será preservada, nem autoriza concluir que obrigações climáticas quantitativas estão presentes.

### 2.2 EIA constitucional e procedimento legal

- A-TEXTO-04 e B-TEXTO-03 contêm literalmente os três elementos a verificar: **instalação** de obra/atividade, **potencial significativa degradação**, **estudo prévio** e **publicidade**.
- A-TEXTO-10 e B-TEXTO-02/04/08 abordam acesso, participação e tutela, mas permanecem abertos os legitimados e meios da ACP/ação popular. Há sobreposição textual na arquitetura B entre B-02 e B-08, sem que isto, isoladamente, determine o resultado de futura integração.
- **V:** art.40 da Lei15190/2025 disciplina audiência e prazo legal; não migrar o prazo de 45 dias como se integrasse expressamente a CF.

### 2.3 Federação: competência constitucional ≠ modalidade de licenciamento

- A-TEXTO-09 e B-TEXTO-05 enunciam dever comum e lei complementar de cooperação; os artigos atuais 23/24/30 contemplam atribuições legislativas e administrativas **não integralmente reproduzidas**.
- A-TEXTO-12 e B-TEXTO-14 delegam concretização técnica por lei, sem estabelecer procedimentos LAC/LOC/LAE como nomes constitucionais.
- **V:** nenhum dos rascunhos demonstra a cobertura integral das competências gerais, da atuação fiscalizatória de cada ente ou da interpretação da LC140 conforme STF ADI4757. Prevalência/supletividade permanecem questões M04/M07, e eventual antinomia de Leis15190/15300 é específica.

### 2.4 Reparação civil, exploração mineral e penal

- A-TEXTO-07/08 e B-TEXTO-06/07 têm comandos experimentais sobre recuperação por exploração mineral, sanções e obrigação reparatória independente. Ambos esclarecem, em termos gerais, que cada espécie de responsabilidade tem garantias próprias.
- **V:** o texto não equivale a reprodução literal de STF Temas999/1194, STJ Tema1204, legitimidade ACP, reparação integral em espécie e execução; lei penal corretiva do art.26§5 Lei15190 continua em domínio M12/CLF, sem declaração genérica de anistia.

### 2.5 Territórios tradicionais e tratados

- A-TEXTO-11 e B-TEXTO-10 remetem a direitos originários e consulta, distinguindo audiência pública e consulta específica.
- **V:** não reproduzem integralmente CF231, não definem hierarquia e âmbito de aplicação da OIT169 e dependem de pesquisa M11/M13/M06. Os gatilhos legais dos arts43–44 da L15190 para manifestação institucional não são automaticamente critérios de titularidade de direito originário.

### 2.6 Cláusulas especiais: reservas não equivalem à sua incorporação

| Função C0 | Ensaio A | Ensaio B | Situação textual |
|---|---|---|---|
| Art225 §1 VIII / EC132 fiscalidade | A-RES-01 | B-RES-02 | **Sem cláusula normativa; transição 2023/2027/2033 aberta** |
| Art225 §4 patrimônio nacional | A-RES-02 | B-RES-03 | **Sem enumeração integrada ao corpo** |
| Art225 §5 terras estaduais indisponíveis | A-RES-03 | B-RES-04 | **Sem norma dominial especial** |
| Art225 §6 localização nuclear | A-RES-04 | B-RES-06 | **Sem reserva de lei federal no texto** |
| Art225 §7 manifestação cultural animal | A-RES-05 | B-RES-05 | **Ressalva mencionada, condições ainda não transpostas** |
| CF170 VI, 186 II, 145 §3 | A-RES-01/A-TEXTO-12 remete incompletamente | B-RES-01 | **Funções econômicas/tributárias não redigidas integralmente** |
| CF5 LXXIII, 129 III, Lei7347 | A-TEXTO-10 | B-TEXTO-02/08 e B-RES-08 | **Tutela específica e legitimados não equivalidos** |

**Advertência de literalidade:** as cláusulas A-06 e B-13 trazem uma referência nominal a A-RES-05/B-RES-05; **num texto constitucional real, um anexo de pesquisa sem norma jurídica não seria uma ressalva constitucional aplicável**. Esta é uma lacuna intencionalmente marcada para deliberação, não um resultado de equivalência.

### 2.7 Clima e novas obrigações

Nenhum esboço definiu percentual de emissões, orçamento reservado, órgão climático, fundo ou prazo administrativo obrigatório; os deveres gerais ambientais e instrumentos da legislação vigente continuam fontes diferentes. A possibilidade de cláusula climática nominal permanece DM-02 **A/V**, sem decisão de introdução.

## 3. Análise dos 14 testes adversariais

Arquivo `M10-01_R9_TESTES_TEXTO_CONCRETO.csv`. Os testes incluem obra significativa sem EIA, ação popular/ACP com legitimados diferentes, fiscalização supletiva, mora no licenciamento, consulta indígena, terra tradicional não homologada, recuperação após multa, regime tributário transitório, biomas, terras estaduais, autorização nuclear, exceção animal, financiamento climático e duplicidade de tutela.

O registro de cada cenário contém: fato **fictício**, fonte C0, cláusulas exatas A/B, constatação estritamente textual, status de verificação e questão factual/probatória. Não atribui probabilidade de resultado judicial, eficácia empírica ou constitucionalidade a nenhum esboço.

## 4. Checagem técnica dos vínculos

Os quatro arquivos de redação/matriz/testes foram relidos na branch após gravação: identificaram-se `A-TEXTO-01–12`, `B-TEXTO-01–14`, **38 linhas de matriz** e **14 linhas de testes**. Todas as referências `A-TEXTO/B-TEXTO` feitas nos CSVs possuem identificador correspondente nos esboços; todos os códigos `A-RES/B-RES` citados nos CSVs constam das seções de reserva.

**O que isso não verifica:** semântica normativa, equivalência de garantias, adequação constitucional à legislação de 2025/2026, risco ecológico real, titularidade territorial e decisões políticas.

## 5. Diferenças editoriais a serem analisadas sem escolha

- **A:** enunciados ecológicos concentrados no mesmo documento; competências, Justiça e consulta são indicadas por remissões textuais dependentes de outros módulos.
- **B:** enunciados repartidos em blocos funcionais; a duplicidade de acesso judicial B-02/B-08 e as referências a economia/fiscalidade/território precisariam ser reconciliadas com o texto canônico dos módulos.
- Os marcadores em ambos **não** constituem artigos constitucionais, não permitem inferir que um texto contém todo regime atual, e não resolvem materialmente as funções em reserva.

Não há uma declaração de superioridade, suficiência, sucesso esperado ou preferência por uma das arquiteturas; a diferença aqui é apenas localização e conteúdo explicitamente presente ou ausente.

## 6. Questões necessárias antes de qualquer F6 e F7

**G2 — interfaces não concluídas:** M01/M06 (titularidade, ação popular, ACP, execução, duplicidade de tutela), M04/M07 (competências e fiscalização), M05/M14 (fiscalidade/EC132), M11/M13 (território e consulta), M03/M08 (nuclear, fauna, patrimônio), M12/CLF (regime penal). Nenhuma revisão independente foi recebida nesta R9.

**G3 — decisões materiais abertas:** conservação, reescrita ou alteração do conteúdo das cinco regras especiais; eventual cláusula climática nominal; separação de ação popular e ACP; direito de consulta e forma de participação; regras de repartição de competência.

**G4 — auditoria de equivalência:** requer cotejar texto canônico completo, IDs válidos, regras transitórias e meios reais de tutela, com prova de não regressão **norma por norma**, não apenas presença de palavras.

**G5 — integração:** exige preflight da main, reservas de ID, CI, revisão jurídica e autorização pertinente. A R9 não autoriza ingressar nessa porta.

## 7. FEITO / PENDENTE / PRÓXIMO

**FEITO:** dois ensaios de redação experimental com 26 cláusulas no total (12 A + 14 B), 5/9 reservas explícitas; matriz N:N de 38 vínculos; 14 testes; verificações de links internas; relatório de lacunas.  
**PENDENTE:** pareceres intermodulares, processos STF de licenciamento 2025, vigência fiscal aplicada, dados reais, decisões G3, solução de reservas, auditoria completa e eventual texto canônico.  
**PRÓXIMO — M10.01-R10:** **conciliação pontual dos 14 testes** e preparação de **fichas de deliberação não ratificadas** restritas a seis assuntos: (i) núcleo direito/dever; (ii) EIA/publicidade; (iii) competências/cooperação; (iv) tutela e legitimidade; (v) consulta territorial; (vi) regras especiais e transição. Para cada assunto, documentar alternativas redacionais, fonte vigente, efeitos jurídicos textuais, risco de remissão vazia, dependência necessária e melhor objeção, **sem recomendar escolha ou atribuir D**. O artefato deve permitir ao usuário deliberar em futuro turno, mantendo os textos R9 como hipóteses autônomas.

**Integridade:** nenhum arquivo de `redacao/`, `indice.csv`, `governanca/03_DECISOES`, CLF ou `main` foi modificado. PR89 continua `draft`. O CI estrutural deve ser verificado após o pacote R9 e não equivale a validação jurídica.
