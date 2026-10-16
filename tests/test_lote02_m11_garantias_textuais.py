"""Salvaguardas literais M11/ADCT do lote H experimental; NÃO prova equivalência R3."""
import csv
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def body(number):
    text = (ROOT / "redacao/propostas" / f"CF-NOR-{number}.md").read_text(encoding="utf-8")
    a, b = "<!-- NORMA-INICIO -->", "<!-- NORMA-FIM -->"
    if text.count(a) != 1 or text.count(b) != 1:
        raise ValueError("fonte malformada: " + number)
    return text.split(a, 1)[1].split(b, 1)[0].casefold()

class GuardasM11(unittest.TestCase):
    def test_todas_tres_permancem_hipoteses_pendentes(self):
        with (ROOT / "redacao/indice.csv").open(encoding="utf-8-sig", newline="") as f:
            rows = {r["id"]: r for r in csv.DictReader(f)}
        for number in ("0025", "0028", "0029"):
            with self.subTest(number=number):
                self.assertEqual((rows["CF-NOR-" + number]["modulo"], rows["CF-NOR-" + number]["status"], rows["CF-NOR-" + number]["auditoria_garantias"]), ("M11", "H", "PENDENTE"))
        self.assertEqual(rows["CF-NOR-0028"]["regra_geral"], "CF-NOR-0025")

    def test_direitos_originarios_e_demarcacao(self):
        x = body("0025")
        self.assertIn("direitos originários", x)
        self.assertIn("competindo à união demarcá-las", x)
        self.assertIn("caráter declaratório", x)

    def test_consulta_propria_e_autorizacao_congressual(self):
        x = body("0025")
        self.assertIn("consultados previamente", x)
        self.assertIn("a audiência pública ambiental geral não substitui", x)
        self.assertIn("autorização do congresso nacional", x)

    def test_remocao_excecoes_e_retorno(self):
        x = body("0028")
        self.assertIn("é vedada a remoção", x)
        self.assertIn("catástrofe ou epidemia", x)
        self.assertIn("retorno imediato", x)

    def test_nulidades_terceiros_e_reserva_mineral(self):
        x = body("0028")
        self.assertIn("são nulos e extintos", x)
        self.assertIn("boa-fé", x)
        self.assertIn("não se aplicam às terras indígenas", x)

    def test_propriedade_quilombola_e_titulacao_declaratoria(self):
        x = body("0029")
        self.assertIn("propriedade definitiva", x)
        self.assertIn("emitir-lhes os títulos", x)
        self.assertIn("sem tornar a expedição do título condição constitutiva", x)

    def test_terceiros_quilombolas_nao_sao_nulidades_indigenas(self):
        x = body("0029")
        self.assertIn("direitos legítimos de terceiros", x)
        self.assertNotIn("são nulos e extintos", x)
        self.assertNotIn("usufruto exclusivo", x)

if __name__ == "__main__":
    unittest.main()
