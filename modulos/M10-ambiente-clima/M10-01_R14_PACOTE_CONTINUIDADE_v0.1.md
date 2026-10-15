# M10.01-R14 — Pacote de continuidade

**ID:** CF-M10.01-S014 · **Corte:** 14/10/2026 · **Issue-mãe:** #88 · **PR:** #89 (draft) · **Branch:** `pesquisa/m10-01-ambiente-clima-20261014`.  
**Base `main` de entrada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **PR HEAD de entrada:** `50c8f596718e7db02d596f56eb02bb1c446e701e`.  
**Status:** coordenação F0, sem pesquisa especializada M11/M13 concluída, sem F6/D, F7/CF-NOR nem prova de equivalência G4.

## FEITO

1. **Preflight de escopo e duplicidade:** catálogo M00–M14, `governanca/04_ESTADO_ATUAL.md`, `13_QUADRO_DE_COORDENACAO.md`, `15_REGISTRO_RESERVAS_IDS.md`; `main` e PR89; issues/PRs `state=all`, branches e busca textual de M11/M13. **Não existia canal específico M11.01 ou M13.01**, segundo a fotografia consultada. A coordenação já previa a separação de objetos no catálogo e no quadro; issue com escopo consolida reserva de subciclo pelo protocolo CF-GOV-015.
2. **Nova [M11.01, issue #92](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/92)** — F0 aberta/reservada para direitos originários, territórios, titulares, consulta e tutela de povos indígenas e comunidades tradicionais, com fontes atuais, insumos M10 R13 e resultados esperados. **Nenhum estudo M11.01 ou PR M11 foi criado nesta rodada.**
3. **Nova [M13.01, issue #93](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/93)** — F0 aberta/reservada para tratados, recepção, hierarquia e controle, com ênfase na OIT169 e interface M11, fontes e produtos esperados. **Nenhum estudo M13.01 ou PR M13 foi criado nesta rodada.**
4. **Coordenação central:** link de M13 no [comentário de M11 #92](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/92#issuecomment-6171535947) e [registro de duas reservas na issue #53](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/53#issuecomment-6171537360). Títulos/canais impedem duplicar a análise ambiental M10 ou a análise de hierarquia M13.
5. **Arquivos na branch M10 PR89:** `M10-01_R14_REGISTRO_CANAL_E_RESERVAS.csv` (**8 registros**, incluindo 2 issues, coordenação e 5 pedidos ainda não respondidos), `M10-01_R14_PARECER_ENCAMINHAMENTO_M11_M13_v0.1.md` e este pacote.
6. **Devolutivas conferidas em canais R12/R13:** M01 #22 (F01/F02), M04 #21 (F03), M05 #25 (F06), M06 #65 (F04) e M14 #90 (F06): **sem parecer específico identificado no recorte GitHub consultado**. M14/PR91 debate mandatos; comentários novos sobre financiamento da primeira investidura não respondem à regra fiscal ambiental.

## PENDENTE

- [ ] Pesquisa efetiva M11.01 (F1–F5): titularidade e território CF231/232, consulta OIT169, representatividade, direito originário versus gatilho de manifestação administrativa, remédio e efeitos para M10 F05.
- [ ] Pesquisa efetiva M13.01: aprovação/ratificação/incorporação/hierarquia de OIT169 versus outros tratados, grau aplicável, controle e distinção do regime da CDPD. **Issue aberta não é parecer recebido.**
- [ ] Respostas documentadas M01/M04/M05/M06/M14; estudos M07/M08/M03 sobre administração/terras/nuclear e clima; não inventar anuência nem prazo.
- [ ] Regras especiais da CF225 (§1 VIII e §§4–7) ainda marcadas como reservas sem transposição válida em R9; F06 aberta.
- [ ] Último status decisório contemporâneo das ADIs7913/7916/7919 e ADC102, sem inferir resultado da pauta; evidência factual de custos/impactos ainda ausente.
- [ ] Decisão F6 expressa, eventual texto F7 canônico e auditoria literal de equivalência: **nenhum executado**.
- [ ] O arquivo `governanca/15_REGISTRO_RESERVAS_IDS.md` da **main** não foi editado para acrescentar M11.01/M13.01; as **issues #92/#93** são o registro operacional das reservas e a [coordenação #53](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/53#issuecomment-6171537360) recebeu o handoff. Evitar edição transversal concorrente na branch M10.
- [ ] Verificar CI estrutural do HEAD final R14 e confirmar `main` intacta após todos os commits.

## RESULTADO / ESTADO

| Objeto | Estado |
|---|---|
| M11.01 / M13.01 | **F0_ABERTO; ESCOPO_RESERVADO_POR_ISSUE**, pesquisa especializada pendente |
| F05 M10 | **DEPENDÊNCIA_AGORA_COM_CANAL**, mas **PARECER_NÃO_RECEBIDO** |
| F01–F04, F06 | H/A/V; solicitações publicadas e sem resposta específica demonstrada |
| R9 A/B e R10 23 alternativas | Hipóteses não selecionadas, sem efeito normativo |
| CF-DEC-004 | D(guia) preexistente, alcance não ampliado por esta rodada |
| CF-NOR, `redacao/` e índice | Nenhuma escrita/reserva de norma |
| `main` e CLF | Sem alterações |
| PR89 | Aberto em draft; não houve merge |

## PRÓXIMO — M11.01-R1, pesquisa própria (tarefa executável)

A partir da [issue #92](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/92), realizar F1–F5 **num branch M11 distinto** após novo preflight: dossiê dos direitos originários/consultas (CF231/232, Convenção169 arts1/6/7), matriz de fatos e titulares, pelo menos 8 testes e resposta documental **específica** à ficha M10 F05 (o que `A-TEXTO-11`/`B-TEXTO-10` cobre ou não). Conservar hierarquia de tratados sob M13.01 #93 até sua pesquisa independente e não inventar parecer recebido. Ao concluir M11, registrar sua própria prestação de contas e enviar referência documental real a M10 #88; M10 permanece draft até decisões e revisões posteriores.

**QA:** CI estrutural não atesta validade jurídica, equivalência ou ratificação. Não fazer merge automático nem editar CLF.
