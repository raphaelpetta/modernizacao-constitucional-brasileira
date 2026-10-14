# M06.02 — Pacote de continuidade obrigatório

**ID:** CF-M06-S002 · **Data:** 14/10/2026 · **CF main de referência:** `eaab37bcd5467d48db0cc0bda133c62ee7801ffe` · **PR:** [#62](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/pull/62), draft · **Issue:** [#65](https://github.com/raphaelpetta/modernizacao-constitucional-brasileira/issues/65). **Status:** pesquisa F0–F5/F8, nenhuma ratificação D, sem nova CF-NOR.

## FEITO
- `M06-02_DOSSIE_REMEDIOS_E_EQUIVALENCIA_v0.1.md`: auditoria de HC/MS/MI/HD/ação popular, acesso material/legitimidade, limites de cada via, normas brasileiras e opções A/B/C.
- `M06-02_MATRIZ_FUNCIONAL_REMEDIOS.csv`: **12 unidades de função institucional**, com titulares, custos, prova, urgência, efeitos e relações `CF-NOR-0007` H / `CF-NOR-0031` PR59.
- `M06-02_TESTES_REMEDIOS.csv`: **22 cenários adversariais**, não testes empíricos medidos.
- Direito brasileiro via CF/1988 LXVIII–LXXIV e LXXVII, Lei12.016/2009 MS, Lei13.300/2016 MI, Lei9507/1997 HD, Lei4717/1965 ação popular, STF ADI4296 2021, STJ Tema1178 2026. Comparações África do Sul e CADH sem equiparar autoridades.
- **Achado crítico:** STF ADI 4296 invalidou restrições a liminares de MS, inclusive oitiva prévia obrigatória em MS coletivo. Rito de tutela urgente não é simples formalidade dispensável.
- Não editar `redacao/` nem promover H→D por pesquisa.

## PENDENTE / NÃO VERIFICADO
- Acórdão integral STF ADI4296 e detalhes de todos dispositivos anulados; interpretação completa do STF/STJ sobre HC substitutivo, HD e MI.
- Dados reais CNJ/Defensorias, custos, temporalidade e execução das medidas; impacto de prazo ordinário MS 120 dias e HD 10/15 dias se a Constituição mudar; direitos de terceiras pessoas e tutela coletiva.
- Parecer crítico específico sobre PR59 privacidade/dados (atual PR draft); articulação com M07/M12/CLF.
- CI estrutural do HEAD final deste PR a confirmar após gravar arquivos; validação não atesta equivalência jurídica.

## PRÓXIMO
**Prioridade:** emitir parecer M06 para PR59 sobre habeas data, reserva de domicílio/comunicações e técnicas urgentes, a partir deste inventário; depois propor M06.03 sobre tutela coletiva, Defensoria e dados reais. Reservar o código M06.03 com busca de issues/PRs atual.
**Interfaces:** M00, M01, M05, M07, M09, M12, M13, M14, CLF T07.M03. **Critério de saída futuro:** matriz material N:N de garantias vigentes × redação, com prova de equivalência de acesso, urgência, prova e execução.

## Handoff adicional — parecer M06 para PR59, 14/10/2026

**Base verificada:** CF main `50b498885e17fa1709e66b0861f40e5387b4f4b0`; PR59 head `62161a6b9eb7dc62aad6efe4c914b1bd85fee411`; PR62 pesquisa draft.
**FEITO:** `M06-02_PARECER_INTERFACE_PRIVACIDADE_PR59_v0.1.md` examinou textos literais `CF-NOR-0030` e `0031` em H, concluiu pela necessidade de reservas especiais e tutela equivalente ao habeas data, mas **não** aprovou nem rejeitou definitivamente as duas cláusulas. `M06-02_MATRIZ_PARECER_PRIVACIDADE.csv` acrescentou **16 verificações conceituais**, com riscos/links M07/M12. Foram consultados CF art5, Lei 9507 arts7–8 e LGPD arts4/6/18/20 e STF ADI 6387/6649, com limites de autoridade explicitados.
**PENDENTE:** exames integrais do STF, redação especial de domicílio/interceptação, comparação granular com HD, supervisão institucional e análise de privacidade de terceiros. Falta parecer de M07/M12; o PR59 segue draft. **PRÓXIMO:** repassar recomendações de 10 controles ao PR59 e issue #57, elaborar alternativas de salvaguardas H pela frente M01.13 após conferência de IDs. Esta pesquisa **não** ocupa código M06.03, reservado para eventual estudo de tutela coletiva. **QA:** conferir CI no HEAD após atualizar.

## Rodada de crítica P2 às especialidades E-DOM/E-COM/E-HD — 14/10/2026

**Preflight:** `main=a763f5edf058a6622cd3d239efa6bf8e77b46e09`, texto examinado `M01-13_MINUTA_INTEGRADA_ESPECIAIS_DOM_COM_HD_v0.1.md` no PR59. **Estado:** parecer M06 com interfaces penais M12 **não revisado formalmente por M12**; sem H canônica nova ou D.

**FEITO:** `M06-02_PARECER_CRITICO_ESPECIALIDADES_DOM_COM_HD_P2_v0.1.md` com 13 recomendações de redação, alternativas P2 para domicílio, comunicação/celular e habeas data, e `M06-02_MATRIZ_PARECER_ESPECIALIDADES_P2.csv` com **18 verificações**. Fontes STF Temas 280 e 977, STJ HC598051/SP (6ª Turma; **não precedente obrigatório universal**), CF art5 e Lei9507. Detectado defeito lógico da fórmula "ingressar contra vontade salvo consentimento"; proposta de substituir por "sem consentimento ... salvo exceções constitucionais", com prova de voluntariedade. **E-COM ainda BLOQUEADA**: exceção estreita de encontro fortuito deve tratar somente identificação do autor/proprietário e não ser autorização geral, enquanto preservação técnica ≠ exploração de dados; delimitar juridicamente após exame M12. E-HD protege gratuidade, acesso/correção e examina anotação de contestação.

**PENDENTE:** parecer efetivo M12 e M07, escolha sobre constitucionalizar excepcionalidade STF977, acórdãos integrais quando necessário, controle de provas e sigilo de terceiros, harmonização CF-NOR0030/31 H em PR59 e risco de omissão do direito vigente. **Sem equivalência certificada.**

**PRÓXIMO:** devolver parecer ao PR59/issue #57, exigir revisão M12 da redação de E-COM e compatibilizar com M06 (prova, nulidade e controle), só então considerar criação de fichas especiais H com IDs disponíveis e fonte única. CI do SHA final da branch M06 a confirmar.
