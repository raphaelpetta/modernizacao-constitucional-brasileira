#!/usr/bin/env python3
"""M03.02.14: QA apenas estrutural de competências A/B-D/B-I/C e portas F6.
Não valida constitucionalidade, competência real, plebiscito, nem decisão D/F6.
"""
import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"modulos"/"M03-parlamento"
def check(fn,columns,n,prefix):
    with (ROOT/fn).open(encoding="utf-8",newline="") as f:
        rd=csv.DictReader(f)
        assert rd.fieldnames==columns,(fn,rd.fieldnames)
        rows=list(rd)
    assert len(rows)==n,(fn,len(rows))
    assert [x["id"] for x in rows]==[f"{prefix}{i:02d}" for i in range(1,n+1)],fn
    assert all(None not in x and all(isinstance(v,str) and v.strip() for v in x.values()) for x in rows),fn
    assert all(x["estado"]=="ABERTA" for x in rows),fn
    return rows
acts=check("M03-02_14_MATRIZ_16_ATOS_TITULARIDADE_A_BD_BI_C.csv",
["id","ato_competencia","A_decisao_e_forma","B_D_decisao_e_forma","B_I_decisao_e_forma","C_decisao_e_forma","refrendo_ou_certificacao_necessarios","controle_e_limite","risco_de_vacuo_ou_captura","parecer_pendente","estado"],16,"F")
gates=check("M03-02_14_MATRIZ_12_TRAVAS_ORIGEM_MANDATO_E_F6.csv",
["id","porta_F6_ainda_aberta","opcoes_de_pesquisa_sem_escolha","evidencia_a_obter","risco_se_nao_for_resolvida","dono_do_parecer","estado"],12,"P")
assert all(all(x[k] for k in ["A_decisao_e_forma","B_D_decisao_e_forma","B_I_decisao_e_forma","C_decisao_e_forma"]) for x in acts)
assert (ROOT/"M03-02_14_PARECER_COMPETENCIAS_CHEFIA_ESTADO_A_B_C_v0.1.md").is_file()
print("M03.02.14 PASS: 16 atos x 4 variantes analíticas; 12 portas F6 ABERTAS.")
print("Controle ESTRUTURAL, não ratificação de chefe Estado, regime ou CF-NOR.")
