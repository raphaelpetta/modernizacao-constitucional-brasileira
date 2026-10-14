#!/usr/bin/env python3
"""Audita combinatória de votos H e invariantes M03.02.10, não validade jurídica.
Uso: python3 scripts/validar_m03_02_10_matrizes.py
"""
from pathlib import Path
from itertools import product
import csv

ROOT = Path(__file__).resolve().parents[1] / "modulos" / "M03-parlamento"
PARTY = {"L2": {"X":46,"Y":44,"Z":10},
         "L3": {"A":27,"B":23,"C":18,"D":14,"E":10,"F":8}}
SUBJECTS = {"HOSP","ESCOLA","CONVENIO","DIVIDA_NOVA"}
def load(name, cols, count):
    with (ROOT / name).open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        assert rd.fieldnames and len(rd.fieldnames) == cols
        assert len(rd.fieldnames) == len(set(rd.fieldnames))
        rows = list(rd)
    assert len(rows) == count
    assert len({r["id"] for r in rows}) == count
    assert all(None not in r and all(v.strip() for v in r.values()) for r in rows)
    return rows
V = load("M03-02_10_24_VOTACOES_LEIS_PARCIAIS.csv", 20, 24)
T = load("M03-02_10_8_CONTROLES_DE_TITULARIDADE_E_CREDITO.csv", 11, 8)
C = load("M03-02_10_12_TESTES_COHERENCIA_FISCAL.csv", 12, 12)
assert {r["id"] for r in V} == {f"{l}-{s}-{v}" for l,s,v in product(PARTY, SUBJECTS, ("V1","V2","V3"))}
assert {r["id"] for r in T} == {f"{l}-{i}" for l,i in product(PARTY, ("REP_RECEITA","DEVER_VIGENTE","PROG_FINDADO","CREDITO_NOVO"))}
assert {r["id"] for r in C} == {f"{l}-{v}-{f}" for l,v,f in product(PARTY,("V1","V2","V3"),("FONTE_NAO_VERIFICADA","FONTE_INDIVIDUAL_PRESUMIDA_H"))}
for row in V:
    l = row["legislatura"]
    groups = [([] if row[k] == "-" else row[k].split("+")) for k in ("partidos_sim","partidos_nao","partidos_abst")]
    assert sorted(sum(groups,[])) == sorted(PARTY[l])
    yes,no,abst = [sum(PARTY[l][p] for p in group) for group in groups]
    assert (yes,no,abst,yes+no+abst) == tuple(int(row[k]) for k in ("votos_sim","votos_nao","abstencoes","total_membros"))
    assert row["resultado_maioria_simples_ilustrativa"] == ("SIM_MAIOR_QUE_NAO" if yes>no else "SIM_NAO_SUPERA_NAO")
    assert row["status_de_aprovacao_legal"] == "NAO_DETERMINADA_POR_CONTAGEM_DE_VOTOS"
    assert row["estatuto"] == "H_SEM_F6"
    assert (l!="L2" or "SEM voto de confiança" in row["trajetoria_origem"])
    if row["ramo_de_votacao"]=="V2":
        assert "OPOSICAO_INICIATIVA_RESERVADA" in row["teste_de_iniciativa"]
for row in T:
    assert row["estatuto"] == "H_CONDICIONAL"
    if row["id"].endswith("REP_RECEITA"):
        assert row["exige_voto_novo_da_camare_para_nascer"] == "NAO_PARA_CRIAR_DIREITO_DE_TITULARIDADE"
for row in C:
    assert row["estado"] == "H"
    assert "NAO_DETERMINADA" not in row["checagem_da_lei_parcial"]
    assert "NOVA_OPERACAO" in row["checagem_nova_divida"]
print("M03.02.10: QA PASS, 24 votos com cadeiras auditadas; 8 invariantes; 12 testes de coerência.")
print("LIMITE: votos H, sem autorização material, caixa, dados reais ou F6.")
