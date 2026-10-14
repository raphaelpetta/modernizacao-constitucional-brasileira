#!/usr/bin/env python3
"""Compila a vista do anteprojeto de fontes CF-NOR; --check detecta divergências.

Não valida conteúdo jurídico, antinomias semânticas nem ratificação substantiva.
"""
from __future__ import annotations
import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "redacao/indice.csv"
OUTPUT = ROOT / "redacao/anteprojeto-de-trabalho.md"
HEADER = (
    "# Anteprojeto constitucional — texto de trabalho (NÃO RATIFICADO)\n\n"
    "> Vista montada automaticamente dos arquivos redacao/indice.csv e "
    "redacao/propostas/CF-NOR-####.md. Não editar esta vista. "
    "As propostas H/P NÃO foram aprovadas e não possuem numeração definitiva.\n\n"
)
COLUMNS = {
    "id", "ordem", "tema", "modulo", "tipo", "status",
    "arquivo", "regra_geral", "justificativa_especialidade",
    "decisao", "auditoria_garantias", "dependencias",
}


def build() -> str:
    with INDEX.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not COLUMNS.issubset(set(reader.fieldnames or [])):
            raise ValueError("Índice CF-NOR sem colunas obrigatórias")
        rows = list(reader)
    ids, orders, norm_texts = set(), set(), {}
    chunks = []
    for row in rows:
        if None in row or any(v is None for v in row.values()):
            raise ValueError("Índice contém número de colunas inconsistente")
        key, order = row["id"].strip(), row["ordem"].strip()
        if not re.fullmatch(r"CF-NOR-[0-9]{4}", key) or key in ids:
            raise ValueError("ID CF-NOR inválido ou duplicado: " + key)
        ids.add(key)
        if not re.fullmatch(r"[0-9]{4,}", order) or order in orders:
            raise ValueError("Ordem inválida ou duplicada: " + order)
        orders.add(order)
        if row["tipo"] not in {"G", "E", "X", "A", "T"}:
            raise ValueError("Tipo de norma inválido: " + key)
        if row["status"] not in {"H", "P", "D"}:
            raise ValueError("Estado de norma inválido: " + key)
        if not re.fullmatch(r"M(?:0[0-9]|1[0-4])", row["modulo"].strip()):
            raise ValueError("Módulo inválido: " + key)
        for dep in filter(None, row["dependencias"].split(";")):
            if not re.fullmatch(r"M(?:0[0-9]|1[0-4])", dep.strip()):
                raise ValueError("Módulo de dependência inválido: " + key)
        if row["tipo"] in {"E", "X"} and (
            not row["regra_geral"].strip()
            or not row["justificativa_especialidade"].strip()
        ):
            raise ValueError("Norma especial/exceção sem regra geral/justificativa: " + key)
        if row["status"] == "D" and not re.fullmatch(
            r"CF-DEC-[0-9]{4}", row["decisao"].strip()
        ):
            raise ValueError("Status D requer ID de decisão ratificada: " + key)
        rel = row["arquivo"].strip()
        if rel != f"redacao/propostas/{key}.md":
            raise ValueError("Caminho da norma não canônico: " + key)
        source = ROOT / rel
        if not source.is_file():
            raise ValueError("Fonte de norma ausente: " + rel)
        body = source.read_text(encoding="utf-8")
        if body.count("<!-- NORMA-INICIO -->") != 1 or body.count("<!-- NORMA-FIM -->") != 1:
            raise ValueError("Marcadores ausentes ou duplicados: " + key)
        norm = body.split("<!-- NORMA-INICIO -->", 1)[1].split(
            "<!-- NORMA-FIM -->", 1
        )[0].strip()
        if not norm or "<!-- NORMA-" in norm:
            raise ValueError("Norma vazia ou malformada: " + key)
        normalized = re.sub(r"\s+", " ", norm).casefold()
        if normalized in norm_texts:
            raise ValueError(f"Texto idêntico entre {key} e {norm_texts[normalized]}")
        norm_texts[normalized] = key
        chunks.append((order, key, row["tema"].strip(), row["status"], row["tipo"], norm, row["regra_geral"].strip()))
    for order, key, tema, state, kind, norm, general in chunks:
        if general and general not in ids:
            raise ValueError(f"{key}: referência a regra geral inexistente: {general}")
        if general == key:
            raise ValueError(f"{key}: referência circular")
    parts = [HEADER]
    for _, key, tema, state, kind, norm, general in sorted(chunks, key=lambda x: x[0]):
        parts.append(f"## {key} — {tema} [{state}; {kind}]\n\n")
        if general:
            parts.append(f"> Regra geral de referência: {general}. Relação em exame.\n\n")
        parts.append(norm + "\n\n")
    return "".join(parts).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    content = build()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != content:
            raise SystemExit("ERRO: texto integrado diverge; regenere com gerar_anteprojeto.py")
        print("OK: texto integrado corresponde ao índice e às fontes versionadas.")
    else:
        OUTPUT.write_text(content, encoding="utf-8")
        print(f"Gerado: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
