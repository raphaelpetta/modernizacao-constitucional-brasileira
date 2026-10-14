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
