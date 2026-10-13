#!/usr/bin/env python3
"""Verifica integridade documental. Não verifica direito vigente ou qualidade científica."""
from __future__ import annotations

import csv
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent.parent
errors: list[str] = []
required = [
    "README.md", "docs/00_LEIA_PRIMEIRO.md",
    "governanca/01_MANIFESTO.md", "governanca/02_METODOLOGIA.md",
    "governanca/03_DECISOES.md", "governanca/04_ESTADO_ATUAL.md",
    "governanca/05_DEPENDENCIAS.md", "governanca/06_CONTINUIDADE_VERSIONAMENTO.md",
    "governanca/08_ROTEIRO_INICIAL.md", "governanca/09_AUDITORIA_GARANTIAS.md",
    "governanca/10_PROVENIENCIA_E_IDS.md", "catalogo/MODULOS.csv",
    "modelos/PACOTE_CONTINUIDADE.md", "modelos/MATRIZ_GARANTIAS.csv",
    "integracao/01_INTERFACE_CLF.md", "chatgpt/INSTRUCOES_PROJETO.md",
    "referencias/guia_mestre_constitucional_v0.1.md",
    "referencias/anteprojeto_constitucional_v0.1_texto.md",
]
for item in required:
    if not (BASE / item).is_file(): errors.append("Arquivo ausente: " + item)

def rows_for(path: Path) -> list[dict[str,str]]:
    if not path.is_file(): return []
    with path.open(encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        columns=reader.fieldnames or []
        if len(set(columns))!=len(columns): errors.append("Cabeçalho repetido: "+str(path))
        rows=list(reader)
        for idx,row in enumerate(rows,2):
            if None in row or any(value is None for value in row.values()):
                errors.append(f"{path.name}:{idx}: colunas inconsistentes")
        return rows

modules=rows_for(BASE/"catalogo/MODULOS.csv")
identifiers=[(r.get("id_modulo") or "").strip() for r in modules]
if len(identifiers)!=len(set(identifiers)): errors.append("IDs duplicados em MODULOS.csv")
if set(identifiers)!={f"M{i:02d}" for i in range(15)}: errors.append("Conjunto M00 a M14 incompleto")
for r in modules:
    for dep in filter(None,(r.get("interfaces") or "").split(";")):
        if dep not in identifiers:
            errors.append(f"Dependência inexistente: {r.get('id_modulo')} -> {dep}")
rows_for(BASE/"modelos/MATRIZ_GARANTIAS.csv")

# Inventário M00.02: registros rastreáveis, sem atribuir a este teste força jurídica.
reserve_file = BASE / "modulos/M00-fundamentos/M00-02_INVENTARIO_RESERVAS_CF1988.csv"
if reserve_file.exists():
    with reserve_file.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        required_fields = {
            "id", "localizacao_constitucional", "categoria_analitica",
            "instrumento_vigente", "titular_competencia", "objeto",
            "observacoes_e_pendencias", "modulos"
        }
        if not required_fields.issubset(set(reader.fieldnames or [])):
            errors.append("M00.02: colunas obrigatórias ausentes")
        reserve_rows = list(reader)
        seen_reserves: set[str] = set()
        for index, row in enumerate(reserve_rows, 1):
            identifier = (row.get("id") or "").strip()
            if identifier in seen_reserves or not re.fullmatch(r"\\d{2,}", identifier):
                errors.append(f"M00.02:{index}: ID duplicado ou malformado: {identifier}")
            seen_reserves.add(identifier)
            if None in row or any(v is None for v in row.values()):
                errors.append(f"M00.02:{index}: colunas irregulares")
            for dep in (row.get("modulos") or "").split(";"):
                if dep and dep not in identifiers:
                    errors.append(f"M00.02:{index}: módulo inexistente: {dep}")
            if not (row.get("localizacao_constitucional") or "").strip():
                errors.append(f"M00.02:{index}: dispositivo vazio")
        if len(reserve_rows) < 53:
            errors.append("M00.02: baseline esperada de 53 registros não encontrada")

# Verifica links Markdown locais; não testa URLs remotas, direito ou fontes externas.
for md in [BASE/"README.md",*BASE.glob("docs/*.md"),*BASE.glob("governanca/*.md")]:
    if not md.is_file(): continue
    text=md.read_text(encoding="utf-8")
    for dest in re.findall(r"\]\(([^)]+)\)",text):
        if dest.startswith(("http://","https://","mailto:","#")): continue
        clean=dest.split("#",1)[0]
        if clean and not (md.parent/clean).exists():
            errors.append(f"{md.relative_to(BASE)}: link local inválido {clean}")

if errors:
    for e in errors: print("ERRO:",e,file=sys.stderr)
    raise SystemExit(1)
print(f"OK: {len(modules)} módulos, dependências e arquivos obrigatórios conferidos.")
print("Validação de estrutura apenas; fontes, decisões e qualidade jurídica exigem auditoria.")
