#!/usr/bin/env python3
"""Validação ESTRUTURAL de M14.01.03, sem efeitos jurídicos.
Não atesta interpretação de STF, consulta obrigatória, resultado eleitoral, posse,
quórum de PEC, caixa, competência militar ou F6. Executar na branch do PR91.
"""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"modulos"/"M14-transicao"
def check(file,header,n,prefix,key):
    with (ROOT/file).open("r",encoding="utf-8",newline="") as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==header,(file,reader.fieldnames)
        records=list(reader)
    assert len(records)==n,(file,len(records))
    ids=[r["id"] for r in records]
    assert ids==[f"{prefix}{i:02d}" for i in range(1,n+1)],file
    assert len(set(ids))==n
    assert all(None not in r and all(isinstance(x,str) and x.strip() for x in r.values()) for r in records)
    assert all(r[key] in ("H","A_V","V_PENDENTE_PARECER") for r in records)
    return records
q=check("M14-01_03_CHECKLIST_12_PARECERES_E_PROVAS.csv",[
    "id","destinatario","questao_de_parecer","fonte_minima","evidencia_que_resolveria",
    "distincao_nao_negociavel","efeito_se_sem_resposta","situacao"
],12,"Q","situacao")
s=check("M14-01_03_MATRIZ_14_CONDICOES_DE_SEQUENCIA.csv",[
    "id","etapa_de_origem","etapa_seguinte","requisito_de_passagem",
    "fonte_positiva","ato_ou_prova_a_exigir","erro_se_ignorado","quem_revisa","carater","estado"
],14,"S","estado")
e=check("M14-01_03_MATRIZ_8_CONTRAEXEMPLOS_DE_TITULARIDADE.csv",[
    "id","erro_pratico","fonte_de_direito","titulo_que_falta",
    "resposta_exigida","nao_concluir","interface","status"
],8,"E","status")
assert all(r["situacao"]=="V_PENDENTE_PARECER" for r in q)
assert all(r["estado"]=="A_V" for r in s)
assert all(r["status"]=="H" for r in e)
assert any("art9" in r["fonte_positiva"] for r in s)
assert any("EC111" in r["fonte_minima"] for r in q)
assert any("CF57" in r["fonte_minima"] for r in q)
assert (ROOT/"M14-01_03_PARECER_DE_APLICABILIDADE_ELEITORAL_E_TRAVAS_DE_TRANSICAO_v0.1.md").is_file()
print("M14.01.03 QA PASS — 12 quesitos, 14 relações de precedência, 8 contraprovas.")
print("Estatuto: pareceres V/A pendentes; nenhuma CF-NOR ou F6 aprovada.")
