# M03.03.01 — Controle da rodada e continuidade
**Data:** 15/10/2026 · **ID:** CF-M03.03-CONT-001 · **Estado:** H/P/A/V; F6/D/F7 **NÃO realizados**.
**Main base:** 2a770a8136f8ca4877e865be3e3b7745a6d4b168.
**Distinção:** esta pesquisa está em branch própria, e **não** altera o PR #85, o PR #99, CF-DEC-006, redacao/indice.csv, CF-NOR ou CLF.

## FEITO
- Verificado que M03.02 R01/02 já mencionavam África do Sul, investidura negativa, censura não construtiva e subtipos semipresidenciais; novidade desta rodada é a comparação sistemática com diretórios, executivos parlamentares protegidos e eleitos diretamente com filtros de candidaturas.
- Produzido M03-03_01_DOSSIE_ARQUITETURAS_ALTERNATIVAS_v0.1.md: 11 famílias/variantes de trabalho, fontes constitucionais identificáveis, critérios de rejeição e metodologia que separa antecedentes internacionais de inovação projetual.
- Matriz M03-03_01_MATRIZ_11_ARQUITETURAS.csv: 11 linhas X-A a X-K; 12 colunas; inclui eleição, chefias, permanência, censura, orçamento, objeção e fonte.
- Matriz M03-03_01_15_TESTES_ADVERSARIAIS.csv: 15 casos T01–T15; 8 colunas; inclui vulnerabilidade, condição de reprovação e interface destinatária.
- **QA executado por leitura efetiva do GitHub e script JavaScript:** 11 linhas/12 colunas, 15 linhas/8 colunas; IDs não duplicados, nenhuma linha com campos ausentes. Essa QA verifica forma e cobertura do arquivo, **NÃO** equivalência comparativa, desempenho real, validade jurídica ou execução de cenários.
- Distinção substantiva: Suíça executa governo colegiado sem presidência executiva unipessoal; Uruguai 1952 experimento abandonado; África do Sul presidente executivo removível politicamente; Micronésia presidente executivo eleito parlamentarmente para prazo fixo; Kiribati combinação de indicações parlamentares/eleição popular e dissolução por censura; Singapura presidente popular com veto de reserva; Noruega parlamentarismo sem dissolução; Israel voto direto do premiê abandonado.

## PENDENTE
- Parecer funcional de M02/M04/M05/M06/M07/M12/M14 sobre alternativas, inclusive igualdade do voto, interesse territorial, poderes de chefia de Estado, direitos, orçamento e mandatos.
- Pesquisa empírica real brasileira sobre coalizões, legislação, confiança, veto, federalismo, orçamento e custos de transição; nosso material não possui amostra causal.
- Verificação contextual histórica sobre por que o Uruguai abandonou colegiado e o Israel revogou voto direto do premiê; sem explicações monocausais. Conferir legislação nacional atualizada diretamente antes de citar como texto final, sobretudo fontes secundárias de Kiribati, Equador e comparadores de microestados.
- 15 testes são **especificações** e não execução com resultados. Falta ficha constitucional completa para cada um dos seis protótipos prioritários.
- Não há decisão P de selecionar arquitetura final nem decisão D de sistemas de governo. A recomendação de estudo continua reversível. Necessidade de nova consulta popular brasileira juridicamente obrigatória é CONTROVERTIDA, não resolvida por precedentes estrangeiros.

## PRÓXIMO — M03.03 R02
1. Preparar seis fichas simétricas X-A, X-B, X-D, X-F, X-G e X-H cobrindo 10 elementos constitucionais (eleição, duração, ministérios, confiança, destituição, orçamento, dissolução, defesa, federação e transição).
2. Priorizar **testes discriminantes**, sem novas matrizes ficcionais repetitivas: X-D contra X-G (responsabilidade difusa ou individual com mandato protegido); X-F contra X-B (censura sobre pessoa governante ou gabinete com chefe de Estado separado); X-H contra X-A (filtro parlamentar dos candidatos e custo da censura); X-G contra X-A (a origem parlamentar de um mandato fixo altera legitimação e barganha?).
3. Reexecutar T01/T02/T03/T05/T07/T11/T14 sob cada texto hipotético e registrar inconsistências, não probabilidades. Separar provas da fonte de valores do protótipo.
4. Somente com evidência nova, voltar a F6. Se algum modelo for incapaz de assegurar cadeia civil única de comando, tutela de direitos e autorização fiscal, corrigir ou descartar a CONFIGURAÇÃO, não eliminar sua família inteira.
5. Levar à pauta existente PR #99 o fato de que A/B/C já não são uma lista fechada **sem mesclar** branches, e registrar manifestação eventual do usuário em CF-DEC apenas de forma expressa.

**Aviso de continuidade:** abertura desta frente autoriza pesquisa. Não há plebiscito, PEC, decisão D, norma CF-NOR, integração com CLF ou merge na main. CI estrutural do novo PR deve ser verificada no HEAD exato, caso venha a existir.
