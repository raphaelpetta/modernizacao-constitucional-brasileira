# M09.03 — Pacote obrigatório de continuidade

**Data:** 14/10/2026. **Base CF main:** `50b498885e17fa1709e66b0861f40e5387b4f4b0`. **Issue:** [#68](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/68). **PR:** [#63](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/63), draft. **Estágio:** pesquisa F0–F5/F8 parcial, **sem F6/D e sem CF-NOR nova**.

## FEITO
- `M09-03_LIBERDADE_SINDICAL_NEGOCIACAO_GREVE_v0.1.md`: dossiê de liberdade positiva e negativa, unicidade versus pluralismo, representatividade, eleições internas, financiamento, negociação de boa-fé, greve e proteção de usuários, modelos A/B/C.
- `M09-03_MATRIZ_ESCOLHAS_SINDICAIS.csv`: **14 eixos SIND01–14**, melhores argumentos, objeções, fontes e prova pendente.
- `M09-03_TESTES_NEGOCIACAO_GREVE.csv`: **20 casos adversariais**, sem alegação de resultados empíricos.
- Fontes oficiais CF arts.7–11/37 VII, Lei7.783, CLT arts611-A/B, STF **Temas 1046, 935 (embargos de 26/11/2025 e movimento adicional em 2026), 531**, OIT C98 ratificada / C87 não ratificada, princípios OIT 1998/2022 e Comitê de Liberdade Sindical.

## PENDENTE
- Dados de densidade sindical, filiação, sindicalização por ramo, taxas de eleição e aderência dos não filiados; financiamento/custos reais e efeitos distributivos.
- Análise integral de acórdãos, CLT sindical, acordos coletivos e decisão final dos recursos do Tema935 mais recente; regimes público/privado e segurança de usuários.
- Interfaces M02 democracia, M05 finanças, M06 remédios, M08 mercado, M07 greve estatutária e CLF. OIT C87 **não é tratado ratificado pelo Brasil**.
- CI estrutural do HEAD final ainda a conferir. Não certifica mérito.

## PRÓXIMO
**Prioridade:** elaborar cenários institucionais completos de unicidade democratizada (A) e pluralismo representativo (B), comparando base de representação, financiamento com oposição, regras de eleição interna, negociação, proteção de grupos minoritários e transição; submeter crítica a M02/M05/M06 antes de nova norma H. Continuar M09.04 quantitativos laborais com pesquisa empírica M05, sujeito a reserva de ID.

**Resultado decisório:** nenhum D nem aprovação de modelo sindical ou de financiamento.

## Handoff complementar — modelagem comparada e testes paramétricos (14/10/2026)

**Versão de entrada da main:** `5ac08b622d7552b7d3b37a695a3027b4b9d827d4`; PR #63 permanece pesquisa draft.
**FEITO:** `M09-03_MODELOS_REPRESENTACAO_E_TRANSICAO_v0.1.md` desenvolveu modelos **A (unicidade com eleições e fiscalização)** e **B (pluralismo com representatividade e coalizões)** e contramodelo C, com regras de legitimação, voto sindical versus voto de toda a categoria, contribuição/oposição, boa-fé, minorias, greve e transição. Confrontados França (audiência 10% empresa / 8% ramo-nacional sob demais requisitos) e México (voto pessoal secreto e aprovação democrática) como comparações NÃO vinculantes. IBGE PNAD 2024, publicada 19/11/2025: **8,9% de sindicalização**, aproximadamente 9,1 milhões, **não** cobertura de acordos nem taxa de legitimação por categoria. `M09-03_MATRIZ_CENARIOS_INSTITUCIONAIS.csv`: **16 simulações e riscos**, inclusive eleições com 600 votos fictícios e 3 cenários artificiais de receitas com oposição 20/40/80%. Todos parâmetros são hipotéticos, sem inferência fiscal/causal.
**PENDENTE:** dados de sindicatos por ramo, acordos coletivos e financiamento real, custos de certificação/eleição, efeitos de limiares de votos, validação por M02/M05/M06/M08, precedentes integrais e Tema 935 em andamento 2026. Não houve norma CF-NOR, escolha de pluralismo nem ratificação D.
**PRÓXIMO:** auditoria setorial A/B de (1) indústria e serviços, (2) trabalho doméstico e pequenos estabelecimentos, (3) trabalhadores de plataformas/terceirização, (4) greve de serviços indispensáveis; obter M05 custos/indicadores IBGE e verificar legitimidade eleitoral e transição M14. Somente então preparar opções normativas H para deliberação.

**QA:** confirmar HEAD/CI PR63 na conclusão desta rodada; testes são cenários analíticos sem validação de impactos.

## Marco R2 — Testes setoriais e pedidos concretos a M02/M05 (14/10/2026)

**Base:** CF main `e648bd71227f407f2b46207e9c8d546a255254d2`; PR #63 draft; issue #68.

**FEITO:** `M09-03_AUDITORIA_SETORIAL_A_B_M02_M05_v0.1.md` compara modelos A unicidade democratizada e B pluralismo representativo **em oito perfis** (indústria, comércio/serviços, administração/saúde/educação, domésticos, plataformas, terceirização, agricultura sazonal e transporte). `M09-03_MATRIZ_SETORIAL_A_B.csv` reúne 8 avaliações e `M09-03_TESTES_SETORIAIS.csv` 24 ataques adversariais. `M09-03_DICIONARIO_EVIDENCIA_SETORIAL.csv` discrimina **17 indicadores/fatos/fontes** observados ou não obtidos com universos e riscos de inferência. Fontes oficiais: IBGE PNAD 2024 divulgado 2025 (8,9% filiação nacional, 11,4% Indústria Geral, 15,5% grupo agregado setor público/educação/saúde); MTE CNES 2026 (cadastro não demonstra voto), MTE 17/07/2026 (169 notificações **subconjunto**, sem prova de fraude), Mediador (instrumentos registrados, sem cobertura por pessoa). Sem dados reais de eleições ou orçamento privado/sindical.

**PENDENTE:** extração válida CNES/Mediador por ramo, base de trabalhadores abrangidos e taxa de voto, oposição assistencial por ramo, custos de eleições e órgão certificador, conexão com M02/M05 e análise comparada de transição M14. **Nenhum resultado causal, modelo vencedor, CF-NOR ou ratificação D.**

**PRÓXIMO:** primeiro piloto de auditoria setorial aprofundado em indústria concentrada **e** serviços domésticos dispersos, comparando A/B em base eleitoral, custos, proteção de não filiados e preservação de acordos; solicitar roteiro de coleta M05/M02 antes de simular valores ou propor lei constitucional.

**QA:** pesquisa versionada e testes conceituais; conferir CI no HEAD, sem equiparar validação estrutural a revisão econômica ou jurídica.

## Rodada piloto IND-01 × DOM-01 e PNAD 2025 — 14/10/2026

**Preflight:** `main=a763f5edf058a6622cd3d239efa6bf8e77b46e09`; [issue #76](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/76), PR63 draft; **nenhuma escolha sindical D**.

**FEITO:** dossiê `M09-03_PILOTOS_INDUSTRIA_DOMESTICO_2025_v0.1.md` examina a viabilidade procedimental de A (unicidade democratizada) versus B (pluralismo com representante eleito) em **indústria concentrada** e **trabalho doméstico disperso**: eleitorado, autonomia, mandatos, votação de não filiados, ratificação de normas, custo público e privado, privacidade, proteção de domésticos/diaristas, transição e objeções. `M09-03_PILOTOS_IND_DOM_CUSTOS_M02_M05.csv` registra **16 variáveis** com denominadores. **Dado novo:** IBGE PNAD 2025 divulgado set/2026: sindicalização nacional **8,8%**, Indústria Geral **11,4%**, Serviços domésticos (agrupamento de atividades) **2,5%**. Comparadores 2024: 8,9%, 11,4%, 2,6%, respectivamente. São **filiação e grupos estatísticos**, não voto nem cobertura. Fonte CNES/Mediador e nota 169 entidades são cadastrais, não microdados de legitimação.

**PENDENTE:** custos eleitorais e de auditoria verificáveis, taxas reais de comparecimento, de oposição e de pessoas únicas cobertas por ACT/CCT, base de empregador doméstico, proteção de dados e estudos M02/M05; não calcular custo observado de registros de CNAE ou dos valores da simulação antiga.

**PRÓXIMO:** [issue #76](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/76) coletar bases públicas por recorte/denominador e estimar custos de votação por estabelecimento/território; retornar à escolha de modelo apenas depois da análise de representatividade **e** viabilidade financeira. CI no HEAD final da branch PR63 a confirmar.

## Marco R4 — Protocolo eleitoral e custos por canal (14/10/2026)

**Preflight:** main `f6b95d977bfe293fd393972d499ca5d1965a1bcd`; PR #63 draft e [issue #76](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/76).

**FEITO:** `M09-03_PROTOCOLO_ELEITORAL_CUSTEIO_IND_DOM_R4_v0.1.md` define **três eleições com denominadores diferentes** — ELE-S direção sindical, ELE-R escolha da representação por trabalhadores abrangidos, RAT-C aprovação de acordo — mais **dez portas processuais verificáveis** em cada modelo A/B, para indústria por turnos e trabalho doméstico por território. `M09-03_PROTOCOLO_ELEITORAL_CUSTOS_AUDITAVEIS.csv` acrescenta **24 controles**, fontes, responsáveis e lacunas. Atualizados STF Tema935: **novos embargos destacados em 05/10/2026, sem decisão colegiada final**; protege direito de oposição e limite de contribuição. LC150/2015 art1: empregado doméstico exige mais de dois dias semanais e demais requisitos; diaristas não são automaticamente abrangidas pelo mesmo regime de emprego. IBGE dados 2025: **8,8%** total, **11,4%** Indústria Geral, **2,5% grupo de atividade Serviços Domésticos, mas **2,8% por posição trabalhador doméstico**; denominadores distintos. CNES/Mediador não medem votos/cobertura únicos.

**PENDENTE:** nenhum custo real de ELE-R, órgão certificador ou oposição foi medido; faltam eleitorado e participação, base setorial doméstica real, financiamento e análise de direitos de minorias, M02/M05/M06/M14. **Não há desenho B aprovado nem CF-NOR.**

**PRÓXIMO:** issue #76 solicitar M02/M05 roteiros e primeiro levantamento de fontes para variáveis de custos por canal e colégio eleitoral, preferindo documentos agregados à coleta identificável de filiação e votos. Em seguida aplicar auditoria jurídico-institucional aos dois modelos e só então eventualmente propor H.


## R5 — Auditoria de bases administrativas (14/10/2026)
**FEITO:** criados `M09-03_TRILHA_FONTES_M02_M05_E_CUSTOS_v0.1.md` e `M09-03_MATRIZ_OBSERVABILIDADE_E_CUSTOS.csv` (18 linhas), com CNES, Mediador, PNAD e categorias de custo; arquivos domésticos disponíveis são históricos de 2022, não 2026. Os procedimentos oficiais para dados RAIS identificados exigem acordo e respeito ao sigilo; nenhum dado pessoal foi acessado. **PENDENTE:** custos e votos reais e extração setorial atual; **PRÓXIMO:** executar amostra pública agregada IND/DOM para M02/M05. PR63 permanece draft, sem decisão D.
