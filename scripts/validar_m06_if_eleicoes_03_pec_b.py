#!/usr/bin/env python3
"""M06-IF-ELEI-003: auditoria ESTRUTURAL de cláusulas funcionais B.
Não certifica constitucionalidade do parlamentarismo ou PEC, cabimento de MS,
consulta obrigatória, direitos efetivos ou F6. Executar na branch PR96.
"""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]/"modulos"/"M06-justica"

def load(file,cols,n,prefix,state,allowed):
    with (ROOT/file).open(encoding="utf-8",newline="") as f:
        rd=csv.DictReader(f)
        assert rd.fieldnames==cols,(file,rd.fieldnames)
        rows=list(rd)
    assert len(rows)==n
    assert [x["id"] for x in rows]==[f"{prefix}{i:02d}" for i in range(1,n+1)]
    assert all(None not in x and all(isinstance(v,str) and v.strip() for v in x.values()) for x in rows)
    assert all(x[state] in allowed for x in rows)
    return rows

clauses=load("M06-IF_ELEICOES_03_MATRIZ_16_CLAUSULAS_B_H_ART60.csv",
["id","clausula_funcional_nao_normativa","fonte_M03","nucleo_art60","defesa_constitucional_condicional","versao_critica_ou_omissao","triagem","prova_necessaria","pareceres_pendentes","F6"],
16,"BH-","triagem",{"DEFENSAVEL_CONDICIONAL","ALTO_RISCO_SE_ABUSIVO","INDETERMINADO_SEM_TEXTO"})
assert all(r["F6"]=="ABERTA" for r in clauses)
contrary=load("M06-IF_ELEICOES_03_MATRIZ_8_CONTRAEXEMPLOS_NUCLEO.csv",
["id","contraexemplo_de_captura","clausulas_alcancadas","risco_a_nucleo","objeção_qualificada","salvaguarda_em_teste","resultado","prova_necessaria","status"],
8,"X","status",{"H"})
gates=load("M06-IF_ELEICOES_03_CHECKLIST_10_PROVAS_ANTES_DA_PEC.csv",
["id","pergunta_para_pec_concreta","ato_ou_documento","nucleo_ou_norma","criterio_de_saida","responsavel","status"],
10,"K","status",{"ABERTA"})
assert (ROOT/"M06-IF_ELEICOES_03_PARECER_ARTICULADO_TESTE_PARLAMENTARISMO_B_ART60_v0.1.md").exists()
print("M06-IF-ELEI-003 QA PASS: 16 cláusulas H, 8 ataques e 10 portas ABERTAS.")
print("Atriagem condiciona o texto; nenhuma PEC, F6, norma ou votação aprovada.")
