#!/usr/bin/env python3
"""M06-IF-ELEI-004: consistência estrutural da comparação A/B/C.
NÃO verifica constitucionalidade, validade de PEC, probabilidade,
necessidade definitiva de plebiscito, nem deliberação F6.
"""
import csv
from pathlib import Path
dir=Path(__file__).resolve().parents[1] / "modulos" / "M06-justica"
f=dir / "M06-IF_ELEICOES_04_MATRIZ_12_COMPARACOES_SIMETRICAS_A_B_C.csv"
h=["id","eixo_comum","A_presidencial_reformado","B_parlamentar_racionalizado",
   "C_premier_presidencial","nucleo_CFC_art60","ataque_adversarial_comum",
   "diferenca_mais_relevante","prova_faltante","fontes","status"]
with f.open(encoding="utf-8",newline="") as fd:
    rd=csv.DictReader(fd)
    assert rd.fieldnames==h,rd.fieldnames
    rows=list(rd)
assert len(rows)==12
assert [r["id"] for r in rows]==[f"S{i:02d}" for i in range(1,13)]
assert all(None not in r and all(isinstance(v,str) and v.strip() for v in r.values()) for r in rows)
assert all(r["status"]=="ABERTA" for r in rows)
assert all(all(r[col] for col in ["A_presidencial_reformado","B_parlamentar_racionalizado","C_premier_presidencial"]) for r in rows)
assert (dir / "M06-IF_ELEICOES_04_CONTROLE_SIMETRICO_A_B_C_ART60_v0.1.md").is_file()
print("M06-IF-ELEI-004 QA PASS: 12 eixos simétricos; 3 alternativas, todas questões ABERTAS.")
print("A auditoria é estrutural, não constitui parecer judicial ou ratificação F6.")
