# CF-IC-001 — Recepção da pesquisa CLF sobre Código juridicamente único

**ID:** CF-INT-004 · **Data:** 13/10/2026 · **Origem:** CLF T01.M04, pesquisa sobre promulgação e atualização.  
**Status:** H/A/V — hipóteses, perguntas e verificações; **SEM decisão constitucional ratificada**.  
**CF lida:** `6e91df55d8801b1a14e0295b511f5e56dbb100eb`. **CLF base:** `c04c78aa5dc42ae8f40da9641c6c4726709d046e`; pesquisa integrada à `main` do CLF no commit `3a5a4977b51b4666d16ab453769ed98cb0442982` via [PR CLF #18](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/18).  
**Vínculos constitucionais:** M00.01/M00.02 (fontes, espécies, reservas), M03.01 (processo legislativo e bicameralismo), M04 (competências), M14 (transições/reforma constitucional), sem impor arquitetura de módulos.  
**Premissas externas:** no CLF, **DEC-001** é objetivo de um Código único realmente integrado; **DEC-016** permanece pendência sobre a forma jurídica. Nenhuma das opções a seguir foi escolhida.

## 1. Pergunta transferida à pesquisa constitucional

A futura Constituição deveria permitir a formação e a alteração de **um corpo único de legislação federal geral/permanente juridicamente promulgado**, preservando competências, iniciativas reservadas, exigências de quórum, garantia de direitos, procedimentos parlamentares e direito intertemporal? Se sim, **como**?

É inadequado confundir:
- um portal de leis vigentes, que não modifica direito;
- títulos aprovados por leis distintas e depois apresentados numa coleção unificada;
- um **único Código positivo** promulgado com unidade formal, mas composto de matérias cujas garantias deliberativas precisam continuar identificáveis.

## 2. Modelos sob comparação — todos H, não decisões

| Hipótese | Mecanismo | Melhor argumento | Objeção estrutural |
|---|---|---|---|
| P2 transitório | Promulgação por título em veículos competentes, corpus editorial comum | Operacionalizável sem redesenhar integralmente a CF/1988 em todos os casos | Não satisfaz automaticamente Código formalmente único |
| P3/CP | **Procedimento constitucional especial** de formação de texto legal uno por propostas componentes de iniciativas legítimas, com votação por matéria | Possível menor mudança de espécies e manutenção de regras substantivas | O ato único pode constituir espécie nova **de fato** se promulgação e atualização não forem explicitadas |
| P4/CE | **Espécie constitucional “Código”** com classes internas definidas pela reserva **material**, iniciativas separadas e aprovação final unitária | Reconhece formalmente o novo tipo, torna o problema explícito | Complexidade, litígio de classificação, risco de quórum artificial e veto/globalização dos efeitos |
| P5 | Redesenho funcional de espécies/reservas e dos códigos permanentes no sistema novo | Potencial simplificação sistemática | Exige decisão ampla sobre direitos, poderes, quóruns e competência federativa; não pressupor aceitação |

**Análise CLF:** `modulos/T01/M04/MODELOS_07_PROMULGACAO_E_ATUALIZACAO_CODIGO.md`. **Dois anteprojetos alternativos, NÃO RATIFICADOS:** `modulos/T01/M04/ESBOCOS_CONSTITUCIONAIS_07_CP_CE.md`, com propostas CP/CE ainda **incompletas** quanto a promulgação, sanção, veto, conciliação bicameral e recusas dos titulares de iniciativa. **Matriz de teste:** `modulos/T01/M04/MATRIZ_MODELOS_PROMULGACAO_07.csv` (18 cenários).

## 3. Caso concreto de confronto com o texto constitucional vigente

**Tributário:** CTN arts. 173–174, matéria abrangida pelo art. 146, III, b, da CF/1988; STF SV 8. A LC 236/2026 modificou o art. 174. A aprovação por maioria ordinária não pode apagar reserva constitucional material nem ignorar a versão de 2026.

**Materialidade da espécie:** LC 70/1991, art. 6º, II, e Lei 9.430/1996, art. 56, no precedente STF RE 377.457/Tema 71 e SV 62. A forma LC histórica não transforma toda disposição em matéria reservada para futura alteração; os textos citados ilustram contexto histórico, não benefício atual.

**Iniciativa judicial:** Lei 11.416/2006 (PL 5845/2005 do STF) e art. 96, II, b, da CF. Reforma material de quadro/remuneração reservado exige proponente adequado. **A constitucionalidade de revogação e reedição literalmente fiel por proposta parlamentar com LC 95 art. 14, §2º, não está pacificada**; não supor que `C0` cure possível vício de iniciativa.

## 4. Questões que M00/M03 não devem omitir

1. **Definição de unidade positiva:** ato formal único? O que o promulga, como é sancionado/vetado e o que significa uma alteração posterior de disposição ordinária em texto inicialmente aprovado por maioria reforçada?
2. **Iniciativas múltiplas e divergentes:** cada titular inicia seu componente; o ato final pode reuni-los? O que ocorre se um Poder recusa submeter texto? É possível incorporar apenas remissão externa sem mascarar cobertura incompleta?
3. **Votações componentes e votação final:** o quórum/veto final pode anular a garantia material anterior? Como respeitar reexame bicameral de emendas?
4. **Consolidação neutra e reforma material:** pode haver certificação institucional de equivalência; quem certifica, como contesta, quem controla judicialmente, e qual efeito da certificação nas iniciativas reservadas?
5. **Autonomia constitucional e federação:** atos privativos das Casas, orçamento periódico, regulamentos, Constituição/EC, normas subnacionais e tratados permanecem em seus procedimentos jurídicos; uma referência no Código não pode convertê-los em norma federal legislativa comum.
6. **Serviço público de codificação:** quem publica, corrige erros e fornece versões oficiais sem adquirir poder legislativo; como garantir história, atos revogados com efeitos residuais, direitos e acesso?
7. **Direitos e reformas:** alteração de lei punitiva, tributária, processual ou de direitos não se presume editorialmente neutra por reorganização topográfica.

## 5. Direito comparado pertinente e seus limites

- **EUA/OLRC:** títulos do US Code promulgados como `positive law` com tabela de origem e destino; a existência de título positivo não prova Código universal formal único. https://uscode.house.gov/codification/legislation.html
- **Nova Zelândia:** `Legislation Act 2019`, ss. 59–62 e 92–99, distingue revisão de direito vigente, exceções de mudança e certificação, e possui regimes de publicação. Não equivale ao sistema federal bicameral brasileiro. https://www.legislation.govt.nz/act/public/2019/0058/latest/DLM7298381.html
- **Espanha:** Constituição art. 82, delegação expressa, matéria e prazo definidos, diferencia reformulação e harmonização. Não admite transposição automática de regimes orgânicos. https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229
- **Itália:** Constituição art. 76, delegação com princípios/diretrizes, objetos e prazo. https://www.senato.it/istituzione/la-costituzione/parte-ii/titolo-i/sezione-ii/articolo-76
- **França:** Constituição art. 38, autorizações e ratificação de `ordonnances` em seu próprio regime. https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019241024/2026-06-26
- **Brasil:** CF/1988 arts. 51, 52, 59, 61, 63, 65, 69, 96 e 146; LC 95 arts. 13–14; precedentes STF indicados no CLF.

Esses modelos oferecem técnicas e alertas, **não comprovam validade de CP/CE no direito brasileiro vigente**.

## 6. Encaminhamento recomendado, sob autoridade autônoma do projeto CF

- **M00.02:** comparar se a proposta constitucional deveria criar *espécie Código* (P4) ou regra de processo coordenado sem espécie nova (P3). Testar tipologia de fontes e reservas já catalogadas no próprio projeto.
- **M03.01:** projetar **fluxo completo** de iniciativa múltipla, votações por componente, conciliação bicameral, sanção/veto, promulgação e alteração posterior; rejeitar modelos que se tornem espécie nova oculta ou eliminem veto constitucionalmente protegido.
- **M14:** examinar efeitos transitórios para normas antigas e direitos ainda em curso, inclusive transição tributária longa; nenhuma norma antiga desaparece por não ter sido indexada.
- **Coordenação:** devolver ao CLF apenas um parecer de compatibilidade e alternativas, com `CF-IC-001` e versões/commits. **Não transferir como decisão texto dos anteprojetos CP/CE**.
- **Porta crítica:** antes de ratificar qualquer artigo, simular 3 casos reais (CTN LC material, conteúdo ordinário de LC formal, lei judicial de iniciativa reservada) do início da proposta ao eventual veto e alteração futura.

**Resultado do encaminhamento:** interface adicionada como pesquisa condicionada. **Não mudou qualquer decisão constitucional.**
