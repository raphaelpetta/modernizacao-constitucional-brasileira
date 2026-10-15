# CF-CC-004 — Auditoria N:N focalizada M11/M10 e condições de integração

**Data:** 15/10/2026. **Natureza:** auditoria textual de função, não certificação jurídica, revisão independente, prova empírica ou decisão F6/D. **Main de referência:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Branch experimental:** `redacao/cfcc004-m11-m10-garantias-20261015`, descendente de #109 na stack #105 → #106 → #108 → #109 → PR CF-CC-004. **Fonte nova:** CF-NOR-0025 (M11 H/A) e CF-NOR-0026 (M10 H/E ligada à CF-NOR-0023). **Pesquisa de origem:** [PR #94](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/94) M11-R1–R6 e [PR #89](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/89) M10-R9–R11, sem integração automática de suas conclusões.

## Produto — aumento de cobertura normativa

Na main: 20 H, módulos M01(18), M04(1), M05(1). Na branch acumulada desta rodada, após acréscimos: **26 H**, M01(18), M04(1), M05(1), M07(1), M08(2), M10(2), M11(1). **7/15 módulos têm ao menos uma ficha**, o que não equivale à cobertura material integral de módulo algum. M09 permanece para rotação horizontal seguinte. A vista derivada é `redacao/anteprojeto-de-trabalho.md`; fichas/índice são canônicos.

## Separação de sujeitos e procedimentos

1. **Indígenas**: direitos originários, terras de posse permanente, usufruto especial e legitimidade CF232, não domínio civil indistinto. O decreto de demarcação é declaratório; o art231 §5 remoção, §6 nulidade e §7 especialidade seguem pendentes.
2. **Quilombolas**: ADCT68 trata propriedade definitiva e titulação de remanescentes de quilombos; não aplicar automaticamente o regime de bem da União do art20 XI a esta titularidade. **SEM CF-NOR ainda**.
3. **Demais grupos tradicionais**: identificar titulares/campo da OIT169 e arts215–216, sem extensão cega dos arts231 ou ADCT68.
4. **Consulta anterior à medida**: Convenção169 nos pressupostos próprios, diferente da publicidade do EIA, audiência ambiental geral, manifestação de órgão administrativo e oitiva/autorização do Congresso na exploração mineral/hídrica de art231 §3. A ausência de prova de afetação requer instrução, não dispensa automática.
5. **Remédios**: CF232 participação judicial dos interessados com MP, distinta de monopólio de representação ministerial e das regras específicas de MI, ACP, ação popular, atuação DP e M06.

## Porta ambiental

CF-NOR-0026 contém três funções diferenciadas: espaço protegido (alteração/supressão por lei; atributos intangíveis), dever técnico de restaurar área de mineração e sanções penais/administrativas separadas da reparação. **Não afirma** cobertura de fauna, educação, substâncias de risco, biomas, reator nuclear, regras tributárias especiais, ação popular ambiental/ACP nem proteção indígena. O direito ao meio ambiente (0023) e esta especialidade (0026) não substituem todo art225.

[**Matriz focal de 16 controles**](CF_CC_004_MATRIZ_16_CONTROLES.csv) diferencia `NUCLEO_EXPRESSO_NAO_EQUIVALENTE`, `PARCIAL` e `NAO_COBERTO`. O rótulo `CRITICO` é risco operacional de supressão silenciosa em futura Constituição, não constatação de regressão no direito vigente.

## Testes e bloqueios

- **T-01** demarcação incompleta → não extingue direito indígena; medir prova e dever de proteção.
- **T-02** remoção contra vontade do povo → SEM regra específica nesta H; exige cláusula do art231 §5 antes de versão de substituição.
- **T-03** autorização de mineração sem ouvir afetados → §5 de 0025 tem requisitos, mas regime da lei e eficácia dos procedimentos precisam revisão.
- **T-04** concessão/licença em zona contígua com impacto direto → consulta segundo afetação, não exclusão por fronteira cartográfica.
- **T-05** audiência única por todos os povos → não satisfaz por si procedimentos e representações próprios.
- **T-06** posse quilombola tratada como terra indígena → não coberto e juridicamente inadequado.
- **T-07** unidade de conservação suprimida por decreto → 0026 vedação expressa, salvo análise de norma aplicável específica.
- **T-08** mineradora paga multa sem restaurar área → 0026 separa reparação e sanção.
- **T-09** animal submetido a crueldade apesar de proteção ambiental geral → regra especial permanece sem texto.
- **T-10** bioma de patrimônio nacional eliminado por silêncio → exigência de destino do art225 §4 pendente.

Cenários hipotéticos aplicados como leitura literal; **não são casos julgados ou testados empiricamente**.

## Integração e próximos passos

**FEITO:** 2 fichas H, índice/vista, vínculo especial com 0023 e matriz de 16 proteções; reuso dos acervos #89/#94; texto deixa explícitas reservas críticas. **PENDENTE:** direito quilombola ADCT68, remoção/nulidades indígenas, fauna/crueldade, biomas e regras ambientais especiais, MP/M06, recepção/consulta M13, validação de compatibilidade com jurisprudência e tratados, indicadores reais e CI remoto. **PRÓXIMO:** redação de duas especialidades de maior risco M11 (art231 §§5–7 e ADCT68 em unidades separadas); rotação a M09 para trabalhos sociais e exame do M03/CLF de orçamento e processos digitais. Nenhuma D nem merge autorizados.
