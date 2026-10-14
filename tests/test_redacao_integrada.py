"""Testes estruturais da montagem do anteprojeto; não validam direitos."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import gerar_anteprojeto as generator


class NormativeAssemblyTests(unittest.TestCase):
    def test_generated_view_is_identical_to_source(self):
        self.assertEqual(
            generator.OUTPUT.read_text(encoding="utf-8"), generator.build()
        )

    def test_no_source_annotations_are_merged_into_norm_text(self):
        merged = generator.build()
        self.assertIn("CF-NOR-0001", merged)
        self.assertIn("CF-NOR-0002", merged)
        self.assertIn("NÃO RATIFICADO", merged)
        self.assertNotIn("<!-- NORMA-INICIO -->", merged)
        self.assertNotIn("## Melhor objeção", merged)

    def test_rejected_when_two_norms_share_same_text(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "redacao/propostas").mkdir(parents=True)
            norm = "<!-- NORMA-INICIO -->\nTexto normativo igual.\n<!-- NORMA-FIM -->"
            for key in ["CF-NOR-0001", "CF-NOR-0002"]:
                (root / f"redacao/propostas/{key}.md").write_text(norm, encoding="utf-8")
            index = root / "redacao/indice.csv"
            with index.open("w", encoding="utf-8", newline="") as fh:
                fields = sorted(generator.COLUMNS)
                writer = csv.DictWriter(fh, fieldnames=fields)
                writer.writeheader()
                for index_num, key in enumerate(["CF-NOR-0001", "CF-NOR-0002"], 1):
                    writer.writerow({
                        "id": key, "ordem": f"{index_num:04d}", "tema": "teste",
                        "modulo": "M00", "tipo": "A", "status": "H",
                        "arquivo": f"redacao/propostas/{key}.md",
                    })
            with patch.object(generator, "ROOT", root), patch.object(generator, "INDEX", index):
                with self.assertRaisesRegex(ValueError, "Texto idêntico"):
                    generator.build()

    def test_special_rule_requires_general_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "redacao/propostas").mkdir(parents=True)
            key = "CF-NOR-0001"
            (root / f"redacao/propostas/{key}.md").write_text(
                "<!-- NORMA-INICIO -->\nHipótese.\n<!-- NORMA-FIM -->",
                encoding="utf-8",
            )
            index = root / "redacao/indice.csv"
            with index.open("w", encoding="utf-8", newline="") as fh:
                writer = csv.DictWriter(fh, fieldnames=sorted(generator.COLUMNS))
                writer.writeheader()
                writer.writerow({
                    "id": key, "ordem": "0001", "tema": "teste", "modulo": "M00",
                    "tipo": "E", "status": "H", "arquivo": f"redacao/propostas/{key}.md",
                })
            with patch.object(generator, "ROOT", root), patch.object(generator, "INDEX", index):
                with self.assertRaisesRegex(ValueError, "sem regra geral"):
                    generator.build()


if __name__ == "__main__":
    unittest.main()
