# M06 — Parecer de interface sobre CF-NOR-0030 e 0031 (PR #59)

**ID:** CF-M06-PAR-001 · **Data:** 14/10/2026 · **Natureza:** parecer jurídico de pesquisa, **não** decisão ratificada D, nem aprovação, rejeição ou alteração da minuta.  
**Versões:** main CF `50b498885e17fa1709e66b0861f40e5387b4f4b0`; PR de redação [#59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59), head `62161a6b9eb7dc62aad6efe4c914b1bd85fee411` (H/draft); [PR #62 M06.01–02](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62). Examino **textos literais do PR59**, não um anteprojeto supostamente aprovado.  
**Destino:** [issue M01.13 #57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57); interfaces M01/M06/M07/M08/M12/M13 e CLF T07.M03.

## Conclusão executiva

**Parecer: FAVORÁVEL À CONTINUIDADE DE PESQUISA; DESFAVORÁVEL A CONSIDERAR O TEXTO MATERIALMENTE COMPLETO OU EQUIVALENTE À CF/1988.** A manutenção do PR59 em H/draft é apropriada até que normas especiais e remédios sejam assegurados por seu próprio texto ou por fichas autônomas coordenadas. **Não** é necessário repetir todos os ritos da LGPD no nível constitucional.

**Risco alto para CF-NOR-0030:** a segunda frase reconhece a inviolabilidade do domicílio e o sigilo de comunicações, mas diz que ingresso/interceptação dependem das "hipóteses e garantias específicas desta Constituição", **ainda não redigidas** no piloto, e menciona "autorização judicial prévia quando constitucionalmente exigida". Se o catálogo for encerrado assim, uma remissão sem objeto deixará restrições de domicílio/interceptação sem patamar de proteção demonstrado.  
**Risco alto para CF-NOR-0031:** "acesso, correção e contestação" são protegidos em termos genéricos, mas falta comprovar via gratuita e tempestiva com função equivalente ao habeas data do art. 5º LXXII/LXXVII, enquanto dados processados por particulares demandam outro regime, não extensão indiscriminada de HD a toda empresa.

## 1. Colação literal × proteção atualmente existente

### CF-NOR-0030 — privacidade, domicílio e comunicações
- **Caput (intimidade, vida privada, honra/imagem):** adição material substantiva coerente com CF/1988 art. 5º X, inclusive esfera digital. **Questões:** deveres preventivos, indenização, imprensa, dados de terceiros, necessidade de vigilância estatal; não criar silêncio sobre reparação não patrimonial.
- **§2 (domicílio):** art. 5º XI da CF/1988 atualmente excepciona inviolabilidade em **flagrante delito, desastre, socorro** ou **determinação judicial durante o dia**. Não é tecnicamente correto inferir que toda entrada demande ordem judicial, mas tampouco permitir ingresso meramente baseado em finalidade genérica de segurança. A relação com ingresso consentido, residência, busca remota e dispositivos conectados requer regras adicionais.
- **§2 (comunicações):** art. 5º XII tem proteção própria e delimita interceptação telefônica por ordem judicial em hipóteses e forma legal para investigação criminal/instrução processual penal. A jurisprudência diferencia interceptação **em fluxo**, acesso a **dados armazenados**, metadados e demais informações. **Não** transpor automaticamente o regime de telefonia de 1988 a todas as categorias digitais sem pesquisa; porém também não transferir todos os limites à discricionariedade regulamentar.
- **§3 (tutela e reparação):** protege genericamente, mas depende de M06 para efetividade de ordens urgentes, prova ilegítima (art. 5º LVI), acesso coletivo e fiscalização de agentes de inteligência. Interface M12 e M07.

**Recomendação de técnica:** manter `0030` como **direito substantivo autônomo H**; abrir dependência **A/E separada** para *reservas especiais de intrusão estatal* ou texto especial no próprio catálogo, desde que não haja duplicação. A expressão "hipóteses específicas desta Constituição" deve ter alvo identificável ANTES de concluir equivalência. **Não propor redação definitiva aqui.**

### CF-NOR-0031 — proteção de dados e decisões automatizadas
- **§1:** direito autônomo de proteção de dados cobre operações digitais e não digitais e inferências, compatível em finalidade com CF art. 5º LXXIX (EC 115/2022), sem sugerir propriedade absoluta sobre todos os dados ou veto irrestrito a políticas públicas.
- **§2:** "fundamento jurídico legítimo" requer **tipicidade e densidade legal de bases/finalidades**, minimização, segurança, transparência e controles. Na LGPD vigente, consentimento **não é a única base** legítima. "Contestação de decisões" representa proteção relevante; **art. 20 LGPD garante direito de solicitar revisão de decisões unicamente automatizadas que afetem interesses, mas não estatui, no texto atual, direito generalizado a revisão por pessoa natural** (referência histórica riscada no texto oficial). Qualquer garantia constitucional de revisão humana, quando escolhida, será proposta inovadora consciente, sujeita a avaliação de efeitos e tutela.
- **§3:** "fiscalização efetiva por autoridade independente" é hipótese constitucional de **organização institucional**, distinta do núcleo de direito; requer interface M07, competência federativa M04 e M05 orçamento. "Independente" sem autonomia decisória, meios, prestação de contas e controles pode virar garantia nominal. Avaliar autoridade própria versus rede de controles com entidade central independente, sem afirmar que cada setor precisa agência separada.
- **Bases públicas/segurança:** LGPD art. 4º afasta sua aplicação ordinária para certos tratamentos exclusivos de segurança pública, defesa nacional, segurança do Estado e investigação/repressão penal; **isso não afasta o direito constitucional** nem as exigências de legalidade, necessidade, proporcionalidade, proteção contra arbitrariedade e mecanismos de controle. A solução especial exige M12/M07.
- **Compartilhamento estatal:** STF ADI 6.387 (MP 954/2020) e ADI 6.649/ADPF 695 (compartilhamento federal) são fontes relevantes sobre finalidade, transparência, base legal e segurança; **não se resumem à proibição total de compartilhar dados** para políticas legítimas. Examinar acórdãos integrais antes de normatizar bases.

## 2. Habeas data: as salvaguardas que não podem desaparecer

CF art. 5º **LXXII**: conhecimento de informações pessoais em registros governamentais/de caráter público e retificação; art. 5º **LXXVII**: gratuidade do habeas data. **Lei 9.507/1997 art. 7º** acrescenta anotação de contestação/explicação nos pressupostos legais; art. 8º parágrafo único demanda evidência de recusa ou decurso do prazo **de dez dias** no caso de acesso e **quinze dias** para retificação/anotação, hipóteses distintas. Esses são **prazos e filtros de lei**, não necessariamente quantitativos a congelar na CF futura.

**Teste de equivalência:** garantias futuras devem responder, para cada pessoa:
(a) como sabe quais informações o Estado mantém; (b) como pede correção e anotação; (c) qual é o custo e duração prática; (d) se pode obter tutela urgente sem esperar todo contencioso administrativo; (e) quem tem legitimidade e como acessar com deficiência/baixo letramento digital; (f) como executar a ordem; (g) como conciliar sigilo legítimo de terceiros e supervisão. **Não confundir provocação administrativa específica para HD com exaurimento recursal universal para acesso à Justiça.**

**Proposta funcional P (não texto final):** assegurar constitucionalmente **acesso e correção efetivos e gratuitos** de dados pessoais em bancos governamentais/de caráter público, com via judicial tempestiva e admissibilidade legal razoável; regime ampliado de proteção de dados por legislação e tutela adequada a controladores privados. Há alternativa legítima de remédio único mais abrangente, mas somente depois de demonstrar custo, urgência, prova e execução equivalente.

## 3. O que o M06 recomenda que o PR59 faça antes de eventual merge

| Controle | Gatilho | Exigência de saída |
|---|---|---|
| **C1** | Cláusula 0030 menciona reservas específicas | Indicar fichas H especiais existentes/pendentes para art.5 XI/XII, com titularidade, exceções e controles |
| **C2** | Entrada em domicílio | Testar flagrante, desastre, socorro, ordem judicial diurna e consentimento, além de dispositivos digitais |
| **C3** | Interceptação/dados armazenados | Distinguir fluxo, acervo, metadados, conteúdos/terceiros, exigências de lei e jurisdição |
| **C4** | Tutela da vida privada | Contraditório diferido, prova ilícita, reparação e risco de vigilância sem supervisão |
| **C5** | Proteção de dados 0031 | Garantir fontes/bases definidas, minimização e controle de finalidade; sem consentimento universal |
| **C6** | Habeas data | Preservar acesso, correção/anotação, gratuidade e resposta judicial tempestiva |
| **C7** | Algoritmos | Descrever decisões unicamente automatizadas, direito a informação, contestação e revisão; **não inventar direito geral à revisão humana vigente** |
| **C8** | Segurança pública | Direito constitucional não desaparece com exceção de aplicação comum da LGPD |
| **C9** | Autoridade independente | Investigar M07: autonomia, competência, orçamento, controle, interação federativa |
| **C10** | Coordenação | Registrar conflito/duplicação com M01/M06/M07/M12 e cláusulas de tutela `0007` |

**Prioridade de entrega:** C1, C2, C3, C6 e C8 são **bloqueios de afirmação de equivalência**, não impedimentos de um PR de **pesquisa H** continuar em draft. C4/C5/C7/C9/C10 são requisitos de aprofundamento e revisão institucional.

## 4. Contraexemplos adversariais críticos

1. Polícia faz varredura irrestrita de telefones em bairro sob "necessidade" sem lei/reserva de acesso a dados.
2. Gestor invade residência por suspeita vaga com base em "controle cabível" sem flagrante, desastre, socorro ou mandado adequado.
3. Governo considera legítimo compartilhar integralmente dados de saúde a prestadores sem finalidade específica/segurança.
4. Lei cria banco estatal com dados inexatos, e proíbe habeas data gratuito porque `0031` diz apenas "meios efetivos".
5. Regime de inteligência alega que a LGPD não se aplica e que nenhum direito constitucional protege o tratamento.
6. Algoritmo recusa benefício e não oferece informação, contestação nem canal de revisão relevante.
7. Reforma confunde acesso a dados de terceiros com direito irrestrito de divulgação e prejudica vítimas.
8. Autoridade fiscalizadora é politicamente removível sem controle, mas mantém rótulo "independente".

Matriz ligada: `M06-03_MATRIZ_PARECER_PRIVACIDADE.csv`. Todos os casos são **testes conceituais**, não estatísticas nem conclusões judiciais para situações particulares.

## 5. Fontes brasileiras e comparadas consultadas

- [CF/1988 compilada](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm), art. 5º X–XII, XXXV, LVI, LXXII, LXXVII, LXXIX; EC 115/2022.
- [Lei 9.507/1997](https://planalto.gov.br/ccivil_03/leis/l9507.htm), arts. 7º–8º (HD).
- [LGPD Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), arts. 4º, 6º, 18 e 20, texto atual.
- [STF ADI 6387 (MP954)](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=6387); [STF ADI 6649](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=6649).
- [CADH arts. 8º, 11 e 25](https://www.oas.org/pt/cidh/mandato/Basicos/convencion.asp): parâmetro convencional de privacidade e tutela; não confundir com regra atual de LGPD.

**Grau de certeza:** confronto literal CF/LGPD/Lei 9507/CF-NOR = alto; efeitos exatos de todos os precedentes e acesso a provas em setores específicos = pesquisa complementar necessária; recomendação institucional = **P**, não fato nem decisão ratificada.

## 6. Handoff obrigatório

**FEITO:** parecer funcional sobre as **duas propostas H** do PR59, dez controles, oito contraexemplos, vínculo com HD, lei de dados e reservas especiais; conteúdo em branch de pesquisa PR62. **PENDENTE:** acórdãos integrais e jurisprudência atual, modelos concretos de autoridade M07, provas empíricas e soluções normativas especiais; **não** reescritas as propostas nem ratificada nova decisão. **PRÓXIMO:** M01.13 e M06 devem preparar alternativas de cláusula específica para reservas do domicílio/comunicações e de tutela de dados, com revisão de M07/M12; **não criar CF-NOR sem reserva de ID e fonte canônica**.

**Localização:** parecer escrito no PR62; feedback ao PR59 deve ser vinculado ao corpo desse PR e à issue #57, distinguindo comentário de edição do texto. CI do HEAD final deve ser rechecado.
