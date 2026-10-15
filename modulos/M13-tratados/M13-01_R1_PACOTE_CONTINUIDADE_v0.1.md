# M13.01-R1 — Pacote de continuidade FEITO / PENDENTE / PRÓXIMO

**ID:** CF-M13.01-S001 · **Corte:** 14/10/2026 · **Issue:** [#93](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/93) · **Branch:** `pesquisa/m13-01-tratados-hierarquia-20261014` criada da **main SHA `2a770a8136f8ca4877e865be3e3b7745a6d4b168`**.  
**Natureza:** F0 reservado na issue, F1–F5 pesquisa jurídica inicial, **sem D/F6, CF-NOR/F7, IDs normativos, escrita `redacao/`, `main` ou CLF**. PR draft/QA pendentes de fechamento.

## FEITO — R1

| Arquivo novo | Comprovação e conteúdo | Limite |
|---|---|---|
| `M13-01_R1_DOSSIE_CADEIA_TRATADOS_E_HIERARQUIA_v0.1.md` | Sete momentos jurídicos de incorporação/controle, quatro instrumentos (OIT169, CDPD, Paris, CADH), CF5 §§2–3, CF49 I/84 VIII, STF RE466343/HC87585 e ADPF708/2022 | É pesquisa documental, não norma constitucional futura nem decisão para qualquer tratado |
| `M13-01_R1_MATRIZ_CADEIAS_TRATADOS_E_HIERARQUIA.csv` | **24 verificações** (4 instrumentos × 6 fases documentais), com datas, fonte oficial, grau de certeza, campo de atuação e limite | Rito/hierarquia não bastam para demonstrar impacto e tutela |
| `M13-01_R1_TESTES_ADVERSARIAIS_TRATADOS.csv` | **12 casos hipotéticos**: rito C169/CDPD, consolidação do decreto, Acordo de Paris, consulta e audiência, órgão interveniente, controle de lei, efeito de ADPF/convencionalidade e competência | Testes não substituem causa real ou parecer de M11/M06 |
| `M13-01_R1_PARECER_INTERFACE_F05_M10_M11_v0.1.md` | **Resposta efetiva e PARCIAL de M13** às questões C169-F05, com classificação supralegal por orientação jurisprudencial e identificação do rito | Parecer não aprova A/B, não soluciona representação territorial ou efeitos judiciais |
| Este pacote | FEITO, PENDENTE, PRÓXIMO e cuidados para QA | CI mede estrutura, não validade normativa |

### Resultado jurídico com prova de rito

1. **C169 OIT:** DL143/20.06.2002; depósito ratificação 25.07.2002; vigência externa Brasil 25.07.2003; Decreto5051/2004 promulgador; AnexoLXXII Decreto10088/2019 consolidado. **Sem rito CF5 §3**, acrescido pela EC45/2004; como tratado DH, **supralegal por orientação STF**, sem alegar julgamento nominal da C169 no RE466343. [Decreto5051](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/decreto/d5051.htm), [Decreto10088 consolidado](https://www2.camara.leg.br/legin/fed/decret/2019/decreto-10088-5-novembro-2019-789348-normaatualizada-pe.html), [STF tratados supralegais](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=100258&ori=1).
2. **CDPD + Protocolo:** DL186/09.07.2008 aprovados **art5 §3**, ratificação 01.08.2008, vigência 31.08.2008, Decreto6949/2009; **equivalência de emenda**, distinto de C169. [DL186](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/congresso/dlg186-2008.htm) e [Decreto6949](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/decreto/d6949.htm).
3. **Acordo Paris:** DL140/16.08.2016, ratificação 21.09.2016, vigência Brasil 04.11.2016, Decreto9073/2017; **ADPF708 julgado em 2022** relacionou tratados ambientais ao DH e reconheceu valor **supralegal** no âmbito climático, **não emenda constitucional**. [Decreto9073](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/decreto/d9073.htm), [STF ADPF708](https://www.stf.jus.br/arquivo/informativo/documento/informativo1061.htm).
4. **CADH:** DL27/26.05.1992; adesão/vigência Brasil 25.09.1992; Decreto678/1992; **supralegalidade em RE466343/HC87585** como paradigma, sem anular texto da CF. [DL27](https://www2.camara.leg.br/legin/fed/decleg/1992/decretolegislativo-27-26-maio-1992-358314-publicacaooriginal-1-pl.html), [Decreto678](https://www.planalto.gov.br/ccivil_03/decreto/d0678.htm).
5. **Efeito sobre F05 M10:** C169 art6 consulta em medidas legislativas/administrativas **suscetíveis de afetação direta**, art7 planos/programas e art15 recursos; [Lei15300 art4 §2](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15300.htm) audiencia LAE ≠ consulta quando devida; [Lei15190](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15190.htm) manifestação institucional ≠ manifestação representativa do povo. Hierarquia **não gera veto universal**.
6. **Limite de pesquisa:** STF/SV25 e Informativo ADPF708 tiveram abertura de páginas com HTTP403 em busca direta; passagens relevantes disponíveis em resultados indexados e em outras páginas oficiais, não certidão de acórdão consultado integralmente. A hierarquia positiva da C169 decorre de enquadramento jurídico do rito e do precedente geral, não atribuição indevida de decisão nominal.

## PENDENTE

- [ ] Abrir **PR próprio draft** para M13.01 e publicar referências em issue #93, M11 #92 e M10 #88; registrar SHA real.
- [ ] M11: exame fático de direitos originários/representação/afetação direta, que a posição do tratado não resolve. [PR94](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/94) é pesquisa paralela H/V.
- [ ] M10: efeitos materiais EIA/LAE e proteção ambiental; arquitetura A/B **não selecionada**, F05 mantém responsabilidade de integração [PR89](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/89).
- [ ] M06: remédios, legitimidade CF232, prova e competência para controle de convencionalidade, recursos judiciais; [PR62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62) já tem pesquisa parcial de MI/popular.
- [ ] M00: cláusulas gerais de fontes, competência para assinatura/aprovação/denúncia, relação com ordenamento reformulado; denúncia/revisão de tratados requer estudo próprio antes de qualquer redação.
- [ ] Instrumentos ambientais adicionais: testar tratados específicos quanto a natureza e precedente, não generalizar ADPF708 a qualquer convenção técnica.
- [ ] Prova e jurisprudência: obter decisões integrais de casos interamericanos/ADPF708 e efeitos do controle nos termos de processo; não converter notícia/resumo em resultado não conferido.
- [ ] F6 e F7: **sem escolhas, texto candidato canônico, prova de equivalência ou integração CF**.
- [ ] QA GitHub: confirmar 4 arquivos, 24 linhas/12 casos/refs, PR draft, CI/HEAD e main inalterada.

## STATUS

| Objeto | Estado |
|---|---|
| M13.01 | F0 issue #93; F1–F5 iniciais na branch, H/V |
| OIT169 | Ato/rito/ingresso demonstrados; classificação supralegal fundamentada em orientação geral STF |
| CDPD | Rito CF5 §3 documental e equivalência de emenda |
| Paris | ADPF708/2022, supralegalidade no contexto do julgamento |
| CADH | Supralegal no precedente STF; não EC |
| F05/M10 e M11 | `PARECER_M13_PARCIAL_R1` após comentário/PR, sem encerrar F05 |
| `main` e CLF | Não alteradas |
| CF-NOR/F6/D | Nenhuma norma ou decisão criada |

## PRÓXIMO — M13.01-R2

**Uma pesquisa adversarial nova, não catálogo repetido:** conflito concreto de **C169 art6 × Lei15190/2025 arts42–45 × Lei15300/2025 art4 §2**, com três padrões territoriais/afetação herdados da M11-R3, delimitando prova e remédio judicial, efeito de norma supralegal contra lei, manifestação institucional versus consulta. Verificar fase/resultado de ADIs ambientais de 2025 **somente com certidão decisória**; não atribuir controle abstrato automático só porque tratado é supralegal.

**Preflight:** antes de novo texto, revisar comentários específicos de M11/M10/M06 e eventual ato superveniente. Sem necessidade de consulta a usuário nem ratificação de alternativa A/B para continuar F1–F5; nenhuma CF-NOR ou merge autorizado por este pacote.
