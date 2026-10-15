# Pacote de continuidade — M03.02, rodada 01
**Data:** 14/10/2026 · **Issue:** [#84](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/84) · **Repositório:** `raphaelpetta/modernizacao-constitucional-brasileira` · **Branch:** `pesquisa/m03-02-governo-responsabilidade-20261014` · **Base da main:** `19cd7a58d4d2addbb960f7e76ecd59c3bcc958a1`.
**Proprietário funcional:** M03; interfaces M00/M02/M04/M05/M06/M07/M12/M14 e CLF T01.M04.

## FEITO (em branch, ainda não na main)
1. Dossiê `M03-02_FORMACAO_RESPONSABILIDADE_E_DISSOLUCAO_v0.1.md`: F0 delimitada; F1–F5 seletivas; estudos comparados Brasil/Alemanha/Espanha/Portugal/África do Sul/França, história 1961–63/1993, pesquisa empírica contraditória e alternativas A–E.
2. `M03-02_MATRIZ_ALTERNATIVAS.csv`: 10 funções confrontadas em cinco modelos (A presidencialismo reformado; B parlamentarismo racionalizado; C premier-presidencialismo; D presidente-parlamentarismo crítico; E presidência executiva eleita pelo Parlamento).
3. `M03-02_MATRIZ_TESTES_ADVERSARIAIS.csv`: 24 cenários fictícios, com falhas e garantias propostas, sem atribuir probabilidade empírica não estimada.
4. **Nenhuma CF-NOR foi escrita ou reservada**, nenhum `D` de forma de governo, câmara, chefia de Estado ou eleição. Texto experimental CF principal não alterado; CLF não modificado.

## PESQUISA EFETIVAMENTE CONSULTADA — selecionar fonte antes de alegar vigência
Normas: https://www4.planalto.gov.br/legislacao/legis-federal/constituicao ; https://www.gesetze-im-internet.de/englisch_gg/englisch_gg.html ; https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229&p=20260520&tn=1 ; https://www.parlamento.pt/Legislacao/Paginas/ConstituicaoRepublicaPortuguesa.aspx ; https://www.gov.za/documents/constitution/constitution-republic-south-africa-1996-chapter-5-president-and-national ; https://www.gov.za/documents/constitution/constitution-republic-south-africa-1996-chapter-4-parliament-07-feb-1997 ; https://www.legifrance.gouv.fr/loda/texte_lc/LEGITEXT000006071194/ .
Brasil histórico: https://www2.camara.leg.br/legin/fed/emecon/1960-1969/emendaconstitucional-4-2-setembro-1961-349692-publicacaooriginal-1-pl.html ; https://legis.senado.gov.br/norma/540706/publicacao/15713660 ; https://www.tse.jus.br/eleicoes/plebiscitos-e-referendos/plebiscito-1993 .
Literatura: https://doi.org/10.1590/S0102-64451998000200005 ; https://doi.org/10.1146/annurev.polisci.5.102301.084508 ; https://doi.org/10.1017/S0007123404000195 ; https://doi.org/10.1017/CBO9780511813344.006 ; https://doi.org/10.1093/acprof:oso/9780199585984.001.0001 ; https://doi.org/10.1080/13510347.2017.1334643 ; https://www12.senado.leg.br/ril/edicoes/61/242/ril_v61_n242_p11 .
Fontes em francês/alemão/espanhol consultadas como texto constitucional e/ou extrato indexado; traduções e versão vigente devem ser novamente checadas em F3 aprofundada. Não houve coleta de dataset comparável ou série temporal nacional neste ciclo.

## PENDENTE
- Controle histórico e causal rigoroso da relação entre parlamentarismo/presidencialismo, estabilidade, políticas públicas e formação de governos; dados atualizados e comparação sem viés de seleção.
- M02: efeito das fórmulas eleitorais, fragmentação, cláusulas de entrada e eleição antecipada. M04: papel de segunda câmara na confiança. M05: orçamento e continuidade de financiamento. M06: controle do chefe de Estado e desvio do impeachment. M12: reserva militar/estado de emergência. M14: transição de mandatos, primeira investidura, proteções.
- Não existem ainda dispositivos detalhados de investidura/queda/sucessão ou parecer de não regressão; posições H não homologadas.
- Verificar exatidão jurídica contra textos integrais traduzidos e versões oficiais consolidadas, atualizar data de acesso em cada nova rodada.
- QA: nenhuma CI de branch verificada neste registro, não afirmar `success` sem consulta; reexaminar conflitos e main antes de integração.
- Se ocorrer mudança concorrente em `governanca/13_QUADRO_DE_COORDENACAO.md`, preferir registro aditivo em integração central, nunca sobrescrever avanço paralelo.

## PRÓXIMO PASSO EXECUTÁVEL — M03.02, rodada 02
**Questão:** qual desenho de investidura/queda/dissolução reduz simultaneamente governo inviável e dissolução oportunista?
**Entradas:** dossiê + matrizes desta rodada, M02.01, M03.01, M04.01 e M14; fontes oficiais Alemanha arts. 63/67–69; Espanha 99/112–115; Portugal 133/172/187/192–195; Brasil 1988.
**Saída mínima:** (i) matrizes de 3 variantes internas de B (investidura expressa estrita / investidura escalonada / nomeação com possibilidade de rejeição), (ii) 4 cenários de dissolução com decisão vinculada ou discricionária e janela para sucessor, (iii) nota sobre orçamento, governo interino, crises e limites da chefia de Estado, (iv) parecer crítico A presidencialismo reformado sem caricatura, (v) handoff com evidência e status.
**Condição de encerramento:** cada mecanismo deve identificar ator, quórum, prazo, efeito, quem decide impasse, abuso possível, interface institucional; nenhuma opção vira D antes de escolha explícita.

## CONTROLE
Branch de pesquisa, sem integração à main. Aprovação de PR/CI não ratifica conteúdo. Antes de fechar/mesclar, registrar SHA real da main, HEAD do PR, estado de CI e possíveis conflitos, preservando `CF-GOV-012` e a autonomia do CLF.