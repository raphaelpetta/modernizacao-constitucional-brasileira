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
            if identifier in seen_reserves or not re.fullmatch(r"[0-9]{2,}", identifier):
                errors.append(f"M00.02:{index}: ID duplicado ou malformado: {identifier}")
            seen_reserves.add(identifier)
            if None in row or any(v is None for v in row.values()):
                errors.append(f"M00.02:{index}: colunas irregulares")
            for dep in (row.get("modulos") or "").split(";"):
                if dep and dep not in identifiers:
                    errors.append(f"M00.02:{index}: módulo inexistente: {dep}")
            if not (row.get("localizacao_constitucional") or "").strip():
                errors.append(f"M00.02:{index}: dispositivo vazio")
        if len(reserve_rows) < 75:
            errors.append("M00.02: baseline esperada de 75 registros não encontrada")

# ADCT: validação estrutural dos registros temporais não exaustivos.
adct_file = BASE / "modulos/M00-fundamentos/M00-02_ADCT_MATRIZ_TEMPORAL_v0.2.csv"
if adct_file.exists():
    with adct_file.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        required_adct_fields = {
            "id", "localizacao_adct", "tipo", "fonte_normativa_ou_procedimento",
            "marco_temporal", "efeito_resumido", "estado_temporal_inicial",
            "modulos", "pendencia", "url_fonte_oficial"
        }
        if not required_adct_fields.issubset(set(reader.fieldnames or [])):
            errors.append("M00.02 ADCT: colunas obrigatórias ausentes")
        adct_rows = list(reader)
        ids_adct: set[str] = set()
        for index, row in enumerate(adct_rows, 1):
            identity = (row.get("id") or "").strip()
            if identity in ids_adct or not re.fullmatch(r"ADCT-[0-9]{3}", identity):
                errors.append(f"ADCT:{index}: ID duplicado ou malformado: {identity}")
            ids_adct.add(identity)
            if None in row or any(value is None for value in row.values()):
                errors.append(f"ADCT:{index}: colunas irregulares")
            for module in (row.get("modulos") or "").split(";"):
                if module and module not in identifiers:
                    errors.append(f"ADCT:{index}: módulo inexistente: {module}")
            if not (row.get("url_fonte_oficial") or "").startswith("https://"):
                errors.append(f"ADCT:{index}: fonte oficial sem URL HTTPS")
        if len(adct_rows) < 18:
            errors.append("M00.02 ADCT: baseline esperada de 18 registros ausente")

# M03.01: matriz adversarial e matriz de classificação por matéria.
for relative_path, prefix, expected_count in [
    ("modulos/M03-parlamento/M03-01_TESTES_PROCESSO_LEGISLATIVO.csv", "CF-TEST-M03-", 12),
    ("modulos/M03-parlamento/M03-01_TRIAGEM_MATERIAS_PROCEDIMENTOS.csv", "M03-MAT-", 10),
]:
    target = BASE / relative_path
    if not target.is_file():
        errors.append(f"M03.01: arquivo ausente {relative_path}")
        continue
    with target.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        current_rows = list(reader)
    if not current_rows or "id" not in (reader.fieldnames or []):
        errors.append(f"M03.01: cabeçalho ou dados inválidos {relative_path}")
        continue
    observed: set[str] = set()
    for index, row in enumerate(current_rows, 1):
        identity = (row.get("id") or "").strip()
        if identity in observed or not re.fullmatch(re.escape(prefix) + r"[0-9]{3}", identity):
            errors.append(f"M03.01:{index}: ID inválido ou duplicado {identity}")
        observed.add(identity)
        if None in row or any(v is None for v in row.values()):
            errors.append(f"M03.01:{index}: colunas irregulares em {relative_path}")
        for dep in (row.get("modulos") or "").split(";"):
            if dep and dep not in identifiers:
                errors.append(f"M03.01:{index}: módulo inválido {dep}")
    if len(current_rows) != expected_count:
        errors.append(f"M03.01: esperado {expected_count}, obtido {len(current_rows)} em {relative_path}")

# M04.01: verificação estrutural dos cenários e triagens de consentimento.
for relative_path, prefix, expected_count in [
    ("modulos/M04-federacao/M04-01_TESTES_IMPASSES.csv", "CF-TEST-M04-", 12),
    ("modulos/M04-federacao/M04-01_TRIAGEM_CONSENTIMENTO.csv", "CF-M04-MAT-", 10),
]:
    candidate = BASE / relative_path
    if not candidate.is_file():
        errors.append(f"M04.01: arquivo ausente {relative_path}")
        continue
    with candidate.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        values = list(reader)
    if not values or "id" not in (reader.fieldnames or []):
        errors.append(f"M04.01: tabela inválida {relative_path}")
        continue
    observed: set[str] = set()
    for line_number, record in enumerate(values, 1):
        identity = (record.get("id") or "").strip()
        if identity in observed or not re.fullmatch(re.escape(prefix) + r"[0-9]{3}", identity):
            errors.append(f"M04.01:{line_number}: ID inválido ou repetido {identity}")
        observed.add(identity)
        if None in record or any(v is None for v in record.values()):
            errors.append(f"M04.01:{line_number}: número de colunas irregular")
        for module in (record.get("modulos") or "").split(";"):
            if module and module not in identifiers:
                errors.append(f"M04.01:{line_number}: módulo inválido {module}")
    if len(values) != expected_count:
        errors.append(f"M04.01: esperado {expected_count}, encontrado {len(values)} em {relative_path}")

