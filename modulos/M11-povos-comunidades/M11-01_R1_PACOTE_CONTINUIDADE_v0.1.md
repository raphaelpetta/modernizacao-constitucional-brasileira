# M11.01-R1 — Pacote de continuidade (FEITO / PENDENTE / PRÓXIMO)

**Sessão:** CF-M11.01-S001 · **Corte:** 14/10/2026 · **Issue M11:** [#92](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/92) · **M13.01:** [#93](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/93) · **Origem de interface:** [M10.01 #88 / PR89](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/89).  
**Main no preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Branch própria:** `pesquisa/m11-01-direitos-originarios-20261014`, criada **a partir daquele SHA**, não derivada da branch da M10.  
**Estado:** pesquisa jurídica F1–F5 inicial e parcial, sem decisões materiais F6/D, redação F7/CF-NOR, IDs normativos ou atualização CLF. Nenhum texto da M10 foi editado.

## FEITO

| Entrega | Conteúdo/prova | Limite |
|---|---|---|
| `M11-01_R1_DOSSIE_DIREITOS_ORIGINARIOS_E_CONSULTA_v0.1.md` | Leitura sistemática CF231/232, ADCT68, regimes indígenas e quilombolas, OIT169 arts1/6/7/15, Lei15300 art4§2 e Lei15190 arts42–45; STF Tema1031, ADI3239 e Lei14701 julgada parcialmente em 2025 | Recorte jurídico, sem avaliação empírica e sem hierarquia convencional aprovada |
| `M11-01_R1_MATRIZ_DIREITOS_TITULARES_CONSULTA.csv` | **24 funções** com titular, devedor, norma, remissão R9 A/B e lacuna jurídica | Presença de remissão não prova equivalência |
| `M11-01_R1_TESTES_CASOS_TERRITORIO_CONSULTA.csv` | **12 cenários fictícios** de demarcação, propriedade quilombola, audiência/consulta, órgão envolvido, usina, isolados, remoção, legitimidade, conservação, Lei14701 e representação | Não são fatos ocorridos nem predições judiciais |
| `M11-01_R1_PARECER_INTERFACE_F05_M10_v0.1.md` | Parecer técnico **parcial**, de M11 para F05 de M10: o que A-TEXTO-11/B-TEXTO-04/10 mencionam e o que não preservam literal ou funcionalmente | Depende de M13 e M06; não ratifica redação M10 |
| Este pacote | Estado factual e próximos atos | PR e CI ainda sujeitos ao fechamento |

**Achado especialmente verificável:** [Tema1031](https://portal.stf.jus.br/jurisprudenciarepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=5109720&numeroProcesso=1017365&numeroTema=1031) reconhece demarcação **declaratória** e ausência de marco temporal geral 05/10/1988; [ADI3239](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=3239) confirma Decreto4887, autoatribuição e disciplina quilombola; [ADC87/ADIs7582/7583/7586, mérito em dezembro/2025](https://noticias.stf.jus.br/postsnoticias/stf-considera-inconstitucional-trecho-de-lei-que-institui-marco-temporal-para-terras-indigenas/) declarou inconstitucionalidade parcial da Lei14701, não total. **Embargos 2026** com suspensões em junho/setembro verificados em registros oficiais; resultado final dos embargos **não certificado**. Há referências a páginas STF que, na abertura direta, retornaram HTTP403; interpretar apenas as informações oficiais indexadas efetivamente acessadas.

**Distinções materiais:** CF231/232 direito originário indígena com posse/usufruto e capacidade judicial; ADCT68 propriedade definitiva quilombola (método e título próprios); cultura 215–216; OIT169 consulta por povos diretamente afetados. Lei15300 art4 §2 exclui substituição da consulta específica pela audiência LAE; Lei15190 participação de órgão interveniente é distinta de consulta pelo povo. **Não presumir veto geral**, nem declarar que homologação administrativa cria direito originário.

## PENDENTE

1. **M13.01 #93:** parecer sobre aprovação, ratificação, promulgação, hierarquia e eficácia da OIT169; o dossiê M11 não encerra a tese de hierarquia dos tratados, nem os efeitos de todos os tratados.
2. **M06/M01:** legitimidade de CF232 e eventual sobreposição com ACP, ação popular, tutela de urgência, custos e execução em texto constitucional futuro.
3. **M04/M08:** competências de bens públicos, títulos, desapropriação, exploração de recursos, unidades de conservação e reservas de lei.
4. **M10.01:** juízo integrado de EIA/LAE e de novo texto A/B. O parecer M11 responde F05 **parcialmente**, sem dar chancela às duas arquiteturas e sem criar norma.
5. **Decisões STF:** verificar ulterior movimentação dos embargos ADC87/ADIs7582/7583/7586 e RE1017365 para atualizar efeitos; não há certidão conclusiva nesta R1.
6. **Pesquisa de campo/provas:** protocolos próprios de consulta, identificação de representação, diferentes sujeitos tradicionais, impactos e dados técnicos de áreas carecem de instrução específica e consentimento quando juridicamente necessário.
7. **G3/G4:** nenhuma deliberação F6, CF-NOR M11 ou prova de equivalência de redação canônica.
8. **Git QA final:** criar PR draft a partir da branch própria, vincular issue #92 e M10 #88 por comentários, conferir HEAD/CI, `main` e arquivos após o último commit.

## PRÓXIMO — M11.01-R2

**Delimitação:** aprofundar **legitimidade e prova** nos conflitos entre terras indígenas não homologadas, sobreposição de unidades de conservação, direitos quilombolas titulados/não titulados e consulta incidente sobre medidas legislativas/administrativas; usar os 12 casos R1 para testar **meios concretos de investigação, prova antropológica, proteção judicial e participação**. Incorporar eventual resposta M13 sobre a OIT169 *somente se existir documento/commit efetivo*. Ao lado do dossiê, organizar matriz de controvérsias decisórias do STF com data/dispositivo e ressalva sobre embargos. Não iniciar CF-NOR ou escolher arquitetura M10.

**Saída esperada:** testes com prova/ônus/campo de aplicação, resposta atualizada ao M10 quando juridicamente justificada e FEITO/PENDENTE/PRÓXIMO; sem repetir catálogo por volume.

## Integridade

| Item | Estado |
|---|---|
| Issue #92 | F0 própria, aberta |
| Pesquisa M11 | F1–F5 parciais, 24 funções, 12 casos, parecer F05 parcial |
| M13 #93 | Dependência de hierarquia, **sem resposta presumida** |
| M10 F05 | Parecer produzido por M11; registrar recebimento em M10 **quando o link for publicado** |
| CF-DEC/F6 | Nenhuma D criada ou inferida |
| CF-NOR/F7 e índice | Nenhuma ficha nem número reservado |
| `main`, `redacao/`, CLF | Sem escrita nesta R1 |
| CI | Estrutural, conferir no HEAD final após PR; não é decisão sobre constitucionalidade |
