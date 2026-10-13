# Protocolo de continuidade entre chats e governança Git

**ID:** CF-GOV-006 · **Versão:** 0.1.

## Fonte oficial de estado
O GitHub é a fonte do **estado documental do projeto**, nunca substituindo leis ou jurisprudência oficiais. `main` armazena documentos integrados; uma branch ou PR representa proposta ainda não incorporada. Sempre identificar SHA de entrada.

## Ao abrir um chat
Ler `governanca/04_ESTADO_ATUAL.md`, `03_DECISOES.md`, `02_METODOLOGIA.md`, `05_DEPENDENCIAS.md` e arquivos do módulo. Dizer quais arquivos/commits foram realmente consultados e quais não estavam disponíveis. Fixar escopo e entregas do chat.

## Durante o trabalho
Separar evidências, opiniões, hipóteses, propostas e decisões ratificadas. Não editar texto compartilhado de outro módulo sem pedido formal de revisão. Atualizar a ficha do módulo apenas após conferir versão mais recente, especialmente se houve trabalho concorrente.

## Ao encerrar ou antes do limite de contexto
Produzir `modelos/PACOTE_CONTINUIDADE.md`, com versões, entregas substantivas, fontes, deliberações realmente ratificadas, pendências, propostas de alteração e pergunta específica da próxima sessão. Salvar pacote no GitHub se houver acesso de escrita; **uma mensagem de chat não o faz automaticamente**.

## Integração
Comparar a base do trabalho com `main` no momento de integrar. Usar branches e pull requests quando houver mudança substantiva, revisão adversarial ou interfaces cruzadas; atualizar log decisório somente após deliberação do usuário. Não alegar aprovação normativa pelo simples merge de documento metodológico.

## Regra de desempate
Se `main` divergir de uma sessão anterior, ler diff/commits e reconciliar; jamais sobrescrever um estado posterior com resumo antigo. Em caso de disputa substantiva, manter ambas as alternativas rastreadas até nova deliberação.
