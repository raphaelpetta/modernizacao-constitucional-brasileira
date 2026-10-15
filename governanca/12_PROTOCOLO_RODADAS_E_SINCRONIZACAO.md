# Protocolo obrigatório de rodadas, reconciliação e coordenação

**ID:** CF-GOV-012 · **Implantação:** 14/10/2026 · **Natureza:** regra operacional de projeto expressamente solicitada pelo usuário. **Não** é deliberação constitucional material (`CF-DEC` sobre conteúdo).  
**Aplica-se a:** TODAS as frentes M00–M14, pesquisas transversais, redação F7, integração CF–CLF e gestão de PRs. Complementa `02_METODOLOGIA.md`, `06_CONTINUIDADE_VERSIONAMENTO.md`, `11_TECNICA_DE_REDACAO_E_INTEGRACAO.md`.

## 1. Regra permanente: cada trabalho gera prestação de contas e próximo passo

**Após cada rodada com trabalho substantivo, antes de declará-la concluída, registrar no mesmo ciclo:**

1. **Base verificada:** repositório, `main` SHA de entrada, SHA de saída (se houve integração), branch, issue, PR; data de corte e fontes efetivamente consultadas, incluindo CLF se pertinente.
2. **Feito:** entregas efetivamente criadas/alteradas, links e IDs estáveis, conclusões jurídicas com grau de confiança, divergências e efeitos concretos. Distinguir **pesquisado**, **redigido H**, **integrado à main**, **deliberado D** e **implementado no direito vigente** — coisas distintas.
3. **Não feito ou não confirmado:** trabalho que falta, decisões e auditorias materiais pendentes, incerteza de fontes, conflitos de branch ou reserva, testes ainda em curso e dependências externas; nunca dizer "tudo pronto" sem comprovação.
4. **O que sugerimos fazer depois:** **uma próxima tarefa prioritária, executável**, identificada por questão/issue, seus insumos e critérios de saída; outras tarefas em fila separada, sem invadir módulo de outra frente.
5. **Coordenação:** demandas a outros módulos e ao CLF, alterações de interface, documentos potencialmente duplicados, decisões que só o usuário pode ratificar.
6. **QA:** status real do GitHub Actions (SHA e resultado), conflitos, scripts específicos usados, e o que cada teste NÃO valida.

A síntese visível ao usuário deve conter, de modo inteligível, **Concluído / Pendente / Próximo passo**, sem depender de leitura do repositório. Se nada tiver sido gravado, declarar isso e indicar o motivo.

## 2. Registro persistente e fontes

- **Fonte documental**: `main` no GitHub, após merge; branches/PRs são propostas ainda não integradas.
- **Fonte normativa experimental única:** `redacao/propostas/CF-NOR-*.md` + `redacao/indice.csv`; o anteprojeto derivado só é alterado pelo gerador. Nunca copiar a minuta para documento concorrente.
- **Por rodada:** pacote `modulos/<modulo>/<subciclo>_PACOTE_CONTINUIDADE*.md` ou documento equivalente do módulo, conforme `modelos/PACOTE_CONTINUIDADE.md`, no MESMO branch/PR que a pesquisa. Para atividades sem módulo, `governanca/14_REGISTRO_DAS_RODADAS.md` e issue de coordenação.
- **Painel transversal:** `governanca/13_QUADRO_DE_COORDENACAO.md` é **fotografia datada**, não mecanismo automático de sincronização. Atualizá-lo quando houver nova frente, mudança relevante de fase, colisão de ID, PR de integração, conclusão ou impedimento crítico. Evitar reescrever inteiro a cada alteração trivial.
- **Índice e reservas:** `governanca/15_REGISTRO_RESERVAS_IDS.md` e `redacao/indice.csv` devem ser lidos ANTES de reservar `CF-NOR` ou novos subciclos.
- **Decisões:** somente `governanca/03_DECISOES.md`, com origem explícita. Merge de pesquisa, CI verde ou texto H não é aprovação D.

## 3. Preflight antes de trabalhar

A. Conferir SHA atual da `main`, PRs abertos relevantes, issues e o índice `CF-NOR`, além de `04_ESTADO_ATUAL.md` e este protocolo. Se outro módulo avançou, atualizar baseline.  
B. Identificar tarefa e escolher **um** responsável funcional, com consultas/interdependências; evitar dois subciclos diferentes com mesmo código.  
C. Antes de propor ID, buscar **também PRs de redação abertos**. Não reservar apenas por consulta à main: branches concorrentes podem conter a mesma sequência. Conflito: **interromper integração de redação**, arquivar/fechar PR colidente se necessário e recriar branch com ID livre/registrado, nunca sobrescrever fonte canônica.  
D. Verificar se a pergunta já foi pesquisada por outro PR. Para duplicação: registrar concordância, preservar fontes singulares e consolidar, sem merge cego ou descartar pesquisa útil.  
E. Congelar o escopo e definir critério de saída (dossiê, matriz, norma H, análise empírica ou decisão solicitada ao usuário). Não presumir autorização de ratificação.

