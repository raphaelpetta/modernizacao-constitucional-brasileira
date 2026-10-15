#!/usr/bin/env python3
"""Audita integridade estrutural dos CSV da M03.02.07.
Nao valida validade juridica, legitimidade eleitoral, custo fiscal ou fonte empirica.
Uso: python3 scripts/validar_m03_02_07_matrizes.py, a partir de qualquer CWD.
"""
from collections import Counter, defaultdict
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "modulos" / "M03-parlamento"
FILES = {
    "cal": ("M03-02_07_CALENDARIOS_ELEITORAIS.csv", 15, 12),
    "fis": ("M03-02_07_MATRIZ_CONTINUIDADE_FISCAL.csv", 3, 11),
    "att": ("M03-02_07_OITO_ATAQUES_ELEICAO_ORCAMENTO.csv", 8, 11),
}

def load(name, count, width):
    with (ROOT / name).open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        assert reader.fieldnames and len(reader.fieldnames) == width, name
        assert len(set(reader.fieldnames)) == width, name
        rows = list(reader)
    assert len(rows) == count, (name, len(rows), count)
    ids = [r["id"] for r in rows]
    assert len(ids) == len(set(ids)), (name, "duplicate IDs")
    for row in rows:
        assert None not in row and all(v is not None for v in row.values()), row
        assert all(v.strip() for v in row.values()), row["id"]
        assert row.get("status") or row.get("estado"), row["id"]
    return rows

cal = load(*FILES["cal"])
fis = load(*FILES["fis"])
att = load(*FILES["att"])
expected = {"ORDINARIO": 5, "EXTRAORDINARIO": 6, "INAUGURAL": 4}
groups = defaultdict(list)
for r in cal:
    groups[r["trajeto"]].append(int(r["ordem"]))
assert {name: len(v) for name,v in groups.items()} == expected, groups
for name, order in groups.items():
    assert order == list(range(len(order))), (name, order)
assert {r["id"] for r in fis} == {"FISC-A","FISC-B","FISC-C"}
assert {r["id"] for r in att} == {f"S{i:02d}" for i in range(1,9)}
assert all(r["status"] == "H" for r in att)
assert all(r["status"] == "H" for r in cal)
print("M03.02.07: estrutura valida; 3 calendarios, 15 marcos, 3 modelos fiscais, 8 ataques.")
print("Limite: nem fontes normativas, nem custos/autoridades, nem escolha F6 foram validados.")
