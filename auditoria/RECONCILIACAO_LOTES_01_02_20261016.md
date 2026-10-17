# CF — reconciliação de lotes experimentais 01/02 (M07/M08/M10/M11; interface M14)

**Data:** 16/10/2026. **Objeto:** união documental das seis CF-NOR H já existentes, sem aprovação material, sem equivalência jurídica integral e sem modificação da Constituição vigente. A integração ocorre **somente na branch experimental do PR #139**, ainda draft. Base de trabalho: `main` `e968895556a9ba5276db63e94a6eeace5182a11c` (20 H); PR #138 SHA `25f74876ab9a15c7a1640a1b7f37afd7328f881f` e PR #139 SHA pré-união `1061fd15e7f62ce1168337456180ca48411265c2`. Preservar ambos como **pais Git** do commit de união. O resultado de CI do commit final deve ser registrado no PR, não presumido a partir do histórico.

## Escolha pelo ganho marginal global

**H horizontal:** seis direitos/funções de M07, M08, M10 e M11 presentes conjuntamente em um **checkout isolado**; M14 tem ficha de transição e não nova fonte normativa. A seleção agrega três H do lote01 e três H do lote02 aos 20 da main = **26 H somente na versão de trabalho deste PR**, não na main ou em nova Constituição.

**V vertical:** comparar interfaces, sem alterar mérito dos seis blocos textuais escolhidos. **I:** reduzir o número de frentes ativas e resolver colisão dos quatro arquivos compartilhados. **D:** registrar expressamente as questões **ainda não aptas a ratificação** e encaminhar revisão jurídica externa antes de estabilizar qualquer resultado.

**Alternativas rejeitadas:** merge automático dos dois PRs na main (revisão R3 ausente), importação integral da pilha de 56 H (alto risco de sobreposição), nova CF-NOR M14 sem decisão sobre a continuidade do ADCT, ou terceira pilha normativa autônoma.

## Proveniência preservada por blob

| ID | Módulo | Seleção canônica | História |
|---|---|---|---|
| CF-NOR-0021 | M07 | `b746d429429b55096a7688a32d3e035162eb93dc` | literal da ponta #137 |
| CF-NOR-0022 | M08 | `69ae9ef5157242bbac23071900f4a3a353823402` | variante H do #138, licitação; origem #137 `e9fc3027e79405057445d2f54816d6e20878a39f` |
| CF-NOR-0023 | M10 | `12a8f84c3e33538795582ec2daf720317bf878a5` | variante H do #138, EIA/fauna/crueldade; origem #137 `77e2ae31e54666fb093dede1a081c04020e9152e` |
| CF-NOR-0025 | M11 | `c6ff113dbfbb708e6279473ea631273ce7a2a389` | literal #137 |
| CF-NOR-0028 | M11 | `ac25d66f464eb0a13735e4ebf6ce55113df7210b` | literal #137; especialidade 0025 |
| CF-NOR-0029 | M11 | `4cbc9fae1db34f336f7198c61a3a78ee1b6a20ab` | variante H do #139, título particular legítimo e desapropriação; origem #137 `73e2bd038751a1b501297643779c74896b46b31d` |

Os textos normativos e blocos de vistas foram selecionados **sem nova reescrita**. Cada uma das três versões alteradas no lote continua H `auditoria_garantias=PENDENTE`. Os dossiês históricos dos lotes permanecem disponíveis e são partes da trilha.

## Reconciliação dos quatro arquivos comuns

1. `redacao/indice.csv`: 20 linhas originais da main idênticas às duas branches; somadas três linhas de cada lote; ordenação por campo `ordem`, CSV com aspas preservadas. Seis IDs adicionais e 26 ordens sem duplicação. **M07=1, M08=1, M10=1, M11=3**, M01=18, M04=1, M05=1.
2. `redacao/anteprojeto-de-trabalho.md`: 26 blocos canônicos já gerados de fontes das duas branches; 20 blocos compartilhados conferidos literalmente iguais. Ordenar por `ordem`, manter cabeçalho NÃO RATIFICADO e verificar pelo gerador original `--check` no SHA final.
3. `central/PAINEL_GERADO.csv`: estado previsto 26 H, nenhuma P/D, exclusivamente nesta branch; validação real pelo `controle_operacional.py --check`.
4. `.github/workflows/validar-estrutura.yml`: três suites legadas (18 testes) + guardas lote01 (7) + lote02 (9) + integradores (4). **38 testes previstos**, condicionados à execução no novo HEAD e sem provar conformidade jurídica.

## Matriz transversal jurídica — proteção, colisão e próximo teste

