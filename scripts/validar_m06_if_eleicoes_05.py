#!/usr/bin/env python3
"""M06-IF-ELEI-005: validação apenas ESTRUTURAL de teses e portas abertas.
Não atesta constitucionalidade de PEC, obrigação de plebiscito, voto direto,
resultado do STF, consulta ou F6. Uso: python3 scripts/validar_m06_if_eleicoes_05.py
"""
from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parents[1]/"modulos"/"M06-justica"
SPEC=[
 ("M06-IF_ELEICOES_05_MATRIZ_12_TESES_E_CONTRA_TESES.csv",
  ["id","proposicao_debate","natureza_da_evidencia","fonte","argumento_pelo_redesenho",
   "melhor_objeção","limite_do_que_foi_decidido","relevancia_para_B_C","estado"],
  12,"VT",{"V_ABERTA","T_CONTROVERSA"}),
 ("M06-IF_ELEICOES_05_CHECKLIST_8_PROVAS_NUCLEO_VOTO.csv",
  ["id","porta_de_evidencia","ato_ou_texto_indispensavel","fundamento_positivo",
   "melhor_argumento","risco_se_nao_atendido","interface","estado"],
  8,"Q",{"ABERTA"})
]
for filename,columns,expected,prefix,allowed in SPEC:
    with (ROOT/filename).open(encoding="utf-8",newline="") as f:
        csvreader=csv.DictReader(f)
        assert csvreader.fieldnames==columns,(filename,csvreader.fieldnames)
        records=list(csvreader)
    assert len(records)==expected,(filename,len(records))
    assert [x["id"] for x in records]==[f"{prefix}{i:02d}" for i in range(1,expected+1)]
    assert all(None not in x and all(isinstance(v,str) and v.strip() for v in x.values()) for x in records)
    assert all(x["estado"] in allowed for x in records)
assert (ROOT/"M06-IF_ELEICOES_05_CONTRAPARECER_VOTO_PRESIDENCIAL_DIRETO_ART60_v0.1.md").exists()
print("M06-IF-ELEI-005 QA PASS: 12 teses, 8 portas ABERTAS.")
print("Não equivale a decisão do STF, F6, PEC ou homologação de B-D/B-I.")
