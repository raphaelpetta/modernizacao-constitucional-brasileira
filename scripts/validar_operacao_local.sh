#!/usr/bin/env bash
# Validacao documental offline da CF: nao valida conteudo juridico.
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/validar_repositorio.py
python3 scripts/gerar_anteprojeto.py --check
python3 -m unittest discover -s tests -p 'test_redacao_integrada.py' -v
python3 scripts/controle_operacional.py --check
echo "OK DOCUMENTAL LOCAL CF (nao certifica revisao juridica nem Actions)."
python3 -m unittest discover -s tests -p 'test_controle_operacional.py' -v