| Interseção | Invariante a proteger | Bloqueio R3 |
|---|---|---|
| M07↔M11 (CF5 XXXIV/LIV/LV, CF231–232) | petição e certidão gratuitas, devido processo, contraditório e tutela em procedimentos de demarcação/titulação | rito, prova, legitimidades, custos e órgãos M04/M06 |
| M08↔M10 (CF175, CF225) | delegação licitada não dispensa EIA prévio/publicidade nem deveres ambientais do prestador/poder concedente | responsabilidade/competências, tarifa, fiscalização e impactos |
| M10↔M11 (CF225, CF231, OIT169) | audiência ambiental geral e estudo de impacto não substituem consulta indígena especial quando devida | povo afetado, temporalidade, sobreposições territoriais e efeitos de consulta |
| M11 indígena↔quilombola (CF231 §6, ADCT68/ADI3239) | direito originário e nulidades indígenas não são nulidade automática de título particular legítimo quilombola | cadeia dominial, desapropriação, indenização, origem de recursos e remédios |
| M11↔M14 (ADCT68 e transição) | direito territorial quilombola, títulos e processos em curso não perdem eficácia por mudança editorial de localização | A/B/C não deliberadas, regras de ponte e repartição administrativa |
| M10↔cultura (CF225 §1 VII, §7, ADI5772/2026) | o registro cultural não elimina exigência concreta de bem-estar animal, fiscalização e responsabilização | manter, reformar ou retirar presunção cultural exige decisão, nunca efeito tácito de merge |

**Fontes e limites do cotejo:** [matriz R3 lote01](LOTE_01_M07_M08_M10_MATRIZ_R3_20261016.md), [matriz R3 lote02](LOTE_02_M11_ADCT68_R3_20261016.md), [ficha M14](M14_ADCT68_FICHA_TRANSICAO_20261016.md). Ali constam Constituição vigente, ADI5772/2026, Tema1031, ADC87, ADI3239, Lei 8.987 e Decreto4887/2003. A auditoria transversal **não** examinou integralmente essas fontes nem supõe encerramento de embargos. Nenhuma revisão humana independente foi identificada.

## Portas e destino

- **G1 PARCIAL:** conferência focal e proveniência da legislação/jurisprudência nas matrizes originais; atualizar efeitos de precedentes, indenizações, competências, financiamento, tratados, atos setoriais e ADCT quando a revisão se tornar decisória.
- **G2 histórico:** no SHA `246c9a122c420bb7165d976e9e1e601b26deeef9`, run [#38985545892](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/38985545892) concluído em sucesso com 38/38 testes, validador/gerador/painel aprovados. A variante M11 posterior demanda **novo run no novo SHA** com 40 testes esperados (38 + dois novos guardas), não se transfere o resultado do SHA anterior.
- **G3 R3 ABERTO/BLOQUEANTE:** sem revisão jurídica humana independente, sem mapa N:N global, sem decisão sobre extensão dos direitos indígenas/quilombolas, lei/licitação setorial, crueldade, tratamento de terceiros e transições.
- **G4 H SOMENTE:** nenhuma CF-DEC, F6, promoção a D, alteração da CF atual ou autorização de merge na main. O eventual fechamento administrativo do PR #138 como **superado por consolidação** não é aprovação normativa e não reduz a revisão R3 exigida no PR #139.

**Critério de parada:** depois da CI verde e da verificação de blobs dos dois pais, encerrar a duplicação técnica de PR #138, conservar **um PR #139 draft** de revisão conjunta, sem abrir terceiro stack. **FEITO:** matriz e regras de recomposição; **PENDENTE:** CI no próprio SHA, revisão humana independente R3 e escolha material futura; **PRÓXIMO:** auditoria externa focal, corrigir lacunas comprovadas e só depois avaliar integração H na main.


## Delta transversal R3 posterior à união — art. 20 XI (16/10/2026)

**Mudança delimitada:** CF-NOR-0025 H/M11 acrescentou §7 expressando **domínio da União sobre terras tradicionalmente ocupadas** (CF20 XI, STF Tema1031 XI), **sem reduzir posse permanente nem usufruto indígena**. Agora a matriz N:N desse artigo passa de remissão parcial para comando textual candidato, ainda sem equivalência demonstrada. A CF-NOR-0029 permanece intocada: propriedade quilombola não se converte em bem da União por essa previsão. O domínio público tampouco resolve os efeitos patrimoniais de terceiros tratados nos itens IV–VI da tese STF Tema1031, que permanecem G3/R3. [Auditoria detalhada do lote02](LOTE_02_M11_ADCT68_R3_20261016.md).

**Duas contraprovas documentais de regressão:** ausência de enunciado de domínio federal em 0025; aplicação de 'bens da União' à fonte 0029 ou perda da posse/uso exclusivo dos povos indígenas. CI detecta apenas a presença e o isolamento lexical, não a constitucionalidade material. **Porta G4:** zero decisões ratificadas; 26 H na branch, main original não alterada.
