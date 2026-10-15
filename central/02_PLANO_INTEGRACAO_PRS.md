# CF — plano de integração dos PRs e prevenção de rebase silencioso
**Corte:** 15/10/2026. **Natureza:** registro operacional de dependências observadas; não ratificação. Revalidar base/HEAD no GitHub antes de qualquer merge. [Central #103](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/103).

## Governança e produto são trilhas diferentes
- **PR #101:** metodologia de desenvolvimento por camadas, catálogo funcional, README, decisões e controles.
- **PR #104:** central, fila, painel de produto e verificação operacional. Comparar conceitos com #101 antes de integrar; um não substitui automaticamente o outro.
- **PRs #105–#109:** produção de texto e variantes, sem integração na main nem ratificação D.

## Grafo observado nas bases dos PRs
```text
main ── #105 M07 (CF-NOR-0021)
         └── #106 M08 serviços (CF-NOR-0022)
              └── #108 M10 ambiente (CF-NOR-0023)
                   └── #109 M08 economia/concorrência (CF-NOR-0024)

main ── #107 M03 alternativas A/B/C (somente variantes)
main ── #101 governança por camadas
main ── #104 central e controles
```

**Atenção:** a ordem decorre do campo `base` de cada PR. Verificar novamente branch-base, HEAD e SHAs antes de executar; branches podem receber revisões.

## Sequência operacional
1. Reconciliar diretrizes dos PRs #101 e #104, escolhendo uma autoridade operacional por tema e preservando PROPOR → INTEGRAR_EXPERIMENTALMENTE → RATIFICAR.
2. Revisar #105 (M07) contra as fontes e garantias, testar compilação e, se cabível, integrar como H experimental — nunca D por simples merge.
3. Revalidar diff de #106 sobre #105 integrado; em seguida #108 sobre #106 e #109 sobre #108. Não mesclar o último diretamente na main sem conferir heranças e recortes.
4. Tratar #107 como frente separada de variantes de M03; não selecionar arquitetura institucional pelo merge de estudo.
5. Fila `central/FILA_TRABALHO.csv` acompanha o trabalho; painel `central/PAINEL_GERADO.csv` conta apenas as fontes do checkout, não cláusulas de PRs ainda ausentes da main.
6. Como GitHub Actions falhou antes dos steps, não declarar testes aprovados; registrar execução local somente se realizada e preservar revisão proporcional ao risco.

## Riscos de colisão
- #105/#106/#108/#109 compartilham alterações no índice e no texto compilado: fora da ordem, podem provocar exclusão de dispositivos, renumeração ou diffs enganosos.
- #102 e #105 tratam M07 sob perspectivas diferentes: reconciliar garantias e origem antes da incorporação experimental.
- #106 e #109 tratam M08 sob recortes diferentes, mas #109 depende do stack que contém M10.
- Merge documental não significa ratificação material nem C0-J.

**Porta de saída:** só encerrar a reconciliação depois de conferir grafo atualizado, QA efetivamente executado, revisão adequada e estados H/D preservados.
