# CF-CC-015 — Pacote de continuidade

**Corte:** 15/10/2026, fontes oficiais consultadas nesta rodada. **Branch:** `pesquisa/cfcc015-m05-caixa-rgf-fiscal-20261015`, derivada do HEAD do [PR #118](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/118), `fcd230c18a20bfd74764034ae4cf3388c6c6cf45`. **Main verificada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168` (**20 H**). **Stack H:** 45 em 15 módulos; a mesma contagem do PR pai, sem nova CF-NOR. **Status político-jurídico:** texto H/A/V, sem F6/D, sem merge, sem CLF.

## FEITO — delta documental
1. O [RGF da União, Poder Executivo, 1º quadrimestre 2025, Anexo 5 retificado de 2024](https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/52223_1645804/01_%20RGF1Q2025.pdf), foi examinado em tabela e nota da página impressa 14 (PDF índice 13). **Dados do exercício 2024, não 2025/2026**; unidade reais, período 31/12/2024.
2. `modulos/M05-financas/M05_CC015_RGF2024_CAIXA_OBSERVADA.csv`: **7 grupos reais**, incluindo totais e subgrupos não aditivos. Recursos ordinários líquidos após RP não processados **R$44.980.772.540**, RGPS **−R$3.135.928.718**; a nota do RGF explica compensação contábil com recursos ordinários, não indisponibilidade sistêmica nem imunidade à vinculação.
3. Parecer `modulos/M05-financas/M05_CC015_PARECER_DADOS_REAIS_CAIXA_VINCULACAO_v0.1.md`: fonte, procedimento, contraprova de inferências proibidas, LRF arts 8º, 41, 42 e 50, marco temporal 2027 do art41 LC212/2025 e tese adversarial.
4. `redacao/propostas/CF-NOR-0048.md` **revisada apenas no terceiro parágrafo H** para exigir discriminação de recursos legalmente utilizáveis, cobertura ordinária legítima, insuficiência financeira residual e vedação de desvio de recursos vinculados. Mesma ID/ordem 0048/0470, não criou D; sincronização literal `redacao/anteprojeto-de-trabalho.md`.
5. `auditoria/CF_CC_015_TESTES_CAIXA_DADOS_REAIS.csv`: **12 testes** de premissas e limitações empíricas, status V/A; se somam, sem substituição, aos 21 testes sintéticos de CF-CC-014.
6. **CI preflight mais específico:** check-run do HEAD do PR #118 `fcd230c1...` possui **2 anotações** relatadas pelo GitHub, mas os detalhes não foram acessíveis pelos conectores autorizados; o workflow run 38764016104 falhou com job sem etapas e logs `404 BlobNotFound`. Não atribuir causa a código ou infraestrutura. **Não executados** testes Python oficiais.

## QA realmente executada (leitura remota da branch)
- **PASS 7/7 registros oficiais** confrontando `líquida antes (f) − RP não processados (g) = líquida após (h)`, tolerância máxima de **R$1** em arredondamento/apresentação da fonte; sem inferir fluxos efetivos mensais. Ressalva: totais e subgrupos não devem ser somados.
- **PASS 12/12 casos** de auditoria com 12 IDs distintos e número de colunas consistente.
- **PASS 45/45 propostas** com fonte existente, marcadores `NORMA` válidos e texto presente na seção correspondente da vista; leitura em cinco blocos de nove documentos.
- **PASS 45/45 no índice** com IDs/ordens únicos, 45 seções, H em todos e cobertura dos **15 módulos**; o corpo da CF-NOR-0048 aparece literalmente no final da vista.
- **Limite essencial:** validação documental *não demonstra* que 45 H preservam integralmente direitos/competências da CF, e não substitui `python scripts/gerar_anteprojeto.py --check`, `python scripts/validar_repositorio.py`, revisão de segurança e CI green.

## PENDENTE — questões substantivas / bloqueios
- RGF federal 31/12/2024 não identifica, por si, disponibilidade diária, pagamentos específicos, custo de saúde/educação, fluxo de cada vinculação ou capacidade de pagamento de municípios. É **contraprova da interpretação simplista**, não teste completo de regime sem LOA.
- Necessário um par município/exercício de RGF Anexo 5 e RREO/anexos, mais execução real por programa, mesmo período e lei orçamentária para cruzamento de despesas essenciais; ver catálogo M05.02 e critérios de representatividade, sem selecionar só casos que confirmem tese.
- Interpretação de disponibilidade de caixa, efeitos do art41 da LRF em 2027, exceções de calamidade, transferências constitucionalmente protegidas e hierarquia das preferências exigem parecer M05/M06/M04/M09/M14.
- Cláusulas de impasse A/B/C, segundo exercício sem orçamento e competência judicial/legislativa continuam abertas; nenhuma decisão política registrada.
- **CI:** investigar as 2 anotações do check-run, a ausência de logs e a execução real do workflow; comparar PRs #59, #101/#104, #105–#118 antes de merge.

## PRÓXIMO — atos autônomos
1. M05/F4-F5: coletar dados oficiais subnacionais 2025/2026 com mesma granularidade e executar modelo de pagamento por fonte vinculado à necessidade efetiva de serviços, com lacunas explicitadas.
2. M05/M03/M14: construir fluxos de impasse prolongado A/B/C e modelo de atendimento mínimo juridicamente executável, sem atribuir ao Judiciário votação da LOA.
3. Coordenação CF #103, M05 #25 e M03 #84: resolver check-run anotado, executar gerador/validador, rever direitos/competências, preservar stack draft e nenhuma D sem ratificação.

**RESPONSÁVEIS/INTERFACES:** M05 (finanças); M03 (governo/orçamento); M04 (finanças federativas); M06 (tutela); M09 (prestações sociais); M14 (transição); CF central (#103); CLF apenas se consequência infra legal concreta exigir interface bilateral, não neste ciclo.

**Nenhuma política fiscal é declarada aprovada por esta documentação.**