## 4. Durante trabalho e encerramento

- Cada rodada gera **DELTA**: arquivos alterados e questões novas; *não* repetir pesquisas já feitas sem justificativa.
- Referenciar fontes oficiais atuais; criar testes adversariais proporcionais ao risco. Para fatos empíricos separar dado oficial, cenário ilustrativo e inferência.
- Rastrear N:N CF/1988 ↔ proposta ↔ direitos/garantias ↔ interfaces; preservação material exige prova, não similaridade de texto.
- Se `main` mudar antes de integrar, comparar IDs, alterações e PRs novamente; rebase/recriar se necessário, não forçar merge.
- Concluir com pacote contendo **FEITO / PENDENTE / PRÓXIMO / RESPONSÁVEL-INTERFACES / SHAs**, e atualizar painel conforme gatilho do item 2.
- Em PR, descrever explicitamente estes campos. **PR em draft** é estado esperado até revisão. Desmarcar draft ou merge somente após testes, reconciliação e autorização aplicável; nenhuma cláusula sobe de H para D sem ratificação material.

## 5. Regras de impedimento

1. **Colisão de IDs** (na main ou PR): bloquear PR editorial e realocar; conservar rastreabilidade do original.
2. **Dependência institucional aberta:** não afirmar redação constitucional materialmente completa; registrar pergunta a M06/M07/M09/M12 conforme função.
3. **Conflito ou fonte superada:** não forçar merge, atualizar histórico e próximo ato.
4. **Sem fonte oficial adequada:** estado V, pesquisa complementar especificada; proibir linguagem de certeza.
5. **Pacote ausente:** rodada não considerada documentalmente encerrada (a conversa pode terminar, mas fica pendência explícita).
6. **CLF:** cooperação por nota/issue versionada, nunca sincronização implícita ou cópia de legislação sem teste de alcance.

## 6. Critérios de aceitação de uma rodada

É considerada **documentalmente fechada** quando o pacote versionado informa base/saída, entrega e status, ao menos uma pendência ou afirmação comprovável de nenhuma, um próximo passo identificável, interfaces e QA. Isso **não** representa conclusão do módulo, decisão constitucional D ou mérito jurídico certificado.

## 6A. Porta de priorização e de encerramento por GANHO MARGINAL

Aplicar, antes do preflight de qualquer matéria e antes de uma terceira rodada consecutiva no mesmo núcleo, a **[CF-GOV-019](19_POLITICA_GANHO_MARGINAL_GLOBAL.md)**. A tarefa escolhida precisa ser comparada com pelo menos uma alternativa preterida; idealmente examinar três classes candidatas: lacuna horizontal, ganho vertical e integração. Registrar expectativa de incremento verificável, custo relativo, risco se não agir, incerteza que poderia mudar o resultado e ponto de parada. **Ao encerrar**, confrontar ganho prometido e obtido, e classificar `NOVO`, `INCREMENTAL`, `BAIXO/REDUNDANTE` ou `BLOQUEADO`, sem criar indicadores numéricos artificiais.

Duas rodadas no mesmo núcleo exigem reavaliação explícita. Terceira rodada seguida só por exceção documentada de risco relevante, prova decisiva, oportunidade de conclusão ou dependência crítica; a regra não afasta pesquisa indispensável a direitos nem produz rotatividade automática de temas. Registrar `SUFICIENTE_NESTE_RECORTE` / `PAUSADO_POR_DEPENDENCIA` / `EXIGE_DECISAO` quando pertinente, **sem confundir com F6/D ou com cobertura integral**. O [modelo de handoff](../modelos/PACOTE_CONTINUIDADE.md) inclui porta específica.

## 7. Aplicação à situação atual

- `CF-NOR-0001…0020` constam na `main` consultada no início da coordenação, todos H; **aumenta conforme trabalhos paralelos**, nunca usar o número sem refazer consulta.
- PR #22: pesquisa M01.01–M01.09 ainda draft; #19: catálogo M01 inicial duplicado em escopo (conferir singularidades); #45: redação privacidade/dados usava IDs 0012–0013 **já ocupados em main por dignidade/vida**. Bloquear merge deste PR e realocar ou retornar à pesquisa.
- M01.11 já foi ocupado por capacidade/diretivas/saúde; liberdade de expressão, consciência e religião precisa ID não colidente (M01.12 candidato).
- As frentes M06/M09 demandam abertura própria; M03/M04/M05 devem validar interfaces com M02 e com finanças reais. Nenhum percentual de desenvolvimento deve ser tomado como medição objetiva.

**Esta regra é procedimental e transversal; não cria obrigações jurídicas constitucionais nem substitui autorização sobre o mérito.**
