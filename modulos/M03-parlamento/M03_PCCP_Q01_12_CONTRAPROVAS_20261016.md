# PCCP-Q01 — roteiro de verificação e contraprovas da primeira prototipagem P-B

**Corte:** 16/10/2026. **Natureza:** verificação jurídico-institucional condicional, sem texto CF-NOR, sem deliberação D e sem escolha de normas constitucionais. A orientação P-B foi dada expressamente pelo usuário apenas como prioridade de prototipagem. Os protótipos condicionais B-01 a B-06 continuam nos documentos do [PR #107](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/107); não os copiar como se estivessem na main.

## Parâmetros jurídicos de confronto

- [Constituição vigente atualizada](https://www2.camara.leg.br/atividade-legislativa/legislacao/constituicao1988): arts. 14, 16, 44–52, 60, 76–84, 165–169 e ADCT.
- [STF: interpretação do art. 16](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=16&abrirBase=CF) e [ADI 3.685](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=3685): verificar anterioridade eleitoral nos efeitos de eventual alteração normativa.
- [Parecer M02 já integrado](../../modulos/M02-eleicoes/M02_CC027_ADMISSIBILIDADE_BD_BI_E_PRECEDENTES_v0.1.md): eleição indireta em dupla vacância do art. 81 não prova admissibilidade automática de regra ordinária futura.
- [Funil F6](../../central/04_FUNIL_DECISOES_F6.csv): F6-02 a F6-09 permanecem sujeitos a seus próprios requisitos, independentemente da preferência P.

## Hipóteses condicionais submetidas a contraprova

| ID | Evento hipotético a verificar | Pergunta verificável / contraexemplo | Dependências |
|---|---|---|---|
| PB-T01 | Ninguém alcança o quórum na primeira investidura | Que autoridade mantém funções legais, por quanto tempo e sob que controle? | M03, M06, M14 |
| PB-T02 | Existe maioria para investir, mas não para aprovar a LOA | Que despesas já possuem autorização e quais dependem de nova lei? Confiança não substitui autorização fiscal | M03, M05, M09 |
| PB-T03 | Moção de censura não identifica sucessor válido | O gabinete continua, renuncia ou há outro rito constitucional? Quais remédios e prazos? | M03, M06 |
| PB-T04 | Primeiro-ministro é substituído durante um processo penal | Que limites separam responsabilidade parlamentar e apuração penal, sem imunidade implícita? | M03, M06, M07 |
| PB-T05 | Chefe de Estado e gabinete emitem ordens conflitantes em emergência | Qual ato tem competência legal expressa e qual controle o invalida? | M03, M06, M12 |
| PB-T06 | Chefe de Estado rejeita nomeação após investidura parlamentar válida | Há ato vinculado, prazo e via jurisdicional identificável? | M03, M06 |
| PB-T07 | Projeto rejeitado é tratado como censura implícita | Qual ato jurídico distingue rejeição de projeto, derrota de LOA e voto formal de confiança? | M03, M05 |
| PB-T08 | Hipótese de dissolução ocorre durante fiscalização parlamentar | Quais limites preservam poderes da oposição e investigação em curso? | M03, M06, M14 |
| PB-T09 | Chefe de Estado tem eleição ordinária indireta proposta | Onde estão o exame dos arts. 14 e 60 §4º, a via específica e a revisão independente? | M02, M06, M14 |
| PB-T10 | Alteração da eleição ocorre a menos de um ano do pleito | Qual regra garante a anterioridade do art. 16 e a continuidade dos mandatos? | M02, M14 |
| PB-T11 | Organização parlamentar futura redefine competências atuais | Quem examina tratados de direitos humanos, autoriza atos com terras indígenas e protege oposição? | M03, M04, M06, M11, M13 |
| PB-T12 | Não há LOA e serviço essencial enfrenta falta de caixa | Distinguir direito exigível, autorização, recurso disponível, ente responsável e tutela sem criar despesa por ficção | M01, M04, M05, M06, M09 |

**Condições de execução:** cada caso está em estado `ABERTO_R3` quanto à viabilidade de uma norma concreta. Uma descrição de caso e testes textuais não são simulação empírica, avaliação de vantagem política nem revisão jurídica humana independente. Não estabelecer quóruns, eleições, poderes presidenciais, orçamento, competências ou transição por omissão.

**Ganho documental:** definir perguntas que precisam ser respondidas para verificar eventual texto de prototipagem, reutilizando os seis protótipos existentes do PR #107 e as pendências do funil, sem redigir artigos concorrentes. **Próxima dependência:** obter variante institucional completa, analisar correspondência CF/ADCT e submeter a auditoria jurídica independente R3 antes de qualquer decisão material D.
