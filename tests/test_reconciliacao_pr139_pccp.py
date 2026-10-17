"""Reconciliacao documental PR #139 com PCCP; CI nao homologa constitucionalidade."""
import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SELECTED = {
    "CF-NOR-0021": "M07",
    "CF-NOR-0022": "M08",
    "CF-NOR-0023": "M10",
    "CF-NOR-0025": "M11",
    "CF-NOR-0028": "M11",
    "CF-NOR-0029": "M11",
}

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

class TestReconciliacao139Pccp(unittest.TestCase):
    def test_26_hipoteses_sem_promocao(self):
        with (ROOT / "redacao/indice.csv").open(encoding="utf-8-sig", newline="") as h:
            rows = list(csv.DictReader(h))
        self.assertEqual(len(rows), 26)
        self.assertEqual(len({r["id"] for r in rows}), 26)
        self.assertEqual(len({r["ordem"] for r in rows}), 26)
        self.assertEqual({r["status"] for r in rows}, {"H"})
        for row in rows:
            self.assertTrue((ROOT / row["arquivo"]).is_file(), row["id"])
        byid = {r["id"]: r for r in rows}
        for key, mod in SELECTED.items():
            self.assertEqual((byid[key]["modulo"], byid[key]["auditoria_garantias"]), (mod, "PENDENTE"))

    def test_pccp_preferencia_apenas_provisoria(self):
        dec = read("governanca/03_DECISOES.md")
        entry = next(line for line in dec.splitlines() if line.startswith("| CF-DEC-006 |"))
        self.assertIn("P (orientação provisória expressa)", entry)
        self.assertIn("sem ratificar", entry)
        agenda = read("central/03_PAUTA_DELIBERACAO_PROGRESSIVA.md")
        self.assertIn("P-B escolhida expressamente pelo usuário", agenda)
        self.assertIn("não D", agenda)
        self.assertIn("BLOQUEADO_POR_DEPENDENCIA", agenda)

    def test_auditorias_r3_presentes_sem_fechamento(self):
        docs = (
            "auditoria/LOTE_01_M07_M08_M10_MATRIZ_R3_20261016.md",
            "auditoria/LOTE_02_M11_ADCT68_R3_20261016.md",
            "auditoria/M14_ADCT68_FICHA_TRANSICAO_20261016.md",
            "auditoria/RECONCILIACAO_LOTES_01_02_20261016.md",
        )
        for path in docs:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file())
                self.assertIn("R3", read(path))
        audit = read("auditoria/RECONCILIACAO_MAIN_PCCP_PR139_20261017.md")
        for word in ("CF175", "CF225", "CF231", "ADCT68", "G1", "G2", "G3", "G4",
                     "independente", "não ratificar"):
            self.assertIn(word, audit)

    def test_workflow_executa_as_duas_familias(self):
        workflow = read(".github/workflows/validar-estrutura.yml")
        suites = (
            "test_m05_02_auditar_dados.py", "test_redacao_integrada.py",
            "test_controle_operacional.py", "test_pccp_governanca.py",
            "test_lote02_m11_garantias_textuais.py", "test_lote01_garantias_textuais.py",
            "test_integracao_lotes_01_02.py", "test_concordancia_paragrafos_r3.py",
            "test_reconciliacao_pr139_pccp.py",
        )
        for name in suites:
            self.assertEqual(workflow.count("-p '" + name + "'"), 1, name)
            self.assertTrue((ROOT / "tests" / name).is_file(), name)
        self.assertIn("gerar_anteprojeto.py --check", workflow)
        self.assertIn("controle_operacional.py --check", workflow)

    def test_adct_e_no_r3_igual_d(self):
        audit = read("auditoria/RECONCILIACAO_MAIN_PCCP_PR139_20261017.md")
        self.assertIn("26 H / 0 D", audit)
        self.assertIn("20 H", audit)
        self.assertIn("seis H", audit)
        self.assertIn("PR #139", audit)
        self.assertIn("PR #137", audit)
        self.assertIn("R3_PENDENTE", audit)
        self.assertNotIn("| CF-DEC-006 | D |", read("governanca/03_DECISOES.md"))

if __name__ == "__main__":
    unittest.main()
