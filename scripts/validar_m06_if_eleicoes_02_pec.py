#!/usr/bin/env python3
"""Valida APENAS estrutura M06-IF-ELEI-002: precedentes e portas abertas.
Não valida jurisprudência, eficácia de precedente, cabimento concreto,
prazo de MS, inconstitucionalidade de PEC ou deliberação F6.
"""
from pathlib import Path
import csv

DIR=Path(__file__).resolve().parents[1]/"modulos"/"M06-justica"
FILES=[
 ("M06-IF_ELEICOES_02_MATRIZ_10_PRECEDENTES_PEC.csv",10,"P",11,"estado","VERIFICADO_"),
 ("M06-IF_ELEICOES_02_CHECKLIST_8_PORTAS_CABIMENTO_MS.csv",8,"K",8,"status","ABERTA")
]
for name, n, prefix, width, state, start in FILES:
    with (DIR/name).open(encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f)
        assert len(reader.fieldnames)==width
        rows=list(reader)
    assert len(rows)==n
    assert [x["id"] for x in rows]==[prefix+f"{i:02d}" for i in range(1,n+1)]
    assert all(None not in x and all(str(v).strip() for v in x.values()) for x in rows)
    assert all(x[state].startswith(start) for x in rows)
assert (DIR/"M06-IF_ELEICOES_02_PARECER_ESPECIFICO_PEC_ART60_PAR4_STF_v0.1.md").exists()
print("M06-IF-ELEI-002 PASS 10 precedentes, 8 portas de cabimento ABERTAS.")
