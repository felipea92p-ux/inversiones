# ESTÁNDAR MAESTRO · TESIS ULTRA QUALITY GROWTH
## Especificación de diseño + memoria operativa para reconstrucción
### Versión 2.0 · Estilo editorial tipo The Economist

---

## CÓMO USAR ESTE ARCHIVO

Este documento es la **fuente única de verdad** para construir cualquier tesis del
portafolio Quality Growth. Sirve dos propósitos a la vez: es legible para una persona
que quiera entender el estándar, y es lo bastante preciso para que cualquier sesión de
Claude reconstruya una tesis idéntica sin re-explicar nada.

**Regla de oro antes de entregar cualquier tesis:** muestrear el color de fondo y los
acentos contra una tesis de referencia ya aprobada (ej. ABNB), y confirmar pixel-exacto
que coinciden ANTES de dar el documento por terminado. Definir un color en una variable
NO basta — el fondo de página debe pintarse activamente con un rectángulo en cada página.

---

## 1 · PALETA OFICIAL (congelada)

Extraída pixel-exacta del fondo y los gráficos de Tesis_Ultra_ABNB_v1.
Todos los colores tienen **sesgo cálido** deliberado: grises con tinte marrón, fondo
crema en vez de blanco, "negro" que en realidad es #2A2A2A. Cualquier color nuevo debe
respetar ese sesgo cálido o desentonará con el conjunto.

### Hex definitivos

| Rol | Hex | Uso |
|---|---|---|
| **fondo** | `#FAF5E9` | Fondo de página Y de gráficos (pintar rectángulo en cada página) |
| **panel** | `#F2ECDC` | Paneles, cajas de KPI, filas alternas de tabla |
| **rojo** | `#C60C2A` | Carmín firma — acento principal, flag rojo, líneas clave del DCF |
| **rojo_oscuro** | `#8C1410` | Alertas, escenario pesimista, barras negativas |
| **azul** | `#2A5A7E` | Petróleo — serie de datos PRINCIPAL (caballo de batalla) |
| **azul_noche** | `#1F3A52` | Cabeceras de tabla, titulares oscuros |
| **azul_acero** | `#547890` | Segunda serie de datos |
| **azul_cielo** | `#8AAEC4` | Tercera serie / barras apiladas |
| **azul_pro** | `#16527A` | NUEVO — cuarto azul más profundo, para 4-5 series juntas |
| **verde** | `#6C7E48` | Oliva — positivo / cuarta serie |
| **terracota** | `#C07E66` | Acento cálido secundario |
| **vino** | `#6E1423` | NUEVO — burdeos profundo, acento sobrio que no grita como el carmín |
| **ocre** | `#B8860B` | Zona neutral / "mantener" |
| **tinta** | `#2A2A2A` | Texto principal (casi-negro cálido) |
| **gris** | `#666054` | Topo — texto secundario, notas al pie |
| **gris_medio** | `#847E72` | Etiquetas suaves |
| **gris_linea** | `#D2CCC0` | Cuadrícula de gráficos, divisores |
| **gris_claro** | `#EAE4D8` | Rellenos sutiles |

### Bloque Python (copiar a paleta_qg.py)

```python
PALETA = {
    "fondo": "#FAF5E9", "panel": "#F2ECDC",
    "rojo": "#C60C2A", "rojo_oscuro": "#8C1410",
    "azul": "#2A5A7E", "azul_noche": "#1F3A52",
    "azul_acero": "#547890", "azul_cielo": "#8AAEC4", "azul_pro": "#16527A",
    "verde": "#6C7E48", "terracota": "#C07E66", "vino": "#6E1423", "ocre": "#B8860B",
    "tinta": "#2A2A2A", "gris": "#666054", "gris_medio": "#847E72",
    "gris_linea": "#D2CCC0", "gris_claro": "#EAE4D8",
}
```

### Reglas de uso (CRÍTICAS para legibilidad)

**Jerarquía de color:** UN solo rojo protagonista (carmín) para lo que debe captar la
atención; UN azul de reparto principal (petróleo) como caballo de batalla de datos; el
resto (acero, cielo, azul_pro, oliva, terracota, vino, ocre) son series secundarias;
los grises cálidos cargan todo el texto secundario en silencio.

