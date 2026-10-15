# M03.02.03 — Três legislaturas hipotéticas e contraensaio presidencialista
**ID:** CF-M03.02-EST-003 | **Data:** 14/10/2026 | **Issue:** #84 | **PR:** #85 (draft) | **main de referência no início:** 2a770a8136f8ca4877e865be3e3b7745a6d4b168 | **Status:** F0–F5/F8 de investigação, F6 não deliberado, F7 não iniciado. **Nenhum texto CF-NOR criado ou alterado.**
**Interfaces:** M02, M03.01, M04, M05, M06, M07, M12, M14; CLF T01 quando e se houver novos veículos legislativos.

## Objetivo e resultado principal
Testar **a compatibilidade entre investidura positiva escalonada (B2), censura construtiva por maioria dos MEMBROS, voto de confiança eventualmente solicitado pelo primeiro-ministro e continuidade fiscal sem orçamento aprovado**. Utilizar três legislaturas imaginárias de exatamente 100 cadeiras, sem adotar tamanho de Câmara, sistema eleitoral ou partidos do Brasil real ou de outro projeto. Confrontar com presidencialismo reformado em mesmas distribuições legislativas, mas **sem inventar resultados de eleição presidencial**.

**Achado lógico, não causal:** permite-se a nomeação de um gabinete com 45 votos favoráveis, 37 contrários, 18 abstenções (sim>não no segundo escrutínio), mas censura apoiada por 47 membros não o substitui (exige 51). Se governo decide não submeter confiança, e orçamento não é aprovado, o modelo proposto **não contém, até aqui, saída automática**. Esta é uma lacuna de desenho real, não prova de que tal situação ocorreria com frequência. Não encobrir com formulação de "estabilidade": estabilidade do titular e capacidade governativa são variáveis diferentes.

## 1. Regras computacionais e escopo da simulação
- **Universo:** 100 cadeiras; cada partido fictício vota em bloco, sem ausências e sem dissidência interna; todos os votos são classificados SIM/NÃO/ABSTENÇÃO; soma 100 em cada votação. **Não há dados sociais, distribuição real de cadeiras ou comportamento modelado estatisticamente.**
- **B1 investidura:** sim >= 51 em todo escrutínio. **B2:** no primeiro escrutínio sim >= 51; se não, em segundo escrutínio (após intervalo **não definido**) sim > não. **B3:** candidato não rejeitado se votos NÃO <= 50, independentemente dos votos favoráveis. Não converter B3 em B2.
- **Censura construtiva:** somente substitui se há candidato alternativo e sim >= 51, votação própria; NÃO se equipara à aprovação de nova investidura B2.
- **Voto de confiança:** para o exercício, usa-se regra experimental sim > não, com derrota caso sim <= não; a Constituição futura ainda NÃO decidiu quórum, titulares, timing ou efeito. **A Alemanha art. 68 usa maioria dos membros, logo não autoriza equiparar este teste à sua disciplina jurídica.** A derrota, na hipótese, abre processo de investidura B2 após renúncia; não convoca automaticamente eleição.
- **Orçamento:** apenas para demonstrar formação de maioria na câmara popular, aplica-se sim > não; sem modelar emendas, iniciativa reservada, segunda câmara, piso constitucional, limites tributários, veto, execução, LDO, arrecadação, juros, dívida e quórum legislativo específico. A rejeição **não equivale** a voto de confiança nem obriga renúncia ou dissolução.
- **Dissolução:** não está simulada como automática por fracasso orçamentário; D1/D2 exigiriam gatilhos e prazos expressamente escolhidos, ausentes em F6.
- **Cronologia:** t=1,2,... significa apenas ordem de eventos, **não dias nem meses**. Trajetórias P1/P2/P3 são RAMOS ALTERNATIVOS e não história única; não combinar votos de ramos diferentes.
- **Contrafactual A presidencial:** presidente hipotético eleito por eleição executiva independente mantém mandato após derrota programática; não presumir que seu partido venceu presidência porque controla bancada; inicial apoio parlamentar é assunção de cenário, não resultado eleitoral. Não supor impeachment por simples desacordo.

