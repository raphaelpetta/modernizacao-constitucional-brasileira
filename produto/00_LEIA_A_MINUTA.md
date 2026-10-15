# Produto constitucional de trabalho — instruções de leitura
**Estado:** texto constitucional experimental; nenhum dos dispositivos H é ratificado.

## A minuta já existe
- [Ler o texto corrido compilado atual da Constituição](../redacao/anteprojeto-de-trabalho.md): 20 propostas CF-NOR H de M01/M04/M05 na `main` de entrada de 15/10/2026.
- [Ver os 20 IDs e metadados canônicos](../redacao/indice.csv).
- [Consultar os arquivos com justificativas e testes](../redacao/propostas/).
- [Conferir o compilador existente](../scripts/gerar_anteprojeto.py).

**Não criar uma segunda cópia do anteprojeto** em outro diretório. Toda alteração no produto passa pelo índice e pelos arquivos fonte, em branch/PR, seguida por `python scripts/gerar_anteprojeto.py` e `python scripts/gerar_anteprojeto.py --check`. As propostas ainda só abrangem alguns M00–M14; não existe texto constitucional completo. Os demais módulos aparecem no [quadro do produto](../central/QUADRO_PRODUTO.csv) até terem unidades reais.

## Formatos para visualizar e decidir
1. **Vista limpa:** texto gerado existente; IDs do projeto visíveis até numeração editorial posterior; sem fingir que artigos isolados compõem Constituição completa.
2. **Vista crítica:** arquivos `redacao/propostas/CF-NOR-####.md` com razões, objeções, verificações e interfaces; PRs concorrentes não são decisões.
3. **Mapa global:** M00–M14 por funções e garantias, confrontado com CF/1988 e ADCT, incluindo lacunas documentadas.
4. **Pauta decisória:** variantes concretas de artigos, impactos Mxx, melhor objeção e consequências de transição; H/P/A/V versus D separados.

## Critério para aproximar o produto final
Produzir primeiro um **anteprojeto progressivamente mais abrangente e coerente**, mesmo com decisões abertas. O selo de `MINUTADO` exige texto real; `INTEGRADO` exige teste de remissões/garantias/dependências; `AUDITADO` exige prova proporcional. Nem compilação nem QA estrutural comprovam validade material. Evitar criar artigos neutros artificiais ou copiar a CF/1988 sem reformulação crítica.

[Central CF](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103) · [Interface CLF](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48).
