# Diario de decisiones, plantilla del .md vivo, vigilancia y hand-off al PDF

## Por qué existe el diario
Es lo único que convierte **experiencia en sabiduría**. Sin un registro escrito EN EL MOMENTO de
decidir —con la tesis, el edge y el gatillo tal como los veías entonces— la memoria reescribe la
historia a tu favor. Registras para poder revisarte **sin piedad** y aprender de verdad.

Dos artefactos:
- **`tesis-<TICKER>-<AAAA-MM-DD>.md`** — el documento vivo (plantilla abajo).
- **`assets/diario-decisiones.csv`** — UNA fila por decisión, acumulado. El cuaderno de vuelo.

---

## Plantilla del .md vivo (secciones OBLIGATORIAS)

La bitácora es cruda en forma, pero nunca vacía en fondo. Sin plantilla, el vacío estructural produce
esqueletos — el "mamarracho" que Felipe rechaza. Secciones mínimas:

1. **Cabecera de ESTADO** (arriba del todo): veredicto actual · gatillo maestro en 1 línea · **régimen
   de datos** [filings/MCP verificado | solo-web degradado] · versión.
2. **Changelog**: entrada fechada por revisión — {qué cambió, motivo (dato nuevo / corrección / cambio
   de opinión), impacto en veredicto}. **El .md nunca se sobreescribe en silencio.** Los hallazgos que
   contradicen la tesis se conservan VISIBLES entre versiones — nunca se borran.
3. **Fase 0 desarrollada**: frase del círculo completada CON dato · tasa base con cohorte + N + % +
   fuente · precedente propio ("antecedente, no garantía").
4. **Fase 1 completa**: 3 razones con dato · narrativa causal fechada · supuestos del pre-mortem ·
   primera ficha del dominó.
5. **Un bloque por paso 1-9**, cada uno con su entregable mínimo y su veredicto.
6. **Cierre de Fase 2**: tabla de rutas del pre-mortem (refutada/confirmada/parcial) + contradicciones
   entre pasos resueltas + (si COMPRAR) el cierre adversarial con ambos números (bruto y post-ataque).
7. **Fase 3**: veredicto + **la disidencia que sobrevive** + **¿qué queda por saber?** (3-5 preguntas
   con evento/fecha + el hueco del modelo).
8. **Supuestos congelados vN** (al cerrar Fase 2): los 3-6 supuestos que, si cambian, cambian el
   veredicto — (supuesto | valor | qué lo movería/refuta).
9. **Lagunas declaradas** — los cabos que la tesis usa pero no pudo verificar.

## Checklist de completitud (correr ANTES de emitir la Fase 3)

Lo que falte es la siguiente ronda de trabajo — **el veredicto no se emite incompleto**:
☐ 3 razones del pre-mortem con dato, una en narrativa causal fechada · ☐ primera ficha del dominó
identificada y cableada a canario · ☐ palanca unitaria con número · ☐ tasa base con cohorte y fuente ·
☐ frase del edge completa, [HECHO], con corroboración independiente · ☐ "¿quién está del otro lado?"
respondida · ☐ arquetipo declarado y detector de trampas corrido · ☐ tabla de supuestos del
conservador completa · ☐ DCF inverso con protocolo de 4 pasos a la vista · ☐ EPV declarado · ☐ gatillo
maestro + tablero de canarios + sensor faltante + matriz P×I · ☐ 3 escenarios con probabilidades y
asimetría con fórmula · ☐ termómetro de ciclo etiquetado · ☐ contradicciones entre pasos resueltas ·
☐ changelog al día · ☐ disidencia superviviente escrita · ☐ "¿qué queda por saber?" con eventos ·
☐ fila CSV lista con las 18 columnas.

---

## Esquema del CSV

Columnas (en este orden). Añade una fila al decidir; no edites filas viejas — si cambia la tesis, es
una fila nueva con nueva fecha y motivo (la re-forja del MISMO día, antes de que Felipe decida, puede
actualizar la fila con el changelog del .md como rastro).

| Columna | Qué va |
|---|---|
| `fecha` · `ticker` · `empresa` | Identidad |
| `accion` | PASO / VIGILAR / COMPRAR_INICIAL / COMPRAR_AGRESIVO / VENDER / AÑADIR (enum CERRADO — nada de "EVITAR"/"ALERTA") |
| `tesis_1frase` | La tesis en una frase |
| `percepcion_variante` | "El mercado cree X, se equivoca porque [HECHO]" |
| `gatillo_falsable` | Gatillo maestro + canarios clave (métrica+umbral+fecha/cadencia) |
| `precio` | Precio el día de la decisión (+ moneda) |
| `asimetria` | Con fórmula; si es <1:1 se reporta el negativo tal cual |
| `mos` | % vs escenario CONSERVADOR (declarar si es negativo) |
| `tasa_base` | La vista exterior en una línea |
| `conviccion` | 1-5 (5 = rara claridad) |
| `tamano_pct` | Peso objetivo (o plan de tramos) |
| `2a_mejor_idea` | Contra qué compitió (incluye SIEMPRE al índice como alternativa por defecto) |
| `disidencia` | La objeción superviviente (si es "ninguna" → bandera de sesgo) |
| `condicion_reentrada_o_ascenso` | PASO/VIGILAR: qué me haría volver (permanente vs re-evaluable); COMPRAR: condiciones de ampliar |
| `regimen_datos` | filings/MCP verificado | solo-web degradado |
| `revision_12m` | (a los 12 meses) qué pasó, qué aprendí |

