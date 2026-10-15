# M09.03-R7 — Catálogo ampliado de instrumentos SP/2026, protocolo replicável de consulta e direitos indisponíveis

**Corte:** 14/10/2026 · **Estado:** V (informações oficiais publicamente indexadas), P (protocolo), A (ausências), **nenhuma hipótese D**. **Base main no início:** `c28f254a76fb14c0ea4c553ebdbd07f7822ad4e8`. [PR #63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63) e [issue #76](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/76). Complementa `M09-03_AMOSTRA_REAL_MEDIADOR_SP_2026_v0.1.md`, sem substituí-la.

## 1. Escopo observado — nove instrumentos, fonte pública, seleção indexada

**Amostra intencional indexada — não probabilística, não censo e NÃO resultado de consulta exaustiva do Mediador.** Foram encontrados **nove extratos oficiais diferentes** com registro **SP.../2026** e data de registro em 2026: **oito ACTs industriais** e **uma CCT de trabalhadores domésticos**. Não há qualquer estimativa da participação de ACT/CCT no universo paulista nem prova de que apenas uma CCT doméstica tenha sido registrada. A busca limitada indexou muitos ACTs industriais e poucas CCTs domésticas — isso pode decorrer de **viés do mecanismo de busca**, do universo de entidades selecionadas e da periodicidade de convenções de dois anos, e não mede a produção geral de normas coletivas.

**Três documentos da rodada anterior, preservados:**
1. **SP002759/2026**, solicitação `MR006804/2026`, ACT **Tecnotrafo** × sindicato metalúrgico CNPJ 52.168.721/0001-09, São Paulo capital, registro 17/03/2026.
2. **SP002465/2026**, `MR009590/2026`, ACT **Teadit Brasil** × sindicato metalúrgico CNPJ 46.106.514/0001-27, Campinas, registro 09/03/2026, com **declaração textual de assembleia de 20/02/2026**, sem ata/resultado de votação conferidos.
3. **SP004864/2026**, `MR022098/2026`, CCT **Sindicato das Empregadas e Trabalhadores Domésticos da Grande SP** CNPJ 08.357.187/0001-97 × **Sindicato dos Empregadores Domésticos do Estado de SP** CNPJ 59.942.607/0001-33, registrada 26/05/2026, com municípios da Grande SP no rol, **sem São Paulo capital**.

**Seis novos extratos indexados e identificados diretamente no domínio oficial:**
4. **SP001796/2026**, `MR000292/2026`, registro **10/02/2026**, ACT sindicato metalúrgico CNPJ 46.106.514/0001-27 × **Robert Bosch Limitada** e pessoas jurídicas de previdência indicadas no extrato. **Atenção:** um ACT pode ter **mais de um CNPJ econômico participante**, não equivale a uma empresa única por registro.
5. **SP002524/2026**, `MR004080/2026`, registro **10/03/2026**, ACT sindicato metalúrgico CNPJ 46.106.514/0001-27 × **WGK Indústria Mecânica Ltda.**, abrangência **Campinas/SP**; extrato menciona compensação de feriados.
6. **SP002773/2026**, `MR009732/2026`, registro **17/03/2026**, ACT sindicato metalúrgico CNPJ 46.106.514/0001-27 × **Coppersteel Bimetálicos Ltda.**, abrangência **Campinas/SP**; instrumento declara autorização em assembleia extraordinária de **20/02/2026** (não comprova voto secreto nem quantidade).
7. **SP004069/2026**, `MR006734/2026`, registro **30/04/2026**, ACT sindicato metalúrgico CNPJ 52.168.721/0001-09 × **Usibani Indústria Metalúrgica Ltda.**; **município de abrangência não confirmado** no trecho indexado, logo não classificar como capital por inferência de sede sindical.
8. **SP004284/2026**, `MR017503/2026`, registro **11/05/2026**, ACT sindicato metalúrgico CNPJ 46.106.514/0001-27 × **Villares Metals S.A.**, abrangência **Sumaré/SP**.
9. **SP004550/2026**, `MR021508/2026`, registro **18/05/2026**, ACT sindicato metalúrgico CNPJ 46.106.514/0001-27 × **Astemo Campinas Ltda.**, **município não confirmado no trecho**; denominação empresarial não prova abrangência territorial.

Todas as nove linhas e URLs correspondentes constam do anexo `M09-03_AMOSTRA_INDEXADA_SP_2026_9_INSTRUMENTOS.csv`; as seis novas foram identificadas pela indexação de `mediador.trabalho.gov.br`, **mas a abertura direta subsequente dos extratos por ferramenta pública devolveu 403**. Isso limita a classificação de **confirmação**: os metadados acima são sustentados pelo conteúdo indexado do domínio oficial, porém **não houve nova verificação interativa integral das seis páginas**, de seu rol de cláusulas nem de eventual retificação posterior. Marcar `VERIFICACAO=INDICE_OFICIAL_NAO_ACESSO_INTEGRAL`. Os três documentos anteriores foram consultados também na rodada anterior.

## 2. Novo achado substantivo: assembleia exigida no registro ≠ auditoria de legitimidade

O [Manual oficial Mediador, versão 3.0, páginas impressas 6–7 e 33](https://www.gov.br/trabalho-e-emprego/pt-br/pdfs/manual_do_sistema_mediador_v30-1.pdf) descreve **ACT** como acordo empresa–sindicato profissional, **CCT** como negociação entre entidades profissionais e patronais e **termo aditivo** como modificação de instrumento registrado. No fluxo de cadastramento, pede **data, local e ata da assembleia deliberativa da categoria**, informações dos signatários, categoria, abrangência, texto e documento de registro; para consulta de instrumentos, recomenda **CNPJ do participante, tipo TODOS, vigência TODOS e UF de abrangência**, com resultado do sistema para o CNPJ indicado.

**Consequência prática do manual:** é possível montar **rastreio sistemático por CNPJ** e pedir ou consultar posteriormente documentos de assembleia; porém a obrigação formal de informar/entregar a ata **não cria publicamente uma base de** (i) eleitores habilitados, (ii) número de votantes, (iii) votos válidos e nulos, (iv) liberdade e sigilo do voto, (v) distinção de filiados e não filiados, (vi) representação de todo trabalhador abrangido. Não presumir que a ata completa está disponível no extrato HTML público, nem que o registro no MTE constitui auditoria material de regularidade da assembleia. **ELE-S, ELE-R e RAT-C são funções eleitorais distintas**, conforme protocolo R4.

**Exemplos observados:** ACT Teadit e ACT Coppersteel contêm **afirmação no próprio instrumento** sobre assembleia em 20/02/2026; é documento autodeclarado, não boletim independente. ACT Bosch com várias pessoas jurídicas demonstra que **um registro não equivale a um empregador nem a N trabalhadores**. ACTs com assuntos PLR ou compensação de feriados não equivalem automaticamente a acordo geral de condições salariais/territoriais. A CCT doméstica tem objeto e alcance territorial distintos.

## 3. CCT doméstica: cláusulas que exigem exame material, não só eleitoral

A CCT SP004864/2026 contém, segundo o extrato, **cláusula 64** com fórmula de prevalência do negociado sobre o legislado citando CLT art.611-A, **cláusula 65** que enuncia obrigações de órgãos públicos e **cláusula 67** que diferencia vigência de cláusulas econômicas e sociais. Essas fórmulas exigem **leitura jurídica estrita**, não aceitação automática de eficácia contra terceiros ou de renúncia a direitos absolutamente indisponíveis:

- **Tema 1046/STF e art. 7º da CF:** negociação pode dispor de direitos coletivos dentro dos limites e **não** implica renúncia universal a garantias indisponíveis. A simples invocação do art. 611-A da CLT em cláusula não autoriza prevalência indiscriminada de toda e qualquer estipulação; verificar art. 611-B, LC150/2015, hierarquia de normas e sujeitos aplicáveis.
- **Eficácia em face de órgãos públicos:** sindicatos não criam por CCT deveres orçamentários ou administrativos para órgãos que não são partes, fora das hipóteses jurídicas existentes; qualquer efeito deve ter **fundamento de competência e norma própria**, não ser presumido pela declaração contratual. **Não afirmar a invalidade global da CCT por essa ressalva**.
- **Trabalho doméstico:** LC150 art1 exige continuidade, subordinação, onerosidade, pessoalidade, ausência de finalidade lucrativa e trabalho **por mais de dois dias na semana**. Uma descrição genérica de cargos na CCT não decide sozinha o enquadramento de todas as diaristas ou prestadoras autônomas.
- **Atenção ao período:** vigência geral 2026–2028 não implica salários fixos até fevereiro/2028: o próprio instrumento distingue revisão econômica. Analisar cláusula por cláusula.

**Aplicação constitucional:** o modelo B de pluralismo representativo não pode usar votação coletiva para legitimar renúncia a direito indisponível nem impor obrigações a entes públicos sem competência. O modelo A de unicidade também não está livre desses filtros; são **critérios comuns**.

## 4. Protocolo reproduzível — separar consulta oficial sistemática da amostra indexada

### Plano P-MED-SP-2026 (ainda não executado como enumeração completa)

**Estratos fixados antes da coleta:** (a) trabalhadores metalúrgicos/indústria — dois CNPJs sindicais **46.106.514/0001-27** e **52.168.721/0001-09**; (b) trabalhadores domésticos — **08.357.187/0001-97** e patronal **59.942.607/0001-33**. **Área:** UF de registro SP, período de **01/01/2026 a 14/10/2026**. **Tipos de instrumento:** ACT, CCT e aditivos em listas separadas. **Vigência:** registrar início/fim por item, sem exigir que todo ACT ainda esteja vigente em 14/10.

**Procedimento previsto pelo manual MTE:**
1. Abrir [consulta pública do Mediador](https://mediador.trabalho.gov.br/sistemas/mediador/ConsultarInstColetivo); introduzir **CNPJ do participante**, UF **SP**, tipo **TODOS**, vigência **TODOS**, datas de registro 01/01/2026–14/10/2026, sem restringir município antes de obter universo.
2. Guardar **número total de resultados retornados por CNPJ** e cada solicitação/registro distinto; deduplicar por ID, pois um mesmo instrumento pode aparecer para ambos os participantes.
3. Para cada ID, coletar: tipo, data, vigência, partes CNPJs, município, atividade, assunto, eventuais referências a assembleia, condições e aditivos/versões, **sem nomes/CPF de participantes de assembleias**.
4. Conferir as CCTs domésticas por todos os municípios expressos, não equiparando Grande SP à capital; avaliar LC150.
5. Vincular CNES atual por CNPJ somente após confirmação, separando base legal e mandato de representante; ata como documento quando disponível **agregado**, nunca inferir voto de mera existência de ACT/CCT.
6. Registrar resultados de consulta e data de extração. **Se o acesso automatizado estiver impedido por proteção técnica 403 ou exigir interação gráfica, não fabricar o universo nem totais**; a execução integral pela interface deve ser realizada em sessão habilitada própria, mantendo este protocolo como especificação.

**Estado real neste ciclo:** etapas de desenho e identificação pontual executadas; **nenhum conjunto completo retornado por formulário/filtros foi exportado**. Foram identificados 9 documentos por indexação do próprio domínio; não houve exportação de CNES ou estatística de custos. Portanto **N_universo=NÃO_OBTIDO**, **cobertura=NÃO_OBTIDO**, **votos=NÃO_OBTIDO** e **custo incremental=INDETERMINADO**.

**Método estatístico condicional:** somente após N_universo e listagem deduplicada, definir distribuição temporal, municípios e tipos; não somar aditivos como novos trabalhadores, nem classificar cláusula com mera busca de palavras sem revisão amostral; eventual amostra aleatória exige fonte de universo de onde sorteá-la. Hoje a análise é **descritiva qualitativa da seleção indexada**.

## 5. Efeito nas escolhas institucionais A/B e custos M02/M05

- A comparação dos ACTs de empresa e CCT territorial confirma **necessidade funcional de unidades de certificação distintas**: ELE-R por estabelecimento é hipótese em parte dos ACTs, mas ELE-R por setor/território seria hipótese adequada a CCT doméstica. **Isso não prova superioridade do pluralismo B**.
- Controle formal de registro e assembleia já existe em parte; custo do B é **incremental**: criar/verificar eleitorado *abrangido*, voto secreto e eleições de representante negociador, não pagar duas vezes cadastro CNES/Mediador. O dado de custo por sindicato/membro/voto ainda **não existe neste estudo**.
- No segmento doméstico, a elegibilidade de profissionais com múltiplos domicílios e vínculos exige critério anti-duplicação e privacidade; identificação por domicílio privado não é método aceitável sem base legal.
- Se a relação de representação depende de um sindicato monopolista no modelo A, a existência do instrumento não prova democracia/participação de trabalhadores; no B, eleição formal tampouco sana ilegalidade material das cláusulas.

## 6. Fontes e limites primários

- [MTE Manual Mediador V3.0, páginas 6–7 e 33](https://www.gov.br/trabalho-e-emprego/pt-br/pdfs/manual_do_sistema_mediador_v30-1.pdf).
- [MTE Consulta oficial de instrumentos](https://mediador.trabalho.gov.br/sistemas/mediador/ConsultarInstColetivo).
- Extratos: [Teadit, MR009590/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR009590%2F2026), [domésticos Grande SP, MR022098/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR022098%2F2026), [Usibani, MR006734/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR006734%2F2026), [Bosch, MR000292/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR000292%2F2026), [WGK, MR004080/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR004080%2F2026), [Coppersteel, MR009732/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR009732%2F2026), [Villares, MR017503/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR017503%2F2026), [Astemo, MR021508/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR021508%2F2026), [Tecnotrafo, MR006804/2026](https://mediador.trabalho.gov.br/sistemas/mediador/Resumo/ResumoVisualizar?NrSolicitacao=MR006804%2F2026). **Busca indexada; leitura direta dos seis novos retornou 403**, conforme auditado.
- [STF Tema 1046](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=1046), [CF art.7º](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm), [CLT arts611-A/611-B](https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm), [LC150 art1](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp150.htm).
- **Nenhuma fonte de eleitorado real, pessoas únicas cobertas ou despesas por ELE-R foi obtida; não concluir eficácia, regularidade eleitoral ou nulidade de CCT individual pelo fato de registrada.**

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** catálogo ampliado para **9 extratos** rastreáveis em CSV (8 ACT industriais + 1 CCT doméstica), análise do Manual MTE (registro pede ata da assembleia mas não revela contagens na publicação), protocolo ex ante de CNPJ/UF/período e crítica material de cláusulas da CCT doméstica sem juízo automático de invalidade. **PENDENTE:** universo completo por filtro oficial; abrir seis extratos via acesso gráfico, CNES vivo por CNPJ, obter ata/eleições agregadas, testar LC150/CLT e custos M02/M05, não há escolha A/B nem D. **PRÓXIMO:** executar P-MED-SP-2026 por interface oficial habilitada, salvando resultados e denominadores; se N/universo indisponível, prosseguir como estudos de caso, sem propor percentuais. Submeter cláusulas domésticas e seus limites ao M06/M09. **QA:** verificar CI da branch no último commit; nenhum `CF-NOR` alterado.
