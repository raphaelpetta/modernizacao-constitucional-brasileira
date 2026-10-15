# M10.01-R8 — Triagem probatória dos quatro eixos antes da redação constitucional

**Sessão:** CF-M10.01-S008 · **Corte:** 14/10/2026 · **Issue:** [#88](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/88) · **PR:** [#89](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/89), draft.  
**Main de entrada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. **PR HEAD de entrada:** `377c1fae178b220a8ac5ecc28b2f107c75e72e3a`.  
**Estado:** F1/F4/F5 documental, sem F6 decidida, F7 redigida ou F8 de equivalência real.  
**Produtos:** `M10-01_R8_TRIAGEM_PROBATORIA_QUATRO_EIXOS.csv` (**14 questões em quatro eixos**), `M10-01_R8_CRONOLOGIA_ART225_VIII_EC132.csv` (**5 marcos**), `M10-01_R8_TESTES_SUFICIENCIA_PROVA.csv` (**8 testes documentais**), parecer e handoff.

## 1. Critério de verificação

Separar com rigor:
1. **NORMA VERIFICADA:** fonte oficial com comando existente no direito positivo; não equivale a conclusão constitucional sobre lei controvertida.
2. **COBERTURA DOCUMENTAL EM PR/MAIN:** trabalho efetivamente lido de outro módulo; não implica parecer dado ao M10 nem revisão cruzada aceita.
3. **RESPOSTA INTERMODULAR:** documento de módulo competente que enfrenta **literalmente** a questão Q da R7 com fatos/ônus/fontes e limites. Não localizar resposta significa **não localizada na amostra Git consultada**, não prova de inexistência universal.
4. **VERIFICAÇÃO PENDENTE:** movimentação judicial atual, eficácia normativa específica, leitura completa de decisões, dados e demonstração material.
5. **D:** somente aprovação material do usuário conforme [governança CF-DEC](../../governanca/03_DECISOES.md), não resultado de PR ou teste estrutural.

Os quatro eixos cobrem 14 das 35 perguntas R7, não todas as funções da CF ou do M10.

## 2. Eixo I — EIA e tutela (Q05, Q19)

### Texto positivo conferido

- [CF/1988 art.225, §1º IV](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm): **EIA prévio e publicidade** quando a obra/atividade pode causar **degradação significativa**. Esse é o limiar constitucional expresso; toda atividade não necessariamente requer o mesmo EIA.
- [Lei 15.190/2025 arts.38–41](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm): modalidades legais de informação e participação. Art.40 exige pelo menos uma audiência prévia à LP para atividade sujeita a EIA, e disponibilização EIA/Rima com 45 dias de antecedência. **45 dias é número da lei, não da CF**.
- [Lei 7.347/1985 compilada](https://www.planalto.gov.br/ccivil_03/leis/l7347compilada.htm): arts.1,3,4,5 e 8 preveem ACP para meio ambiente, obrigação de fazer/não fazer/indenização, instrumento preventivo, legitimados diferentes e obtenção de informações. MP e Defensoria, entes estatais e associações com condições legais; **não** trocar legitimidade de ACP pela legitimidade do **cidadão** na ação popular (CF5 LXXIII).

### O que existe no projeto, e o que não foi respondido

O [CF-NOR-0007](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/main/redacao/propostas/CF-NOR-0007.md) está **H na main** e contém garantia geral de acesso judicial; não menciona EIA, remédios coletivos específicos, ônus de perícia ou legitimados. O [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62) documenta **ação popular e cinco remédios constitucionais**, com ressalva explícita de não equivalência da tutela geral. **Não foi encontrado dossiê próprio de ACP ambiental por legitimado, custos, prova e execução**, nem resposta M06 Q19. O trabalho do PR62 não pode ser reportado como validação de ACP ambiental.

**Resultado:** comandos materiais e processuais no direito vigente = **verificados**; equivalência a CF-NOR H e interface M06 = **não demonstradas (A/V)**.

## 3. Eixo II — Federação, órgão licenciador e fiscalização (Q11–13)

- [LC 140/2011, art.13](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp140.htm): um ente federativo responsável pelo licenciamento ambiental por empreendimento; art.17 contém regra fiscalizatória sem eliminar dever comum de proteção.
- **STF, [ADI 4.757/DF](https://portal.stf.jus.br/constituicao-supremo/artigo.asp?abrirArtigo=23&abrirBase=CF), julgamento encerrado em 12/12/2022, DJE 17/03/2023:** interpretação conforme do art.14 §4 (mora injustificada/imotivada e desproporcional na renovação faz incidir supletividade) e do art.17 §3 (fiscalização de outro ente quando comprovada omissão/insuficiência). A decisão *não* instituiu quatro licenciadores simultâneos.
- [LC140 art.14 §3](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp140.htm): ultrapassar prazo **não cria licença tácita**; art.14 §4 trata da renovação tempestiva e sua prorrogação legal, que não é concessão automática de licença nova.
- [Lei 15.190/2025 art.1 §1 e art.18](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm): regras nacionais procedimentais no contexto das atribuições da LC140; a hipótese de antinomia demanda dispositivo e interpretação específicos.

**Interface real:** a [M04.01 na main](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/blob/main/modulos/M04-federacao/M04-01_CONSENTIMENTO_TERRITORIAL_E_IMPASSES_v0.1.md) distingue legislação/execução/finanças e reserva de competências, porém estuda **consentimento territorial e processo de lei**, não responde com parecer de licenciador/fiscalização/atuação supletiva ambiental para Q11–13. Não presumir parecer jurídico emitido ao M10.

**Litigância de 2025:** na [pauta oficial STF de 12/08/2026](https://noticias.stf.jus.br/postsnoticias/confira-a-pauta-do-stf-desta-quarta-feira-12-2/) constam ADIs 7913/7916/7919 e ADC102. Registros indexados do portal incluem movimentações em agosto/setembro/2026, mas **o acesso direto aos autos retornou HTTP 403 em 14/10**; portanto **última decisão de mérito/cautelar não certificada nesta auditoria**. Pauta e petição não têm efeito de julgamento.

**Resultado:** LC140 e dispositivo ADI4757 verificados; decisão sobre constitucionalidade da legislação de 2025 não atestada; parecer M04/M07 ambiental **ausente na pesquisa**.

## 4. Eixo III — Povos, direitos originários, consulta e tratados (Q26–27, Q30)

- [CF art.231](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) reconhece direitos originários dos indígenas. Não confundir **existência de direito material** com o estágio de formalização do procedimento de demarcação.
- [Decreto 10.088/2019, **Anexo LXXII**](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/d10088.htm) contém **Convenção OIT nº 169**, especialmente arts.1,6 e 7, cujo campo de incidência e formas de consulta devem ser analisados por instrumento e fato.
- [Lei 15.300/2025 art.4 §2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm) distingue expressamente audiência pública no LAE de consulta prévia, livre e informada aos povos/comunidades tradicionais, quando aplicável.
- [Lei 15.190/2025 arts.43–44](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm) utiliza *gatilhos institucionais* referidos a terras homologadas/tituladas para manifestação de órgãos envolvidos; não esgota, por si, a interpretação dos direitos constitucionais e convencionais dos titulares.

**Interface real:** no preflight, nenhum dossiê M11/M13 com parecer de consulta específico foi encontrado entre módulos da `main` ou PRs abertos do projeto. A formulação da R7 é **pedido de exame funcional** e não evidência de que M11/M13 tenham concluído validação. Determinar hierarquia da Convenção 169, legitimidade da consulta, alcance do consentimento e regime jurídico de povos afetados requer estudo competente; **não presumir veto geral ou dispensa de consulta**.

**Resultado:** fontes positivas verificadas; parecer intermodular M11/M13 e resultado final do controle de normas sobre licenciamento **pendentes**.

## 5. Eixo IV — Regras especiais e transição (Q08, Q10, Q14, Q17, Q29, Q31)

O [art.225 da CF](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) contém comandos especiais que não devem desaparecer inadvertidamente:
- **§1 VII e §7**: proteção da fauna/flora e ressalva cultural específica com condições;
- **§4**: enumeração de territórios/ecossistemas integrantes do patrimônio nacional, sem significar domínio federal apenas pela expressão;
- **§5**: indisponibilidade de terras devolutas ou arrecadadas pelos estados necessárias à proteção de ecossistemas naturais; não alcança automaticamente toda terra devoluta;
- **§6**: localização de usina com reator nuclear definida por **lei federal** como condição de instalação;
- **§1 VIII**: comando fiscal setorial, **não** mera norma geral de desenvolvimento sustentável.

### Nova verificação documental relevante — aplicação temporal da EC132

A [EC 132/2023](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc132.htm) determina **três versões sucessivas** do art.225 §1 VIII:
1. **Art.1º**, vigente desde a publicação da EC132 em dezembro/2023 até antes da próxima redação: regime favorecido para biocombustíveis e hidrogênio de baixa emissão com remissões aos tributos então existentes e ao IBS/CBS previsto.
2. **Art.3º**, que pelo **art.23 I** só entra em vigor em **2027**: nova redação ajustada à extinção de contribuições e à transição do sistema tributário.
3. **Art.4º**, que pelo **art.23 II** só entra em vigor em **2033**: outra redação, removendo referência ao ICMS em razão do faseamento.
A [LC 214/2025 compilada, art.175](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm) estabelece diferencial tributário com faixa **legal** de 40% a 90% das alíquotas de IBS/CBS relativas a fósseis comparados. **O percentual não consta na norma constitucional.** Sem estudo fiscal M05 não afirmar como se opera integralmente o tributo em 2026 nem simular impactos reais.

**Consequência de rastreio:** copiar em 2026 a redação prevista apenas em 2033 apagaria remissões que o legislador constituinte ainda trata no período de transição. Esta rodada conferiu o **faseamento no texto da emenda**; ainda falta parecer M05/M14 sobre aplicação concreta, dispositivos intertemporais adicionais, legislação e contratos.

**Outras funções especiais:** pesquisas R5–R7 catalogam, mas não há texto M10 aprovado, parecer setorial completo ou decisão material sobre sua manutenção/reorganização. A inexistência de `CF-NOR` correspondente não constitui proposta de supressão.

## 6. Resultado da matriz e dos testes

**14 questões:** eixo EIA e tutela Q05/Q19 (2), Federação Q11–13 (3), povos e tratados Q26–27/Q30 (3), regimes especiais/transição Q08/Q10/Q14/Q17/Q29/Q31 (6). A matriz distingue norma pública verificada, documentação existente em Git, lacuna precisa e fonte.

**Oito cenários hipotéticos:** (1) EIA ausente e ação cívica; (2) ACP sem fácil acesso a estudo; (3) fiscalização supletiva de ente não licenciador; (4) demora em licença inicial versus renovação; (5) audiência LAE sem consulta devida; (6) terra indígena não homologada; (7) confusão temporal EC132; (8) omissão simultânea de quatro comandos especiais. Não são eventos observados nem previsão de decisões.

## 7. Preparação para eventual F6/F7: limites da suficiência

| Eixo | Direito positivo verificável | Resposta intermodular sobre equivalência | Porta que permanece aberta |
|---|---|---|---|
| EIA e tutela | CF EIA; Lei7347 ACP e legitimados; L15190 participação | PR62 examina ação popular, **não ACP ambiental integral**; nenhuma validação de texto M10 | G2 + G3 + G4 |
| Federação | LC140 e dispositivo STF ADI4757 | M04.01 trata leis e consentimento territorial, **não** revisa ambiental por operação | G2 + G3 + G4 |
| Povos e tratados | CF231; OIT169 no Decreto10088; lei LAE | M11/M13 não emitiram parecer identificado | G2 + G3 + G4 |
| Especiais e transição | CF225 regras e EC132 com 2023/2027/2033 | M05 analisa finanças em geral; M14 e setoriais não responderam à temporalidade específica | G2 + G3 + G4 |

**Nenhum eixo reúne evidência suficiente para declarar equivalência de uma norma candidata**, pois não há texto candidato; a legislação e a existência de um dossiê paralelo não fecham a porta G2. Para uma futura deliberação F6, distinguir (a) escolha sobre **função/alcance material**; (b) escolha **editorial A/B**; (c) implementação legal e revisão técnica. A documentação **autoriza formular questões e alternativas sem selecionar**; não autoriza registrar D.

## 8. Preliminar de continuidade e crítica do próprio método

A sequência de oito rodadas M10 tem matrizes extensas, mas repetições não equivalem a revisão independente. Na próxima etapa, evitar produzir outro catálogo amplo sem novo objeto. A tarefa precisa resultar em **produtos editoriais concretos de comparação**, mantendo C0 como baseline e sinalizando as questões sem resposta.

**FEITO:** triagem baseada em leitura literal de legislação, STF ADI4757, CF-NOR0007 H, PR62/M04.01/M05.01, quatro eixos e 14 perguntas, cronologia tributária e oito testes.  
**PENDENTE:** respostas M04/M05/M06/M11/M13/M14, STF pós-pauta, dados materiais, decisão F6, texto e avaliação de equivalência.  
**PRÓXIMO — M10.01-R9:** *provas de redação não canônica*: dois esboços em documento de pesquisa (A capítulo e B distribuição) para as funções **cujos pressupostos positivos foram identificados**, com colchetes de reserva para Q19/Q26/Q27/Q30/Q17 e regras especiais; a cada frase, mapa exato CF vigente→fonte/competência→remédio→dependência. **Não** criar ou reservar CF-NOR nem mexer no índice sem preflight e deliberação de técnica editorial. Esse artefato deverá permitir uma auditoria N:N **sobre texto concreto hipotético**, ao contrário das rodadas apenas estruturais.

**Regra:** PR89 draft, `main` intacta; F6 material continua A/V. CI estrutural não certifica constitucionalidade ou equivalência.
