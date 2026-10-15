# CF-CC-016 — Parecer transversal: quatro núcleos de direitos e riscos de compactação

**Estado:** pesquisa H/V e redação H, não F6/D. **Recorte:** M01.14 liberdades, M02 direitos políticos, M06 independência judicial, M14 interface. **Main governança de referência:** `7c3bd80470899a09e31f25a6a3a47d7c9cca669c`, [CF-GOV-019](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/main/governanca/19_POLITICA_GANHO_MARGINAL_GLOBAL.md). **Stack base PR #119:** `948e0405e8fb74d4b0945f1c44007967b5d5b5c0`; documentação da política integrada na main após criação do stack e deverá ser reconciliada antes de merge. **Sem reescrever CF-DEC-006/007/008** (governo, Senado e Corte constitucional seguem abertos).

## Decisão de carteira por ganho marginal ANTES da redação

| Candidata | Entrega nova plausível | Custo / risco | Escolha |
|---|---|---|---|
| H: M01.14 liberdades civis | proteção textual ainda ausente no stack e destino de incisos CF5/220 | médio / R3 (censura/associação) | **Selecionada** |
| V: M02 sufrágio / M06 independência judicial | núcleo de art14 e arts93/95/99 sem adoção de arquitetura política | médio / R3 (voto/Judiciário) | **Selecionada transversalmente** |
| I: reconciliar stack/CI #101/#104/#120 | potencial para liberar integração, mas a causa de CI não é recuperável pelos conectores atuais | alto no escopo técnico / bloqueio externo | **Não prioritária nesta rodada**, incidente #120 permanece |
| H alternativa: aprofundar M05 caixa | novo dado isolado sem prova de alterar a escolha fiscal | alto esforço empírico / ganho imediato baixo | **Pausada** |

**Critério de parada:** uma rodada deverá produzir núcleos redacionais distintos, matriz explícita de garantias, testes que revelem ausências, e handoff; **não** iniciar nova bateria de pesquisas sobre os mesmos quatro artigos sem pergunta capaz de mudar escolha constitucional ou evitar regressão grave.

## 1. O que a CF de 1988 protege e o texto NÃO reproduz por inteiro

### M01.14 — liberdade de expressão, reunião e associação

