# M12.01-R2 — Redline constitucional P4 e teste de regressão da prova digital

**Corte:** 14/10/2026 · **ID:** CF-M12-S001-R2 · **STATUS:** P/V/A, **não decisão D nem CF-NOR**. **Main de referência:** `19cd7a58d4d2addbb960f7e76ecd59c3bcc958a1`; [issue #80](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/80), [PR82](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/82), interlocução com M01.13 [PR59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59) e M06 [PR62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62). Complementa parecer M12.01-R1. **Não houve edição dos direitos H `CF-NOR-0030/0031`.**

## 1. Decisão editorial substancial que continua aberta

A solução **P3-E** reproduz como proposta o núcleo da exceção de identificação fortuita do STF Tema 977; **P3-R** prefere reserva judicial inclusive para essa identificação, ampliando a proteção frente ao direito interpretado hoje; **P3-S**, no primeiro parecer M12, tentou combiná-las mas conservou remissões genéricas ("condições constitucionais precisas") e um limiar indeterminado de dados "intensamente" pessoais. **P4** abaixo testa remédios redacionais para esses defeitos sem declarar a escolha ratificada.

### P4-E — exceção expressamente delimitada e fiscalizável (alternativa P, não H)

> A apreensão legal de equipamento eletrônico não autoriza, por si, o acesso investigativo ao conteúdo de comunicações e dados pessoais nele armazenados. A consulta estatal coercitiva para fins de investigação criminal depende de consentimento livre e expresso do titular dos dados ou de decisão judicial prévia, fundamentada em elementos concretos, proporcional e delimitada quanto à pessoa, finalidade, objeto e alcance.
>
> **Exclusivamente quando telefone celular for encontrado fortuitamente no contexto de fato supostamente criminoso**, sem ter sido apreendido como objeto de diligência destinada à investigação de seu conteúdo, admite-se consulta estritamente necessária para **identificar o proprietário do aparelho ou esclarecer a autoria desse fato**, mediante registro contemporâneo da localização, das circunstâncias, da razão da consulta e das categorias de dados examinados, com **justificação posterior e possibilidade de revisão judicial**. Essa faculdade não autoriza pesquisa exploratória de fatos estranhos, acesso irrestrito a conversas, imagens, arquivos pessoais ou contas remotas, nem pode ser invocada para converter apreensão em flagrante ou por mandado em suposto encontro fortuito.
>
> Para impedir perecimento de prova, a autoridade poderá, antes de ordem judicial de acesso, executar medidas **tecnicamente necessárias de conservação** dos dados e metadados de aparelho legalmente apreendido, documentando motivação, escopo, operações realizadas, integridade e custódia, com justificação posterior e mecanismos eficazes de controle; **preservar ou produzir cópia forense não constitui, só por isso, autorização para examinar livremente o conteúdo com finalidade investigativa**.
>
> A lei regulará meios técnicos, proteção de terceiros e sigilo profissional, acesso adequado da defesa, controle judicial e consequências dos ilícitos, sem ampliar as hipóteses constitucionais de acesso não consentido. Interceptações de comunicações em curso seguem reserva judicial e finalidade constitucional específica em cláusula própria.

**Melhoria da P4-E:** delimita evento, objeto (celular), fim, proibição de uso para investigação nova, prova documental e revisão. **Limitações:** (i) "sem ter sido apreendido como objeto de diligência" é teste fático P novo, não fórmula literal STF; situações-limite de delito flagrante e encontro fortuito simultâneos precisam apreciação; (ii) o texto parece preservar a exceção no plano constitucional com rigidez alta, mesmo que o futuro constituinte queira reduzir poderes policiais; (iii) declaração de proibição de "conversas" deve ser lida como proibição de **devassa não necessária**, porque às vezes identificação mínima poderá envolver número/contato relacionado ao fato; refinar com M06/M07/M01 e técnica legislativa para evitar colisão com o próprio propósito; (iv) a cláusula de preservação não estabelece até quando pode persistir sem submissão ao juiz; requer prazo legal adequado e controle ex post. **Não** transpor exceção do celular a nuvens, provedores ou biometria por analogia automática.

### P4-R — reserva mais restritiva sem exceção identificadora, com acesso judicial urgente (alternativa distinta)

> A apreensão legal de equipamento não autoriza, por si, a leitura investigativa de dados e comunicações nele armazenados. O acesso estatal coercitivo dependerá de consentimento livre e expresso do titular ou de ordem judicial individualizada e fundamentada, com objeto, finalidade e alcance delimitados. A lei instituirá **procedimento judicial prioritário e de plantão** para identificação urgente de proprietário ou autor, inclusive quando o aparelho tiver sido encontrado fortuitamente.
>
> A conservação técnica estritamente necessária dos dados de aparelho legalmente apreendido, com registros e justificação posterior, não autoriza consulta investigativa do conteúdo. Permanecem preservados sigilo de terceiros, contraditório efetivo e medidas contra abuso.

**Melhoria:** não constitucionaliza nova licença de acesso por encontro fortuito. **Consequência material deliberada:** ao eliminar exceção identificadora do Tema 977, **não representa equivalência fiel ao conjunto de poderes policiais atualmente reconhecidos**; seria opção constitucional mais protetiva. Precisa estudo de custo/capacidade do plantão e de socorro a vítima/identificação em crime urgente; o texto não pode presumir que polícia acesse o conteúdo enquanto "aguarda" mandado.

## 2. Parecer jurídico sobre qual deve progredir

**Recomendação de metodologia, não decisão de mérito:** manter **P4-E e P4-R lado a lado até decisão deliberativa**. É metodologicamente indevido escolher apenas por curta redação. Se o projeto priorizar continuidade funcional da tese STF977, P4-E é candidata editorial mais próxima; se priorizar máxima reserva judicial, P4-R é candidata de nova política de direitos. **Nenhuma das duas é candidata a aprovação H neste momento**, porque ainda faltam M01 (direito de dados), M06 (contraditório e exclusão), M07 (supervisão e dados administrativos), M12 (casos-limite de flagrante/fortuito) e teste N:N completo.

**A quem cabe o quê?** M01 direitos e restrições; M12 função policial, discricionariedade permitida e conservação; M06 decisão judicial, assistência técnica/contraditório e consequências processuais; M07 protocolos de execução, transparência e responsabilidade; CLF disciplina operacional e penal. Constituições não devem especificar algoritmo hash, modelo de ferramenta forense ou forma única de coleta de prova.

## 3. STJ 2026: limite entre licitude e confiabilidade

A [Jurisprudência em Teses **281** de 03/06/2026](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/03062026-Nova-edicao-de-Jurisprudencia-em-Teses-traz-entendimentos-sobre-prova-digital-e-dados-estaticos-de-conexao.aspx) resume necessidade de integridade da cadeia de custódia, exame técnico independente e distinção de dados estáticos versus interceptação de fluxo. O [Informativo STJ **879**](https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisar&aplicacao=informativo&b=INFJ&i=41&l=20&livre=%22HC%22&p=true&refinar=S.DISP.&t=) documenta AgRg no HC **1.014.212/ES**, Sexta Turma, julgamento 10/02/2026, com necessidade de perícia complementar **quando houver dúvida razoável** sobre autenticidade/integridade.

Por outro lado, a [decisão RHC **237.288/AM**, Sexta Turma, julgada 15/09/2026, publicada 21/09/2026](https://scon.stj.jus.br/SCON/pesquisar.jsp?O=RR&b=ACOR&p=true&preConsultaPP=4945%2F0&thesaurus=JURIDICO&tp=T) exige indícios concretos de quebra da cadeia, não nulidade automática por afirmação genérica; a [decisão AgRg no HC 1.074.020/SP, Quinta Turma, publicação 26/08/2026](https://scon.stj.jus.br/SCON/pesquisar.jsp?O=RR&b=ACOR&p=true&preConsultaPP=4208%2F0&thesaurus=JURIDICO&tp=T) também trata de cerceamento e via inadequada para revolver amplamente prova em habeas corpus. Essas decisões **não** permitem dizer que qualquer ausência de hash gera nulidade ou que a defesa precise provar adulteração impossível de investigar sem acesso aos elementos necessários.

**Teste triplo M12 — independente:**
- **L (legalidade):** observou-se a reserva judicial/consentimento/exceção correta? Violação da reserva de ingresso/acesso não se cura com hash perfeito.
- **I (integridade):** a prova é tecnicamente confiável? Uma falta documental pode exigir perícia complementar se houver dúvida razoável, mas nem toda formalidade ausente implica adulteração.
- **C (contraditório):** a defesa teve acesso tecnicamente suficiente para impugnar, preservando intimidade de terceiros? Uma cópia perfeita inacessível à defesa pode gerar restrição processual própria.

**Regra proposta P:** garantir constitucionalmente devido processo e acesso útil à prova, deixar padrões tecnológicos e soluções de nulidade concreta à lei/jurisprudência compatíveis com garantia constitucional de exclusão de prova ilícita.

## 4. Matriz de não regressão, portões de revisão e critérios adversariais

Anexo `M12-01_TESTES_REDLINE_P4.csv`: **18 cenários**, cada um com proteção constitucional, comportamento adversarial e diferença entre P4-E/P4-R. Pontos de bloqueio:
- Celular encontrado por acaso durante atendimento emergencial vs aparelho apreendido de suspeito (classificação fática, registros e escala do acesso).
- Preservação técnica completa de memória vs extração/consulta substancial: a primeira pode envolver leitura instrumental de bytes, mas não acesso investigativo livre.
- Dados em conta remota de terceiro sem aparelho apreendido, localização ao vivo, biometria, metadados estáticos: **fora do perímetro da exceção** até estudo específico.
- Ordem judicial que cita genericamente "todos os dados" sem finalidade/suspeita individualizada.
- Prova ilícita de origem com perícia perfeita; prova lícita com fragilidade de integridade; defesa privada de acesso útil.
- Controvérsia de modulação do Tema977 para prova obtida antes do julgamento: texto de Constituição nova não reescreve automaticamente efeitos de acórdão anterior.
- Especialidade não pode apagar CF5 XI (domicílio), XII (sigilo), LIV/LV/LVI (devido processo/contraditório/prova ilícita) e LXXIX (dados).

**Gatilhos para eventual ficha E H:** G1 alternativa E/R escolhida conscientemente; G2 revisão M01/M06/M07 e M12; G3 perímetro sem remissão em branco; G4 consequências prova/controle; G5 bibliografia STF/STJ vigente e acórdãos lidos quando necessário; G6 fonte única/ID disponível e matriz N:N. **Estado:** todos ainda PENDENTE/PARCIAL, sem CF-NOR.

## 5. Fonte primária e rastreabilidade
- [STF Tema 977 e julgamento 25/06/2025](https://portal.stf.jus.br/processos/detalhe.asp?incidente=5173898), incluindo item 2 que alude a "referido acesso" no contexto de preservação; texto do voto-vista anterior não é tese final.
- [STJ JTes281/2026](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/03062026-Nova-edicao-de-Jurisprudencia-em-Teses-traz-entendimentos-sobre-prova-digital-e-dados-estaticos-de-conexao.aspx), [Informativo879/2026](https://scon.stj.jus.br/jurisprudencia/externo/informativo/?acao=pesquisar&aplicacao=informativo&b=INFJ&i=41&l=20&livre=%22HC%22&p=true&refinar=S.DISP.&t=), [RHC237288/AM/2026](https://scon.stj.jus.br/SCON/pesquisar.jsp?O=RR&b=ACOR&p=true&preConsultaPP=4945%2F0&thesaurus=JURIDICO&tp=T).
- [CF](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm), [CPP](https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689.htm), [Marco Civil](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm).

## FEITO / PENDENTE / PRÓXIMO
**FEITO:** correção P3-S em duas variantes P4-E/R mais rigorosas, confronto com STJ2026 e 18 cenários, ressalva de caso-limite. **PENDENTE:** deliberação de política, acórdãos completos em controvérsia, revisão M01/M06/M07, M12 prova/exceção e viabilidade do plantão; **não CF-NOR nem D**. **PRÓXIMO:** produzir confronto jurídico final P4-E/P4-R com objeção mais forte de cada órgão e remissões constitucionais específicas, submeter à discussão de mérito antes de reservar ID e redigir norma H.
