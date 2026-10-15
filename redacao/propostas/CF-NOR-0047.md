# CF-NOR-0047 — Fiscalização parlamentar e direito de investigação das minorias

**Estado:** H/A, hipótese autônoma não ratificada. **Módulo:** M03.01/M03.02 (garantia transversal aos modelos A/B/C). **Corte:** 15/10/2026. **Base:** PR #116 `abf450fd5491b8310e1e02b88102c370dcaeac45`; `main` `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **Proveniência:** [CF/1988 art. 58, §§ 2–3 (texto oficial Câmara)](https://www2.camara.leg.br/legin/fed/consti/1988/constituicao-1988-5-outubro-1988-322142-normaatualizada-pl.html), [STF jurisprudência do art. 58](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=58&abrirBase=CF), [STF Informativo 572, MS 24.831/MS 24.847](https://stf.jus.br/arquivo/informativo/documento/informativo572.htm), [STF MS 23.452/reserva judicial](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=5&abrirBase=CF), [protótipos M03 no PR #107](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/107). **Risco:** R3 — minorias/oposição, separação de poderes e direitos individuais.

<!-- NORMA-INICIO -->
O Poder Legislativo exercerá fiscalização e controle dos atos do Governo e da Administração Pública, assegurados instrumentos efetivos de informação e investigação e a participação das minorias parlamentares, nos limites desta Constituição.

A comissão parlamentar de inquérito será instituída mediante requerimento de um terço dos membros da Casa legislativa competente, para apuração de fato determinado e por prazo certo, independentemente de autorização política da maioria, quando preenchidos os requisitos constitucionais.

A comissão terá poderes de investigação próprios das autoridades judiciais, respeitadas a reserva de jurisdição, as garantias fundamentais e os direitos da pessoa investigada ou convocada, inclusive a não autoincriminação e a assistência por advogado. Suas conclusões serão encaminhadas, quando cabível, ao Ministério Público e aos órgãos competentes, sem substituir suas atribuições constitucionais.
<!-- NORMA-FIM -->

## Função transversal e direito vigente

- **CF/1988 art. 58 §3º:** CPI requer 1/3, fato determinado e prazo certo, com poderes investigativos próprios de autoridades judiciais; remessa ao Ministério Público quando cabível. Essas garantias constam expressamente da H; não trocar o quórum por maioria nem subordinar instauração ao Presidente ou primeiro-ministro.
- **MS 24.831, MS 24.847 e STF Informativo 572:** preenchidos os três requisitos constitucionais, instalação traduz garantia contramajoritária; não permitir que a maioria converta dever de instalação em juízo político de conveniência.
- **MS 23.452 e outros precedentes:** poderes da CPI não alcançam atos sob reserva de jurisdição como interceptação telefônica, busca domiciliar e prisão fora de flagrante. Direito ao silêncio/não autoincriminação, advogado e fundamentação são preservados. A eventual quebra de sigilos segundo precedentes e legislação demanda especificação da competência, proporcionalidade, motivação e controle.
- **INV-03 do protótipo M03 PR #107:** oposição precisa de fiscalização e informação em A presidencialismo reformado, B parlamentarismo racionalizado, C premier-presidencialismo e contramodelos. O texto não outorga voto de confiança, censura, dissolução ou investidura, nem define Câmara alta, quórum legislativo ou quem preside o governo. A primeira oração é hipótese G funcional, mas a ficha é classificada A por assegurar mecanismo institucional próprio em um único bloco articulado.

## Objeções e trade-offs

**Melhor objeção (abuso minoritário):** instalação automática pode causar CPIs sobre fatos artificiais, exposição de dados privados e controle sem freio; a maioria perderia toda capacidade de agenda. **Contrapeso:** fato determinado, prazo certo, normas de procedimento e direitos, controle de legalidade e responsabilidade; não transformar a maioria em filtro político quando preenchidos requisitos.

**Melhor objeção (congelamento de bicameralismo):** o termo “Casa legislativa” poderia pressupor duas casas. **Resposta:** emprega singular e designa a unidade com competência investigativa; uma futura arquitetura unicameral também possuirá órgão legislativo, sem decidir número de casas nem competência investigativa subnacional.

**Melhor objeção (processo inquisitorial):** assegurar contraditório integral como se CPI fosse processo judicial criaria incoerências e poderia impedir fiscalização. **Resposta:** enunciar garantias fundamentais, silêncio, assistência e controle segundo o ato; não equiparar CPI a tribunal ou dar poder de julgar/censurar automaticamente.

**Melhor objeção (redundância com arts 5 e tutela):** direito de defesa/não autoincriminação já tem norma geral; manter referência na CPI impede leitura de poderes judiciais sem garantias. O efeito especial é delimitar investigação parlamentar e o direito contramajoritário.

## Correspondência N:N e lacunas

| Garantia atual | Proposta | Estado |
|---|---|---|
| CF 58 §3, 1/3 + fato + prazo | §2 | preservada expressamente |
| CF 58 §3, poderes investigativos | §3 | preservada com limites |
| CF 58 §3, remessa ao MP | §3 | preservada |
| STF direito da minoria | §2 | expressamente resguardado |
| Reserva de jurisdição CF 5 | §3 | explícita |
| CF 5 direito ao silêncio/advogado | §3 | explícita, demais garantias sob revisão |
| CF 58 §2 outros poderes de comissões | §1 genérico | **parcial**: pedidos, convocações, audiências e petições exigem norma futura |
| CPI conjunta de duas Casas | ausente | **pendente** se bicameralismo for escolhido |
| Fiscalização financeira CF 49/70–75 | §1 genérico | **pendente** M05/M06, TCU/órgãos próprios |
| Censura/confiança e dissolução | ausente | **deliberação M03 aberta** |

## Testes adversariais

1. Governo tenta impedir investigação de seus próprios contratos em Câmara onde controla maioria.
2. Um terço subscreve CPI e a Mesa recusa instalação por conveniência.
3. Um terço requer fato indeterminado ou CPI sem prazo certo.
4. CPI pretende decretar interceptação telefônica ou busca domiciliar sem ordem judicial.
5. Depoente investigado é obrigado a se autoincriminar.
6. Convocação exige advogado seja impedido de assistir pessoa convocada.
7. CPI fiscaliza política pública legítima sem razão concreta; fundamentação e proteção de dados.
8. Governo B perde maioria, mas CPI exige investigação independente de voto de censura.
9. Presidente A se recusa a enviar informação legislativamente devida.
10. Câmara alta futura desconhecida reivindica criação de CPI conjunta.
11. CPI tenta julgar criminalmente pessoa convocada em vez de remeter às instituições competentes.
12. Em urgência fiscal, maioria tenta suspender toda fiscalização, invocando continuidade governamental.

**FEITO:** hipótese H/A de núcleo fiscalizatório comum, sem escolher sistema de governo, mais matriz N:N e testes. **PENDENTE:** revisão M03/M06/M05/M12, especialidades de convocação/sigilo, desenho de Casas, fiscalização financeira e controle de governos de exceção; não afirmar equivalência integral com CF 58 e 49/70–75. **PRÓXIMO:** formular opções A/B/C de controle financeiro, confiança, voto de censura e poderes parlamentares sem atrelar este núcleo de CPI a um modelo específico. **Interfaces:** M00/M01/M02/M04/M05/M06/M07/M12/M14; nenhum efeito direto no CLF.