**Autovalidación pre-fila:** acción dentro del enum · asimetría con signo correcto · gatillo con
métrica+umbral+cadencia · MoS declarado contra el conservador · disidencia no vacía.

---

## Entre la decisión y los 12 meses (la vigilancia que faltaba)

El pre-compromiso sin patrulla es letra muerta: el gatillo puede saltar meses antes de que alguien
mire. Tres mecanismos:

1. **Patrulla de gatillos** — bajo pedido ("revisa mis gatillos"), tras resultados trimestrales o en
   un drawdown: recorrer las filas abiertas del CSV y contrastar cada métrica+umbral y los canarios
   contra datos primarios frescos. Salida por posición: **INTACTA / EN ALERTA (se acerca al umbral) /
   GATILLO SALTÓ → ejecutar lo pre-comprometido, sin re-litigar.**
2. **Protocolo de drawdown (mecánico):** caída ≥20-25% **desde el MÁXIMO** (jamás desde tu coste —
   anclar al precio de entrada es el error de contabilidad mental más caro; el coste solo sirve para
   impuestos) reabre la tesis desde la Fase 0 como tesis nueva. *El drawdown es una alarma, no un
   veredicto:* tres lecturas posibles (deterioro real / oportunidad / precio aún insuficiente) que
   solo el trabajo distingue. Vocabulario: ampliar / mantener / salir + fila nueva en el CSV.
3. **Mini-ritual por earnings** (posiciones abiertas): 3 líneas — qué predije / qué pasó /
   interpretación (**Acertado / Corregido / Refutado**). Es la calibración de cadencia corta que
   convierte cada trimestre en dato de aprendizaje.

## Revisión a 12 meses (el cierre profundo)

Para cada fila con ≥12 meses: ¿se cumplió la tesis? ¿el gatillo saltó y actué? ¿mi convicción estaba
calibrada (las de 5 rindieron más que las de 3)? ¿promedié a la baja sin re-verificar? ¿las preguntas
de "¿qué queda por saber?" se respondieron y en qué dirección? Anota en `revision_12m`.
**Regla anti-saturación:** si >50% de las tesis del diario salieron COMPRAR, se endurecen los umbrales
del proceso EN FRÍO (sesión aparte editando la skill) — nunca se re-juzgan casos a mano.

## Protocolo de re-forja (versionado sin autoengaño)

Al reabrir una tesis (por gatillo, drawdown o revisión):
1. **Auditar los supuestos congelados** de la versión anterior: CONFIRMADO / PARCIAL / REFUTADO.
2. **Re-anclar todas las cifras** a la base vigente — prohibido reciclar números viejos como [HECHO].
3. Conservar VISIBLES los hallazgos que contradicen la tesis (nunca se borran entre versiones).
4. Cerrar con "cabos sueltos para la próxima versión".
5. **Regla espejo:** una vN+1 que SUBE el valor debe citar la evidencia nueva que lo justifica — "no
   basta con que el precio se haya movido".

## Lógica de sizing (resumen; la escala completa y sus candados están en SKILL.md)
- 5 filtros para el tier; candados de degradación (flaquea/cuarentena/régimen de datos) topan el tier.
- MoS cuantificado: suficiente ≥25% / amplio ≥40% sobre el conservador. Asimetría con fórmula.
- COMPRAR_AGRESIVO exige ≥2 señales de extremo documentadas + detector de trampas en PASA.
- Candados: 2ª mejor idea (incluye índice) · nunca promediar sin re-verificar POR ESCRITO · pérdida
  permanente fija el techo · techo de múltiplo (regla de hierro 7) · umbrales no negociables en caliente.

---

## Hand-off al PDF (paso OPCIONAL, solo bajo pedido)
El PDF no es requisito para decidir. Solo si Felipe lo pide explícitamente:
- **Narrativa larga (el formato que Felipe validó):** el ensayo de 40-100+ págs que enseña con
  metáforas y ejemplos. Escribe un `caps_<ticker>.json` según **`references/narrativa-pdf.md`** y
  córrelo con `scripts/build_narrativa.py`. Es la ruta por defecto para una Ultra Tesis de convicción
  — Felipe ya rechazó una vez el PDF técnico de 12 págs.
- **Estilo Economist (casa), formato corto:** delega en el motor probado de `ultra-tesis-qg`
  (`references/diseno.md` + `scripts/` ReportLab, fondo crema, flag rojo). Pásale el `.md` vivo como
  contenido; NO reconstruyas el motor.
- **Estilo Anthropic:** usa `anthropic-skills:pdf` (o `docx`) con el branding de Anthropic.
En todos los casos el PDF **presenta** la tesis ya forjada — no re-decide nada.
