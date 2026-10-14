---
name: val-mos
description: >-
  Sistema propio de Felipe para el EJE VALORACIÓN: valor intrínseco (PWFV-Valor con owner earnings
  y EPV), margen de seguridad escalonado por calidad, detector de trampas de valor y biblioteca de
  patrones de superinversores. CONSUME el output del skill qg-seilern (exige score QG vigente).
  Úsalo SIEMPRE que Felipe pida valorar una empresa, calcular valor intrínseco / precio objetivo /
  MoS, saber si algo "está caro o barato", si es momento de comprar, detectar trampas de valor,
  buscar oportunidades de "ultra calidad a buen precio", cruzar el ranking QG con precio, o revisar
  la watchlist. Este skill mide el EJE PRECIO; NUNCA puntúa calidad (eso es qg-seilern) — los dos
  ejes se calculan por separado y se cruzan al final.
---

# Sistema VAL-MOS — Valor intrínseco, MoS y oportunidades certeras (v2)

Calibrado con Felipe (25 decisiones, 1-2 jul-2026) sobre dos investigaciones convergentes: 30+
grandes apuestas históricas de superinversores + informe propio de Felipe. Espec viva:
`INVESTMENTS/Research/Valoracion_Sistema/decisiones_valoracion.md` (referencia, no dependencia).

**v2 (2-jul-2026):** corrige la sobre-severidad de v1. Valor por ARQUETIPO de negocio; EPV como
suelo (peso 0 en el ancla); múltiplos DENTRO del ancla; WACC escalado por tier de calidad. Ver
`references/metodologia.md`. Regla de oro del enfoque QG: **no se exige descuento deep-value a un
compounder; se exige múltiplo de entrada razonable + runway largo + ROIC alto** (la matemática del
compounding, no la de Graham).

## Regla de oro
**CALIDAD ≠ PRECIO, físicamente separados.** Este skill EXIGE como input un score QG /100 vigente
del skill `qg-seilern` (tier Núcleo ≥85 / Alta convicción 75-84 / Sólida 65-74 / Watchlist <65).
Si la empresa no tiene score QG, corre qg-seilern primero. **Watchlist QG no se valora para
comprar** (fuera del universo comprable).

## Orden de aplicación EXPLÍCITO (anti-conflictos, decisión de Felipe)
```
0. Score QG vigente (input obligatorio) — knock-outs QG ya aplicados
1. DETECTOR DE TRAMPAS (references/trampas.md) → TRAMPA = VETO · GRIS = restricciones · PASA
2. VALORACIÓN (references/metodologia.md) → DCF inverso primero, PWFV-Valor, zonas
3. MoS POR TIER + CANDADOS (escalera 15/25/35, techo 35x/30x/25x, EPV>60%→GANGA, vía sin crisis)
4. SOBRECARGO TURNAROUND (solo deterioro cíclico confirmado dentro del universo QG)
5. ASIMETRÍA ≥3:1 (último filtro universal)
6. PATRONES (references/patrones.md) → SOLO amplifican convicción/tamaño, nunca generan la señal
```
**La asimetría y los patrones NUNCA anulan un veto del detector** — no hay vías de escape.

## Flujo por modo
- **valorar** (1-N empresas): ficha completa por empresa → veredicto COMPRAR TRAMO / VIGILAR /
  ESPERAR / VETO-TRAMPA, con tamaño sugerido.
- **cruzar ranking**: toma el ranking qg-seilern, valora los tiers comprables (Núcleo + Alta
  convicción; Sólida solo si ya está en zona), produce la matriz calidad × precio.
- **watchlist**: mantiene PWFV-Valor y zonas vivas de las top ~15 del ranking; refresco
  trimestral; alertas −25% (revisar/clasificar) y −35% (candidata a tramo) desde máximo 52s.
- **revisar cartera**: detector de trampas trimestral sobre posiciones IBKR + gatillo drawdown
  >25% **desde máximo histórico/52s, NO desde costo** (en ganadores antiguos el costo es inerte).

## Datos
Misma disciplina que qg-seilern (`~/.claude/skills/qg-seilern/references/datos.md`): HECHO solo
con filing primario o MCP financiero cuyo dato origina en filings auditados; forward/consenso =
INFERENCIA de terceros; web suelta nunca es HECHO. Precio actual y consenso: citar fuente y fecha.
Dato clave sin verificar → la cifra que dependa de él se marca DEGRADADA y el veredicto no puede
ser COMPRAR (máximo VIGILAR).

## Ritual de compra (obligatorio, paquete completo)
Toda recomendación de COMPRA del skill debe incluir: (1) **frase-tesis**: «el mercado teme X; X
está mal dimensionado porque [dato verificable]»; (2) clasificación en 1 de las **5 condiciones
de oportunidad**; (3) **elemento falsable** escrito (qué dato verificable en tiempo real mataría
la tesis); (4) recordatorio de las 4 reglas anti-sesgo (no promediar sin re-verificar por escrito,
no vender compounder por ancla de precio, no apalancamiento, falsable previo). Los **PASES** se
registran igual que las compras (auditoría del detector cada 12 meses).

## Reglas de venta DUALES (nunca mezclarlas)
- **Núcleo / Alta convicción:** vender SOLO por deterioro de moat/tesis (detector en rojo). NUNCA
  por múltiplo caro (error Graham/GEICO, Templeton'39).
- **Sólida / casos GRIS:** vender además por valoración en zona BURBUJA (>35% sobre PWFV-Valor).

## Advertencia operativa
El skill ANALIZA y recomienda; **jamás ejecuta órdenes** ni mueve dinero. Sizing: tramos 3-5% del
NAV; categoría excepcional hasta 15% NAV solo con [pánico general + Núcleo + GANGA + patrón claro
+ 0 señales de trampa + falsable escrito]. La vía sin crisis NO puede aumentar posiciones >20% NAV.

## Referencias del skill
| Archivo | Contenido |
|---|---|
| `references/metodologia.md` | PWFV-Valor, EPV, DCF inverso, checks anti-Damodaran, zonas, escalera MoS, candados |
| `references/trampas.md` | Detector ternario, 6 señales estructurales, checklist 15, test decisivo, burbuja sectorial |
| `references/patrones.md` | P1-P8 con señales de reconocimiento y gatillos (divergencia, VIX, autoinfligido, tamaño) |
| `references/output.md` | Ficha por empresa, matriz calidad×precio, formatos CSV/HTML, registro de decisiones |
