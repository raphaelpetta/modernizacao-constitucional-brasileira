# Redação constitucional — versão viva de trabalho

**Regra de autoridade:** a pasta `redacao/` contém propostas para uma nova Constituição, **não** texto constitucional vigente, nem decisões materiais ratificadas por mera integração técnica.

## Onde está o texto?

- **Texto completo para consulta:** [anteprojeto-de-trabalho.md](anteprojeto-de-trabalho.md), **gerado automaticamente**, com IDs permanentes e situação `H/P/D`. Não é uma versão constitucional completa.
- **Fonte única de cada norma:** [propostas/](propostas/) — arquivos `CF-NOR-####.md`, cada um com texto entre `<!-- NORMA-INICIO -->` e `<!-- NORMA-FIM -->`, mais justificativa e testes fora da redação.
- **Índice canônico:** [indice.csv](indice.csv), que informa a sequência provisória, estado, assunto, módulo, regra geral, justificativa de especialidade, interfaces e avaliação de garantias.
- **Protocolo editorial:** [governanca/11_TECNICA_DE_REDACAO_E_INTEGRACAO.md](../governanca/11_TECNICA_DE_REDACAO_E_INTEGRACAO.md), que define regra geral, especialização, exceção, norma autônoma e transitoriedade.
- **Anteprojeto antigo de 2026:** [referencias/anteprojeto_constitucional_v0.1_texto.md](../referencias/anteprojeto_constitucional_v0.1_texto.md) — **apenas histórico**, não base normativa obrigatória.

## Como editar

1. Conferir SHA de `main`, `governanca/03_DECISOES.md` e módulo de pesquisa responsável. Criar branch.
2. Formular `CF-NOR` em `redacao/propostas/`, com justificativa, objeção, evidência e exame da continuidade de direitos; registrar no índice com `status=H` por padrão.
3. Se especialização (`E`) ou exceção (`X`), vincular `regra_geral` e justificar qual consequência jurídica adicional existe. Não substituir garantia específica por regra abstrata sem análise material.
4. Atualizar apenas arquivos-fonte/índice; executar `python scripts/gerar_anteprojeto.py`; executar `python scripts/gerar_anteprojeto.py --check` e `python scripts/validar_repositorio.py`.
5. Abrir PR, conferir compatibilidade cruzada e **não** alterar `H` para `D` sem decisão explícita documentada com `CF-DEC`. A validação estrutural não atesta constitucionalidade.
6. Integrar após verificação; citar o SHA final. **Uma cópia da conversa, arquivo anexado, memória ou resumo não é sincronizada automaticamente** com GitHub.

## Dispositivos de demonstração

`CF-NOR-0001` e `CF-NOR-0002` são **dois testes de técnica redacional** em áreas de federalismo/custeio pesquisadas no M04/M05, **ambos H**, sem numeração definitiva e sem ratificação substantiva. A primeira vista integrada **não** é minuta integral e não autoriza presumir texto de direitos, governo ou Justiça definido.

## Como recuperar a mesma versão em outro chat

Solicitar recuperação de `redacao/anteprojeto-de-trabalho.md` diretamente da `main` do GitHub e conferir o **SHA**, ou usar URL com SHA fixo para congelar a exata revisão. Arquivos antigos anexados ao ChatGPT e mensagens em outros chats podem ficar desatualizados. **Fonte documental do projeto = GitHub; nunca atualizar duas cópias manuais do texto.**

## Piloto de regime geral de direitos — M01.07

A etapa F7 recebeu **cinco hipóteses H de direitos fundamentais**: `CF-NOR-0003` titularidade, `0004` aplicação imediata/deveres públicos, `0005` especialidade de incidência privada, `0006` limites de restrição e `0007` tutela. [Dossiê](../modulos/M01-direitos-fundamentais/M01-07_MINUTA_PILOTO_REGIME_GERAL_v0.1.md) e [auditoria com 16 conjuntos da CF/1988](../modulos/M01-direitos-fundamentais/M01-07_MATRIZ_DE_CONTINUIDADE.csv). O PR de pesquisa M01.01–M01.06 permanece draft [#22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22), não integrado automaticamente. A inclusão H e a montagem do texto **não aprovam** titularidades, cláusula geral de restrição, efeitos privados ou arquitetura judicial; a matriz marca equivalência não demonstrada e direitos especiais pendentes.

## Piloto de igualdade material — M01.09 (13/10/2026)

O texto de trabalho inclui quatro novas hipóteses `H` `CF-NOR-0008` a `0011`: igualdade material (G); antidiscriminação direta/indireta (E da 0008); adaptações razoáveis (E da 0009); e admissibilidade de medidas afirmativas (E da 0008). [Dossiê M01.09](../modulos/M01-direitos-fundamentais/M01-09_REDACAO_IGUALDADE_v0.1.md) e [matriz de 16 garantias/testes](../modulos/M01-direitos-fundamentais/M01-09_MATRIZ_IGUALDADE_E_GARANTIAS.csv). **A CDPD já é constitucionalmente equivalente a emenda no regime atual**; não presumir novidade ou equivalência de direitos. O PR #22 permanece draft, com pesquisa própria M01.08 sobre privacidade; o nome M01.09 evita duplicação de subciclos. A integração H não ratifica qualquer cláusula.

## M01.10 — integridade e bioética: seis hipóteses H (13/10/2026)

O anteprojeto de trabalho contém `CF-NOR-0012–0017` para dignidade (A), proteção da vida (A), integridade/autonomia (G), tortura e tratamento degradante (E), consentimento assistencial (E), e experimentação humana (E), em [dossiê M01.10](../modulos/M01-direitos-fundamentais/M01-10_DOSSIE_DIGNIDADE_VIDA_AUTONOMIA_v0.1.md) e [20 registros de não regressão](../modulos/M01-direitos-fundamentais/M01-10_MATRIZ_CONTINUIDADE.csv). São cláusulas **H NÃO ratificadas**. O direito atual inclui CF/1988, CDPD e regimes legais setoriais; temas de aborto, eutanásia, saúde mental coercitiva e crianças dependem de estudo e escolha próprios, não de dedução automática dessas cláusulas. Texto integrado é derivado de arquivos únicos e índice, com CI; não editar manualmente uma cópia.
