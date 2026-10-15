# M01.09 — Pacote de continuidade e interfaces

**ID:** CF-M01-S009 · **Data:** 13/10/2026 · **Estado:** pesquisa e auditoria transversal F0–F5, testes F8 parciais; **sem decisões substantivas ratificadas nem texto normativo definitivo**.  
**Main consultada:** `35703d9fec8a30579faa0d8dad079e149923f8bf`, com protocolo M00.03 e `CF-NOR-0003–0007` em status H. **PR de pesquisa:** #22, branch `pesquisa/m01-01-catalogo-direitos-v01`, sem merge.  
**Origem:** M01.01–M01.08; [issue #5](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/5).

## Arquivos consultados de fato
- `redacao/propostas/CF-NOR-0003.md` (blob `d3570b22594451a02e5cc4f240d23fd56f694026`).
- `redacao/propostas/CF-NOR-0004.md` (blob `7eec23891f0cb95efa577f0476a514e3e843a4aa`).
- `redacao/propostas/CF-NOR-0005.md` (blob `00c00fa1eaa0101d14f8f06f35661ac8f4982d88`).
- `redacao/propostas/CF-NOR-0006.md` (blob `992c31fbe1a96e4d7a43cc9e063422889d0d4ab6`).
- `redacao/propostas/CF-NOR-0007.md` (blob `21d238a368b8ac0ad3c2f077af60fc8b6b6c6fa5`).
- `governanca/11_TECNICA_DE_REDACAO_E_INTEGRACAO.md` (blob `dc6cdab9e2fab7a6608d2448763fefd834297cb7`).
- `scripts/gerar_anteprojeto.py`, `scripts/validar_repositorio.py`, `redacao/indice.csv` da main.
- `modulos/M01-direitos-fundamentais/M01-07_MATRIZ_DE_CONTINUIDADE.csv` (16 grupos na main) e pesquisa M01.01–08 (PR22).
- CF/1988 atualizada [Câmara até EC 139/2026](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html); STF [Tema 698](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=698); CDPD equivalente à Constituição [Dec. 6949/2009](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/decreto/d6949.htm).

## Entregas
1. `M01-09_ARQUITETURA_E_AUDITORIA_TRANSVERSAL_v0.1.md`: diagnóstico do piloto e arquitetura funcional em quatro camadas, alternativas A/B/C, nove perguntas Q01–09, interfaces, hierarquia de prioridades, limites e fontes.
2. `M01-09_MATRIZ_TRANSVERSAL_GARANTIAS.csv`: **96 grupos** por fonte/função, dispositivo piloto, cobertura inicial, destino, tipo G/E/A/T e risco. Distribuição: 4 cobertura geral parcial; 7 parcial; 14 ausente especial; 71 não equivalente.
3. `M01-09_TESTES_INTEGRACAO.csv`: **20 cenários adversariais** destinados a testar supressão silenciosa, reserva de lei, direitos sociais, restrições, tutela e transição.
4. Este pacote.

## O que é verificado e o que não é
- **Verificado:** texto dos cinco `CF-NOR` H, índices do projeto, localização de conjuntos de garantias na CF/1988, existência de direitos sociais e garantias instrumentais específicas, Tema 698 e CDPD constitucional.
- **Interpretação preliminar:** estado de *cobertura pelo piloto* e proposta de camadas/tipos e agrupamentos. 96 linhas **não** são 96 direitos autônomos nem auditoria exaustiva artigo por artigo.
- **Não demonstrado:** equivalência material, impacto distributivo, custo, suficiência dos remédios/financiamento/transição, compatibilidade final com demais módulos, tutela satisfatória de cada instituto; consultas integrais a todos os acórdãos e tratados pertinentes.
- Os códigos `NAO_EQUIVALENTE` e `AUSENTE_ESPECIAL` indicam **ausência de proteção específica no piloto hipotético atual**, não revogação do direito vigente; nunca usar contagens para afirmar quantitativamente “direitos retirados”.

## Erros a bloquear no próximo trabalho
1. `CF-NOR-0006` geral não se confunde com reserva penal, interceptação, busca, prisão ou proibições absolutas.
2. `CF-NOR-0007` não assegura automaticamente habeas corpus, mandado de segurança, de injunção, habeas data, ação popular, assistência jurídica gratuita e presunção de inocência.
3. `CF-NOR-0004` não substitui direitos concretos de férias, jornada, SUS, educação, Fundeb, previdência, assistência, povos indígenas ou ambiente.
4. A vinculação horizontal `CF-NOR-0005` não torna todos particulares devedores de prestação universal idêntica à do Estado.
5. O art. 5º §2º (abertura) e §3º (tratados) exigem tratamento próprio, conjunto M00/M13; inclusão da CDPD equivalente à Constituição não pode ser suprimida por editoração.
6. `CF-NOR-0003` não representa por si direitos originários territoriais nem direitos políticos completos.

## Pacote prioritário sugerido
- **M01.10 — liberdades civis e políticas em interfaces:** liberdade de expressão/consciência/religião/reunião/associação/circulação e limites particulares; direito à informação, objeção, religião, direitos de fonte, conflito com antidiscriminação.
- **F7 H exploratória em branch baseada na main atual**, se útil ao método: primeiras fontes CF-NOR novas *autônomas* para direitos substantivos nucleares, sem duplicar `0003–0007`; toda ficha exige índice canônico, regeneração da vista e testes. A existência de fonte separada não equivale a decisão de mérito.
- M05/M09/M06/M12/M11/M10 devem ser consultados antes de inserir quaisquer normas especiais que possam ter custos, reservas, território, controle e tutela próprios.
- Antes de merge: verificar SHA atualizado da main e do PR22; caso outro chat já tenha criado novos `CF-NOR`, não reutilizar IDs nem editar cópias antigas.

## Questões para futura deliberação
- Aprovar ou não o modelo B de quatro camadas e qual sua localização topográfica;
- decidir direitos fundamentais com regras próprias sem excesso de detalhamento;
- avaliar perdas reais versus simplificação legítima em cada linha N:N;
- integrar diretrizes de M00/M13 sobre tratados e fontes;
- especificar remédios M06 e reservas penais M12;
- manter proteções financeiras e distribuição M05/M09, especialmente pisos constitucionais e transições até 2097 quando pertinentes.

**Nada foi ratificado por este pacote.** A futura aprovação de norma requer decisão explícita documentada. CI valida apenas estrutura, não direito vigente, equivalência, mérito nem causalidade.

## Atualização de concorrência e piloto de F7 — ainda em 13/10/2026

Após esta auditoria, a `main` avançou para `c321aecf9c6a479e7f4635cf44775706a9baeb0e` e **recebeu quatro cláusulas adicionais H**:
- `CF-NOR-0008` igualdade jurídica/material (G);
- `CF-NOR-0009` discriminação direta/indireta (E da 0008);
- `CF-NOR-0010` acessibilidade e adaptação razoável (E da 0009);
- `CF-NOR-0011` medidas especiais para igualdade efetiva (E da 0008).

A matriz de **96 grupos acima é fotografada contra o piloto de CINCO normas `0003–0007` da main no SHA de entrada**, **não** deve ser reproduzida como retrato atualizado da cobertura de igualdade depois da adição de `0008–0011`. A mudança posterior exige **nova auditoria incremental**, sem apagar a linha histórica.

Um primeiro PR editorial exploratório [#44](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/44) colidiu com os IDs `0008–0010`; foi **fechado SEM MERGE** para proteger a fonte única. Sua proposta de igualdade foi descartada como duplicação editorial, e a privacidade/dados foram refeitos em branch da main atual com IDs livres:
- [PR #45 — `CF-NOR-0012` privacidade e `0013` dados pessoais](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/45), ambos **A/H**, com índice e vista derivados atualizados, SEM decisão D, SEM equivalência demonstrada e SEM integração à main. Verificar resultado CI e conflitos antes de qualquer merge.

**Procedimento futuro obrigatório:** ler `main` imediatamente antes de reservar IDs e, caso tenha avançado, reconciliar índice e vista gerada. Não tentar forçar merge de branch antiga, nem reabrir #44 sem reconstrução. Os documentos do PR #22 e do #45 têm funções distintas: **pesquisa e auditoria** versus **piloto editorial hipotético**.

## Rodada incremental de 14/10/2026 — auditoria com o anteprojeto realmente existente

**Versão principal relida:** CF `main=df689704613ab389bdbef4228857f162e66ae8cd` (20 fichas H `CF-NOR-0001–0020`, 18 materiais do M01). **PR de redação #59** com `0030/0031` H *não integrado*. **Pesquisa PR #22** permanece draft. Fonte vigente CF atualizada EC139/2026.

**FEITO:**
- [Auditoria incremental do PR22](M01-09_AUDITORIA_INCREMENTAL_PR22_MAIN_20261014.md) e [matriz 96×20 H](M01-09_ATUALIZACAO_96_CONJUNTOS_CF_NOR_0020.csv) adicionadas ao PR22. Estado classificatório: **7 parcial específico, 68 geral não equivalente, 16 sem especial na main e 5 somente em PR59**, todas sem equivalência material certificada.
- Comparados textos efetivos `CF-NOR-0003–0020` e dossiês M01.06/.07/.08/.09 e M01.10/.11; lacunas materiais identificadas em tutela, penas/garantias penais, privacidade/dados, liberdades civis e direitos sociais.
- STF [Tema 698](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=698), [Tema 548](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?classeProcesso=RE&incidente=5085176&numeroTema=548), [Tema 6](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=6), [Tema 1234](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=6335939&numeroTema=1234) (com alterações em 2026) e STJ [Tema 1178](https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?cod_tema_final=1178&cod_tema_inicial=1178&novaConsulta=true&tipo_pesquisa=T) checados em páginas oficiais; esgotamento de todo material decisório **não** afirmado.
- M06.01 [issue #55](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/55) e M09.01 [issue #56](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/56) iniciaram pesquisa própria em PRs separados.

**PENDENTE:** auditoria granular juridicamente exaustiva dos 96 conjuntos e 29 arquivos originais, exame integral dos precedentes e fontes empíricas, revisão de compatibilidade com as especializações da main, dados fiscais M05 e interfaces M06/M09/M12/M13, CI do último SHA do PR22 e eventual merge. **Não** declarar suprimidos os direitos identificados como lacuna: o piloto é incompleto, não direito positivo. PR #59 exige revisão das reservas de domicílio e comunicações antes de merge.

**PRÓXIMO:** iniciar auditoria especializada de remédios judiciais e devido processo com M06.01, direitos materiais trabalho/saúde/educação com M09.01; revisar PR22 em lotes de fontes e compatibilidade, **antes** de sugerir integração. Não editar `redacao/` nesta branch, nem elevar H a D.

**Qualidade/proveniência:** matriz N:N por 96 *grupos* e remissões **não equivale** a 96 artigos, direitos individuais ou certificação material de proteção. O GitHub Action é apenas estrutural. Fechar rodada com status de PR, SHA e check atualizados.
