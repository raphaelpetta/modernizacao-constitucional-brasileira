#!/usr/bin/env python3
"""M03.02.13: conferência apenas estrutural dos modelos de transição H.
Não certifica constitucionalidade de emenda, direito a plebiscito, mandatos,
fonte de caixa, validade de eleições ou aprovação F6.
Uso: python3 scripts/validar_m03_02_13_transicao.py
"""
from itertools import product
from pathlib import Path
import csv

BASE = Path(__file__).resolve().parents[1] / "modulos" / "M03-parlamento"
def read(file, cols, count):
    with (BASE / file).open(encoding="utf-8", newline="") as fh:
        r = csv.DictReader(fh)
        assert r.fieldnames == cols, (file, r.fieldnames)
        rows = list(r)
    assert len(rows) == count, (file, len(rows))
    assert all(None not in row and all(v and v.strip() for v in row.values()) for row in rows), file
    return rows

calendar = read("M03-02_13_MATRIZ_12_ETAPAS_T0_T3_A_B_C.csv", [
    "id","arquitetura","fase","fato_juridico_indispensavel","autoridade_anterior",
    "autoridade_nova_ou_potencial","esfera_eleitoral","fonte_orcamento_credito",
    "cadeia_de_comando","risco_constitucional","parecer_pendente","status"], 12)
powers = read("M03-02_13_MATRIZ_18_PODERES_CARETAKER.csv", [
    "id","arquitetura","poder","poder_do_titular_em_transicao_a_testar",
    "limite_proposto_H","obrigacao_que_persiste","risco_de_captura",
    "fonte_comparada_ou_brasileira","revisor","status"], 18)
gates = read("M03-02_13_DEZ_PORTAS_DE_TRANSICAO_F6.csv", [
    "id","ordem","problema_juridico","fundamento_positivo","alternativa_H",
    "limite_da_conclusao","revisao_independente","status"], 10)
for data, key in [(calendar,"id"),(powers,"id"),(gates,"id")]:
    assert len({row[key] for row in data}) == len(data)
arch = ("A","B","C")
assert {row["id"] for row in calendar} == {f"{x}-{t}" for x,t in product(arch,("T0","T1","T2","T3"))}
assert {row["id"] for row in powers} == {f"{x}-{t}" for x,t in product(arch,(
    "ORCAMENTO_CREDITO","DIVIDA_NOVA","NOMEACOES","DISSOLUCAO_CONFIANCA",
    "DEFESA_EMERGENCIA","SERVICOS_REPARTICAO"))}
assert {row["id"] for row in gates} == {f"TR-{i:02d}" for i in range(1,11)}
assert sorted(int(row["ordem"]) for row in gates) == list(range(1,11))
assert all(row["status"]=="ABERTA" for row in gates)
assert all(row["status"].startswith("H_") for row in calendar+powers)
assert all("M14" in row["parecer_pendente"] for row in calendar)
print("M03.02.13 QA PASS: 12 fases, 18 poderes e 10 portas F6 abertas.")
print("Limite: pesquisa H M03, não parecer M14/M02, autorização de transição ou norma.")
