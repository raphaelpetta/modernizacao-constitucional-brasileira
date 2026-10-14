# Quadro de coordenação das frentes — fotografia verificada

**ID:** CF-GOV-013 · **Atualização:** 14/10/2026 · **Main de referência:** `c82d41b8313c79a7c7b7d93b3a69269eb86a99c3`.  
**ATENÇÃO:** fotografia, **não estado em tempo real**. Antes de decidir/mesclar, ler o SHA atual e a situação das issues/PRs, especialmente `redacao/indice.csv`. A numeração CF-NOR abaixo é a dessa referência, não uma reserva para outro ciclo.

## 1. Regra de leitura

- **Integrado na main:** existe como arquivo versionado, **não** aprova materialmente conteúdo constitucional.
- **PR draft:** pesquisa ou proposta ainda não incorporada.
- **H/P/A/V:** hipóteses/propostas/questões/verificações; **D:** apenas diretriz ratificada segundo `03_DECISOES.md`.
- **Próximo:** uma atividade verificável, não mera intenção. A cada mudança relevante registrar no `14_REGISTRO_DAS_RODADAS.md` ou handoff.

## 2. Frentes, entregas e próximos atos

| Frente | Estado na fotografia | Entrega verificada | Próximo trabalho prioritário | Dependências |
|---|---|---|---|---|
| **M00 — Teoria/fontes** | pesquisa `main` | M00.01 reserva constitucional; M00.02 fontes e reservas; M00.03 redação integrada, geração, CI | Completar inventário por dispositivo e preparar decisões sobre lei, delegação e tratados | M03/M04/M06/M13/M14 |
| **M01 — Parte geral** | H em `main` | CF-NOR 0003–0007; regime geral e 16 garantias em piloto | Reconciliar PR22, não presumir cobertura dos remédios | M00/M06/M09 |
| **M01 — Igualdade** | H em `main` | CF-NOR 0008–0011, dossiê/matriz de 16 garantias | Conciliar com M01.06 no PR22, testar lacunas CDPD/leis | M06/M09/M11/M13 |
| **M01 — Vida e bioética** | H em `main`, ciclo M01.11 em andamento | CF-NOR 0012–0017; M01.10 matriz de 20; índice atual já inclui **0018–0020** capacidade/diretivas/involuntariedade | Terminar auditoria específica M01.11 e revisar impacto CDPD/saúde/justiça | M05/M06/M09/M12 |
| **M01 — Privacidade/dados** | pesquisa PR22, proposta conflitante PR45 | M01.08 (28 testes; 18 registros digitais); #45 antigo 0012/0013 já ocupados | **Não mesclar #45**; reconstruir com IDs livres sobre main atual ou preparar texto novo após reserva | M06/M07/M12 |
| **M01 — Liberdades civis** | pendência M01.12 (nome a reservar) | lacunas identificadas pela auditoria transversal M01.09 | Abrir dossiê próprio sobre expressão, consciência, religião, informação, reunião, associação e circulação | M02/M06/M08/M12 |
| **M02 — Eleições** | planejado; issue #14 | salvaguardas preliminares M00 | Dossiê M02.01 sobre integridade e restrições oportunistas antes de fórmulas eleitorais | M03/M06/M14 |
| **M03 — Parlamento e governo** | pesquisa; issue #18 | M03.01 processo legislativo, 12 testes, 10 triagens | Cruzar iniciativa/veto com modelos CLF e camadas normativas M00 | M00/M04/M05/M14 |
| **M04 — Federação** | pesquisa; issue #21 | M04.01 participação territorial e tipos T0–T3, 12 testes/10 triagens | Confrontar competências e objeções com M03/M05, sem aprovar Câmara alta | M03/M05/M07/M14 |
| **M05 — Finanças** | pesquisa; issues #25/#29 | M05.01 encargo/equalização; M05.02 10 fontes, validador e testes sintéticos | Coletar, harmonizar e validar dados fiscais reais por município-ano antes de conclusão empírica | M04/M09/M05 |
| **M06 — Justiça e tutela** | sem dossiê próprio integrado | dependências e proteções processuais inventariadas em M01 | Abrir M06.01: remédios constitucionais, tutela coletiva, processo/controle constitucional e legalidade penal em interfaces | M01/M12/M13 |
| **M07 — Administração** | planejado | interfaces digitais, fiscais e CLF | Abrir estudo de boa administração e decisões administrativas/digitais; integrar CF-IC-001 | M01/M04/M06/CLF |
| **M08 — Economia** | planejado | direitos propriedade/mercado em matrizes M01 | Abrir pesquisa de propriedade, função social e prestação privada de serviços | M01/M04/M09 |
| **M09 — Direitos sociais e trabalho** | sem dossiê próprio integrado | garantias sociais/financiamento identificados M01/M05 | Abrir M09.01: mapa material arts. 6º–11 e 194–230, fontes de custeio e direitos exigíveis | M01/M04/M05/M06 |
| **M10 — Ambiente** | planejado | direito intergeracional listado | M10.01 ambiente/clima e deveres dos poderes e privados | M04/M08/M11 |
| **M11 — Povos** | planejado | direitos territoriais/capacidade coletiva inventariados | M11.01 proteção originária, consulta, autonomia e tutela | M01/M04/M06/M10 |
| **M12 — Segurança/emergência** | planejado | reservas de polícia e prisão inventariadas | M12.01 liberdade e força, necessidade, emergência e controle | M01/M06/M14 |
| **M13 — Internacional** | planejado | hierarquia e CDPD em estudos M00/M01 | M13.01 tratados, recepção, hierarquia e controle | M00/M01/M14 |
| **M14 — Reforma/transição** | planejado | efeitos ADCT/recepção já identificados | M14.01 proteção de direitos, reforma e etapas de implementação | todos |
| **CF ↔ CLF** | interface documentada `main` | CF-IC-001: Lei 9784 e devido processo; CLF T01.M04/T07.M03 | Triagem bilateral por competência, veto, processos e alcance territorial, sem transformar hipótese legal em CF decidida | M00/M03/M04/M06/M07/M14 |

