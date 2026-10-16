#!/bin/zsh
# Uso: ./sellar.sh <archivo> "<qué sella>"  — añade una fila a SELLOS.md con sha256 y hora UTC. Nunca sobrescribe un sello anterior.
set -e
F="$1"; Q="$2"
[ -f "$F" ] || { echo "no existe $F"; exit 1; }
H=$(shasum -a 256 "$F" | cut -d' ' -f1)
TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
N=$(($(grep -c '^| [0-9]' SELLOS.md) + 1))
printf '| %s | %s | %s | `%s` | %s |\n' "$N" "$F" "$Q" "$H" "$TS" >> SELLOS.md
echo "sellado #$N $F $H $TS"
