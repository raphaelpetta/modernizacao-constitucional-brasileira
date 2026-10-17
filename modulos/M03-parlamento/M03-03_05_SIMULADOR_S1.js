#!/usr/bin/env node
/**
 * M03.03 R05 — teste CONDICIONAL, jamais reconstituição eleitoral histórica.
 * Node.js puro. Execução: node modulos/M03-parlamento/M03-03_05_SIMULADOR_S1.js
 * Fonte cadeiras: TSE, representatividade 2022 com retotalizações até 20/07/2024.
 * Fonte votos: TSE Portaria 10/2023 anexos com atualização de 2023.
 * TOTAL de votos candidato+legenda por agrupamento NÃO representa ranking partidário
 * de um eleitor e cadeiras reais estaduais NÃO reproduzem proporcionalidade nacional.
 * Preferências posteriores são artificiais e uniformes em cada cenário.
 */
"use strict";
const fs=require("node:fs");
const path=require("node:path");
const assert=require("node:assert/strict");
const source=fs.readFileSync(path.join(__dirname,"M03-03_05_DADOS_TSE_2022_BASE.csv"),"utf8").trim().split(/\r?\n/);
const hdr=source.shift().split(";");
assert.equal(hdr.length,4);
const base=source.map(l=>{const [p,s,v,desc]=l.split(";");return {p,seats:Number(s),votes:Number(v),desc};});
assert.equal(new Set(base.map(x=>x.p)).size,base.length);
assert.equal(base.reduce((s,x)=>s+x.seats,0),513);
assert.equal(base.reduce((s,x)=>s+x.votes,0),109491000);
const smap=Object.fromEntries(base.map(x=>[x.p,x.seats]));
const mainA="PL",mainB="FE_BRASIL";
function runoff(q){
  assert(Number.isInteger(q)&&q>=0&&q<=1000);
  let ballots=[];
  for(const d of base){
    if(d.p===mainA||d.p===mainB){
      ballots.push({rank:[d.p,d.p===mainA?mainB:mainA],votes:d.votes});
    } else {
      const towardA=Math.floor(d.votes*q/1000);
      ballots.push({rank:[d.p,mainA,mainB],votes:towardA});
      ballots.push({rank:[d.p,mainB,mainA],votes:d.votes-towardA});
    }
  }
  const active=new Set(base.map(x=>x.p));
  const trace=[];
  function tally(){
    const t=Object.fromEntries([...active].map(x=>[x,0]));
    for(const b of ballots){
      const p=b.rank.find(x=>active.has(x));
      if(p)t[p]+=b.votes;
    }
    return t;
  }
  while(active.size>2){
    const t=tally();
    const last=Object.entries(t).sort((a,b)=>a[1]-b[1]||a[0].localeCompare(b[0],"en"))[0][0];
    trace.push(last);
    active.delete(last);
  }
  const votes=tally(),total=Object.values(votes).reduce((a,b)=>a+b,0);
  assert.equal(total,109491000);
  assert.deepEqual([...active].sort(),[mainA,mainB].sort(),"Cenário não preservou dois finalistas assumidos");
  const anchor=[mainA,mainB].sort((a,b)=>smap[a]/votes[a]-smap[b]/votes[b])[0];
  const other=anchor===mainA?mainB:mainA;
  const conf={[anchor]:smap[anchor],[other]:Math.floor(smap[anchor]*votes[other]/votes[anchor])};
  assert(conf[mainA]<=smap[mainA]&&conf[mainB]<=smap[mainB]);
  const winner=conf[mainA]===conf[mainB]?"EMPATE":conf[mainA]>conf[mainB]?mainA:mainB;
  return {q,PL_final:votes[mainA]/total*100,FE_final:votes[mainB]/total*100,anchor,PL_c:conf[mainA],FE_c:conf[mainB],winner,collegium:conf[mainA]+conf[mainB],eliminations:trace};
}
const qvals=[400,450,475,480,485,500,550,600];
const results=qvals.map(runoff);
assert(results.some(x=>x.winner==="EMPATE"),"Não foi encontrado caso de empate sob arredondamento");
const header="q_permille;PL_pct_final;FE_BRASIL_pct_final;ancora;PL_cadeiras_confianca;FE_BRASIL_cadeiras_confianca;vencedor;total_confianca";
const lines=[header,...results.map(x=>[x.q,x.PL_final.toFixed(3),x.FE_final.toFixed(3),x.anchor,x.PL_c,x.FE_c,x.winner,x.collegium].join(";"))];
process.stdout.write(lines.join("\n")+"\n");
