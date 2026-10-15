# M13.01-R4 — Pacote de continuidade e fechamento documental

**ID:** CF-M13.01-S004 · **Corte:** 15/10/2026 · **Issue:** [#93](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/93) · **PR:** [#98](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/98), draft.  
**Branch:** `pesquisa/m13-01-tratados-hierarquia-20261014` · **main preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **HEAD anterior R4:** `e39ad3c3b916d7cb482b298dc833a5dae7648cc4`.  
**Governança:** F1–F5 pesquisa, **sem decisão F6/D, texto CF-NOR F7, reserva de identificador, alteração `redacao/`, `main`, CLF ou merge**.

## FEITO

| Artefato | Entrega | Limite |
|---|---|---|
| `M13-01_R4_PARECER_XUCURU_SENTENCA_E_CUMPRIMENTO_v0.1.md` | Dossiê **Corte IDH sentença 05/02/2018 Série C346**, resoluções 2019 e 2023, audiência 2024, painel CNJ; **obrigações distintas por ponto** | Não é perícia da área nem andamento atualizado de cada ação judicial interna |
| `M13-01_R4_MATRIZ_PONTOS_RESOLUTIVOS_XUCURU.csv` | **7 pontos resolutivos relevantes (PR7–PR13), 8 entradas** (PR11 reparado em duas obrigações financeiras), natureza/beneficiário/prazo/status/fonte | PR8/9 pendentes no estado público não provam inexistência de qualquer ação estatal recente |
| `M13-01_R4_CRONOLOGIA_SUPERVISAO_XUCURU.csv` | **7 marcos** sentença, supervisões, relatórios, audiência, monitoramento até 2026 | Separar fonte judicial, CNJ e notícia do Ministério |
| `M13-01_R4_TESTES_EXECUCAO_E_EFEITOS_XUCURU.csv` | **10 cenários fictícios** sobre pagamento, desintrusão, benfeitorias, relatórios, legitimidade e sentença internacional | Não avaliam chance de processos concretos |
| `M13-01_R4_DEVOLUTIVA_F05_M06_M11_v0.1.md` | Devolutiva parcial e **3 perguntas delimitadas à M06** sobre cumprimento/efetivação e CADH68; comunicação a M11 e F05/M10 | Perguntas não equivalem a resposta independente M06 |
| Este pacote | FEITO/PENDENTE/PRÓXIMO e QA | CI estrutural não valida o mérito jurídico |

## Achado comprovado e grau de fonte

**[Corte IDH, resolução de 26/06/2023](https://www.corteidh.or.cr/docs/supervisiones/pueblo_indigena_xucuru_26_06_23_spa.pdf):** declara **integralmente cumpridos** pagamentos por dano imaterial ao povo Xucuru e custas aos representantes previstos em PR11. Já a garantia de propriedade coletiva **PR8** e a conclusão da desintrusão/pagamento de benfeitorias a terceiros/remoção de obstáculos **PR9** permaneceram **sob supervisão aberta**. **[CNJ painel atual](https://www.cnj.jus.br/poder-judiciario/relacoes-internacionais/monitoramento-e-fiscalizacao-das-decisoes-da-corte-idh/casos-contenciosos-brasileiros/)** classifica **PR8 e PR9 pendentes**, publicações e pagamentos cumpridos. As publicações **PR10** haviam sido reconhecidas cumpridas na supervisão **22/11/2019**.

**[Corte IDH sentença original 2018](https://www.corteidh.or.cr/docs/casos/articulos/seriec_346_por.pdf):** obrigações de propriedade coletiva contínua e desintrusão não se confundem com indenização por dano imaterial. [Ministério dos Povos Indígenas, audiência 23/05/2024](https://www.gov.br/povosindigenas/pt-br/assuntos/noticias/2024/05/em-audiencia-mpi-relata-evolucoes-para-conclusao-do-caso-da-comunidade-xukuru-em-pernambuco) mostrou ações judiciais internas relevantes **em 2024**, sem efeito declaratório de cumprimento pela Corte.

**Cuidados de prova:** documentos judiciais em PDF do portal da Corte foram indexados e triangulados com CNJ, mas as URLs oficiais retornaram HTTP403 em abertura web integral; não afirmar leitura completa/paginação de acórdão onde o acesso integral falhou. Nenhuma nova resolução de encerramento **foi certificada nesta pesquisa**, o que não exclui posteriores medidas não localizadas. Não atualizar processo específico de reintegração de posse ou ação rescisória só com notícia de 2024.

## PENDENTE

1. **M06 [#65](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/65), [PR62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62):** resposta jurídica própria sobre CADH68.1 e §2, execução interna de obrigação de fazer/dar/proteger, tutela de urgência, relação com coisa julgada doméstica e CF232.
2. **M11 [#92](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/92), [PR94](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/94):** prova fática e antropológica de propriedade/posse, desintrusão e representatividade, sem tomar um caso como diagnóstico de todos os povos.
3. **M10 [#88](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/88), [PR89](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/89):** F05 continua aberta quanto a direitos materiais e tutela, sem extrapolar sentença Xucuru para LAE/LGL de 2025.
4. **Processos internos Xucuru:** checar consulta judicial atualizada de ações em TRF5/STJ e dados sobre retirada/benfeitorias antes de afirmar evolução de 2026. Monitorar resolução da Corte caso publicada depois de 26/06/2023.
5. **Arquitetura de futuras fontes M00/M13:** auditoria de equivalência com CF5 §§2–3, CF231/232, CADH e art68, sem norma canônica/deliberação F6.
6. **Fechamento GitHub:** conferir 6 arquivos, 8 registros da matriz para 7 pontos, 7 marcos e 10 testes; atualizar PR98 e encaminhar links a #93, #65, #92, #88; validar SHA main e workflow do HEAD final.

## PRÓXIMO — M13.01-R5

Escolher **uma revisão de cumprimento real**, não outra matriz genérica: obter **resposta escrita M06** sobre via de execução dos pontos **8 e 9**, confrontar **andamento atual dos processos internos** com a informação de supervisão, e verificar formalmente se a Corte publicou **nova resolução de cumprimento**. Somente então examinar efeitos de dispositivo novo, distinguindo responsabilidade internacional do Estado, comando concreto e sua execução doméstica. Sem assumir consulta a povos feita, sem CF-NOR ou deliberação D.

**Status a confirmar após QA:** `PARECER_M13_PARCIAL_R4`, `XUCURU_8_9_PENDENTES_NO_PAINEL_CNJ`, `M06_PARECER_EXECUCAO_PENDENTE`, `F05_ABERTA`; PR draft e main/CLF inalterados.
