# CF-CC-001 — Auditoria global do produto e primeira entrega M07

**Data:** 15/10/2026. **Baseline da main CF:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Natureza:** fotografia e desenvolvimento experimental, sem deliberação normativa. **Issue central:** [#103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103). **PRs de protocolo:** [#104](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/104) e [#101](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/101), ambos drafts não integrados ao baseline.

## Duas dimensões, não confundidas

- **Produto na main antes desta PR:** 20 CF-NOR H, de M01 (18), M04 (1), M05 (1), nenhum D/P; compilado `redacao/anteprojeto-de-trabalho.md`. O índice contabiliza dispositivos, **não** exaustão dos direitos.
- **Pesquisa/planejamento:** dispersos em main e PRs drafts; não contam como cláusulas integradas. Com esta PR, o **ramo proposto** passa a 21 H, incluindo 1 M07; a main continua com 20 enquanto não houver merge.
- **Estados:** maturidade documental (`MAPEADO`, `MINUTADO_H`, `INTEGRADO_EXPERIMENTAL`, `AUDITADO`) é distinta de `D/P/H/A/V`. Nenhum H foi ratificado.

## Auditoria de 15 módulos (recortes demonstrados, NÃO completude global)

| Módulo | H na main | Base documental mais imediata | Lacuna prioritária para avanço |
|---|---:|---|---|
| M00 | 0 | fontes, reservas e ADCT na main | espécie normativa, hierarquia, poder de reforma e interfaces CLF |
| M01 | 18 | main; PRs #22, #59 | liberdades, remédios, concordância N:N e reservas privacidade/dados |
| M02 | 0 | PR #95 | eleições gerais e proteção contra mudança oportunista; M03/M14 |
| M03 | 0 | main; PRs #85, #99, #100 | variantes articuladas e processo legislativo; escolhas F6 abertas |
| M04 | 1 | main | repartição geral de competências, território e controles |
| M05 | 1 | main | tributação, orçamento, equalização real e dependências fiscais |
| M06 | 0 | PRs #62, #96 | remédios, justiça institucional e garantias de coerção digital |
| M07 | 0 | PR #102 | primeira cláusula H de procedimentos/acesso digital nesta PR, pendente auditoria |
| M08 | 0 | apenas planejamento sistemático conhecido | iniciar F0 por propriedade, intervenção, concorrência e serviços |
| M09 | 0 | PR #63 | saúde, educação, seguridade e trabalho: titulares/custeio/tutela |
| M10 | 0 | PR #89 | deveres ambientais, clima, participação e efeito intergeracional |
| M11 | 0 | PR #94 | territórios, consulta, remédios e autonomia coletiva |
| M12 | 0 | PR #82 | controles da investigação e regimes excepcionais, M01/M06 |
| M13 | 0 | PR #98 | tratados, convencionalidade e proteção internacional |
| M14 | 0 | PR #91 e reconciliação #97 | transição, mandatos, controle e compatibilidade de reforma |

**Principal falha:** 12 dos 15 módulos ainda não aparecem na fonte normativa da main, apesar do acervo de estudos. Em muitos módulos, cobertura funcional sequer foi delimitada exaustivamente; não estimar percentual global. Especialmente M08, o catálogo geral não substitui mapeamento jurídico. **Segunda falha:** garantias da CF/1988/ADCT não dispõem de concordância N:N global fechada. **Terceira:** a compilação é ordenada por sequência de criação das fichas, não por arquitetura constitucional final. **Quarta:** a concentração de versões em PRs drafts exige controle de colisões ao integrar (em especial #59, que edita o índice e a mesma vista compilada).

## Entrega vertical desta rodada

- Criada ficha experimental `redacao/propostas/CF-NOR-0021.md`, **M07, H/G**, proveniente das 12 funções do PR #102; novo índice em ordem **0230**, preservando ordens 0210/0220 propostas pelo PR #59 (CF-NOR-0030/0031, ainda não integrados).
- Atualizada **vista gerada** `redacao/anteprojeto-de-trabalho.md` com o corpo H, sem alterar os 20 dispositivos anteriores.
- O texto contém preservação explícita de contraditório/defesa, acesso a petições, inclusão digital e não exclusão de remédios/sigilos; isso **não** prova não regressão jurídica. A ficha registra dez âncoras de concordância parcial/pendente e oito testes adversariais, sem resultados inventados.
- Opções institucionais H-A/H-B e localização final permanecem abertas. A redação é variante utilizável, não aprovação de conteúdo.

## Distribuição dinâmica da próxima fila

1. **Horizonte subcoberto:** M08 F0 com propriedades e limites, serviços, concorrência e recursos, assegurando âncoras CF/ADCT e interfaces M04/M05/M07/M10/M11; se houver base suficiente, criar H em PR próprio, sem cláusula fictícia.
2. **Aprofundamento jurídico:** executar testes M07 com casos reais/hipotéticos discriminados, concordância N:N e revisões M01/M04/M06/T07/T43; decidir se conservar H-invariante ou apresentar variantes H-A/H-B, sempre sem D automático.
3. **Arquitetura sistêmica:** M03 transformar as alternativas #99/#100 em pacotes normativos comparáveis de Governo/Parlamento/lei com salvaguardas M02/M04/M05/M06/M14; submeter eventual escolha ao usuário.
4. **Rotação posterior:** M09/M10/M11 ou M06 conforme dependências e menor presença no texto, evitando mais de três ciclos no mesmo núcleo sem justificativa.

**Critério de escolha:** primeiro ganho de cobertura real, depois criticidade constitucional e interfaces desbloqueadas, sem divisão de horas igualitária. É recomendável **1 recorte vertical + 1 frente horizontal + 1 interface** por rodada, sujeitos a reavaliação do risco e das novas entregas. Não medir sucesso pela quantidade de arquivos/PRs.

## CI, integração e decisões

**QA local documental desta entrega:** conferir ID não usado na main, marcadores únicos, colunas/ordem do índice, comparação dos primeiros 20 textos sem alteração e recompilação determinística. **QA remoto de GitHub Actions:** somente considerar aprovado após status conclusivo no HEAD da PR; não há certificação jurídica. **Merge:** não autorizado sem revisão/anuência sobre o texto material. Caso #59 ou #104 avancem primeiro, rebase/reconstrução do compilado e nova auditoria de reservas obrigatórios.

**Deliberações materiais necessárias (não tomadas):** (i) direito autônomo à boa administração H-B versus técnica H-A distribuída; (ii) intensidade das obrigações nacionais e custeio da inclusão digital; (iii) sistemas de governo M03 A/B/C e transição, em pauta separada; (iv) efeitos de CF M00/M03/M14 sobre o CLF DEC-016, competência exclusiva da central CLF.

## Interface CF–CLF

[Central CLF #48](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48): encaminhar apenas quatro requisitos funcionais verificáveis de M07: **(a)** âmbito federal/estadual/municipal e aplicação de leis específicas; **(b)** intimação efetiva e defesa em meios eletrônicos; **(c)** apoio ou canal alternativo e acessibilidade; **(d)** dados de terceiros e sigilo. Solicitar devolutiva sobre T07/T43, **sem editar** o repositório CLF ou absorver seus modelos e decisões.

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** inventário main/PRs, diagnóstico dos 15 módulos, cláusula H em fonte canônica + índice + compilado desta branch, controles e fila dinâmica.  
**PENDENTE:** auditoria N:N integral da CF/1988/ADCT, revisão substantiva externa, resultados dos oito testes M07, status CI ao término do PR, choque editorial com #59, PRs #101/#104, ratificações F6.  
**PRÓXIMO:** executar M08 F0 autônomo; testar/revisar M07 H; preparar M03 alternativas redacionais auditáveis. Nunca promover H→D por mero resultado estrutural do CI.
