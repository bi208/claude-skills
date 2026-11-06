#!/usr/bin/env bash
# Gera um .zip por skill em dist/ para subir no claude.ai (Configurações → Capacidades → Skills)
# ou nas skills da organização. Uso: bash scripts/empacotar_zips.sh [plugin]
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
for plugin in plugins/${1:-*}; do
  name=$(basename "$plugin"); mkdir -p "dist/$name"
  for skill in "$plugin"/skills/*/; do
    s=$(basename "$skill")
    (cd "$plugin/skills" && zip -qr "../../../dist/$name/$s.zip" "$s" -x '*/evals/*')
  done
  echo "$name: $(ls dist/$name | wc -l) zips"
done
