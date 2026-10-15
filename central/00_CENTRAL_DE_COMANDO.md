# Central de comando — Constituição Federal
**Corte inicial:** 15/10/2026 · **Situação:** protocolo operacional de trabalho EM PR; não é decisão constitucional material.
**Comando CF:** https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103
**Comando CLF (interface):** https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48
**Pesquisa e governança preexistentes:** PR #101; **fonte de conteúdo vigente no projeto:** `redacao/indice.csv`, `redacao/propostas/` e compilador `scripts/gerar_anteprojeto.py`.

## Produto em primeiro plano
A entrega final em construção é um texto constitucional único, legível e criticável — **experimental até ratificação**. Usar a **fonte normativa canônica já existente** (`CF-NOR`, índice e fontes), não duplicar artigos nesta central. Vista textual: [anteprojeto-de-trabalho.md](../redacao/anteprojeto-de-trabalho.md), reconstruível com `python scripts/gerar_anteprojeto.py`, verificação `--check`. Quando houver alteração no índice ou nas cláusulas, recompilar e testar a vista na **mesma PR**. IDs persistentes não são numeração final. A CF/1988 e ADCT atuais são base de confronto, **não** fonte automática das escolhas futuras.

## Horizontalidade + verticalidade: regra de execução
**Horizontal:** o ciclo deve considerar TODOS os M00–M14, a cobertura funcional e as lacunas sistêmicas, com impulso especial a áreas subdesenvolvidas. Não dividir horas igualmente nem declarar completude por número de módulos/arquivos.
**Vertical:** em cada intervenção escolher **um recorte fechável**, da função/garantia à fonte atual, controvérsia, texto H/variantes, correspondência N:N, interface e teste jurídico proporcional. O resultado preferido é um **delta de texto rastreável**, não outro dossiê inconcluso. Alternar fontes de demanda (lacuna, dependência, decisão madura, correção de garantia). Não inventar artigo para ocupar espaço.
**Rotação:** conferir entregas recentes e evitar três ciclos substantivos seguidos no mesmo núcleo enquanto houver frente independente negligenciada com contribuição viável; exceção motivada por risco, dependência ou oportunidade de fechamento. Pode haver 1–2 frentes profundas por rodada e uma interface transversal.

## Fases independentes; nunca colapsar aprovação e maturidade
`NAO_MAPEADO` → `MAPEADO` → `RECONSTRUIDO` → `MINUTADO_H` → `INTEGRADO_EXPERIMENTAL` → `AUDITADO_NO_RECORTE`; progresso não é necessariamente linear. **D/P/H/A/V** é eixo distinto. Não promover H→D, escolher modelo político, suprimir garantia ou autorizar texto material por silêncio. Lacunas fora do texto como registro editorial, não cláusulas simuladas. Quando uma escolha impedir a variante, manter alternativas e trabalhar invariantes.

## Critérios de qualidade proporcionais
- Direitos, coerção, regimes de exceção, eleições, competências, separação de poderes, saúde, povos vulneráveis, finanças e transição são de risco material alto (R3) mesmo quando o texto parece simples.
- Guardar origem da proteção na CF/1988/ADCT, titular, âmbito, exceções, via de tutela, implementação, temporalidade e destino na proposta. Sem perda silenciosa de garantias; controles N:N.
- Pesquisa deve conter melhor objeção e resultado que poderia mudar a preferência; evitar ciclos redundantes, rankings artificiais e revisão circular da própria IA.
- CI e scripts detectam problemas documentais; **não** certificam equivalência jurídica, mérito nem controle humano independente.
- Avançar textos experimentais em PR/branch; mesclar estudos após revisão documental permitida, mas **nunca** integrar como aprovado um dispositivo substantivo sem decisão expressa.

## Algoritmo de seleção da próxima rodada
1. Conferir SHAs de ambas as mains, PRs/CI, issue central, `redacao/indice.csv`, decisões, catálogos, handoffs e os últimos deltas.
2. Montar três candidatos independentes: uma lacuna horizontal; uma entrega textual vertical; uma necessidade transversal/decisória.
3. Escolher pelo maior benefício material demonstrável, menor risco de colisão, dependências, atraso relativo e custo do próximo resultado; justificar em 2–4 frases, **sem pontuação numérica fictícia**.
4. Executar, registrar fonte/data, SHA/branch/PR, mudança efetiva, teste realizado e pendente, módulo afetado e nova situação das garantias.
5. Atualizar quadro **somente quando o estado do produto efetivamente mudar**; encerrar com FEITO / PENDENTE / PRÓXIMO (3 tarefas alternativas).
6. Se faltar decisão: apresentar A/B, impacto no texto e recomendação condicional; não atribuir ratificação ao usuário. Impedimento de CI não trava trabalho não dependente.

## Primeiras entregas preferenciais
- **Produto:** validar compilação CF 20 H existentes em `main` e transformar em versão editorial limpa **sem mudar conteúdo**; criar ordem provisória transversal só com o que houver.
- **Cobertura:** preparar unidades concretas M07/M08 e outras frentes pouco refletidas no texto, com vínculo a CF/1988/ADCT e garantias, por PR próprio.
- **Sistema de governo:** M03 PRs #99/#100: produzir variantes normativas completas e invariantes M02/M04/M05/M06/M14; escolhas seguem A/P até ratificação.
- **Interface CLF:** remeter apenas dependências reais sobre normatização/competência, processo administrativo digital, fontes e transição; registros na issue #48, sem transposição automática.
- **Distribuição:** conferência a cada 14 dias por *novas funções cobertas, mudanças reais na minuta, garantias com destino verificável e áreas sem entrega*, sem porcentagem global sem denominador.

### Referências técnicas
[Regra de execução por camadas proposta — CF PR #101](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/101) · [Central CLF](https://github.com/raphaelpetta/codigo-legislacao-federal/issues/48).

## Controles operacionais verificáveis (propostos no PR)
- [Fila com recortes, estados, critérios e reservas](FILA_TRABALHO.csv).
- [Painel calculado exclusivamente do produto no checkout](PAINEL_GERADO.csv) — **presença no produto, não cobertura jurídica global**.
- [Política de integração experimental, ratificação e concorrência](01_POLITICA_INTEGRACAO_E_CONCORRENCIA.md).
- [Verificador e gerador do painel](../scripts/controle_operacional.py) (`--write` / `--check`).
- [Validação local de contingência](../scripts/validar_operacao_local.sh); falha de Actions sem steps não valida nem invalida documentos.
- [Minuta atual](../redacao/anteprojeto-de-trabalho.md). A compilação é uma vista derivada; não editar suas cópias de forma independente.

Os controles acima passam a ser definitivos somente após revisão e integração da documentação. O registro de tarefas não substitui a conferência dos PRs nem a revisão jurídica, e cada reserva é cooperativa.

## Integracao de PRs e prioridade da fila (atualizacao operacional)
O [plano de integracao dos PRs](02_PLANO_INTEGRACAO_PRS.md) registra a dependencia observada **#105 → #106 → #108 → #109**, mais o #107 independente, e as salvaguardas para nao fundir em `main` trabalhos de texto herdados sem conferir cada recorte. A [fila persistente](FILA_TRABALHO.csv) acompanha M07, M08, M10 e M03 como **EM_REVISAO** nesses PRs; nao iniciar do zero ou contabiliza-los como texto ja integrado. A [politica de portas](01_POLITICA_INTEGRACAO_E_CONCORRENCIA.md) separa PR, integracao experimental H e ratificacao D. Os [painéis](PAINEL_GERADO.csv) refletem o checkout das fontes versionadas, nao todos os PRs abertos.
