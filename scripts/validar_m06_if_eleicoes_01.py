#!/usr/bin/env python3
"""Validação apenas ESTRUTURAL da interface M06-M02-M14.
Não atesta cabimento real, competência judicial, mérito de PEC, legalidade de
plebiscito, lei eleitoral aplicável, mandato, direito a crédito ou decisão F6.
Rodar: python3 scripts/validar_m06_if_eleicoes_01.py
"""
import csv
from pathlib import Path

DIR=Path(__file__).resolve().parents[1]/"modulos"/"M06-justica"
def check(file, columns, n, prefix, field, accepted):
    with (DIR/file).open(encoding="utf-8",newline="") as fp:
        reader=csv.DictReader(fp)
        assert reader.fieldnames == columns,(file,reader.fieldnames)
        rows=list(reader)
    assert len(rows)==n,(file,len(rows))
    assert [row["id"] for row in rows]==[f"{prefix}{i:02d}" for i in range(1,n+1)],file
    assert all(None not in row and all(str(value).strip() for value in row.values()) for row in rows),file
    assert all(row[field] in accepted for row in rows),file
    return rows
acts=check("M06-IF_ELEICOES_01_MATRIZ_16_ATOS_E_REMEDIOS.csv",
    ["id","fase","ato_documentado","autoridade_ou_sujeito","objeto_de_controle","via_potencial_atual","condicao_de_cabimento_a_verificar","tutela_possivel_sem_usurpar_poder","risco_de_excesso","documento_probatorio","fonte_primaria","estado"],16,"J","estado",{"H","A","V"})
tests=check("M06-IF_ELEICOES_01_MATRIZ_12_TESTES_DE_ABUSO_JURISDICIONAL.csv",
    ["id","abuso_a_evitar","fase","premissa_H","fonte_positiva_ou_precedente","resultado_de_controle_condicional","limite_do_juiz","objeção_forte","interface","status"],12,"G","status",{"H","A","V"})
gates=check("M06-IF_ELEICOES_01_PAUTA_10_PONTOS_F6_ABERTOS.csv",
    ["id","foco_de_decisao","pergunta_material","alternativas_de_pesquisa_H","fundamento_verificavel","risco_de_controle_excessivo","risco_de_controle_insuficiente","parecer_a_colher","status"],10,"F6-J","status",{"ABERTA"})
assert {row["fase"] for row in acts} >= {"P0_PEC","P1_CONSULTA","P2_EC","P3_ELEICAO"}
assert all(row["status"]=="ABERTA" for row in gates)
assert any("MS32033" in row["fonte_primaria"] for row in acts)
assert any("Lei9709 art9" in row["fonte_primaria"] for row in acts)
assert (DIR/"M06-IF_ELEICOES_01_PARECER_AUTONOMO_CONTROLE_JUDICIAL_DE_REFORMA_E_PLEITO_v0.1.md").is_file()
print("M06-IF-ELEI-001 QA PASS: 16 atos, 12 abusos, 10 portas F6 abertas.")
print("NÃO valida tese de plebiscito obrigatório nem permite controlar toda PEC por ADI.")
