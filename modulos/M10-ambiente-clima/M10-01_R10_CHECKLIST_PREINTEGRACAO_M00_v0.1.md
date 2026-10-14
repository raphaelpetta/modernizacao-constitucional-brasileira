# M10.01-R10 — Checklist de pré-integração M00.03 e revisão jurídica cruzada

**Identificador:** CF-M10.01-S010-QA · **Data de corte:** 14/10/2026 · **PR:** #89 (draft).  
**Status:** checklist prospectivo e conferência documental, **NÃO AUTORIZA INTEGRAÇÃO**. Os seis documentos `R10_FICHA_F01–F06` são questões **A/V**, não decisões D. Os trechos da R9 A/B são H de pesquisa **fora da `redacao/`**.

## G0 — Inventário e identidades

- [x] Main lida na abertura: `2a770a8136f8ca4877e865be3e3b7745a6d4b168`.
- [x] PR89 draft lido, HEAD de entrada `f1d34b0aa05a1d22bb7d71d2c9b4d82038c907d9`; issue #88 aberta.
- [x] Verificados outros PRs abertos: #22 (M01 pesquisa), #59 (M01.13 H), #62 (M06 pesquisa), #63, #82 (M12 prova digital), #85. Nenhuma entrega nesses PRs foi tratada como revisão ambiental independente.
- [x] `M10-01_R9_ESBOCO_A/B`, matriz NN e testes R9 servem de baseline editorial.
- [ ] Novo preflight de `main`, catálogo, registro de reservas e `redacao/indice.csv` **se e quando houver decisão de avançar F7**; não feito como pedido de reserva nesta R10.
- [ ] Confirmar proprietários/revisores funcionais e suas respostas sobre as perguntas discriminadas da R7; apontá-los por escopo não equivale a manifestação recebida.

## G1 — Fonte oficial e vigência

- [x] CF compilada arts.5,23,24,30,129,145,170,186,216,225,231.
- [x] LC140 arts7–9,13–17 e STF ADI4757 sobre supletividade.
- [x] Lei7347/1985 compilada e distinção constitucional de ação popular.
- [x] Lei15300 art4 §§1–2 (EIA/Rima LAE, audiência versus consulta devida).
- [x] EC132 arts1/3/4/22/23 e fases programadas 2027/2033.
- [ ] Determinar último andamento e eventual decisão no mérito/cautelar em ADIs7913/7916/7919 e ADC102, em fonte processual primária acessível **no corte**. Incluir número, relator, órgão, data, dispositivo e efeitos. Pauta de 12/08/2026 **não** certifica decisão.
- [ ] Acórdãos inteiros e regime convencional aplicável, inclusive posição jurídica da OIT169 em M13, antes de afirmar hierarquia.

## G2 — Conteúdo textual e remissões

| Tema R10 | Item sem encerramento | Critério de prova |
|---|---|---|
| F01 direito intergeracional | A/B direito comum ≠ remédio temporal demonstrado | Titular, devedor, fato, prazo, legitimação e tutela |
| F02 EIA | Texto contém gatilho do EIA, mas tutela/participação incompletas | EIA prévio, publicidade, órgão competente e remédio |
| F03 Federação | A/B resumem competências sem corpo completo M04 | Quem legisla/licencia/fiscaliza, cooperação, supletividade |
| F04 Tutela | B02 e B08 possivelmente duplicam CF-NOR0007 H | ACP/popular diferentes, custos, prova, urgência e execução |
| F05 Povos | Consulta em A/B é remissão sem parecer M11/M13 | Titulares, incidência, participação, representação, controle |
| F06 Especiais | A-RES/B-RES não são artigos ou normas válidas | Regra específica, efeito, data, local, remédio e transição |

**Teste de falhas obrigatórias:** nenhum `CF-NOR` deve apontar a um identificador `A-RES`/`B-RES` em substituição de texto promulgável; não declarar ausência de matéria porque ela ainda não foi redigida; não transpor LC140/Lei15190 como CF vigente automaticamente.

## G3 — Decisão explícita

- [ ] Para cada F01–F06, registrar fonte da decisão, data, alternativas efetivamente consideradas, alcance, ressalvas, efeitos, autor da ratificação e impactos em módulos.
- [ ] Escolha A/B editoriais, se feita, não decide automaticamente política climática, competências, consulta ou regras especiais.
- [ ] Não converter `CF-DEC-004` D(guia) (sustentabilidade/gerações futuras) em aprovação de `A-TEXTO` ou `B-TEXTO`.
- [ ] Nenhum dos rótulos `F01-0` etc é CF-DEC; as alternativas permanecem H/A/V.

## G4 — Reserva, equivalência e redação F7

- [ ] Após decisão F6, consultar registro `CF-GOV-015`, `redacao/indice.csv`, fichas H vigentes e PRs de redação contemporâneos.
- [ ] Reservar IDs antes de criar CF-NOR, com especialidade G/E/A documentada e fundamento de remissão.
- [ ] Construir equivalência `CF vigente → texto novo literal → competência → lei residual → titular → remédio → transição`; quando falhar, explicitar **alteração material** e sua deliberação, não rotular como mera correção editorial.
- [ ] Testar inafastabilidade, tutela ACP/popular, preservação de EIA, direitos originários, supletividade e incidência da EC132.

## G5 — QA, integração e governança

- [x] Registro presente exclusivamente em `modulos/M10-ambiente-clima` na branch de pesquisa.
- [ ] Verificar CI estrutural associado ao HEAD **final desta R10** após último arquivo.
- [ ] Confirmar que `main` não foi alterada; PR89 permanece em draft.
- [ ] Revisão jurídica independente dos responsáveis nos módulos pertinentes; CI verde não certifica conteúdo jurídico.
- [ ] Qualquer merge, alteração no CLF ou criação de norma canônica requer ato próprio posterior; **não executar automaticamente**.

## Escopo de risco e continuidade

A ausência de `CF-NOR` M10 candidata significa que as fichas R10 são **pré-deliberações**, não demonstração de preservação ou regressão. O R10 torna os problemas documentais localizáveis mas não decide se/como mudar direitos e competências constitucionais.

**Próxima atividade executável (R11):** quadro comparativo de respostas efetivamente existentes às seis fichas, preenchido por fonte GitHub/parecer do responsável, e auditoria das reservas especiais por cláusula. Se não houver pareceres externos, produzir notas de pendência fundamentadas, **sem criar novas matrizes extensas apenas para reiterar as mesmas lacunas**.
