# Metodo_Nuevo — índice del proceso de refundación (2026-07-19/20)

Esta carpeta es el **archivo del proceso**, no el método en sí. La skill que de verdad se usa vive en
`../Skills/qg-nucleo/` — separada, sin reemplazar a `Skills/metodologia-qg/` (v1), que sigue
activa. Aquí queda todo el trabajo que la fundamenta, para que puedas auditarlo sin tener que releer
la sesión completa.

## Empieza aquí

1. **`../Skills/qg-nucleo/CAMBIOS-VS-ORIGINAL.md`** — el resumen ejecutivo real: qué se
   conserva de v1, qué se añade, qué se corrige, qué muere, y el estado exacto de los 6 simulacros y
   las 8 enmiendas. Si sólo vas a leer un documento, es éste.
2. **`../Skills/qg-nucleo/SKILL.md`** — el método en sí, completo y operativo.

## Estado en una línea

6 simulacros históricos corridos, los 6 con el veredicto correcto (Amazon y Microsoft: COMPRAR;
Nokia, Coca-Cola, Groupon, GoPro: RECHAZAR). 4 de los 5 juegos de cifras que los sostienen ya están
verificados contra SEC EDGAR real. Las 8 enmiendas que el proceso produjo están en **cuarentena hasta
el 2026-08-19** por la propia constitución del método (Frontera F-1.0) — hasta entonces, sólo valen
para simulacros, no para una decisión de capital real.

## Documentación de fondo (`Documentacion/`)

**Nivel 2 — el fundamento, vale la pena leer si quieres entender el "por qué":**
- `DOSSIER.md` (212 KB) — el documento que más peso tiene. Núcleo rescatado de `metodologia-qg` v1,
  la "guillotina" de lo que se descartó y por qué, el banco completo de ~60 preguntas forzantes
  destiladas de 12 inversores legendarios, y las tensiones que quedaron sin resolver.
- `SIMULACROS.md` (52 KB) — el banco de casos históricos con desenlace conocido, diseñado antes de
  correr ninguno, con el veredicto correcto esperado para cada uno.

**Nivel 3 — el detalle técnico, útil si quieres profundizar en una pieza concreta:**
- `criterio-ultra-calidad.md` — la investigación que fundó las seis puertas de "ultra calidad" antes
  de que las enmiendas las corrigieran (el contenido vigente y corregido está en
  `Skills/qg-nucleo/references/ultra-calidad.md`, no aquí).
- `criterio-universo-preaprobado.md` — el mecanismo del universo pre-aprobado.
- `criterio-sizing.md` — la investigación detrás de la fórmula de tamaño y la caja.
- `criterio-venta-drawdown.md` — el protocolo de venta y la protección de CAYLA.
- `cimientos/` — tres informes de base: `cartera.md`, `valoracion.md`, `circulo.md` (la tensión del
  círculo de competencia entre CAYLA y tecnología).

**Nivel 4 — material crudo y de procedencia, normalmente no hace falta abrirlo:**
- `raw/` — los 16 informes originales (12 lentes de maestros + 4 auditorías) recuperados del primer
  workflow, que murió a mitad de camino por un corte de conexión. Se recuperaron del journal antes de
  que se perdieran.
- `fusion_raw/` — 9 informes recuperados de la segunda corrida, que chocó con el límite de gasto
  mensual de la cuenta a mitad de las 9 rondas adversariales.
- `arq-secuencial.md`, `arq-preguntas.md`, `arq-decisiones.md` (~120 KB cada uno) — las tres
  arquitecturas completas que compitieron entre sí antes de fusionarse en una sola. Interesante si
  quieres ver los caminos que NO se tomaron, pero no es el método vigente.
- `FUSION.md` — el borrador que quedó a medias cuando el segundo workflow murió (llegó hasta la
  sección 3 de 9). Superado por completo por `Skills/qg-nucleo/SKILL.md`; se conserva sólo
  como registro de cómo empezó la fusión.
- `backup/metodologia-qg-original-20260719-2202/` — copia de seguridad de `Skills/metodologia-qg` (v1)
  tal como estaba antes de empezar a fusionar, por si hiciera falta comparar o revertir.
- `motor.py`, `oe.py`, `inverso.py`, `smith.py` — scripts exploratorios de valoración escritos durante
  una corrida que no llegó a término. No forman parte del método final, que es enteramente en prosa
  (sin código ejecutable) por diseño — para que cualquier sesión de Claude pueda aplicarlo sin depender
  de un entorno de Python.

## Otros archivos en esta carpeta

- `METODO_v0.md` — el primer borrador acordado contigo, antes de descubrir que ya existía una
  refundación completa (`metodologia-qg` v1) corriendo en paralelo en otra sesión. Es donde nacieron
  varias de tus decisiones que sobrevivieron hasta el final: núcleo 3-9, tope 25%, la matriz de MoS de
  dos ejes, el candado anti-sobrepago mutado. Interesante como origen, pero superado en el fondo por
  `Skills/qg-nucleo/`.
