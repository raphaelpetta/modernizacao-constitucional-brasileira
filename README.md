# Modernização constitucional brasileira

Projeto independente de **pesquisa, auditoria crítica, desenho institucional e redação de uma Constituição brasileira modernizada**, com liberdade de preservar, modificar, suprimir ou substituir qualquer solução normativa do anteprojeto preliminar. O objetivo não é reformatar a CF/1988 nem reproduzir automaticamente o anteprojeto v0.1.

> **Estado:** pacote de implantação v0.1 — 13/10/2026. Este repositório é documentação de pesquisa e propostas, **não** texto constitucional vigente, projeto aprovado ou registro de decisões ainda não ratificadas.

## Começar aqui

1. [Guia de implantação](docs/00_LEIA_PRIMEIRO.md) e [estado do projeto](governanca/04_ESTADO_ATUAL.md).
2. [Manifesto](governanca/01_MANIFESTO.md), [metodologia](governanca/02_METODOLOGIA.md) e [registro de decisões](governanca/03_DECISOES.md).
3. [Catálogo funcional de módulos](catalogo/MODULOS.csv), [dependências](governanca/05_DEPENDENCIAS.md) e [protocolo de continuidade](governanca/06_CONTINUIDADE_VERSIONAMENTO.md).
4. [Guia de interface com o CLF](integracao/01_INTERFACE_CLF.md) e [avaliação do PR #2 do CLF](integracao/02_AVALIACAO_PR2_CLF.md).
5. [Instruções para Projeto ChatGPT](chatgpt/INSTRUCOES_PROJETO.md) e [modelos de dossiê](modelos/DOSSIE_MODULO.md), [problema](modelos/FICHA_PROBLEMA.md), [decisão](modelos/DECISAO.md) e [handoff](modelos/PACOTE_CONTINUIDADE.md).

## Duas autonomias, uma interface

O [Código da Legislação Federal](https://github.com/raphaelpetta/codigo-legislacao-federal) (CLF) e a modernização constitucional mantêm **governança, versões, premissas e textos normativos independentes**. Integram-se por solicitações identificadas e documentos de interface. A CF/1988 vigente é parâmetro para o direito positivo; a Constituição proposta constitui cenário hipotético de reforma, nunca direito vigente.

## Estrutura

```text
governanca/   manifesto, metodologia, decisões, estado e continuidade
catalogo/     módulos funcionais e classificação das questões
modulos/      dossiês de pesquisa (criados sob demanda)
modelos/      fichas, decisões e pacotes de continuidade
integracao/   vínculo metodológico com o CLF e revisão de mudanças
redacao/      minutas de texto constitucional, não presumidas aprovadas
referencias/  anteprojeto e guia-mestre legados, com proveniência
chatgpt/      instruções de operação com vários chats
scripts/      validações documentais
```

O código dos módulos **não** determina a divisão em títulos, capítulos ou artigos do futuro texto. A numeração do anteprojeto v0.1 é exclusivamente uma referência histórica.

## Regra fundamental

**Chat é ambiente de trabalho, Git é a fonte de estado.** Discussão não equivale a decisão. Proposta não equivale a texto aprovado. Cada sessão deve fixar a versão do repositório que leu, documentar conclusões e conflitos e encerrar com pacote de continuidade. Somente decisões validadas são registradas como tais; versões conflitantes não são mescladas silenciosamente.
## Controle documental

A verificação estrutural pode ser executada localmente com `python scripts/validar_repositorio.py` e é acionada pelo GitHub Actions em PRs e na `main`. Ela confere presença dos arquivos, IDs e dependências do catálogo, além de links Markdown locais. **Não** certifica validade jurídica, integridade de precedentes ou deliberações.

## Priorização transversal por ganho marginal

A [política CF-GOV-019 de ganho marginal e rotação justificada](governanca/19_POLITICA_GANHO_MARGINAL_GLOBAL.md) aplica-se a todas as frentes M00–M14, pesquisas F0–F8, texto experimental e integração. **Comparar a próxima rodada com alternativas**, privilegiando ganho material em direitos, cobertura e capacidade decisória, não volume de documentos. Duas rodadas sucessivas no mesmo núcleo ativam reavaliação da carteira; terceira rodada exige motivação específica, sem dispensar rigor em direitos sensíveis. Todo handoff registra ganho esperado/realizado e custo de oportunidade; H/D permanecem distintos.

## Coordenação permanente e resultado de cada rodada

O projeto opera com o [protocolo transversal de ciclos](governanca/12_PROTOCOLO_RODADAS_E_SINCRONIZACAO.md), um [quadro de frentes, entregas, pendências e próximas tarefas](governanca/13_QUADRO_DE_COORDENACAO.md), o [registro de marcos e handoffs](governanca/14_REGISTRO_DAS_RODADAS.md) e o [controle de identificadores](governanca/15_REGISTRO_RESERVAS_IDS.md).

**Toda rodada substantiva deve encerrar com `FEITO / PENDENTE / PRÓXIMO`, registrar estado Git e dependências e salvar um pacote de continuidade.** Antes de reservar `CF-NOR` ou iniciar subciclo Mxx.yy, conferir também PRs e issues abertos. Quadro e contagens são fotografias datadas; verificar sempre `main` ao começar e antes de integrar. Nenhum resultado de pesquisa ou CI equivale a ratificação de conteúdo constitucional.

## Central operacional e integração seletiva (CF-CC-019)

A [central de comando da CF](central/00_CENTRAL_DE_COMANDO.md) e a [política de integração sem ratificação tácita](central/01_POLITICA_INTEGRACAO_E_CONCORRENCIA.md) complementam a [regra global de ganho marginal](governanca/19_POLITICA_GANHO_MARGINAL_GLOBAL.md). O [plano atualizado do grafo de PRs](central/02_PLANO_INTEGRACAO_PRS.md) e o [diagnóstico da CI e da integridade das 54 propostas experimentais](governanca/20_DIAGNOSTICO_CI_E_INTEGRIDADE_STACK_CF_CC_019.md) distinguem **integração documental de governança** de **integração de hipóteses normativas**. O catálogo de cobertura do PR #101 foi **reconciliado seletivamente na CF-CC-020**, distinguindo a `main` e a pilha do PR #124; scripts, painéis e demais artefatos operacionais dos PRs #101/#104 permanecem em revisão. CF-DEC-014/015 são decisões apenas operacionais.

**Acesso ao produto:** [leia a minuta experimental e seus estados](produto/00_LEIA_A_MINUTA.md) e consulte o [mapa M00–M14 de 20 H integradas versus 54 H na pilha](catalogo/COBERTURA_FUNCIONAL.csv). **As contagens não medem completude, maturidade jurídica ou ratificação.**

## Consolidação, auditoria e fechamento

A [política operacional de consolidação e fechamento](governanca/POLITICA_CONSOLIDACAO_E_FECHAMENTO_20261015.md) prioriza o ganho marginal entre novas propostas, auditoria jurídica, eliminação de bloqueios de integração e encaminhamento de decisões maduras. Enquanto perdurar a dívida da pilha de PRs e o incidente [CI #120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120), o fechamento deve disputar prioridade real com novas CF-NOR. A fonte de conteúdo H e os estados D/P/H/A/V são preservados; **nenhuma integração implica ratificação constitucional**.

**Decisões constitucionais pendentes:** consulte o [funil F6 de prioridades e dependências](central/04_PAUTA_EXECUTIVA_F6_20261015.md). A pauta existente no PR #99 admite eventual escolha expressa de **foco de trabalho P**, sem definir regime de governo ou ratificar artigos.
