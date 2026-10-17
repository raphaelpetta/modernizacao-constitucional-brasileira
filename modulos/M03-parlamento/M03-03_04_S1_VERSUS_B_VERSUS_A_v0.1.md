# M03.03 — R04-S: semiparlamentarismo S1 versus parlamentarismo B e presidencialismo A
**Data/corte:** 15/10/2026. **Estado:** pesquisa H/A/V; F6/D/F7 não realizados; CF-DEC-006 inalterado; não é minuta normativa homologada. **Base:** M03.02 PR #85; M03.03 PR #100 R01-R03; pauta PR #99. **Eixo novo:** regra eleitoral REAL do artigo Ganghof 2016, sensibilidade, orçamento e igualdade entre parlamentares.

## 1. Referência acadêmica precisa
Steffen Ganghof, *Combining proportional and majoritarian democracy: An institutional design proposal*, Research & Politics (2016), https://doi.org/10.1177/2053168016665640 : única cédula com ranking de listas partidárias. Primeiras preferências definem, de maneira proporcional, o total de cadeiras da Assembleia. Transferências preferenciais por eliminação sucessiva até restarem DOIS partidos determinam o placar majoritário que definirá a instância de confiança. As cadeiras de confiança pertencem apenas aos dois finalistas, são SUBCONJUNTO das cadeiras proporcionais desses partidos; seus outros membros, assim como parlamentares das demais siglas, ficam em assentos legislativos sem direito de votar censura. O autor cria fórmula para não atribuir a um partido mais cadeiras de confiança que seu número total. Artigo tipológico Ganghof (2018), https://doi.org/10.1111/1475-6765.12224 : tipo mínimo sem eleição popular do Executivo, duas partes legislativas diretamente legitimadas, responsabilidade governamental apenas perante uma parte. Ideal de duas partes com legitimidade eleitoral equivalente e, em geral, veto legislativo significativo da parte não investidora; o autor admite variações de veto orçamentário e resolução de impasses. A versão S1 de 2016 não é reprodução de uma Constituição em vigor. Livro (2021), https://doi.org/10.1093/oso/9780192897145.003.0008 .

**Correção ao R03:** dizer somente “colégio que escolhe o gabinete” é insuficiente; não há simplesmente seleção de uma facção parlamentar por acordo partidário. É preciso verificar regra de votos transferidos, proporcionalidade da Assembleia, limite físico de representantes finalistas e legitimidade de excluir deputados da competência de censura. Uma maioria no colégio de confiança não implica maioria na Assembleia.

## 2. Mecanismo lógico mínimo e caso reprodutível de 100 assentos
Para fins de TÉCNICA, não como previsão do Brasil: total de 100 cadeiras distribuídas em exata proporção a votos de primeira preferência: A36, B29, C16, D11, E8. Todas as cadeiras são de pessoas eleitas; o subconjunto que votará censura deve caber no total partidário. Transferências finais são premissas de dois exercícios de ranking; NÃO foram inferidas de cédulas brasileiras nem executadas por programa de IRV completo.

| Cenário | C (A/B) | D (A/B) | E (A/B) | Dois finalistas A/B | Âncora pelo menor quociente cadeiras/votos finais | Confiança A | Confiança B | Governo identificado |
|---|---|---|---|---|---|---|---|---|
| P0 | 4/12 | 3/8 | 2/6 | 45/55 | B, 29/55 menor que 36/45 | piso(29×45/55)=23 | 29 | B (29 a 23) |
| P1 | 7/9 | 5/6 | 3/5 | 51/49 | B, 29/49 menor que 36/51 | piso(29×51/49)=30 | 29 | A (30 a 29) |

As duas linhas respeitam C16, D11, E8 e distribuem precisamente seus 35 votos finais entre A/B; alocações de confiança satisfazem confiança_A <=36 e confiança_B <=29. Nenhuma cadeira adicional é criada. **Apenas seis votos finais transferidos de B para A**, mantendo EXATAMENTE as primeiras preferências e a composição legislativa 36/29/16/11/8, trocam o partido governante. É sensibilidade eleitoral, NÃO fraude nem fragilidade matemática provada. A fórmula de ancoragem acima reproduz a lógica e as notas do artigo de 2016 (o autor usa partido com menor razão assentos/votos finais); para implementar eleição real ainda são indispensáveis regras de arredondamento, candidaturas, empates, ranking parcial, federações, vacância, distrito, piso eleitoral e consistência em múltiplas circunscrições.

~~~text
para cada partido p: seats[p] = alocação proporcional das primeiras preferências
AV modificado elimina listas até restarem duas, retornando sharesFinal[p]
anchor = argmin(seats[p] / sharesFinal[p])
confidence[anchor] = seats[anchor]
confidence[other] = floor(seats[anchor] * sharesFinal[other] / sharesFinal[anchor])
assert confidence[p] <= seats[p] para ambos
~~~
**Não é algoritmo legal pronto:** a apuração real necessita especificação integral de fórmula de proporcionalidade, transferências, distritos, votos inválidos, quocientes e garantia de pluralidade de candidatos individuais. A afirmação “quase garante governos de partido único” é tese formal do autor sob premissas específicas, não previsão para dados brasileiros.

## 3. Confronto SIMÉTRICO diante dos mesmos votos parlamentares
Tomar **B como partido governista em P0**, sem confundir isso com vitória presidencial: na alternativa A, a eleição popular presidencial é uma variável separada; pressupor presidente associado a B serve apenas para isolar a dificuldade legislativa, NÃO simula eleição presidencial real.

