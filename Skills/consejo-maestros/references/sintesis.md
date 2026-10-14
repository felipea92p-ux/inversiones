# Síntesis — de los dos ejes + el debate de lentes a un veredicto de convicción /100

La convicción NO es un cuarto score independiente: es una **función de los dos ejes congelados**,
afinada por los empujones acotados del Consejo y recortada por los gates. El diseño garantiza que
ninguna suma de escuelas desborde la disciplina de calidad+precio.

## Paso 0 — Precondición (sin esto no hay convicción)
Se requieren, congelados: **tier QG** (qg-seilern) y **veredicto MoS + detector + asimetría** (val-mos).
Falta uno → se manda al skill de origen. Nunca se estiman.

## Paso 1 — Base de los dos ejes (0–70)
La base sale de la confluencia calidad×precio ANTES de que hable ninguna lente:

| | Zona Ganga | Zona Oportunidad | Zona Justo | Zona Caro/Burbuja |
|---|---|---|---|---|
| **Núcleo QG ≥92** | 70 | 62 | 48 | 30 |
| **Núcleo QG 85–91.9** | 66 | 58 | 45 | 28 |
| **Alta convicción 75–84** | 58 | 50 | 38 | 24 |
| **Calidad sólida 65–74** | 46 | 38 | — (no se compra fuera de Ganga/Oportunidad) | — |

- Si `val-mos` dio **VETO-TRAMPA** → base = VETO, no se continúa.
- Si el **MoS exigido no se cumple** en la zona actual → base topada a máx 40 (convicción baja), aunque
  la calidad sea Núcleo. El precio manda sobre la convicción de compra.
- Si la **asimetría < 2:1** → base topada a máx 45 (el precio ya pagó la calidad).

## Paso 2 — Empujones del Consejo (acotados)
Suma de empujones de las lentes bottom-up y del overlay, con **tope duro agregado de ±18**:

    empujón_total = clamp( L1 + L2 + L3 + L4 + L5 , −18 , +18 )

- L1 (ciclo): −8..+8 · L2 (factorial): −10..+6 · L3 (GARP): −6..+6 · L4 (contrarian): 0..+10 ·
  L5 (scuttlebutt): −5..+5.
- El clamp a ±18 es deliberado: **el coro de escuelas nunca mueve la convicción más de ~18 puntos** sobre
  la base de los dos ejes. Las escuelas afinan; no reescriben calidad ni precio.
- Todo empujón apoyado solo en SUPUESTO se reduce a la mitad de su rango antes de sumar.

## Paso 3 — Gates (solo restan; nunca suman)
Se aplican DESPUÉS de los empujones, sobre el subtotal:

- **L6 (benchmark Bogle):** si la tesis no bate creíblemente a un índice de bajo coste tras costes e
  impuestos → **−0 a −12** y **acción topada en VIGILAR**. Exige escribir retorno esperado tesis vs. índice.
- **L7 (temperamento / coste de oportunidad):** sesgo conductual detectado o, en modo priorizar, existe
  una idea claramente superior con el mismo capital → **−0 a −10**.
- **Bandera de coherencia (L2):** divergencia factorial a la baja → ya incluida en el empujón de L2, pero
  además **impide** que la convicción entre en el tramo "máxima" (≥85) hasta re-verificar la regla en
  cuestión.

## Paso 4 — Convicción final y clamp
    convicción = clamp( base + empujón_total − gates , 0 , 100 )

Redondeo a entero. Nunca supera 100 ni baja de 0. Si algún **candado heredado** de val-mos está roto
(trampa / candado duro / MoS), la convicción se fija en su tope correspondiente **con independencia** de
lo que sumen las lentes — el candado gana siempre.

## Paso 5 — Mapeo a acción

| Convicción | Etiqueta | Acción (subordinada a los candados y al sizing de val-mos) |
|---|---|---|
| ≥ 85 | Convicción máxima | Tramo pleno / sizing excepcional SOLO si val-mos y régimen FRÍO ya lo permitían |
| 70–84 | Convicción alta | COMPRAR TRAMO en zona · 3–5% NAV |
| 55–69 | Convicción moderada | ACUMULAR EN ZONA · tramo reducido |
| 40–54 | Convicción baja | VIGILAR · documentar qué la subiría |
| < 40 | Sin convicción | ESPERAR |
| — | VETO | VETO-TRAMPA (heredado de val-mos) |

La convicción **jamás** autoriza un tamaño mayor al que `val-mos/mos_sizing.md` permitía para ese tier y
zona. Sube la *confianza*, no el *techo de riesgo*.

## Paso 6 — Ritual de decisión (obligatorio si la acción es de compra)
Toda recomendación COMPRAR/ACUMULAR debe traer, por escrito:
1. **Frase-tesis:** *"el mercado cree X; X está mal dimensionado porque [dato verificable HECHO]."*
2. **Escuela(s) dominante(s):** qué lente(s) lideran la convicción (p. ej. L4 contrarian + L1 ciclo FRÍO).
3. **Elemento falsable:** qué dato en tiempo real, con métrica + umbral + fecha, mataría la tesis.
4. **La disidencia más fuerte:** la objeción de mayor peso del Consejo, escrita — nunca se oculta la voz
   que estuvo en contra. Si ninguna lente disintió, decláralo explícitamente (señal de posible sesgo de
   confirmación → cruza con L7).
5. **Recordatorio anti-sesgo (heredado de val-mos):** no promediar a la baja sin re-verificar por escrito;
   no vender un compounder por ancla de precio; sin apalancamiento sobre tesis volátil; falsable ANTES de
   comprar, no después.

## Nota de calibración
La base (Paso 1) es intencionalmente la que más pesa: en un caso típico, calidad×precio fija ~70% del
resultado y el Consejo afina el resto. Si al calibrar se observa que las lentes deciden más que los dos
ejes, **baja el tope del clamp** (Paso 2), no ajustes casos a mano — misma disciplina anti-saturación que
qg-seilern y val-mos.