**Regla de contraste (medida con WCAG contra el fondo crema):**
- Sirven como TEXTO (≥4.5:1): tinta, azul, azul_noche, rojo, rojo_oscuro, vino, gris.
- SOLO para rellenos y formas, NUNCA texto (contraste insuficiente):
  `ocre`, `azul_cielo`, `terracota`, `verde`, `gris_medio`. En una barra están bien
  porque la etiqueta del número va en negro encima o al lado; como texto se leen mal.

### Orden recomendado de series en gráficos (de mayor a menor protagonismo)
`azul → azul_acero → azul_pro → azul_cielo → verde → terracota → ocre`

---

## 2 · ESTÉTICA EDITORIAL (estilo The Economist)

**Firma visual:** el rectángulo rojo (#C60C2A) arriba a la izquierda — el "flag" — sobre
cada gráfico y cada cabecera de sección, seguido de titular en sans negrita y subtítulo
fino en gris. Es el gesto que hace reconocible el estilo a un metro de distancia.

**Tipografía:**
- Titulares: sans negrita (Helvetica-Bold). Pegados a la izquierda, nunca centrados.
- Cuerpo: serif legible (Times-Roman), justificado, interlineado generoso (~15.8pt).
- Subtítulos de sección: serif itálica en gris.
- La combinación titular-sans + cuerpo-serif evoca la jerarquía Economist sin falsificar
  su tipografía propietaria (Officina/Milo), que no está disponible.

**Maquetación:**
- Página A4, márgenes 2.0 cm.
- Fondo crema #FAF5E9 pintado en TODA la página (portada y contenido).
- Cabecera: mini-flag rojo + "TESIS ULTRA · QUALITY GROWTH" a la izquierda + nombre de
  empresa a la derecha + línea fina gris debajo.
- Pie: línea roja corta + "Tesis ultra para uso personal..." + "Página X de N".
- Portada: banda roja superior + pie negro + nombre empresa en sans negrita grande +
  tagline en serif itálica + panel de 3 KPIs en crema + fila de meta (fecha/precio/horizonte).

**Cajas de callout (recurrentes en el cuerpo):**
- "PAUSA REFLEXIVA" — pregunta que obliga a pensar antes de seguir.
- "LECCIÓN TRANSFERIBLE" — principio que aplica más allá de esta empresa.
- Formato: fondo panel crema + barra roja vertical a la izquierda + título rojo en
  Helvetica-Bold + cuerpo en serif itálica.

---

## 3 · LOS 20 GRÁFICOS (orden y función fijos)

Todos comparten: fondo crema #FAF5E9, flag rojo + título sans-bold + subtítulo gris,
cuadrícula SOLO horizontal y finísima (#D2CCC0), etiquetas de datos directamente sobre
las barras/puntos, línea de fuente en itálica gris al pie, sin marco (spines off salvo
el eje X). Generados con matplotlib, embebidos como PNG a 150 dpi.

| # | Nombre | Tipo | Qué muestra | Colores |
|---|---|---|---|---|
| 01 | radar | Radar polar | Las 10 reglas de Seilern, 0-10, con anillo de umbral en 8 | navy relleno, rojo umbral, puntos rojo/ocre/navy según score |
| 02 | segments | Barras apiladas | Ingresos por segmento operativo, 3 años | navy / acero / cielo |
| 03 | azure | Línea + área | Crecimiento YoY del producto estrella, con umbral de venta | navy línea, rojo umbral |
| 04 | cloudshare | Barras horizontales | Cuota de mercado vs competidores + crecimiento sobre barras | gris/navy/vino/gris según jugador |
| 05 | capex | Barras apiladas + línea | CapEx vs depreciación (la tensión de la R7) | navy/cielo barras, rojo línea depreciación |
| 06 | fcf | Doble panel | Izq: flujo anual. Der: margen FCF trimestral comprimiéndose | acero/navy + rojo línea |
| 07 | margins | Triple línea | Márgenes bruto/operativo/neto a 5 años, etiquetas al final de línea | gris/navy/acero |
| 08 | dcf | Barras + 2 líneas | 3 escenarios DCF + precio actual + valor ponderado | rojo_oscuro/navy/verde, líneas tinta y rojo |
| 09 | pricezones | Barra horizontal por zonas | Mapa operativo: Ganga/Oportunidad/Justo/Caro/Burbuja + marcador "HOY" | verde→acero→ocre→terracota→rojo_oscuro |
| 10 | multiples | Barras | Múltiplos actuales vs media histórica | navy, gris para el histórico |
| 11 | balance | Barras | Caja vs deuda vs leases vs posición neta | navy/terracota/ocre/verde |
| 12 | airunrate | Barras | Trayectoria de monetización del run-rate de IA (o métrica análoga) | navy + rojo % crecimiento |
| 13 | investors | Barras horizontales | Panel de 9 inversores con convicción y veredicto | navy=BUY, ocre=HOLD, rojo_oscuro=PASS |
| 14 | projection | Triple línea | Proyección a 5 años de inversión hipotética, 3 escenarios | verde/navy/rojo_oscuro |
| 15 | rpo | Barras | Backlog contratado (o métrica de demanda futura) | verde + rojo % crecimiento |
| 16 | returns | Barras apiladas | Retorno al accionista: dividendos + recompras | navy/cielo |
| 17 | wacc | Barras de construcción | Cómo se arma el WACC paso a paso | navy/cielo/acero/ocre/rojo |
| 18 | copilot | Barra de penetración | Adopción del producto clave sobre la base instalada (runway) | navy sobre gris_claro |
| 19 | sensitivity | Heatmap | Valor intrínseco según WACC × crecimiento terminal | colormap rojo_oscuro→gris→navy |
| 20 | eps | Barras | Beneficio por acción diluido a 5 años (compounding) | navy |

**Nota de adaptación:** no todas las empresas usan los 20 idénticos. El esqueleto es
fijo, pero un banco no tiene "capex" como una semiconductora. Adaptar el CONTENIDO de
cada gráfico a la empresa, manteniendo el TIPO y el ESTILO. Los gráficos 01, 08, 09, 10,
13, 14, 19 son universales (aplican a cualquier empresa); el resto se adapta al modelo de
negocio (ej. para un banco, sustituir "azure growth" por "crecimiento de préstamos o
depósitos"; "capex" por "ratio de eficiencia"; etc.).

---

## 4 · LAS 11 SECCIONES (estructura fija)

Estructura espejo de la tesis de referencia. Cada sección abre con flag rojo + título +
subtítulo. El documento completo ronda las 35 páginas.

**Apertura (antes de §1):**
- **Portada** — nombre, ticker, sector, tagline, 3 KPIs, fecha/precio/horizonte.
- **Resumen en treinta segundos** — 3 "big numbers" + veredicto en una línea + los tres
  puntos críticos a recordar + una PAUSA REFLEXIVA.
- **El veredicto cuantificado** — radar de las 10 reglas + tabla regla por regla con
  score/peso/veredicto + LECCIÓN TRANSFERIBLE sobre el score como filtro, no veredicto.

**Las secciones numeradas:**

- **§1 · La historia detrás del veredicto** — narrativa de origen de la empresa; el ADN
  del negocio contado como historia, no como ficha. Termina conectando con el moat.
- **§2 · Historia de mi posición** — la situación REAL del usuario en esa acción (posición
  actual, coste, o "testimonial/inmaterial"). Ancla la tesis en su portafolio concreto.
- **§3 · El modelo de negocio en dos minutos** — la prueba de Lynch: explicar el negocio
  simple. Segmentos, mecánica, cómo gana dinero. Incluye gráfico de segmentos y márgenes.
- **§4 · Las diez reglas de Seilern aplicadas con bisturí** — cada regla desarrollada,
  agrupada en bloques temáticos. NO perdonar la regla que falla; puntuar honesto.
- **§5 · El moat** — las capas de ventaja competitiva, de la más superficial a la más
  profunda. Cuántos años de defensa tiene cada capa. PAUSA REFLEXIVA sobre erosión.
- **§6 · El campo de batalla competitivo** — análisis de la guerra del sector con máxima
  profundidad. El frente que decide la década. Varios gráficos competitivos.
- **§7 · TAM, runway y catalizadores** — mercado direccionable (tabla descompuesta +
  narrativa), penetración actual, y los catalizadores concretos de los próximos años.
- **§8 · Valoración** — estilo Damodaran: los 5 supuestos del DCF descompuestos y
  justificados + desglose completo del WACC + 3 escenarios probabilísticos + sensibilidad
  + múltiplos vs historia + PEG (prueba de Lynch) + mapa de zonas de precio.
- **§9 · Gestión, cultura y gobernanza** — track record del CEO, asignación de capital,
  los deméritos de gobernanza sin maquillar. Gráfico de retorno al accionista.
- **§10 · Nueve inversores legendarios opinan** — Graham, Buffett, Munger, Fisher, Lynch,
  Templeton, Marks, Seilern, T. Smith. Cada uno con su veredicto y convicción. La
  divergencia es la señal valiosa, no el consenso.
- **§11 · Veredicto final, triggers y proyección** — veredicto operativo (BUY/HOLD/SELL),
  estrategia de entrada en tramos, triggers de venta falsables con indicador cuantitativo,
  PRE-MORTEM (la historia del fracaso a 5 años), proyección de la posición, y conexión con
  el sistema integrado del usuario (su empresa + inversiones + vida).

**Cierre (después de §11):**
- **Glosario** — términos técnicos en orden alfabético, definición de una línea.
- **Advertencias finales** — etiquetado HECHO/INFERENCIA/SUPUESTO; ambigüedad del score
  Seilern (aritmética estricta vs ponderada); datos no verificados; naturaleza del
  documento (uso personal, no asesoría registrada).

---

## 5 · METODOLOGÍA DE CONTENIDO (recordatorios clave)

- **Etiquetar todo:** HECHO (fuente primaria) / INFERENCIA (derivado) / SUPUESTO (asunción
  justificada). Jerarquía de fuentes: 10-K > transcripts > datos > prensa.
- **Score Seilern ponderado:** R1, R3, R4 pesan 1.5×; el resto 1.0×; denominador máximo
  13.5. Umbral de núcleo: 80% (10.8/13.5). NO aplicar mecánicamente — explicar la
  ambigüedad entre aritmética estricta y lectura ponderada por calidad.
- **No perdonar fallos:** si una empresa falla una regla (ej. intensidad de capital), se
  puntúa como fallo. El veredicto puede seguir siendo compra si el moat compensa, pero eso
  es un juicio explícito, no un maquillaje del número.
- **SBC >15% del FCF = penalización** en la regla de contabilidad.
- **Caída >20% = re-análisis** de la tesis completa.
- **Valoración:** DCF ×2 (primario, 3 escenarios), P/E ×1, EV/EBITDA ×1, P/FCF ×1,
  PEG ×1 (<1.5 atractivo, 1.5-2.5 aceptable, 2.5-4.0 requiere moat monstruoso), Price/Sales
  ×1.5 solo para empresas sin FCF positivo en expansión. SOTP para conglomerados.
- **Tono:** socio intelectual, no validador. Confrontar sesgos sin que lo pidan. Conectar
  los puntos entre la empresa, el portafolio y el sistema del usuario. Verdad aunque duela.

---

## 6 · ARQUITECTURA TÉCNICA (para reconstrucción)

El documento se construye con **separación estricta contenido/diseño**:
- **Motor de diseño** (1 archivo): paleta, estilos tipográficos, helpers (flag rojo,
  callouts, tablas, función chart()), cabecera/pie, portada, y la función de pintar el
  fondo crema en cada página.
- **Generador de gráficos** (1 archivo): los 20 gráficos en matplotlib, misma paleta.
- **Archivos de contenido** (varios): SOLO la prosa, tablas y datos. Importan del motor.
  Cambiar el diseño NO debe tocar estos archivos. Cambiar el contenido NO debe tocar el
  motor. El único punto de conexión es la línea de import.

Ventaja: para una empresa nueva, se reutiliza el motor y el generador intactos; solo se
escriben los archivos de contenido con los datos y la narrativa de esa empresa.

Herramientas: matplotlib (gráficos), ReportLab (PDF). Salida a /mnt/user-data/outputs/.

---

## 7 · CHECKLIST DE ENTREGA (no saltarse)

1. Fondo crema #FAF5E9 pintado en TODAS las páginas (muestrear y confirmar pixel).
2. Acentos (rojo, azul) coinciden con tesis de referencia (muestrear y confirmar).
3. Los gráficos relevantes para el modelo de negocio están presentes y bien embebidos.
4. Las 11 secciones + apertura + cierre, en orden.
5. Score Seilern con la ambigüedad explicada, fallos no perdonados.
6. Veredicto con tamaño de posición, rango de entrada, triggers falsables.
7. Pre-mortem y panel de 9 inversores incluidos.
8. Etiquetado HECHO/INFERENCIA/SUPUESTO aplicado.
9. Datos no verificados marcados explícitamente como tales.
10. Render visual revisado (no solo que compile — que se VEA bien).
