# CF-CC-017 — Continuidade, ganho marginal e contraprovas M01/M02/M06

**Data de corte:** 15/10/2026. **Fonte de prioridade:** CF-GOV-019 integrada na `main` `7c3bd80470899a09e31f25a6a3a47d7c9cca669c`; **stack base:** [PR #122](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/122), HEAD `d8f730f01cf58e3106d35012ac71b39d38bf68ba`, 49 H nos 15 módulos. **Esta branch:** 51 H em 15 módulos. **Estado:** H/P/A/V, nenhum F6/D de mérito, nenhum merge; CLF independente.

## Preflight de ganho marginal: candidatas e oportunidade

| Categoria | Candidata | Ganho marginal esperado | Custo e risco | Decisão gerencial |
|---|---|---|---|---|
| Cobertura horizontal | **M01.14 — CF5 VI–VIII + art19I** | Proteger consciência/crença e escusa, antes desprotegidas na minuta experimental | Moderado / R3; exige direitos da pessoa vulnerável | **Executada**, H-0053 |
| Cobertura política | **M02 — CF17 partidos** | Complementar H-0051 sobre sufrágio e impedir perda de autonomia/controle | Moderado / R3; financiamento/fidelidade ainda em aberto | **Executada**, H-0054 |
| Arquitetura e decisão | **M06 — órgão de controle constitucional** | Reduzir risco de decisão não fundamentada sobre Corte apartada; criar critérios comparáveis J1/J2/J3 | Moderado / R3; não há F6 sobre Corte | **Executada como comparação, SEM nova H institucional** |
| Integração | Resolver CI #120, conciliar PRs #101/#104 e stack | Alto se eliminar bloqueio do merge, mas diagnóstico de anotações/runner inacessível nesta ferramenta | Alto esforço/risco de ciclo improdutivo | **Alternativa preterida**, permanece issue própria |
| Aprofundamento repetitivo | Nova rodada em M05/caixa e dados | Baixo sem prova capaz de inverter uma escolha constitucional | Alto custo empírico | **Não executada** |

**Saturação:** a CF-CC-016 também explorou M01/M02/M06, mas **a CF-CC-017 trata funções diferentes** (religião, organização partidária, arquitetura de Corte), com critérios explícitos de parada. A próxima rodada deve **comparar outras frentes**, por exemplo M04 competências, M07 administração e M13 fontes/direitos internacionais, antes de persistir neste trio sem ganho comprovável. Política CF-GOV-019 não é licença para reduzir proteção de direitos ou deixar função R3 sem exame.

## FEITO — delta real

1. **CF-NOR-0053** (`redacao/propostas/CF-NOR-0053.md`) M01 H/A: crença e não crença, cultos/liturgias, assistência religiosa voluntária em internação, escusa e prestação alternativa, neutralidade e colaboração estatal sem favorecimento arbitrário. Contraexemplos: STF ADI4439 ensino confessional **facultativo**, RE494601 ritos de matriz africana, Tema952 autonomia de paciente **adulto capaz** — não extrapolar.
2. **CF-NOR-0054** (`redacao/propostas/CF-NOR-0054.md`) M02 H/A: pluralismo, criação/autonomia dos partidos, transparência e tutela contra discriminação, proibição de organização paramilitar e financiamento/subordinação estrangeiros; **não escolhe fidelidade, coligações, fundo/propaganda, fórmula eleitoral nem órgão registrador**. STF ADI5081 diferencia perda de mandato majoritário e proporcional.
3. **M06 — J1/J2/J3:** `modulos/M06-justica/M06_CC017_TRES_ARQUITETURAS_CONTROLE_CONSTITUCIONAL_v0.1.md`: Supremo integrador, Corte Constitucional separada e câmara especializada com critérios idênticos; Alemanha 12 anos, Portugal 9, Espanha 9 **somente como comparação**; não importar mandato.
4. **Auditoria N:N e testes:** `auditoria/CF_CC_017_MATRIZ_24_GARANTIAS.csv` (**24 verificações**, nenhuma alegação de equivalência integral) e `auditoria/CF_CC_017_MATRIZ_18_TESTES.csv` (**18 casos**, 6 por M01/M02/M06).
5. **Texto de trabalho:** `redacao/indice.csv` acrescenta `0053 / 0520` e `0054 / 0530`, ambas H/A; `redacao/anteprojeto-de-trabalho.md` foi compilada por transcrição literal das fontes, agora **51 H em 15 módulos** na branch; `main` segue **20 H**.

## PENDENTE — auditorias materiais e CI

- **M01.14:** extensão exata da objeção de consciência, lei de prestação alternativa, efeitos na cidadania, tutela de incapacidades em internação, matriz laicidade versus parcerias legítimas, ensino religioso facultativo, imunidades, povos tradicionais, liberdade contra particulares.
- **M02:** CF17 caráter nacional, registro e forma da Justiça Eleitoral, §3 financiamento/propaganda e distribuição protetiva de candidaturas, disciplina/fidelidade segundo modo de eleição, participação de grupos sub-representados; CF14§§1–16 e CF15 ainda carentes.
- **M06:** J1/J2/J3 não são CF-NOR H nem alternativa material deliberada; órgão de cúpula, compatibilidade CNJ/MP/Defensoria, conflitos de competência, queixa constitucional, efeitos e transição ainda requerem desenho. Sem independência e garantias revisadas, não realizar F6.
- **Política integrada na main fora deste stack:** branch #122 e descendentes precedem a integração do CF-GOV-019. **Reconciliar a main** e os PRs concorrentes (#59, #101, #104, #105–#122) antes de qualquer integração, sem apagá-los. Não usar merge cego.
- **QA:** verificar o estado real do GitHub Actions deste HEAD; `python scripts/gerar_anteprojeto.py --check`, `scripts/validar_repositorio.py` e testes integrais em checkout fiel ainda não executados; issue #120 investiga falhas recorrentes sem logs/anotações visíveis. Auditoria por IA não substitui revisão jurídica independente.

## GANHO efetivo / próximo ciclo

**Esperado:** ampliar cobertura com duas garantias constitucionais e tornar a escolha J1/J2/J3 verificável sem decidir. **Obtido até a criação da documentação:** duas fontes H, duas matrizes e três arquiteturas com 8 invariantes; validação remota de índices/texto deve ser declarada com resultado separadamente, não presumida. **Classe de ganho:** `NOVO` em direitos/organização partidária e em comparação institucional; não maturidade plena nem direitos integralmente protegidos.

**Próximo por custo de oportunidade:** antes de aprofundar religião/partidos/justiça novamente, comparar **M04 federação e competências (horizontal)**, **M07 tutela da administração (vertical)**, **M13 hierarquia de tratados (integração)** e **resolução CI/PRs (operacional)**. Só retomar este trio por lacuna grave demonstrada ou etapa de fechamento com revisão independente. **Interfaces:** central CF #103, M01 #54, M02 #14, M06 #55, M14 #90, CI #120; CLF só se uma dependência material concreta surgir.
