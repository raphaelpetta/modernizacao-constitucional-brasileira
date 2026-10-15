# M01.13 — Minuta integrada experimental de reservas especiais e tutela de dados (A+B)

**ID documental:** CF-M01-S013-R2 · **Data:** 14/10/2026 · **Status:** **P (protótipo NÃO ratificado)**. Não é dispositivo da Constituição; **nenhuma** ficha `CF-NOR` nova foi criada ou renumerada e o texto das propostas `CF-NOR-0030/0031` permaneceu INALTERADO. A implementação canônica na pasta `redacao/`, se vier a ser escolhida, exige reserva de IDs e nova verificação da main/PRs.  
**Base jurídica/documental:** main `e648bd71227f407f2b46207e9c8d546a255254d2`; [PR59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59) (H/draft); dossiê anterior `M01-13_ALTERNATIVAS_RESERVAS_E_TUTELA_v0.1.md`; parecer M06 [PR62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62), critérios C1–C10; [issue #57](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/57).

## 1. Conceito da integração e escolha de técnica

A regra **G** de direitos, restrições e tutela já existe em `CF-NOR-0003–0007` (H na main). Os direitos **A** de privacidade e dados estão no PR59 como `0030/0031` (H). A presente minuta testa **três especializações E** — DOM (domicílio), COM (sigilo/tecnologia), HD (remédio gratuito) — que acrescentam hipóteses explícitas onde regras gerais seriam insuficientes. **Não duplicar** no corpo de cada E o princípio geral de proporcionalidade, eficácia privada ou tutela geral; aplicar esses princípios cumulativamente. Outras garantias permanecem próprias de M06/M12/M07: devido processo, prova ilícita, poder investigatório, fiscalização da proteção de dados e responsabilidade de agentes.

**Porta de qualidade:** os trechos abaixo são texto de discussão, não aprovação de substituir art. 5º XI, XII, LXXII ou LXXVII da CF/1988; até auditoria completa, usar as garantias atuais como piso de teste e marcar cada exceção em aberto.

## 2. Três especialidades E propostas para teste (sem CF-NOR atribuída)

### E-DOM — domicílio, consentimento, exceções e revisão (texto P)

> O domicílio é inviolável. Ninguém poderá nele ingressar contra a vontade de quem legitimamente o ocupa, salvo: I — mediante consentimento livre e válido; II — em situação de flagrante delito, fundada em circunstâncias objetivas verificáveis; III — em caso de desastre; IV — para prestar socorro; ou V — por ordem judicial fundamentada, cumprida durante o dia.
>
> O ingresso coercitivo sem ordem judicial será limitado à situação que o justifica, documentado e sujeito a controle judicial posterior. Quando fundado em flagrante, as razões devem ser anteriores à diligência e justificadas posteriormente, asseguradas as consequências constitucionais do ingresso ilícito e a responsabilidade de seus autores.
>
> A lei disciplinará o modo de cumprimento, os registros, os direitos dos ocupantes, os limites espaciais da busca, a proteção de terceiros e a fiscalização, sem ampliar as hipóteses constitucionais de exceção.

**Observação crítica:** "durante o dia" conserva requisito material atual para ordem judicial, mas a definição de dia (civil/solar) e ingressos em espaço com peculiaridades exigem discussão M12. O termo "consentimento" exige regras de prova e voluntariedade; não transformar presença policial e silêncio em consentimento presumido. Flagrante não autoriza inspeção geral independente do motivo. Há um potencial **risco de interpretação** em incluir "consentimento" entre exceções quando é justamente hipótese de ingresso não coercitivo; redação pode ser reorganizada para separar consentimento e exceções compulsórias. Lei não pode criar sexta exceção indistinta.

### E-COM — correspondência, fluxos e conteúdos digitais (texto P)

> São invioláveis o sigilo da correspondência e das comunicações privadas, qualquer que seja a tecnologia empregada, bem como o núcleo protegido de sua confidencialidade informacional.
>
> A interceptação de comunicações privadas em curso dependerá de prévia decisão judicial fundamentada, nas hipóteses, para os fins e na forma definidos em lei para investigação criminal ou instrução processual penal, com delimitação de pessoas, objeto, duração, minimização dos dados de terceiros e controle da execução. A legislação não poderá instituir autorização geral e indiscriminada de interceptação.
>
> A apreensão lícita de equipamento não autoriza, só por isso, a exploração de seu conteúdo. O acesso coercitivo a comunicações e demais dados pessoais armazenados que afete intensamente a privacidade depende de decisão judicial individualizada e fundamentada ou de consentimento válido do titular, **ressalvadas hipóteses constitucionais estritas de identificação incidental e de preservação urgente de dados, sem exploração indiscriminada de conteúdo e sujeitas a controle posterior**.
>
> A lei disciplinará salvaguardas, garantias de cadeia de custódia, proteção de terceiros, controle de urgências e recursos efetivos, preservado o conteúdo essencial dos direitos fundamentais.

**Questão deliberativa de alta prioridade:** o terceiro parágrafo é deliberadamente **PENDENTE**: (i) o Tema 977 do STF estabeleceu acesso identificador limitado para **encontro fortuito** sem ordem ou consentimento, mediante justificativa posterior; (ii) autorizou providências **necessárias à preservação de dados e metadados**, antes da autorização, sujeitas à justificação posterior; (iii) no celular apreendido em flagrante ou art. 6º CPP, para **acessar** dados há consentimento livre e expresso ou decisão judicial com delimitação. A constitucionalização de uma exceção técnica precisa decidir se descreve **hipóteses** e sua amplitude ou remete ao tratamento penal por lei sem criar autorização indistinta. **A frase em negrito é ancoragem provisória, NÃO redação final suficiente** para equivalência. Separar investigação criminal de outros regimes constitucionais de acesso a informações (tributário, administrativo, prevenção com devido processo) a examinar por M07/M12. Não copiar mecanicamente a excepcionalidade telefônica de 1988 a todo tipo de mensagem/dado: auditar o grau de proteção. Não transformar “informação comunicacional” em proibição de acesso voluntário do próprio titular.

### E-HD — conhecimento, retificação, anotação e tutela gratuita (texto P)

> É assegurado a toda pessoa, gratuitamente, remédio judicial célere e efetivo para conhecer dados pessoais a seu respeito mantidos em registros governamentais ou de caráter público e obter sua retificação, garantida a anotação de contestação ou explicação nas hipóteses definidas em lei.
>
> A lei estabelecerá procedimento acessível, inclusive a pessoas com deficiência e sem meios digitais, com prazos razoáveis e meios de urgência, admitida a exigência de pedido prévio simples ao responsável quando necessária para caracterizar a recusa ou omissão, **vedado o esgotamento compulsório de recursos administrativos como condição geral de acesso à Justiça**.
>
> A proteção de dados pessoais perante responsáveis privados, inclusive em decisões automatizadas, será assegurada por meios administrativos e judiciais adequados nos termos das garantias gerais e da legislação, sem restringir a tutela constitucional da pessoa ou a proteção de terceiros.

**Decisão em aberto:** manter expressamente o nome histórico `habeas data` ou garantir a função gratuita pelo conteúdo; ambos podem proteger o direito se a equivalência procedimental for testada. CF/1988 art.5 LXXII/LXXVII garante HD e sua gratuidade, e Lei9.507/1997 arts7–8 prevê três funções e comprovação de recusa/prazos diferenciados (10/15 dias). **Não se está propondo incorporar esses números à Constituição.** O texto HD não torna gratuito todo e qualquer litígio privado sobre dados; garantir proporcionalidade de custas e assistência jurídica pela regra M06.

## 3. Teste de montagem editorial da Constituição de trabalho

| Peça | Tipo | Conteúdo e obrigação | Relação |
|---|---|---|---|
| `CF-NOR-0003…0007` (main) | Gerais G | Titulares, deveres, eficácia privada, limites, tutela | **Não reproduzir** |
| `CF-NOR-0030` (PR59) | Direito A | Vida privada, honra, imagem, domicílio e sigilo em nível geral | **Remissão obrigatória às E-DOM/E-COM**, hoje ainda inexistentes na fonte canônica |
| `CF-NOR-0031` (PR59) | Direito A | Proteção de dados, bases legítimas, segurança, contestação e fiscalização | Remédio E-HD via M06; não copiar estrutura ANPD sem M07 |
| E-DOM (este arquivo) | Especial E | Exceções de ingresso, razão objetiva, ordem diurna, controle | Tem conexão M12, processo penal e responsabilidade |
| E-COM (este arquivo) | Especial E | Interceptação em fluxo, dados armazenados, apreensão ≠ acesso, minimização | M12/M07, decisão judicial, prova ilícita |
| E-HD (este arquivo) | Especial E | Acesso e correção gratuitos em registros públicos/de caráter público | M06, Lei HD, direitos informacionais e M07 |

**Integração exata pendente:** texto atual do segundo parágrafo de 0030 diz que medidas dependem das "hipóteses e garantias específicas desta Constituição". Só será aceitável reconhecer equivalência após **concretizar e referenciar** E-DOM/E-COM na fonte canônica; vale o mesmo para 0031 e E-HD. Não criar fonte normativa paralela com o rótulo `CF-NOR` dentro deste dossiê.

## 4. Confronto jurídico N:N, garantias vigentes e pontos de regressão

| CF/1988 | Conteúdo mínimo a testar | Especialidade | Lacuna remanescente |
|---|---|---|---|
| 5 X e V | Intimidade/vida privada/honra/imagem, reparação e direito de resposta quando aplicável | 0030 A + M01.14 | Regime de imprensa e expressão não concluído |
| 5 XI | Consentimento; flagrante, desastre, socorro; ordem judicial diurna | E-DOM | Conceito de residência/terceiros/horário, exceções constitucionais específicas |
| 5 XII | Correspondência, telecomunicações e dados; reserva do fluxo nas hipóteses penais | E-COM | Conteúdo da exceção digital e relações intersetoriais |
| 5 LVI | Inadmissibilidade de provas obtidas por meios ilícitos | M06/M12, **não suprida por E-DOM sozinha** | Norma penal/processual específica em elaboração |
| 5 XXXV/LXXVIII | Jurisdição e tutela tempestiva | `0007` H + M06 | Tempo útil de interceptação, execução e reparação |
| 5 LXXII | Conhecimento e retificação de dados pessoais em bancos públicos/de caráter público | E-HD | Exigências legais de requerimento/administração/produção de prova |
| 5 LXXVII | Gratuidade do habeas data | E-HD | Ritos gratuitos efetivos e assistência |
| 5 LXXIX | Direito autônomo de proteção de dados | `0031` H | Segurança penal, revisões automatizadas, competências |
| 21 XXVI e 22 XXX | Competência da União para organizar/fiscalizar dados e legislar sobre proteção | M04/M07 | Repartição para futuro federalismo cooperativo |

**Classificação:** **PROTEÇÃO PROPOSTA, MATERIALMENTE NÃO CERTIFICADA**. As reservas de E-COM para dados digitais são motivo explícito para não pedir merge de PR59 ainda. Não existe rebaixamento formal dos direitos vigentes: nenhum dos novos textos está promulgado.

## 5. Parecer M06 (dez condições) e teste de adversário legislativo

C1 alvo de remissões; C2 ingresso domiciliar; C3 interceptação ≠ arquivo; C4 sigilo/prova ilícita; C5 bases de dados; C6 HD gratuito; C7 decisões automatizadas; C8 exclusões LGPD para segurança ≠ exceção constitucional; C9 autoridade independente; C10 não duplicação de gerais.  
**Adversário 1:** lei declara que toda "suspeita" autoriza busca domiciliar: bloqueio E-DOM, exigir razões concretas.  
**Adversário 2:** lei autoriza interceptação de qualquer pessoa para planejamento administrativo: E-COM proíbe técnica generalizada e exige finalidade constitucional precisa.  
**Adversário 3:** lei autoriza leitura integral de telefone apenas por ter sido apreendido: E-COM distingue apreensão e acesso, Tema977.  
**Adversário 4:** legislador cobra taxa para corrigir cadastro público: E-HD protege gratuidade funcional.  
**Adversário 5:** governo define dados de inteligência fora da proteção constitucional porque LGPD exclui tratamento setorial: `0031` preserva direito geral, pede especialização M12.  
**Adversário 6:** qualquer pessoa usa HD para obter prontuário sensível de terceiro: tutela fica limitada aos dados sobre o próprio titular, com proteção de terceiros.

**Portão faltante:** intercepção coletiva em massa, requisição de metadados, consentimento em abordagens coercitivas, reconhecimento facial/biometria pública, vigilância por geolocalização, criptografia e defesa de prova digital. Essas matérias não foram aprovadas e serão auditadas linha a linha em `M01-13_MATRIZ_CONCORDANCIA_ABC_v0.1.csv` e `M01-13_TESTES_CONSOLIDACAO_E.csv`.

## 6. Alternativa mais concisa para confronto (não escolhida)

Se a futura técnica redacional exigir menos parágrafos, pode-se **concentrar** E-DOM e E-COM em duas cláusulas curtas e remeter procedimentos à lei, **mas jamais omitir**: quatro situações constitucionais de entrada + ordem diurna, fundamentos prévios de flagrante, interceptação penal judicial, apreensão distinta de acesso e HD gratuito. Por isso não produzo uma “versão concisa final” sem auditoria M06/M12.

## 7. Referências primárias

1. [Constituição Federal, art5 e competências, Planalto](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm).
2. [STF Tema 280, tese de ingresso sem mandado](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=280), RE603616, 05/11/2015.
3. [STF Tema 977, tese de dados de celular e modulação](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=977), ARE1042075, 25/06/2025; conferir embargos pendentes antes de declarar estabilidade processual total.
4. [Lei9.296/1996, interceptação](https://www.planalto.gov.br/ccivil_03/leis/l9296.htm).
5. [Lei9.507/1997, habeas data](https://www.planalto.gov.br/ccivil_03/leis/l9507.htm).
6. [Lei13.709/2018 LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).
7. [Parecer M06 de pesquisa no PR62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62), dez controles.

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** minuta P integrada E-DOM/E-COM/E-HD, montagem G+A+E, N:N para garantias vigentes, seis riscos adversariais e registro de fontes; **sem CF-NOR criada/editada**, nenhuma decisão D.  
**PENDENTE:** conflito de exceção digital do Tema977, perícia e prova ilícita M12, parecer M07, urgência e ação judicial M06, acórdãos integrais e avaliação artigo por artigo, tutela coletiva e direito de terceiros.  
**PRÓXIMO:** confrontar as linhas da matriz com pareceres M06/M07/M12 e converter a minuta, **somente se aprovada como candidata H**, em fichas E com reserva atômica de ID/ordem após preflight; manter PR59 draft até demonstrar equivalência.

**Localização:** branch de PR59; CI no SHA final ainda a verificar. A main não contém esta minuta.
