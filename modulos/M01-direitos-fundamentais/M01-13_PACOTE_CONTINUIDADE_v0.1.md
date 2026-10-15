# M01.13 — Pacote obrigatório após alternativas de proteção de domicílio, comunicações e dados

**Data:** 14/10/2026. **Base main de entrada:** `5ac08b622d7552b7d3b37a695a3027b4b9d827d4`. **PR:** [#59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59), *draft de propostas H*; **issue:** [#57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57); M06 [#62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62). **Aprovação material:** nenhuma D.

## FEITO
- Dossiê `M01-13_ALTERNATIVAS_RESERVAS_E_TUTELA_v0.1.md`: **3 arquiteturas** (A reservas explícitas, B tecnológica neutra e funcional, C delegação ampla adversarial), **6 protótipos especiais A/B e um contramodelo**, sem gerar nova ficha `CF-NOR`, 8 escolhas PRI01–PRI08.
- `M01-13_TESTES_ALTERNATIVAS_PRIVACIDADE.csv`: **20 cenários adversariais** de domicílio, consentimento, flagrante, socorro, interceptações, celular, provas, habeas data, dados estatais, algoritmos e autoridade.
- Novo marco jurídico **STF Tema 977** (ARE1042075, julgamento 25/06/2025; publicação 24/09/2025): separar apreensão/preservação/acesso a conteúdo e exceção fortuita estreita; **Tema 280** sobre fundada razão de flagrante e controle posterior. Consultadas Lei9296/1996, Lei9507/1997, LGPD art20 e Constituição.
- Recomendação **P para testes:** regime substantivo `CF-NOR-0030/0031` + reservas especiais de intrusão e remédio gratuito/autônomo conduzido por M06, sem repetir `CF-NOR-0007`.
- Fichas `CF-NOR-0030` e `CF-NOR-0031` **não alteradas**, ainda H e draft; não houve reserva de identificador adicional, geração de anteprojeto ou decisão D.

## PENDENTE
- Verificar inteiro teor dos acórdãos STF 977/280 e outros regimes de busca/acesso remoto; definir tecnicamente hipóteses de exceção digital sem enfraquecer a proteção de 1988.
- Resolver remissões às cláusulas especiais ainda inexistentes, garantir tutela equivalente a habeas data gratuito, revisão por M06/M07/M12/M13/M04, supervisão e competências; comparação N:N e alternativas editoriais completas.
- Decisão de arquitetura A/B e novo ID para norma E **somente após preflight**, acórdãos e revisão; não presumir equivalência.

## PRÓXIMO
**Prioridade executável:** M01.13/M06 preparar minuta experimental *reconciliada* de especialidades E sob opção híbrida A+B, contendo (a) exceções domiciliares e reserva temporal, (b) distinção interceptação de fluxo, acesso a dados armazenados, apreensão e preservação, (c) remédio público de dados com gratuidade e contestação; submeter a revisão M07/M12 e testes antes de reservar CF-NOR. Atualizar `redacao/indice.csv` só na fase editorial posterior autorizada.

**QA:** CI estrutural e estado real do PR59 a conferir no HEAD depois do pacote; a pesquisa não certifica não regressão.

## Marco R2 — Consolidação experimental DOM/COM/HD (14/10/2026)

**Base:** CF `main=e648bd71227f407f2b46207e9c8d546a255254d2`; PR #59 draft; parecer M06 PR #62.

**FEITO:** `M01-13_MINUTA_INTEGRADA_ESPECIAIS_DOM_COM_HD_v0.1.md` reúne **três textos P** (E-DOM: ingresso e exceções, E-COM: fluxo, apreensão, dados armazenados e preservação, E-HD: acesso/correção/anotação gratuitamente) e mapa de integração G+A+E sem duplicar `CF-NOR-0003–0007` ou `0030/0031`. `M01-13_MATRIZ_CONCORDANCIA_ABC_v0.1.csv` mapeia **24 garantias/funções**, e `M01-13_TESTES_CONSOLIDACAO_E.csv` contém **24 casos adversariais**. STF Tema 280/977, CF5 XI/XII/LXXII/LXXVII e Lei9507 foram conferidos; distinção entre apreender, preservar, identificar fortuitamente e acessar foi incorporada. **Não foi criado ID, norma CF-NOR, texto na main nem decisão D.**

**PENDENTE:** cláusula de exceção digital especial ainda admite interpretação ampla e exige texto mais preciso + revisão M06/M07/M12 e do inteiro teor da jurisprudência; conexão ao CPP, sigilo de terceiros, cadeia de custódia, controle de prova ilícita, custos de tutela de dados, reparação e competência M04. Nenhuma equivalência material certificada.

**PRÓXIMO:** M06/M12 revisar frase a frase a E-COM, sobretudo o alcance de identificação fortuita e de preservação sem autorização prévia; M01/M06 comparar E-HD com a garantia constitucional de gratuidade; só então abrir eventuais fichas E com ID livre e geração automatizada, mantendo todas como H até deliberação.

**Critérios editoriais:** esta minuta está em pesquisa; `redacao/propostas/CF-NOR-0030.md` e `0031.md` permaneceram literais; não há segundo índice; conferir CI e main reais após gravação.