**Cenário Q1, aprovação por matéria:** coalizão B+C+D = 29+16+11 = 56 permite aprovar projeto e LOA, se houver disciplina, quórum e tramitação adequados.
- S1: gabinete B mantém confiança 29/52; maioria legislativa para projeto é 56/100. Há convergência CONDICIONAL e o modelo não impede governo eficaz.
- B: gabinete sustentado por B+C+D=56 poderia ser investido por maioria absoluta e aprovar o projeto; coalizão tem custo de negociação e repartição de cargos potencialmente diferentes.
- A: presidente do partido B precisa de B+C+D=56 para aprovar lei; no entanto, mandato presidencial não depende de voto de confiança. Limites de iniciativa e veto ainda abertos no A.
**Cenário Q2, oposição legislativa a LOA:** A+C+D+E = 36+16+11+8 = 71 votam contra LOA de gabinete B. Não supor que os 71 concordariam sobre QUEM substitui B ou qual orçamento aprovariam.
- S1: o colégio B29/A23 mantém a confiança em B por sua composição; LOA perde por 29×71. Governo permanece, orçamento sem autorização nova.
- B: gabinete minoritário B29 pode persistir sem sucessor para censura construtiva; se a coalizão B+C+D se mantém, este Q2 é por definição outro cenário de preferência, não votação da mesma matéria.
- A: presidente B permanece por mandato; mesma necessidade de negociar novas leis e limites de continuidade fiscal.
**Resultado:** nenhum produz aprovação orçamentária por fórmula de investidura. S1 pode facilitar governo identificável sem coalizão positiva de plenário, mas cria diferença constitucional entre o colégio que mantém o gabinete e os representantes que podem rejeitar sua política fiscal.

## 4. Três regimes de veto fiscal para estudar (NÃO escolher um sem M05)
**S-F1 — plenário controla LOA integral:** preserva autoridade fiscal de todos os deputados; governo B pode sobreviver a bloqueio de vários exercícios. Sem autonomia para nova despesa por decreto.
**S-F2 — reserva do orçamento à instância de confiança:** aproxima responsabilidade fiscal da maioria governista, mas retira do Legislativo proporcional plena autoridade sobre despesa e pode piorar separação de poderes. Que contenção externa e federativa restaria? Não adotar pelo simples ganho de capacidade.
**S-F3 — regra repartida e mecanismo público de negociação:** programação nova depende de plenário; continuidade estritamente legal e fiscalmente possível; negociação obrigatória por prazo, com eventual arbitragem popular excepcional DEFINIDA, nunca eleição/referendo automático a cada derrota. A exigência de negociação não cria receita, LOA ou crédito; risco de chantagem plebiscitária.
O artigo de 2016 admite, em nota, a necessidade de que algum órgão possua veto orçamentário; não descrevê-lo como licença constitucional brasileira para deslocar LOA a quem investe gabinete.

## 5. Quatro possíveis reprovações
- **V1 legitimidade:** se S1 diferencia representantes sem critério eleitoral inteligível, sufrágio equivalente, direitos de oposição e revisão jurisdicional de atos, rejeitar configuração.
- **V2 fiscal:** se S1 faz derrota de LOA gerar gasto programático, censura fictícia ou dissolução automática, rejeitar.
- **V3 federal:** se instância de confiança altera distribuição de receitas e competências federativas sem consentimento/controle definido, rejeitar.
- **V4 poderes:** se maioria de confiança passa a controlar tribunais, fiscalização, Legislativo e emergência sem freios, rejeitar.

## 6. A questão constitucional específica do Brasil
Igualdade de representação, voto direto (art. 60 §4º, II), antecedência de lei eleitoral (art. 16), mandatos e pacto federativo devem ser cotejados com regras CONCRETAS do S1, e não com mero nome. Senado federativo brasileiro NÃO é automaticamente a casa “proporcional” da teoria de Ganghof. Transplantar tipo puro pode exigir terceira arena, redefinir Senado ou combinar representação territorial com proporcionalidade mediante estudos M02/M04/M06. Art. 167 §7º atual protege entes contra encargos sem fonte; qualquer LOA e serviço essencial depende de norma financeira, não de nome da instância investidora.
Fontes oficiais Brasil: https://www.tse.jus.br/legislacao/codigo-eleitoral/constituicao-federal/constituicao-da-republica-federativa-do-brasil ; https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc128.htm .

## 7. Resultado e condição de avanço
**Achado novo:** S1 é electoralmente especificável em exemplo pequeno e sua maioria de confiança pode mudar com transferências preferenciais sem mudança na representação proporcional; isso exige ensaio real de incentivos partidários e inteligibilidade eleitoral. **Achado preservado:** não resolve T01 orçamento sem maioria e pode reforçar desconexão entre sobrevivência e lei. **Falsificador:** se o S1 requer esvaziar o Parlamento fiscal ou criar poder executivo de dissolução oportunista para ser governável, deixa de justificar seus custos; se alternativa B/A alcançar representação, continuidade e pluralidade semelhantes com menos assimetria parlamentar, S1 perde prioridade.

**FEITO:** duas apurações finais sintéticas por fórmula explícita, duas maiorias de política, três modelos fiscais e quatro reprovações. **PENDENTE:** execução de simulador com dados TSE e cédulas preferenciais efetivamente observadas (não existem no voto brasileiro atual), revisão M02/M04/M05/M06/M14. **PRÓXIMO:** testar distribuição 2022/2026 pelo TSE sem inventar preferências secundárias (usar distribuição de cenários transparente) e especificar S-F3 constitucionalmente. Nada aqui aprova CF-NOR, F6 ou alteração do CF-DEC-006.
