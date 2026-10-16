"""Testes literais de salvaguardas do lote H: não comprovam equivalência constitucional."""
import csv
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def norma(ident):
    text = (ROOT / "redacao/propostas" / f"CF-NOR-{ident}.md").read_text(encoding="utf-8")
    ini, fim = "<!-- NORMA-INICIO -->", "<!-- NORMA-FIM -->"
    if text.count(ini) != 1 or text.count(fim) != 1:
        raise ValueError("marcadores malformados: " + ident)
    return text.split(ini, 1)[1].split(fim, 1)[0].casefold()

class GuardasH(unittest.TestCase):
    def test_indice_permanece_h_pendente(self):
        with (ROOT / "redacao/indice.csv").open(encoding="utf-8-sig", newline="") as handle:
            data = {row["id"]: row for row in csv.DictReader(handle)}
        for ident, mod in [("0021", "M07"), ("0022", "M08"), ("0023", "M10")]:
            with self.subTest(ident=ident):
                row = data["CF-NOR-" + ident]
                self.assertEqual((row["modulo"], row["status"], row["auditoria_garantias"]), (mod, "H", "PENDENTE"))
    def test_peticao_e_certidao_sem_taxas(self):
        text = norma("0021")
        self.assertIn("independentemente do pagamento de taxas", text)
        self.assertIn("direito de petição aos poderes públicos", text)
        self.assertIn("obtenção de certidões", text)
    def test_delegacao_exige_licitacao(self):
        text = norma("0022")
        self.assertIn("concessão ou permissão", text)
        self.assertIn("será precedida de licitação", text)
        self.assertIn("na forma da lei", text)
    def test_eia_previo_e_publicidade(self):
        text = norma("0023")
        self.assertIn("significativa degradação", text)
        self.assertIn("estudo prévio de impacto ambiental", text)
        self.assertIn("ao qual se dará publicidade", text)
    def test_fauna_flora_extincao_e_crueldade(self):
        text = norma("0023")
        self.assertIn("proteger a fauna e a flora", text)
        self.assertIn("extinção de espécies", text)
        self.assertIn("animais a crueldade", text)

    def test_cultura_animal_condicoes_especificas(self):
        text = norma("0023")
        self.assertIn("práticas desportivas", text)
        self.assertIn("manifestações culturais", text)
        self.assertIn("bens de natureza imaterial", text)
        self.assertIn("lei específica", text)
        self.assertIn("bem-estar dos animais", text)


if __name__ == "__main__":
    unittest.main()
