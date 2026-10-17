# Protocolo de execução por cobertura, risco e integração — CF

**ID:** CF-GOV-017 · **Data:** 15/10/2026 · **Natureza:** diretriz operacional integrada seletivamente ao repositório CF; não aprova qualquer artigo ou escolha constitucional. Complementa a [CF-GOV-019](19_POLITICA_GANHO_MARGINAL_GLOBAL.md). Complementa CF-GOV-002, 009, 012 e 016.

## Objetivo e limites
Transformar pesquisa dispersa em proposta constitucional integral, com rastreabilidade de proteções, testes de funcionamento e preservação da liberdade deliberativa. **Não** abreviar exame jurídico necessário, confundir entrega experimental com direito vigente, impor opção política ou declarar equivalência por aparência textual.

## Três trilhas simultâneas (não uma sequência rígida)
1. **Cobertura funcional:** identificar funções da CF/1988/ADCT, grupos titulares, garantias especiais, órgãos, receitas, competências e interfaces ainda não tratados. Usar `catalogo/MODULOS.csv` como mapa de escopos inicial, não censo exaustivo de dispositivos; o mapa específico de cobertura proposto no PR #101 requer reconciliação e **não foi incorporado** por esta operação. Registrar `NAO_EXAMINADO` sem presumir ausência de proteção.
2. **Desenvolvimento com profundidade proporcional:** F0–F5 e, quando possível, F7 de dispositivos experimentais `H`; concentrar revisão jurídico-empírica nas incertezas que poderiam modificar solução/garantias.
3. **Integração e auditoria:** construir texto de trabalho funcionalmente completo, inclusive lacunas e variantes, sem converter placeholders em dispositivos normativos. Fazer revisão transversal CF/1988 → função/garantia → proposta → efeitos → transição → CLF.

As trilhas podem avançar em paralelo; a carência de uma decisão F6 não bloqueia investigação, texto condicional nem trabalho independente.

## Quarta função transversal: convergência decisória sem interromper as três trilhas

As três trilhas existentes **continuam independentes e simultâneas**. Em cada preflight e encerramento, comparar a entrega adicional esperada de **cobertura H, vertical V, integração I, e deliberação/fechamento D**. D não tem quota temporal nem autorização para contornar garantia; uma questão madura sobe à pauta e libera pesquisa em outra frente. A carteira é coordenada na [pauta única](../central/03_PAUTA_DELIBERACAO_PROGRESSIVA.md), vinculada à issue #103; usar dossiês, fontes e matrizes existentes, sem PR ou relatório para cada troca de status.

**Fluxo local, repetível e reversível:** `PESQUISA_FOCAL` → `PREFERENCIA_PROVISORIA`/investigação complementar → `APTO_A_DELIBERAR` (declarar *nível*: orientação, princípio/arquitetura ou redação) → registro expresso de eventual `RATIFICADO_D` → `FECHADO_NO_RECORTE` quando verificados efeitos e interfaces. `BLOQUEADO_POR_DEPENDENCIA` afeta **a decisão indicada**, não todo trabalho: prosseguir em invariantes, outros módulos e hipóteses H. Esse fluxo orienta trabalho e não substitui D/P/H/A/V ou G1–G4.

**Relação H↔D:** a fonte versionada de CF-NOR não é atualizada automaticamente ao deliberar um princípio; um D de arquitetura não resolve seus artigos instrumentais. O sistema vigente (CF/1988/ADCT) e as alternativas seguem separados. Fechamento local exige auditoria N:N do recorte e interfaces identificadas; fechamento sistêmico exige integração das decisões interdependentes; global exige exame integral de CF/ADCT, transições e antinomias. Reabrir somente por evidência decisiva, erro, regressão de direitos, conflito de decisões ou autorização expressa, preservando histórico `SUBSTITUIDA`.

**Aplicação piloto:** (a) questão estrutural conjunta M00/M02/M03/M14, aptidão **orientadora** a qualificar sem fingir D; (b) salvaguardas M07/M08/M10/M11 do PR #139 com revisão R3 ainda bloqueante para ratificação, mas execução H/V/I livre. Evitar induzir fechamento material por total de normas, número de módulos ou CI aprovada.

## Estados separados: maturidade técnica e aprovação política
**Maturidade técnica por função:** `MAPEADA` (escopo/fontes e lacunas), `RECONSTRUIDA` (direito vigente e prática no recorte), `PROPOSTA` (variantes/recomendação e redação H quando cabível), `INTEGRADA_PROVISORIA` (texto experimental ou interface com variantes), `AUDITADA_NO_RECORTE` (evidências, garantias e testes adequados à classe de risco); `NAO_EXAMINADA` quando sem recorte. A trilha e o recorte devem ser explicitados: não inferir sequência concluída só por existir um arquivo.
**Status normativo:** manter **D/P/H/A/V** de CF-GOV-003 sem equivalência automática com a maturidade técnica. Um item pode estar tecnicamente auditado e politicamente `A`; `D` exige ratificação expressa.

