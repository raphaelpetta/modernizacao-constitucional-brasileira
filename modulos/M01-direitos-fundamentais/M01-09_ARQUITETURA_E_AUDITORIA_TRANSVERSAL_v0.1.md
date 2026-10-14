# M01.09 — Consolidação transversal do catálogo e auditoria do piloto constitucional

**ID:** CF-M01-S009 · **Data de corte:** 13/10/2026 · **Estado:** PESQUISA F0–F5, revisão interdisciplinar preliminar e testes F8; **sem ratificação F6**.  
**Main de entrada verificada:** `35703d9fec8a30579faa0d8dad079e149923f8bf`; [PR #22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22) aberto em **draft**, sem fusão.  
**Protocolo editorial novo da main:** `governanca/11_TECNICA_DE_REDACAO_E_INTEGRACAO.md` (M00.03), `redacao/indice.csv`, cinco fichas `CF-NOR-0003…0007`, status **H**. A vista `redacao/anteprojeto-de-trabalho.md` é derivada, nunca editada manualmente.  
**Antecedentes na branch:** M01.01–M01.08 e matrizes de 38 conjuntos gerais, 16 direitos do piloto (main) e 18 pontos digitais (PR22); nenhum documento é inventário exaustivo de todas as garantias e suas interações.

## 1. Questão de pesquisa e resultado metodológico (F0)

Como compor uma **estrutura constitucional única** a partir do rol de 1988, da jurisprudência e dos oito subciclos do M01, distinguindo:
(a) cláusulas verdadeiramente gerais;
(b) direitos substantivos autônomos;
(c) especializações materiais ou de titularidade;
(d) garantias institucionais, processuais e financeiras;
(e) regras de restrição, exceção, emergência e transição?

A alternativa “substituir tudo por aplicação imediata + proporcionalidade + ação judicial” **falha** em manter direitos, titulares, obrigações, reservas de lei, mecanismos de execução, recursos e prioridades financeiras que hoje têm função própria. **A opção oposta — copiar integralmente 1988 em sequência — também falha** em sanar redundâncias, conflitos, lacunas tecnológicas, inflação de minúcias e baixa inteligibilidade. A solução estrutural depende de **normas gerais com especializações funcionalmente justificadas, sem correspondência artificial 1:1 entre CF/1988 e anteprojeto**.

## 2. Resultado do inventário transversal e limite de leitura (F1/F4)

Arquivo: `M01-09_MATRIZ_TRANSVERSAL_GARANTIAS.csv`, **96 registros de *conjuntos* de garantias**, derivados da CF atualizada, normas com equivalência constitucional e temas jurisprudenciais de relevância transversal. Isto **NÃO** significa 96 direitos distintos, 96 artigos propostos nem verificação de todo inciso/subinciso/disposição transitória.

| Cobertura pela minuta CF-NOR-0003–0007 | Quantidade de conjuntos | Significado correto |
|---|---:|---|
| `COBERTURA_GERAL_PARCIAL` | 4 | Texto geral aborda parcela da função, sem equivalência integral certificada |
| `PARCIAL` | 7 | Referência geral indireta; deveres, titularidades ou conteúdo próprios ainda pendentes |
| `AUSENTE_ESPECIAL` | 14 | Garantia específica não aparece no piloto, ainda que regra geral possa orientar interpretação |
| `NAO_EQUIVALENTE` | 71 | A função concreta não é substituída pela cláusula geral indicada; pode precisar de norma especial, capítulo setorial ou disciplina intermodular |

**Todos os 96 registros são uma triagem documental; equivalência MATERIAL a CF/1988 = NÃO DEMONSTRADA em TODOS.** Não somar os 71 como “direitos suprimidos”: **o piloto é incompleto por definição** e não é uma Constituição aprovada ou vigente. Os códigos indicam lacunas perante o *piloto* atual; a nova proposta só seria regressiva se finalizada com omissão ou substituição insuficiente.

As 96 linhas abrangem:
- art. 5º caput/I–LXXIX e §§, em agrupamentos funcionais, incluindo titularidade, legalidade, liberdades, propriedade, penal, processo, prisões, remédios e dados;
- arts. 6º–11: direitos sociais e proteção trabalhista/sindical;
- arts. 12–17: nacionalidade, representação e processo democrático;
- garantias de igualdade e instituições de tutela fora do título (arts. 37, 41, 127–129, 134);
- ordem econômica, urbana, agrária e social, seguridade, saúde, previdência, assistência, educação, cultura, mídia, ambiente, família, infância, idosos e povos;
- regras do ADCT a auditar e CDPD equiparada à Constituição; compromissos internacionais e jurisprudência identificada.

**Próxima exigência:** separar blocos agregados por inciso/alínea/parágrafo (particularmente art. 7º, financiamento, ADCT) e verificar jurisprudência/responsáveis/efetividade/ônus fiscal individualmente antes de atestar equivalência. Fonte-base: CF/1988 atualizada até EC 139/2026, edição Câmara. A tabela é rastreio de risco e **não catálogo jurídico fechado**.

## 3. Anatomia do piloto F7 já existente na main

| Ficha H | Função legítima já rascunhada | Fronteira material identificada |
|---|---|---|
| `CF-NOR-0003` | titularidade das pessoas humanas, jurídicas e coletividades | não garante direitos territoriais originários, conteúdo de igualdade, requisitos próprios de nacionalidade e capacidade de ação |
| `CF-NOR-0004` | aplicabilidade imediata e deveres positivos dos poderes públicos | não incorpora prestações de saúde, aposentadorias, jornada, escola, financiamento, proteção do ambiente |
| `CF-NOR-0005` | incidência calibrada frente a particulares | não estabelece por si direitos trabalhistas, remuneração, proteção do consumidor ou requisitos de transparência de plataformas |
| `CF-NOR-0006` | requisitos gerais de proporcionalidade com ressalva da reserva e proibições absolutas | **não autoriza** nem reconstrói hipóteses específicas de busca, prisão, extraditar, censura e restrições penais; art. 5º II/XXXIX e demais reservas permanecem como funções distintas |
| `CF-NOR-0007` | tutela judicial efetiva e tempestiva | não substitui devido processo, devido processo administrativo, presunção de inocência, assistência integral gratuita, habeas corpus, habeas data, mandado de segurança, mandado de injunção nem ação popular sem avaliação concreta |

**Advertência à integração:** A inclusão de um dispositivo `H` no anteprojeto integrado **não** é decisão `D`. As fichas da `main` foram lidas integralmente, inclusive reservas, objeções e matriz `M01-07_MATRIZ_DE_CONTINUIDADE.csv`, de 16 conjuntos. A branch do PR22 foi iniciada antes da pilotagem editorial, razão para **não** alterar `redacao/` dentro dela sem ressincronização com a main.

## 4. Arquitetura por funções em quatro camadas (F5; nenhuma ratificada)

### Camada I — regime geral: uma única localização lógica para regra comum

Os cinco enunciados atuais são **ponto de partida**, não fechamento. Investigar a necessidade de:
- **abertura material do catálogo, tratados e hierarquia** (`CF art. 5º §§2º–3º`, M00/M13; garantir cláusula que não feche direitos);
- igualdade de proteção e não discriminação (direito material, não derivado de mera titularidade);
- validade de restrições legais e regulamentares mediante competências e reservas específicas;
- deveres privados e responsabilização regulatória com critérios de natureza e função;
- garantias processuais e institucionais gerais sem anular especiais.

**Risco:** se todo direito for posto em uma única cláusula geral, os remédios e deveres especiais desaparecem. Se cada capítulo repetir integralmente o regime geral, podem emergir divergências de termos que geram interpretações contraditórias.

### Camada II — direitos substantivos nucleares, próprios do catálogo

Propor agrupamentos funcionais provisórios, **não título/capítulo fixo**:
1. **Vida, integridade, liberdade pessoal e autonomia existencial:** preservar proibição de tortura, escravidão, proteção sob custódia, consentimento e garantias contra coerção; BIO05–BIO09 em aberto.
2. **Igualdade e não discriminação:** lista aberta de fundamentos e discriminação direta/indireta; adaptação razoável da CDPD já constitucionalmente protegida; ações afirmativas sob controle proporcional, sem impor percentuais legislativos.
3. **Privacidade, domicílio, comunicações e dados:** direitos distintos, reservas especiais de intervenção, fiscalização e remédios; art. 5º LXXIX não substituível apenas por direito à intimidade.
4. **Liberdades de consciência, religião, pensamento, informação, ciência, arte, reunião, associação e circulação:** bloco ainda subpesquisado no M01, alta prioridade para o próximo ciclo; incluir objeção de consciência e sigilo de fontes.
5. **Liberdade econômica e propriedade, inclusive sua função social:** direitos e restrições com impacto M08; não presumir que propriedade não exige previsão por ter dimensão infraconstitucional.

A localização constitucional de direitos sociais **pode** ser em capítulo geral ou matéria específica, sem prejuízo de proteção direta. A preocupação é **efeito jurídico**, não topografia.

### Camada III — garantias específicas e dispositivos institucionais setoriais

- **M02 eleições:** sufrágio, direitos políticos, pluralismo, partidos, anualidade eleitoral e garantias materiais contra captura da maioria;
- **M06 Justiça:** garantias penais e processuais, remédios constitucionais, Judiciário, acesso à defesa, tutela coletiva e execução;
- **M05/M09:** trabalho, sindicatos, seguridade, saúde, educação, assistência, cultura, moradia, direitos sociais, financiamento e coordenação de competências;
- **M10 ambiente:** prevenção, participação, responsabilidades e proteção intergeracional, não simples intenção de política ambiental;
- **M11 povos:** direitos territoriais originários, cultura, autogoverno/consulta, legitimidade própria;
- **M07 administração:** transparência, dados, controles, acesso a informações, autorizações e boa administração;
- **M08 economia e propriedade:** liberdade econômica, proteção de consumidores, função social, inovação;
- **M12 segurança:** privação de liberdade, reserva de polícia, legislação penal estrita e proibições de sanções;
- **M13 tratados e direitos internacionais:** hierarquia, abertura, controle de convencionalidade;
- **M14 transição e proteção contra supressão/revisão:** regras de emergência, reformas, continuidade de direitos adquiridos e medidas transitórias.

**Requisito de integração:** uma garantia pode aparecer como regra autônoma no núcleo M01 **ou** no capítulo M06/M09/M11, desde que seu conteúdo esteja protegido com acesso a remédio e interfaces legíveis. Não duplicar normas por duplicar matérias.

### Camada IV — operação: remédios, exceções, custeio e transição

Cada direito exigível deve responder: titular, sujeito responsável, obrigação imediata/progressiva, fonte de competências e recursos, tutela e defesa, limite e reserva, fiscalização, efeitos temporais. Garantias institucionais não ficam protegidas se sua implementação é transferida sem critérios a decreto ou lei ordinária.

## 5. Confrontação histórico-comparada (F2–F3)

**Brasil e 1988:** histórico de constitucionalização extensa de direitos civis, sociais, laborais, políticos, de povos e de garantia financeira. Objetivo de recomposição do catálogo não é mera edição textual. Proteções sociais e garantias de processo e de liberdade podem exigir densidade elevada para serem efetivas em cenário de captura, crise ou baixa capacidade administrativa.

**Alemanha e Portugal:** reforço transversal de aplicabilidade, conteúdo essencial, competência e restrições, mas com direitos específicos. Alemanha organiza matérias materiais de liberdades e proteção de justiça em artigos; Portugal também tem regime geral de direitos, liberdades e garantias e regimes específicos. **Não** usar índices estrangeiros como esquema pronto do Brasil.

**África do Sul:** §7–9,36,38 oferecem deveres estatais, eficácia privada funcional, igualdade e tutela coletiva; §§26–29 distinguem prestações sociais com obrigações progressivas e condições. **Não** converter progressividade em imunidade orçamentária à jurisdição ou generalizá-la a proibições imediatas.

**Internacional:** CADH/PIDESC/CDPD e jurisprudência de cortes internacionais fornecem deveres, proteção de grupos, igualdade e garantias de emergência. **CDPD equivale a norma constitucional no Brasil;** não pode desaparecer sob uma expressão geral de dignidade. O regime doméstico dos demais tratados demanda M00/M13.

**STF Tema 698, RE 684.612 (2023):** tutela judicial de direitos fundamentais em caso de ausência ou deficiência grave de serviço não viola por si separação de poderes; como regra, decisão orientada a fins com plano administrativo. Isso é **ilustração funcional** de tutela do direito social sem confundir diretriz judicial com prestação substitutiva. Não extrapolar a toda ação ou extinguir tutela urgente.

**Problema de desenho judicial:** mesmo um catálogo excelente pode falhar se dependente somente de litigância individual cara ou geograficamente desigual; as garantias coletivas, administrativas, de legitimidade e fiscalização precisam funcionar em contextos reais, e não apenas no texto.

## 6. Alternativas de estrutura, com objeções

| Opção | Formulação | Melhor benefício | Melhor objeção |
|---|---|---|---|
| A — concentração integral | colocar todas as garantias num capítulo extenso de direitos | localização simples e facilidade editorial | sistema de saúde, fundos e organização setorial dissociados do direito; duplicação de deveres institucionais |
| B — regime geral + direitos materiais nucleares + especiais setoriais integradas | catálogo claro com normas comuns e remissões mínimas justificadas por efeito jurídico | menor repetição sem tornar garantias abstratas | dispersão exige índice funcional e obriga controle permanente de N:N |
| C — direitos distribuídos por matéria, sem regime comum robusto | direitos nos setores da Constituição, sem bloco inicial forte | vincula direito a executor e financiamento | desigualdade de tutela; cláusulas especiais inconsistentes e ausência de padrão comum |

**Hipótese P para aprofundamento:** B, **não aprovada pelo usuário**. Critério de comparação: número de remissões estritamente necessárias, direitos sem regra material, vulnerabilidade de minoria, vulnerabilidade orçamentária, duplicação inútil, conflito de competências, eficiência de tutela e compreensão cidadã.

## 7. Fichas de decisão que NÃO podem ser consideradas concluídas

- **CF-M01-09-Q01:** capítulos/ligações funcionais: local único de garantia ou distribuição por matéria? Proposta B apenas de pesquisa.
- **CF-M01-09-Q02:** como constitucionalizar expressamente liberdade de expressão, religião, reunião, associação e privacidade, hoje ausentes do piloto? Dividir em normas materiais autônomas.
- **CF-M01-09-Q03:** separar rigorosamente `CF-NOR-0006` de reservas especiais para domicílio, telecomunicações, prisão, restrição penal e emergência.
- **CF-M01-09-Q04:** preservar tutela material e remédios específicos sem repetir indiscriminadamente a cláusula `CF-NOR-0007`. Eventual substituição de `habeas corpus` por outro remédio requer equivalência demonstrada, não presumida.
- **CF-M01-09-Q05:** onde ficam direitos trabalhistas, fundos educacionais, SUS, povos, ambiente e garantias coletivas? Precisam de texto material e mecanismos suficientes, no M01 ou setor.
- **CF-M01-09-Q06:** abertura material e tratados, peso especial da CDPD e direitos de cidadãos estrangeiros, com M00/M13.
- **CF-M01-09-Q07:** como uma CF-NOR de direito digital pode gerar defesa contra discriminação algorítmica sem usurpar atribuições legais/M07 e sem repetir a cláusula geral?
- **CF-M01-09-Q08:** instrumentos de medição institucional e teste de efetividade, inclusive efeitos distributivos e captura de instituições.
- **CF-M01-09-Q09:** preservação de direitos em reformas, ADCT, transições de sistema e possíveis inconsistências de legislação herdada.

Nenhuma dessas questões é decisão `D`, não há autorizações para retirar dispositivos constitucionais existentes nem equivalências reconhecidas.

## 8. Testes adversariais prioritários

Matriz: `M01-09_TESTES_INTEGRACAO.csv`, com 20 cenas que reproduzem riscos próprios de integrações normativas:
- governo restringe protesto citando cláusula genérica sem reserva legal; dissidente perde remédio específico por “tutela geral”;
- ministro usa decreto para interceptação digital; dados cadastrais substituem cadastro protetivo pela inteligência;
- dissidente é detido sem juiz natural; direito à defesa fica oculto em regra geral;
- orçamento educacional mantém direito abstrato mas extingue garantia de financiamento sem alternativa equivalente;
- entidade privada presta serviço público sem dever de igualdade;
- transição constitucional considera ADCT sempre esgotado;
- pessoa jurídica tenta se apropriar de direito à integridade corporal de cidadão;
- financiamento descentralizado transfere ônus a município sem fonte;
- sindicato perde garantia de representação;
- direito originário de povos é reduzido a personalidade jurídica civil;
- código penal apaga proibição absoluta sob argumento de proporcionalidade;
- regra de proteção de dados retira transparência democrática ou direitos de fonte;
- reforma do acesso à justiça retira gratuidade concreta;
- nova constituição reconhece assistência social mas não BPC e deveres correlatos, entre outros.

Cada teste tem um **critério mínimo verificável** e identifica responsável e fonte de proteção existente. Resultado atual = desenho ainda não aprovado; nenhum cenário considerado “resolvido” por regra abstrata.

## 9. Portas de qualidade para redação de direitos específicos

1. O grupo faz parte de direito material, regra de competência, procedimento, instituição, finança ou transição? **Não** fundir categorias heterogêneas por aparência editorial.
2. O `CF-NOR` geral atual já produz essa consequência jurídica? Se não, especial autônoma (`A`) ou especialização (`E`) justificada.
3. Mapeamento N:N de cada direito da CF vigente e jurisprudência, **incluindo direitos fora do art. 5º** e tratados qualificados; documentar mais de um destinatário.
4. Apontar a **melhor objeção** e alternativa legislativa/administrativa menos rígida. Às vezes a falha é implementação, não ausência de norma constitucional.
5. Obrigações estatais e privadas, reserva de lei e controle judicial, colaboração federativa e financiamento previstos onde cabível.
6. Testar governante hostil, baixa capacidade, crise fiscal, administração capturada, maioria eleitoral abusiva e sistema judicial lento.
7. Se houver substituição ou supressão real, justificar e **deliberar expressamente**, não declarar equivalência por similaridade verbal.
8. Apenas no fluxo M00.03 gerar `redacao/propostas/CF-NOR-####.md` em status `H`, atualizar índice e **regenerar** a vista com `scripts/gerar_anteprojeto.py`, `--check` e verificador. Não editar o anteprojeto de trabalho diretamente nem replicá-lo em dossiês.

## 10. Próximas etapas com prioridade funcional

**P0, alta prioridade:** direitos substantivos do M01 **ainda não trabalhados autonomamente**: expressão, consciência/religião, reunião, associação, circulação, direito à informação; segurança/liberdade pessoal e remédios com M06/M12. Abrir subciclo M01.10 e matriz própria.

**P0 transversal:** assegurar direitos à vida/integridade, privacidade/dados e igualdade com fichas normativas de teste que acrescentem direito material, mas **sem** absorver sem prova garantias de busca, interceptação, sigilo, autonomia, sanções e privacidade dos envolvidos.

**P1:** integração M05/M09 para materialidade do catálogo social (art. 6–11 e 194–230), orçamento/ADCT; M10/M11 para proteção coletiva/ambiental/povos; M02 para democracia e direitos políticos.

**P2:** somente após pesquisa setorial preparar arquitetura de títulos/capítulos e possível redação definitiva, mantendo fonte única com IDs estáveis.

## 11. Fontes, grau de confiança e pendências

**Fonte primária oficial atualizada (texto vigente):** https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html (edição até EC 139/2026, consulta 13/10/2026).  
**STF Tema 698, RE 684.612:** https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=698 — tese vinculante, consulta atual de 13/10/2026.  
**CDPD equivalente à Constituição:** https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/decreto/d6949.htm .  
**Comparados:** https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html ; https://www.parlamento.pt/Legislacao/Paginas/ConstituicaoRepublicaPortuguesa.aspx ; https://www.justice.gov.za/legislation/constitution/chp02.html .  
**Fontes internas com SHA consultado:** `redacao/propostas/CF-NOR-0003…0007`, `redacao/indice.csv`, `governanca/11_TECNICA_DE_REDACAO_E_INTEGRACAO.md`, `M01-07_MATRIZ_DE_CONTINUIDADE.csv`, PR22 M01.01–M01.08.

**Nível de certeza:** localização de garantias na CF/1988 e existência de cinco propostas H = **verificado**; atribuição de cobertura e de módulos = **avaliação funcional inicial**; efeitos institucionais, financeiros e de direitos = **a testar**. **Não** foram lidos todos os acórdãos integrais, todas as emendas transitórias ou toda legislação infraconstitucional por matéria. A auditoria de 96 grupos **não** equivale a inventário por inciso/lei ou controle exaustivo de constitucionalidade.

**Riscos de reuso:** status do PR, SHA da main e edição oficial da CF podem mudar; sempre confirmar versão. Esta pesquisa não ratifica normas da CF, do CLF ou critérios decisórios de outros módulos.
