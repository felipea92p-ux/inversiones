# Backup del skill qg-seilern (v1 · 1-jul-2026)

Copia de respaldo del skill que vive en `~/.claude/skills/qg-seilern/` (local de la Mac).

## Cómo restaurarlo en una máquina nueva
1. Instalar Claude Code / Cowork.
2. Copiar la carpeta `qg-seilern/` de este backup a `~/.claude/skills/`:
   `cp -R qg-seilern ~/.claude/skills/`
3. Listo — se activa solo al pedir rankings/auditorías de calidad QG.

## Fuente de verdad de la calibración
`INVESTMENTS/Research/QG_Sistema/decisiones_calibracion.md` (64 decisiones).
Si se cambia un umbral ahí, hay que actualizar `references/rubrica.md` del skill.

## Regla de mantenimiento
La copia VIVA es la de `~/.claude/skills/`. Este backup se refresca manualmente
tras cada cambio del skill (pedirle a Claude: "refresca el backup del skill qg-seilern").
