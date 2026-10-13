# CF-IC-001 — Devolutiva da simulação integral CP/CE: formação, veto e atualização do Código único

**ID:** CF-INT-005 · **Corte:** 13/10/2026 · **Estado:** PESQUISA H/A/V, **nenhuma aprovação constitucional**.  
**Baseline constitucional consultado:** `4c728c0bc5ef1d5c9fb6b4d76a20286f759704fb`.  
**Referência CLF:** baseline `3a5a4977b51b4666d16ab453769ed98cb0442982`, integração confirmada no commit `74aa56d2942d1499044fbf5256909692be904ece`, via [PR CLF #19](https://github.com/raphaelpetta/codigo-legislacao-federal/pull/19).  
**Documento substantivo de origem:** `modulos/T01/M04/SIMULACAO_08_PROCESSO_COMPLETO_CP_CE.md`.  
**Dados:** `MATRIZ_ETAPAS_CP_CE_08.csv` (72 estados) e `FALHAS_E_DECISOES_CP_CE_08.csv` (20 riscos e bloqueios).  
**Módulos afetados:** M00.02 (espécies/reservas), M03.01 (Parlamento/competências/iniciativa/veto), M04 (federalismo), M06 (autonomia do Judiciário), M14 (transição), M01 (direitos processuais).

## 1. Correção importante: trocar componente ordinário histórico por direito vigente

A simulação **não** reproduziu a antiga isenção da COFINS da LC 70/1991 como norma vigente. Esse dispositivo é exclusivamente **ilustração jurisprudencial histórica** da Súmula Vinculante 62, sobre LC formal de conteúdo materialmente ordinário.

O componente **O** foi substituído pela **Lei 9.784/1999, art. 2º**, de processo administrativo federal, materialmente lei ordinária no recorte; mantém garantias de contraditório, motivação, segurança jurídica e proporcionalidade, em diálogo com a Constituição. Fonte: https://www2.camara.leg.br/legin/fed/lei/1999/lei-9784-29-janeiro-1999-322239-normaatualizada-pl.html .

Outros componentes:
- **T:** CTN art. 174, prescrição tributária e reserva de LC em normas gerais (CF art. 146, III, b). A **LC 236/2026 teve vetos parciais efetivos** em trechos projetados para o art. 174, conforme cadastro e Mensagem 743/2026; o texto vetado não deve aparecer como direito positivo sem ulterior superação válida do veto. https://www2.camara.leg.br/legin/fed/leicom/2026/leicomplementar-236-4-setembro-2026-799905-norma-pl.html .
- **J:** Lei 11.416/2006 arts. 11–13, remuneração do Judiciário federal. Alteração material reservada depende da iniciativa dos tribunais competentes; iniciativa parlamentar em **consolidação inteiramente fiel com revogação/reedição** continua controvérsia não pacificada na pesquisa do CLF #14. https://www2.camara.leg.br/legin/fed/lei/2006/lei-11416-15-dezembro-2006-548306-normaatualizada-pl.html .

## 2. Resultado constitucional por modelo

### CP/P3 — procedimento de codificação coordenada sem espécie nova expressa

A sequência pode identificar iniciativas reservadas, controlar matérias, votações e conciliações (`S00–S06`). Na fase `S07`, porém, o esboço **não define o estatuto do ato formal uno**, a sanção, o veto, a promulgação e o procedimento de futuras emendas. Logo, **não demonstrou unidade jurídico-formal real em sua redação atual**. Pode ser melhorado, mas talvez isso equivalha a criar espécie especial *de facto*.

### CE/P4 — Código como espécie constitucional

A Constituição hipotética daria identidade **a um corpo único de legislação federal permanente**, mas a sequência `S07–S09` permanece bloqueada pelas regras incompletas sobre veto, promulgação, revogação dependente, votação final, impasses entre Câmaras e ausência de iniciativa reservada. A identificação de espécie **é necessária para clareza, mas insuficiente** para declarar o desenho pronto. Alterações futuras devem respeitar a **reserva material**, não rigidificar toda norma por seu lugar no Código.

**Não há resultado empírico que prove ser CE superior a CP**, apenas hipótese de melhor explicitação formal. Não classificar CE como arquitetura ratificada pela CF.

## 3. Um problema de veto concreto que exige solução

O direito brasileiro vigente disciplina veto no art. 66 da CF/1988. Seu §2º permite vetar apenas texto **integral de artigo, parágrafo, inciso ou alínea**, e a rejeição pelo Congresso segue as regras do §4º. A LC 236/2026, com vetos parciais em matéria tributária, mostra que o legislador precisa distinguir texto aprovado no Parlamento, veto e promulgação.

**Hipótese adversarial:** componente **T** é apropriadamente votado e aprovado, mas o veto elimina parágrafo novo que substituiria dispositivo antigo. Um artigo de revogação da norma antiga não pode permanecer eficaz por presunção do editor; a hipótese constitucional precisa dizer como funciona a **dependência entre substituição e revogação**. Se ambos são independentes no texto promulgado, o resultado pode criar lacuna involuntária.

**Duas hipóteses rivais para pesquisa (não ratificadas):**
- **V1 — veto em unidades de texto + cláusulas de dependência legislativa expressas**, com efeito preestabelecido em lei votada, preservando legalidade de veto no sistema escolhido;
- **V2 — veto de componente material indivisível previamente delimitado**, admitido somente em Constituição que regulamente exatamente seus limites, revisão legislativa e proibição de veto estratégico amplo.

**A pesquisa NÃO concluiu** que a norma vigente art. 66 pode ser alterada por LC ou regimento, nem que o veto de bloco inteiro seja permitido hoje.

## 4. Perguntas ao M03.01 para desenho constitucional mais completo

1. **Identidade do ato único:** no CP, que instrumento transforma votações por espécies diferentes em **norma formalmente una**, com força legal e alteração posterior? Criaria espécie nova oculta?
2. **Iniciativas múltiplas:** como combinar proposta dos tribunais, iniciativa geral parlamentar e eventualmente iniciativa executiva? O que fazer se um titular não participar? Não presumir que houve iniciativa válida por ratificação informal/sanção.
3. **Bicameralismo:** a nova Constituição ainda não decidiu papel e composição das Casas. Como reapreciar componente modificado pela revisora, sem apagar quórum/autor de iniciativa?
4. **Voto final de integração:** ato de aprovação normativa efetiva ou mera certificação? Qual competência e qual maioria? Como não substituir votações de componente reservadas?
5. **Sanção e veto:** quem exerce veto no sistema de governo ainda **não definido**? Existe veto de mérito e de constitucionalidade, ou controle diferente para componentes de iniciativa judicial? Quem revê o veto e por qual maioria?
6. **Promulgação parcial:** quando só dois dos três componentes passam, o corpo legislativo do Código pode entrar em vigor sem falsa promessa de cobertura completa? Normas externas antigas devem ficar claramente vigentes.
7. **Regras de transição e dependência:** como condicionar revogação a novo dispositivo eficaz e preservar direitos constituídos e efeitos residuais?
8. **Emenda ordinária a Código formalmente reforçado:** matéria materialmente ordinária pode ser alterada por rito ordinário sem exigir quórum qualificado artificial?
9. **Editor e fonte oficial:** que órgão publica o corpo promulgado; como corrigir erro de indexação ou de transcrição sem exercer competência legislativa?
10. **Controle judicial e conflitos de competência:** controle concentrado de parte do Código, inconstitucionalidade por falta de iniciativa, preservação dos componentes não atingidos e comunicação dos efeitos temporais.

## 5. Encaminhamento ao CLF e estado da interface

**Pedido de devolução:** quando M03.01 e M00.02 concluírem comparação constitucional própria, devolver **dois fluxos completos CP e CE** com respostas expressas para S07–S10, inclusive autoridade promulgadora, veto parcial, revogação dependente e primeiro ato alterador por matéria. Formular uma **solução alternativa** se ambos falharem, sem privilegiar CE apenas por nome.

O projeto CLF pode prosseguir em estudo modular e criação de metadados com a fonte real, sem alegar positividade de algum texto hipotético. `CF-IC-001` permanece **PESQUISA**, e `DEC-016` (CLF) **PENDENTE**. Os artigos constitucionais antigos e alternativas de governo não foram ratificados por esta devolutiva.

**Integridade dos vínculos:** a integração deste dossiê é uma transferência documental de perguntas e testes, não uma transposição automática de dispositivo CLF para a futura Constituição.
