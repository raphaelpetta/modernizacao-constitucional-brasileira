#!/usr/bin/env python3
"""M05.02: auditoria descritiva de CSV municipal NORMALIZADO, sem dados oficiais embutidos.

Números monetários em reais nominais, decimais com ponto, sem separador de
milhar. Células vazias = ausência de informação, jamais zero presumido.
Ano da população diferente do ano fiscal bloqueia indicadores per capita.
NÃO estima custo incremental, déficit fiscal nem violação do art. 167 §7º.
"""
from __future__ import annotations
import argparse
import csv
import json
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path

FIELDS = [
    "codigo_ibge", "uf", "municipio", "ano", "ano_populacao", "populacao",
    "receita_total_realizada", "receita_tributaria_realizada",
    "transferencias_correntes_realizadas", "despesa_saude_paga",
    "despesa_educacao_paga", "fonte_contas", "fonte_populacao",
]
MONEY = FIELDS[6:11]
DERIVED = [
    "transferencias_correntes_sobre_receita_total",
    "receita_total_por_habitante", "receita_tributaria_por_habitante",
    "despesa_saude_paga_por_habitante", "despesa_educacao_paga_por_habitante",
    "alertas",
]


def dec(value: str, field: str) -> Decimal | None:
    value = value.strip()
    if not value:
        return None
    if not re.fullmatch(r"\d+(?:\.\d+)?", value):
        raise ValueError(f"{field}: somente números não negativos com ponto decimal")
    return Decimal(value)


def divide(numerator: Decimal | None, denominator: Decimal | None, digits: str) -> str:
    if numerator is None or denominator is None or denominator == 0:
        return ""
    return str((numerator / denominator).quantize(Decimal(digits)))


def run(source: Path, output: Path) -> dict:
    with source.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(line for line in handle if line.strip() and not line.startswith("#"))
        missing = [name for name in FIELDS if name not in (reader.fieldnames or [])]
        if missing:
            raise ValueError("Colunas ausentes: " + ", ".join(missing))
        rows = list(reader)
    if not rows:
        raise ValueError("Nenhuma observação fornecida: não emitir resultado empírico vazio")
    seen = set()
    count_good = Counter()
    count_alerts = Counter()
    results = []
    for lineno, row in enumerate(rows, 2):
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f"Linha {lineno}: colunas irregulares")
        code = row["codigo_ibge"].strip()
        year = row["ano"].strip()
        pop_year = row["ano_populacao"].strip()
        if not re.fullmatch(r"\d{7}", code):
            raise ValueError(f"Linha {lineno}: código IBGE precisa ter sete dígitos")
        if not re.fullmatch(r"20\d{2}", year) or not re.fullmatch(r"20\d{2}", pop_year):
            raise ValueError(f"Linha {lineno}: ano inválido")
        if (code, year) in seen:
            raise ValueError(f"Linha {lineno}: município-ano repetido")
        seen.add((code, year))
        if not re.fullmatch(r"[A-Z]{2}", row["uf"].strip()) or not row["municipio"].strip():
            raise ValueError(f"Linha {lineno}: UF ou município inválido")
        pop = dec(row["populacao"], "populacao")
        if pop is not None and pop != pop.to_integral_value():
            raise ValueError(f"Linha {lineno}: população deve ser inteira")
        finance = {col: dec(row[col], col) for col in MONEY}
        flags = []
        if year != pop_year:
            flags.append("ANO_POPULACAO_DIFERENTE")
        if pop is None or pop == 0:
            flags.append("POPULACAO_AUSENTE_OU_ZERO")
        if not row["fonte_contas"].startswith("https://"):
            flags.append("FONTE_CONTAS_AUSENTE")
        if not row["fonte_populacao"].startswith("https://"):
            flags.append("FONTE_POPULACAO_AUSENTE")
        total = finance["receita_total_realizada"]
        transfers = finance["transferencias_correntes_realizadas"]
        if total is not None and transfers is not None and transfers > total:
            flags.append("TRANSFERENCIAS_ACIMA_RECEITA_TOTAL")
        for flag in flags:
            count_alerts[flag] += 1
        for name in MONEY:
            if finance[name] is not None:
                count_good[name] += 1
        if pop is not None:
            count_good["populacao"] += 1
        result = {key: row[key].strip() for key in FIELDS}
        percap_pop = pop if year == pop_year else None
        result["transferencias_correntes_sobre_receita_total"] = divide(transfers, total, "0.0001")
        result["receita_total_por_habitante"] = divide(total, percap_pop, "0.01")
        result["receita_tributaria_por_habitante"] = divide(finance["receita_tributaria_realizada"], percap_pop, "0.01")
        result["despesa_saude_paga_por_habitante"] = divide(finance["despesa_saude_paga"], percap_pop, "0.01")
        result["despesa_educacao_paga_por_habitante"] = divide(finance["despesa_educacao_paga"], percap_pop, "0.01")
        result["alertas"] = ";".join(flags)
        results.append(result)
    output.mkdir(parents=True, exist_ok=True)
    with (output / "m05_02_indicadores_descritivos.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS + DERIVED)
        writer.writeheader()
        writer.writerows(results)
    report = {
        "natureza": "indicadores descritivos dos dados fornecidos; sem inferência causal ou déficit constitucional",
        "linhas": len(results),
        "entes": len({code for code, _ in seen}),
        "anos": sorted({year for _, year in seen}),
        "campos_preenchidos": dict(sorted(count_good.items())),
        "alertas": dict(sorted(count_alerts.items())),
        "limites": [
            "Sem custo incremental, receita disponível e transferência atribuível, não estimar lacuna do art. 167 §7º.",
            "Transferências correntes não são sinônimo de todos os repasses nem de receita discricionária.",
            "SIOPS, SIOPE e FINBRA exigem reconciliação de estágio da despesa, contabilização e duplicidades.",
            "Nenhum dado ausente foi imputado; amostra não pressuposta exaustiva."
        ]
    }
    (output / "m05_02_qualidade.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entrada", type=Path, required=True)
    parser.add_argument("--saida", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(run(args.entrada, args.saida), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
