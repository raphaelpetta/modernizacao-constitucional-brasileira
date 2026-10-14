#!/usr/bin/env python3
"""Auditoria estrutural M14.01; não certifica constitucionalidade de uma PEC,
obrigatoriedade plebiscitária, preservação real de direitos, custo ou F6.
Uso: python3 scripts/validar_m14_01_transicao.py
"""
from pathlib import Path
from itertools import product
import csv

ROOT=Path(__file__).resolve().parents[1]/"modulos"/"M14-transicao"
def get(file,columns,count,key):
    with (ROOT/file).open(encoding="utf-8",newline="") as f:
        rd=csv.DictReader(f)
        assert rd.fieldnames==columns,(file,rd.fieldnames)
        data=list(rd)
    assert len(data)==count,(file,len(data),count)
    assert len({row[key] for row in data})==count
    assert all(None not in row and all(isinstance(s,str) and s.strip() for s in row.values()) for row in data)
    return data
routes=get("M14-01_MATRIZ_18_ROTAS_E_MANDATOS.csv",[
    "id","arquitetura","estrategia_tempo","alcance_territorial","efeito_mandato_federal","efeito_mandato_subnacional","eleicao_inaugural","cadeia_comando","orçamento_e_caretaker","risco_principal","fonte_e_interface","status"],18,"id")
tests=get("M14-01_MATRIZ_12_TESTES_DE_TRANSICAO.csv",[
    "id","ataque_ou_conflito","arquitetura_afetada","premissa_de_direito_vigente","resultado_que_nao_se_pode_presumir","salvaguarda_em_teste","risco_remanescente","interface_para_parecer","nivel_de_prova","estado"],12,"id")
gates=get("M14-01_PAUTA_12_PORTAS_F6.csv",[
    "id","etapa","questao_decisoria","alternativas_de_estudo","fundamento_ou_risco","interface_exigida","pre_requisito","status"],12,"id")
assert {x["id"] for x in routes}=={"-".join(x) for x in product(("A","B","C"),("PROSPECTIVA","IMEDIATA"),("FED1","FED2","FED3"))}
assert {x["id"] for x in tests}=={f"T{i:02d}" for i in range(1,13)}
assert {x["id"] for x in gates}=={f"F6-M14-{i:02d}" for i in range(1,13)}
assert all(x["status"]=="H_COM_F6_ABERTA" for x in routes)
assert all(x["estado"]=="H" for x in tests)
assert all(x["status"]=="ABERTA" for x in gates)
assert all("M14" in x["fonte_e_interface"] for x in routes)
assert (ROOT/"M14-01_PARECER_AUTONOMO_VIABILIDADE_CONSTITUCIONAL_E_TRANSICAO_v0.1.md").is_file()
print("M14.01 QA PASS: 18 cenários, 12 ataques e 12 portas F6 abertas, parecer versionado.")
print("Limites: nenhum dado financeiro, revisão judicial definitiva ou ratificação F6 validada.")
