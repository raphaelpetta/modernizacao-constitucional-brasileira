#!/usr/bin/env python3
"""M14.01.02: conferência combinatória de hipótese eleitoral/transitória.
Não valida constitucionalidade da emenda, plebiscito, aplicação específica do
art. 16, mandato, disponibilidade financeira, posse real ou decisão F6.
Uso: python3 scripts/validar_m14_01_02_primeira_posse.py
"""
from itertools import product
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1] / "modulos" / "M14-transicao"

def load(filename, cols, n):
    with (ROOT / filename).open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == cols, (filename, reader.fieldnames)
        rows = list(reader)
    assert len(rows) == n, (filename, len(rows))
    assert all(None not in row and all(isinstance(v, str) and v.strip() for v in row.values()) for row in rows), filename
    ids = [r["id"] for r in rows]
    assert len(set(ids)) == n, filename
    return rows

routes = load("M14-01_02_MATRIZ_18_TRILHAS_DE_CONSULTA_E_POSSE.csv",[
    "id","arquitetura","rota_consulta","solucao_jan_fev","ordem_democratica",
    "condicao_art60_e_consulta","condicao_art16_e_eleicao","efeito_mandato",
    "momento_de_investidura","quem_exerce_comando_ate_posse",
    "fonte_fiscal_do_interino","objeção_maxima","parecer_independente","estado"
],18)
cases = load("M14-01_02_MATRIZ_12_CONTRAPROVAS_DO_PLEITO_INAUGURAL.csv",[
    "id","cenario_de_captura","arquitetura","direito_ou_norma_de_controle",
    "inferência_vedada","salvaguarda_em_teste","parecer_responsavel","status"
],12)
gates = load("M14-01_02_CHECKLIST_10_BLOQUEIOS_DE_POSSE.csv",[
    "id","condicao_de_posse","norma_ou_fonte","prova_necessaria","revisor","status"
],10)
expected = {"-".join(items) for items in product(("A","B","C"),("R-CON1","R-CON2"),("J1","J2","J3"))}
assert {x["id"] for x in routes} == expected
assert all(x["estado"]=="H_SEM_DATA_E_F6" for x in routes)
assert all("art16" in x["condicao_art16_e_eleicao"] for x in routes)
assert all("M02" in x["parecer_independente"] for x in routes)
assert {x["id"] for x in cases} == {f"T{i:02d}" for i in range(1,13)}
assert all(x["status"]=="H" for x in cases)
assert {x["id"] for x in gates} == {f"G{i:02d}" for i in range(1,11)}
assert all(x["status"]=="ABERTA" for x in gates)
assert (ROOT / "M14-01_02_PARECER_PRIMEIRO_PLEITO_E_POSSE_ASSIMETRICA_v0.1.md").is_file()
print("M14.01.02 QA PASS: 18 trilhas (3x2x3), 12 contraprovas, 10 bloqueios abertos.")
print("Apenas estrutura: não há datas inaugurais, parecer F6, lei nova ou titularidade executiva aprovada.")
