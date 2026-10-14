# M01.12.02 — Fiscalização de internações e indicadores territoriais da RAPS

**ID:** CF-M01.12.02-F1F5-001 · **Corte:** 14/10/2026 · **Status:** pesquisa documental, indicadores projetados, verificação empírica **parcial**; **sem F6 ratificada, sem CF-NOR criada**.  
**Base de entrada CF:** `5ac08b622d7552b7d3b37a695a3027b4b9d827d4`; [issue #49 — M01.12](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/49); [dossiê anterior M01.12.01](M01-12_COERCAO_EM_SAUDE_RAPS_ALTERNATIVAS_v0.1.md).  
**Fontes novas e seus limites:** [15 origens institucionais](M01-12_02_CATALOGO_BASES_E_CONTROLES.csv); [14 indicadores com denominadores](M01-12_02_DICIONARIO_INDICADORES.csv); [amostra restrita de cinco serviços CAPS de portaria federal de 2025](M01-12_02_AMOSTRA_PORTARIA_CAPS_2025.csv).  
**Preflight:** main, PRs #22/#59/#62/#63 draft, reservas M01.12 #49, M01.13 #57 e M01.14 #54 consultados. Não repetir colisão já resolvida nem editar cláusulas CF-NOR H.

## 1. Resposta documentada: existe dado sobre internação involuntária?

**Sim, há registros administrativos identificados em Ministérios Públicos estaduais**, mas **não se obteve nesta rodada uma série pública nacional de internações involuntárias com cobertura validada**. Não confundir número registrado de comunicações, número de internações reais, número de pessoas, número de leitos, judicializações e qualidade das decisões.

| Fonte institucional | O que se verificou oficialmente | O que NÃO foi obtido |
|---|---|---|
| [MPMG — SIAPI](https://www.mpmg.mp.br/portal/menu/areas-de-atuacao/cidadania/saude/siapi.shtml), atual. 26/06/2026 | Comunicações/altas monitoradas, sistema acessível a membros do MP; hospitais possuem acesso autorizado. A [notícia técnica do MPMG](https://www.mpmg.mp.br/portal/menu/comunicacao/noticias/mpmg-publica-resolucao-sobre-o-sistema-de-comunicacao-de-internacoes-psiquiatricas-involuntarias.shtml) informa alertas de prazo e capacidade de relatórios | Microdados, registros anonimizados e totais por ente/ano, universo de hospitais obrigados a informar e percentual de completude |
| [MPRJ — MSM 2.0](https://www.mprj.mp.br/web/guest/visualizar?noticiaId=215101), 16/03/2026 | Painéis BI sobre cumprimento dos prazos de comunicação, duração, estabelecimentos e território de origem, com acesso de órgãos do MP | Base exportada, números, métodos, cobertura e resultados concretos das fiscalizações; painel interno não presumido público |
| [MPSP — formulário institucional](https://sis.mpsp.mp.br/internacaoinvoluntaria/InternacaoInvoluntaria/Comunicacao/Alta) | Interface de comunicação e alta foi identificada no portal; possui campos individuais e clínicos sensíveis | Não comprovado acesso a painel agregado público, nem proporção de preenchimento; acesso dinâmico pode ter limitações |
| [SIH/SUS](https://datasus.saude.gov.br/acesso-a-informacao/producao-hospitalar-sih-sus/) | Consulta de produção hospitalar, com dados por local de internação/residência, gestor e AIH, desde 2008 em algumas séries | **Não há comprovação de variável confiável para consentimento ou natureza involuntária em toda AIH.** Não gerar “taxa de internação involuntária” simplesmente filtrando psiquiatria/urgência |

Os registros ministeriais permitem perguntar se os prazos e decisões são fiscalizados. **Não demonstram que o número de notificações corresponde a toda internação:** comunicações ausentes ou tardias são precisamente possível objeto de fiscalização e geram **viés de subcobertura**. Para identificação de pessoas deve prevalecer restrição/acesso institucional; análise pública apenas agregada e com proteção de grupos pequenos.

## 2. Territorialização: oferta e financiamento ≠ acesso efetivo

- [RAPS no Portal de Dados Abertos do SUS](https://dadosabertos.saude.gov.br/dataset/mgdi-rede-de-atencao-psicossocial-raps): conjunto mostra **42 recursos** sobre modalidades de CAPS, SRT, unidades de acolhimento e leitos, com recursos atualizados em maio de 2026. **Contar recursos do portal não é contar serviços nem municípios.** Não descarregar/combinar rubricas sem inspecionar cabeçalhos, competência e repetição de tipos.
- [CNES, dados de estabelecimentos](https://dadosabertos.saude.gov.br/dataset/cnes-cadastro-nacional-de-estabelecimentos-de-saude): atualizado em 13/10/2026 segundo portal, contém registros de estabelecimentos, mas cadastro não prova atendimento clínico, equipe presente, ocupação ou serviço de crise acessível.
- [CNES, habilitações](https://cnes2.datasus.gov.br/Mod_Ind_Habilitacoes.asp?VTipo=H): complementar série por estabelecimento e competência, especialmente mudanças de habilitação que afetam comparação.
- [SISMAC — detalhado](https://sismac.saude.gov.br/teto_financeiro_detalhado), [SISMAC — por assunto](https://sismac.saude.gov.br/teto_financeiro_por_assunto): teto MAC, incentivos e portarias por ente/gestão; **não é prova automática de pagamento efetivo, despesa executada, suficiência de repasse ou custo integral**.
- [FINBRA/SICONFI](https://siconfi.tesouro.gov.br/siconfi/pages/public/consulta_finbra/finbra_list.jsf), [SIOPS/FNS](https://portalfns.saude.gov.br/siops/siops-downloads/) e [IBGE](https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html) são complementares, como já mapeado no [M05.02](../M05-financas/M05-02_PROTOCOLO_EMPIRICO_E_AUDITORIA_v0.1.md), com cautela de exercício financeiro e população coerentes.

**Exemplo factual restrito:** a [Portaria GM/MS nº 7.126/2025](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2025/prt7126_17_06_2025.html) autoriza incorporação de custeio MAC em **cinco CAPS** descritos no anexo, com efeitos desde a 6ª parcela de 2025. Somam R$ **331.468 mensais de valores normativos**, anualizados em **R$ 3.977.616** (RJ R$ 42.994; SP R$ 288.474 mensais). A [amostra CSV](M01-12_02_AMOSTRA_PORTARIA_CAPS_2025.csv) preserva município, serviço, CNES e valores do ato. **Não** é o total nacional de recursos CAPS, nem prova que todo valor anual foi efetivamente transferido em 2025: anualização de doze meses difere do impacto de parcelas iniciadas no meio do exercício.

**Nota de códigos:** a Portaria usa códigos de município IBGE no formato de **seis dígitos**; converter para o código de sete dígitos somente usando mapeamento IBGE verificado. Não completar dígito por dedução aritmética ou preencher ano/população sem fonte.

## 3. Matriz de indicadores e regras de não confusão

O [dicionário com 14 indicadores](M01-12_02_DICIONARIO_INDICADORES.csv) separa:
1. **Notificações e fiscalização**: contagem, proporção comunicada depois de 72 horas, duração mediana/quartis, registros de alta, estabelecimentos notificadores, defensor/assistência e revisão independente;
2. **Taxas por população**: notificações por 100 mil habitantes residentes, mas com distinção entre **origem**, **local do estabelecimento** e cobertura dos sistemas notificadores;
3. **Oferta e execução**: CAPS e leitos habilitados por habitantes, CAPS efetivamente funcionando, valores **autorizados** por portaria, recursos **pagos** e necessidade de cuidado; denominadores da mesma competência;
4. **Direitos e continuidade**: evidência documentada de recursos extra-hospitalares, revisão da internação e alta assistida, sem confundir um campo preenchido com efetiva proteção.

**Regras de qualidade:** NA quando numerador/denominador indisponível, zero somente quando registro confiável assim o demonstrar; distinguir eventos de pessoas; intervalos e censura de internações ainda em curso; períodos de registro e competência clínica; desduplicar eventos entre serviços; tratar variação na obrigatoriedade, adesão e implantação de sistemas estaduais; evitar subamostras que revelem dados de saúde de indivíduos. Não inferir causalidade ou ilegalidade individual de um indicador.

## 4. Jurisprudência nova localizada e sua pertinência exata

### STJ, REsp 2.228.271/ES — publicação 22/12/2025
[Pesquisa no STJ](https://scon.stj.jus.br/SCON/pesquisar.jsp?b=ACOR&fr=veja&i=1&livre=REsp%202228271) e [inteiro teor disponibilizado](https://scon.stj.jus.br/SCON/GetInteiroTeorDoAcordao?num_registro=202503017889). Ementa localizada da ministra Maria Thereza de Assis Moura: em conflito negativo de competência, a ação de internação compulsória não deve ser excluída do Juizado Especial da Fazenda Pública **simplesmente por alegação genérica de complexidade**; a competência absoluta do juizado exige olhar para valor da causa e limites legais, com retorno à origem para definição pertinente.

**Limite decisório:** julgado **processual**, NÃO tese material de que internações compulsórias sempre sejam permitidas, necessárias, eficazes ou constitucionais. A inferência de dever de revisão periódica do paciente não foi demonstrada por este precedente. Não o confundir com decisões do STJ mais antigas (HC 135.271 etc.) sobre circunstâncias específicas.

### CNJ, Resolução 487/2023, alterada por 572/2024
[Texto normativo compilado](https://atos.cnj.jus.br/atos/detalhar/4960): instituiu política antimanicomial **no âmbito do processo penal e da execução de medidas de segurança**, dirigida a pessoas sob incidência do sistema penal e providências judiciais relacionadas. **Não** estabelecer que o mesmo ato cria rito geral de internação civil por iniciativa médica/familiar. Interessa à interface M06/M12/M09 e à proteção de desinstitucionalização, sem substituir Lei 10.216/2001.

### STF, processo de controle da política antimanicomial
[Andamento no portal do STF](https://portal.stf.jus.br/processos/detalhe.asp?incidente=6740815) contém propostas de tese e pedido de vista em 2025. **Sem conferência conclusiva de resultado final e publicação de acórdão em 14/10/2026** nesta rodada; não invocar voto ou proposta de tese como decisão final vinculante.

### Inspeção MPF/MPT
[Notícia de 13/11/2025](https://www.mpf.mp.br/o-mpf/unidades/pr-pfdc/noticias/relatorio-nacional-aponta-graves-violacoes-de-direitos-humanos-em-comunidades-terapeuticas): inspeções em 2024 apontaram ilegalidades em estabelecimentos inspecionados, como internações involuntárias, isolamento e contenções. **Não** extrair prevalência nacional nem frequência de infrações: relatório completo e amostragem não examinados.

## 5. Duas conclusões institucionais que alteram a prioridade da pesquisa

**Primeira: fluxo de proteção não equivale a controle independente.** Comunicação em 72h é importante e mensurável, mas não prova que a pessoa foi ouvida, obteve assistência jurídica, teve acesso a remédio rápido ou revisão periódica. Os dados de MPMG/MPRJ permitem formular indicadores adequados; ainda é necessário solicitar informações agregadas sobre revisões concretas.

**Segunda: a pesquisa não depende apenas de criar um direito novo.** O texto experimental `CF-NOR-0020` já exige controle de legalidade, motivação, assistência e impugnação sem instituir permissão de coerção. Uma nova CF-NOR neste momento pode ser redundante e ocultar questões de efetividade e implementação. A prioridade de M01.12.03 deve ser **provar a lacuna de garantias e avaliar execução real**, em interlocução com M06/M09/M05, não promulgar nova cláusula.

## 6. Roteiro de obtenção de agregados — pedido institucional a formular, NÃO enviado

Solicitar separadamente às unidades responsáveis por SIAPI (MPMG), MSM 2.0 (MPRJ) e sistema do MPSP:

> Informar, para os anos 2023, 2024 e 2025, preferencialmente por UF, município do estabelecimento (código IBGE) e trimestre ou ano, o número de comunicações de internação involuntária recebidas; internações e altas vinculadas; proporção comunicada após 72h; duração agregada (mediana, quartis e quantidade de casos ainda em curso); número de estabelecimentos comunicantes e universo estimado dos sujeitos à obrigação; quantitativos de comunicações que motivaram apuração, providência corretiva ou revisão; e metadados de cobertura, duplicações e implantação do sistema. Informar também se há campos relativos a acesso à defesa/Defensoria, impugnação, revisão independente, avaliação periódica e disponibilidade documentada de alternativas comunitárias, distinguindo campo existente de campo preenchido e de ocorrência comprovada. **Fornecer somente dados agregados e anonimização adequada, suprimindo células pequenas e identificadores pessoais ou de saúde individual; indicar hipóteses de indisponibilidade e dicionário de dados.**

Pedir **separadamente** fontes reais de operação/ocupação e custeio por serviço à SAES/MS e gestões estaduais/municipais, com competência, CNES, valor autorizado vs valor efetivamente transferido/recebido vs gasto e atendimento. **Nenhuma solicitação administrativa foi enviada nesta rodada.** As atribuições de acesso, sigilo e recorte territorial deverão respeitar LGPD, sigilo médico e transparência pública.

## 7. Quatro arquiteturas constitucionais — o que os dados ainda não respondem

As alternativas **A** (aperfeiçoamento legal/execução), **B** (garantias constitucionais sem autorização material), **C** (vedação de coerção com transição) e **D** (permissão excepcional estrita) mantêm objeções e dependências do [dossiê M01.12.01](M01-12_COERCAO_EM_SAUDE_RAPS_ALTERNATIVAS_v0.1.md). A identificação dos sistemas estaduais de fiscalização é **evidência de capacidade de registro**, não evidência de cumprimento, eficácia da coerção ou suficiência financeira para qualquer das quatro opções.

**Pendente decisivo:** cobertura de comunicações, fiscalização real, dados de internações involuntárias e desfechos, acessibilidade de serviços, gastos efetivos, consulta às pessoas afetadas, jurisprudência de mérito atual e impacto das alternativas sobre proteção e abandono.

## 8. FEITO / PENDENTE / PRÓXIMO

**FEITO:** preflight da main e PRs; 15 fontes oficiais/institucionais com status individual, dicionário de 14 indicadores com denominadores e vieses, cinco registros oficiais de custeio de CAPS de 2025 (somando R$ 331.468 por mês autorizados e R$ 3.977.616 anualizados), parecer de pertinência STJ 2.228.271/ES e CNJ 487, roteiro de LAI agregado com confidencialidade. Não houve acesso aos dados nominais, nem coleta de valor nacional de internações.

**PENDENTE:** microdados/agregados oficiais sob acesso institucional; séries de SIH e RAPS brutas não baixadas; pedido de informação ainda não enviado; dados de custos reais e execução; controle de qualidade e amostra da inspeção 2024; jurisprudência substantiva recente e parecer M06/M09/M05; ninguém foi consultado como representante das pessoas afetadas.

**PRÓXIMO:** M01.12.03, **na mesma issue #49**: obter agregados de SIAPI/MSM 2.0/MPSP por meio institucional/LAI; baixar e auditar CSV RAPS por competência; validar denominadores IBGE, estabelecer cobertura e rodar indicadores de fiscalização e acesso territorial; obter análise M06 sobre legitimidade e revisão. Se não houver dados, registrar a inexistência de resposta e simular apenas cenários explicitamente fictícios, sem conclusão causal.

**Decisão:** zero novas CF-NOR; 20 hipóteses H da main de entrada inalteradas. Nenhuma alternativa constitucional ratificada.
