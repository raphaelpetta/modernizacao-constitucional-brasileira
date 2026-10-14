#!/usr/bin/env python3
"""QA estrutural M02.01. NÃO atesta julgamento STF, eleição válida, plebiscito
nacional juridicamente obrigatório, sistema de votação ou decisão F6.
Uso: python3 scripts/validar_m02_01_matrizes.py
"""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"modulos"/"M02-eleicoes"
def check(name, header, count, pref, statusfield, statuses):
    with (ROOT/name).open(encoding="utf-8", newline="") as f:
        csvread=csv.DictReader(f)
        assert csvread.fieldnames==header,(name,csvread.fieldnames)
        rows=list(csvread)
    assert len(rows)==count,(name,len(rows))
    assert [row["id"] for row in rows]==[f"{pref}{i:02d}" for i in range(1,count+1)]
    assert all(None not in row and all(str(v).strip() for v in row.values()) for row in rows)
    assert all(row[statusfield] in statuses for row in rows)
    return rows
a=check("M02-01_MATRIZ_16_ENQUADRAMENTOS_ART16_E_PLEBISCITO.csv",
["id","classe","tipo_de_ato","cenario_material","fonte_vigente","exame_art16","risco_principal","regra_de_verificacao","interface","status"],16,"E","status",{"H","A","V"})
b=check("M02-01_MATRIZ_12_TESTES_ADVERSARIAIS.csv",
["id","ataque","premissa_ficticia","controle_juridico","resultado_que_nao_presumir","resposta_hou_a","objeção_residual","revisor","estado"],12,"T","estado",{"H","A","V"})
c=check("M02-01_CHECKLIST_10_PROVAS_PRIMEIRO_PLEITO.csv",
["id","condicao_para_primeiro_pleito","fonte_de_direito_ou_interface","prova_documental","risco_se_ausente","responsavel_parecer","status"],10,"G","status",{"PENDENTE"})
assert all(r["status"]=="PENDENTE" for r in c)
assert any("Res23772" in r["cenario_material"] for r in a)
assert any("Lei9709" in r["controle_juridico"] and "art9" in r["controle_juridico"] for r in b)
assert (ROOT/"M02-01_PARECER_AUTONOMO_INTEGRIDADE_E_TRANSICAO_ELEITORAL_v0.1.md").is_file()
print("M02.01 QA PASS: 16 classificações, 12 contraprovas, 10 condições abertas.")
print("Nenhuma decisão de F6, aplicação eleitoral, plebiscito nacional ou eleição foi certificada.")
