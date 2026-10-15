#!/usr/bin/env python3
"""Auditoria estrutural do encerramento crítico M03.02 R01–R11.

Validar existência dos onze arquivos de origem, unicidade/ordem/status das duas
matrizes e links para tipos de fonte; NÃO julga direito constitucional,
admissibilidade de F6, fidelidade de pesquisa empírica nem pareceres de interfaces.
Executar no checkout da branch: python3 scripts/validar_m03_02_12_auditoria.py
"""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1] / "modulos" / "M03-parlamento"
EVIDENCE = "M03-02_12_MATRIZ_EVIDENCIAS_R01_R11.csv"
INTERFACE = "M03-02_12_INTERFACE_CHECKLIST_F6.csv"
EXPECTED_EVIDENCE = [
    "rodada","arquivo_principal","pergunta_testada","unidade_de_evidencia",
    "tipo_de_evidencia","achado_mais_forte","limite_da_inferencia",
    "correcao_ou_advertencia","status_de_suficiencia",
    "interface_critica","encaminhamento"
]
EXPECTED_INTERFACE = [
    "id","frente","issue_ou_pr","base_existente_com_estado",
    "pergunta_material_independente","resposta_formal_verificada",
    "efeito_na_escolha_A","efeito_na_escolha_B","efeito_na_escolha_C",
    "criterio_de_saida","prioridade","estado"
]

def load(name, headers, expected_count, key):
    with (ROOT / name).open(encoding="utf-8", newline="") as f:
        rdr = csv.DictReader(f)
        assert rdr.fieldnames == headers, (name, rdr.fieldnames)
        records = list(rdr)
    assert len(records) == expected_count, (name, len(records))
    assert all(None not in r for r in records), name
    assert all(all(isinstance(x,str) and x.strip() for x in r.values()) for r in records), name
    ids = [r[key] for r in records]
    assert len(set(ids)) == len(ids), (name,"duplicate")
    return records

ev = load(EVIDENCE, EXPECTED_EVIDENCE, 11, "rodada")
it = load(INTERFACE, EXPECTED_INTERFACE, 9, "id")
assert [x["rodada"] for x in ev] == [f"R{i:02d}" for i in range(1,12)]
assert [x["id"] for x in it] == [f"IF-{i:02d}" for i in range(1,10)]
for row in ev:
    assert (ROOT / row["arquivo_principal"]).is_file(), row["arquivo_principal"]
    assert any(k in row["tipo_de_evidencia"] for k in [
        "JURIDICA", "FORMAL", "LOGICA", "ADVERSARIAL", "SISTEMICA",
        "INVENTARIO", "COMPARATIVA", "CLASSIFICACAO", "INSTITUCIONAL",
        "ARITMETICA", "ALGORITMICA"
    ])
    assert "SUFICIENTE" in row["status_de_suficiencia"] or row["status_de_suficiencia"].startswith("PARCIAL")
for row in it:
    assert row["resposta_formal_verificada"] == "NAO"
    assert row["estado"].startswith("PENDENTE")
assert {f"IF-{i:02d}" for i in range(1,10)} == {x["id"] for x in it}
print("M03.02.12: QA PASS — 11 documentos de origem, 11 evidências e 9 interfaces pendentes.")
print("Limitação: não emite parecer jurídico, não cria dados empíricos nem ratifica F6.")
