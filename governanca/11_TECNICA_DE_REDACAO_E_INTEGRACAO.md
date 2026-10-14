# M00.03 — Técnica de redação integrada da nova Constituição

**ID:** CF-GOV-011 · **Versão operacional:** 0.1 · **Corte:** 13/10/2026 · **Status:** metodologia de trabalho em teste, NÃO opção material ratificada.  
**Origem:** [issue #35 — M00.03](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/35).  
**Fonte do estado do projeto:** repositório CF, branch `main`, commit consultado e proveniência da pesquisa. **Não confundir** estado documental Git com promulgação constitucional.

## 1. Finalidade e quatro riscos

O texto deve ser **integrado, legível, modular e auditável**, sem que módulos funcionais de pesquisa obriguem capítulos próprios. Quatro riscos distintos:
1. **Repetição supérflua:** enunciado de mesma função repetido em diferentes artigos/títulos sem novo efeito.
2. **Conflito substantivo:** dois dispositivos atribuem competências, garantias ou limites incompatíveis; sinônimos e remissões também podem esconder contradições.
3. **Supressão disfarçada:** compactação de garantias atuais elimina quem deve prestar, prazos, tutela, financiamento, limites de competência ou controle.
4. **Excesso de abstração/remissão:** regra geral tão ampla que demanda litígios para revelar exceções; cadeia de remissões entre artigos impede leitura autônoma.

**Nem toda repetição é erro:** repetição funcional pode ser deliberada para reforço de tutela, independência, acessibilidade ou delimitação de direito específico. Sua necessidade e seu efeito deverão estar documentados. Eliminar redundância verbal nunca é justificativa suficiente para suprimir garantia constitucional.

## 2. Cinco tipos funcionais — critérios editoriais, não espécies jurídicas

- **G — Geral:** regra transversal aplicável por padrão a matérias/órgãos/sujeitos determinados; dizer qual é o âmbito.
- **E — Especialização:** precisa materialmente a regra geral num contexto determinado, sem afastá-la. Registrar `regra_geral` e efeito adicional.
- **X — Exceção:** afasta ou modifica regra geral num campo delimitado. Exigir fundamento constitucional, sujeito, condição, procedimento, controle e cláusula de retorno ao geral.
- **A — Autônoma:** regra de função própria que não deve ser derivada artificialmente de norma genérica. Garantia, competência ou direito próprio pode se enquadrar aqui.
- **T — Transitória:** disciplina entrada em vigor, adaptação, recepção, continuidade, prazo e efeitos residuais; não é inferior à parte permanente.

A categoria principal pode coexistir com qualificações de direito, dever, competência, garantia institucional, procedimento e objetivo. `G/E/X/A/T` não equivale à lista de espécies legislativas do M00.02.

## 3. Princípios operacionais da redação

**Uma função normativa principal por disposição.** Reunir o mesmo problema sob um enunciado lógico, sem combinar obrigações materialmente desconexas só para reduzir o número de artigos.

**Geral antes do especial, com exceção identificável.** Regra geral deve enunciar de modo inteligível o sujeito, comando e âmbito; regra especial deve indicar o que acrescenta ou afasta. Não exigir que o leitor siga várias remissões para compreender um direito essencial.

**Terminologia controlada.** Usar o mesmo termo para o mesmo conceito. Sinônimos podem gerar efeitos jurídicos diferentes; manter glossário de conceitos sensíveis (ente federativo, lei nacional/federal, legislação, órgão, autoridade, direitos, serviços essenciais).

**Competência, poder e responsabilidade separados.** Perguntar para cada dispositivo: quem legisla, quem executa, quem financia, quem fiscaliza e quem recebe tutela. Normas que alocam poder sem responsabilização institucional devem ser reexaminadas.

**Reserva constitucional e densidade.** Não constitucionalizar cada aspecto operacional, mas também não deslocar silenciosamente garantias, financiamentos e participação democrática a leis ordinárias. Usar M00.01 e `governanca/09_AUDITORIA_GARANTIAS.md`.

**Remissão expressa e limitada.** Preferir conteúdo autossuficiente e referência por ID de proposta durante a redação; resolver IDs em artigos numerados apenas na fase editorial consolidada. Não usar remissões do tipo "dispositivo anterior" na minuta final.

**Regras transitórias separadas pela função.** Disposições do ADCT vigente podem ter efeitos até 2097; renumerar, resumir ou excluir parte transitória sem avaliação de direitos, créditos, finanças e efeitos residuais é proibido no projeto.

**Não fixar estrutura antes da decisão.** Títulos, capítulos e numeração de artigos serão definidos segundo coerência de funções após deliberação; `M00–M14` são módulos de pesquisa, NÃO uma divisão final obrigatória.

## 4. Duas fontes editoriais que NÃO devem divergir

**Fonte única da norma:** `redacao/propostas/CF-NOR-####.md`. Cada arquivo contém entre os marcadores `<!-- NORMA-INICIO -->` e `<!-- NORMA-FIM -->` só a redação candidata. O restante do arquivo guarda justificativa, objeção, fontes e salvaguardas, **fora do anteprojeto montado**.

**Registro canônico de posição e estado:** `redacao/indice.csv` com ID, ordem editorial provisória, tema, módulo, tipo G/E/X/A/T, estado H/P/D, caminho da fonte, vínculo à geral, justificativa de especialidade, decisão rastreável, auditoria de garantias e dependências. O índice não é duplicação do texto: guarda seu identificador e metadados.

**Vista integrada derivada:** `redacao/anteprojeto-de-trabalho.md`, **GERADA SOMENTE** por `python scripts/gerar_anteprojeto.py`. Não editar manualmente essa vista. Em CI, `--check` bloqueia deriva entre texto fonte, índice e documento gerado.

**Status:** H = hipótese de redação; P = proposta preferida não ratificada; D = ratificada com entrada `CF-DEC` e evidência de ratificação explícita. `H` não torna norma vigente, aprovada nem parte definitiva do anteprojeto. O ato de integrar a proposta experimental via PR **não** converte H em D.

**Histórico:** IDs nunca são reutilizados; modificações relevantes exigem registro de substituição, confronto com a CF/1988 e revisão do módulo de origem. O artigo definitivo só recebe numeração na fase de integração ratificada, não pela ordem provisória.

## 5. Checklist de novo dispositivo e bloqueios

1. Função constitucional, assunto, pessoa/órgão responsável e norma da CF/1988 relevante identificados?
2. Já existe uma regra `G` que cubra a mesma função? Se sim, a especial adiciona algo juridicamente indispensável?
3. Tipo `E` ou `X` tem `regra_geral` e justificativa **expressa**?
4. Termos, remissões, relações com direitos e competências dos demais módulos compatíveis?
5. Direitos/garantias do texto atual: correspondência `1:1, 1:N, N:1, N:N`; eventuais perdas analisadas no procedimento de auditoria?
6. Se houver lei/ato de implementação, espécie, competência, iniciativa e controle consistentes com o M00.02 e o CLF?
7. Há disposições transitórias, direitos creditórios ou efeitos retroativos relevantes?
8. O documento deixa claro melhor argumento contrário e alternativa menos intervencionista?
9. O texto ainda é H/P ou a ratificação substantiva está realmente registrada como D?
10. O PR passou pela validação estrutural E pela revisão humana contra duplicação semântica, exceções conflitantes e perdas materiais?

## 6. Comparação normativa e limites metodológicos

**Brasil:** LC 95/1998, arts. 10–11, unidade do artigo, texto claro/preciso, parágrafos complementam/excepcionam e uso consistente de terminologia. É referência técnica da redação, **não prova de que todo seu formato de lei comum deva ser constitucionalizado**. Fonte: https://www2.camara.leg.br/legin/fed/leicom/1998/leicomplementar-95-26-fevereiro-1998-363948-normaatualizada-pl.html .

**África do Sul:** Constituição arts. 7, 8 e 36: regras gerais de vinculação/alcance/limitação de direitos se combinam com garantias específicas do capítulo de direitos. A fórmula `law of general application` do art. 36 não corresponde necessariamente à exigência brasileira de lei formal parlamentar. Fonte: https://www.gov.za/ts/documents/constitution/chapter-2-bill-rights .

**Alemanha:** Lei Fundamental arts. 1(3), 19 e 80: vinculação geral dos poderes públicos aos direitos, regime geral de limitações com garantias específicas e limites de delegação regulamentar. Não basta importar os artigos sem seus mecanismos institucionais e jurisprudência. Fonte: https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html .

**União Europeia:** guia conjunto de redação legislativa enfatiza consistência, precisão e previsibilidade; não tem autoridade vinculante sobre a Constituição brasileira. Fonte: https://op.europa.eu/en/publication-detail/-/publication/3879747d-7a3c-411b-a3a0-55c14e2ba732/language-en .

## 7. Limitações da verificação automatizada

A automação pode verificar **IDs, estados, tipos, referências, sequência, ausência de texto duplicado literal, campos vazios e deriva da compilação**. NÃO pode, por si só, detectar antinomias materiais complexas, redundância conceitual, violação de direitos, repartição inválida de competência ou inconsistência entre propostas politicamente abertas. Essas tarefas exigem revisão humana fundamentada com dossiês e fontes.

**Porta atual:** permitir iniciar redação F7 experimental `H` em assuntos com pesquisa parcial suficiente, mantendo o texto integrado explicitamente provisório. A consolidação substantiva de D, a arquitetura de governo e a versão `v1.0` dependem de deliberação posterior. A prioridade de estudos M01, M06, M14 e de auditoria transversal permanece alta.
