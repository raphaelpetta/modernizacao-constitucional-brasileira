# CF-CC-006 — Auditoria de remédios e jornada especial, cobertura modular e CI

**Corte:** 15/10/2026. **PR:** draft #112 empilhado sobre #111, este por #110/#109/#108/#106/#105; **main** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`, 20 H. **Produto H da branch:** 31 entradas e 31 seções em 9 módulos. **Classificação:** documento de concordância PARCIAL e rastreabilidade, não parecer independente conclusivo, equivalência, decisão F6/D ou autorização de merge.

## FEITO

1. **M06 inaugurado normativamente:** [CF-NOR-0033](../redacao/propostas/CF-NOR-0033.md) H/E ligada à regra geral CF-NOR-0007: habeas corpus preventivo/repressivo e gratuito, mandado de injunção por omissão regulamentadora impeditiva. Pesquisa de origem PR #62. **Mantém lacunas expressas** MS individual/coletivo, HD e gratuidade, ação popular, assistência jurídica e detalhes de MI coletivo.
2. **M09 especializado:** [CF-NOR-0034](../redacao/propostas/CF-NOR-0034.md) H/E ligada à CF-NOR-0027, assegura jornada de seis horas nos turnos ininterruptos de revezamento, salvo negociação coletiva, sem presunção de que acordo possa abolir direitos indisponíveis. Origem PR #63.
3. **Regra de reservas:** PR #59 mantém 0030/0031 em versão independente. **0032 não criado** neste recorte; nenhuma suposição de que pertence à main. Nenhuma alteração textual de M01/PR59.
4. **Matriz focal** [15 destinos positivos e negativos](CF_CC_006_MATRIZ_15_CONTROLES.csv), com proteção vigente, texto experimental e risco residual. Critérios do sistema de compilação documentados: IDs/ordens únicos, 31 blocos, especialidades com referência/justificativa, estados todos H.

## Diagnóstico horizontal atualizado

| Módulo | Quantidade H na branch | Status de cobertura material |
|---|---:|---|
| M00 | 0 | governança/índice, fontes e decisões ainda sem cláusula |
| M01 | 18 | outros direitos e PR #59 dados ainda pendentes |
| M02 | 0 | pesquisa no PR #95; **sem texto canônico integrado** |
| M03 | 0 | 16 protótipos A/B/C e estudos ORC/INV no PR #107, não adotados |
| M04 | 1 | competência e finanças federativas sem mapa exaustivo |
| M05 | 1 | custeio e orçamento transitório sem solução normativa |
| M06 | 1 | remédios HC/MI, outros instrumentos pendentes |
| M07 | 1 | administração digital/procedimento com especialidades pendentes |
| M08 | 2 | economia/serviços sem regimes estatais integrais |
| M09 | 2 | jornada geral + revezamento, maioria art7 e sindicato pendente |
| M10 | 2 | EIA e especialidade espacial/mineral/danos, fauna e biomas pendentes |
| M11 | 3 | território indígena/quilombola, terceiros e efeitos incompletos |
| M12 | 0 | pesquisa segurança/tecnologia sem unidade integrada |
| M13 | 0 | tratados e hierarquia sem unidade integrada |
| M14 | 0 | transição/mandatos sem unidade integrada |

**Soma:** 31 H em 9/15 módulos; zero D. Cobertura quantitativa por ficha é só contagem de produto, não denominador de direitos reconstruídos.

## QA documental e bloqueio remoto

Read-back no GitHub: 31 entradas CSV válidas, 31 seções, IDs e ordens sem repetição, 15 controles na matriz, fonte NORMA de 0033/0034 reproduzida exatamente nas respectivas seções, especialidades E com regra geral e justificativa. **Não rodamos** localmente `python scripts/gerar_anteprojeto.py --check` nem os testes unitários Python.

CI do PR #112, [run 38731440833](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/actions/runs/38731440833), `completed/failure`, job `arquivos-e-modulos` retornado com `steps=null`; no mesmo dia outras branches tiveram sintoma semelhante. **Causa não demonstrada**. A [página oficial de status](https://www.githubstatus.com/) informa ausência de incidente geral em 15/10/2026; o registro de 13/10 relativo a logs informa que os workflows efetivamente executados não foram afetados por aquele incidente. Assim, **não justificar o CI por outage comprovada nem por erro de norma sem provas**. Próxima revisão técnica precisa de anotação e logs do job/runners ou teste independente do mesmo SHA.

## PENDENTE e próxima fila

- M02 ainda sem norma no corpus; prova e discussão eleitoral no PR #95, revisão M06/M14 e rito autorizado necessários. Sem classificação de texto bloqueado como “entrega”.
- M06: mandado de segurança, habeas data, ação popular, assistência jurídica, tutela coletiva e execução.
- M09: proteção salarial, maternidade, dispensa, FGTS, trabalho infantil, risco/automação e organização sindical/greve, sem retrocesso por resumo.
- M03/M05: discriminar rubricas, fontes, dotações, caixa e regras ORC sem LOA antes de elevar norma; PR #107 contém a matriz de 12 rubricas desta rodada.
- Qualidade: testes oficiais e CI, auditoria CF/ADCT N:N e revisão jurídica independente, integração com o PR #59.

**FEITO:** duas normas H, nova cobertura M06 e especialidade M09, controle por origem/destino. **PENDENTE:** qualidade remota e recortes restantes. **PRÓXIMO:** horizontal M12/M13 ou M02 por interface permitida, vertical M06/M09, auditoria M03/M05 e CI antes de merge; nenhuma decisão material por impulso.
