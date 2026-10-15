# CF-CC-007 — Consolidação horizontal M12/M13 e vertical M06/M09

**Corte:** 15/10/2026. **Origem canônica:** `redacao/indice.csv` e `redacao/propostas/CF-NOR-####.md`; texto compilado `redacao/anteprojeto-de-trabalho.md` é derivado. **Main inalterada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`, 20 H. **Branch experimental:** `redacao/cfcc007-m12-m13-m06-m09-20261015`, herdeira da stack de #105 a #112, com **35 H em 11 módulos**. Nenhuma decisão D/F6 ou ratificação material.

## FEITO — quatro fontes H e duas frentes horizontais

| ID e tipo | Função constitucional explícita | Origem e prova ausente |
|---|---|---|
| **CF-NOR-0035 M12 A/H** | prova ilícita, integridade/rastreabilidade, contraditório técnico e distinção apreensão física/preservação/acesso | CF5 LVI/LV, [PR #82](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/82), Tema977. P4-E/P4-R **não escolhidas**; efeitos das irregularidades a auditar |
| **CF-NOR-0036 M13 A/H** | abertura de direitos a tratados e rito qualificado art5 §§2–3; publicidade de etapas como proposta H | CF5 §§2–3, CF49/84, [PR #98](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/98). OIT169 ≠ DL186/CDPD; controle processual pendente |
| **CF-NOR-0037 M06 E/H** | MS individual/coletivo, legitimidade, remédio urgente | CF5 LXIX–LXX, [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62), Lei12016. HD/ação popular/DP **não cobertos** |
| **CF-NOR-0038 M09 A/H** | salário mínimo nacional, reajuste, irredutibilidade, piso de variáveis, décimo terceiro | CF7 IV/VI–VIII, [PR #63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63), matriz 35 funções. Direito previdenciário e outras garantias não substituídos |

[**Matriz de 22 correspondências**](CF_CC_007_MATRIZ_22_CONTROLES.csv) evidencia estados `NUCLEO_EXPRESSO`, `PARCIAL`, `ALTERNATIVA_ABERTA` e `NAO_COBERTO`. A matriz não afirma equivalência material nem revogação de fontes.

## Distribuição de texto — não confundir unidades com cobertura jurídica

| Módulo | H acumuladas | Próxima lacuna essencial |
|---|---:|---|
| M00 | 0 | CF/ADCT N:N integral, reservas e fontes |
| M01 | 18 | privacidade/dados PR #59, outros direitos |
| M02 | 0 | anterioridade, voto/mandatos, consulta; pesquisa #95 |
| M03 | 0 | arquiteturas A/B/C, orçamento/investidura; pesquisa #107 |
| M04 | 1 | repartição de competências e custeio |
| M05 | 1 | regras orçamentárias e limites de gastos |
| M06 | 2 | HD, ação popular, tutela coletiva e assistência jurídica |
| M07 | 1 | ciência digital, devido processo, recursos especiais |
| M08 | 2 | estatais, regulação econômica e recursos |
| M09 | 3 | trabalho infantil, maternidade, FGTS, sindicatos |
| M10 | 2 | fauna, biomas, fiscalização e direitos especiais |
| M11 | 3 | nulidades patrimoniais, titulação e consulta |
| M12 | 1 | delimitação da exceção do Tema977, defesa e emergência |
| M13 | 1 | TPI, denúncia de tratados, vias convencionais |
| M14 | 0 | transição/mandatos, segurança jurídica e via de alteração |

**Total:** 35 H em 11/15 módulos; não há percentuais de direitos preservados certificados, zero ratificações D.

## Problemas não resolvidos deliberadamente

1. **M12 P4-E/P4-R:** o padrão comum L/I/C H não concede poder geral de acesso a celulares; a opção de constitucionalizar ou abolir a exceção identificadora do Tema977 é decisão material ainda em pauta. Exigir dados e exame de plantão, legitimidade, vítimas, terceiros e tempo.
2. **M13:** tratados de direitos humanos sem rito qualificado são objeto da orientação STF de supralegalidade, distinta da equivalência formal §3º; não converter posição do tratado em anulação automática de qualquer licença, lei ou norma individual. A consulta da OIT169 tem condições próprias de afetação e representação, diferentes de audiência geral.
3. **M06:** preservação de MS coletivo não equivale a suprir todos os remédios. Prazos de lei, inclusive 120 dias de MS, não foram constitucionalizados.
4. **M09:** direitos monetários têm incidências distintas no emprego, domésticos, aposentados e regimes estatutários; não transformar fórmula geral em revogação tácita das proteções e da EC72/2013.
5. **M03/M05/M07/CLF:** alternativas ORC-A/B/C não têm validação orçamentária real; T07/T43 exige prova de opção, envio, recebimento, leitura, ciência e prazo segundo normas vigentes. Não atribuir CLF DEC-016 à Constituição experimental.

## Qualidade e integração

As fontes 0035–0038 e o compilado exigem teste `python scripts/gerar_anteprojeto.py --check` e validator oficial antes de qualquer merge. O cotejo estrutural por leitura remota da branch controla IDs, tipos, status, links, marcadores e integridade do corpo das quatro novas fontes, **sem** afirmar execução local do Python. A CI GitHub Actions continua como bloqueio técnico a diagnosticar pelo run exato e logs de job/runner; ausência de incidente geral no GitHub Status não certifica causa específica.

**FEITO:** entrada M12/M13, duas cláusulas verticais e concordância 22 relações. **PENDENTE:** revisão jurídica independente e N:N completa, CI, conflitos de índice/vista com PR #59, M00/02/03/14 sem fonte normativa, custos, dados e consulta. **PRÓXIMO — CF-CC-008:** atacar o déficit horizontal com **M14 ou M00**, produzir conclusão de escopo sobre M02 conforme via autorizada, completar HD/ação popular M06 e direitos laborais M09, obter teste técnico oficial e fontes reais em duas rubricas fiscais e fluxo de ciência T07/T43. Sem ratificação por impulso.
