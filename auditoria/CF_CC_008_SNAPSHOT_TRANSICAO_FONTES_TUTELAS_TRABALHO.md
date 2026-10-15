# CF-CC-008 — horizontalidade M14/M00 e salvaguardas específicas M06/M09

**Corte:** 15/10/2026. **Produto experimental cumulativo:** 41 hipóteses H em **13/15 módulos** na branch `redacao/cfcc008-m14-m00-m06-m09-20261015` (descendente dos PRs #105–#113), **main não alterada: 20 H** no HEAD `2a770a8136f8ca4877e865be3e3b7745a6d4b168`. Nenhuma D/F6, mudança vigente, merge ou aprovação de arquitetura A/B/C/P4-E/R.

## FEITO — seis novas fichas e duas frentes horizontais

| Ficha | Módulo/status | Objeto e origem | Risco preservado |
|---|---|---|---|
| CF-NOR-0039 | M14 A/H | segurança jurídica da transição, marcos de eficácia e investidura; pesquisa [PR #91](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/91) | **não** escolhe plebiscito R-CON1/2, transição TR-PROS/imediata, aplicação FED1/2/3, A/B/C ou validade de PEC concreta |
| CF-NOR-0040 | M00 G/H | legalidade/reserva de lei penal e tributária, limites do regulamento; dossiê M00.01 | **não** redefine espécies ou autoriza materialmente delegação irrestrita; compatibilidade com arts.59/62/68/84/150 PENDENTE |
| CF-NOR-0041 | M06 E/H de 0007 | **habeas data gratuito**, informação/retificação de dados; pesquisa [PR #62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62) e [PR #59](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/59) | **função legal de anotação Lei 9507 art. 7º III não transposta**; não igualar HD a dados privados ou MS |
| CF-NOR-0042 | M06 E/H de 0007 | **ação popular** e legitimidade de cidadão, isenção custas/sucumbência salvo má-fé, art5 LXXIII | não igualar ACP ou demais tutelas coletivas |
| CF-NOR-0043 | M09 A/H | **maternidade 120 dias**, estabilidade gestante até cinco meses pós-parto, paternidade sob lei/ADCT; pesquisa PR #63 | **paternidade: Lei 15.371/2026 publicada mas vigência somente 01/01/2027**, com 10 dias em 2027, 15 em 2028 e 20 em 2029 **sujeitos a condição fiscal**; 2026 cinco dias ADCT; texto H não transcreve mínimo provisório |
| CF-NOR-0044 | M09 E/H de 0027 | trabalho infantil vedado antes dos 16, aprendiz desde 14 e atividades noturnas/perigosas/insalubres vedadas antes dos 18 | proteção integral art227, educação, ECA/CLT e exceções legais ainda não examinadas |

[**Matriz de 24 controles positivos/parciais/ausentes**](CF_CC_008_MATRIZ_24_CONTROLES.csv) classifica as proteções e reservas, especialmente a correta cronologia de licença-paternidade (Lei 15.371/2026 arts.11,14). Não confundir lei publicada com direito cujo novo prazo já vigora.

## Distribuição modular do corpus H acumulado

| Módulo | H |
|---|---:|
| M00 | 1 |
| M01 | 18 |
| M02 | 0 |
| M03 | 0 |
| M04 | 1 |
| M05 | 1 |
| M06 | 4 |
| M07 | 1 |
| M08 | 2 |
| M09 | 5 |
| M10 | 2 |
| M11 | 3 |
| M12 | 1 |
| M13 | 1 |
| M14 | 1 |

**Soma: 41 H em 13/15 módulos**, mas não há percentual comprovado de equivalência material ao direito vigente. A lacuna horizontal restante de M02/M03 não justifica ratificar modelo de governo ou suprimir limitações eleitorais.

## Portas de não regressão e objeções centrais

1. **M14:** parecer M14.01.03 descreve datas diferentes de posse presidencial e instalação da Câmara após eleições de 2026. Consulta popular e exigibilidade de plebiscito para mudança de sistema seguem controversas; nenhuma norma H de transição pode virar competência de premier antes da investidura.
2. **M00:** legalidade geral + reserva penal/tributária não suprimem exceções de decretos constitucionais, medidas provisórias e competências próprias; a CLF não pode mudar a espécie/rito de normas apenas por consolidação editorial.
3. **M06:** houve ganho de habeas data, ação popular e gratuidades; restam assistência jurídica integral art5 LXXIV, duração/efetividade e instrumentos coletivos específicos, além de publicidade de dados/controle de terceiros, mesmo com CF-NOR-0033/0037 anteriores.
4. **M09:** patamares de maternidade, emprego, paternidade, proteção de jovens são texto H, não abrangem todos direitos sociais, previdência e infância; **Lei 15.371/2026 tem vigência diferida** e gatilho fiscal de 2029 que impede afirmar cronologia de 20 dias incondicional. Conferir regime doméstico, adoção, seguridade e benefícios atuais.
5. **CI:** GitHub Actions de PRs anteriores retornou jobs sem `steps` e logs `404 BlobNotFound`; a causa técnica continua sem prova. QA por leitura de fonte não substitui `python scripts/gerar_anteprojeto.py --check` nem `validar_repositorio.py`.

## FEITO / PENDENTE / PRÓXIMO

**FEITO:** seis fichas H, índice e compilado atualizados, 24 vínculos de proteção, inclusão de M00/M14 e verificação de legislação recente de paternidade. **PENDENTE:** confronto N:N CF/ADCT integral, documentação de todas leis setoriais, revisão jurídica independente, conflitos com PR #59 no índice/vista, execução do CI e escolha dos modelos. **PRÓXIMO CF-CC-009:** (i) recuperar M02 e começar protótipos constitucionais condicionais M03 quando sua via de edição estiver autorizada; (ii) completar assistência jurídica/gratuidades e parte dos direitos coletivos M06/M09; (iii) diagnostic CI com logs de ambiente/permissão/runner ou executar os três testes oficiais em ambiente próprio; (iv) entregar ao CLF mapa de reserva de lei x espécies x corpus com colisões de vigência concretas. Nenhum F6/D ou merge.
