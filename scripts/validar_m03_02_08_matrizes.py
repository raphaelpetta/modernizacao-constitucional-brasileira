#!/usr/bin/env python3
"""Confere integridade e combinatória de cenários HIPOTÉTICOS da M03.02.08.
Não audita direito, caixa, solvência, dados observacionais, quóruns vigentes ou F6.
Uso: python3 scripts/validar_m03_02_08_matrizes.py
"""
from collections import Counter
from itertools import product
from pathlib import Path
import csv

BASE = Path(__file__).resolve().parents[1] / "modulos" / "M03-parlamento"
FILE_FISC = "M03-02_08_MATRIZ_112_CONDICOES_FISCAIS.csv"
FILE_ELE = "M03-02_08_MATRIZ_16_TESTES_ELEITORAIS.csv"

def load(name, expected_len, expected_fields):
    with (BASE / name).open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        assert rd.fieldnames == expected_fields, (name, rd.fieldnames)
        rows = list(rd)
    assert len(rows) == expected_len, (name, len(rows))
    ids = [r["id"] for r in rows]
    assert len(set(ids)) == len(ids), (name, "id repetido")
    for r in rows:
        assert None not in r and all(isinstance(v, str) and v.strip() for v in r.values()), (name, r)
        assert "NAO" in r["status"] or r["status"].startswith("H"), (name, r["id"])
    return rows

fiscal_fields = [
    "id","legislatura","trajetoria_origem","exercicio_sintetico","modelo_fiscal",
    "fase","categoria","base_juridica_condicional","resultado_hipotetico",
    "autorizacao_a_verificar","fonte_caixa_a_verificar","risco_direitos_entes",
    "revisao_necessaria","status"
]
elect_fields = [
    "id","legislatura","origem_de_caso","regra_eleitoral","evento",
    "causa_dissolucao","dissolucao_legitima","resposta_eleitoral_condicional",
    "efeito_sobre_orcamento","falha_auditoria","controle_e_remedio","status"
]
F = load(FILE_FISC, 112, fiscal_fields)
E = load(FILE_ELE, 16, elect_fields)
categories = {"SERV_SAUDE","SERV_EDUCACAO","REP_CONSTIT","REP_CONVENIO","DIVIDA_SERVICO","DIVIDA_NOVA","PROG_EXTINTO","PROG_NOVO"}
phases = {
    ("FISC-A","Y1","A"), ("FISC-A","Y2","A"),
    ("FISC-B","Y1","B"), ("FISC-B","Y2","B"),
    ("FISC-C","Y1","H1-B"), ("FISC-C","Y1","H2-A"),
    ("FISC-C","Y2","H2-A")
}
expected_fiscal = set(product({"L2","L3"}, phases, categories))
actual_fiscal = {(r["legislatura"],(r["modelo_fiscal"],r["exercicio_sintetico"],r["fase"]),r["categoria"]) for r in F}
assert len(actual_fiscal) == len(F)
assert actual_fiscal == expected_fiscal, ("combinação fiscal ausente", expected_fiscal ^ actual_fiscal)
assert all(r["id"] == "-".join([r["legislatura"],r["modelo_fiscal"],r["exercicio_sintetico"],r["fase"],r["categoria"]]) for r in F)
assert all((r["legislatura"] != "L2" or "NÃO incorpora questão de confiança de t5" in r["revisao_necessaria"]) for r in F), "L2 deve cortar confiança original"
assert all("Y2" not in r["fase"] for r in F), "Y2 é EXERCICIO, não reinicialização H1"
assert not any(r["modelo_fiscal"] == "FISC-C" and r["exercicio_sintetico"] == "Y2" and r["fase"] == "H1-B" for r in F), "H1 não deve reiniciar Y2"
assert all(r["categoria"] != "DIVIDA_NOVA" or r["resultado_hipotetico"] == "SEM_AUTORIZACAO_AUTOMATICA_PARA_NOVO_CREDITO" for r in F)
assert all(r["categoria"] not in {"PROG_EXTINTO","PROG_NOVO"} or r["resultado_hipotetico"].startswith("NAO_") for r in F)
elect_keys = set(product({"L2","L3"},{"ELE-1","ELE-2"},{"C1","C2","C3","C4"}))
actual_elect = {(r["legislatura"],r["regra_eleitoral"],r["id"].split("-")[-1]) for r in E}
assert actual_elect == elect_keys
assert all(r["dissolucao_legitima"] == "NAO" for r in E if r["id"].endswith(("-C1","-C4")))
assert all(r["dissolucao_legitima"] == "CONDICIONAL_GATILHO_AUTONOMO" for r in E if r["id"].endswith(("-C2","-C3")))
assert all("NÃO muda autorização" in r["efeito_sobre_orcamento"] for r in E)
print("M03.02.08 QA PASS: 112 condições (2 x 7 x 8), 16 testes ELE (2 x 2 x 4).")
print("Limitado à estrutura, sem aprovação constitucional, probabilidade, custos ou execução do Tesouro.")
