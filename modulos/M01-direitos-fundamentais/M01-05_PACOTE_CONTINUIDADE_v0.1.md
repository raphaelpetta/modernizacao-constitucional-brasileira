# M01.05 — Pacote de continuidade (CF-M01-S005)

**Data:** 13/10/2026; **status:** F0–F5 + primeiros testes F8; nenhuma decisão constitucional material ratificada.  
**SHA de entrada main:** `92a1af3d4ca6fd0560d1a576f48079500ca519c5` (histórico de integrações paralelas M03/M04/M05 e CLF).  
**PR de trabalho:** #22 (draft) / branch `pesquisa/m01-01-catalogo-direitos-v01`, cumulativa de M01.01–M01.04.  
**Issue de referência:** #5.

## Arquivos/estado efetivamente lidos
- `governanca/03_DECISOES.md`, blob `e04874878e20dd399df3aba258730b9fd3aa8e0c`.
- `governanca/04_ESTADO_ATUAL.md`, blob `56308108db053473dc8cbd88ea70a9614f4d4543`.
- `modulos/M01-direitos-fundamentais/M01-03_ESCOLHAS_INSTITUCIONAIS_E_PROTOTIPOS_v0.1.md`, blob `39b98365194149df80599f78cafba426302d1d8e`.
- `modulos/M01-direitos-fundamentais/M01-04_TITULARIDADE_E_EFICACIA_HORIZONTAL_v0.1.md`, blob `7aa10bc2efef002709f2ad493f2d5a94d60fd752`.
- Referências metodológicas M00/M01 anteriores e fontes normativas/jurisprudenciais identificadas no dossiê M01.05.

## Entregas concluídas (pesquisa, não artigo homologado)
1. `M01-05_AUDITORIA_DIREITOS_DA_PESSOA_v0.1.md`: mapeamento focal de seis núcleos (vida, integridade, igualdade, autonomia, privacidade, dados), precedentes brasileiros e referências estrangeiras, oito matérias decisórias, seis protótipos **não normativos**, limites de transposição e prioridades de pesquisa.
2. `M01-05_MATRIZ_DIREITOS_E_TESTES.csv`: 24 casos adversariais discriminando titulares, obrigados, garantia, hipótese de tutela, objeção, fontes e interface.
3. Este pacote de continuidade.

## Achados rastreáveis

- Vida inclui proteção contra privação arbitrária e investigação/segurança; a proteção de gestação e embriões envolve controvérsias específicas: ADI 3.510 e ADPF 54 **não** decidem geral e definitivamente sobre aborto. Não foi verificado mérito final atualizado da ADPF 442 em outubro/2026; status processual pendente de conferência.
- Integridade física e psíquica demandam consentimento livre e esclarecido e disciplina excepcional de tratamento involuntário sem extrapolar o regime de medicina/biologia da Carta UE.
- Igualdade formal não veda todo tratamento diferenciado: ADPF 186 legitima ações afirmativas proporcionais; ADI 4277/ADPF 132 e ADI 4275 reconhecem direitos da identidade/família; ADO 26/MI 4733 requer distinguir direitos antidiscriminatórios de sanção penal concreta.
- Privacidade não se confunde com tratamento de dados pessoais: ADI 6387 referendou liminar de suspensão de MP de compartilhamento; EC 115/2022 reconheceu expressamente dados. Consentimento **não** é base única: Carta UE art. 8 permite outra base legítima na lei, mantendo princípios e autoridade independente.
- Técnicas específicas, como reconhecimento facial ou IA, não devem substituir garantias tecnologicamente neutras; seus efeitos concretos exigem tutela, limites, prova e fiscalização.

## Pontos materiais em aberto; nenhuma ratificação do usuário

| ID | Tema | Estado | Natureza |
|---|---|---|---|
| CF-M01-M01 | Proteção positiva do direito à vida e uso de força | A/P | Necessária articulação M12 |
| CF-M01-M02 | Integridade e consentimento médico | A/P | Precisa verificar leis e exceções |
| CF-M01-M03 | Igualdade direta/indireta e ação afirmativa | A/P | Verificar efeitos distributivos e ônus probatório |
| CF-M01-M04 | Autonomia, identidade e escolhas existenciais | A/P | Não antecipar aborto/fim da vida |
| CF-M01-M05 | Privacidade e limites especiais à vigilância | A/P | Reserva legal/judicial M00/M06/M12 |
| CF-M01-M06 | Dados pessoais, finalidade e fiscalização | A/P | Autoridade e processos M07 |
| CF-M01-M07 | Deveres positivos e remédios | A | M06/M09 |
| CF-M01-M08 | Colisões, reservas e limites | A | M00/M12 |

Os protótipos P-VIDA, P-INTEGRIDADE, P-IGUALDADE, P-AUTONOMIA, P-PRIVACIDADE e P-DADOS são **instrumentos de teste**, não redação da Constituição, não recebem `CF-NOR`. Nenhum direito da CF/1988 foi declarado materialmente equivalente, preservado por mudança de texto ou suprimido.

## Verificações adicionais necessárias

1. Decisões íntegras e situação mais recente da ADPF 442 (verificação de andamento de outubro/2025 não substitui consulta do mérito até 13/10/2026).
2. Jurisprudência STF e Corte IDH sobre uso da força, abortamento, cuidados paliativos/fim da vida, experimentação humana, capacidade civil e dever de prevenção; diferenciar precedente vinculante, decisão de turma, cautelar, parecer, texto normativo e interpretação acadêmica.
3. Aspectos específicos da LC/lei/lei regulatória sobre pessoas com deficiência, consentimento clínico, proteção de dados, intercepção, fiscalização de inteligência e uso policial de biometria.
4. Revisão conjunta M06/M07/M09/M12 sobre remédios, controle independente, financiamento, urgência e restrições penais.
5. Construir matriz N:N de todos os direitos afetados pela futura parte geral, inclusive fundos sociais e proteções setoriais.

## Proposta para o próximo ciclo
**M01.06 — Igualdade e não discriminação:** pesquisa dedicada a discriminação direta/indireta, categorias protegidas abertas, medidas compensatórias, adaptações razoáveis, dados e igualdade algorítmica; hipóteses de legislação e reparação sem compromisso normativo final. Em paralelo, revalidar integrações e checagens do PR #22 e considerar remessa de interfaces aos módulos afetados, sem transplantar decisões unilateralmente.

## Controle de qualidade
Os arquivos foram criados apenas na branch de pesquisa do PR #22. Confirmar após o último commit a validação `arquivos-e-modulos` e a ausência de conflito com a `main`; teste automatizado jamais comprova precisão do mérito jurídico ou da evidência empírica.
