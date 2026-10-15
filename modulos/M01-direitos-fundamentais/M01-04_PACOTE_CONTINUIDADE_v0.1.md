# M01.04 — Pacote de continuidade (CF-M01-S004)

**Data:** 13/10/2026. **Entrada:** `main` no commit `480bafa81902dd1a076a6863926477d3475eed89` e M01.01–M01.03 da branch do PR #22, não integrada à main.  
**Status:** F0–F5 e testes preliminares; **sem deliberação de conteúdo constitucional**.

## Arquivos pesquisados

Conferida situação do GitHub (`main`, PR #22 e árvore). Retomados M01.01–M01.03, a metodologia e a auditoria de garantias do projeto. Fontes oficiais externas:

- STF: Informativos 405 (RE 201.819) e 502 (HC 94.016); Temas 987/533 (inclusive ajuste final de 17/06/2026) e 1.031.
- CF/1988 atualizada; OIT Convenções 111 e 169 (esta no Decreto 10.088/2019, Anexo LXXII).
- África do Sul: Bill of Rights §8; decisões constitucionais `AB v Pridwin`, `Daniels v Scribante`, referência a `Juma Musjid`.
- Alemanha: GG art. 19(3) e `Lüth`; Portugal CRP art.18; ONU 2011, Princípios Orientadores de Empresas e Direitos Humanos.

Links e diferenças de autoridade estão no dossiê. O relatório da jurisprudência de plataformas de 2026 **não** significa direito universal de acesso a redes sociais ou aplicação automática do devido processo judicial a plataformas privadas.

## Entregas

1. `M01-04_TITULARIDADE_E_EFICACIA_HORIZONTAL_v0.1.md`: seis categorias de titulares; seis graus funcionais de dever (D0–D5); revisão crítica de enunciados do M01.03; separação entre Constituição, lei, regulamento e jurisdição.
2. `M01-04_CASOS_TITULARIDADE_HORIZONTALIDADE.csv`: 16 casos distintos, direitos, sujeitos, mecanismos, contraprovas, fonte e módulo.
3. Este pacote de continuidade.

## Achados jurídicos e riscos

- Distinção tripla obrigatória: **titular do direito ≠ destinatário do dever ≠ legitimado processual**.
- O STF Tema 1.031 afirma capacidade civil/processual indígena: povos e comunidades não dependem de personalidade jurídica privada. Revisar "poderão ser titulares" do protótipo M01.03 por parecer concessão de direito atualmente originário.
- Assimetria de poder é fator de intensidade, **não pressuposto** para vedar violações de privacidade, violência ou discriminação entre particulares.
- Empregador, hospital contratado, plataforma e associação têm deveres diferentes; dever estatal de assegurar acesso universal a sistemas sociais não se transfere automaticamente.
- Direitos das futuras gerações exigem representação, prevenção e tutela, mas a adoção de personalidade jurídica atual para pessoas futuras não foi escolhida.
- Pessoas jurídicas públicas não são equiparadas a sujeitos humanos para invocar dignidade corporal; proteger autonomia institucional/federativa em categoria apropriada.
- Regime de provedores do STF sofreu ajustes em 17/06/2026; impedir desatualização de documentos anteriores. Verificar acórdão integral do RE 201.819 e textos integrais dos Temas 987/533 no aprofundamento.

## Estado decisório

| Questão | Estado | Ratificação |
|---|---|---|
| M01-Q01 — pessoas humanas; titularidade universal diferenciada | P de pesquisa | Não |
| M01-Q02 — incidência horizontal calibrada por natureza do direito/dever | P de pesquisa | Não |
| M01-Q09 — pessoas jurídicas por compatibilidade material | P de pesquisa | Não |
| M01-Q10 — direitos coletivos próprios, sem obrigatoriedade de PJ | P de pesquisa | Não |
| Direitos extraterritoriais, grupos e legitimação, menores, serviços digitais | A/V | Não |

O pedido de prosseguimento de pesquisa foi cumprido, sem assumir aceitação de texto. **Não criado CF-NOR**, nenhuma cláusula declarada final e nenhuma equivalência de garantias atestada.

## Interfaces e verificação

- M00/M03: titularidades versus espécies e reserva legal, delegação; M06: legitimidade/ações; M07/M08: serviços e plataformas; M09: proteção do trabalho/saúde/educação; M10: gerações futuras; M11: direitos indígenas; M12: segurança; M13: estrangeiros e tratados; M14: proteção intertemporal.
- Faltam: acórdão integral de RE 201.819; análise de jurisprudência recente trabalhista/empresarial; modelagem de dever privado de contestação/explicação em decisões automatizadas; exame de direitos fundamentais de entes públicos; avaliação de impactos distributivos/judiciais; harmonização específica com artigos sobre deveres de prestação.

## Próximo ciclo M01.05 sugerido

Construir **auditoria aprofundada dos direitos da personalidade e da igualdade** já identificados (vida, corpo, privacidade, dados, não discriminação, autonomia pessoal, tutela diante de empresas e Estado). Em paralelo, pedir integração dos testes M01.04 com M06/M07/M09/M11, documentando efeitos na matriz N:N. Se houver deliberação das opções M01-Q01/02/09/10, só então emitir IDs CF-NOR para redação normativa final. Revalidar SHA main e PR no começo da próxima rodada.
