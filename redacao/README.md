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
