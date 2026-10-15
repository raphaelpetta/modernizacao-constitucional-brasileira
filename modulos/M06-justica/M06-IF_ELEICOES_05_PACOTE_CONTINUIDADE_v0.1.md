# M06-IF-ELEI-005 — Continuidade (14/10/2026)

**Responsável M06 issue #55; PR #96 draft; branch pesquisa/m06-interface-controle-eleitoral-20261014.** Interfaces M02 PR95, M03 PR85, M14 PR91, coordenação PR97, todas em pesquisa e fora da main. Estágios H/P/A/V, **F6/D/F7, CF-NOR e CLF não alterados**.

## FEITO
- Contraparecer `M06-IF_ELEICOES_05_CONTRAPARECER_VOTO_PRESIDENCIAL_DIRETO_ART60_v0.1.md`: distingue PM investido por Câmara diretamente eleita de Presidência escolhida indiretamente na dupla vacância do art81§1, mudança permanente da escolha presidencial ordinária do art77 e mandato presidencial em curso. A ADI5525/5619 STF 2018 julgou lei ordinária sob CF81/56, não PEC que altere art77.
- **EC2/1992 §1º**: plebiscito de 21/04/1993, eficácia prospectiva prevista em **01/01/1995**. Precedente histórico de separação consulta/vigência, não prazo obrigatório em futura reforma nem regra originária do ADCT2.
- **MS22972**: PGR opinou pela concessão segundo pauta STF, relator havia negado liminar; fim por desistência sem mérito em 2018. Manifestação da PGR não é holding STF.
- Matriz `M06-IF_ELEICOES_05_MATRIZ_12_TESES_E_CONTRA_TESES.csv`: 12 teses e objeções; checklist `M06-IF_ELEICOES_05_CHECKLIST_8_PROVAS_NUCLEO_VOTO.csv`: oito portas ABERTAS.
- `scripts/validar_m06_if_eleicoes_05.py` versionado. **Auditoria independente executada em JS com dados GitHub:** PASS 12/8 registros, 9/8 campos, IDs e cobertura EC2/MS22972, nenhuma célula vazia. Não presumir execução individual do Python pelo CI.

## PENDENTE
M03 deve informar origem e poderes da chefia Estado e premier, títulos, vetos, defesa, orçamento e dissolução. M02 deve qualificar art16/art77 e eleição. M14 deve proteger mandato atual e marcos de posse. M06 deve examinar o texto específico futuro sob art60§4 II, sem supor obrigação ou dispensa definitiva de plebiscito R-CON1/2. Não extrapolar art81 originário para eleição presidencial indireta permanente nem tratar plebiscito como dispensa de art60.

## PRÓXIMO
Devolver conclusão a M02/M03/M14 e coordenação. Aguardar texto real ou F6 expressa para teste por dispositivo; interromper repetição abstrata. PR #96 permanece draft.

Fontes: CF arts14/60/77/81; EC2/1992; Lei8624/1993; STF ADI5525; STF MS22972; Gussoli/Hachem, Seqüência v43 n92 (2022, publicado em 2023). URLs constam do parecer integral.
