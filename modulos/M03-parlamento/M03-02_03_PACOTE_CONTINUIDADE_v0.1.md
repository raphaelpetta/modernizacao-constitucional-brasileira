# M03.02.03 — FEITO / PENDENTE / PRÓXIMO
**Data:** 14/10/2026. **Issue:** [CF #84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84). **PR:** [CF #85](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/85), draft.
**Baseline da main da rodada:** 2a770a8136f8ca4877e865be3e3b7745a6d4b168; **branch:** pesquisa/m03-02-governo-responsabilidade-20261014. Não houve mudança no texto normativo experimental, repositório CLF ou ratificação D. Propriedade funcional: M03; interfaces M02/M04/M05/M06/M07/M12/M14.

## FEITO
- Dossiê \`M03-02_03_TRES_LEGISLATURAS_E_CONTRAFACTUAL_PRESIDENCIAL_v0.1.md\`: três Câmaras fictícias de 100 cadeiras e SEIS trajetórias alternativas, B1/B2/B3, censura construtiva, confiança hipotética, orçamento, possíveis saídas e contrafactual presidencial reformado.
- \`M03-02_03_COMPOSICAO_LEGISLATURAS.csv\`: 13 registros partidários sintéticos; soma 100 em L1, L2 e L3.
- \`M03-02_03_EVENTOS_SIMULADOS_AUDITAVEIS.csv\`: **29 votações** fictícias explicitadas em 6 trajetórias; IDs únicos, partições de cadeiras e quóruns. Os resultados de B2 distinguem aprovação já na primeira fase (SIM>=51) de aprovação apenas no segundo escrutínio (SIM>NÃO).
- \`M03-02_03_CONTRAFACTUAL_PRESIDENCIALISMO.csv\`: 6 votações hipotéticas de orçamento em idênticas composições legislativas, sem presumir origem da legitimidade presidencial nem substituir impeachment por censura.
- \`scripts/validar_m03_02_simulacoes.py\`: verificador reproduzível de aritmética, partidos e quóruns (executar explicitamente; não valida direito).
- QA aritmética executada também de modo independente em JavaScript no ciclo da pesquisa: **PASS**, 3 legislaturas, 6 trajetórias, 29 votações parlamentares e 6 votações no contrafactual presidencial. Atenção: não informar que script Python foi executado se CI não o provar.
- Achado crítico: L3/P2 mantém gabinete investido por 45 a 37 com 18 abstenções e incapaz de aprovar orçamento (45 a 47), enquanto censura com 47 votos não elege sucessor por exigir 51. A derrota do orçamento NÃO é confiança, censura ou dissolução automática. A saída por confiança voluntariamente requisitada não é institucionalmente assegurada se premier deseja permanecer.

## FONTES PRIMÁRIAS E LITERATURA
- GG Alemanha arts. 63,67,68,111: https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html e https://www.gesetze-im-internet.de/gg/art_111.html .
- Constituição espanhola, arts. 99,113–115,134(4), consolidada BOE 20/05/2026: https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229&p=20260520 .
- Cheibub, Przeworski, Saiegh (2004), British Journal of Political Science, democracias 1946–1999: https://doi.org/10.1017/S0007123404000195 .
- Cheibub (2002), Comparative Political Studies, presidencialismos 1946–1996: https://doi.org/10.1177/0010414002035003002 .
**Ressalvas:** texto legal e estudos observacionais reais NÃO validam frequência ou probabilidade de nossos cenários fabricados. Não há estudo atualizado brasileiro de custo fiscal, governos minoritários, disciplina, eleição antecipada e second chamber nesta rodada.

## PENDENTE
1. M02: incentivos de abstenção, partidos e eleição antecipada, janela de dissolução; rejeitar alteração oportunista.
2. M04: segunda Câmara/representação territorial; orçamento/consentimento e salvaguarda federativa.
3. M05: continuidade fiscal e direitos sociais; duração, reindexação, limites de despesa, receitas, impostos e dívida, sem transformar orçamento derrotado em confiança tácita.
4. M06: justiça constitucional e imparcialidade de chefe de Estado; não judicializar mérito orçamentário e político.
5. M07/M12: limites de governo provisório, atos urgentes, nomeações e poderes militares.
6. M14: eleição suplementar, interinidade, preservação de mandatos e regras de dissolução sucessiva.
7. **Revisão de desenho:** riscos R1 (conciliação fiscal obrigatória), R2 (iniciativa parlamentar de questão de confiança), R3 (dissolução objetiva por impasse persistente) e R4 (aceitação do bloqueio com gestão fiscal restrita). Nenhum antídoto selecionado.
8. Dados empíricos e pareceres ainda não obtidos; novas referências requerem consulta às fontes oficiais. Nenhuma escolha entre presidencialismo e parlamentarismo aprovada.
9. O CI estrutural do commit 00a6c808c757ca51e14faccf84653369be710187 retornou **workflow concluído com sucesso** em consulta direta, mas não se afirma que esse workflow tenha executado o validador M03 específico; verificar CI novamente no último SHA após adicionar este pacote.

## PRÓXIMO PASSO PRIORITÁRIO — M03.02.04
Realizar teste de incentivos estratégicos do bloqueio e examinar R1–R4, com três governantes adversariais:
- G1: primeiro-ministro deliberadamente propõe orçamento inaceitável para fabricar dissolução.
- G2: oposição se recusa a formar sucessor e bloqueia orçamento para provocar nova eleição.
- G3: chefe de Estado não cumpre nomeação vinculada e tenta controlar calendário.
**Insumos:** dossiê e matrizes M03.02.01–03, M02.01/M04.01/M05.01, pareceres M06/M14. **Saída:** tabela ator–condição–quórum–prazo–efeito–salvaguarda–objeção, teste contra presidencialismo reformado, parecer de portas deliberativas F6 com alternativas realmente distintas. **Sem redigir CF-NOR ou registrar D sem deliberação explícita.**

## INTEGRAÇÃO / ESTADO
Pesquisar não é ratificar. Toda alteração permanece em PR draft #85, sem merge. A main pode avançar por coordenação de M01/M09/M12; antes de qualquer merge conferir SHA real, conflitos e validações. Ao abrir esta rodada, PR #85 estava temporariamente marcado não-mergeable após avanços em governança; comparação de caminhos observou edições novas apenas em governanca/13 e /14, fora do escopo M03. A leitura posterior devolveu mergeable=true; evitar afirmação permanente de ausência de conflito e revalidar no último HEAD.