# M05.01: validar matriz adversarial e cenários numéricos exclusivamente fictícios.
for relative_path, prefix, expected_count in [
    ("modulos/M05-financas/M05-01_TESTES_ENCARGOS.csv", "CF-TEST-M05-", 12),
    ("modulos/M05-financas/M05-01_SIMULACAO_ILUSTRATIVA.csv", "HYP-M05-", 6),
]:
    location = BASE / relative_path
    if not location.is_file():
        errors.append(f"M05.01: arquivo ausente {relative_path}")
        continue
    with location.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(line for line in f if line.strip() and not line.startswith("#"))
        study_rows = list(reader)
    seen_study: set[str] = set()
    for i, record in enumerate(study_rows, 1):
        identity = (record.get("id") or "").strip()
        if identity in seen_study or not re.fullmatch(re.escape(prefix) + r"[0-9]{3}", identity):
            errors.append(f"M05.01:{i}: ID inválido/duplicado: {identity}")
        seen_study.add(identity)
        if None in record or any(x is None for x in record.values()):
            errors.append(f"M05.01:{i}: linha com colunas inválidas")
        for dep in (record.get("modulos") or "").split(";"):
            if dep and dep not in identifiers:
                errors.append(f"M05.01:{i}: módulo inexistente: {dep}")
        if identity.startswith("HYP-M05-"):
            try:
                B = float(record["custo_minimo_B"])
                A = float(record["gasto_existente_A"])
                R = float(record["receita_disponivel_R"])
                prev = float(record["transferencia_prevista_Tprev"])
                real = float(record["transferencia_recebida_Trec"])
                increment = max(0, B - A)
                if (abs(float(record["custo_incremental_M"]) - increment) > 1e-9
                    or abs(float(record["lacuna_planejada_Gprev"]) - max(0, increment - R - prev)) > 1e-9
                    or abs(float(record["lacuna_efetiva_Gefet"]) - max(0, increment - R - real)) > 1e-9):
                    errors.append(f"M05.01:{i}: cálculo didático inconsistente")
            except (KeyError, TypeError, ValueError):
                errors.append(f"M05.01:{i}: colunas numéricas inválidas")
    if len(study_rows) != expected_count:
        errors.append(f"M05.01: esperado {expected_count}, obtido {len(study_rows)} em {relative_path}")

# M05.02: esquema vazio e catálogo de fontes rastreáveis (não dados empíricos).
source_catalog = BASE / "modulos/M05-financas/M05-02_CATALOGO_FONTES.csv"
schema_file = BASE / "modelos/M05_02_ESQUEMA_NORMALIZADO.csv"
for target in [source_catalog, schema_file]:
    if not target.is_file():
        errors.append(f"M05.02: arquivo obrigatório ausente {target}")
if source_catalog.is_file():
    with source_catalog.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        docs = list(reader)
    source_ids: set[str] = set()
    for i, document in enumerate(docs, 1):
        identity = (document.get("id") or "").strip()
        if identity in source_ids or not re.fullmatch(r"M05-FONT-[0-9]{3}", identity):
            errors.append(f"M05.02:{i}: fonte duplicada ou inválida: {identity}")
        source_ids.add(identity)
        if not (document.get("pagina_ou_api_oficial") or "").startswith("https://"):
            errors.append(f"M05.02:{i}: URL de fonte ausente")
        if "NAO" not in (document.get("estado_verificacao_2026_10_13") or "") and "VERIFICADA" not in (document.get("estado_verificacao_2026_10_13") or ""):
            errors.append(f"M05.02:{i}: estado de verificação não informado")
    if len(docs) < 10:
        errors.append("M05.02: catálogo inicial incompleto")
if schema_file.is_file():
    with schema_file.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        if not {"codigo_ibge", "ano", "ano_populacao", "fonte_contas", "fonte_populacao"}.issubset(set(reader.fieldnames or [])):
            errors.append("M05.02: cabeçalho do esquema incompatível")
        if list(reader):
            errors.append("M05.02: esquema não pode conter observações presumidamente oficiais")

# M01.07: auditoria amostral sem alegar equivalência constitucional e cinco normas H.
m01_matrix = BASE / "modulos/M01-direitos-fundamentais/M01-07_MATRIZ_DE_CONTINUIDADE.csv"
if not m01_matrix.is_file():
    errors.append("M01.07: matriz amostral de garantias ausente")
