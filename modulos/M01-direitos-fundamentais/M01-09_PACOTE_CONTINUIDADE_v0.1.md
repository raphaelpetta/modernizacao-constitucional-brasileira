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
