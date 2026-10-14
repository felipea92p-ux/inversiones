# ESPEC · ULTRA TESIS DECK EN PDF · arquitectura, API y reglas de estilo

**Directorio de trabajo (único):**
`/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build/`

Ahí están ya: `motor_qg.py` (motor de maquetación), `paleta_qg.py`, `chart_style.py`, `DATOS.md`
(fuente única de verdad numérica) y la carpeta `charts/`.

## EL ENCARGO, EN UNA FRASE
Un PDF editorial estilo *The Economist* —fondo crema, flag rojo, serif— que **enseña de lo más
sencillo a lo más complejo**, profundizando por capas, **con el peso del documento en la valoración**,
con gráficos y con aire suficiente para leerse de un tirón sin fatiga.

## PRINCIPIO PEDAGÓGICO — no negociable
El documento va en **cinco niveles de profundidad**. Cada nivel presupone el anterior y **ninguno
presupone el siguiente**. Un lector que abandone al final de cualquier nivel se lleva algo completo.

- **Nivel 1 · LA RESPUESTA** — el veredicto, sin razonamiento. 5 minutos.
- **Nivel 2 · EL NEGOCIO** — qué es Deckers, explicado sin un solo múltiplo ni una sola tasa de
  descuento. Aquí se enseña qué es un margen, qué es el ROIC y por qué importan. **Tono de profesor.**
- **Nivel 3 · LOS NÚMEROS** — qué está diciendo la trayectoria. Aquí ya se puede usar vocabulario
  introducido en el nivel 2, y sólo ese.
- **Nivel 4 · LA VALORACIÓN** — el corazón. **Debe ser el bloque más largo del documento.** Se
  construye paso a paso: primero qué significa valorar, luego cada insumo por separado, luego las
  matrices, luego las lecturas. Un lector sin formación financiera tiene que poder seguirlo entero.
- **Nivel 5 · EL JUICIO** — el nivel de calidad, el cruce adversarial, la decisión, los falsables.

**Regla dura:** ningún término técnico aparece sin haber sido definido antes, en el sitio donde aparece
por primera vez, en una frase. `owner earnings`, `NOPAT`, `ROIC`, `capital invertido`, `g₀`, `g∞`,
`terminal`, `MoS`, `N2/N3`, `DCF inverso`, `TIR`. Si un término se define en el nivel 2, en el nivel 4
se usa sin volver a explicarlo.

## ARQUITECTURA COMPLETA

| Módulo | Funciones que expone | Contenido |
|---|---|---|
| `contenido_1.py` | `portada()`, `como_leer()`, `seccion_1()` | Portada · Cómo leer · **§1 Veredicto** |
| `contenido_2.py` | `parte_2()`, `seccion_2()`…`seccion_5()` | **NIVEL 2 · El negocio** |
| `contenido_3.py` | `parte_3()`, `seccion_6()`…`seccion_10()` | **NIVEL 3 · Los números** |
| `contenido_4.py` | `parte_4()`, `seccion_11()`…`seccion_15()` | **NIVEL 4a · Valoración: los insumos** |
| `contenido_5.py` | `seccion_16()`, `seccion_17()`, `seccion_18()` | **NIVEL 4b · Valoración: matrices y lecturas** |
| `contenido_6.py` | `parte_5()`, `seccion_19()`…`seccion_24()`, `anexo()` | **NIVEL 5 · El juicio** + anexo |

