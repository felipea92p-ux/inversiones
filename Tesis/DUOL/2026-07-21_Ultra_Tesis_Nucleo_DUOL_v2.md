# DUOL — El precio del candado: qué pasa cuando se audita la propia auditoría

### Ultra Tesis Núcleo v2 · método metodologia-qg (12 pasos) · 2026-07-21

---

> **Relación con documentos previos.** Este documento reemplaza como insumo de mayor calidad al
> ejercicio de ayer (`2026-07-20_Ultra_Tesis_Nucleo_DUOL.md`) y audita explícitamente a la Tesis
> Ultra v4.1 (`2026-07-09_Tesis_Ultra_DUOL_v4.pdf`, sistema viejo qg-seilern+val-mos, retirado
> 2026-07-19). No es un ritual repetido sin señal nueva: hay tres hechos nuevos desde ayer —
> (1) el precio vivo cayó 5,4% a 124,93 USD, (2) se auditó por primera vez el archivo fuente de la
> v4 y se encontró que su WACC nunca fue de mercado, y (3) un segundo `abogado-diablo`, en sesión
> limpia independiente de la de ayer, atacó el caso con el hallazgo del WACC ya incorporado y llegó
> a un veredicto más severo. Autoridad formal sobre las 150 acciones reales sigue siendo la v4 hasta
> que Felipe reconcilie las dos fuentes — ver §8.

---

## 0. Monólogo borrador (qué se creía antes de tocar ningún dato nuevo hoy)

DUOL es la posición número 2 de la cartera por tamaño. Ayer el ejercicio núcleo, con su propio veto
de abogado-diablo, concluyó recortar de 150 a 75 acciones (7,3% NAV), con un falsable al "12 de
agosto". La duda que quedaba abierta, sin resolver, era cuál documento gobierna la orden real —
la v4 vigente (VIGILAR) o el ejercicio núcleo en cuarentena. Hoy la pregunta no es si repetir el
ejercicio de ayer, es si algo cambió que lo invalide o lo refuerce.

## 1. Lo que cambió desde ayer — tres hechos, no opiniones

**Precio.** DUOL cayó de 132,01 a **124,93 USD** en un día (−5,4%), con volumen 89% por debajo del
promedio — sin noticia negativa identificable. Al contrario: Jefferies, Morgan Stanley y JPMorgan
subieron su precio objetivo a 125 USD entre el 14 y el 17 de julio, con calificación "hold". Lectura:
ruido de mercado sobre una acción ya deprimida, no una señal fundamental nueva.

**Fecha del gate — corrección de HECHO.** Tanto `gates.md` como el documento de ayer citan el
falsable como "12 de agosto". Verificado contra fuente primaria (comunicado de la propia Duolingo,
GlobeNewswire, 8-jul-2026, y confirmado independientemente vía búsqueda cruzada): Duolingo reporta
resultados del Q2 FY2026 el **miércoles 5 de agosto de 2026**, no el 12. Es una semana de diferencia
sobre una posición del 14% del NAV — importa. *(Nota adicional: el segundo abogado-diablo de hoy,
en sesión limpia con cero acceso a archivos, mencionó "~12-ago" y afirmó que era "consistente con el
gate ya registrado en gates.md" — una afirmación que no podía verificar porque no leyó ningún
archivo. Es un recordatorio de que hasta un agente en sesión limpia puede sonar seguro citando algo
que nunca vio. La fecha correcta, verificada dos veces contra fuente primaria, es 5-ago.)*

**Auditoría de la v4 — el hallazgo grande.** Por primera vez se auditó el archivo fuente de la Tesis
Ultra v4 (`dcf_duol.py`) contra EDGAR y contra sí mismo. Dos resultados, ambos verificados:

## 2. Auditoría de la v4: qué acertó, qué falló

**Lo que acertó, con evidencia:**
- La serie financiera cruda (ingresos, margen operativo, SBC 2021-2025) coincide **exacta al
  decimal** contra los datos estructurados de EDGAR (XBRL, CIK 0001562088). Cinco años, tres
  métricas, cero desviación.
- La metodología de owner earnings (FCF − SBC) es correcta: SBC es dilución real, no se puede tratar
  como gasto no-cash gratis.
