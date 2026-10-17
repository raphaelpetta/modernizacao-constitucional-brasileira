"""Conferencia de coexistencia documental H, sem provar equivalencia juridica R3."""
import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDS = {
    "CF-NOR-0021": "M07", "CF-NOR-0022": "M08", "CF-NOR-0023": "M10",
    "CF-NOR-0025": "M11", "CF-NOR-0028": "M11", "CF-NOR-0029": "M11",
}

def norm(number):
    content = (ROOT / "redacao/propostas" / (number + ".md")).read_text(encoding="utf-8")
    a, b = "<!-- NORMA-INICIO -->", "<!-- NORMA-FIM -->"
    if content.count(a) != 1 or content.count(b) != 1:
        raise ValueError("marcadores incompletos: " + number)
    return content.split(a, 1)[1].split(b, 1)[0].casefold()

class TesteIntegracaoR3(unittest.TestCase):
    def test_ids_ordem_e_status_sem_promocao(self):
        with (ROOT / "redacao/indice.csv").open(encoding="utf-8-sig", newline="") as fh:
            entries = list(csv.DictReader(fh))
        rows = {row["id"]: row for row in entries}
        self.assertEqual(len(entries), len(rows), "IDs duplicados")
        self.assertEqual(len(entries), len({row["ordem"] for row in entries}), "ordem duplicada")
        self.assertEqual([row["ordem"] for row in entries], sorted(r["ordem"] for r in entries))
        for key, module in IDS.items():
            with self.subTest(key=key):
                row = rows[key]
                self.assertEqual((row["modulo"], row["status"], row["auditoria_garantias"]),
                                 (module, "H", "PENDENTE"))
        self.assertEqual(rows["CF-NOR-0028"]["regra_geral"], "CF-NOR-0025")

    def test_licitacao_meio_ambiente_peticao(self):
        self.assertIn("será precedida de licitação", norm("CF-NOR-0022"))
        self.assertIn("estudo prévio de impacto ambiental", norm("CF-NOR-0023"))
        self.assertIn("padrões legais mínimos de bem-estar animal", norm("CF-NOR-0023"))
        self.assertIn("direito de petição aos poderes públicos", norm("CF-NOR-0021"))

    def test_nao_confundir_propriedade_indigena_e_quilombola(self):
        self.assertIn("são nulos e extintos", norm("CF-NOR-0028"))
        quilombola = norm("CF-NOR-0029")
        self.assertIn("procedimento regular de desapropriação", quilombola)
        self.assertIn("sem aplicar automaticamente", quilombola)
        self.assertNotIn("são nulos e extintos", quilombola)

    def test_uma_vista_por_id_e_ambas_auditorias(self):
        view = (ROOT / "redacao/anteprojeto-de-trabalho.md").read_text(encoding="utf-8")
        self.assertIn("NÃO RATIFICADO", view)
        for key in IDS:
            self.assertEqual(view.count("## " + key + " — "), 1, key)
        for filename in (
            "LOTE_01_M07_M08_M10_MATRIZ_R3_20261016.md",
            "LOTE_02_M11_ADCT68_R3_20261016.md",
            "M14_ADCT68_FICHA_TRANSICAO_20261016.md",
            "RECONCILIACAO_LOTES_01_02_20261016.md",
        ):
            self.assertTrue((ROOT / "auditoria" / filename).is_file(), filename)

if __name__ == "__main__":
    unittest.main()
