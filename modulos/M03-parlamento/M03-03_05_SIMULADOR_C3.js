#!/usr/bin/env node
/**
 * M03.03 R05 C3 — testes determinísticos de regras de seleção e decisão.
 * Fonte de pesos: TSE, cadeiras históricas de 2022 retotalizadas até 20/07/2024.
 * Eleição de um conselho de cinco NÃO aconteceu; alinhamentos e coalizões são H.
 * Execução: node modulos/M03-parlamento/M03-03_05_SIMULADOR_C3.js
 */
"use strict";
const fs=require("node:fs"),path=require("node:path"),assert=require("node:assert/strict");
const rows=fs.readFileSync(path.join(__dirname,"M03-03_05_DADOS_TSE_2022_BASE.csv"),"utf8").trim().split(/\r?\n/).slice(1);
const s=Object.fromEntries(rows.map(row=>{const [p,seats]=row.split(";");return [p,Number(seats)];}));
assert.equal(Object.values(s).reduce((a,b)=>a+b,0),513);
function dhondt(votes,m){
 const allocated=Object.fromEntries(Object.keys(votes).map(k=>[k,0]));
 const history=[];
 for(let i=0;i<m;i++){
   const ranks=Object.keys(votes).map(p=>({p,quotient:votes[p]/(allocated[p]+1)})).sort((a,b)=>b.quotient-a.quotient||a.p.localeCompare(b.p,"en"));
   const w=ranks[0];history.push(w.p);allocated[w.p]++;
 }
 return {allocated,history};
}
const partyVotes=Object.fromEntries(Object.entries(s).filter(([p,n])=>n>0));
const proportional=dhondt(partyVotes,5);
assert.equal(proportional.allocated.PL,2);
assert.equal(proportional.allocated.FE_BRASIL,1);
assert.equal(proportional.allocated.UNIAO,1);
assert.equal(proportional.allocated.PP,1);
const blocNames=["PL","UNIAO","PP","REPUBLICANOS","MDB"];
const governing=blocNames.reduce((n,p)=>n+s[p],0);
assert.equal(governing,287);
const rival=513-governing;
const blocSplit=dhondt({BLOCO_287:governing,RESTANTE_226:rival},5);
assert.equal(blocSplit.allocated.BLOCO_287,3);
function decision(yes,totalAbsent,yesAbsent,quorum=4,positive=3){
 const present=5-totalAbsent,affirm=yes-yesAbsent;
 return {present,affirm,approved:present>=quorum&&affirm>=positive,reason:present<quorum?"SEM_QUORUM":affirm<positive?"SEM_TRES_VOTOS":"APROVADO"};
}
const scenarios=[
 ["C01","todos_presentes_cartel_3",decision(3,0,0)],
 ["C02","um_opositor_ausente",decision(3,1,0)],
 ["C03","um_cartel_ausente",decision(3,1,1)],
 ["C04","dois_opositores_ausentes",decision(3,2,0)],
 ["C05","dois_cartel_ausentes",decision(3,2,2)],
 ["C06","nomeacao_sensivel_4_votos_sem_pacto",decision(3,0,0,4,4)],
 ["C07","nomeacao_sensivel_4_votos_com_um_opositor",decision(4,0,0,4,4)]
];
const fields=["id","situacao","presentes","sim","aprovacao","motivo"];
process.stdout.write(fields.join(";")+"\n"+scenarios.map(([id,label,o])=>[id,label,o.present,o.affirm,o.approved?"SIM":"NAO",o.reason].join(";")).join("\n")+"\n");
process.stderr.write(JSON.stringify({partidos_dhondt:proportional.allocated,ordem:proportional.history,coalizao_287:governing,oposicao: rival,lista_dois_blocos:blocSplit.allocated,suporte_PL_UNIAO:s.PL+s.UNIAO,fracao_PL_UNIAO:(s.PL+s.UNIAO)/513},null,2)+"\n");
