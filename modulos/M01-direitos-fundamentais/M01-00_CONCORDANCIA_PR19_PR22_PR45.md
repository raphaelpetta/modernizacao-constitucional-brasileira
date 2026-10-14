# Concordância e saneamento dos trabalhos M01 — PR #19, #22, #45 e main

**ID:** CF-M01-CORD-001 · **Data:** 14/10/2026 · **Main de referência ao iniciar:** `d06921663eb3df5e00385968d3a6d4357c86a467`.  
**Natureza:** auditoria documental de proveniência, sem revisão exaustiva de mérito jurídico ou ratificação constitucional.  
**Fonte:** [PR #19](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/19), [PR #22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22), [PR #45 arquivado](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/45), `main` M01.07/M01.09/M01.10/M01.11.

## 1. Por que dois catálogos iniciais não devem ser mesclados cegamente

**PR #19 (antigo, 2 arquivos):** 
- `M01-01_CATALOGO_E_REGIME_GERAL_v0.1.md`: **16.590 caracteres**, roteiro funcional amplo e comparativo, proposta inicial de grupos, menções a OECD, ADPF 347, jurisprudência de união homoafetiva e OC-32/2025 e testes.
- `M01-01_PACOTE_CONTINUIDADE.md`: 2.593 caracteres, próximos passos de inventário, hierarquia, história, alternativas, garantias e integração.
- Ambos se referem ao **mesmo baseline `6e91df55...` e mesmo código de sessão `CF-M01-S001`** utilizado também no começo do PR #22; mantê-los juntos como catálogos principais gera ambiguidade de fonte.

**PR #22 (mais amplo, 29 arquivos, ainda draft):** pesquisa M01.01–M01.09, com novo dossiê M01.01 e matriz de **38 grupos iniciais**, aprofundamentos sucessivos M01.02–08 e matriz transversal de **96 conjuntos** na fotografia do piloto inicial de cinco normas H. Não foi feita auditoria jurídico-documental que certifique que toda frase, fonte ou hipótese do PR #19 esteja reproduzida; logo, a substituição é de **função editorial**, não equivalência literal/jurídica.

**Decisão documental de coordenação:** preservar INTEGRALMENTE os dois textos do PR #19 em `referencias/pesquisas-arquivadas/` com cabeçalho de proveniência e tornar PR #22 **único candidato corrente de pesquisa acumulada M01.01–M01.09**, após revisão jurídica. O arquivo arquivado é acessível mas **não é dossiê ativo ou deliberação D**.

## 2. Pontos de confronto de conteúdo (ainda V)

| Tema | PR19 | PR22/main | Encaminhamento |
|---|---|---|---|
| Catálogo vigente | rol indicativo de arts.1–5, 6–11 e 194–232; 16 grupos funcionais | PR22 matriz inicial 38 grupos + 96 grupos transversais | Usar PR22 como roteiro ativo; nenhuma exaustividade demonstrada |
| Direito comparado | Portugal, África do Sul, UE, OECD e Corte IDH | PR22 soma Alemanha, Canadá, sistemas ONU e outros, com limites | OECD e OC-32/2025 no PR19 mantidas como pistas, verificar fontes e autoridade antes de usar |
| Jurisprudência | ADI 4277/ADPF132, Tema 698, ADPF347 | estudos M01.01–09, parte julgados de novo | ADPF347 e tutela estrutural devem ser especificamente auditadas em M06/M12 |
| Titularidade e limites | questões iniciais de horizontalidade | M01.02–04 e `CF-NOR-0003–0007` H na main | Confrontar direitos coletivos existentes, proibições absolutas e reservas especiais |
| Igualdade | hipótese geral | M01.06 PR22 e `CF-NOR-0008–0011` H na main | Redação não comprova equivalência CDPD e garantia penal |
| Integridade/bioética | dossiê inicial genérico | M01.05/.07 PR22 e `CF-NOR-0012–0020` H na main da fotografia | M01.11 trata de capacidade/medidas involuntárias; controvérsias abertas |
| Privacidade/dados | roteiro sem cláusula própria | M01.08 PR22; PR45 colidiu ID 0012/0013 | **Não mergear PR45**; reconstruir em M01.13 issue #57 com IDs livres |
| Expressão/reunião/liberdade | componentes em catálogos | matriz M01.09 identifica lacunas | Issue #54 M01.12 dedicada |
| Justiça/remédios | previsto em interface | CF-NOR-0007 H genérico; PR22 testes | Issue #55 M06.01, garantias específicas a desenvolver |
| Sociais | arts.6–11 e garantias setoriais | PR22 matriz transversal e M05 | Issue #56 M09.01; custeio e competência M05/M04 |

## 3. Colisões e vocabulário controlado

- `M01.07-PESQUISA` designa autonomia e bioética no PR22; `M01.07-REDACAO` designa piloto do regime geral já na main — **não são o mesmo dossiê**.
- `M01.09-PESQUISA` designa a auditoria transversal 96 grupos no PR22; `M01.09-REDACAO` designa igualdade na main (16 testes). Usar sempre sufixo funcional quando houver ambiguidade, sem reescrever os documentos históricos.
- PR45 atribuiu `CF-NOR-0012/0013` a privacidade/dados enquanto a main os reservou a **dignidade/vida**. Fechado sem merge; novo trabalho issue #57.
- O índice `redacao/indice.csv`, a [reserva de IDs](../../governanca/15_REGISTRO_RESERVAS_IDS.md) e os PRs abertos precisam ser relidos em cada nova rodada.
- **PR19** pode ser fechado *somente depois* que o arquivo histórico estiver preservado na main; fechar não revoga nem aprova pesquisas.

## 4. Critérios objetivos para PR #22

- [ ] Verificar inexistência de colisão de caminhos no estado atualizado de `main` e integridade do CI.
- [ ] Incluir no pacote final de PR22 nota de que `M01.07`/`M01.09` possuem dupla função histórica e versões da main.
- [ ] Auditar **fontes jurídicas críticas** (STF, leis posteriores 2025/26, CDPD, dados empíricos) antes de considerar o PR22 materialmente consolidado.
- [ ] Verificar que nenhum protótipo do PR22 é confundido com `CF-NOR` D.
- [ ] Atualizar mapa de cobertura segundo `CF-NOR` realmente presentes **na main de fechamento**, não tomar matriz antiga de cinco cláusulas como estado atual.
- [ ] Requisitar interfaces M06/M07/M09/M11/M12/M13 onde ainda não há estudo próprio.
- [ ] Ao integrar arquivos de pesquisa, manter `redacao/` e `governanca/` mais recentes; não substituir com versões antigas.
- [ ] Separar resultado CI estrutural de revisão material.

## 5. Feito / pendente / próximo

**FEITO:** documentos do PR #19 arquivados com proveniência; confronto de escopos e fontes; colisão do PR45 documentada e bloqueada.  
**PENDENTE:** auditoria jurídica do conjunto PR22, atualização incremental da matriz N:N, deliberação material e nova redação de privacidade/dados após reserva.  
**PRÓXIMO:** sanear os estados dos PRs após merge deste documento; realizar revisão de PR22 por ciclos e elaborar matriz de concordância com as normas H atuais antes de integração.  
**Interfaces:** M01 ↔ M00, M06, M07, M09, M11, M12, M13 e CLF.
