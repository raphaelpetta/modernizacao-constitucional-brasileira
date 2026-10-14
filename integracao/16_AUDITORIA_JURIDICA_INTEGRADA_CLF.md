# CF-IC-001 — Recepção do CLF ciclo 20: equivalência jurídica e unidade normativa real

**ID:** CF-INT-016 · **Corte:** 14/10/2026 · **Situação:** PESQUISA; sem dispositivo constitucional nem codificação homologada.  
**Origem:** [CLF PR #36](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/36), integrado ao `main` no commit `16fba172c875c7a0de388288fe70005c944021d6`.  
**Módulos destinatários:** M00.02 — fontes e reservas; M01 — direitos procedimentais, igualdade e proteção de dados; M03 — procedimento legislativo, veto e codificação; M04 — federação e repartição de competências; M06 — controle judicial e devido processo; M07 — administração, serviços e segurança jurídica; M14 — transição normativa.  
**Fontes:** [Lei 9.784/1999](https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html), [LC95/1998](https://www2.camara.leg.br/legin/fed/leicom/1998/leicomplementar-95-26-fevereiro-1998-363948-normaatualizada-pl.html), [LINDB/Lei13.655/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13655.htm), [Lei14.129/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14129.htm).

## 1. Feito no CLF e limite de confirmação

O CLF concluiu o **primeiro ciclo de auditoria jurídico-semântica**, posterior ao espelho textual de 215 unidades da Lei 9.784/1999. Entregas:

- `MATRIZ_TRIAGEM_215_UNIDADES_CICLO20.csv`: **215 unidades** rastreadas até os seis CSVs originais, com sinais **automáticos** de risco, destinos de título dentro de **um Livro único** e estado `Q` para todas.
- `CONTRAPROVAS_SEMANTICAS_CICLO20.csv`: **32 transformações hipotéticas** examinadas quanto a riscos de alteração de âmbito, garantias, competência, prazos, vetos, revogação e direito especial.
- `MATRIZ_INTERFACES_EXTERIORES_CICLO20.csv`: **15 interfaces** com legislação e jurisprudência exteriores à Lei 9.784 (LINDB, governo digital, LAI, LGPD, prescrição punitiva, licitação, usuário de serviços públicos, STJ 633 e regimes especiais), com vigência e inclusão **pendentes**.
- `ARQUITETURA_E_MINUTA_DEMONSTRATIVA_CICLO20.md`: **14 artigos experimentais** ilustrativos, distribuídos por **seis títulos de um só Livro**. É proposta incompleta de técnica, **não transposição de todas as 215 regras**, nem promulgação.
- `DOSSIE_20_AUDITORIA_SEMANTICA_INICIAL.md`: metodologia C0-T/C0-J/C1/M/Q e requisitos para cada certificado.

**Resultado normativo:** **ZERO** das 215 unidades recebeu comprovação jurídico-funcional `C0-J`. As 14 cláusulas resumidas são **Q**, não artigos homologados. O verificador compara as 215 linhas com seus arquivos de origem, **não** com todas as publicações históricas do DOU nem com o sentido jurídico aplicado em cada setor.

## 2. Questões concretas para o projeto constitucional

### M00/M03/M04: delimitar Livro processual sem universalizar competência

**Lei 9.784, arts. 1º e 69:** `Esta Lei` remete ao diploma do processo administrativo federal. A transformação `este Código` num CLF de 48 títulos **mudaria o referente** e poderia estender subsidiariedade a todo um Código amplo. A alternativa sob estudo é **Livro único tematicamente delimitado**, com aplicação aos Poderes da União **em funções administrativas**, sem converter orientação jurisprudencial (STJ Súmula 633) em competência nacional obrigatória sobre estados e municípios.

**Conseqüência constitucional:** M04 deve decidir competências normativas nacionais versus federais próprias explicitamente, e M03/M00 devem assegurar que a espécie normativa do Código não ultrapasse iniciativa, reserva material, veto e a disciplina autêntica da revogação. **DEC-016 permanece PENDENTE**, não se resolveu apenas por numerar artigos em novo Livro.

### M01/M06/M07: norma geral não suprime garantias específicas

A integração tem de conciliar:
- art. 2º X com art. 38 §2º (prova admissível e recusa fundamentada);
- art. 26 com art. 41 (intimação geral e intimação específica de prova, antecedência);
- art. 31 §2º com art. 9º (resposta à consulta sem legitimidade processual automática);
- art. 42 §§1º/2º (consequências opostas de atraso de parecer obrigatório **vinculante/não vinculante**);
- art. 49-A §6º (exclusões de licitações, processos sancionadores e autoridades de Poderes distintos);
- art. 64 e art. 65 (possível agravamento em recurso com defesa **versus** vedação em revisão sancionatória);
- art. 66 §2º (contagem de prazos em **dias contínuos** e exceções).

**Conseqüência constitucional:** preservar o núcleo de direitos de audiência, prova, revisão e segurança jurídica sem transferir números e ritos específicos para texto constitucional por mera reprodução da legislação ordinária.

### M01/M07/M14: LINDB, governo digital e efeitos temporais

**LINDB**, arts. 20–30 (alteração de 2018), disciplina consequências de decisões públicas, transição da interpretação, compromissos, orientação e motivação. **Lei 14.129/2021** disciplina processo eletrônico e modalidades de intimação digital. **Lei 9.784 arts. 22, 26 e 50** não exaurem o regime hoje aplicável.

A futura Constituição poderá oferecer princípios de segurança jurídica, transparência, acessibilidade, devido processo, não discriminação digital e proteção de dados, mas deve reservar ao legislador a articulação dos meios de comunicação, as exceções e os efeitos de atos normativos externos. O projeto de codificação precisará decidir **quais dessas normas serão incorporadas**, quais permanecerão fora por competência/objeto, e em que condições.

**Art. 70 da Lei 9.784:** a vigência histórica de 1999 não pode definir entrada em vigor do CLF. Art. 49-C vetado e demais vetos históricos não podem ser recriados por edição documental. A LC 95, art. 13 §1º, exige preservação do alcance e continuidade normativa na consolidação fiel.

## 3. Encaminhamentos para as frentes autônomas

1. **M00.02/M03:** avaliar competência, espécie, sanção/veto, revogação condicionada e autenticidade do Livro dentro do Código juridicamente uno, preservando `DEC-001` e mantendo `DEC-016` pendente.
2. **M01/M06:** usar as 32 contraprovas como testes das futuras normas constitucionais sobre devido processo, justiça administrativa, contraditório e decisão motivada, sem aprovar automaticamente nenhuma redação.
3. **M04:** estudar especificamente normas administrativas **federais** versus eventuais garantias nacionais, respeitando autonomia dos entes e limites da súmula STJ 633.
4. **M07:** avaliar a sistemática de processo eletrônico e direito à administração digital, oitiva e direitos dos usuários, sem fundir competências e regimes setoriais por edição.
5. **M14:** exigir protocolo de sucessão de textos, preservação de processos e prazos em curso, versões históricas, vigência, cláusulas de revogação e efeitos de eventual derrubada de veto.

## 4. Registro de coordenação

**FEITO:** recebidos no projeto constitucional o [PR CLF #36](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/36) e suas matrizes/arquitetura, sem pressupor aprovação de direitos, processo ou mecanismo de Código.

**PENDENTE:** demonstração C0-J de qualquer unidade; direitos e leis especiais; constitucionalidade da espécie do Código; pesquisa detalhada de cada interface; redação completa do Livro, cotejo histórico e situação intertemporal.

**PRÓXIMO:** CLF deve aprofundar **arts. 1º–3º/69 + LINDB** e **arts. 22–28/41 + Lei 14.129/2021**, submetendo sucessivamente conclusões de direito vigente e eventuais propostas de reforma material. CF-IC-001 permanece PESQUISA, sem deliberação constituinte.

**Objetivo preservado:** o Código não será apenas um arquivo de leis dispersas; deverá ser juridicamente único e integrado, na espécie competente que vier a ser validamente escolhida.