- Aislar caja neta del enterprise value (EV = mkt cap − caja neta) es la práctica correcta.
- Citó fuente primaria explícita (10-K FY2025 + 10-Q Q1'26 + DEF 14A, SEC EDGAR CIK 0001562088) —
  buena disciplina de citación, aunque como se ve abajo, citar la fuente no garantiza haber
  reconciliado cada cifra contra ella.

**Lo que falló, con magnitud cuantificada:**
- **El WACC nunca fue de mercado.** El propio archivo calcula su CAPM (RF=4,49% verificado contra
  la curva del Tesoro de EE.UU. misma fecha; beta ajustado a mano a 1,2, sin metodología citada;
  ERP=5,0%) → COE≈10,5%. Y luego, en la línea siguiente, usa WACC=8,5% con un comentario explícito
  en el propio código: *"anclado al escalón de tier (Alta ~8,5%)"*. No es un error de cálculo — es
  una elección documentada de sustituir la tasa de mercado por la tasa barata que el tier de calidad
  autorizaba. Es el caso de manual exacto que motivó el candado B de la refundación.
- **Cuantificado:** recalculando con WACC=10,5% sobre la misma proyección de flujos (extrapolación
  fuera de la grilla de sensibilidad original, tres métodos de ajuste convergen en una banda, no un
  punto), el valor por acción cae de ~160 a **~119-125 USD**. El "margen de seguridad" del 21% que
  reportaba la v4 se explica casi por completo por la tasa de descuento equivocada, no por el
  negocio.
- **Inconsistencia interna sin resolver, admitida por escrito.** El archivo "fuente única de verdad"
  (`dcf_duol.py`) no coincide con el PDF que Felipe realmente lee: score 78,2 vs 80,8 en el
  documento, PWFV 160/163,75 vs 153, caja neta 1,39B vs 1,16B, probabilidades de escenario distintas.
  El propio `changelog.md` de la v4.1 **documenta la divergencia y decide no resolverla**
  ("este refresco editorial no tenía mandato para resolver esta divergencia"). Es un defecto de
  proceso, no de Duolingo como negocio — pero es serio: la autoridad formal sobre 150 acciones reales
  se apoyaba en un documento que ni siquiera está de acuerdo consigo mismo.
- Una tabla de múltiplos en la v4 está etiquetada "HECHO" citando como fuente "multiples.vc" — eso es
  prensa/web suelta, no HECHO según la propia disciplina de datos de Felipe. Mal etiquetado.

## 3. Los seis puertas (heredado sin cambios de ayer — ningún hecho nuevo las mueve)

DUOL sigue abriendo solo G5 (la caja no miente) de seis. G1 (retorno tardío) y G6 (mecanismo bajo
amenaza) tienen evidencia sustantiva real en contra; G2/G3/G4 son vacíos de información, no pruebas
de fallo — la distinción que el abogado-diablo de ayer ya defendió con el error de categoría. No se
repite el detalle aquí porque nada cambió: ver `2026-07-20_Ultra_Tesis_Nucleo_DUOL.md` §4-5 para el
desarrollo completo puerta por puerta.

## 4. Scuttlebutt de hoy — confirmado, no heredado a ciegas

- Google Translate: la función de racha diaria (lanzada ago-2025) se **expandió a 20 países
  adicionales** para julio 2026, con widget de pantalla de inicio dedicado. La amenaza sigue viva y
  creciendo, no se desinfló.
- Guía oficial Q2 FY2026 (carta a accionistas, SEC, may-2026): bookings +5,8% reportado / **+4,1% en
  moneda constante** — verificado independientemente contra fuente primaria, no heredado sin
  chequeo. Coincide con lo que citaba el documento de ayer.
- DAU Q1 FY2026: +21% interanual a 56,5M, suscriptores de pago +21% a 12,5M — verificado, coincide
  con el 21,2% que citaba ayer.
- MAU (desaceleración +32%→+14%→+5,8%): **no re-verificado hoy contra fuente primaria** — se hereda
  como INFERENCIA del análisis de ayer, no como HECHO confirmado en esta pasada. Es, según el
  abogado-diablo de hoy, precisamente el dato que probaría o mataría la erosión del moat, y hoy sigue
  sin estar confirmado en fuente primaria de esta sesión.

## 5. Valoración — tres métodos de mercado, tres respuestas parecidas

| Método | WACC | Resultado |
|---|---|---|
| CAPM propio de la v4, con la tasa que **descartó** | 10,5% (beta ajustado a mano) | ~119-125 USD |
| Bottom-up sin ajustar beta (ejercicio de ayer) | 8,46% | banda 90-145 USD |
| Consenso 24 analistas Wall Street | — | 82-145 USD, mediana 113,50 |

El precio de hoy, 124,93 USD, cae **en el techo o encima** del rango que produce el método más
conservador (CAPM con beta ajustado) y en el tercio medio-alto del rango más generoso. Ningún método
que respete el candado B (WACC de mercado, sin ajuste de tier) pone el valor justo claramente por
encima de 145. La única vía a un valor mayor pasa por descartar el ajuste de beta por riesgo de IA —
que es, en sí, un juicio cualitativo legítimo (dominio del moat, no de la tasa de descuento) que no
debería colarse en el WACC, sino tratarse aparte como lo que es: una pregunta sobre si el mecanismo
resiste, no sobre cuánto vale el dinero en el tiempo.

**Pregunta sin resolver, honesta:** ¿el beta 0,88-0,89 histórico subestima el riesgo real de
disrupción por IA que el precio pasado, por definición, no pudo haber capturado si la amenaza es
reciente? No hay una respuesta limpia — es zona de juicio, no de HECHO, y merece tratarse como tal en
vez de resolverse ad-hoc dentro del WACC (que es exactamente el error que cometió la v4, solo que en
sentido contrario: allá se abarató la tasa por el tier de calidad, aquí la tentación sería encarecerla
por el miedo a la IA — ambas son la misma contaminación, con signo distinto).

## 6. El segundo abogado-diablo — más severo que el de ayer

Sesión limpia, independiente de la de ayer, con el hallazgo del WACC ya incorporado a los hechos que
recibió. Atacó tres pilares — moat, motor de crecimiento, precio — y concluyó que **ninguno sobrevive
intacto**:

1. **Moat:** el propio dato admite que es "conductual, no medible en dinero" — la confesión de que no
   hay barrera de imitación. Google Translate ya la imitó, con más distribución que nadie. El dato que
   probaría si la racha sobrevive (MAU) no está verificado hoy. Carga de la prueba incumplida, no
   satisfecha.
2. **Motor de crecimiento:** cinco años de mejora monótona del margen operativo sin un solo retroceso
   es el perfil de apalancamiento operativo agotándose, no de reinversión compuesta genuina — y el
   techo de ese apalancamiento llega justo cuando la guía se desploma a +4,1% cc.
3. **Precio:** con el candado bien aplicado, no existe ningún método limpio que ponga el valor justo
   claramente por encima de 124,93. El precio de hoy es el techo del rango honesto, no un descuento.
   Sesgo identificado, documentado por escrito, no especulado: la v4 calculó su CAPM correcto y lo
   sustituyó por uno más barato — el ejemplo más limpio posible de confirmation bias porque quedó en
   el registro.

**Su veredicto independiente:** el recorte a la mitad (75 acciones, ~7,3% NAV) que ya estaba
registrado es "el piso, no el objetivo" — recomienda bajar más, a un rango de **5-7% del NAV**, no
salida completa (no hay señal de sobreprecio extremo que la justifique), pero tampoco mantener el
tamaño actual sin margen de seguridad y con el moat activamente atacado.

## 7. Test del hoy y veredicto

¿Compraría Felipe 150 acciones de DUOL hoy, a 124,93 USD, con esta tesis exacta? Con el hallazgo del
WACC ya sobre la mesa, la respuesta es un no más rotundo que ayer, no menos. La carga de la prueba
sigue invertida: mantener el 100% es lo que necesita justificarse, y hoy tiene menos con qué
justificarse que ayer.

**Veredicto: recortar más allá de la mitad.** Dos ejercicios adversariales independientes, en
sesiones limpias distintas, con datos parcialmente distintos (el de hoy incorpora el error de WACC
cuantificado), convergen en la misma dirección con distinta intensidad: ayer "recortar a la mitad,
7,3% NAV"; hoy "eso es el piso, bajar a 5-7% NAV". Ninguno de los dos, en ningún momento, pidió
ampliar. La sustancia que sostiene no ir a cero sigue intacta: DAU y suscriptores de pago creciendo
21% interanual pese a la presión competitiva, ningún múltiplo de mercado en zona de alarma, sin
evidencia de trampa de valor (el negocio no se está cayendo, se está desacelerando desde muy alto).

**Acción recomendada:** vender entre 75 y 100 de las 150 acciones, dejando la posición en un rango de
50-75 acciones (≈5,9%-8,9% del NAV a precio de hoy). El punto exacto dentro de ese rango es una
decisión de Felipe sobre cuánta piel quiere mantener en el juego de cara al 5 de agosto, no algo que
el método pueda resolver con más precisión sin violar el candado C (piso de resolución).

## 8. Lo que sigue sin resolverse — y hay que resolverlo antes de ejecutar nada

**Pendiente de ayer, todavía abierto:** ¿cuál fuente gobierna la orden real sobre las 150 acciones —
la Tesis Ultra v4 (autoridad formal hoy, pero con el WACC ahora demostrado como no-de-mercado y una
inconsistencia interna admitida y no resuelta) o el ejercicio núcleo (en cuarentena metodológica hasta
19-ago, pero con dos vetos adversariales independientes convergentes y el único que aplicó el candado
B correctamente)? Este documento no decide eso por Felipe — lo señala con más urgencia que ayer,
porque la v4 acaba de perder buena parte de su autoridad al auditarse.

## 9. Diario — predicción falsable, registrada hoy

**Falsable, fecha exacta: 5 de agosto de 2026** (Q2 FY2026, corregido de "12-ago"). Condiciones que
matarían la tesis de crecimiento compuesto y obligarían a vender el resto, no solo recortar:
- Bookings en moneda constante por debajo de +4,1% (la propia guía ya rebajada, incumplida)
- MAU o DAU interanual verificado en fuente primaria por debajo de +15% (frente al +21% actual)

Si el 5 de agosto ambas condiciones se superan (bookings ≥4,1% cc, DAU/MAU sostenidos ≥15%), el caso
para no recortar más, o incluso reconsiderar el tamaño, se reabre con datos frescos — no antes.

---

## Ficha técnica

| Concepto | Valor |
|---|---|
| Posición real (IBKR, vivo, 2026-07-21) | 150 acciones DUOL |
| Precio en vivo | 124,93 USD (−5,4% vs ayer) |
| Coste promedio | 132,15 USD |
| Valor de mercado | 18.739,50 USD |
| Peso actual en NAV | 14,01% (NAV total 133.794,36 USD) |
| Caja disponible hoy | 5.184,61 USD (3,87% NAV) |
| WACC de mercado, CAPM propio de v4 (descartado por v4) | 10,5% → valor ~119-125 USD |
| WACC de mercado, bottom-up sin ajuste (ayer) | 8,46% → banda 90-145 USD |
| Consenso 24 analistas | 82-145 USD, mediana 113,50 |
| Veredicto abogado-diablo #1 (2026-07-20) | Recortar a 75 acc. (~7,3% NAV) |
| Veredicto abogado-diablo #2 (2026-07-21, con hallazgo WACC) | Recortar a 5-7% NAV (piso más bajo) |
| Acción recomendada este documento | Vender 75-100 de 150 acciones |
| Posición resultante sugerida | 50-75 acciones (~5,9%-8,9% NAV) |
| Falsable — fecha corregida | **5 de agosto de 2026** (no 12-ago) |
| Falsable — condiciones | Bookings cc <4,1% guiado, o DAU/MAU YoY <15% |
| Autoridad formal vigente sobre capital real (pendiente de reconciliar) | Tesis Ultra v4 — auditada hoy, WACC no-de-mercado confirmado |

---

*Documento de síntesis narrativa, ejercicio metodologia-qg sobre DUOL, 2026-07-21. Audita y
reemplaza como insumo al ejercicio de 2026-07-20. No sustituye formalmente a la Tesis Ultra v4 como
autoridad de decisión sobre capital real hasta que Felipe reconcilie §8.*
