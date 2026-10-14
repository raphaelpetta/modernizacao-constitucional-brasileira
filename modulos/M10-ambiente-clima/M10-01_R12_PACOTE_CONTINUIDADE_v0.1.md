# M10.01-R12 — Pacote de continuidade e recibos de coordenação

**Ciclo:** CF-M10.01-S012 · **Corte:** 14/10/2026 · **Issue:** #88 · **PR:** #89 (draft).  
**Branch:** `pesquisa/m10-01-ambiente-clima-20261014`.  
**Main de entrada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **PR HEAD inicial:** `fcdea83074f9dfae6dc39aad509a565747ed3f8c`.  
**Estado:** coordenação intermodular, **não deliberação F6 ou redação F7**. Sem decisão D, nova CF-NOR, reserva de ID, edição do CLF, `redacao/`, índice ou `main`.

## FEITO — novos produtos

| Arquivo | Conteúdo |
|---|---|
| `M10-01_R12_REGISTRO_CONSULTAS_PLANEJADAS.csv` | 4 solicitações delimitadas e 2 dependências sem canal especializado, com escopo por ficha |
| `M10-01_R12_PROTOCOLO_SOLICITACOES_v0.1.md` | Fórmula jurídica de cada consulta, fontes e critérios de resposta; links para fichas R10 |
| `M10-01_R12_RECIBOS_PUBLICACAO_E_ESTADO.csv` | 4 **IDs e URLs reais** de comentários publicados; 2 dependências sem comentário setorial |

### Pedidos efetivamente publicados

| ID | Destino aberto e interface | Comentário GitHub | Situação no ato |
|---|---|---|---|
| `REQ-R12-01` | M06.02 [issue #65](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/65) — [F04 tutela/ACP/popular](M10-01_R10_FICHA_F04_TUTELA_AMBIENTAL_v0.1.md) | [6169976170](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/65#issuecomment-6169976170) | `PEDIDO_PUBLICADO_AGUARDA_PARECER` |
| `REQ-R12-02` | M04.01 [issue #21](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/21) — [F03 competências/licença/fiscalização](M10-01_R10_FICHA_F03_FEDERALISMO_AMBIENTAL_v0.1.md) | [6169977235](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/21#issuecomment-6169977235) | `PEDIDO_PUBLICADO_AGUARDA_PARECER` |
| `REQ-R12-03` | M05.01 [issue #25](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/25) — [F06 EC132/2023 e CF225 §1 VIII](M10-01_R10_FICHA_F06_REGRAS_ESPECIAIS_TRANSICAO_v0.1.md) | [6169978299](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/25#issuecomment-6169978299) | `PEDIDO_PUBLICADO_AGUARDA_PARECER` |
| `REQ-R12-04` | M01 [PR #22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22) — [F01 direito intergeracional](M10-01_R10_FICHA_F01_DIREITO_INTERGERACIONAL_v0.1.md) e [F02 EIA/publicidade](M10-01_R10_FICHA_F02_EIA_PUBLICIDADE_v0.1.md) | [6169979400](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/22#issuecomment-6169979400) | `PEDIDO_PUBLICADO_AGUARDA_PARECER` |

**Critério de proveniência:** IDs e links acima correspondem a **comentários realmente publicados** via GitHub. Um comentário de consulta não comprova revisão, aceitação, concordância, decisão, delegação de competência ou criação de obrigação para a outra frente. Não há parecer recebido nesta rodada.

### Coordenação sem pedido setorial (evitar duplicações)

- **DEP-R12-05, F05:** M11/M13, titulares indígenas/tribais, consulta adequada, alcance/hierarquia OIT 169, CF231, distinção de audiência LAE e manifestação de órgão; **não foi encontrado canal especializado aberto na fotografia consultada**, e não foi criado automaticamente novo issue/subciclo nem atribuída aprovação.
- **DEP-R12-06:** M07/M08/M14/M03, questões administrativas, bens e atividades econômicas, cultura/fauna, localização nuclear e transição; ainda requer coordenação e revisão própria. A presença na R12 não dá cobertura à cláusula experimental nem encerra a F06.
- O [PR89](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/89) segue veículo documental do M10, e a [issue88](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/88) é referência de dependências abertas.

## PENDENTE — o que falta de fato

1. **Resposta M06 à F04:** comparar ação popular ambiental (cidadão/isenção salvo má-fé) com ACP Lei7.347/1985, legitimados, tutela preventiva, prova, custas, execução e duplicidade B-TEXTO-02/08 com `CF-NOR-0007` H.
2. **Resposta M04 à F03:** repartir o verbo legislar, proteger, licenciar, fiscalizar e agir supletivamente; LC140 e alcance do julgamento ADI4757; interface M07.
3. **Resposta M05 à F06:** efeito de CF225 §1VIII da EC132 nas redações 2026/2027/2033, LC214, faseamento e eventual impacto; sem estimativa inventada.
4. **Resposta M01 às F01–F02:** titular/devedor/legitimado intergeracional e enunciado autônomo EIA prévio/publicidade; relação com justiça.
5. **M11/M13:** consulta/direitos originários/hierarquia convencional sem parecer especializado no recorte de fontes; não supor que o tratado concede veto universal ou que audiência supre consulta.
6. **Regras especiais restantes:** biomas patrimônio nacional, terras estaduais especialmente protegidas, reatores nucleares, proteção animal e ressalva cultural; reservas A/B permanecem marcadores sem efeito normativo.
7. **Jurisprudência pendente:** último estado processual inteiro das ADIs7913/7916/7919 e ADC102 em 14/10/2026 não certificado nesta rodada; pautas não são mérito.
8. **F6/F7/G4:** nenhuma alternativa constitucional deliberada; não há CF-NOR M10 candidata e não se pode afirmar equivalência ou não regressão real.
9. **QA fechamento:** confirmar SHA do último commit, CI estrutural e `main` final; status **recebido** só pode nascer de evidência nova, nunca da emissão dos pedidos.

## PRÓXIMO — M10.01-R13

**Triagem de devolutivas e coordenação dos temas sem canal:** consultar, com referência aos IDs de comentários R12, os quatro canais, verificando se algum ato posterior trouxe parecer documental literal e commit. Se houver, reconciliar o conteúdo com F01–F06, preservando concordâncias e divergências sem promover automaticamente H→D. Se não houver, **não refazer o mesmo inventário**: atualizar apenas o estado do recibo e executar o preflight de abertura de M11/M13 para avaliar um caminho documental sem duplicação de frente. Na ausência de novos documentos, preservar o projeto como `DEPENDENCIA_ABERTA`, não gerar parecer externo fictício.

**Critério de saída:** status de resposta por pedido com URL/SHA ou `SEM_DEVOLUTIVA_DOCUMENTADA`; nova atividade concreta para M11/M13 ou ausência justificada de canal, sem criar CF-NOR e sem editar outro subciclo de maneira implícita.

## INTEGRIDADE

| Objeto | Estado |
|---|---|
| CF-DEC-004 | D(guia) preexistente, sustentabilidade/futuras gerações; não é aprovação R12 |
| F01–F06 / 23 alternativas | H/A/V, sem seleção ou nova D |
| Arquiteturas A/B e reservas | H experimental, sem texto canônico |
| Solicitações aos módulos | **4 comentários publicados**, zero parecer tratado como recebido |
| `main`, `redacao/`, CLF | Sem alterações |
| PR89 | Aberto/draft, sem merge |
| CI | Verificar após último commit; valida estrutura, não mérito jurídico |