Os dados completos, os nomes e a conferência aritmética estão em:
1. \`M03-02_03_COMPOSICAO_LEGISLATURAS.csv\`: 13 partidos-situação, somatório 100 por legislatura.
2. \`M03-02_03_EVENTOS_SIMULADOS_AUDITAVEIS.csv\`: 29 votações nos seis ramos, com soma SIM+NÃO+ABST=100, resultados condicionados e IDs.
3. \`M03-02_03_CONTRAFACTUAL_PRESIDENCIALISMO.csv\`: seis votações fiscal-programáticas de teste no modelo presidencial.
São **cenários de stress test**, não amostra da história parlamentar do Brasil ou previsão de probabilidade.

## 2. Legislatura L1 — coalizão ampla que se desfaz
**Composição:** A44, B26, C18, D12.

**P1, sequência:** (1) candidato A investido por A+B=70 contra C+D=30: satisfaz B1, B2 desde primeiro escrutínio e B3; (2) orçamento A+B=70 aprovado; (3) B rompe — A44 SIM versus B+C+D56 NÃO, orçamento rejeitado, sem queda implícita do gabinete; (4) B+C+D56 elegem B por censura construtiva (A44 opõe), nomeação vinculada do sucessor; (5) orçamento do novo gabinete por 56 x 44.

**Resultado mecânico:** censura construtiva resolve a perda de maioria quando oposição consegue **também formar maioria sucessora**, sem dissolver Parlamento. Não demonstra se C/D aceitariam realmente programa de B ou se custos de coalizão seriam altos.

**Presidencialismo A, igual composição legislativa:** eventual presidente apoiado inicialmente por A+B consegue orçamento 70 x30; após ruptura B, perde votação por 44 x56, mas não cai por censura parlamentar. Pode negociar recomposição de ministros, propor novo orçamento ou construir maioria legislativa alternativa; se nenhuma maioria surgir, enfrenta bloqueio programático até solução política ou eleição constitucional regular. **Vantagem presidencial própria:** mandato executivo não depende de alianças legislativas oportunistas. **Custo:** bloqueio sem substituição política ordinária. Não presumir que toda legislatura adversa gera crise democrática.

## 3. Legislatura L2 — dois blocos quase empatados e partido pivô
**Composição:** X46, Y44, Z10.

**P1, trajetória de realinhamento:** investidura de X recebe 46 SIM, 44 NÃO, 10 abst.: falha B1, passa B2 no segundo escrutínio e B3. Primeiro orçamento: 46 SIM, 44 NÃO e Z abstém → aprovado na regra simplificada. Se Z formaliza alternativa Y+Z=54, moção construtiva aprova e governo Y passa a deter 54 votos; seu orçamento passa contra X46.

**P2, trajetória de bloqueio:** mesmo governo X é investido; primeiro orçamento passa com abstenção Z; Z rejeita segundo orçamento com Y (X46 SIM/Y+Z54 NÃO); Y tenta censura mas Z se abstém na eleição de sucessor (44 favor, 46 contra, 10 abst.), censura falha; X solicita **hipoteticamente** confiança, perde por 46 x54; tenta-se candidato Y, mas Z não o apoia, e B2 também falha (44 x46, 10 abst.). Sem maioria alternativa, eventual eleição antecipada não decorre da votação fiscal: depende de **gatilho e janela constitucionalmente definidos**, sujeitos a exame M02/M14. A confiança governamental ser voluntariamente solicitada é condição crítica, nunca presumir que X optará por perder.

**Lição:** partido pivô pode votar contra orçamento sem aceitar o programa do sucessor. Se a Constituição só contempla censura construtiva, a decisão de produzir uma crise formal fica assimetricamente dependente da iniciativa do próprio governo. Ao mesmo tempo, parlamentarismo não obriga Z a aderir a um de dois blocos: pode cooperar caso a caso.

**Presidencialismo reformado:** presidente com bancada X46 obtém orçamento quando Z abstém (46>44) e não o obtém quando Z se soma a Y (46<54); mandato do chefe de Governo permanece. A separação entre poderes produz incentivo para compromisso legislativo e dificulta substituição oportunista, mas não garante orçamento aprovado ou transparência de barganhas.

## 4. Legislatura L3 — multipartidarismo fragmentado
**Composição:** A27, B23, C18, D14, E10, F8.

**P1 — iniciativa do próprio gabinete:** candidato A apoiado por A+C=45, oposição B+D=37, E+F=18 abstém. Falha B1, passa B2 (45>37 em segundo escrutínio) e B3. Orçamento recebe A+C45 SIM versus B+D+E47 NÃO, F8 abstém → rejeitado. Censura proposta com candidato B obtém B+D+E47 SIM, A+C45 NÃO e F8 abstém → **não alcança 51**. Primeiro-ministro A solicita confiança (hipótese voluntária) e perde por 45 x47 com 8 abst.; abre-se novo processo de investidura. Candidato B com B+D+E47 favoráveis, A+C45 contra, F8 abstém é eleito na **segunda fase de B2** porque 47>45; então seu orçamento também passa por 47>45. Isso exige decisão do chefe do governo de provocar a própria derrota na confiança; **não corrige sozinho a paralisia quando ele se recusa a fazê-lo**.

**P2 — gabinete não requisita confiança:** mesma investidura, duas derrotas orçamentárias consecutivas com A+C45 contra B+D+E47 (F8 abst.). Censura 47 não passa. Sem disposição adicional, o modelo **mantém o gabinete e a Câmara, sem orçamento aprovado**, autorizando apenas as funções fiscais que uma regra de continuidade M05 venha a permitir. Não presumir que governo se dissolve por insucesso de políticas, nem que repetição da derrota faz surgir magicamente maioria absoluta. É a principal contraprova de nosso protótipo.

**P3 — coalizão sucessora finalmente alcança maioria absoluta:** após a derrota orçamentária, F8 passa ao candidato B: B+D+E+F=55 contra A+C45; censura construtiva passa, e orçamento do gabinete B recebe 55 votos. Demonstra que **mudanças nas preferências dos partidos, não fórmulas de quórum isoladamente**, determinam possibilidade de solução.

**Presidencialismo reformado:** presidente eleito à parte e apoiado por A+C45 pode perder orçamento 45 x47; mandato fixo mantém titularidade executiva, mas pode formar maioria pontual com F (A+C+F=53 > B+D+E47) para aprovar uma medida sem trocar o chefe de governo. Em presidencialismo, não se exige investidura parlamentar do presidente, mas permanência independente não torna Congresso irrelevante. **Não há prova de que a possibilidade de troca de gabinete seja superior à barganha presidencial em resultado econômico/social.**

## 5. Resultado da comparação em cinco critérios funcionais
| Critério | B2 + censura construtiva | A — presidencialismo reformado |
|---|---|---|
| Formação de executivo minoritário | Permite com maioria relativa favorável na segunda fase; proteção apenas política para base baixa | Presidente não precisa investidura parlamentar, eleito por sufrágio executivo próprio |
| Troca por nova maioria parlamentar | Possível no curso da legislatura sem novas eleições, se 51 membros elegem sucessor | Não há troca por simples divergência; mandato fixo e hipóteses próprias de impedimento |
| Parlamento sem maioria sucessora e orçamento rejeitado | Impasse persiste, a menos que Governo requeira confiança ou ocorra gatilho constitucional adicional | Impasse legislativo persiste; Executivo também precisa de autorização fiscal ou mecanismo de transição |
| Risco de oportunismo | Censura estratégica mitigada; confiança/dissolução podem ser manipuladas pelo incumbente | Impeachment instrumentalizado e barganhas legislativas pouco transparentes são riscos; não consequências automáticas |
| Controle do chefe de Estado | Investidura e nomeação devem ser vinculadas; poder de dissolver delimitado | Presidente executivo tem legitimidade eleitoral própria e poderes definidos, fiscalizados por parlamento/justiça |

**Não atribuir notas nem inferir "vencedor":** teste revela propriedades normativas lógicas com um conjunto construído de votações, mas não modela negociação, coesão partidária, voto secreto, Executivo com agenda exclusiva, controle da mídia, limitação orçamentária real, tribunais, sistema de partidos, segundos turnos eleitorais ou segunda câmara territorial.

## 6. Que mecanismos adicionais testar antes de ratificar B?
### Mecanismo R1 — cláusula de arbitragem por impasse fiscal objetivo, sem renúncia automática
Diante de reapresentações motivadas e rejeições reiteradas de orçamento, exigir publicação de alternativas, comissão de conciliação, relatório independente de execução e debate parlamentar específico. **Mérito:** publicidade e pressão política sem forçar queda. **Limite:** nenhum ator obrigado a produzir maioria; não resolve impasse persistente por si só. **Risco:** burocratizar sem custo político efetivo.

### Mecanismo R2 — confiança solicitada pelo Parlamento em casos estritamente taxativos
Parcela dos deputados poderia exigir que Governo submetesse formalmente sua confiança; efeito da derrota precisaria de desenho cuidadoso. **Mérito:** evita monopólio do Primeiro-ministro na decisão de suscitar confiança; pode abrir janela de sucessão pelo B2. **Objeção decisiva:** se basta maioria simples negativa, converte-se em censura não construtiva disfarçada; se exige maioria absoluta para instaurar/derrubar, reproduz o bloqueio observado na L3. Não aprovar sem M02/M06 e simulações de abuso.

### Mecanismo R3 — dissolução extraordinária após impasse legislativo comprovado
Somente se fracassarem tentativas reais de formação alternativa, conciliação fiscal e critérios objetivos de incapacidade de aprovação de orçamento, admitir pedido/decisão institucional de dissolução. **Mérito:** saída democrática quando votos parlamentares não geram governo funcional. **Objeção decisiva:** oposição pode bloquear orçamento propositalmente para obter eleição antecipada; chefe de Governo pode apresentar orçamento inaceitável para criar gatilho. Necessária barreira de boa-fé difícil de judicializar sem transformar tribunal em árbitro de mérito político.

### Mecanismo R4 — preservar o impasse como custo democrático legítimo
Aceitar que às vezes Parlamento rejeitará opções relevantes e que eleição ordinária deve resolver, usando continuidade fiscal estrita e incentivos políticos, sem mecanismo de destituição/eleição extraordinário. **Mérito:** evita dissolução oportunista e instrumentalização judicial; reconhece que nem todo conflito necessita solução institucional forçada. **Objeção:** pode tornar perdurável um Executivo legislativamente ineficaz e deixar direitos sociais dependentes de orçamento pretérito. Exige deveres objetivos de prestação de contas e impossibilidade de governar indefinidamente por regime excepcional.

**Juízo provisório:** R1 + proteção fiscal necessária parecem opção menos intrusiva, mas são insuficientes como saída de impasse extremo. Comparar R2/R3 com a alternativa presidencial, em que o problema também existe e o mandato fixo é deliberado como custo legítimo. Não constitucionalizar uma "moção de desconfiança orçamentária" sem prova de compatibilidade com censura construtiva e risco de chantagem eleitoral.

## 7. Federalismo e orçamento — limites materiais ignorados pelos números de plenário
Todas as decisões simplificadas ocorreram na **Câmara popular**, sem Senado/Conselho e sem distribuição territorial. Isso impede concluir aprovação de uma lei federal real: a proposta pode exigir participação do órgão territorial, consentimento qualificado, controle sobre encargos ou procedimentos distintos. O teste de orçamento **não incorpora nem altera** CF-NOR-0001/0002 H de custeio federativo. Uma fórmula de destituição não determina, por si, competência para impor despesa a Estado/Município. M04/M05 devem examinar o procedimento completo e a situação de entes com capacidade fiscal desigual.

## 8. Evidência jurídica e empírica verificadas e limites de causalidade
1. [Lei Fundamental alemã, arts. 63/67–68](https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html): investidura, censura construtiva e derrota de confiança com condições próprias; não é direito vigente no Brasil.
2. [Lei Fundamental alemã, art. 111](https://www.gesetze-im-internet.de/gg/art_111.html): execução provisória de despesas estritamente necessárias na ausência de lei orçamentária; não é orçamento ilimitado.
3. [Constituição espanhola, arts. 99/113–115/134(4)](https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229&p=20260520): investidura escalonada, censura construtiva, dissolução com limites, prorrogação de orçamento.
4. Cheibub, Przeworski e Saiegh (2004), [Government Coalitions and Legislative Success Under Presidentialism and Parliamentarism](https://doi.org/10.1017/S0007123404000195): democracias 1946–1999; coalizões presidenciais frequentes e governos minoritários não necessariamente menos exitosos legislativamente, em nenhum dos dois sistemas. **Associação observacional histórica não explica nem prediz os seis ramos artificiais.**
5. Cheibub (2002), [Minority Governments, Deadlock Situations, and the Survival of Presidential Democracies](https://doi.org/10.1177/0010414002035003002): estudo observacional do presidencialismo e bloqueio até 1996, com limites de desenho e seleção de casos.
**Pendências empíricas:** história pós-1999, governos minoritários latino-americanos/europeus, dados de budget failure x duração de gabinete e reformas brasileiras pós-2015, financiamento, segunda câmara e custo constitucional de eleições antecipadas.

## 9. Síntese decisória de rodada (sem F6)
- **Rejeitar como conclusão apressada** que censura construtiva **resolve sempre** impasse: L3/P2 demonstra contraprova mecânica.
- **Rejeitar como conclusão apressada** que parlamentarismo exige governo majoritário: B2 e B3 admitem minoria, com diferentes graus de apoio e abstenção.
- **Rejeitar como conclusão apressada** que presidencialismo minoritário é necessariamente ingovernável: acordos por matéria e veto parlamentar variam.
- **Não equiparar derrota orçamentária a censura ou confiança por ficção constitucional.**
- **Manter B2 como hipótese P de engenharia** apenas se integrada a deveres verificáveis de transparência fiscal, oportunidade de oposição, gabinete interino limitado, prazos de consulta e exame da possível saída R2/R3. R1 não é antídoto suficiente em toda configuração.
- **Não deliberar** sistema de governo, tamanho da Câmara, chefia de Estado, composição federativa, quóruns finais, prazo de dissolução nem redação CF-NOR antes de F6 expresso.

**Próximo trabalho M03.02.04:** parecer crítico integrado de M02/M05/M06/M14 sobre opções R1–R4 e presidencialismo reformado, três testes de agentes oportunistas com incentivos conflitantes (governo provoca bloqueio, oposição provoca bloqueio, chefe de Estado não coopera), proposta de porta deliberativa com alternativas e objeção máxima; eventualmente agendar F6 para opção de arquitetura, ainda sem promulgação.