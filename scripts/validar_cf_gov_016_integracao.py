from pathlib import Path
import csv

p = Path(__file__).resolve().parents[1] / "governanca"
items = [
    ("16_MATRIZ_18_CONVERGENCIAS_DIVERGENCIAS_M02_M06_M14.csv", 18, "R"),
    ("16_CHECKLIST_12_PORTAS_DE_VALIDADE.csv", 12, "V"),
    ("16_MATRIZ_10_ERROS_DE_TRANSPLANTE_E_COMPETENCIA.csv", 10, "A")
]
for name, count, prefix in items:
    with (p / name).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == count, name
    assert [r["id"] for r in rows] == [f"{prefix}{i:02}" for i in range(1, count+1)]
    assert all(all(v and v.strip() for v in row.values()) for row in rows)
print("CF-GOV-016: 18 reconciliacoes, 12 portas e 10 testes validados estruturalmente.")
