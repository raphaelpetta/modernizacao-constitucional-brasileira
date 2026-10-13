# M05.02 — Protocolo empírico: capacidade fiscal, transferências e custos municipais

**ID:** CF-M05.02-EST-001 · **Corte documental:** 13/10/2026 · **Status:** fontes oficiais identificadas; protocolo e auditor preparados; **dados municipais brutos ainda não coletados e harmonizados**, sem conclusões financeiras numéricas.  
**Issue:** [#29 — M05.02](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/29) · **Base CF lida:** `92a1af3d4ca6fd0560d1a576f48079500ca519c5` · **Base CLF lida:** `1d4fbd2ea3ba792b8c7137e9bb26b68a04b721e8`.  
**Interfaces:** M04.01, M05.01, M03, M09, M01, M06, M14; CLF T01.M04.  
**Registro verificável:** [Catálogo de dez conjuntos oficiais](M05-02_CATALOGO_FONTES.csv); [modelo de colunas normalizadas](../../modelos/M05_02_ESQUEMA_NORMALIZADO.csv); [auditor descritivo](../../scripts/m05_02_auditar_dados.py); [testes de consistência](../../tests/test_m05_02_auditar_dados.py).

## 1. Resposta da verificação de disponibilidade (não confundir com análise de valores)

Foram identificados e consultados dez documentos/serviços/datasets oficiais (catálogo) quanto à identidade, propósito, localização e, quando disponível, período de referência. **Não foi possível baixar neste ambiente os arquivos brutos CSV/XLSX dos portais nem obter uma extração municipal FINBRA completa.** O `web` possibilitou verificar páginas e o retorno JSON de metadados CKAN, não o conteúdo do CSV financeiro. A consulta interativa FINBRA requer parâmetros e pode apresentar desafio hCaptcha; os anexos XLSX do Boletim tampouco foram processados. Assim, **NÃO** existe na revisão: base brasileira de valores reais comparáveis, microbase municipal harmonizada ou estimativa `G(i,s,t)` de déficit.

| Fonte | Conclusão documental verificável | A pesquisa ainda não autoriza |
|---|---|---|
| [Tesouro — Boletim edição 2025](https://www.tesourotransparente.gov.br/publicacoes/boletim-de-financas-dos-entes-subnacionais/2025/114) | Publicado **11/02/2026**, trata principalmente de **exercício 2024** e apresenta panorama municipal agregado, capitais e CAPAG | Atribuir todas as observações ao ano de 2025 ou inventar números do anexo não lido |
| [FINBRA/SICONFI](https://siconfi.tesouro.gov.br/siconfi/pages/public/consulta_finbra/finbra_list.jsf) e [manual](https://manualsiconfi.tesouro.gov.br/area-publica/consultas/consultar-finbra/consultar-dados-finbra) | Portal oferece exercício, escopo e tabela; exporta CSV compactado para dados homologados/retificados | Pressupor 100% de transmissão/qualidade de 2025–2026 só porque o exercício aparece no seletor |
| [CKAN — transferências obrigatórias por município](https://www.tesourotransparente.gov.br/ckan/api/3/action/package_show?id=transferencias-obrigatorias-da-uniao-por-municipio) | JSON oficial retornou dataset modificado em **06/10/2026** e recursos **FPM** (id `d69ff32a-6681-4114-81f0-233bb6b17f58`) e **Fundeb** (id `18d5b0ae-8037-461e-8685-3f0d7752a287`), em CSV, com URLs oficiais | Confundir última atualização do recurso com último mês de dados efetivamente contido; somar FPM e Fundeb com receita total indiscriminadamente |
| [Tesouro — nota metodológica PAF](https://www.tesourotransparente.gov.br/temas/estados-e-municipios/boletim-de-financas-dos-entes-subnacionais-conteudos-relacionados) | **Quebra no PAF em 2024**: transferências constitucionais a municípios passaram a deduzir receita estadual, em vez de registrar despesa; mudou também cálculo do resultado primário | Comparar totais de resultados primários do PAF 2023/2024 sem harmonizar a metodologia; supor mesma quebra em todos os relatórios municipais |
| [SIOPS/FNS — arquivos](https://portalfns.saude.gov.br/siops/siops-downloads/) e [situação de entrega](https://www.gov.br/saude/pt-br/acesso-a-informacao/siops/entrega-de-dados) | Disponíveis publicamente arquivos municipais do **6º bimestre de 2018–2025** por fonte/subfunção/natureza; situação de declaração identificável | Considerar ausência de declaração como zero; misturar despesa empenhada, liquidada e paga |
| [SIOPE/FNDE](https://webservice.fnde.gov.br/siope/dadosInformadosMunicipio.do) | Consulta pública por exercício, período, UF e município | Equiparar Fundeb isolado à despesa educacional total ou presumir exportação/abrangência sem inspeção |
| [IBGE — estimativas municipais](https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html) | Tabelas com referência em **01/07/2026**, publicadas em **28/08/2026**; estimativa nacional anunciada de **214,2 milhões de habitantes** em 2026 | Dividir receita/despesa de 2024 por população de 2026 como se fosse mesmo ano e extrair inferência municipal da média nacional |

A distinção **versão do dataset × exercício de referência × data da publicação × data de acesso** é obrigatória no histórico de proveniência. Os dados do Boletim 2025 são primordialmente de 2024, e a existência de base municipal até 2025 em outro sistema não resolve, por si, compatibilidade contábil e cobertura.

## 2. Pergunta empírica e unidade de observação

**Pergunta:** capacidade própria de arrecadação e receitas recebidas são suficientes para suportar **encargos concretos** de padrões nacionais de prestação de serviços, considerando custo marginal, capacidade real, responsabilidades anteriores e desigualdade territorial?

A unidade mínima para análises gerais de capacidade é **município × ano**, identificado por código IBGE de sete dígitos e exercício financeiro, com uma linha por chave. A análise de serviço exige outra tabela **ente × serviço × exercício × padrão nacional**, com fonte legal, custo, data de obrigação e transferências **especificamente atribuíveis** ao encargo — não apenas transferências agregadas.

Antes de calcular:
- Fazer cadastro de universos de entes por ano, transições territoriais e municípios novos; distinguir população do Censo de estimativas anuais.
- Selecionar prioritariamente **2024** como exercício inicial comparável ao Boletim publicado em 2026, admitindo corte em 2025 apenas onde documentos anuais tenham sido transmitidos, conferidos e compatibilizados.
- Extrair DCA/FINBRA receita realizada, receitas tributárias, transferências correntes e despesas; manter rótulos oficiais de tabela/conta/fonte, unidade (R$ ou mil R$), estágio e método de consolidação.
- Juntar SIOPS e SIOPE somente após validar a cobertura de cada órgão, estágio de despesa, financiamento intra/intergovernamental e eventual dupla contagem com DCA.
- Para cada item registrar código de origem, tabela oficial, variável, subfunção, unidade, data extraída, status transmissão e método de transformação. Não estimar automaticamente valores por aproximação.

## 3. Pipeline reproduzível e limites

**Entrada de arquivo normalizado:** [modelo CSV](../../modelos/M05_02_ESQUEMA_NORMALIZADO.csv) — **apenas cabeçalho, nenhuma observação oficial neste commit**. Cada linha deve conter:
- `codigo_ibge`, `uf`, `municipio`, `ano`, `ano_populacao`, `populacao`;
- `receita_total_realizada`, `receita_tributaria_realizada`, `transferencias_correntes_realizadas`, `despesa_saude_paga`, `despesa_educacao_paga`;
- `fonte_contas` e `fonte_populacao` como URLs HTTPS literais.

Valores monetários em **reais correntes do exercício, separador decimal ponto e sem separador de milhar**; campos ausentes **vazios**, não zero. A entrada exige **mapeamento manual/documentado da taxonomia das fontes originais** antes da execução. Não afirmar que um CSV do Tesouro possa ser usado sem transformação; o schema de cada recurso bruto ainda precisa ser inspecionado.

**Execução local após reunir entradas documentadas:**
```bash
python scripts/m05_02_auditar_dados.py --entrada dados_municipais_normalizados.csv --saida relatorios/m05_02
python -m unittest discover -s tests -p 'test_m05_02_auditar_dados.py'
```

**Saídas:** `m05_02_indicadores_descritivos.csv` e `m05_02_qualidade.json`. O auditor:
- rejeita chaves município/ano duplicadas, UF inválida, ano inválido, inteiros populacionais inconsistentes e valores monetários negativos ou com formatação ambígua;
- registra quantitativos preenchidos/alertas; considera vazio = **sem informação**, nunca zero;
- calcula razão transferências correntes/receita total e indicadores per capita apenas com numeradores, denominadores e períodos compatíveis;
- **não gera resultado per capita** quando o ano populacional diverge do ano do dado fiscal;
- **não calcula lacuna de financiamento, causalidade ou cumprimento constitucional** a partir desses totais administrativos.

**Teste:** script experimentado localmente com entrada de **dois entes explicitamente fictícios** para verificar contagem, razão e bloqueio do denominador fora do período. Há testes unitários sintéticos reexecutáveis no GitHub Actions. Esses números **não são evidência empírica brasileira** e não são armazenados como observações oficiais.

## 4. O que significam os indicadores — e o que NÃO significam

- `transferencias_correntes_realizadas / receita_total_realizada` é **um quociente contábil descritivo**, não indicador completo de dependência econômica do município nem avaliação de autonomia fiscal. Os conceitos devem ser harmonizados e as parcelas de receita são potencialmente sobrepostas.
- `receita_tributaria_realizada / população` mede arrecadação tributária **observada**, não capacidade tributária potencial. Município de baixa arrecadação pode ser pobre, ter base tributável menor, isenções, baixa fiscalização ou combinações.
- `despesa_saude_paga / população` e `despesa_educacao_paga / população` não medem por si qualidade, necessidade, cobertura, suficiência ou custo eficiente. As responsabilidades intermunicipais/estaduais podem alterar relação entre atendimento e domicílio.
- `transferencias_correntes_realizadas` não representa necessariamente a transferência vinculada à **nova obrigação específica** exigida pelo art. 167 § 7º; FPM/Fundeb podem ser transferências estruturais e estar refletidos em outras contas.
- `receita_total_realizada` não corresponde a dinheiro de uso livre: deduzir vinculações, obrigações preexistentes, disponibilidades e eventos não recorrentes antes de alegar capacidade de financiamento incremental.

## 5. Só depois: teste de encargo concreto e equivalência de serviços

O dossiê [M05.01](M05-01_ENCARGOS_FINANCIAMENTO_EQUALIZACAO_v0.1.md) criou notação didática `B` (custo do padrão), `A` (custo anterior), `R` (receita efetivamente disponível) e `T` (transferência específica). Os seis cenários da rodada anterior são **inteiramente fictícios**. Este ciclo **não valida** essas variáveis empiricamente e **não deve preencher a lacuna G com o simples total das receitas e transferências**.

Para primeiro caso real selecionar uma obrigação legislativa federal individualizável (possíveis pilotos: piso de agentes de saúde ou piso de enfermagem), registrar norma, titular, variação do custo `B-A`, transferências efetivamente pagas e datas, implementação e exclusões/decisões do STF aplicáveis. Cruzar com população e bases contábeis do **mesmo exercício**, incluindo execução e estoques. Fazer análise de sensibilidade e eventuais intervalos, sem presumir custo unitário idêntico para todos.

Apenas depois calcular **lacuna fiscal programática** (se dados suficientes) e testar: orçamento de origem, adequação a CF 167 § 7º, ADCT 113, LRF 16–17, tutela judicial, transição e efeitos distributivos. A existência de estimativa ou lacuna aparente **não comprova violação jurídica** automaticamente; depende de titular da obrigação, competências, exigibilidade, fonte e decisões concretas.

## 6. Quebra metodológica e armadilhas de identificação

**Tesouro PAF 2024:** desde esse exercício transferências constitucionais estaduais a municípios são deduções de receita, enquanto antes figuravam como despesa; houve simultaneamente mudança de apuração do resultado primário. **Logo, evitar inferir queda de despesa estadual/ganho de equilíbrio só por mudança de classificação.** Essa nota se aplica ao PAF conforme fonte, não automaticamente a toda DCA municipal.

**Município ano único:** para comparações entre 2024 e 2025, registrar alterações territoriais/municipais; manter painéis comparáveis ou explicar mudança de universo. Para per capita, IBGE do mesmo exercício, sem misturar 2026 com 2024 silenciosamente.

**Dados declaratórios:** conferir ausência de transmissão, retificação, cadastros e datas. Não imputar ausência como zero e não generalizar a amostra de declarantes à população de municípios.

**Transferências:** distinguir previsão, obrigação legal, valor autorizado, empenho, liquidação, pagamento efetivo e crédito bancário. Em séries do Tesouro identificar se valor se refere aos municípios diretamente ou aos governos estaduais para posterior distribuição; proibir soma indiscriminada da mesma verba.

**Nível do efeito:** a contabilidade municipal **não revela causalidade** de mudanças constitucionais. Comparação causal exigirá desenho próprio, identificação exógena, medidas de confusão, contrafactual e instrumentos de verificação.

## 7. Resultados da rodada, objeções e caminho decisório

**Resultado documental positivo:** 10 fontes oficiais individualizadas, períodos, mecanismos de acesso, atualização e problemas de comparabilidade catalogados; arquivo normalizado definido; auditor e testes prontos; protocolo para transformar bases em indicadores condicionados à disponibilidade.

**Resultado não obtido e explicitamente bloqueado:** valor de receita/despesa para municípios reais, distribuição por região/porte, estimativa `G`, ranking de dependência ou conclusão sobre suficiência da regra constitucional. Não dizer que a pesquisa empírica de M05.02 foi concluída.

**Objeção central ao modelo empírico:** as rubricas gerais de contas públicas não se traduzem automaticamente em custos marginais de prestação de serviços. Resposta: começar com rastreabilidade e estatística descritiva e, em paralelo, construir piloto com legislação e transferências vinculadas identificáveis; só depois qualificar dever de compensação, equalização e tutela.

**Próximos passos em M05.02:** obter fisicamente os CSV ZIP FINBRA/DCA 2024 e 2025, arquivos SIOPS e SIOPE, recursos CKAN FPM/Fundeb, estimativas IBGE correspondentes; inspecionar cabeçalhos e códigos; transformar com dicionário auditado; rodar pipeline em cobertura documentada; selecionar serviço/piso concreto; confrontar hipóteses A–D de M05.01 com dados reais e parecer M04/M05/M09.

**Aprovação:** nenhuma alteração constitucional, fórmula fiscal, quórum territorial, CF-NOR ou proposta do CLF ratificados. Projeto de pesquisa prossegue em F1/F3, com F4/F5 condicionados a dados de efetiva execução.
