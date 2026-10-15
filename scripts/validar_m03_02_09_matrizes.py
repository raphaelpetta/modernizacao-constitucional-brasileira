#!/usr/bin/env python3
"""M03.02.09: valida apenas forma e completude das matrizes hipotéticas.
Não verifica direito, solvência, execução fiscal, causalidade, votação ou F6.
Executar: python3 scripts/validar_m03_02_09_matrizes.py
"""
import csv
from itertools import product
from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / "modulos" / "M03-parlamento"

def load(filename, count, cols):
    with (BASE / filename).open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        assert reader.fieldnames == cols, (filename, reader.fieldnames)
        records = list(reader)
    assert len(records) == count, (filename, count, len(records))
    ids = [r["id"] for r in records]
    assert len(set(ids)) == len(ids), (filename, "duplicate IDs")
    for record in records:
        assert None not in record, (filename, record)
        assert all(isinstance(v, str) and v.strip() for v in record.values()), (filename, record["id"])
    return records

fields_abuses = [
    "id","ator","ataque","instituto_em_risco","P1_base_minima",
    "P2_lei_especial","P3_revisao_parlamentar","P4_controle_objetivo",
    "risco_residual","controle_federativo_ou_de_direitos","interface","conclusao_H"
]
fields_interactions = [
    "id","legislatura","ano_ficticio","mecanismo","voto_LOA_do_cenario",
    "evento_de_interacao","poder_ativo","efeito_possivel_condicionado",
    "o_que_nao_decide","filtro_de_direitos_federativos","prova_pendente","status"
]
abuses = load("M03-02_09_MATRIZ_12_TESTES_CONTROLE_FISCAL.csv", 12, fields_abuses)
interactions = load("M03-02_09_MATRIZ_24_INTERACOES_L2_L3.csv", 24, fields_interactions)
assert {r["id"] for r in abuses} == {f"T{i:02d}" for i in range(1,13)}
expected = set(product(("L2","L3"), ("Y1","Y2","Y3"), ("P1","P2","P3","P4")))
actual = {(r["legislatura"],r["ano_ficticio"],r["mecanismo"]) for r in interactions}
assert actual == expected and len(actual) == len(interactions)
assert all(r["id"] == "-".join([r["legislatura"],r["ano_ficticio"],r["mecanismo"]]) for r in interactions)
assert all(r["status"] == "H_CONDICIONAL" for r in interactions)
assert all("não altera" not in r["o_que_nao_decide"].lower() or len(r["o_que_nao_decide"]) > 10 for r in interactions)
assert all("NÃO presumida" in r["efeito_possivel_condicionado"] or r["mecanismo"] != "P2" or r["ano_ficticio"] == "Y3" for r in interactions)
assert all("sem dados fiscais" in r["prova_pendente"] for r in interactions)
assert all("excluindo derrota formal de confiança t5" in r["evento_de_interacao"] for r in interactions if r["legislatura"] == "L2"), "ramo pré-confiança obrigatório"
print("M03.02.09: QA estrutural PASS — 12 ataques, 24 interações completas (2 x 3 x 4).")
print("Nenhum dado financeiro, parecer M05, quórum F6 ou CI do validador é presumido.")
