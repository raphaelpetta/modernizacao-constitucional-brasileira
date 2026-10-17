// M03.03.05 — Cenários DIDÁTICOS de eleição e quórum de conselho.
// 55%/45% são apoios HIPOTÉTICOS, não dados parlamentares brasileiros.
// Não estima probabilidade de cartel, captura ou consequências constitucionais.
// Representação 2G+2O+1I é cenário hipotético com I adicionado ao campo G
// somente para efeito do cálculo binário; não mede a liberdade de voto de I.
"use strict";
function dhondt(a,b,n){
 const opts=[];
 for(let i=1;i<=n;i++){opts.push({group:"G",score:a/i,divisor:i},{group:"O",score:b/i,divisor:i})}
 opts.sort((x,y)=>y.score-x.score||x.group.localeCompare(y.group));
 if(opts[n-1].score===opts[n]?.score)throw Error("Empate nao decidido");
 const winners=opts.slice(0,n),g=winners.filter(x=>x.group==="G").length;
 return {G:g,O:n-g,quotients:winners.map(x=>x.group+":"+x.divisor)};
}

function councilCase(name,composition,requiredPresent,requiredYes,yesG,yesO,absentG=0,absentO=0) {
 const [g,o]=composition;
 const presentG=g-absentG,presentO=o-absentO,present=presentG+presentO;
 if(presentG<0||presentO<0||yesG>presentG||yesO>presentO)throw Error("Cenario incoerente");
 const pass=present>=requiredPresent&&yesG+yesO>=requiredYes;
 return {case:name,G:g,O:o,absentG,absentO,present,quorum:requiredPresent,votesYesG:yesG,votesYesO:yesO,threshold:requiredYes,approved:pass?"SIM":"NAO",basis:"SIMULACAO_H"};
}

function check(){
 const dh=dhondt(55,45,5);
 if(dh.G!==3||dh.O!==2)throw Error("D'Hondt");
 const R=[
 councilCase("simultaneo_majoritario_cinco_cargos",[5,0],4,3,5,0),
 councilCase("dhondt_55_45_politica_ordinaria",[3,2],4,3,3,0),
 councilCase("dhondt_55_45_boycott_oposicao",[3,2],4,3,3,0,0,2),
 councilCase("dhondt_55_45_quorum_tres",[3,2],3,3,3,0,0,2),
 councilCase("dhondt_55_45_nomeacao_4",[3,2],4,4,3,0),
 councilCase("dhondt_55_45_nomeacao_4_apoio",[3,2],4,4,3,1),
 councilCase("pivotal_2_2_1_com_independente_agregado_G",[3,2],4,3,3,0),
 councilCase("pivotal_2_2_1_ausencia_agregado_G",[3,2],4,3,2,0,1,0),
 councilCase("ausencia_dois_conselheiros",[3,2],4,3,2,1,1,1),
 councilCase("escalonamento_maioria_55_45_constante",[5,0],4,3,5,0)
 ];
 const expect={simultaneo_majoritario_cinco_cargos:"SIM",dhondt_55_45_politica_ordinaria:"SIM",dhondt_55_45_boycott_oposicao:"NAO",dhondt_55_45_quorum_tres:"SIM",dhondt_55_45_nomeacao_4:"NAO",dhondt_55_45_nomeacao_4_apoio:"SIM",pivotal_2_2_1_com_independente_agregado_G:"SIM",pivotal_2_2_1_ausencia_agregado_G:"NAO",ausencia_dois_conselheiros:"NAO",escalonamento_maioria_55_45_constante:"SIM"};
 for(const x of R)if(x.approved!==expect[x.case])throw Error("Cenario "+x.case);
 return {dh,rows:R};
}
console.log(JSON.stringify(check(),null,2));
