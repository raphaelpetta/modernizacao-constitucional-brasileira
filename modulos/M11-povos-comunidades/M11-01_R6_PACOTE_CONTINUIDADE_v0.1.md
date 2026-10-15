# M11.01-R6 — Pacote FEITO / PENDENTE / PRÓXIMO

**Sessão:** CF-M11.01-S006 · **Corte:** 14/10/2026 · **Issue:** [#92](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/92) · **PR:** [#94](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/94), draft.
**Branch:** `pesquisa/m11-01-direitos-originarios-20261014` · **main de entrada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **HEAD PR94 de entrada:** `4d94777fea405860b9dcb0892f86291b0a349c8d`.
**Estado:** pesquisa F1–F5, sem F6/D, F7/CF-NOR, reserva de identificador normativo, escrita em `redacao/`, main ou CLF.

## FEITO

| Entrega M11-R6 | Resultado novo e verificável | Limitação |
|---|---|---|
| `M11-01_R6_PARECER_TUTELA_LEGITIMIDADE_E_COISA_JULGADA_v0.1.md` | Seis vias: legitimidade CF232, MI individual, MI coletivo, ACP, popular, MP/DP; STF ADPF991 e **Tema1075**; confronto real com M06 PR62 e `CF-NOR-0007` H | Não é revisão de competência processual assinada por M06; não aprova arquitetura |
| `M11-01_R6_MATRIZ_SOBREPOSICAO_REMEDIOS.csv` | **16 funções** com normas/titulares/objetos/efeitos, referência A/B e revisor | É auditoria de remissões, não certificação de equivalência |
| `M11-01_R6_TESTES_LEGITIMIDADE_VIAS.csv` | **12 casos hipotéticos**, entre eles MI sem norma, omissão administrativa, legitimidade especial, associação recente, MI individual/coletivo, ACP nacional e custos, ação popular e CF232 | Não são decisões de casos concretos |
| `M11-01_R6_PEDIDO_REVISAO_M06_v0.1.md` | **8 perguntas de interface para M06** com normas, objeto, saída esperada, prova/limites | Publicação de pedido não é parecer M06 recebido |
| `M11-01_R6_COMPLEMENTO_F05_M10_TUTELA_v0.1.md` | Devolutiva **M11 parcial R6** à F05/M10; distingue acesso geral, titular indígena e remédios especiais | Depende da revisão M06/M13 e de futuro texto |
| Este pacote | FEITO/PENDENTE/PRÓXIMO, estados e controles técnicos | CI final deve ser conferido no HEAD |

### Achados jurídicos a preservar no próximo ciclo

1. **CF232** assegura legitimidade judicial própria dos indígenas, comunidades e organizações, com intervenção do MP em todos os atos. [STF ADPF991 MC-Ref](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=232&abrirBase=CF) reconheceu legitimidade da APIB no objeto concreto, não a equiparação automática de todos os ritos.
2. **CF5 LXXI e Lei13.300** protegem o exercício de direito constitucional inviabilizado por omissão normativa. Arts8–13 têm regras específicas de concretização, extensão, revisão, efeitos intertemportais, impetração coletiva e concorrência com individuais; arts12 III/13 tratam, respectivamente, de associação com requisitos legais e prazo de 30 dias após ciência comprovada para desistência individual quando se pretendem benefícios da coisa julgada coletiva. **Não copiar o prazo de 30 dias como prazo de consulta indígena.**
3. **ACP (Lei7347)** permite tutela transindividual e obrigação de fazer/não fazer, com legitimados e custos próprios; **STF Tema1075, RE1.101.937, trânsito em julgado 01/09/2021**, invalidou limitação territorial posterior do art16 e restabeleceu a redação original, com competência/prevenção para ações nacionais/regionais. O texto literal consolidado sem o julgamento pode induzir erro.
4. **Popular** continua ação do cidadão, com isenção de custas e sucumbência salvo comprovada má-fé; **não** é consequência direta do art232 uma associação indígena tornar-se cidadã autora de ação popular.
5. **M06 PR62** realmente possui MI individual/coletivo, popular, tutela coletiva e execução. **Falta na amostra o parecer específico da interface com CF232**, não todo o estudo de MI.
6. **MI7516** é teste de omissão normativa mineral e tutela contra garimpo ilegal distinta; o plano de desintrusão determinado pelo STF **não comprova execução final** e não autoriza exploração automaticamente.

## PENDENTE

- [ ] **M06 #65 / PR62:** receber parecer específico sobre oito perguntas da R6 e cotejar CF232 × MI × ACP × popular e aplicação do STF Tema1075. Não presumir aceitação de texto M11.
- [ ] **M13 #93:** hierarquia/alcance da Convenção169 ainda sem resposta especializada identificada.
- [ ] **M03/M05/M10/M07/M08:** autorização parlamentar, participação em lavra, EIA/licenças, bens/terras e deveres ambientais, nos objetos respectivos.
- [ ] **M10 F05:** parecer M11 deve constar `PARECER_M11_PARCIAL_R6`, sem aprovar os ensaios A/B e sem misturar CF-NOR0007 H com D.
- [ ] **MI7516:** decisões posteriores sobre plano desintrusão e eventual lei/outorga precisam de fontes oficiais antes de afirmação de conclusão de cumprimento.
- [ ] **Constituição futura:** inexistem texto canônico de M11, deliberação F6, equivalência integral ou revisão intermodular ratificada.
- [ ] **QA de fechamento:** reler 6 arquivos e contar 16 registros/12 testes/8 perguntas, conferir refs de cláusulas A/B, publicar links nos canais, verificar SHA/CI/main.

## PRÓXIMO

**Evitar novas matrizes semelhantes enquanto não houver evidência.** Há duas tarefas autônomas possíveis com ganho real:
- **M13.01-R1 na [issue #93](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/93):** abertura de pesquisa própria de aprovação/ratificação/promulgação/hierarquia e aplicabilidade da OIT169, com confronto com a CDPD e a participação/consulta da M11, **sem simular resposta pronta**.
- **M11.01-R7:** apenas após devolutiva real M06 ou nova jurisprudência, fazer teste de equivalência de uma cláusula de tutela especial em texto canônico **se F6 for deliberado**, conservando H/A/V na ausência dessa decisão.

**Integridade:** PR #94 draft, main/CLF/redacao sem escrita. CI estrutural é QA, não revisão jurídica ou consentimento dos povos afetados.
