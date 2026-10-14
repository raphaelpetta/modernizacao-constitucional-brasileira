# M01.08 — Pacote de continuidade e integração (CF-M01-S008)

**Corte:** 13/10/2026. **Estado:** pesquisa F0–F5, testes preliminares F8, sem decisão material D, sem norma CF-NOR nova.  
**Main lida em GitHub:** `680f5463253fee6e0bdbee5fa3214fb4f08fbef9`. **PR de pesquisa:** [#22](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/22), draft e ainda não mesclado.  
**Pesquisa anterior:** M01.01–M01.07 (mesma branch). **Issue:** #5.  
**Fato novo relevante em main:** foi implantado piloto integrado de redação `CF-NOR-0003` a `0007` (**todos H**) e protocolo M00.03 G/E/X/A/T, conforme `redacao/README.md`, `redacao/indice.csv`, `governanca/11_TECNICA_DE_REDACAO_E_INTEGRACAO.md`. Os documentos `M01-07_MINUTA_PILOTO_REGIME_GERAL_v0.1.md` e `M01-07_MATRIZ_DE_CONTINUIDADE.csv` registram **direitos da intimidade/dados como ainda não cobertos** pelo piloto.

## Entregas desta rodada
1. `M01-08_PRIVACIDADE_DADOS_AUTOMACAO_v0.1.md`: dossiê sobre seis objetos, jurisprudência STF, LGPD e exceções, comparação RGPD/AI Act/BVerfG/TJUE, nove decisões DIG01–DIG09, três protótipos e críticas.
2. `M01-08_CASOS_PRIVACIDADE_DADOS_AUTOMACAO.csv`: **28 casos adversariais** com direitos/obrigações/salvaguardas/testes e objeções.
3. `M01-08_MATRIZ_CONTINUIDADE_DIGITAL.csv`: **18 relações N:N** de garantias CF/1988, legislação/tratados específicos e piloto `CF-NOR-0003–0007`; nenhuma equivalência plena presumida.
4. Este pacote.

## Descobertas jurídicas verificadas

- **EC 115/2022:** proteção de dados pessoais é **direito autônomo** art. 5º LXXIX e a União tem competência privativa para legislação sobre proteção/tratamento art. 22 XXX. Privacidade não a substitui automaticamente.
- **LGPD art. 20:** revisão de decisão tomada **unicamente** por automação e informações claras sobre critérios; §3º vetado; **não há garantia legal expressa universal de revisão humana no texto vigente desse artigo**. A futura Constituição precisa avaliar revisão efetiva, autoridade e grau de impacto sem criar presunção falsa de texto positivo brasileiro.
- **STF ADI 6387:** precedente cautelar relevante para dados, não proibição geral de uso governamental.
- **STF ADI 6649 + ADPF 695 (2022):** compartilhamento de dados entre órgãos públicos admitido sob finalidade legítima, especificidade, compatibilidade, minimização, transparência, segurança e responsabilização. O direito constitucional não depende de consentimento universal.
- **LGPD art.4 III:** exclusão do âmbito ordinário da LGPD para segurança/investigação não suspende direitos da CF; requer regime especial, competente, proporcionado e controlado, sob M12/M06.
- **Lei 15.352/2026:** ANPD é **Agência Nacional de Proteção de Dados**, autarquia especial/agência reguladora. A agência/fiscalização existente é arranjo legal; constitucionalização de independência deve ser justificada em M07 e não necessariamente cristalizar seu nome.
- **Lei 15.211/2025 ECA Digital**, com vigência alterada em 2026: proteção de crianças e verificação etária requerem cuidado com vigilância indevida em massa; pendem detalhes de implementação.
- **Alemanha, BVerfG 2008:** proteção da integridade/confidencialidade de sistemas informáticos; referência funcional para infiltração remota, sem transferência automática da doutrina.
- **UE GDPR art22 vs LGPD art20:** regras distintas para decisões automatizadas; TJUE `SCHUFA` abrange score fortemente determinante para decisão contratual.
- **AI Act UE:** edição consolidada 27/07/2026 (Reg 2024/1689), com vigência escalonada, inclusive requisitos específicos de alto risco para anos posteriores; não dizer que todo AI Act de alto risco está plenamente exigível em out/2026.

## Status decisório/proveniência

| Questão | Conteúdo | Status |
|---|---|---|
| CF-M01-DIG01–02 | Autonomia de dados; privacidade, comunicações e sistemas | P de pesquisa, sem ratificação |
| CF-M01-DIG03 | Compartilhamento governamental com finalidade e controles | P de pesquisa, sem ratificação |
| CF-M01-DIG04 | Biometria/vigilância e reservas judiciais | A/V, sem ratificação |
| CF-M01-DIG05–06 | Revisão efetiva, explicação e grau de supervisão humana | A/P, sem ratificação |
| CF-M01-DIG07 | Fiscalização independente institucional | A/P, interface M07 |
| CF-M01-DIG08 | Direitos da infância e dados sensíveis | A/P, interface M09 |
| CF-M01-DIG09 | Dados penais/inteligência e lei especial | A/V, interface M12 |

**Não houve ratificação do usuário das alternativas; nenhum dos protótipos A/B/C recebeu ID CF-NOR**. Não criar artigos normativos concorrentes diretamente na branch #22: o protocolo M00.03 define fonte única `redacao/propostas` e índice canônico, que devem ser mantidos coesos. A autorização para seguir pesquisa não é instrução de fundir PR draft à main.

## Questões de controle de qualidade e lacunas

1. Auditar o texto integral e evolução de STF ADI6529, métodos invasivos, registros de conexão, metadados, sigilo de fonte, biometria e execução de medidas policiais.
2. Distinguir risco de algoritmo, causalidade de discriminação e mera diferença de resultado; exigir estudo empírico, dados representativos, falsa identificação e contextos.
3. Garantir que transparência não exponha dados sensíveis/segredos legítimos e que segurança não sirva de pretexto para imunidade completa de fiscalização independente.
4. Mecanismos de defesa devem ser realmente executáveis por pessoas comuns e não apenas formalmente previstos; estudar custo/prazo de revisão e risco de `human-washing`.
5. A competência constitucional atual art22 XXX e a autonomia territorial futura devem ser revisadas por M04, e não simplesmente transportadas.
6. Conferir o estado das normas de ANPD e AI Act ao reutilizar o estudo; agendas não são resoluções terminadas.
7. Auditabilidade com logs, proteção de dados dos próprios logs, acesso de vítimas e supervisores, retenção e destruição proporcionadas.
8. Nomes e categorias de autoridades só após deliberação dos módulos institucionais; a independência técnica depende também de controle democrático e financiamento.

## Arquivos e fontes consultados nesta sessão

**GitHub `main`:** `redacao/README.md`, `redacao/anteprojeto-de-trabalho.md`, `redacao/indice.csv`, `redacao/propostas/CF-NOR-0001.md`, `governanca/11_TECNICA_DE_REDACAO_E_INTEGRACAO.md`, `governanca/03_DECISOES.md` e `04_ESTADO_ATUAL.md`, `M01-07_MINUTA_PILOTO_REGIME_GERAL_v0.1.md`, `M01-07_MATRIZ_DE_CONTINUIDADE.csv`. Da branch de pesquisa, `M01-07_PACOTE_CONTINUIDADE_v0.1.md`.

**Oficiais externos, links no dossiê:** CF/1988/EC115; LGPD atualizada, art20 e veto; STF ADI6387, ADI6649/ADPF695; Lei15352/2026; Lei15211/2025; ANPD agenda; RGPD 2016/679, AI Act consolidado, BVerfG 2008 e TJUE SCHUFA. A questão jurídica formal de certos julgamentos/atos permaneceu `V`, não concluída por resumo de imprensa.

## Trilha seguinte

**M01.09 — auditoria de continuidade e organização constitucional integrada:** consolidar N:N de proteção do art5 e direitos pessoais fora dele; confrontar pilotagem CF-NOR-0003–0007 com direitos substantivos de M01.05–M01.08; propor fichas de redação apenas conforme protocolo de fonte única, tipo G/E/A/X/T, índice e script, nunca como cópias paralelas. Em paralelo aprofundar segurança pública/biometria e auditoria algorítmica M07/M12, com estudo empírico em vez de mera comparação de leis.

**Checagem de GitHub pendente após gravação:** confirmar o último commit, teste `arquivos-e-modulos`, PR mergeable e a existência de alterações simultâneas na main. Validação estrutural não significa aprovação jurídica, empírica ou material.
