# CF-NOR-0021 — Garantias na atuação e no procedimento administrativo

**Estado:** H — hipótese experimental, sem ratificação. **Tipo editorial:** G (garantia geral funcional). **Módulo:** M07.01. **Corte:** 15/10/2026. **Risco material:** R3. **Origem:** dossiê e 12 funções M07.01, PR draft #102 (não incorporado à main). **Rodada:** CF-CC-001, issue #103.

<!-- NORMA-INICIO -->
No exercício da função administrativa, o poder público assegurará atendimento acessível e não discriminatório, recepção e exame de petições e reclamações, informação adequada sobre procedimentos e decisões que afetem as pessoas interessadas e resposta fundamentada em prazo razoável, ressalvados os sigilos constitucionalmente legítimos e os direitos de terceiros.

Nos processos administrativos em que figurem litigantes ou acusados, são assegurados o contraditório e a ampla defesa, com os meios e recursos a eles inerentes. Nos demais procedimentos capazes de afetar direitos ou interesses juridicamente protegidos, será garantida oportunidade efetiva de ciência e manifestação compatível com a natureza do ato, sem prejuízo das garantias constitucionais especiais.

A adoção de meios digitais não poderá inviabilizar o exercício dos direitos de petição, informação e defesa, nem o acesso efetivo aos serviços públicos. Serão assegurados acessibilidade, apoio apropriado e canais alternativos adequados quando necessários ao exercício desses direitos, na forma da lei e observadas as competências federativas.

Este dispositivo não afasta o devido processo legal, a tutela jurisdicional, a proteção de dados pessoais, as garantias de publicidade e sigilo constitucionalmente aplicáveis, nem os mecanismos de controle da administração pública.
<!-- NORMA-FIM -->

## Fundamento, proveniência e limites

- **Direito vigente a confrontar:** CF/1988, arts. 5º, XXXIII, XXXIV, LIV, LV, LXXVIII e LXXIX; 37, caput e § 3º; 70, 74 e 175; direito a certidões (art. 5º, XXXIV, b) permanece pendência expressa, sem presunção de cobertura. A investigação da redação constitucional atual e da legislação está documentada no [M07.01 PR #102](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/102).
- **Legislação infraconstitucional de controle de efeitos:** Lei 9.784/1999, arts. 1º a 3º, 26, 50 e 69; Lei 14.129/2021, arts. 2º, 3º, 5º, 6º e 14; LGPD, arts. 6º e 23. Não transportar para o texto constitucional a abrangência federal dessas leis nem presumir adesão por outros entes.
- **Justificativa limitada da nova redação:** torna legível no M07 um piso administrativo e uma salvaguarda contra exclusão digital, já funcionalmente mapeados; **não comprova equivalência** à CF/1988 nem substitui disposições setoriais, remédios constitucionais ou hipóteses especiais.
- **Alternativas abertas:** H-A (garantias distribuídas, com deveres institucionais no M07) e H-B (direito autônomo à boa administração). O protótipo acima é **H-invariante experimental**, útil para comparar as duas, **não é escolha de H-A ou H-B**; a localização final também está aberta.
- **Melhor objeção:** o texto pode produzir duplicidade com o art. 5º e ampliar deveres administrativos com custos não quantificados, inclusive obrigação de canal alternativo, ou reduzir garantias ao diferenciar litigantes/acusados de demais interessados. Exige cotejo com M01/M04/M05/M06/M09/M12/M14, controle de prova e contraditório, custos e condições efetivas de acesso.

## Controles de continuidade de garantias — NÃO AUDITADOS COMO EQUIVALENTES

| Âncora vigente | Ponto candidato no texto H | Lacuna/risco ainda aberto |
|---|---|---|
| CF 5º XXXIII (informação) | primeiro parágrafo | extensão, limites e dever de acesso ainda parciais |
| CF 5º XXXIV a (petição) | primeiro e terceiro | independência de taxa e amplitude de titulares não expressas |
| CF 5º XXXIV b (certidões) | **sem correspondente específico** | exige destino expresso em M01/M07 |
| CF 5º LIV (devido processo) | segundo e quarto | procedimentos restritivos fora da hipótese litigiosa |
| CF 5º LV (contraditório e defesa) | segundo | alcance, prova, intimação e recurso concreto em revisão |
| CF 5º LXXVIII (duração razoável) | primeiro | não cobre expressamente todos os processos |
| CF 5º X e LXXIX (privacidade/dados) | primeiro e quarto | remissão, sem equivalência; ver PR #59 |
| CF 37 caput/§3º (administração/usuários) | primeiro e terceiro | princípios e participação não reconstruídos integralmente |
| CF 70/74 (controle) | quarto | controles financeiro e interno ainda sem novo destino |
| CDPD e acessibilidade | primeiro e terceiro | deveres específicos e ônus indevido não exauridos |

**Testes pendentes:** (1) intimação exclusivamente eletrônica de pessoa sem acesso; (2) dados sensíveis e sigilo de terceiros; (3) Município sem adesão à Lei 14.129/2021; (4) procedimento sancionador especial; (5) capacidade orçamentária para canal alternativo; (6) caso de petição e certidões; (7) urgência e contraditório posterior; (8) controle judicial/administrativo efetivo. Os casos são especificações de teste, **não resultados de validação**.

**Interface CLF:** T07 (procedimentos e especiais) e T43 (administração digital). Pedir concordância de âmbito, canais, intimações e efeitos sobre procedimento, **sem transpor texto automaticamente** nem modificar a decisão CLF DEC-016.

**Decisão substantiva:** nenhuma. **Auditoria jurídica independente:** pendente. **Efeito sobre fonte canônica:** uma nova ficha H indexada com ordem editorial 0230; a ordem não é numeração constitucional definitiva.
