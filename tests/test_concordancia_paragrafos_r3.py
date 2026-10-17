"""Confere concordancia editorial por paragrafo em M07/M10 (nao equivalencia juridica)."""
from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1] / "redacao" / "propostas"


def ler(ident):
    return (BASE / ("CF-NOR-" + ident + ".md")).read_text(encoding="utf-8")


def corpo(ident):
    texto = ler(ident)
    a, b = "<!-- NORMA-INICIO -->", "<!-- NORMA-FIM -->"
    assert texto.count(a) == texto.count(b) == 1
    return [x.strip().casefold() for x in texto.split(a, 1)[1].split(b, 1)[0].strip().split("\n\n") if x.strip()]


def coluna_destino(ident, ancora):
    linhas = [x for x in ler(ident).splitlines() if x.startswith("| " + ancora + " |")]
    assert len(linhas) == 1, (ident, ancora, linhas)
    colunas = [x.strip() for x in linhas[0].strip("|").split("|")]
    assert len(colunas) == 3
    return colunas[1]


class ConcordanciaR3(unittest.TestCase):
    def conferir(self, ident, casos, total):
        paragrafos = corpo(ident)
        self.assertEqual(len(paragrafos), total, "alteracao exige nova concordancia")
        for ancora, pos, trecho in casos:
            with self.subTest(ident=ident, ancora=ancora):
                self.assertIn(trecho.casefold(), paragrafos[pos - 1])
                self.assertIn("§" + str(pos), coluna_destino(ident, ancora))

    def test_m07_garantias_e_destinos(self):
        self.conferir("0021", [
            ("CF 5º XXXIII (informação)", 1, "informação adequada"),
            ("CF 5º XXXIV a (petição)", 2, "independentemente do pagamento de taxas"),
            ("CF 5º XXXIV b (certidões)", 2, "obtenção de certidões"),
            ("CF 5º LIV (devido processo)", 3, "nos processos administrativos"),
            ("CF 5º LV (contraditório e defesa)", 3, "contraditório e a ampla defesa"),
            ("CF 5º LXXVIII (duração razoável)", 1, "prazo razoável"),
            ("CF 5º X e LXXIX (privacidade/dados)", 5, "proteção de dados pessoais"),
            ("CF 37 caput/§3º (administração/usuários)", 1, "atendimento acessível"),
            ("CF 70/74 (controle)", 5, "mecanismos de controle"),
            ("CDPD e acessibilidade", 4, "acessibilidade, apoio apropriado"),
        ], 5)

    def test_m10_garantias_e_destinos(self):
        self.conferir("0023", [
            ("Art. 225 caput (direito, dever do poder público/coletividade, gerações)", 1, "todos têm direito"),
            ("Art. 225 §1 I (processos ecológicos)", 2, "processos ecológicos essenciais"),
            ("Art. 225 §1 II (patrimônio genético)", 2, "patrimônio genético"),
            ("Art. 225 §1 VII (proteção da fauna e flora, extinção e crueldade)", 3, "proteger a fauna e a flora"),
            ("Art. 225 §7 (práticas desportivas com animais e requisitos culturais específicos)", 4, "práticas desportivas"),
            ("Art. 225 §1 IV (obra/atividade, significância, EIA prévio, publicidade)", 6, "estudo prévio de impacto ambiental"),
        ], 6)

    def test_eia_nao_se_confunde_com_bem_estar(self):
        cultural = coluna_destino("0023", "Art. 225 §7 (práticas desportivas com animais e requisitos culturais específicos)")
        eia = coluna_destino("0023", "Art. 225 §1 IV (obra/atividade, significância, EIA prévio, publicidade)")
        self.assertIn("§4", cultural)
        self.assertIn("§5", cultural)
        self.assertIn("padrões legais mínimos", corpo("0023")[4])
        self.assertEqual(eia, "§6 H (EIA prévio e publicidade)")
        self.assertNotIn("estudo prévio de impacto ambiental", corpo("0023")[4])


if __name__ == "__main__":
    unittest.main()
