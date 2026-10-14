# M11.01-R3 — Pacote de continuidade (FEITO / PENDENTE / PRÓXIMO)

**ID:** CF-M11.01-S003 · **Corte:** 14/10/2026 · **Issue:** [#92](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/92) · **PR:** [#94](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/94), draft.  
**Branch:** `pesquisa/m11-01-direitos-originarios-20261014` · **Main no preflight:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` · **HEAD do PR na abertura R3:** `92a24a4f5b2562757841b18522a3056a271d56a4`.  
**Estado:** pesquisa F1–F5, não deliberação F6/D ou redação F7/CF-NOR; **sem alteração de `redacao/`, índice, `main` ou CLF**.

## FEITO

| Artefato R3 | Conteúdo novo e verificável | Limite |
|---|---|---|
| `M11-01_R3_PARECER_INCIDENCIA_MEDIDAS_TERRITORIOS_v0.1.md` | Parecer de incidência com **seis perguntas discriminantes**, distinção de ADI7008, OIT169, LAE e autoridade interveniente, controle de tempo sem prazo fictício | Não é exame empírico de caso real nem parecer de hierarquia M13 |
| `M11-01_R3_MATRIZ_NOVE_HIPOTESES_MEDIDA_AFETACAO.csv` | **9 testes:** `3 atos` (lei, concessão, LAE) × `3 situações` (dentro, contígua diretamente afetada, fora com afetação não demonstrada), cada um com fonte, fatos, prova, ator, tempo, resultado condicionado e objeção | Cenários **hipotéticos**, sem presunção de consulta/dispensa para casos reais |
| `M11-01_R3_TRILHA_DOCUMENTAL_CONSULTA.csv` | **7 etapas de controle** — ato, sujeitos, afetação, representantes, consulta prévia, motivação, fatos novos | Não cria prazo de 30/45/90 dias nem rito universal |
| `M11-01_R3_COMPLEMENTO_F05_M10_v0.1.md` | Novo complemento **parcial** da F05 do M10, com discriminação de alcance de A-11/B-04/B-10 e das lacunas de CF231/232/ADCT68 | M13 e M06 permanecem abertas; não ratifica esboços A/B |
| Este pacote | Registro de estado, dependências, próxima frente e QA a conferir | Não autoriza merge |

**Pontos jurídico-probatórios confirmados:**

- **ADI7008/SP, Plenário 12–19/05/2023**, [decisão oficial](https://portal.stf.jus.br/processos/detalhe.asp?incidente=6270590): exclusão de terra tradicional do objeto de concessão da Lei paulista 16.260/2016; consulta prévia às comunidades de **zona contígua diretamente afetada**; legislação ambiental preservada. **Não** é veto judicial geral a qualquer contrato de qualquer lei.
- **Convenção169 OIT, art.6**, [Decreto10088 AnexoLXXII](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10088.htm): medidas legislativas e administrativas **suscetíveis** de afetar diretamente, por instituições representativas. Afetação direta não exige lesão já consumada; tampouco a distância ou contiguidade resolve sozinha.
- **[Lei15300/2025 art4§2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm):** audiência obrigatória da LAE e consulta devida não se substituem; **[Lei15190 arts42–45](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm)** participação de autoridades envolvidas é distinta e seus gatilhos legais não definem sozinhos direito originário.
- **[Funai — apoio a protocolos próprios](https://www.gov.br/pt-br/servicos/solicitar-apoio-a-processos-de-construcao-de-protocolos-e-outros-instrumentos-de-consulta-livre-previa-e-informada):** consulta não é simples participação cidadã; representação, idioma, oportunidade e registro da deliberação dependem de características dos povos.

**Limitação de método:** 'dentro' na matriz R3 descreve **incidência material no povo**, não só um polígono; 'contígua' pressupõe impacto direto narrado; 'fora' significa **sem afetação demonstrada na instrução disponível**, não inexistência provada de efeito. Sem essa diferenciação, classificação automática consulta/dispensa seria falsa.

## PENDENTE

1. **M13.01 [#93](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/93):** hierarquia/aprovação/incorporação do tratado OIT169 e relação com instrumentos internacionais. Nenhum PR M13 específico constou da busca de preflight da R3. **Não atribuir parecer à M13**.
2. **M06/M01:** titularidade e tutela CF232, ACP, popular, competência, prova, execução e relação com audiência judicial de conflitos.
3. **M04/M07/M10/M08:** definição administrativa do licenciador, concessionário/órgãos, estudos ambientais, bens/recursos naturais e resposta jurídica à afetação contígua; ação judicial da ADI7008 tem objeto específico.
4. **Casos concretos:** falta informação empírica sobre perímetro, localização real, protocolos de consulta, representação, impactos socioculturais e controvérsia; simulações não satisfazem prova pericial.
5. **STF:** eventuais embargos pendentes Tema1031/ADC87 e causas de licenciamento 2025 requerem atualização de atos decisórios por fonte processual, não dedução a partir de pautas.
6. **F6/F7:** nenhuma decisão normativa nem texto constitucional M11 integrado; não há prova de equivalência ou regressão material de anteprojeto real.
7. **Fechamento técnico:** ler arquivos da branch, conferir nove casos + sete etapas + referências A/B, publicar progresso no PR94/issue #92 e adendo ao M10 #88; verificar CI no HEAD e `main` após último commit.

## RESULTADO ATUAL

| Registro | Estado |
|---|---|
| M11.01 | Pesquisa H/V R1–R3; R3 com 9 casos e 7 etapas |
| M10 F05 | `PARECER_M11_PARCIAL_R3` (agora específico a tipo de ato e afetação); **M13/M06 pendentes** |
| M13.01 | F0 aberta issue #93, sem parecer hierárquico atribuído nesta rodada |
| Texto M10 A/B | Experimental, sem norma de povos integrada nem ratificação |
| `main`, CLF, `redacao/` | Sem escrita |
| PR94 | Draft, CI do HEAD final a conferir |

## PRÓXIMO — M11.01-R4 (somente avanço material)

Escolher **um núcleo probatório delimitado**, em vez de fazer nova matriz geral: **recursos naturais em terra indígena** (CF231 §3 e CF49 XVI, autorização parlamentar + oitiva + relação com OIT169 art15) **ou** **legitimidade especial CF232 e proteção coletiva** (art232, MP, ACP, tutela, mediação possessória CPC565), com caso de teste completo e confronto ao texto ambiental M10. Registrar o impacto de eventual parecer M13 quando realmente publicado. Não selecionar constitucionalmente uma arquitetura A/B ou converter estudo em `CF-NOR` sem deliberação própria.

**QA:** a validação de integridade dos arquivos/CI mede estrutura, não prova compatibilidade constitucional nem a ocorrência de consulta real.