A [CF arts5 IV–XXI e 220](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm) mantém direitos separados de pensamento, resposta, consciência, cultos, escusa, informação, profissão, locomoção, reunião e associação. A [ADPF130](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=220&abrirBase=CF) e a [ADI4815](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=4815) proíbem censura prévia e autorização de biografia, sem suprimir responsabilidade e direitos da personalidade. A [ADPF187 e ADI4274](https://stf.jus.br/arquivo/informativo/documento/informativo631.htm) distinguem defender publicamente mudança de lei de praticar ilícito.

**Risco:** um único parágrafo “liberdade de expressão” que não consigne sigilo de fonte, resposta/reparação e proteção contra censura pode regredir; por isso a 0049 especifica esses elementos. A 0050 **mantém a distinção entre suspensão judicial e dissolução com trânsito em julgado**, e não converte aviso em autorização. **Lacunas expressas:** consciência/religião (VI–VIII), profissão (XIII), locomoção (XV), imprensa plural, moderação de plataformas e responsabilização de provedores, sindicalismo (art8), partidos (art17), tutela urgente e proteção contra particulares; a próxima proposta precisa ser independente e fundamentada.

### M02 — direitos políticos, não modelo eleitoral

A [CF art14](https://www.tse.jus.br/legislacao/codigo-eleitoral/constituicao-federal/constituicao-da-republica-federativa-do-brasil) contém voto, consultas, critérios de alistamento, idade, inelegibilidade, reeleição e outras proteções. [CF art60§4º II](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm) protege o voto direto, secreto, universal **e periódico**. A H-0051 é um núcleo de participação e acessibilidade, mas **a periodicidade não foi incluída expressamente na H** e exige revisão. Não escolher obrigação de votar, fórmulas partidárias, sufrágio de 16–18 anos, conscritos, cargos de eleição indireta ou modelo de chefia de Estado por omissão. A Res TSE 23.748/2026 descreve calendário para **eleições sob direito vigente**, não resolve automaticamente um futuro sistema constitucional A/B/C. [Fonte TSE](https://www.tse.jus.br/legislacao/compilada/res/2026/resolucao-no-23-748-de-26-de-fevereiro-de-2026).

### M06 — independência institucional não equivale a estrutura do Judiciário

[Art.93 IX](https://www.cnj.jus.br/programas-e-acoes/gestao-documental-e-memoria-proname/constituicao-federal/) estabelece publicidade, fundamentação **sob pena de nulidade**, com hipóteses restritas de sigilo. [Art.95](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm) garante vitaliciedade, inamovibilidade e irredutibilidade à magistratura, além de proibições de atividades incompatíveis, com regimes detalhados; [art.99](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm) prevê autonomia administrativa e financeira, não imunidade a controle. [CADH art8](https://www.planalto.gov.br/ccivil_03/decreto/d0678.htm) protege tribunal competente, independente e imparcial, previamente estabelecido por lei, prazo razoável.

**Objeção forte:** a H-0052 mantém vitaliciedade para juízes de carreira, porém qualquer tribunal constitucional especial com mandato determinado requer desenho próprio e avaliação da independência em termos funcionais. **Lacunas críticas:** nulidade de decisão imotivada não reproduzida explicitamente; exceções ao sigilo amplas; CNJ e disciplina administrativa; composição e competências das cortes; remuneração/proibições éticas, legitimidade de ações constitucionais, Defensoria e assistência gratuita. A H **não certifica integridade dos arts92–126**.

## 2. Como a auditoria altera a pauta

Arquivos:
- [30 verificações N:N](../../auditoria/CF_CC_016_MATRIZ_30_GARANTIAS.csv): todos os resultados por direito são **PARCIAL**, **NAO_COBERTO**, **APENAS_REMISSAO**, **EM_OUTRA_FICHA_H** ou **SEM_DECISAO**, nunca “equivalente”.
- [20 ataques adversariais](../../auditoria/CF_CC_016_MATRIZ_20_TESTES.csv): censura e manifestação; licenciamento de reunião; associações; voto, acessibilidade e consultas; juízes, nulidade, orçamento e tribunal separado. **São testes de hipóteses, não 20 julgados concluídos.**
- Quatro novos textos em `redacao/propostas/CF-NOR-0049..0052.md`, fontes indexadas e anteprojeto derivado.

**Melhor objeção à rodada inteira:** quatro H curtas ainda podem ampliar **aparência de cobertura** sem resolver perdas do sistema vigente. **Resposta provisória:** matriz com ausências explícitas, 20 testes, fontes oficiais e estados H, sem declaração de conclusão dos módulos. A prioridade seguinte não será elevar contagem, mas **decidir qual lacuna substantiva distinta possui maior ganho marginal**, por exemplo: art5 VI–VIII (consciência/religião), CF14 parágrafos/CF17, ou controle constitucional e acesso à justiça (M06). Escolher por risco e falta de tutela, não por número de artigos.

## 3. FEITO / PENDENTE / PRÓXIMO

**FEITO:** quatro blocos H em três módulos; mapa N:N e contraprovas; preservação explícita das decisões políticas abertas. **PENDENTE:** compatibilidade normativa com CF5 integral, CDPD, CADH, CF14–17 e art60§4 II, cortes e autonomia judicial, participação de minorias, efeitos na transição M14, revisão externa R3. **PRÓXIMO:** rodada independente de maior ganho comparado, com direitos de consciência (M01), garantias de elegibilidade/periodicidade (M02) ou estrutura do controle constitucional (M06); não repetir mecanicamente estes mesmos quatro textos. **INTERFACES:** M00/M01/M02/M03/M04/M05/M06/M07/M08/M12/M13/M14; CLF não impactado diretamente.
