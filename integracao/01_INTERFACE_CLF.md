# Interface entre o projeto constitucional e o Código da Legislação Federal

**ID:** CF-INT-001 · **Versão:** 0.1 · **Status:** procedimento de pesquisa, não escolha material constitucional.

**Repositórios**
- CF: https://github.com/raphaelpetta/modernizacao-constitucional-brasileira
- CLF: https://github.com/raphaelpetta/codigo-legislacao-federal
- CLF: `docs/09_INTERFACE_CONSTITUCIONAL.md`, `catalogo/10_MATRIZ_COMPATIBILIDADE_CONSTITUCIONAL.csv` (34 interfaces históricas), `governanca/12_REGISTRO_INTERFACE_CONSTITUCIONAL.md`.

## Planos jurídicos
**A:** CF/1988 vigente, verificada em fonte oficial. **B:** Constituição nova hipotética, submetida à pesquisa e decisões deste repositório. **C:** CLF — codificação infraconstitucional independente e também hipotética. Nunca tratar B ou C como legislação vigente.

## Fluxo bilateral
CF → CLF: mudanças propostas em competências, espécies, garantias, instituições ou transições produzem nota `CF-IC-...`, condicionada e versionada, com impacto para títulos/módulos CLF. CLF → CF: problema demonstrado no mapeamento das leis gera pedido `IC-AAAA-NNN` com evidências, sem vincular decisão constitucional. Alteração em qualquer texto requer aprovação própria e rastreabilidade, não transferência automática de premissas.

A matriz CLF contém links por **artigos antigos** do anteprojeto constitucional v0.1. Se a arquitetura constitucional mudar, manter o identificador histórico da interface e registrar os novos IDs `CF-NOR-`, sem presumir correspondência de números.

## Estado adicional de integração (13/10/2026)

A metodologia v0.2 do CLF (PR #2) e a governança operacional v0.3 (PR #3) foram incorporadas à `main` daquele repositório. O novo repositório constitucional foi reconhecido pelo CLF no PR #8, commit `74e37ea35b96621cefce68fec2e61b59beeec959`. Em análises futuras consultar **o último commit de ambos** em vez de depender desta fotografia. A Constituição adaptou padrões de proveniência e QA em `governanca/10_PROVENIENCIA_E_IDS.md` e `.github/workflows/validar-estrutura.yml`, sem adotar categorias de codificação C0/C1/M/Q.
