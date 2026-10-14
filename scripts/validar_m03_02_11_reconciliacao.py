#!/usr/bin/env python3
"""M03.02.11 — reconciliador de tokens de fonte FICTÍCIOS, não orçamento real.
Uso: python3 scripts/validar_m03_02_11_reconciliacao.py
Valida integridade do catálogo e confronta 20 resultados esperados, sem F6, custo, caixa
ou autorização jurídico-financeira. Não transforma reserva técnica em dotação.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "modulos" / "M03-parlamento"
FILE_S = "M03-02_11_CATALOGO_11_FONTES_HIPOTETICAS.csv"
FILE_C = "M03-02_11_20_REIVINDICACOES_E_RESULTADOS.csv"
FILE_T = "M03-02_11_MATRIZ_12_TESTES_RECONCILIACAO.csv"
FILE_G = "M03-02_11_PORTAS_F6_RECONCILIACAO.csv"

def load(filename, expected_count, cols):
    with (ROOT / filename).open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == cols, (filename, reader.fieldnames)
        rows = list(reader)
    assert len(rows) == expected_count, (filename, len(rows), expected_count)
    assert all(None not in row for row in rows), (filename, "campos excedentes")
    assert all(all(isinstance(v,str) and v.strip() for v in row.values()) for row in rows), filename
    return rows

resources=load(FILE_S,11,[
    "source_id","exercicio","classe","destinacao_permitida","estado_hipotetico",
    "titularidade","limite_ilustrativo","valor_monetario","fundamento_a_verificar","status_epistemico"
])
claims=load(FILE_C,20,[
    "claim_id","exercicio","objeto","source_id","apoio_votos_H","iniciativa_H",
    "base_material_H","resultado_esperado","razão_do_teste","status_epistemico"
])
tests=load(FILE_T,12,[
    "id","ataque","rastro_de_casos","camada_violada","resultado_exigido",
    "teste_de_exequibilidade","efeito_politico_fiscal","risco_residual",
    "pareceres_exigidos","status"
])
gates=load(FILE_G,10,[
    "gate_id","sequencia","tema_f6","alternativas_H","evidencia_nesta_rodada",
    "parecer_pendente","proibicao_ate_deliberacao","status"
])
rs={r["source_id"]:r for r in resources}
assert len(rs)==len(resources)
assert len({r["claim_id"] for r in claims})==len(claims)
assert {r["id"] for r in tests}=={f"G{i:02d}" for i in range(1,13)}
assert {r["gate_id"] for r in gates}=={f"F6-11-{i:02d}" for i in range(10)}
assert sorted(int(r["sequencia"]) for r in gates)==list(range(10))
assert all(r["status"]=="ABERTA" for r in gates)
assert all(r["status_epistemico"]=="H" for r in claims+resources)
reserved=set()
outcomes={}
for row in claims:
    obj=row["objeto"]
    src_id=row["source_id"]
    if obj=="REPARTICAO_CONSTIT":
        assert src_id in rs and rs[src_id]["classe"]=="RECEITA_PARTILHADA"
        result="NAO_SUBMETER_TITULARIDADE_A_VOTO"
    elif row["apoio_votos_H"]!="SIM_H":
        result="SEM_MAIORIA_ILUSTRATIVA"
    elif row["iniciativa_H"]!="ADMISSIVEL_H":
        result="BLOQUEIO_INICIATIVA"
    elif row["base_material_H"]!="EXISTENTE_H":
        result="BLOQUEIO_BASE_MATERIAL"
    elif src_id=="SEM_FONTE":
        result="PENDENTE_FONTE"
    else:
        assert src_id in rs, (row["claim_id"],src_id)
        source=rs[src_id]
        state=source["estado_hipotetico"]
        if state=="CREDITO_NAO_AUTORIZADO_H":
            result="BLOQUEIO_CREDITO_NOVO"
        elif state=="EXPIRADA_H":
            result="BLOQUEIO_EXPIRADA"
        elif state=="COMPROMETIDA_H":
            result="BLOQUEIO_COMPROMISSO_PREVIO"
        elif state=="NAO_VERIFICADA_H":
            result="PENDENTE_DISPONIBILIDADE"
        elif source["exercicio"]!=row["exercicio"]:
            result="BLOQUEIO_EXERCICIO"
        else:
            purpose=source["destinacao_permitida"]
            eligible=((purpose=="OBRIGACAO_SERVICO" and obj in ("HOSPITAL","ESCOLA"))
                     or (purpose=="EDUCACAO" and obj=="ESCOLA")
                     or (purpose=="CONVENIO_EXIGIVEL" and obj=="CONVENIO"))
            if not eligible:
                result="BLOQUEIO_VINCULACAO"
            elif src_id in reserved:
                result="BLOQUEIO_DUPLICIDADE"
            else:
                reserved.add(src_id)
                result="RESERVA_TECNICA_CONDICIONAL"
    outcomes[row["claim_id"]]=result
    assert result==row["resultado_esperado"], (row["claim_id"],result,row["resultado_esperado"])
assert len(reserved)==5, reserved
assert outcomes["C01"]=="RESERVA_TECNICA_CONDICIONAL"
assert outcomes["C02"]=="BLOQUEIO_DUPLICIDADE"
assert outcomes["C12"]=="NAO_SUBMETER_TITULARIDADE_A_VOTO"
assert outcomes["C19"]=="PENDENTE_DISPONIBILIDADE"
known=set(outcomes)
for row in tests:
    assert all(item in known for item in row["rastro_de_casos"].split(";")), row["id"]
print("M03.02.11 QA PASS: 11 fontes H, 20 pedidos H, 12 ataques e 10 portas F6 abertas.")
print("Reservas técnicas condicionais:", sorted(reserved))
print("Aviso: um slot é token lógico, NÃO reais, dotação, saldo, dinheiro ou direito.")