## Classificação de risco por efeito, com promoção obrigatória
- **R1, baixo:** terminologia, remissão e estrutura sem evidência de alteração material; verificar fonte, rastreabilidade, comparação literal e efeitos possíveis.
- **R2, moderado:** alterações editoriais com potencial interpretativo, delimitação setorial, novas interfaces; análise de especialidades, precedentes e simulações focais.
- **R3, alto:** direitos/restrições, coerção, eleições, separação dos poderes, federalismo, finanças, justiça, grupos vulneráveis, alterações potencialmente irreversíveis e transição; exigência de comparações relevantes, evidência disponível, análise de implementação, revisão adversarial e independência de crítica.

O risco de um detalhe isolado pode ser R3 independentemente do módulo. Incerteza substancial sobre direitos ou competência **impede homologação**, não impede pesquisa independente. Nenhuma média de risco autoriza compensar possível violação de direito por conveniência administrativa.

## Critério de encerramento técnico e abertura responsável
Para cada investigação: (1) alternativas decisivamente plausíveis; (2) fato/precedente realmente verificado e fonte/datacorte; (3) objeção mais forte; (4) garantia/direito com destino; (5) efeito institucional e transição; (6) evidência faltante e se ela plausivelmente inverteria a preferência; (7) próximo ato: `APTA_A_DELIBERAR`, `PREFERENCIA_PROVISORIA`, `PESQUISA_FOCAL`, `BLOQUEIO_MATERIAL` ou `AVANCAR_INVARIANTE`. Não declarar `AUDITADA_NO_RECORTE` se proteção essencial não tiver destino ou a verificação requerida não tiver ocorrido. Um estudo apto à deliberação não equivale a decisão D.

## Política antitravamento e fluxo de trabalho
- Descrever dependência como `BLOQUEIA_RATIFICACAO`, `BLOQUEIA_VARIANTE` ou `NAO_BLOQUEIA_TRABALHO_INVARIANTE`. Diante de decisão pendente, redigir variantes condicionais e avançar em salvaguardas invariantes. Nunca escolher silenciosamente.
- Limite inicial de trabalho em curso: até **duas frentes substantivas ativas da CF** e uma interface transversal compartilhada com CLF, excluindo pesquisas em espera; é política revisável, não restrição a descobrir questões novas.
- Ao concluir uma rodada, registrar entrega **materialmente nova**, estágio do recorte, garantia conferida, riscos, arquivo/PR/commit, pendências e próxima tarefa desbloqueada. Se o ganho incremental for apenas cosmético, alternar a frente.
- Rever periodicamente PRs antigos quanto a duplicação, base obsoleta, direitos omitidos e integração documental; integrar pesquisa validada não ratifica suas propostas H.
- Não reescrever `governanca/13_QUADRO_DE_COORDENACAO.md` em cada ciclo: preservá-lo como histórico, com resumo corrente específico e atualização apenas em marcos relevantes.
- Antes de afirmar cobertura integral, confrontar Constituição atual e ADCT por **função e garantia**, inclusive disposições dispersas; não inferir percentuais do número de arquivos ou cláusulas.

## Texto condicional e interface CLF
O anteprojeto funcional é construído apenas pelo pipeline `redacao/propostas/` + `redacao/indice.csv`. Lacunas/variantes aparecem em documentos de controle e estudos, **não** como artigos fictícios na fonte normativa gerada. Cada variante identifica interfaces M00–M14 e CLF, riscos de implementação e dispositivo transitório associado. Cláusulas `CF-NOR` só seguem regras existentes de IDs e não mudam para D sem o usuário.

## Proteções irrenunciáveis
Auditoria N:N de continuidade material dos direitos existentes; dignidade/igualdade/devido processo/tutela/privacidade e regimes especiais; fonte primária datada; análise de capacidade estatal e abusos; distinção entre teste automatizado, revisão jurídica e deliberação; rastreamento de lacunas em vez de supressão tácita. Revisão do mesmo agente, sem contraste independente de fontes e argumentos, não é auditoria humana independente.

## Indicadores quinzenais (sem percentuais fictícios)
Contar funções com estado/verificação demonstrável; número de garantias com destino ou lacuna explícita; quantidade de variantes técnicas maduras; conflitos intermodulares críticos; tempo gasto em loops/CI; PRs de pesquisa integrados e ainda pendentes. Denominador preliminar e instável implica **sem percentual de completude global**.

**Relação:** coordenação CLF em [CLF-GOV-020](https://github.com/raphaelpetta/codigo-legislacao-federal/blob/main/governanca/20_EXECUCAO_CAMADAS_E_AUDITORIA.md) é interface proposta, não incorporação automática; conferir existência/branch ao consultar.
