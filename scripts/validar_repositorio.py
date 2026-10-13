#!/usr/bin/env python3
"""Validação estrutural mínima; não atesta qualidade jurídica das propostas."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parent.parent
required = [
    "README.md", "docs/00_LEIA_PRIMEIRO.md",
    "governanca/01_MANIFESTO.md", "governanca/02_METODOLOGIA.md",
    "governanca/03_DECISOES.md", "governanca/04_ESTADO_ATUAL.md",
    "governanca/05_DEPENDENCIAS.md", "governanca/06_CONTINUIDADE_VERSIONAMENTO.md",
    "catalogo/MODULOS.csv", "modelos/PACOTE_CONTINUIDADE.md",
    "integracao/01_INTERFACE_CLF.md",
    "referencias/guia_mestre_constitucional_v0.1.md",
    "referencias/anteprojeto_constitucional_v0.1_texto.md"
]
errors = ["Arquivo obrigatório ausente: " + p for p in required if not (root / p).is_file()]
with (root / "catalogo/MODULOS.csv").open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))
ids = [r["id_modulo"] for r in rows]
if len(ids) != len(set(ids)): errors.append("IDs duplicados no catálogo")
if set(ids) != {"M%02d" % i for i in range(15)}: errors.append("Conjunto M00-M14 incompleto")
for r in rows:
    for dep in filter(None, r["interfaces"].split(";")):
        if dep not in ids:
            errors.append("Dependência inexistente: " + r["id_modulo"] + " -> " + dep)
for problem in errors: print("ERRO:", problem)
if errors: raise SystemExit(1)
print("OK:", len(rows), "módulos; arquivos e dependências coerentes.")
print("Nota: esta checagem não valida direito vigente, decisões nem qualidade de pesquisa.")
