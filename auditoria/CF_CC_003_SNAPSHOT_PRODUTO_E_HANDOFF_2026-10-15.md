# CF-CC-003 — snapshot verificável da minuta e integração M03/M07/M08/M10

**Corte:** 15/10/2026. **Main CF:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`, com **20 H** (M01=18, M04=1, M05=1) antes dos merges. **Esta branch é draft**, dependente da stack #105 → #106 → #108 → #109. **Estado aqui:** 24 H (M01=18, M04=1, M05=1, M07=1, M08=2, M10=1), distribuídas por seis dos quinze módulos. Números são **dispositivos indexados**, NÃO completude do direito vigente, ratificação, nem unidades únicas adicionáveis entre PRs sobrepostos.

## FEITO efetivo na rodada

| Frente | PR/branch e artefato | Resultado |
|---|---|---|
| M10 horizontal | [#108](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/108), `redacao/propostas/CF-NOR-0023.md`, `modulos/M10-ambiente-clima/M10_CC003_INTEGRACAO_NUCLEO_AB_v0.1.md` | Núcleo H/A ambiental com dever intergeracional e EIA prévio/publicidade; extraído do PR pesquisa #89, sem escolher arquitetura A/B |
| M08.02 vertical | [#109](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/109), `redacao/propostas/CF-NOR-0024.md`, `modulos/M08-ordem-economica/M08-02_PRINCIPIOS_E_CONCORRENCIA_v0.1.md` | Núcleo H/G do art.170 e repressão concorrencial; arts.173–174, ambiente diferenciado, pequena empresa e propriedade especial pendentes |
| M07 auditoria/revisão | [#105](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/105), `redacao/propostas/CF-NOR-0021.md` | Inserida em H a garantia de **petição e certidões sem taxas**, enfrentando lacuna do teste T06. O diagnóstico anterior é preservado como histórico, não auditoria homologada |
| M03 integração crítica | [#107](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/107), `modulos/M03-parlamento/M03_CC003_TESTES_FISCAIS_JUDICIAIS_E_M07_v0.1.md` | Quatro casos aplicados A/B/C (LOA, investidura, defesa, transição digital), com três invariantes normativas propostas fora de CF-NOR e sem F6/D |
| Integridade de branches | commits sintéticos de reconciliação **sem alterar árvores normativas** em #106/#108/#109 | Recuperada relação de ancestralidade entre branches: PR #106 só delta M08.01 (5 arquivos), #108 só delta M10 (4), #109 só delta M08.02 (4 antes deste snapshot). **Sem merge na main** |

## Regras e decisões preservadas

- As fichas canônicas estão em `redacao/propostas/`, apontadas por `redacao/indice.csv`; a vista `redacao/anteprojeto-de-trabalho.md` é produto derivado, não fonte editável autônoma. CF-NOR-0021/22/23/24 permanecem **H**, sem migração para D.
- A escrita de uma H com texto semelhante à CF não demonstra preservação da integralidade de art.5 XXXIV, art.170 e art.225, tampouco auditoria da ADCT e direitos especiais. **Riscos materiais ficam expressos no arquivo-fonte**, não escondidos do usuário.
- No M10, direitos e deveres especiais do art.225 (§1 III e V–VIII, §§2–7), consulta, ação popular/ACP e regras de competência exigem cláusulas específicas e controle N:N. EIA com significativa degradação, prévio e público, consta no núcleo H.
- No M08, art.170 VI inclui tratamento diferenciado segundo impacto ambiental; estatais, recursos, exploração econômica, propriedade urbana/rural e concessões não foram consideradas cobertas.
- No M07, a nova frase de gratuidade é hipótese textual; efeitos jurisdicionais, prazo, defesa, via administrativa, competência e custos ainda precisam de verificação.
- No M03, nenhuma prioridade técnica P-B resolve por si orçamento sem LOA, substituição de gabinete ou defesa. A/B/C e S1/C3 permanecem opções, sem escolha F6. Não registrar CF-DEC material com base em 'a' (impulso operacional).
- No CLF, DEC-016 não é decidida aqui; o corpus legislativo e a Constituição experimental possuem autonomia e apenas interfaces de competência, procedimento, serviço, reparação, sanções e transição.

## QA documental e CI

**Read-back de GitHub:** última branch #109, `redacao/indice.csv` com 24 dados e vista com 24 blocos; fonte NORMA de 0021/22/23/24 localizada no texto compilado; IDs/ordens e status verificados no recorte. O teste interno não cobre revisão semântica dos 20 textos iniciais. **Não alegar que o script oficial foi executado**, nem que toda norma vigente está validada.

**GitHub Actions:** verificar o workflow após os HEADs finais; os PRs da rodada anterior apresentaram falhas rápidas sem etapas ou logs de job disponíveis, e não foi comprovada causa técnica. Status `failure` nunca equivale a reprovação jurídica; CI `success` tampouco equivale a homologação.

## PENDENTE — portas de qualidade e integração

1. **Revisão humana jurídica independente** M07/M08/M10 e concordância CF/1988/ADCT N:N, com riscos de direitos de indígenas, animais, serviços essenciais, propriedade e contrato.
2. **M03 decisão estruturante:** via constitucional (PEC/constituinte), voto direto, governo/interregno, orçamento, comando civil, revisão M02/M05/M06/M12/M14, mais teste de contramodelos S1/C3 quando houver valor discriminante.
3. **Integração técnica:** PR #59 (CF-NOR-0030/0031) edita índice/vista e requer reconciliação com stack de 21–24 H; PRs #101/#104 são governança em draft, exigem revisão antes do merge. **Nenhum merge normativo sem autorização material.**
4. **CI remoto:** causa de falhas ainda não verificada com evidência suficiente e testes Python oficiais pendentes.

## PRÓXIMO — fila dinâmica com três caminhos independentes

1. **Cobertura horizontal:** M09 (direitos sociais/garantias laborais e proteção quantitativa art.7) ou M11 (direitos originários/consulta), conforme função menos representada e estado probatório; produzir H com controle de supressões.
2. **Vertical:** M10 especialidades art.225 (áreas protegidas, reparação/sanções, fauna), ou M08.03 regimes de estatais/planejamento, conforme pesquisa disponível e risco; não fingir completude com 24 H.
3. **Integração/qualidade:** M03 mecanismos de orçamento transitório, confiança e competência de defesa, em confronto A/B/C e contraprovas; M07 contraditório, intimação e CLF T07/T43; diagnóstico CI para permitir revisão de PRs.

**FEITO/PENDENTE/PRÓXIMO deste arquivo são fotografia versionada**, não procedimento de aprovação de cláusulas. GitHub [central #103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103) e [central CLF #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48) recebem handoff, sem importar decisões.