### Índice de secciones
- **§1 · El veredicto, en una página** *(nivel 1)*
- **§2 · Qué compras cuando compras Deckers** — dos marcas, ninguna fábrica
- **§3 · Los tres márgenes, sobre una zapatilla de 150 dólares** — bruto, operativo, neto
- **§4 · El mapa del dinero** — marca, canal, geografía; unidades contra precio
- **§5 · Por qué rinde el 101% sobre el capital** — qué es el capital invertido y qué es el ROIC
- **§6 · Nueve trimestres: donde las dos líneas se cruzan**
- **§7 · Las dos empresas dentro de la empresa** — UGG defiende margen, HOKA lo pierde
- **§8 · Empuje contra tirón** — el canal, y por qué el mayorista creciendo el doble es una alarma
- **§9 · Promesas contra entregas** — el mejor activo cualitativo del expediente
- **§10 · El foso: qué defiende a Deckers y cuántos años**
- **§11 · Qué significa valorar una empresa** — la idea entera en una página, sin fórmulas
- **§12 · Primer insumo · Los owner earnings** — la cascada de 1.182,0 a 947,1
- **§13 · Segundo insumo · La tasa** — por qué 9,70% y por qué no se toca
- **§14 · Tercer insumo · El crecimiento** — `g₀`, `g∞`, y la regla del método que aquí se rompe
- **§15 · Cuarto insumo · El puente** — caja, deuda, acciones, y el arbitraje de los arrendamientos
- **§16 · Las tres matrices, celda a celda**
- **§17 · Las tres lecturas obligatorias** — la celda más dura, el DCF inverso, la TIR
- **§18 · La escalera de margen de seguridad** — de 121,36 a 66,75
- **§19 · El nivel: N2 o N3, y los veinticuatro dólares que decide**
- **§20 · El cruce 10c: diablo contra ángel**
- **§21 · La decisión y los seis campos del anti-limbo**
- **§22 · Los falsables**
- **§23 · Sesgos declarados**
- **§24 · Lo que esta tesis no puede resolver**
- **Anexo · Glosario y trazabilidad**

## GRÁFICOS · nombres de fichero EXACTOS
Se generan en `charts/` con `dpi=150` y se insertan con `M.figura("charts/<nombre>.png", pie="…")`.

| Fichero | Contenido | Usado en |
|---|---|---|
| `c01_mapa_dinero.png` | De dónde salen los 5.472,3 M: tres barras apiladas (marca / canal / geografía) | §4 |
| `c02_zapatilla_margenes.png` | Cascada sobre una zapatilla de 150 USD: bruto → operativo → neto | §3 |
| `c03_roic_capital.png` | NOPAT contra capital invertido, FY2022-FY2026, con el ROIC en línea | §5 |
| `c04_cruce_lineas.png` | Nueve trimestres: crecimiento de ingresos contra crecimiento de EBIT, cruzando el cero | §6 |
| `c05_dos_marcas.png` | Márgenes operativos de segmento UGG contra HOKA, FY2024-26 | §7 |
| `c06_hoka_coste.png` | Lo que HOKA gasta por cada dólar nuevo: ingresos, marketing, alquiler, nóminas indexados a 100 | §7 |
| `c07_empuje_tiron.png` | Mayorista contra venta directa por marca, FY2026 | §8 |
| `c08_margen_incremental.png` | 41,6% → 36,1% → 17,2% contra el margen medio | §6 |
| `c09_promesas.png` | Guía inicial contra realizado: margen operativo FY2024 y FY2025 | §9 |
| `c10_cascada_oe.png` | **Cascada 1.182,0 → 947,1** con los seis pasos | §12 |
| `c11_matriz_valoracion.png` | Mapa de calor 3×4 de la matriz que gobierna, con el precio marcado | §16 |
| `c12_dcf_inverso.png` | Crecimiento implícito en el precio (−3,07%) contra lo que la empresa guía | §17 |
| `c13_tir_alternativas.png` | TIR por celda contra el Tesoro (4,70%) y contra la tasa exigida (9,70%) | §17 |
| `c14_escalera_precios.png` | Escalera: hoy 88,73 · N2 91,02 · N3 66,75 · pleno 48,54 sobre los 105 cierres semanales | §18 |
| `c15_colapso_2022.png` | Flujo de caja libre e ingresos FY2019-FY2026, con FY2022 marcado | §19 |
| `c16_dos_precedentes.png` | EBIT FY2015-FY2019 reportado contra limpio de deterioros | §19 |

Cada gráfico vive en **su propio fichero** `graficos_<n>.py` que se ejecuta una vez.

