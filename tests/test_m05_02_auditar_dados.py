"""Testes sintéticos do pipeline M05.02. NENHUM registro é dado oficial."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from m05_02_auditar_dados import FIELDS, run


def make_row(code="3550308", year="2024", pop_year="2024"):
    return {
        "codigo_ibge": code, "uf": "SP", "municipio": "Município FICTÍCIO",
        "ano": year, "ano_populacao": pop_year, "populacao": "100",
        "receita_total_realizada": "1000.00",
        "receita_tributaria_realizada": "200.00",
        "transferencias_correntes_realizadas": "500.00",
        "despesa_saude_paga": "125.00", "despesa_educacao_paga": "",
        "fonte_contas": "https://exemplo.invalid/contas",
        "fonte_populacao": "https://exemplo.invalid/pop",
    }


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.path = self.root / "input.csv"
        self.output = self.root / "result"

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rows):
        with self.path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)

    def test_does_not_impute_empty_values(self):
        self.write([make_row()])
        report = run(self.path, self.output)
        self.assertEqual(report["linhas"], 1)
        with (self.output / "m05_02_indicadores_descritivos.csv").open(encoding="utf-8") as h:
            result = next(csv.DictReader(h))
        self.assertEqual(result["transferencias_correntes_sobre_receita_total"], "0.5000")
        self.assertEqual(result["receita_total_por_habitante"], "10.00")
        self.assertEqual(result["despesa_educacao_paga_por_habitante"], "")

    def test_mismatched_population_year_blocks_per_capita(self):
        self.write([make_row(pop_year="2026")])
        report = run(self.path, self.output)
        self.assertEqual(report["alertas"]["ANO_POPULACAO_DIFERENTE"], 1)
        with (self.output / "m05_02_indicadores_descritivos.csv").open(encoding="utf-8") as h:
            result = next(csv.DictReader(h))
        self.assertEqual(result["receita_total_por_habitante"], "")

    def test_duplicate_entity_year_is_rejected(self):
        self.write([make_row(), make_row()])
        with self.assertRaisesRegex(ValueError, "repetido"):
            run(self.path, self.output)

    def test_empty_csv_rejected(self):
        self.write([])
        with self.assertRaisesRegex(ValueError, "Nenhuma observação"):
            run(self.path, self.output)

    def test_bad_decimal_rejected(self):
        row = make_row()
        row["receita_total_realizada"] = "1.000,00"
        self.write([row])
        with self.assertRaisesRegex(ValueError, "não negativos"):
            run(self.path, self.output)


if __name__ == "__main__":
    unittest.main()
