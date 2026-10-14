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

## Coordenação permanente e resultado de cada rodada

O projeto opera com o [protocolo transversal de ciclos](governanca/12_PROTOCOLO_RODADAS_E_SINCRONIZACAO.md), um [quadro de frentes, entregas, pendências e próximas tarefas](governanca/13_QUADRO_DE_COORDENACAO.md), o [registro de marcos e handoffs](governanca/14_REGISTRO_DAS_RODADAS.md) e o [controle de identificadores](governanca/15_REGISTRO_RESERVAS_IDS.md).

**Toda rodada substantiva deve encerrar com `FEITO / PENDENTE / PRÓXIMO`, registrar estado Git e dependências e salvar um pacote de continuidade.** Antes de reservar `CF-NOR` ou iniciar subciclo Mxx.yy, conferir também PRs e issues abertos. Quadro e contagens são fotografias datadas; verificar sempre `main` ao começar e antes de integrar. Nenhum resultado de pesquisa ou CI equivale a ratificação de conteúdo constitucional.
