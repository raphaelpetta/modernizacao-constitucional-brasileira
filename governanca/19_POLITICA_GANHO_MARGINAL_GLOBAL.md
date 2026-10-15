# CF-GOV-019 — Política global de ganho marginal, diversidade de frentes e suficiência da pesquisa

**Natureza:** regra **operacional e transversal** expressamente solicitada pelo usuário em 15/10/2026; registro decisório `CF-DEC-015` (D **apenas operacional**). **Aplica-se a:** M00–M14, F0–F8, coordenação, redação, auditorias, empilhamento de PRs, interface CF–CLF **apenas no lado CF**. **Não** ratifica regime de governo, direitos, cláusulas CF-NOR, políticas econômicas nem obriga o CLF, que é independente.

**Integração metodológica:** complementa o protocolo de pesquisa proporcional [CF-GOV-002](02_METODOLOGIA.md) e o de rodadas [CF-GOV-012](12_PROTOCOLO_RODADAS_E_SINCRONIZACAO.md). **Não substitui** os mecanismos de cobertura/risco ainda propostos no [PR #101](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/101) nem a fila e a central ainda propostas no [PR #104](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/104). Após integração desses PRs, reconciliar duplicações por **referência**, não por cópia de regras.

## 1. Princípio decisório: comparar o benefício ADICIONAL da próxima unidade de trabalho

Antes de cada nova rodada e antes de prolongar um subciclo, perguntar:

> **O que uma rodada adicional nesta frente acrescentaria de verificável ao texto, à proteção de direitos, à qualidade da decisão ou à capacidade de integração, comparado às melhores alternativas que poderíamos executar agora?**

**Ganho marginal** é a diferença entre o estado *efetivamente comprovado* do projeto e o resultado plausível de uma próxima atividade específica; não é a importância abstrata do tema, o volume de pesquisa acumulada, o número de páginas, de CF-NOR, de PRs ou de chamadas de ferramenta. O custo marginal compreende tempo, complexidade, riscos, retrabalho, saturação cognitiva e atraso de outras frentes. Não se trata de maximizar uma razão matemática fabricada.

**Critérios de benefício material:** (i) direito/garantia atual com destino auditado; (ii) função constitucional ainda descoberta ou pouco tratada; (iii) incompatibilidade/risco intermodular crítico resolvido; (iv) variante A/B/C tornada comparável; (v) decisão antes bloqueada tornada madura; (vi) cláusula H/teste/auditoria que efetivamente muda a capacidade de avaliar o produto; (vii) defeito técnico demonstrado corrigido. Repetição editorial, novo resumo e dado adicional que **não mudaria** entendimento, escolha ou proteção são ganhos baixos.

## 2. Preflight da CARTEIRA inteira — obrigatório, curto e concreto

Conferir `main` e SHAs, PRs concorrentes, `redacao/indice.csv`, fontes, quadro de coordenação e **as 2–4 rodadas mais recentes**. Examinar lacunas e dependências **em M00–M14**, sem presumir que um módulo esteja completo por ter uma H. Formular **ao menos três candidatas concorrentes de tarefa**, sempre que existirem:
1. **H — cobertura horizontal:** direito, competência, poder, regime transitório ou função de CF/1988/ADCT com cobertura ausente/incompleta;
2. **V — profundidade vertical útil:** revisão/adversarial de risco alto, norma H ou variante com critérios de saída;
3. **I — integração/coordenação:** resolver colisão, dívida de PR, contradição, falha de validação ou decisão desbloqueadora.

Para cada candidata, registrar sucintamente: **resultado novo verificável**, lacuna ou risco que reduz, **qual evidência concreta ainda falta e se poderia alterar conclusão**, dependências, esforço relativo (baixo/médio/alto), risco de dano se não trabalhada agora, confiabilidade da previsão e melhor objeção. Concluir com **uma escolha motivada e ao menos uma alternativa preterida**. Pode haver execução transversal de 2–3 frentes em uma rodada quando viável; jamais dividir trabalho igualmente por ritual.

**Sem pontuação fictícia:** os critérios são ordinais/qualitativos; não converter preferências em porcentagens, produtividade estimada ou dinheiro sem base. Escolher a opção de maior ganho líquido plausível **sujeita às garantias de direitos, à necessidade de evidência e aos bloqueios jurídicos reais**. Direitos fundamentais, casos R3, revisão crítica e obrigações legais não podem ser descartados porque sejam custosos.

## 3. Sinais de SATURAÇÃO e regra de troca de frente

Reavaliar e **presumir troca de subtema** quando ocorrer pelo menos um destes sinais:
- duas rodadas substantivas **consecutivas no mesmo núcleo** sem mudança relevante de redação, garantia, decisão, evidência que poderia mudar a conclusão ou desbloqueio;
- próxima entrega consiste essencialmente em mais referências, testes, planilhas ou pareceres para conclusão já suficientemente delimitada;
- esforço empírico elevado traria apenas um exemplo a mais sem resolver a lacuna decisória;
- o texto avançou em quantidade, mas a auditoria de cobertura constitucional continua com grandes lacunas em outras frentes;
- ciclos adicionais dependem de dados, revisão humana, autoridade ou decisão não disponíveis **na rodada**;
- CI/PR concorrente bloqueado: investigar o bastante para identificar o impedimento e abrir incidente, **prosseguindo em trabalho independente**, sem abandonar o dever de corrigir o bloqueio antes de integrar.

**Terceira rodada seguida no mesmo subtema:** somente com justificativa documentada de **benefício marginal superior às outras candidatas**, urgência ou risco grave concreto, prova decisiva identificável, dependência efetivamente bloqueadora ou oportunidade de fechamento; indicar critério de parada. A regra **não** impede continuidade quando necessário para proteger direitos ou evitar erro jurídico grave. Evitar alternância artificial que gere trabalho superficial.

Quando o ganho marginal for baixo: declarar **SUFICIENTE_NESTE_RECORTE**, **PAUSADO_POR_DEPENDENCIA** ou **EXIGE_DECISAO** e mover a pesquisa não decisiva à fila. Esses estados são gerenciais, **não** significam equivalência material, F6, D ou conclusão do módulo.

## 4. Custo de oportunidade e limite de trabalho em curso

Um novo dossiê/CF-NOR/PR só deve ser criado se tiver **produto distinguível** dos existentes e critério de aceitação definido; verificar alternativa de atualizar fonte anterior em vez de criar outro arquivo. A fila ativa deve permanecer pequena: **1–2 frentes com aprofundamento efetivo e eventual interface transversal**, salvo motivo concreto para ação simultânea. Pesquisas em espera não são frentes ativas.

Em cada rodada distribuir atenção entre **carteira constitucional** (M00–M14) e **recorte selecionado**. Cobertura global e profundidade de direitos são complementares; não equiparar número de módulos com normas ao percentual constitucional coberto. Dar preferência a lacunas de proteção grave e funções estruturantes quando a pesquisa atual já tem retornos decrescentes.

A prioridade de integração **não** se resolve por abrir cada vez mais PRs empilhados. Avaliar ganho de reconciliar/validar material existente versus acrescentar outro PR, com efeito na confiabilidade e uso futuro do texto.

## 5. Portas de suficiência e prova do benefício entregue

**Antes:** registrar no pacote ou PR, de forma breve: candidatas H/V/I, razão de escolha, ganhos esperados, custo relativo, evidência que mudaria decisão, critério de parada e última rodada do mesmo núcleo.

**Depois:** comparar promessa ao efetivamente obtido:
- **NOVO:** efeito adicional concreto (por exemplo, garantia rastreada, norma H, risco resolvido, fonte nova decisiva, PR desimpedido);
- **INCREMENTAL:** melhora justificável, mas não suficiente para repetir;
- **BAIXO/REDUNDANTE:** resultados não alteram a próxima decisão ou cobertura; declarar pausa, não continuar automaticamente;
- **BLOQUEADO:** dependência externa ou jurídica identificada; devolver à fila com condição de retomada.

O próximo passo deve comparar ao menos **uma candidata alternativa** e justificar por que retomar/rotacionar. Em pacote de continuidade: **FEITO / PENDENTE / GANHO MARGINAL (esperado × realizado) / PRÓXIMO / INTERFACES**, sem perder SHAs, CI, fontes, D/P/H/A/V e auditoria N:N.

## 6. Segurança contra o uso indevido da política

- **Não** trocar rigor por velocidade, omitir direitos, antecipar ratificação D, suprimir comparação essencial ou ignorar incerteza judicial de risco R3.
- **Não** exigir que todas as fases F0–F8 se encerrem em uma rodada; **não** fabricar dados, rankings quantitativos, ganhos fiscais ou percentuais globais.
- **Não** executar tarefas só para melhorar contagens de PRs, H, linhas ou tokens; nem transformar problema de CI sem diagnóstico em investigação infinita.
- **Não** implementar regras de priorização no CLF por simples interface; encaminhar proposta formal, se a independência exigir.
- **Não** supor que merge de governança aprova conteúdo constitucional: `CF-DEC-015` é **D operacional**, separada de qualquer escolha de mérito.
- Auditar criticamente a **própria regra** em cada mudança relevante: ela deve reduzir retrabalho e elevar valor do produto, não produzir relatórios ou métricas que consumam mais recursos do que poupam.

## 7. Exemplo de aplicação — rodada CF-CC-012 a CF-CC-015

As quatro rodadas sucessivas M05 (execução orçamentária, caixa, insuficiência e dados RGF) agregaram conhecimentos, mas após estabelecer a distinção autorização/caixa/cobertura legal, **o benefício de novos dados fiscais desagregados ficou condicionado** à obtenção de informação que altere o desenho constitucional. Desdobramento: **M05 em `PAUSADO_POR_DEPENDENCIA` no recorte caixa/LOA**, preservar dados/dossiê PRs #118–#119; não reduzir obrigação de rever legalidade e direitos antes de ratificação. A próxima carteira candidata preferencial compreende **M01 liberdades/garantias, M02/M03 direitos políticos/governo e M06 justiça/tutela**, com M14 como interface, sem afirmar ordem rígida para os próximos ciclos.

**Indicadores de êxito da política:** menos ciclos sem delta, mais funções/garantias com destino documentado, menos colisões/retrabalho, PRs consolidados, decisões tecnicamente maduras e clareza das pendências. **Não** medir apenas novos arquivos, H ou commits.

**Base de entrada verificada:** `main` `2a770a8136f8ca4877e865be3e3b7745a6d4b168`, ainda **20 H**; PR #119 é draft no stack e possui **45 H**, não integrado. Esta fotografia não substitui consulta dinâmica ao GitHub.
