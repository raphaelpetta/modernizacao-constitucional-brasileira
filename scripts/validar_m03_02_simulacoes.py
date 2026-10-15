#!/usr/bin/env python3
"""Valida apenas a aritmética dos cenários hipotéticos M03.02.03.

Não verifica validade jurídica, probabilidade empírica ou deliberação constitucional.
Executar da raiz: python3 scripts/validar_m03_02_simulacoes.py
"""
from collections import defaultdict
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "modulos" / "M03-parlamento"

def read(filename):
    with (ROOT / filename).open(encoding="utf-8", newline="") as fp:
        return list(csv.DictReader(fp))

seats = defaultdict(dict)
for row in read("M03-02_03_COMPOSICAO_LEGISLATURAS.csv"):
    s, party, size = row["cenario"], row["partido_ficticio"], int(row["cadeiras"])
    assert party not in seats[s], (s, party)
    assert size > 0, row
    seats[s][party] = size
assert len(seats) == 3
for sc, parties in seats.items():
    assert sum(parties.values()) == 100, sc

def vote_weight(sc, code):
    names = code.split("+") if code else []
    assert len(names) == len(set(names)), code
    assert set(names) <= set(seats[sc]), (sc, code)
    return set(names), sum(seats[sc][k] for k in names)

def check_partition(sc, yes, no, abst):
    y, sy = vote_weight(sc, yes)
    n, sn = vote_weight(sc, no)
    a, sa = vote_weight(sc, abst)
    assert not (y & n or y & a or n & a), (sc, yes, no, abst)
    assert y | n | a == set(seats[sc]), (sc, yes, no, abst)
    assert sy + sn + sa == 100
    return sy, sn, sa

events = read("M03-02_03_EVENTOS_SIMULADOS_AUDITAVEIS.csv")
assert len(events) == 29, len(events)
assert len({x["id"] for x in events}) == len(events)
by_path = defaultdict(list)
for e in events:
    sc, typ = e["cenario"], e["ato"]
    sy, sn, sa = check_partition(sc, e["partidos_sim"], e["partidos_nao"], e["partidos_abstencao"])
    assert (sy, sn, sa, sy + sn + sa) == tuple(map(int, (
        e["votos_sim"], e["votos_nao"], e["abstencoes"], e["total_membros"]
    ))), e["id"]
    b1 = b2 = b3 = censura = ordinary = "NA"
    if typ == "investidura":
        b1 = "APROVA" if sy >= 51 else "REJEITA"
        b2 = "APROVA_FASE_1" if sy >= 51 else (
            "APROVA_FASE_2" if sy > sn else "REJEITA_FASE_2"
        )
        b3 = "NAO_REJEITADO" if sn <= 50 else "REJEITADO"
    elif typ == "censura_construtiva":
        censura = "APROVA_SUBSTITUICAO" if sy >= 51 else "NAO_APROVA"
    elif typ in {"orcamento", "confianca_teste"}:
        ordinary = "MAIORIA_SIMPLES_SIM" if sy > sn else "MAIORIA_SIMPLES_NAO"
    else:
        raise ValueError((e["id"], typ))
    actual = tuple(e[k] for k in (
        "resultado_B1", "resultado_B2_fase_indicada", "resultado_B3",
        "censura_51", "maioria_simples"
    ))
    assert actual == (b1, b2, b3, censura, ordinary), (e["id"], actual)
    by_path[(sc, e["trajetoria"])].append(int(e["ordem"]))

assert len(by_path) == 6
for key, ids in by_path.items():
    assert ids == list(range(1, len(ids) + 1)), (key, ids)

pres = read("M03-02_03_CONTRAFACTUAL_PRESIDENCIALISMO.csv")
assert len(pres) == 6
for row in pres:
    sc = row["cenario"]
    sy, sn, sa = check_partition(sc, row["partidos_sim"], row["partidos_nao"], row["partidos_abstencao"])
    assert (sy, sn, sa) == tuple(map(int, (row["sim"], row["nao"], row["abstencoes"]))), row["id"]
    predicted = "APROVA_SIMPLIFICADO" if sy > sn else "REJEITA_SIMPLIFICADO"
    assert row["resultado_lei_hipotetico"] == predicted, row["id"]
print(f"VALIDAÇÃO ARITMÉTICA: {len(seats)} legislaturas, {len(by_path)} trajetórias, {len(events)} votações parlamentares, {len(pres)} votações presidenciais; nenhum juízo de validade jurídica.")