## API DEL MOTOR — lo único permitido
```python
import motor_qg as M
from reportlab.platypus import Spacer, PageBreak, KeepTogether, NextPageTemplate
from reportlab.lib.units import cm
```
| Llamada | Qué hace |
|---|---|
| `M.flag_titulo(titulo, subtitulo)` | Cabecera de sección: flag rojo + título serif + bajada itálica. **Devuelve LISTA** |
| `M.portadilla(nivel, titulo, bajada)` | Divisor de PARTE con número grande. **Devuelve LISTA** |
| `M.p(txt, "cuerpo")` | Párrafo. Estilos: `cuerpo`, `h2`, `h3`, `nota` |
| `M.tabla(data, col_w, header=True, font_sz=8.6)` | Tabla; primera fila = cabecera azul-noche |
| `M.callout(tipo, texto)` | Caja. Tipos exactos: `"PAUSA REFLEXIVA"` (rojo), `"LECCIÓN TRANSFERIBLE"` (verde), `"CASO HISTÓRICO"` (azul) |
| `M.dato_grande(valor, etiqueta, nota)` | Cifra protagonista en caja crema con filo rojo |
| `M.caja_formula(titulo, formula, explicacion)` | Caja azul-noche para fórmulas del motor |
| `M.figura(path, pie="…")` | Gráfico + pie, mantenidos juntos, con aire |
| `M.kpi_panel([(v,l,s),(v,l,s),(v,l,s)])` | Tres cajas de KPI. **Exactamente tres** |
| `M.hr()`, `M.respiro(0.6)`, `M.semaforo("verde"/"ambar"/"rojo")` | Filete, espacio, glifo de semáforo |

## REGLAS DURAS DE MAQUETACIÓN
1. **Ancho útil = 17 cm.** La suma de `col_w` de cualquier tabla debe ser **≤ 17 cm**. Las tablas de más
   de 5 columnas usan `font_sz=7.6`.
2. **Escapado XML de ReportLab:** `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`. Marcado permitido:
   `<b>`, `<i>`, `<font size="" color="#RRGGBB">`, `<br/>`, `&nbsp;`, `&minus;`, `&middot;`, `&#9679;`.
   **Nunca uses `<br>` sin barra.** Nunca metas markdown (`**`, `|`, `#`) en una cadena.
3. **Ritmo:** después de cada gráfico, `M.respiro()`. Antes de cada `§`, la sección empieza con
   `M.flag_titulo(...)`. Cada módulo termina con `PageBreak()`. Las portadillas de parte van
   **precedidas** de `PageBreak()`.
4. **Un `M.dato_grande` por sección como máximo.** Es el énfasis; si se repite, deja de serlo.
5. **Callouts:** máximo dos por sección. `LECCIÓN TRANSFERIBLE` es para lo que sirve más allá de
   Deckers; `PAUSA REFLEXIVA` para poner al lector frente a su propio sesgo; `CASO HISTÓRICO` para
   precedentes de otras empresas.
6. **Tono:** español de España, segunda persona cuando enseña ("imagina que vendes"), primera cuando
   juzga ("lo digo sin rodeos"). Frases cortas. **Veredicto antes que razonamiento** en cada sección
   que tenga veredicto. Cero adjetivos vacíos, cero "es importante destacar".
7. **Etiquetas de fiabilidad:** todo dato que sostenga un juicio lleva `[HECHO]`, `[INFERENCIA]` o
   `[SUPUESTO]` al menos una vez por sección, integrado en el texto o en el pie de tabla.
8. **Cifras:** coma decimal, punto de millar, exactamente como en `DATOS.md`. Nunca redondees distinto.

## REGLAS DE LOS GRÁFICOS
```python
from chart_style import deco, save
from paleta_qg import PALETA as P
```
- Siempre `deco(ax, titulo, subtitulo, fuente)` y `save(fig, "cNN_nombre")`.
- **Nunca dos `$` en un título o subtítulo** (matplotlib lo interpreta como mathtext y lo destroza).
- Fondo crema heredado de `chart_style`; **nunca** `facecolor="white"`.
- Colores semánticos: pesimista/alerta `P["rojo_oscuro"]`, serie principal `P["azul"]`, positivo
  `P["verde"]`, umbral/línea clave `P["rojo"]` (discontinua), "HOY" `P["tinta"]` (sólida), neutral
  `P["ocre"]`.
- `figsize` entre `(10.0, 5.4)` y `(10.8, 6.6)`. Etiquetas de datos legibles a 8-9 pt.
- **El gráfico debe contar la conclusión solo.** Título afirmativo, no descriptivo: "Dos trimestres
  seguidos de beneficio cayendo con las ventas subiendo", no "Evolución trimestral".
- Acentos y "ñ" **sí** se pueden usar (DejaVu Serif los cubre).

## VERIFICACIÓN OBLIGATORIA ANTES DE ENTREGAR
Cada agente ejecuta su propio fichero y comprueba que corre sin excepción:
```bash
cd "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build"
python3 graficos_N.py          # gráficos
python3 -c "import contenido_N; [f() for f in (contenido_N.seccion_X,)]"   # contenido
```
Si algo falla, se arregla antes de reportar. **No se entrega código que no se ha ejecutado.**