else:
    with m01_matrix.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        m01_items = list(reader)
    required_m01 = {"id", "fonte_cf1988", "garantia_vigente", "propostas_relacionadas", "resultado_inicial", "risco_de_equivalencia", "pesquisa_necessaria", "modulos"}
    if not required_m01.issubset(set(reader.fieldnames or [])):
        errors.append("M01.07: colunas ausentes")
    ids_m01 = set()
    for idx, item in enumerate(m01_items, 1):
        code = (item.get("id") or "").strip()
        if code in ids_m01 or not re.fullmatch(r"M01-AUD-[0-9]{3}", code):
            errors.append(f"M01.07:{idx}: ID inválido/repetido {code}")
        ids_m01.add(code)
        if None in item or any(v is None for v in item.values()):
            errors.append(f"M01.07:{idx}: colunas irregulares")
        if item.get("resultado_inicial") not in {"INDETERMINADO", "PARCIAL_E_INDETERMINADO", "NAO_COBERTO", "NAO_EQUIVALENTE"}:
            errors.append(f"M01.07:{idx}: equivalência material não foi validada: {item.get('resultado_inicial')}")
        for dep in (item.get("modulos") or "").split(";"):
            if dep and dep not in identifiers:
                errors.append(f"M01.07:{idx}: módulo desconhecido: {dep}")
    if len(m01_items) != 16:
        errors.append("M01.07: matriz inicial deve conter 16 linhas")

# M01.09: matriz de continuidade da igualdade, sem declarar equivalência.
eq_csv = BASE / "modulos/M01-direitos-fundamentais/M01-09_MATRIZ_IGUALDADE_E_GARANTIAS.csv"
if not eq_csv.is_file():
    errors.append("M01.09: matriz de igualdade ausente")
else:
    with eq_csv.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        eq_rows = list(reader)
    required = {"id", "garantia_vigente", "fonte_primaria", "candidatas_cf_nor",
                "estado_de_continuidade", "risco_ou_lacuna", "teste_adversarial", "modulos"}
    if not required.issubset(set(reader.fieldnames or [])):
        errors.append("M01.09: colunas faltantes")
    eq_ids: set[str] = set()
    for i, entry in enumerate(eq_rows, 1):
        key = (entry.get("id") or "").strip()
        if key in eq_ids or not re.fullmatch(r"M01-EQ-AUD-[0-9]{3}", key):
            errors.append(f"M01.09:{i}: identificador inválido/duplicado {key}")
        eq_ids.add(key)
        if None in entry or any(value is None for value in entry.values()):
            errors.append(f"M01.09:{i}: linha malformada")
        if entry.get("estado_de_continuidade") not in {
            "INDETERMINADO", "PARCIAL_E_INDETERMINADO", "NAO_EQUIVALENTE", "NAO_COBERTO"
        }:
            errors.append(f"M01.09:{i}: alegação indevida de equivalência material")
        for module in (entry.get("modulos") or "").split(";"):
            if module and module not in identifiers:
                errors.append(f"M01.09:{i}: dependência desconhecida {module}")
    if len(eq_rows) != 16:
        errors.append("M01.09: esperados 16 registros na amostra")

# M01.10: verificação de estrutura e ressalvas de continuidade em bioética.
bio_file = BASE / "modulos/M01-direitos-fundamentais/M01-10_MATRIZ_CONTINUIDADE.csv"
if not bio_file.is_file():
    errors.append("M01.10: matriz de garantias ausente")
else:
    with bio_file.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        bio_rows = list(reader)
    required_bio = {"id", "fonte_direito_vigente", "garantia_ou_materia", "propostas_relacionadas",
                    "avaliacao_inicial", "risco_de_regressao_ou_excesso", "teste_adversarial", "modulos"}
    if not required_bio.issubset(set(reader.fieldnames or [])):
        errors.append("M01.10: colunas ausentes")
    bio_ids = set()
    for i, record in enumerate(bio_rows, 1):
        key = (record.get("id") or "").strip()
        if key in bio_ids or not re.fullmatch(r"M01-BIO-AUD-[0-9]{3}", key):
            errors.append(f"M01.10:{i}: ID repetido/inválido: {key}")
        bio_ids.add(key)
        if None in record or any(val is None for val in record.values()):
            errors.append(f"M01.10:{i}: linha irregular")
        if record.get("avaliacao_inicial") not in {
            "NAO_COBERTO", "NAO_EQUIVALENTE", "PARCIAL_E_INDETERMINADO", "INDETERMINADO"
        }:
            errors.append(f"M01.10:{i}: alegação não demonstrada de equivalência material")
        for module in (record.get("modulos") or "").split(";"):
            if module and module not in identifiers:
                errors.append(f"M01.10:{i}: módulo inexistente {module}")
    if len(bio_rows) != 20:
        errors.append("M01.10: são esperados 20 casos de continuidade")

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
