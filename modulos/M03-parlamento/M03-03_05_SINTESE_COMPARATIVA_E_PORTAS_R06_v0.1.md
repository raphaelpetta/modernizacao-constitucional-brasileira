# M03.03 R05 — Síntese crítica e controle comum A/B/F/S1/C3/I1
**Corte:** 15/10/2026 · PR #100 draft, hipóteses H/A/V. F6, ratificação D, redação CF-NOR e mudança de CF-DEC-006/CLF/main: NÃO realizados.

## 1. Qual resultado pode alterar nossa escolha?
Duas perguntas testam contribuição DIFERENCIAL, não fascínio por novidade:
- **S1:** a legitimação de governo por preferências transferidas proporciona maior compromisso entre representação, governabilidade e responsabilização do que A/B/F, DEPOIS de protegidos o veto da Câmara, o Senado territorial e a igualdade de deputados?
- **C3:** decisão colegiada com gabinete administrativo impede captura personalista de um modo que controles de nomeação, urgência, partido e oposição não conseguiriam fornecer a A/B/F mais simplesmente?
Não há contrafactual causal observado; cenários apenas identificam inviabilidades e mecanismos.

## 2. Quadro de validade das proposições
| Proposição | Resultado R05 | Natureza | O que ainda refutaria |
|---|---|---|---|
| Preferências secundárias podem mudar quem sustenta Executivo sem mudar cadeiras | Sim, para oito cenários artificiais sobre âncoras reais TSE | matemático-condicional, não eleição brasileira | método de ranking nacional/estadual incoerente, desiguais direitos e assentamento |
| Maioria final pode não virar maioria na confiança por arredondamento | Sim, q=48,5% gera PL50,263% mas 81×81 | defeito da implementação floor INGÊNUA, reconhecido como caso de borda da literatura | regra ímpar e de empate robusta sem distorção incompatível |
| S1 resolve impasse fiscal | NÃO demonstrado; PL99 ainda negocia leis para maioria | inferência lógico-jurídica | modelo SF1/SF3 aprova LOA por incentivos verificáveis sem esvaziar Parlamento |
| Colegialidade exige pluralidade partidária para evitar personalismo | C3 por maioria simples pode eleger 5/5 de coalizão 287 | possibilidade lógica | regras vinculantes de seleção, agenda e contrapesos independentes |
| Com seleção D'Hondt 5, pluralidade formal impede cartel | NÃO; PL2+União1 = 3/5 com 158/513 parlamentares somados | cálculo sob pesos da Câmara 2022, não eleição real do Conselho | regra de composição que equilibre diversidade e responsabilidade sem blindar grupos |
| Quórum reforçado elimina captura sem custo | NÃO; exigir 4/5 permite veto; exigir 3/5 permite bloco 3 | análise institucional | regra por objeto + controle externo que sobreviva crise sem arbitrariedade |
| I1 resolve rigidez do Presidente sem maioria | NÃO; troca origem, não mandato | inferência | ganho federativo/anticaptura específico comprovado |

## 3. Contraprovas devem preservar simetria
**A:** voto direto; mandato fixo; direção unipessoal e poderes normativos controlados. Aplicar mesmas salvaguardas externas M06/M07 que C3. Se A obtiver efeito anticaptura próximo ao de C3 com menos bloqueio, C3 perde valor adicional.
**B:** confiança, censura construtiva, chefe Estado separado; pressão fiscal sobre gabinete protegido é cenário equivalente a S1. Se B obtiver escolha identificável e Parlamento fiscal pleno com menos diferença de competências de deputados, S1 precisa demonstrar ganho.
**F:** presidente eleito pelo Legislativo e politicamente removível; F1 remove por maioria negativa com risco interinidade, F2 exige sucessor mas protege bloqueio. Sob regras equivalentes de anticaptura, comparar com C3 na clareza de comando e responsabilidade.
**I1:** caso contrafactual, não opção preferencial de redação: Presidente com mandato rígido e origem indireta requer vantagem específica que compense alteração de voto popular direto.

## 4. Restrições transversais que impediram “escolher vencedor”
- **Voto e representação:** dados de 2022 não representam eleição 2026 nem rankings. A origem do Executivo em S1/C3/F/I1 altera o significado do voto presidencial e pode afetar CF art. 60§4º II, art. 16 e mandatos; sem decisão do rito de mudança.
- **Senado/federação:** distrito nacional único da proposta Ganghof tensiona estados; Conselho de 5 não é automaticamente órgão federativo legítimo, nem pode controlar repasses sem título.
- **Orçamento:** 245/513 é abaixo da maioria absoluta, 287/513 acima; esses são apoios HIPOTÉTICOS, sem inferência de preferências programáticas. Nenhum modelo transforma falta de caixa em autorização legal.
- **Administração e defesa:** C3 só é colegiado real se Conselho decidir matérias materiais e ministro/delegado não for “presidente informal”; urgência conservatória exige fonte, prazo e controle; A/B/F também precisam de controles de urgência.
- **Proteção judicial:** tribunais verificam rito, direitos e legalidade, não substituem maioria partidária nem escolhem governante.
- **Resultado comparativo:** o S1 é mais distintivo em ORIGEM/representatividade dual; o C3, em CONCENTRAÇÃO interna; sua recombinação é teórica, mas somar S1+C3 automaticamente multiplica custos de coordenação/legitimação e NÃO foi testado como pacote.

## 5. Três alvos concretos de próxima rodada
1. **R06-S, M02/M04:** S1 em (N) voto nacional adicional de preferência, (E) derivação do voto estadual, (H) sistema compensatório UF/nacional; especificar a única cédula ou duas decisões, igualdade de voto, distribuição estadual e segundo órgão territorial. Usar dados abertos por UF, não somente 513 bancadas.
2. **R06-C, M07/M12/M06:** C3-P (proporcional), C3-E (mandatos escalonados), C3-R (colegiado responsivo), com mesmo pacote de atos, quóruns, conflito, cadeia de defesa, eleição/substituição, nomeações, anticaptura; variar origem e sobrevivência separadamente.
3. **R06-F, M05/M14:** definição de lei orçamentária transitória, crédito e encargo federativo sob todas arquiteturas, cenário de dois anos sem LOA, proteção de mandatos/plebiscito/consulta/via PEC versus constituinte.

## 6. Integração no projeto e cautela de QA
Os scripts S1 e C3 são reexecutáveis em Node puro e só dependem do CSV de dados histórico do TSE (cópia auditável). A execução do CI de PR apenas valida estrutura/repositório, não mérito de estatísticas nem juridicidade. As duas matérias devem ser revisadas pelas frentes M02/M04/M05/M06/M07/M12/M14 antes de qualquer F6/D. O método deve preferir **refutação de modelos** a abrir mais siglas sem ganho observável.

**FEITO:** contrafactuais com base real, sensibilidade S1 e contraprovas C3, roteiro objetivo de portas. **PENDENTE:** dados de UF, votos ordenados inexistentes, desempenho de coalizões, transição, equivalência das garantias, CI do HEAD final. **PRÓXIMO:** R06 com portas eleitorais/territoriais e governo colegial, e eventual consulta para preferência P; CF-DEC-006 permanece H/P.
