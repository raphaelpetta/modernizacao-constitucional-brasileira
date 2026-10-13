# Padrão de dados, identificadores e proveniência da pesquisa constitucional

**ID:** CF-GOV-010 · **Versão:** 0.2 · **Data:** 13/10/2026.

## Identidades estáveis
- `M00` a `M14`: módulos funcionais de pesquisa; não determinam títulos da Constituição.
- `CF-PROB-Mxx-0001`: problema documentado; o status não equivale a problema comprovado.
- `CF-DEC-0001`: deliberação; exige D/P/H/A/V, data, fonte e responsável pela ratificação.
- `CF-NOR-0001`: proposta de enunciado normativo, independente do número de artigo final.
- `CF-CR-AAAA-NNN`: alteração transversal ou pedido de compatibilização.
- `CF-IC-...`: interface constitucional → CLF, com versão bilateral.
Identificadores antigos não se reutilizam quando a proposta muda substancialmente; usar histórico de substituição, fusão ou divisão.

## Fontes e documentação
Cada pesquisa registra: ID de fonte, entidade e tipo, norma/artigo ou precedente, URL oficial (quando houver), data de corte, data de acesso, conteúdo efetivamente examinado, versão aplicável, proposição que sustenta e limitações. Distinguir legislação vigente de minuta, hipótese, precedente, doutrina, inferência e decisão política.

Fonte de direito brasileiro: preferir texto oficial e jurisprudência efetivamente verificada. Direito comparado: país, data, função, contexto institucional e força jurídica. Evidência empírica: amostra, desenho, resultados, inferência causal/descritiva e limitações. Quando não conferido, `A_VERIFICAR`; nunca fabricar validade, consenso ou precedente.

## Rastreabilidade constitucional
Um artigo vigente pode alimentar vários dispositivos propostos e vários direitos atuais podem ser protegidos por um só artigo novo. Registrar relações `1:1`, `1:N`, `N:1`, `N:N` com justificativa. Toda omissão de garantia ou mecanismo exige ficha `governanca/09_AUDITORIA_GARANTIAS.md`. Preservação material não se mede apenas por palavras idênticas.

## Controles e segurança
Checar IDs únicos, referências entre módulos, links locais, campos e fontes, pendências explícitas e estados de decisão. A validação automática atesta apenas **integridade documental**, nunca qualidade científica, constitucionalidade ou direito vigente. Não versionar documentos sigilosos de clientes, dados pessoais desnecessários, segredos, tokens ou URLs temporariamente assinadas. Respeitar licenças e direitos autorais.
