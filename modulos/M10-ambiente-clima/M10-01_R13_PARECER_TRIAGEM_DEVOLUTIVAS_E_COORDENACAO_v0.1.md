# M10.01-R13 — Parecer de triagem de devolutivas e abertura de canal temporal M14

**Sessão:** CF-M10.01-S013 · **Corte:** 14/10/2026 · **PR M10:** #89, draft · **Issue M10:** #88.  
**Main na abertura:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`; **HEAD do PR89 na abertura:** `771c02493b5aff8ea5a67fdfffaf2d9658089c3e`.  
**Natureza:** coordenação documental e revisão de fontes, sem escolha material F6/D, redação F7, criação de CF-NOR, reserva de ID nem edição de main ou CLF.

## 1. Retornos à R12: quatro pedidos conferidos, nenhum parecer específico identificado

A consulta às **conversas GitHub em 14/10/2026** encontrou:

| Solicitação anterior | Canal | Observação posterior | Estado |
|---|---|---|---|
| `REQ-R12-01`, F04 tutela/ACP | [M06 #65](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/65#issuecomment-6169976170) | Só o próprio comentário da consulta aparece na discussão depois de publicado | `SEM_DEVOLUTIVA_DOCUMENTADA` |
| `REQ-R12-02`, F03 licenciar/fiscalizar | [M04 #21](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/21#issuecomment-6169977235) | Comentário posterior `6170217229` trata de transição/mandatos M14, não de F03 | `SEM_DEVOLUTIVA_DOCUMENTADA` |
| `REQ-R12-03`, F06 art225 §1 VIII | [M05 #25](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/25#issuecomment-6169978299) | Comentário posterior `6170218807` trata de custos/caretaker M14, não de art225 VIII | `SEM_DEVOLUTIVA_DOCUMENTADA` |
| `REQ-R12-04`, F01/F02 | [M01 PR22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/22#issuecomment-6169979400) | Apenas comentário original de interface no diálogo consultado | `SEM_DEVOLUTIVA_DOCUMENTADA` |

**Outros controles:** PR #89 tinha **zero reviews formais e zero comentários de código** no retorno da API; seus comentários de issue #88 até esta ronda eram registros do próprio M10. Não confundir a pesquisa já existente nos PRs #22/#62 ou na main M04/M05 com **devolutiva posterior** a cada pergunta de R12. O estado é uma fotografia de canais/arquivos consultados, **não afirma ausência universal de comunicações fora desse recorte**.

Os links e IDs com evidência de cada estado são consolidados em `M10-01_R13_STATUS_DEVOLUTIVAS_E_CANAIS.csv`.

## 2. Fato novo: M14.01 tem canal real, mas outro objeto prioritário

A primeira busca por PRs abertos, feita pela pesquisa de PRs, não expôs o **[PR #91 M14.01](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/91)**. A listagem direta da API `pulls?state=all` e a leitura de PR91 e da [issue funcional #90](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/90) confirmaram que estão abertos, **em draft**, branch `pesquisa/m14-01-transicao-constitucional-20261014`, HEAD consultado `ae15beb6e923bda060ee3edb43db9fe2b310519a`.

**Escopo encontrado:** transição de sistema de governo e mandatos, continuidade de governo, consulta popular, competências e T0–T4. Seu parecer autônomo não se apresenta como exame da regra tributária ambiental de biocombustíveis e hidrogênio de baixo carbono.

**Ação executada:** [comentário 6170667693 na issue #90](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/90#issuecomment-6170667693) pede **apenas** verificação da recepção e vigência temporal do art.225 §1 VIII sob as versões da EC132 (2023/2027/2033), com separação da pesquisa fiscal específica de M05. **Status: pedido publicado, não resposta recebida; não amplia unilateralmente M14.01 nem cria subciclo novo.**

## 3. M11/M13: nota jurídica própria do M10, sem simular revisão independente

As listagens de `issues?state=all` e `pulls?state=all`, filtradas por M11/M13 e assunto, não apresentaram canal específico de povos/tratados; a main consultada continha apenas M00/M01/M03/M04/M05, sem dossiê setorial desses módulos.

A [nota M10-R13 sobre consulta/tratados](M10-01_R13_NOTA_INTERFACE_M11_M13_CONSULTA_TRATADOS_v0.1.md) estabelece **oito perguntas divididas por titularidade e representação, consulta, tutela judicial, hierarquia de tratados e procedimentos ambientais**, com fontes primárias:
- [CF art231 e art5 §§2–3](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm);
- [Convenção OIT 169, arts6–7](https://www.ilo.org/pt-pt/resource/c169-sobre-povos-indigenas-e-tribais), incorporada em [Decreto10.088/2019, Anexo LXXII](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10088.htm);
- [Lei15.300/2025, art4 §2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm): audiência LAE não substitui consulta prévia quando exigível;
- [Lei15.190/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm): manifestações de órgãos envolvidos e procedimentos legais próprios.

**Inferências proibidas:** consulta equivale automaticamente a veto universal; o ato de um órgão estatal substitui a voz dos titulares; não homologação exclui necessariamente direito originário; hierarquia de qualquer tratado é idêntica à de outro; um esboço A-TEXTO/B-TEXTO equivale ao dispositivo CF231 ou à Convenção169 sem cotejo.

A questão jurisprudencial de último andamento das ADIs7913/7916/7919 e ADC102 permanece pendente de fonte processual decisória integral em 14/10. [Notícia oficial do pautamento de 12/08/2026](https://noticias.stf.jus.br/postsnoticias/confira-a-pauta-do-stf-desta-quarta-feira-12-2/) não valida resultado.

A nota foi comunicada como dependência na [issue M10 #88, comentário 6170736588](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/88#issuecomment-6170736588), sem criar issue ou PR M11/M13 fictício.

## 4. Consequência operacional para cada ficha R10

| Ficha | Incremento verificável nesta R13 | Limite |
|---|---|---|
| F01/F02 | M01 continua com pedido R12 sem retorno | Nenhuma ratificação nem equivalência da CF-NOR0007 H |
| F03 | M04 #21 tem comentário posterior de outra interface | Não constitui resposta ao licenciamento/fiscalização |
| F04 | M06 #65 segue sem devolutiva | Pesquisa M06 existente sobre ação popular permanece válida, mas não é novo parecer ACP |
| F05 | Oito perguntas e fontes oficiais reunidas no **M10** | Não é resposta de M11/M13 nem resolve hierarquia e remédio |
| F06 | M05 sem retorno e M14 #90 agora recebeu pedido de alcance temporal | Nenhuma transposição das reservas fiscais, patrimoniais, dominiais, nucleares ou culturais |

**Todas as seis fichas seguem H/A/V**. A criação de comentário não modifica a matriz de direitos, competências ou as 23 alternativas não selecionadas da R10.

## 5. FEITO / PENDENTE / PRÓXIMO

**FEITO:** conferir respostas nos quatro canais; descobrir e ler M14.01 PR91/#90; publicar quinto pedido `REQ-R13-05`; produzir quadro de seis estados e nota de oito perguntas M11/M13; registrar dependência na issue #88.  
**PENDENTE:** retornos independentes, canal próprio M11/M13, revisão técnica do tratado e direito originário, parecer fiscal de vigência, jurisprudência de licenciamento atualizada, decisões F6, CF-NOR F7 e auditoria de equivalência.  
**PRÓXIMO — R14:** preflight de escopo e de reservas de subciclo para decidir **onde** iniciar M11.01/M13.01, caso ainda inexistentes, sem reapresentar como matéria M10; alternativamente incorporar resposta específica recém-publicada dos canais. O produto mínimo será **um encaminhamento funcional claro** com número de issue/PR existente ou decisão de aguardar coordenação, não novo inventário repetitivo.

**Integridade:** PR89 permanece draft, sem merge; nenhuma alteração em `main`, `redacao/`, `indice.csv`, CF-DEC ou CLF. CI deve ser conferido após último commit e valida somente estrutura.
