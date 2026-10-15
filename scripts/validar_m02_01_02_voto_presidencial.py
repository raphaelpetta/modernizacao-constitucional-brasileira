#!/usr/bin/env python3
"""M02.01.02: consistência ESTRUTURAL de voto presidencial e parlamentarismo.
Não valida holdings, previsão STF, PEC, eleição, voto direto ou F6.
"""
from pathlib import Path
import csv
BASE=Path(__file__).resolve().parents[1] / "modulos" / "M02-eleicoes"
items=[
 ("M02-01_02_MATRIZ_12_PROPOSICOES_VOTO_DIRETO.csv",
  ["id","proposicao_concreta","categoria_epistemica","fonte_ou_precedente",
   "conclusao_juridica_limitada","melhor_contra_argumento","implicacao_A_B_C",
   "prova_ou_parecer_a_obter","status"],12,"VD",{"V_ABERTA","T_DOUTRINA"}),
 ("M02-01_02_CHECKLIST_9_CONDICOES_VOTO_MANDATO.csv",
  ["id","condicao_de_decisao","prova_documental_futura","nucleo_protegido",
   "tese_mais_favoravel","tese_mais_restritiva","interface_responsavel","status"],
  9,"G",{"ABERTA"})
]
for file,cols,n,prefix,allowed in items:
    with (BASE/file).open(encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==cols,(file,reader.fieldnames)
        rows=list(reader)
    assert len(rows)==n,(file,len(rows))
    assert [row["id"] for row in rows]==[f"{prefix}{i:02d}" for i in range(1,n+1)]
    assert all(None not in row and all(str(v).strip() for v in row.values()) for row in rows)
    assert all(row["status"] in allowed for row in rows)
assert (BASE/"M02-01_02_PARECER_VOTO_DIRETO_PRESIDENCIAL_PARLAMENTARISMO_v0.1.md").is_file()
print("M02.01.02 QA PASS: 12 teses e 9 portas ainda abertas.")
print("QA estrutural NÃO representa ratificação F6 ou juízo STF sobre parlamentarismo.")
