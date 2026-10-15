// M03.03.05: simulador DIDATICO S1; zero dados TSE, nenhum numero ratificado.
// Uma cédula fictícia = uma cadeira em Câmara fictícia de 100 assentos.
// NÃO implementa conversão proporcional em distritos reais, nem resolve empates.
// Rodar: node M03-03_05_SIMULADOR_DIDATICO_S1.js
"use strict";
function makeBallots(which) {
 if(which==="small")return [{n:35,r:["A","B"]},{n:15,r:["B","A"]},{n:29,r:["C","B","A"]},{n:13,r:["D","B","A"]},{n:8,r:["E","B","A"]}];
 if(!["base","invert","exhaust"].includes(which))throw Error("Cenario desconhecido");
 const isInv=which==="invert",isEx=which==="exhaust";
 return [{n:34,r:["A","B"]},{n:29,r:["B","A"]},{n:10,r:["D","B","A"]},{n:2,r:["D","A","B"]},{n:isInv?5:14,r:["C","B","A"]},{n:isInv?12:3,r:["C","A","B"]},...(!isEx?[{n:5,r:["E","B","A"]}]:[]),{n:3,r:["E","A","B"]},...(isEx?[{n:5,r:["E"]}]:[])];
}

function countVotes(ballots,live){
 const counts=Object.fromEntries(live.map(p=>[p,0]));let exhausted=0;
 for(const b of ballots){const choice=b.r.find(x=>live.includes(x));if(choice)counts[choice]+=b.n;else exhausted+=b.n;}
 return {counts,active:Object.values(counts).reduce((a,b)=>a+b,0),exhausted};
}

function runIRV(ballots){
 if(ballots.some(b=>!Number.isInteger(b.n)||b.n<=0||!Array.isArray(b.r)||new Set(b.r).size!==b.r.length))throw Error("Cedula invalida");
 let live=[...new Set(ballots.flatMap(b=>b.r))].sort(),history=[];
 if(live.length<2)throw Error("Numero insuficiente de siglas");
 while(live.length>2){
  const t=countVotes(ballots,live);const min=Math.min(...Object.values(t.counts));
  const lowest=live.filter(x=>t.counts[x]===min);
  if(lowest.length!==1)throw Error("Empate de eliminacao sem regra constitucional:"+lowest.join(","));
  history.push({remaining:live.join("/"),...t,eliminated:lowest[0]});
  live=live.filter(x=>x!==lowest[0]);
 }
 const final=countVotes(ballots,live),[a,b]=live;
 if(final.counts[a]===final.counts[b])throw Error("Empate final sem desempate institucional");
 return {history,final,winner:final.counts[a]>final.counts[b]?a:b,finalists:live};
}

function assignConfidence(firstSeats,irv){
 const total=Object.values(firstSeats).reduce((a,b)=>a+b,0),[a,b]=irv.finalists,t=irv.final.counts;
 if(t[a]===0||t[b]===0)throw Error("Finalista sem voto ativo");
 const rA=firstSeats[a]/t[a],rB=firstSeats[b]/t[b];
 if(rA===rB)throw Error("Empate de ancoragem");
 const anchor=rA<rB?a:b,other=anchor===a?b:a;
 if(firstSeats[anchor]<=0)throw Error("Colegio vazio");
 const otherCount=Math.floor(firstSeats[anchor]*t[other]/t[anchor]);
 const conf={[anchor]:firstSeats[anchor],[other]:otherCount};
 if(conf[other]>firstSeats[other])throw Error("Confianca excede assentos eleitos");
 const seats=Object.fromEntries(Object.keys(firstSeats).map(p=>[p,conf[p]||0]));
 const chamber=Object.values(seats).reduce((x,y)=>x+y,0);
 const winners=Object.entries(seats).filter(([,v])=>v>chamber/2).map(x=>x[0]);
 if(winners.length!==1)throw Error("Sem maioria inequívoca");
 return {chamber,anchor,seats,leader:winners[0],outside:total-chamber};
}

function scenario(which){
 const ballots=makeBallots(which),seats={};
 for(const b of ballots){let p=b.r[0];seats[p]=(seats[p]||0)+b.n;}
 const irv=runIRV(ballots);
 return {name:which,seats,irv,confidence:assignConfidence(seats,irv),total:Object.values(seats).reduce((a,b)=>a+b,0)};
}

function verify(){
 const expected={base:["B",58,42,50,29,21,0],invert:["A",49,51,59,29,30,0],exhaust:["B",53,42,51,29,22,5],small:["B",65,35,23,15,8,0]}, rows=[];
 for(const [name,[winner,bVote,aVote,n,bConf,aConf,ex]] of Object.entries(expected)){
  const s=scenario(name),f=s.irv.final,c=s.confidence;
  if(s.total!==100||s.irv.winner!==winner||f.counts.B!==bVote||f.counts.A!==aVote||c.chamber!==n||c.seats.B!==bConf||c.seats.A!==aConf||f.exhausted!==ex||c.leader!==winner)throw Error("Divergencia "+name+":"+JSON.stringify(s));
  rows.push({case:name,firstA:s.seats.A,firstB:s.seats.B,firstC:s.seats.C,firstD:s.seats.D,firstE:s.seats.E,finalA:aVote,finalB:bVote,active:f.active,exhausted:ex,irvWinner:winner,confidenceA:aConf,confidenceB:bConf,totalConfidence:n,nonConfidence:100-n,confidenceLeader:c.leader,elimination:s.irv.history.map(x=>x.eliminated).join("/")});
 }
 return rows;
}
console.log(JSON.stringify(verify(),null,2));