## 3. Repositórios/PRs em coordenação

- **CF:** https://github.com/raphaelpetta/modernizacao-constitucional-brasileira .
- **CLF:** https://github.com/raphaelpetta/codigo-legislacao-federal .
- **#19 CF:** PR draft com dois arquivos iniciais de M01.01 em base antiga. **Supersessão de escopo provável, não equivalência documental comprovada**; preservar pesquisa útil antes de encerrar.
- **#22 CF:** PR draft, 29 arquivos de pesquisa M01.01–M01.09; contém protocolo de comparações e 96 conjuntos em fotografia **anterior às H 0008–0020**; revisão incremental necessária.
- **#45 CF:** PR draft de privacidade/dados com IDs **0012–0013 já utilizados na main**. **BLOQUEADO PARA MERGE**; original deve ficar registrado, recriação sobre `main` com ID próprio.
- **#44 CF:** fechado sem merge por primeira colisão de numeração.
- **M01.10 #43 e M01.11 #47:** frentes já identificadas, não reutilizar seus nomes para liberdades civis.
- **M06/M09:** sem issues dedicadas na fotografia, abertura prioritária com escopo cruzado.

## 4. Conflitos de interface que exigem uma só decisão

| Dúvida | Módulo de condução | Revisores funcionais | Bloqueia o quê |
|---|---|---|---|
| Reservas de lei e delegação | M00 | M03/M06/M13 | reservas substantivas de poderes e direitos |
| Liberdades e legalidade penal | M01 + M12 | M06 | restrições, sanções e garantias especiais |
| Remédios judiciais | M06 | M01/M09/M11 | afirmar equivalência de tutela geral |
| Proteção digital e fiscalização | M01 (direito) / M07 (autoridade) | M06/M08/M12 | aprovar CF-NOR proteção de dados completo |
| Encargos, competência e receita | M04/M05 | M03/M09 | definir distribuição fiscal |
| Prestação social sem fonte | M09/M05 | M04/M06 | concluir execução e exigibilidade |
| Mudança da CF com CLF | M00/M03/M14 | CLF T01.M04/T07.M03 | alterar vigência e revogação |
| Propostas repetidas e IDs | coordenação M00.03 | todos autores afetados | qualquer merge editorial colidente |

## 5. Decisões e qualidade

Nenhuma norma `CF-NOR-0001–0020` da fotografia recebeu status `D`. O registro de decisões mantém diretrizes gerais e as decisões históricas do guia com proveniência diferenciada. Não deliberar forma de governo, eleições, Câmara alta, Justiça ou tributação apenas porque estudos já existem.

**Próxima atualização deste quadro:** após saneamento de PR #45 e abertura M06/M09, ou quando a main mudar estruturalmente. Toda nova rodada deve fazer handoff mesmo se este quadro ainda não tiver sido editado.
