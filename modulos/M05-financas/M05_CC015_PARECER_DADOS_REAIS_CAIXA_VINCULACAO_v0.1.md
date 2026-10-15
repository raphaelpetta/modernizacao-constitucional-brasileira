# CF-CC-015 — M05: teste fiscal real e correção do modelo de caixa da CF-NOR-0048

**Estado:** evidência primária E/estudo F1/F4/F5, hipótese constitucional **H/A/V**, sem escolha F6/D. **Corte:** 15/10/2026. **Base do PR anterior:** [#118](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/118) `fcd230c18a20bfd74764034ae4cf3388c6c6cf45`; main `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Objetivo:** sair de cenários completamente fictícios de caixa para um caso oficial verdadeiro, SEM criar inferências de falta de pagamento ou viabilidade de orçamento provisório.

## 1. Evidência oficial — granularidade e proveniência

**Documento:** STN/SIAFI, *Relatório de Gestão Fiscal do Poder Executivo Federal — 1º quadrimestre de 2025*, **Anexo 5 retificado do exercício 2024** (janeiro a dezembro), página 14 impressa (página PDF 14, índice 13). URL do documento oficial: [RGF 1Q2025, PDF](https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/52223_1645804/01_%20RGF1Q2025.pdf). A informação é o **estoque contábil de 31/12/2024**, não observação do exercício de 2025, não dado de 2026, nem série mensal; tabela publicada em retificação de 2025. Fonte interna declarada STN/CCONT/GEINF/SIAFI.

**Arquivo reprodutível:** [M05_CC015_RGF2024_CAIXA_OBSERVADA.csv](M05_CC015_RGF2024_CAIXA_OBSERVADA.csv); sete linhas com números exatos em reais, colunas bruta (a), líquida antes de inscrição em RP não processados (f), RP não processados do exercício (g), líquida depois (h=f−g); agrupamentos rotulados para **impedir dupla contagem**. Totais I/II, subgrupos do II e total III NÃO devem ser somados entre si.

| Destinação (31/12/2024) | Caixa bruta (R$) | Líquida após RP não processados (R$) |
|---|---:|---:|
| Recursos não vinculados/ordinários (I) | 202.791.184.246 | 44.980.772.540 |
| Recursos vinculados (II) | 1.545.203.247.956 | 1.371.440.118.889 |
| Educação, subgrupo II | 37.999.587.565 | 34.593.985.108 |
| Seguridade social exceto previdência, subgrupo II | 113.355.303.799 | 70.651.350.119 |
| Previdência Social — RGPS, subgrupo II | 7.830.620.917 | **−3.135.928.718** |
| Transferências a entes subnacionais, subgrupo II | 39.399.433.489 | 11.221.188.301 |
| Total consolidado III | 1.747.994.432.201 | 1.416.420.891.428 |

**Prova aritmética:** em todos os sete registros `|f−g−h| <= R$1` de diferença de apresentação/transcrição; em I/II e RGPS a igualdade é exata; o total III possui variação de **R$1** na apresentação. Registrar tolerância expressa, não corrigir número oficial nem atribuir motivo causal não demonstrado.

**Nota de leitura obrigatória:** a nota 1 do Anexo 5 declara: *eventuais recursos vinculados com insuficiência de caixa são compensados pelos recursos ordinários*. Essa nota comprova a metodologia de apresentação/compensação informada no documento — **não** licença geral para redirecionamento de receita legalmente vinculada. A conta de RGPS ser negativa **não significa**, por si, default, inadimplemento, déficit previdenciário atuarial, inviabilidade de benefícios, nem falta de liquidez em todas as contas. O estoque líquido total ser positivo **não significa** que recursos vinculados de outra destinação estão livremente disponíveis.

## 2. Limites jurídicos da cobertura financeira

- **LRF, art. 8º, parágrafo único:** receita legalmente vinculada permanece destinada exclusivamente ao objeto legal mesmo em outro exercício. Cobertura por **recursos ordinários juridicamente disponíveis** pode ser cogitada, não equivalente a movimentar fonte vinculada de outra finalidade. [Lei complementar 101/2000](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm).
- **LRF, art. 50, I–IV:** escrituração identifica disponibilidade vinculada individualmente, distingue competência/caixa e segregação previdenciária. O futuro dispositivo deve exigir quadro financeiro por fonte/grupo e **compromissos** que expliquem a diferença entre saldo bruto e líquido.
- **LRF, art. 42:** restrição à assunção de obrigações nos **últimos dois quadrimestres de mandato**, não proibição uniforme de todo empenho sempre que uma subconta aparecer negativa. [LRF](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm).
- **LRF, art. 41, inserido pela LC 212/2025:** norma prevê a partir de **1º/01/2027** vedações quando persistir insuficiência em restos a pagar e obrigações; não está em vigor temporal para o dado de 2024 ou em 15/10/2026. É referência futura para teste de sanções e continuidade; não aplicar retroativamente.
- **LDO:** execução provisória de orçamento depende de disciplina do exercício e não equivale a uma autorização genérica constitucional de apropriar saldo disponível. A CF-NOR-0048 H é **projeto novo de título constitucional**, não reprodução de competência atual.

## 3. Confronto constitucional — por que mudar a H

**Versão CF-CC-014:** mandava demonstrar insuficiência por fonte e obrigação e proibia desvio de recursos vinculados, mas não distinguia claramente a **cobertura ordinária legítima** da alteração indevida da destinação. Também permitia ler saldo contábil negativo como insuficiência residual, sem confronto de todos os compromissos e possibilidades legalmente autorizadas.

**Mudança CF-CC-015 (somente § financeiro):** obrigar transparência de bruto, compromissos exigíveis, RP, líquido, fontes juridicamente aplicáveis e cobertura ordinária permitida; só falar em insuficiência **residual** após esse teste; vedar o uso do impasse para novo endividamento por inferência. Os demais parágrafos da H permanecem experimentais.

**Melhor objeção à mudança:** detalhar variáveis de demonstrativo contábil na Constituição pode engessar alterações metodológicas do MDF/MCASP. **Resposta provisória:** enunciado material genérico, sem codificar fórmulas específicas ou siglas oficiais, e desenvolvimento por lei de finanças; se o detalhe for excessivo, migrar a exigência de metodologia a norma infraconstitucional. A denominação “caixa líquido” deve ser regulamentada compatível com padrões contábeis dinâmicos.

## 4. Teste adversarial de inferências proibidas

1. Saldo RGPS −R$3,136 bi isolado: **não** prova falta de recursos totais, não prova inadimplência.
2. Saldo ordinário +R$44,981 bi: **não** se presume que toda essa quantia está livre de compromissos posteriores ou disponível para qualquer decisão.
3. Saldo bruto total +R$1,748 tri: não representa margem para novos programas, crédito ou PEC fiscal.
4. Soma de subgrupos com total: dupla contagem proibida.
5. Positividade do total III e negatividade do RGPS: coexistem legitimamente em demonstrativo; examinar cobertura legal e nota 1.
6. RGF 2024 publicado em 2025: não sustenta previsão de caixa de 2026.
7. Nota de compensação do Anexo 5: é metodologia, não revoga LRF art.8º/50.
8. RP não processados: `f−g` pode divergir de disponibilidade imediatamente mobilizável em datas futuras; atualizar posição.
9. Crise de LOA no primeiro mês: RGF de dezembro anterior é **insumo, não orçamento**.
10. LC212/2025 art41: marco de efeitos 01/01/2027; evitar retroatividade.
11. Pagamento de serviço essencial e saldo negativo: eventual tutela de direitos não cria automaticamente fonte financeira.
12. Executivo invoca caixa do regime previdenciário de vinculação diversa: vedação sem título legítimo e verificação constitucional.

## 5. FEITO / PENDENTE / PRÓXIMO / RESPONSÁVEIS

**FEITO:** sete números efetivamente transcritos de RGF oficial com recorte, natureza, ressalvas e aritmética, confronto da LRF com H-0048 e do limite do dado agregado. **PENDENTE:** (i) extração 2025 de estados/municípios por fonte específica, (ii) custos efetivos de serviços e calendário de caixa para simular o impasse, (iii) parecer M03/M04/M05/M06/M09/M14 sobre mecanismo constitucional provisório, (iv) validação CI e semântica. **PRÓXIMO:** obter caso municipal/auditado de RGF 2025/2026, confrontar orçamento de serviços e restos a pagar com mesma base temporal e fonte; não concluir causalidade do RGF federal isolado. **INTERFACES:** CF central #103, M05 #25, M03 #84; PR #118 e estudo M05.02; CLF não alterado.

**Status do ciclo:** pesquisa + norma H revisada; nenhum D/F6, nenhuma aprovação A/B/C, nenhum merge.