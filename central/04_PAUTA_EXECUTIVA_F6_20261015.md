# CF-CC-026 — Funil executivo F6: uma escolha de prioridade apresentável, nove portas ainda abertas

**Situação:** coordenação operacional/triagem **F5 → pauta possível**, não decisão F6 efetivamente tomada, não CF-DEC de mérito e **não redação constitucional**. Corte em 15/10/2026. **Base de trabalho:** `main` `866665bbfc84c0b37167cbdb8ef88e013a733287` (20 H). **Pilha de pesquisa:** [#124](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/124) (54 H), [#129](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/129) (interfaces R3), [#130](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/130) (reforma/Parlamento), [#107](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/107) (16 protótipos A/B/C), [#99](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/99) (pauta F6-00 já elaborada). **Não** reproduzir no repositório `main` os 54 textos H sem validação e reconciliação.

## 1. Ganho marginal — por que um funil e não mais pesquisa genérica

| Alternativa de trabalho | Potencial incremental | Custo/risco | Resultado |
|---|---|---|---|
| **H — outra norma H** sobre rigidez/Parlamento | Baixo neste instante: art.60§4 e quatro competências são lacunas documentadas, mas modelos de governo/órgãos permanecem não escolhidos | Alto R3; risco de redação contraditória | **Rejeitada por ora** |
| **V — decidir algo com evidência já reunida** | Alto para a **preferência de prototipagem** A/B/C, porque a [pauta já existe no PR #99](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/99); mais pesquisa A/B/C sem decisão de foco arrisca saturação | Baixo para P; alto para D institucional | **Selecionada somente para colocar P em condições de apresentação futura**, não para aprovação |
| **I — ordenar dependências e concentrar validação** | Alto: impedir ratificação cruzada indevida, reabrir PRs paralelos sem nova prova e reduzir divergência entre 20 H na main e 54 em rascunho | Moderado, artefato documental reversível | **Executada**: [funil CSV](04_FUNIL_DECISOES_F6.csv) de 10 recortes |
| **CI/runner** | Elevado se surgirem permissões/anotações, mas atualmente nenhum acesso novo; repetir as mesmas chamadas não entrega resultado | Redundância comprovada na [#120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120) | **Pausada por dependência, sem alegar falha de Python** |

Não atribuir pontuação numérica falsa de ganho ou percentuais de completude. A produtividade aqui é **diminuir o número de perguntas prematuras**, não obter 10 decisões.

## 2. A única escolha que pode ser submetida AGORA, se houver decisão específica: F6-00 **P**, não D

A [pauta original](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/99) distingue a escolha revisável de **prioridade de prototipagem (P)** da adoção constitucional (**D**). Não duplicar sua análise: ela já compara responsabilidade política, investidura, LOA, dissolução, defesa, voto e transição.

**Pergunta de escopo estrito para manifestação futura inequívoca:** *Qual arquitetura recebe a primeira minuta de Governo com contraprova obrigatória e análise R3 das interfaces, sem adoção constitucional?*

| Resposta admissível | Efeito operacional após manifestação explícita | O que NÃO produz |
|---|---|---|
| **P-A** | Priorizar presidencialismo reformado, com B como contraprova | Não aprova Presidente, poderes ou mandatos |
| **P-B** — recomendação técnica preexistente do PR #99 | Priorizar parlamentarismo racionalizado, com A como contraprova adversarial e C como alternativa sob prova | **Não** aprova parlamentarismo, eleição indireta ou mudança de regime |
| **P-C** | Priorizar premier-presidencialismo e exigir justificação independente para poderes de reserva presidenciais | Não aprova duas cadeias de comando nem faculdade de demitir gabinete |
| **D0** | Adiar preferência **somente** se apontada prova capaz de inverter o foco, com critério de parada | Não equivale a autorização de pesquisa repetitiva ilimitada |

**P-B é recomendação técnica P**, já existente; não é uma nova escolha desta rodada, não vira D e **não foi selecionada pelo usuário**. A letra isolada que autorizou a rodada executiva **não é voto em P-B, R1/R2 ou A/B/C**.

**Por que a escolha P é apresentável?** A/B/C estão descritos com 16 protótipos condicionais no [PR #107](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/107), e o [PR #99](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/99) documenta comparativos, custo fiscal e melhores objeções; o usuário pode indicar foco de trabalho sem presumir que seu conteúdo será constitucionalmente válido. **Escolha D continua bloqueada**, ainda que seja possível pedir P.

## 3. As outras nove questões — por que ainda NÃO podem ser apresentadas como texto aprovado

Consultar [funil de 10 recortes](04_FUNIL_DECISOES_F6.csv) para estados e responsáveis. **Uma está `REVISAO_JURIDICA_PRE_F6` e as outras oito são `BLOQUEADO_*`**, nenhuma se converte em D:

| Porta | Situação e prova imprescindível |
|---|---|
| **F6-01 — rigidez material R1/R2** | Preservar o piso vigente de [CF art.60§4](https://www.planalto.gov.br/ccivil_03/constituicao/constituicaocompilado.htm) nas quatro categorias e obter revisão de alcance/efetividade. R3, só rito sem núcleo, é contraprova insuficiente, não recomendação |
| **F6-02 — Governo A/B/C como D** | Exigir poderes, investidura, defesa, LOA e via constitucional testados; priorização P não substitui adoção D |
| **F6-03 — B-D/B-I, eleição da chefia de Estado** | Prova específica do conteúdo do voto protegido por art.60§4 II; exceção de dupla vacância (art81§1) não resolve B-I ordinário; avaliar anterioridade |
| **F6-04 — Parlamento P1/P2/P3** | Escolher Casas/competências separadamente do Governo; proteger consultas indígenas e rito de tratados H-0025/0028/0036, legitimidade coletiva H-0037 |
| **F6-05 — Corte J1/J2/J3** | Legitimados, juiz natural, competência, conflito entre cortes, transição de feitos e remédios, não presumir Corte apartada aprovada |
| **F6-06 — via PEC/consulta/constituinte** | Parecer de admissibilidade **por ato**: PEC sujeita art.60; consulta não sana inconstitucionalidade; processo constituinte não decorre automaticamente de PEC |
| **F6-07 — transição temporal M14** | Sequência de legitimidade, marcos eleitorais, instalação de casas, primeira investidura, processos e serviços, respeitando art16 |
| **F6-08 — custeio, LOA e serviços** | Teste de direito exigível versus ente devedor, recurso, autorização, plano e tutela judicial sem criar despesa por decreto |
| **F6-09 — H→D de texto CF-NOR** | Cada artigo requer decisão específica, fonte, auditoria de CF/ADCT, parecer jurídico, controle de direitos e integração. **Nunca decisão em bloco por número de H** |

## 4. Ordem de desbloqueio — dependências em vez de rodadas isoladas

```text
Direito vigente CF/1988 + art.60 §4 e art.16 + ADCT
  ├─> F6-01 (piso contra emendas regressivas; revisão R3)
  ├─> F6-06 (via PEC/consulta/constituinte; parecer por ato)
  └─> F6-00 (prioridade P-A/P-B/P-C/D0, única pauta apresentável agora)
         ├─> F6-02 (Governo como D, depois de garantias e funções completas)
         ├─> F6-03 (modo de eleição de chefe de Estado e art.60)
         ├─> F6-04 (organização do Parlamento P1/P2/P3, decisão independente)
         ├─> F6-05 (controle constitucional J1/J2/J3, decisão independente)
         ├─> F6-07 (eleição/investidura/transição após modelos e vias concretos)
         └─> F6-08 (LOA/custeio/tutela social testados de modo independente)
                   └─> F6-09 (norma H individual → D, só após revisão/decisão)
```

**A disposição no grafo é de compatibilidade**, não cronograma obrigatório. A solução de LOA pode e deve avançar **antes** da escolha do Governo se uma contraprova relevante puder alterar a decisão; a definição de Justiça não exige que todo o sistema de Governo esteja ratificado; as portas são paralelas onde possível. A política de ganho marginal pode priorizar M01 direitos concretos acima de qualquer discussão de Governo se um dano R3 decisivo surgir.

## 5. Contraprovas exigíveis e prazos de conclusão substantiva

- **Rigor de art.60:** as quatro categorias protegidas contra emenda tendente a abolir são federação, voto direto/secreto/universal/periódico, separação dos Poderes e direitos/garantias individuais. [STF ADI 3.685/DF](https://portal.stf.jus.br/peticaoInicial/verPeticaoInicial.asp?base=ADI&numProcesso=3685) reconhece proteção da anterioridade eleitoral inclusive contra emenda casuística. Isso não torna B-I categoricamente inconstitucional sem exame da PEC e seus efeitos, nem autoriza assumi-lo válido.
- **Legitimidade processual:** proposta de emenda antes da promulgação, consulta convocada, emenda promulgada, pleito/diplomação e posse/investidura são fatos e vias distintas; referenciar o parecer independente [PR #96](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/96) em vez de criar remédio universal de controle prévio.
- **Contraprova A:** aferir se presidencialismo com oposição, orçamento e controle independente pode oferecer benefícios equivalentes aos esperados de B; sem esse confronto a superioridade de B é apenas hipótese.
- **Ruptura não presumida:** a eventual elaboração de nova Constituição é debate próprio de legitimidade e transição, nunca atalho técnico para escapar do art.60 vigente.
- **Não impor prazo fictício:** nenhuma data de eleição, mandato ou ratificação foi decidida; a eventual escolha de P define foco de trabalho, não cronograma.

## 6. FEITO / PENDENTE / GANHO / PRÓXIMO

**FEITO:** reconciliação da pauta preexistente #99 com protótipos #107 e controles #129/#130, separando dez objetos em um funil com único recorte pronto para **apresentação** e nove portas de risco. A coordenação atualizada fica na `main` apenas como documentação, se aprovado o PR correspondente. **PENDENTE:** revisão jurídica R3, evidências de viabilidade orçamentária/eleitoral e decisão expressa F6, além da infraestrutura CI [#120](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/120) e integração do stack. **Ganho esperado versus realizado:** esperado redução de duplicação de pautas e identificação da próxima decisão útil; obtido quadro rastreável sem H novas, sem F6 ou D. **PRÓXIMO:** quando houver manifestação específica do usuário, apresentar **uma** escolha P-A/P-B/P-C/D0; caso contrário, trabalhar em uma das nove provas que efetivamente possa desbloquear F6-01/F6-02, reavaliando outras frentes pelo ganho marginal. **CLF independente e sem alteração.**
