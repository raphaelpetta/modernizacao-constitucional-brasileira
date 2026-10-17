# CF-CC-003 — aplicação crítica fiscal, judicial e administrativa aos pacotes M03 A/B/C

**Corte:** 15/10/2026. **Fonte:** [protótipos M03 CF-CC-002 no PR #107](M03_CC002_PROTOTIPOS_CONSTITUCIONAIS_A_B_C_v0.1.md), [9 testes existentes](M03_CC002_NOVE_TESTES_PACOTES_A_B_C.csv), agenda A/B/C [PR #99](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/99), contraprovas adicionais [PR #100](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/100). **Interface formal:** M07 [PR #105](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/105) (garantias administrativas) e M08 [PR #106](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/106) (serviços). **Estados:** H/P/A/V, nenhum F6/D, sem inferir CI aprovado.

## Quatro cenários adversariais — julgamento textual do que já foi escrito

| Cenário | A: presidencialismo reformado | B: parlamentarismo racionalizado | C: premier-presidencialismo | Resultado |
|---|---|---|---|---|
| **S01 — Câmara rejeita LOA por dois anos** | A-05 remete à continuidade de obrigações, mas não especifica dotação, extensão temporal nem aprovação de créditos | B-05 permite medidas conservatórias, sem definir quais gastos exigem novo título legal; censura construtiva pode manter gabinete sem maioria | C-04 veda dissolução automática e poder orçamentário presidencial, mas não descreve solução para empate | **LACUNA em A/B/C**; sem autorização legal não há poder de despesa novo. M05 deve redigir cláusula de transição orçamentária, sujeitos e controle |
| **S02 — Chefe de Estado recusa nomeação do premier investido** | A não tem primeiro-ministro parlamentar sujeito a investidura; fiscalização de nomeações segue separada | B-01/B-03 dizem ato vinculado e vedam veto político, mas não trazem prazo, suplência e execução jurisdicional | C-01/C-02 exigem investidura e proíbem exoneração livre, sem dizer se investidura também vincula formalmente Presidente | **B parcial / C lacuna**: exigir ato vinculado, prazo e remédio sem juiz escolher maioria |
| **S03 — Presidente e gabinete dão ordens militares contraditórias em crise** | A mantém único chefe eleito, mas legislação militar e limites de emergência não foram escritos | B-06 indica cadeia civil governamental única, sem designar responsabilidade constitucional completa por ato | C-03/C-04 proíbem poderes presidenciais implícitos, mas lista de atos presidenciais e referenda continua em branco | **R3 geral; C maior porta específica**: titular material, formal, referenda, delegação e controle M12/M06 |
| **S04 — Troca de Governo e falha do sistema digital impedem petições e serviços essenciais** | A-02 dirige ministros, não garante expressamente responsabilidade pela continuidade e acesso durante troca de gabinete | B-05 mantém atos ordinários, mas não define quem mantém canais alternativos/aceita petições sob transição | C-04 declara continuidade sem distribuir operação a cada autoridade responsável | **LACUNA comum**: vincular INVARIANTE M07 sem transformar direitos subjetivos em poderes fiscais ou militares extraordinários |

O teste é **lógico-textual**, sem fatos brasileiros simulados, sem estimar causalidade, custo fiscal ou viabilidade de PEC. O modelo B permanece P de prioridade técnica para redação comparável, não recomendação imutável nem D; A preserva força de contraprova, C tem condição adicional de responsabilização dual.

## Protótipos de correção invariantes (apenas propostas redacionais; NÃO CF-NOR)

**INV-M03-08 — Continuidade de direitos e serviços.** “A sucessão, vacância, substituição ou funcionamento interino do Governo não suspendem os direitos fundamentais, a proteção dos usuários de serviços públicos, os deveres legais de atendimento e resposta administrativa nem a sujeição dos agentes à fiscalização e à responsabilidade. A lei definirá a cadeia administrativa de execução, preservadas as competências dos entes federativos.” **Ressalva:** esse dever não cria crédito financeiro, ordem militar ou poder normativo material por urgência.

**INV-M03-09 — Despesa e impasse parlamentar.** “A ausência ou a rejeição de lei orçamentária não autorizam o Poder Executivo a criar despesa, crédito, tributo ou dívida por ato próprio. A continuidade das despesas legalmente autorizadas observará limites, fontes, condições e controles previamente estabelecidos por esta Constituição e por lei.” **Ressalva:** precisa de catálogo de direitos exigíveis e disciplina de transição M05; não afirmar que texto é suficiente para crise de dois anos.

**INV-M03-10 — Atos de investidura.** “Quando a Constituição vincular a nomeação de autoridade governamental a uma deliberação válida da Câmara, a autoridade nomeante praticará o ato formal nos termos e prazos constitucionalmente estabelecidos, sem discricionariedade política adicional, assegurado controle jurisdicional do procedimento.” **Ressalva:** não estende isso a nomeações discricionárias de A; não autoriza Judiciário a formar maioria ou escolher dirigente.

## Portas de invalidação antes de selecionar arquitetura

1. **Fisco:** simular dois exercícios consecutivos sem LOA, discriminando despesa previamente autorizada, nova obrigação, dívida, despesa constitucional exigível e repasse federativo; fundamento jurídico por rubrica (M05).
2. **Eleição:** validar constitucionalmente forma de investidura/dissolução, proteção ao voto direto art.60 §4º II, eleições e art.16 (M02/M14).
3. **Justiça:** identificar legitimados, objeto da tutela e efeito de decisão sem eleição judicial de chefe de Governo (M06).
4. **Administração:** pessoa com deficiência ou sem conectividade durante crise institucional deve conseguir peticionar e obter decisão; a CF-NOR-0021 H já contém acesso, canais e gratuidade, mas sua eficácia administrativa depende do corpus CLF T07/T43, sem importar regra setorial automaticamente.
5. **Defesa:** indicação inequívoca de titular, referenda e controle dos atos materiais de comando e urgência (M12).
6. **Anticaptura:** o uso de voto de confiança/dissolução como blindagem de investigações deve reprovar o modelo; A também exige controle de nomeações, orçamento e poder de agenda.

## Interface M07 + CLF

CF-NOR-0021 (H, PR #105) passou a enunciar **independência de taxas para petições/certidões** em rodada posterior ao diagnóstico original. Isso não ratifica o conteúdo, não comprova N:N completa, nem atribui competência processual uniforme à Lei 9.784/1999; CLF pode detalhar intimação e atendimento digital conforme incidência e especialidades. A CLF central #48 deve receber apenas pedido de verificação operacional específico e não decisão sobre arquitetura de Governo, vigência ou DEC-016.

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** quatro cenários aplicados ao texto A/B/C, identificação de lacunas por modelo, três invariantes corretivas explicitamente não normativas, portas de prova M02/M05/M06/M07/M12/M14 e interface CLF. **PENDENTE:** casos fiscais reais, custo, reforma constitucional, revisão adversarial humana, correções legislativas setoriais e deliberação material específica. **PRÓXIMO:** produção de artigos constitucionais completos de orçamento transitório e competência de nomeação para comparação, sem CF-DEC e sem aprovar B por silêncio; explorar contrafactuais S1/C3 apenas se alterarem classificação de risco.
