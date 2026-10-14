# M09.03 × M02/M05 — Fonte pública, auditabilidade de votos e custo de certificação sindical

**ID:** CF-M09-S003-R5 · **Corte:** 14/10/2026 · **Status:** V/P/A (mapeamento de evidência e protocolo operacional), **sem norma CF-NOR, sem escolha institucional D e sem estimativa fiscal inventada**.  
**Base de pesquisa:** main CF `b9dbdc540310ed5dc34fb1e5f314c46af343dc98`; [PR #63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63), [issue M09.03 #68](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/68) e [issue interface M02/M05 #76](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/76). Complementa `M09-03_PROTOCOLO_ELEITORAL_CUSTEIO_IND_DOM_R4_v0.1.md`. A fonte oficial `M05-02_PROTOCOLO_EMPIRICO_E_AUDITORIA_v0.1.md` foi consultada para distinguir custos e fontes, **não** para presumir levantamento fiscal sindical executado.

## 1. Resultado central da pesquisa de fontes

A fiscalização de representação do modelo **B — pluralismo com certificação eleitoral** exige dados que os sistemas existentes **não fornecem diretamente**. A **base administrativa** pode dizer qual entidade a administração registra, sua categoria/território e dirigentes; o **instrumento coletivo** pode demonstrar acordo publicado. Nenhum desses objetos revela necessariamente quantos trabalhadores distintos foram abrangidos, votaram livremente, aprovaram o texto ou se opuseram à contribuição. Não é metodologicamente válido somar o número de instrumentos e inferir cobertura nem dividir o orçamento total do MTE por sindicatos para estimar custo de eleição não existente.

**CNES, página oficial atualizada 01/04/2026:** registro sindical, enquadramento, categoria e base; documentação de situação e dirigentes. O MTE afirma que o sistema atual relaciona solicitações e cadastro. **Limitação:** dados de registro não são resultado certificado de ELE-S, ELE-R ou RAT-C.

**Painel de Relações do Trabalho, documentação técnica atualizada em 12/06/2026:** integra CNES e Mediador e facilita análises de entidades sindicais, mediações e instrumentos. A integração permite estudar o **lado organizacional e documental** por setor e período, não confirmar votos/abrangidos. Antes de reproduzir qualquer soma, definir filtros de instrumento (ACT/CCT/aditivo), vigência, município/UF, categoria, duplicados e versões.

**MTE, listagem pública de arquivos de entidades sindicais domésticas:** planilhas `Entidades_Sindicais_Trabalhadores_e_Empregadores_Domesticos - BRASIL.xlsx` e `Entidades Sindicais - Trabalhadores e Empregadores -Domésticos (08-12-2022).xlsx` estão no portal. Apesar da atualização da **página em maio/2026**, os arquivos publicados trazem carimbo de **08/12/2022** e **não podem ser tratados como cadastro corrente 2026**. **Os conteúdos das planilhas não foram abertos/extraídos nesta rodada**; não alegar número de entidades ou filiados a partir de sua existência.

**RAIS/CAGED identificados:** MTE informa procedimento de solicitação conforme LGPD/LAI, com **Acordo de Cooperação Técnica ou Acordo de Cooperação**, finalidade lícita e dever de sigilo. Atualização do serviço em **17/06/2026**, com referência à **Portaria Consolidada MTE 1/2025, arts. 49–61**. **Sem ACT/AC não se obtiveram microdados identificados**, e não se deve reconstruir dados identificáveis cruzando registros públicos para explorar filiação sindical. Priorizar agregados estatísticos públicos.

**IBGE PNAD Contínua 2025 (divulgada em setembro/2026):** filiação nacional 8,8%, Indústria Geral 11,4%, atividade Serviços Domésticos 2,5%, posição trabalhador doméstico 2,8%. São denominadores distintos dos eleitores/abrangidos; a menor filiação doméstica justifica mais atenção a acessibilidade, **não** prova ausência de representatividade ou superioridade causal de B.

## 2. Dicionário de observabilidade por eixo ELE-S / ELE-R / RAT-C

| Informação | Fonte institucional plausível | Estado em 14/10/2026 | Por que não equivale a voto |
|---|---|---|---|
| Entidades e base reconhecida | MTE CNES | Página e estrutura pública verificadas, **sem amostra atual extraída** | Cadastro de organização, não universo eleitoral |
| Instrumentos coletivos | MTE Mediador/Painel | Portal e integração documentados, sem extração setorial | Um instrumento pode cobrir muitas pessoas e ter aditivos |
| Filiação por grupo econômico | IBGE PNAD2025 | Observada em 2025, grupo estatístico amplo | Associação não é participação em ELE-R |
| Número de trabalhadores formais por ramo/território | RAIS agregada, métodos IBGE | Fonte possível, **não tabulada** | Trabalhadores informais/domésticos podem ficar fora |
| Eleitores habilitados à escolha do negociador | Registros de eleição auditada legalmente | **Não observado** | Nem CNES nem Mediador contém automaticamente a lista eleitoral |
| Votos válidos/nulos e abstenção | Boletim independente do pleito | **Não observado** | Sem boletim não medir apoio |
| Ratificação de texto específico | Ata/votação RAT-C autenticada | **Não observado** | Eleição de direção é evento diferente |
| Custeio de entidade/negociação | Contas auditadas, balanços e receitas lícitas | **Não obtido** | CNES não é contabilidade sindical |
| Custo público de cadastro/fiscalização | SIAFI/Portal Transparência + órgão responsável | Fonte a selecionar por rubrica, **sem valor atribuído** | Orçamento agregado não estima serviço novo |
| Custo marginal de certificação ELE-R | Contratos/tempo de equipe/tecnologia e testes | **Não existente para modelo hipotético B** | Requer cenários reais de custo e premissas abertas |

**Atenção à causalidade:** preço por voto, custo por trabalhador coberto e ganho salarial precisam de base, método, controle territorial/ramo, período e unidade de análise. Não computar valores apenas com taxas PNAD ou planilhas estáticas de 2022.

## 3. Dois pilotos implementáveis em desenho de pesquisa (não execução administrativa)

### IND-01 — Indústria: estabelecer um universo eleitoral verificável

**Entrada necessária:** recorte setorial e territorial documentado; instrumento coletivo atual no Mediador; entidade(s) registradas por base no CNES; empregadores/estabelecimentos e vínculos **em forma de contagem agregada lícita**, com turnos/afastados/terceirizados e regras de elegibilidade. **Não** escolher empresa específica sem base ou autorização.

**Três estimandos diferentes:**
- `associacao_IBGE = associados_sindicatos_no_grupo / ocupados_no_grupo` (11,4% em 2025 para todo grupo Indústria Geral);
- `participacao_ELE_R = votantes_unicos_elegiveis / eleitores_unicos_elegiveis` (**não observado**);
- `cobertura = trabalhadores_unicos_abrangidos_por_ACT_CCT / trabalhadores_unicos_elegiveis` (**não observado**).

**Procedimento de amostra futuro:** delimitar um setor/território ou estabelecimento; usar CNES/Mediador apenas para mapear atores/instrumentos; obter boletins ELE-S se publicamente disponíveis e consentidos, **não imputar** que uma eleição interna de membros representa não filiados; observar meios de voto por turno, cadeia de auditoria e ratificação de acordo quando existir; custos em rubricas reais.

### DOM-01 — Trabalho doméstico: evitar extrapolação de base documental de 2022

**Entrada necessária:** entidades da base atual e suas datas de mandato/território, eventual instrumento negociado, definições de empregados domésticos segundo LC150/2015 versus diaristas/outros vínculos, universo de pessoas **por atividade** e de pessoas **por posição** (IBGE: 2,5% versus 2,8% de associação sindical em 2025), meios de acesso sem revelar residências.

**Procedimento futuro:** validar cadastro **corrente** CNES; usar arquivo histórico 2022 apenas como linha de base de evolução institucional; examinar critérios de representatividade patronal/doméstica e aplicação legal de ACT/CCT; testar postos neutros e votação assistida, custos de transporte/apoio, integridade da lista e opção de voto sem internet. **Não** transformar domicílios privados em locais de fiscalização eleitoral ou publicar endereço de trabalhador.

**Objeção de maior peso:** se B exigir verificação individual complexa de todo trabalhador doméstico por empregador, poderá violar privacidade, custar desproporcionalmente e excluir exatamente a base que pretendia proteger. A escolha de **representação territorial/setorial sem monopólio** é hipótese institucional P, não opção D.

## 4. Contabilidade de custos a requisitar para M05 — sem fabricar valores

| Tipo | Itens | Evidência mínima e unidade |
|---|---|---|
| `CP_registro` | horas de analista, TI, manutenção, protocolo, atendimento, recursos | custo anual por órgão/programa e atribuição causal a registro |
| `CP_certificacao` | organização ELE-R, listas, tecnologia sigilosa, apuração, impugnação | horas/custo por pleito e por pessoa *elegível*, não filiado PNAD |
| `CP_justica` | ação/urgência de impugnação, Defensoria e perícia | dados CNJ/órgão, natureza da demanda, custo incremental |
| `CS_direcao` | eleição interna ELE-S, auditoria privada e prestação de contas | demonstrações sindicato, periodização anual |
| `CS_negociacao` | equipe, consulta, mediação, RAT-C e publicação | custo por instrumento e número de abrangidos validados |
| `CE_empregador` | horário de voto, informação agregada, proteção antirretaliação | não remunerar controle do voto pelos empregadores |
| `CT_transicao` | nova certificação, formação de bases, migração de registros, continuidade de acordos | horizonte definido e custos não recorrentes |
| `CD_territorial` | polos de votação domésticos, deslocamento, proteção/apoio sem internet | custo por microrregião/eleitorado elegível, com anonimização |

**Modelo de custos:** `C_sistema(B)-C_sistema(A)` deve ser estimado como **diferença incremental** entre funções novas e antigas (evita cobrar duas vezes CNES existente), para uma unidade territorial e período definidos. **Sem orçamento atribuível a uma autoridade de certificação hipotética**, o campo deve permanecer `INDETERMINADO`. Variar participação, dispersão, custo de identificação e risco de repetição de pleito; não usar 8,8% ou 2,5% como participação eleitoral.

## 5. Trilha operacional de coleta lícita — prioridade, não pedido já enviado

**Etapa 1 — disponível publicamente:** usar as páginas CNES/Mediador/Painel, definir filtros de data/UF/categoria/tipo/vigência e executar amostra reprodutível **sem dados privados**; registrar link estável, data, resultado, denominador e versão.
**Etapa 2 — transparência administrativa:** para M05, buscar relatórios/orçamento efetivo de manutenção do registro e mediação, número de processos por equipe, contratos de TIC e dados de pessoal **de forma agregada**, sem assumir que são custos de ELE-R. Se necessário formular pedido de LAI **não enviado aqui**.
**Etapa 3 — agregados eleitorais:** obter atas/boletins voluntariamente publicados ou dados agregados por órgão competente e estudos acadêmicos, sob licitude, **não** acesso a nome, CPF, filiação, voto, endereço.
**Etapa 4 — acesso identificado só por acordo:** se estatística não puder ser feita por agregados, qualquer uso de RAIS/CAGED **identificados** exige procedimento ACT/AC próprio e conformidade à LGPD/MTE, sem trabalho fora do escopo/autoridade da pesquisa.
**Etapa 5 — estimativa/sensibilidade:** somente após observar custos e unidades de escala, produzir faixas e cenários A/B com premissas declaradas, sem preferir B por liberdade formal sem medir exclusão do trabalhador disperso.

**O primeiro insumo concreto de M02/M05** é o protocolo `M09-03_MATRIZ_OBSERVABILIDADE_E_CUSTOS.csv`. Ele distingue disponibilidade e data **publicadas** de variáveis ainda **não observadas**, e tipos de autorização de acesso. **Nenhum dado de filiação individual foi processado**.

## 6. Fontes primárias rastreáveis

- [MTE CNES — informações gerais (atualização 01/04/2026)](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/sindicatos/cadastro-de-entidades/cadastro-de-entidades-sindicais/informacoes-gerais-sobre-o-cadastro-nacional-de-entidades-sindicais).
- [MTE Painel — documentação de integração CNES/Mediador (atualização 12/06/2026)](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/onmt/acervo2/copy_of_publicacoes/atualizacao-e-inclusao-de-informacoes-no-painel-de-informacoes-sobre-relacoes-do-trabalho).
- [MTE listagem de planilhas históricas de entidades domésticas, arquivos datados 08/12/2022](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/sindicatos/cadastro-de-entidades/entidade-sindical-registrada/arquivos).
- [MTE requerimento de acesso a RAIS/CAGED identificados (atualização 17/06/2026)](https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/acoes-e-programas/programas-projetos-acoes-obras-e-atividades/estatisticas-trabalho/solicitar-bases-de-dados-identificados).
- [MTE Plano de Dados Abertos 2025–2027](https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/dados-abertos/dados-abertos).
- [IBGE PNAD2025, publicado setembro/2026](https://agenciagov.ebc.com.br/noticias/202609/cresce-o-numero-de-meis-com-cnpj-e-protecao-previdenciaria-mostra-pesquisa-do-ibge).
- [LC150/2015 domésticos](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp150.htm).

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** auditoria de quatro famílias de fontes oficiais 2022–2026, separação de eleição, filiação, instrumento e cobertura, mapeamento de 8 classes de custo e trilha lícita para IND/DOM. **Não foram baixadas planilhas 2022 nem acessados microdados individuais.**
**PENDENTE:** extrações setoriais reais no painel, números de votos de entidades e cobertura, custos administrativos atribuíveis, protocolos M02/M05 e estudo de impacto/regime doméstico, nenhum modelo A/B ratificado.
**PRÓXIMO:** executar **amostra pública delimitada por uma UF e duas atividades** no CNES/Mediador (com corte e filtros), consultar despesas MTE atribuíveis e construir estimativas apenas se houver custo e eleitorado verificáveis. O status anterior `INDETERMINADO` persiste para custos ELE-R e direitos de não filiados. **Documento de pesquisa no PR63 draft**, sem CF-NOR e sem D.
