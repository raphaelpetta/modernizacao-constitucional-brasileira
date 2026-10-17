"""Guardas documentais PCCP. Nao homologam conteudo juridico/constituinte."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

def document(path):
    return (ROOT / path).read_text(encoding="utf-8")

class TestPccpGovernanca(unittest.TestCase):
    def test_f0_f8_f6_nao_sequencial_e_proveniencia_custo(self):
        s = document("governanca/02_METODOLOGIA.md")
        for step in range(9):
            self.assertIn("F" + str(step), s)
        self.assertIn("F7 pode produzir H antes de F6", s)
        self.assertIn("F6 é acionada", s)
        self.assertIn("F8 audita", s)
        self.assertIn("## Avaliação de custo efetivo", s)
        self.assertIn("custo total efetivo", s)
        self.assertIn("Convergência Constitucional Progressiva", s)

    def test_tres_niveis_e_decisao_material_expressa(self):
        progress = document("governanca/16_PROGRESSIVIDADE_DECISORIA.md")
        for key in ("**Orientação**", "**Princípio/arquitetura**", "**Redação**"):
            self.assertIn(key, progress)
        self.assertIn("ratificação tácita", progress)
        self.assertIn("revisão independente humana identificável", document(
            "governanca/POLITICA_CONSOLIDACAO_E_FECHAMENTO_20261015.md"))

    def test_cinco_tipos_fechamento_e_reabertura(self):
        s = document("governanca/POLITICA_CONSOLIDACAO_E_FECHAMENTO_20261015.md")
        for target in ("Fechamento técnico/documental", "Estabilização material",
                       "Fechamento normativo local", "Fechamento sistêmico",
                       "Fechamento global", "Reabertura motivada"):
            self.assertIn(target, s)
        self.assertIn("G1", s)
        self.assertIn("G2", s)
        self.assertIn("G3", s)
        self.assertIn("G4", s)

    def test_decisao_operacional_sem_ratificacao_de_conteudo(self):
        s = document("governanca/03_DECISOES.md")
        lines = [line for line in s.splitlines() if line.startswith("| CF-DEC-016 |")]
        self.assertEqual(len(lines), 1)
        self.assertIn("D (exclusivamente operacional)", lines[0])
        self.assertIn("jamais ratificação", lines[0])
        self.assertIn("16/10/2026", lines[0])
        self.assertNotIn("CF-NOR-002", lines[0])

    def test_pauta_sem_nova_h_ou_d_de_merito(self):
        agenda = document("central/03_PAUTA_DELIBERACAO_PROGRESSIVA.md")
        ids = re.findall(r"\bPCCP-Q\d{2}\b", agenda)
        self.assertEqual(set(ids), {"PCCP-Q01", "PCCP-Q02", "PCCP-Q03"})
        self.assertIn("**Nenhuma das três questões abaixo foi materialmente ratificada D**", agenda)
        for label in ("PREFERENCIA_PROVISORIA", "BLOQUEADO_POR_DEPENDENCIA",
                      "PESQUISA_FOCAL", "APTO_A_DELIBERAR", "FECHADO_NO_RECORTE"):
            self.assertIn(label, agenda)
        self.assertIn("**Orientação P**", agenda) if "**Orientação P**" in agenda else self.assertIn("**orientação P**", agenda)
        self.assertIn("revisão jurídica humana independente", agenda)

    def test_pauta_unica_e_ganho_global_d(self):
        select = document("governanca/19_POLITICA_GANHO_MARGINAL_GLOBAL.md")
        index = document("central/01_POLITICA_INTEGRACAO_E_CONCORRENCIA.md")
        layering = document("governanca/17_EXECUCAO_CAMADAS_E_AUDITORIA.md")
        self.assertIn("D (tornar questão deliberável", select)
        self.assertIn("03_PAUTA_DELIBERACAO_PROGRESSIVA.md", index)
        self.assertIn("03_PAUTA_DELIBERACAO_PROGRESSIVA.md", layering)
        self.assertIn("H/V/I", layering)
        self.assertIn("auditoria humana independente", layering)

    def test_q01_maduro_apenas_para_orientacao_p(self):
        agenda = document("central/03_PAUTA_DELIBERACAO_PROGRESSIVA.md")
        row = next(x for x in agenda.splitlines() if x.startswith("| PCCP-Q01 |"))
        self.assertIn("`APTO_A_DELIBERAR`", row)
        self.assertIn("SOMENTE para preferência orientadora P", row)
        self.assertIn("não escolha do usuário nem D", row)
        for option in ("P-A", "P-B", "P-C", "D0"):
            self.assertIn(option, agenda)
        self.assertIn("`CF-DEC-006=H/P` intacto", agenda)
        self.assertIn("nenhuma resposta P-A/P-B/P-C/D0 foi atribuída", agenda)

    def test_f6_pccp_nao_confunde_governo_parlamento_e_via(self):
        agenda = document("central/03_PAUTA_DELIBERACAO_PROGRESSIVA.md")
        executive = document("central/04_PAUTA_EXECUTIVA_F6_20261015.md")
        for text in (agenda, executive):
            self.assertIn("P1/P2/P3", text)
            self.assertIn("S1/C3", text)
            self.assertIn("revisão jurídica humana independente r3", text.casefold())
            self.assertIn("art.60", text)
        self.assertIn("não inferir admissibilidade de uma PEC", executive)
        self.assertIn("gabinete", executive)

    def test_f6_sem_voto_automatico_por_comando_de_continuacao(self):
        executive = document("central/04_PAUTA_EXECUTIVA_F6_20261015.md")
        self.assertIn("“bora”, “continue”", executive)
        self.assertIn("não conta como voto", executive)
        decisions = document("governanca/03_DECISOES.md")
        self.assertIn("| CF-DEC-006 | H/P |", decisions)
        self.assertNotIn("CF-DEC-017", decisions)

if __name__ == "__main__":
    unittest.main()
