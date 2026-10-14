# M10.01-R13 — Nota de interface M11/M13: consulta, direitos originários e tratados

**Sessão:** CF-M10.01-S013 · **Corte:** 14/10/2026 · **Estado:** H/V (pesquisa e pedido de futura revisão, **não** parecer M11/M13).  
**Issue M10:** #88 · **PR M10:** #89, draft. **Main de entrada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`.  
**Referência:** [R10 F05](M10-01_R10_FICHA_F05_POVOS_CONSULTA_v0.1.md) e [R9 arquitetura A/B](M10-01_R9_MATRIZ_TEXTO_NN.csv). Os módulos M11 e M13 não possuem issue/PR próprio aberto identificado na varredura de issues/PRs de 14/10/2026. Esta nota não lhes atribui autoria ou concordância.

## 1. Baseline jurídico comprovável, sem inferir uma nova Constituição

- **CF/1988 art. 231:** direitos originários indígenas e regime territorial constitucional específico; **mera etapa administrativa de reconhecimento/demarcação não é a fonte do direito originário**. [Texto atualizado oficial da CF](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm).
- **Convenção OIT 169, art. 6º (Decreto nº 10.088/2019, Anexo LXXII):** consulta aos povos interessados mediante procedimentos apropriados e suas instituições representativas **quando houver medidas legislativas ou administrativas suscetíveis de afetá-los diretamente**; consultas de boa-fé com objetivo de acordo/consentimento. Art. 7º abrange participação em decisões sobre suas prioridades de desenvolvimento. [Texto na OIT](https://www.ilo.org/pt-pt/resource/c169-sobre-povos-indigenas-e-tribais) · [Promulgação no Brasil](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10088.htm). **Objetivo de consenso não autoriza inferir veto universal**, nem permite descartar exigência concreta de consentimento estabelecida em outras normas específicas.
- **Lei nº 15.300/2025, art. 4º, § 2º:** audiência pública obrigatória na LAE **não substitui** consulta prévia, livre e informada de povos e comunidades tradicionais quando prevista no direito aplicável. O § 1º exige EIA/Rima na LAE. [Texto oficial](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm).
- **Lei nº 15.190/2025, arts. 42–45:** manifestações institucionais de autoridades envolvidas seguem hipóteses e requisitos legalmente estabelecidos, com critérios relativos a terras/territórios; **manifestação de órgão, direito territorial e consulta de titulares são institutos distintos**. [Texto oficial](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm).
- **CF/1988 art. 5º, §§ 2º–3º:** abertura a direitos convencionais e procedimento de equivalência constitucional em hipótese específica de aprovação. **Hierarquia e incidência exata da OIT 169 não foram fixadas pelo M13 neste projeto**; classificação jurídica por instrumento e situação permanece `V`.

**Cautela adicional:** pendências quanto ao último andamento das ADIs 7913, 7916, 7919 e ADC 102 relativas à legislação de 2025 permanecem `V`: [notícia da pauta STF de 12/08/2026](https://noticias.stf.jus.br/postsnoticias/confira-a-pauta-do-stf-desta-quarta-feira-12-2/) não equivale à certidão do julgamento de mérito e seus efeitos.

## 2. Perguntas jurídicas distintas para os revisores futuros

| ID pesquisa | Responsável funcional proposto | Pergunta estrita | Evidência documental exigida |
|---|---|---|---|
| M11-Q1 | M11 | Quais sujeitos coletivos são protegidos pela CF231 e quais requisitos de titularidade são materialmente originários? | Constituição, jurisprudência pertinente com limites, regime territorial/demarcação |
| M11-Q2 | M11 | Quando a medida ambiental ou empreendimento afeta diretamente povos indígenas/tribais e qual população precisa ser consultada? | Fatos de afetação, titularidade, mapa de impactos, Convenção169 art6 |
| M11-Q3 | M11 | Como identificar instituições representativas, forma, momento prévio e boa-fé da consulta sem confundí-la com audiência ampla? | Protocolos próprios quando existirem, art6 e art7 OIT, fonte de atuação |
| M11-Q4 | M11/M06 | Qual via processual protege consulta e direito originário; que sujeitos têm legitimidade, prova e remédio? | CF5/129/231, legislação processual, ações/medidas cabíveis |
| M13-Q1 | M13 | Qual foi a aprovação/incorporação da Convenção169 e qual a tese hierárquica aplicável a ela, sem extrapolar outros tratados? | Decreto Legislativo143/2002, Decreto10088 AnexoLXXII, jurisprudência de hierarquia, CF5 §§2-3 |
| M13-Q2 | M13 | Como resolver interação entre tratados de direitos humanos e Lei15190/15300 em uma hipótese concreta de licenciamento? | Norma convencional, condição de incidência, controle e remédio, data de vigência |
| M11/M13-Q3 | M11/M13 | Existe situação de consentimento específico/vedação material distinta do dever de consultar? | Norma particular e fatos; não inferir veto de qualquer consulta |
| M07-Q1 | M07/M11 | Como separar (i) oitiva de autoridade envolvida, (ii) audiência LAE e (iii) consulta a titulares coletivos em procedimento e cronograma? | Lei15300 art4 §§1–2; Lei15190 arts42–45; exemplo de fluxo verificável |

Os nomes de módulos aqui indicam **competência temática esperada**, não designação formal de um revisor, prazo ou conclusão.

## 3. Testes de fronteira para a redação A/B

**H-01 — audiência sem consulta:** LAE com EIA/Rima e audiência realizada, mas povo diretamente afetado não foi consultado. [A-TEXTO-11](M10-01_R9_ESBOCO_A_NUCLEO_CONCENTRADO_v0.1.md)/[B-TEXTO-10](M10-01_R9_ESBOCO_B_PROTECAO_DISTRIBUIDA_v0.1.md) distinguem os institutos em termos gerais; **não** fornecem por si sujeito, timing, legitimidade e tutela suficientes para toda hipótese.

**H-02 — ausência de homologação:** procedimento de licenciamento utiliza apenas requisito de terra homologada/titulada para manifestação institucional; povo reivindica direito originário em área afetada. A diferença entre gatilho administrativo e direito material deve ser testada com CF231, a OIT169 e a legislação em vigor; **não** presumir que não haja direito material nem que toda oposição produza veto.

**H-03 — remissão à legislação:** futura cláusula apenas diz que a lei disciplinará consulta, mas o texto constitucional de povos ainda não existe. Exigir mapa `direito atual → texto candidato válido → titular/representação → dever → remédio`; **reserva documental não protege materialmente a garantia**.

**H-04 — múltiplos tratados:** não transpor automaticamente o regime hierárquico de um instrumento de direitos humanos a todo tratado climático. Exigir parecer individualizado M13 por forma de incorporação, conteúdo e operação normativa.

## 4. Situação de coordenação e resultado desta nota

**Confirmado:** fontes gerais atuais e distinções de procedimento; a pesquisa de M01/PR22 identifica M11/M13 como interfaces, não responde especificamente a esta ficha F05.  
**Não confirmado:** parecer M11/M13, hierarquia exata e efeitos da consulta em cada caso, status atualizado das ADIs/ADC, equivalência funcional dos esboços A/B.  
**Próximo ato intermodular:** referenciar esta nota na issue M10 #88 como **handoff sem canal especializado**, sem publicar comentário fictício em M11/M13 ou iniciar subciclo sem pré-verificação de governança. Na próxima atividade, pesquisar se apareceu issue/PR próprio; se não, submeter à coordenação a abertura de estudo M11/M13 **sem duplicar M10 F05**.

**Status das questões R10 F05:** H/A/V; **nenhuma deliberação F6 nem texto F7**, sem alteração CLF.
