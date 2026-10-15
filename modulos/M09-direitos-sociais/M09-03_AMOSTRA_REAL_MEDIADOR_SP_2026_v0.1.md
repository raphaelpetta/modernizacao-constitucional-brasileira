# M09.03-R6 — Primeira amostra pública rastreável do Mediador: indústria × domésticos em SP (2026)

**ID:** CF-M09-S003-R6 · **Data de corte:** 14/10/2026 · **Status:** V — **amostra documental selecionada**, não amostra probabilística, não universo de registro, não validação eleitoral. **Base `main`:** `19cd7a58d4d2addbb960f7e76ecd59c3bcc958a1`. PR63 draft, [issue #76](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/76). **Novo:** foram encontrados e conferidos três extratos reais com ID MTE, tipo, registro, vigência, categoria/município e texto publicamente indexado. **Não** foram obtidos votos, colégio eleitoral, quantidade única de beneficiários, gastos administrativos ou confirmação cadastral individualizada no CNES. O portal Mediador oferece busca parametrizada, mas seus resultados dinâmicos não foram extraídos exaustivamente neste ciclo; amostra obtida por pesquisa de URLs indexadas e cotejo manual da origem oficial.

## 1. Amostra real, documental e reproduzível

| ID | Estrato | Tipo, registro e data | Partes verificadas | Perímetro publicado | Fonte |
|---|---|---|---|---|---|
| IND-SPC-01 | Indústria metalúrgica, São Paulo **capital** | **ACT SP002759/2026**, registrado **17/03/2026**, solicitação **MR006804/2026**, vigência **05/01/2026–03/01/2027** | Sindicato de trabalhadores nas indústrias metalúrgicas (CNPJ 52.168.721/0001-09) e **Tecnotrafo Ind. e Com. Importação e Exportação Ltda.** | Instrumento **de empresa**, categoria industrial metalúrgica, abrangência **São Paulo/SP** | [MTE Mediador — MR006804/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR006804%2F2026) |
| IND-CPS-02 | Indústria metalúrgica, Campinas, **controle da dimensão eleitoral** | **ACT SP002465/2026**, registrado **09/03/2026**, solicitação **MR009590/2026**, vigência **01/01–31/12/2026** | Sindicato de trabalhadores nas indústrias metalúrgicas (CNPJ 46.106.514/0001-27) e **Teadit Brasil Ltda.** | Instrumento **de empresa**, categoria metais, abrangência **Campinas/SP**; texto menciona **aprovação em assembleia extraordinária de 20/02/2026**, sem dados de votantes ou deliberação nominal | [MTE Mediador — MR009590/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR009590%2F2026) |
| DOM-GSP-01 | Trabalho doméstico, **municípios da Grande SP, não a capital** | **CCT SP004864/2026**, registrada **26/05/2026**, solicitação **MR022098/2026**, vigência **01/03/2026–29/02/2028** | **Sindicato dos Empregadores Domésticos do Estado de São Paulo** (CNPJ 59.942.607/0001-33) e **Sindicato das Empregadas e Trabalhadores Domésticos da Grande SP** (CNPJ 08.357.187/0001-97) | Convenção territorial com municípios nomeados, entre eles **Guarulhos, Osasco, Barueri, Arujá, Cotia, Suzano e Taboão da Serra**; **São Paulo capital NÃO integra o rol exibido** | [MTE Mediador — MR022098/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR022098%2F2026) |

**Alerta contra generalização:** a amostra tem **dois ACTs industriais** de entidades/empresas diferentes e **uma CCT doméstica**. Não representa "quantidade total de sindicatos", "taxa de sindicalização", "cobertura da Grande São Paulo" ou mesmo o quadro completo de uma única base. A CCT doméstica é **intermunicipal** e **exclui São Paulo capital no rol transcrito**. Os ACTs versam sobre empresas específicas. A existência de CCT com nomes de categorias **não resolve por si** eventual controvérsia legal sobre quem se enquadra como empregado doméstico, diarista ou empregador abrangido nos termos da LC150/2015.

**Sobre a declaração de assembleia no IND-CPS-02:** há **menção textual à aprovação em assembleia extraordinária dos trabalhadores da empresa em 20/02/2026**. Isso é evidência de **declaração constante do próprio instrumento**, não prova independente de lista de eleitores, abstenção, votos válidos, votação secreta, participação dos não filiados, nem ratificação individual de cada cláusula. Uma CCT assinada por sindicatos tampouco demonstra, só por isso, que cada trabalhador votou.

## 2. Filtros, viés de seleção e replicabilidade

**Recorte:** UF de registro **SP**, instrumentos **registrados em 2026** e ao menos parcialmente vigentes no ano; dois perfis intencionais: (i) indústria metalúrgica com empresa e sindicato e (ii) trabalho doméstico com entidades sindicais representativas de lados profissional/econômico. **Canal de descoberta:** busca textual pública restrita ao domínio `mediador.trabalho.gov.br`; **canal de conferência:** extratos originais publicados pelo Mediador, IDs de solicitação e de registro, datas, representantes, vigência, abrangência. A interface de busca oficial em [Consultar Instrumentos Coletivos](https://mediador.trabalho.gov.br/sistemas/mediador/ConsultarInstColetivo) dispõe de filtros de **tipo, categoria, UF, datas e abrangência**, mas a extração sistemática do conjunto completo de resultados **não foi executada**; consultas por mecanismos de indexação podem privilegiar páginas mais bem rastreadas.

**Limitação do portal:** o extrato exibido é autodeclarado pelas partes e registrado no MTE; o registro tem relevância documental e jurídica própria, mas **não equivale a auditoria substantiva de legitimidade eleitoral ou de cumprimento de direitos**. O cadastro sindical CNES possui informação de registro e representatividade formal; **não foi realizada nesta rodada conferência do status individual das três entidades pelos CNPJs no CNES**. Portanto, o CSV classifica `CNES_status_individual=NÃO_VERIFICADO`, e não `ativo`.

**Reprodução mínima:**
1. Abrir cada URL estável com parâmetro de solicitação.
2. Confirmar número registro MTE, tipo, data registro e vigência.
3. Confirmar partes e recorte de categoria/território e classificar empresa versus categoria.
4. Para aprovação em assembleia, copiar apenas a **afirmação do instrumento**, sem inferir números de voto.
5. Marcar votos, filiados da entidade, pessoas únicas cobertas e custos como `NÃO_OBTIDO`.
6. Não presumir que a CCT doméstica alcança a capital por pertencer à Região Metropolitana; respeitar cidades listadas.

**Próximo passo para amostragem real representativa:** usar a busca dinâmica em UF SP com filtros por categoria e período e exportação autorizada, arquivar universo de resultados e aplicar critérios de seleção antes de medir proporções/abrangência. Os **três** registros disponíveis aqui são primeiros casos concretos comparáveis **qualitativamente**, não estimativa de prevalência de acordos.

## 3. O que o teste institucional A/B pode — e não pode — extrair dos casos

**Indústria (IND-SPC/IND-CPS):** a unidade **empresa** existe juridicamente no ACT e torna possível imaginar ELE-R por estabelecimento/turnos e eventual RAT-C sobre instrumento específico. Não se pode deduzir número de turnos, participação de não filiados ou custos somente do ACT. Uma frase sobre assembleia pode ser ponto de partida para pedir ata/boletim agregado, mas não demonstra voto democrático na forma proposta em B.

**Domésticos (DOM-GSP):** a **CCT territorial** evidencia negociação **entre sindicatos** para múltiplas cidades; a representação de trabalhadores dispersos exigiria no modelo B uma **ELE-R setorial/territorial** e meio de votação seguro e acessível, sem controle do empregador nem exposição de residência. O instrumento não demonstra aprovação individual nem que todos os vínculos domésticos/dias de serviço estão legalmente cobertos. No modelo A, sindicatos atuais negociam com base em regras existentes; a presença no documento não prova democracia interna.

**Mudança de escala jurídica:** não comparar cobertura de ACT por um CNPJ com cobertura de CCT intermunicipal usando só o **número de registros**; um ACT pode incluir milhares de pessoas e uma CCT pode atingir outro universo. Exigir denominador de trabalhadores **únicos** juridicamente elegíveis, sem compartilhamento indevido de dados pessoais.

## 4. Lista de variáveis reais e faltantes

A nova `M09-03_AMOSTRA_REAL_MEDIADOR_SP_2026.csv` contém **três registros verificados** e campos de id/tipo/categoria/município/partes/vigência/data/source, além de `eleitores_votos`, `trabalhadores_unicos_abrangidos`, `custos_eleitorais` e `CNES_status_individual` **NÃO_OBTIDOS**. Esses dados não autorizam preços nem inferência causal.

Para M02/M05, pesquisas prioritárias: ① delimitar base jurídica pela CCT e instrumentos; ② consultar status de registro das entidades no CNES atual (não arquivos 2022) e estatutos públicos quando disponíveis; ③ verificar atas eleitorais/assembleias **agregadas e licitamente disponibilizadas**; ④ vincular despesas reais de registro/mediador a processos sem inventar custo de certificação ELE-R; ⑤ testar impacto de polos eleitorais sobre trabalhadores domésticos dispersos.

## 5. Conclusão metodológica e critérios de saída

**Constatação empírica modesta mas real:** foram encontrados instrumentos **registrados em 2026**, com estrutura diferente **ACT de empresa versus CCT intermunicipal**, e ao menos um ACT contendo **alegação de aprovação em assembleia**. Isso fornece casos de teste de representação A/B, sem qualquer prova quantitativa do direito de voto de não filiados ou da sustentabilidade de B.

**Feito:** dois setores, três extratos oficiais, datas/partes/territórios rastreáveis, CSV de evidências e não observáveis. **Pendente:** extração exaustiva, CNES atualizado por entidade, votos/atas independentes, pessoal coberto e custo fiscal; nenhuma escolha de A/B, H ou D. **Próximo:** seleção aleatória documentada após obtenção do universo oficial ou aprofundamento qualitativo com atas/boletins, além de pesquisa M05 de orçamento efetivo para funções de cadastro. **QA:** validação GitHub estrutural ainda a verificar, não certifica afirmações do instrumento/representatividade material.
