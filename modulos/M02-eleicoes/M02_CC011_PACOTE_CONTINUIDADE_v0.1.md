# CF-CC-011 — Pacote de continuidade / M02 e M03

**Data de corte:** 15/10/2026. **Branch:** `redacao/cfcc011-m02-m03-confianca-cpi-20261015`. **Base do stack:** PR [#116](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/116), SHA `abf450fd5491b8310e1e02b88102c370dcaeac45`. **Main verificada:** `2a770a8136f8ca4877e865be3e3b7745a6d4b168`, 20 normas H (sem merge). **Estado material:** tudo H, nenhuma nova D/F6; governo A/B/C permanece em aberto, CLF inalterado.

## FEITO
1. `CF-NOR-0046`: proteção da confiança contra virada de jurisprudência do órgão superior eleitoral durante ou logo após pleito; especialização E de 0045, sem confundir regra de um ano para lei (art16/Tema387) com prospectividade jurisprudencial (Tema564).
2. `CF-NOR-0047`: direito de minoria parlamentar instaurar CPI com 1/3, fato determinado, prazo certo, poderes de investigação e direitos fundamentais/reserva de jurisdição. Hipótese A funcional neutra entre A presidencialismo, B parlamentarismo e C premier-presidencialismo; não decide Câmara alta, investidura, confiança ou censura.
3. Pareceres `modulos/M02-eleicoes/M02_CC011_PARECER_PROSPECTIVIDADE_JURISPRUDENCIA_v0.1.md` e `modulos/M03-parlamento/M03_CC011_PARECER_CPI_NEUTRALIDADE_ARQUITETURAS_v0.1.md`.
4. `auditoria/CF_CC_011_MATRIZ_16_TESTES_M02_M03.csv`: oito situações M02 e oito M03; riscos V/A, sem tratar simulações como julgados.
5. `redacao/indice.csv` atualizado com 0046/0450 M02 E e 0047/0460 M03 A; vista derivada `redacao/anteprojeto-de-trabalho.md` com **44 H em 15/15 módulos** na branch experimental.

## QUALIDADE EFETIVAMENTE OBSERVADA
Verificação JavaScript após leitura dos arquivos reais pelo conector GitHub:
- 44 registros, 44 IDs únicos e 44 ordens únicas no índice, todos H;
- 44 seções correspondentes e 15 módulos M00–M14 presentes;
- 16 linhas de auditoria, 16 IDs únicos e colunas consistentes;
- os blocos `NORMA` de 0046 e 0047 ocorrem literalmente nos trechos correspondentes da vista integrada;
- nenhuma edição de `main`, CF-DEC, CLF ou modelo de governo.

**Limites:** QA apenas para estes invariantes; não houve execução dos scripts Python `gerar_anteprojeto.py --check` e `validar_repositorio.py`, nem prova de que 44 textos foram todos semanticamente comparados com CF/1988. Conclusão do CI deverá ser inspecionada após abertura do PR; falhas anteriores nos PRs #115/#116 tinham etapas ausentes/logs `BlobNotFound`, não se atribuindo causa.

## PENDENTE / NÃO VERIFICADO
- **M02/M06:** se a formulação de prospectividade H impede correção de injustiça urgente, decisão de inconstitucionalidade e eleições suplementares; como aplicar Tema564 sem confundir lei e jurisprudência.
- **M03/M06:** contorno dos poderes de CPI, reserva de jurisdição, direito a informações, sigilos, convocação e acesso da oposição; proteção do direito da minoria de abuso instrumental.
- **M03/M04/M05/M14:** bicameralismo ou unicameralismo, CPIs conjuntas, fiscalização financeira e transição de procedimentos investigativos.
- **M01/M02:** cobertura CF14 §§1–16, CF17, acessibilidade, elegibilidade e voto, não resolvidos por 0045–0046.
- **Coordenação:** revisão PR #59 (0030/0031 reservadas), #101/#104 governança; stack #105–#116 permanece sem integração; PR #107 M03 independente, sem colisão textual decidida.

## PRÓXIMO — três atos independentes
1. M03/M05: construir três variantes condicionais de relação governo-orçamento e controle fiscal A/B/C, preservar proibição de criar gasto por derrota da LOA e confrontar problemas da fiscalização financeira.
2. M02/M06/M01: completar matriz de direitos políticos CF14–17 e redigir garantias de elegibilidade/participação com teste de não regressão, sem fixar sistema eleitoral.
3. Coordenação: revisar técnica, testes, CI da branch específica, cotejar PRs concorrentes e decidir sobre merge **somente depois de revisão operacional/material**; não converter H para D.

**RESPONSÁVEIS E DEPENDÊNCIAS:** M02 (issue #14), M03 (issue #84), M06 (issue #55), M14 (issue #90), central (issue #103); PRs #95, #107, #115, #116. Interface CLF apenas se nova consequência concreta exigir comunicação bilateral. Documentação desta rodada não aprova via constituinte, PEC, voto direto presidencial ou modelo A/B/C.
