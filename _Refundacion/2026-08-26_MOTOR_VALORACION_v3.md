# MOTOR DE VALORACIÓN v3 — Recalibración total del cálculo de valor intrínseco
Fecha: **2026-08-26**. Sustituye al motor que produjo `Rankings/Los36_Ultracalidad_ValorIntrinseco_2026-08-26.pdf`.
Decidido por Felipe en sesión de 28 preguntas cerradas. Formato exigido por el ADN: paso / candado / antes / después / motivo.

---

## 0 · Por qué se recalibra

El PDF del 26-ago declaró que 34 de 36 empresas de ultracalidad estaban caras, con primas de hasta
**+588%** (UNP) y **+262%** (GOOGL), mientras ponía a NVDA con **−24,5% de descuento**. Felipe lo rechazó
por irreal. La auditoría del CSV del motor (`Rankings/2026-08-26/Valor_Intrinseco_36_2026-08-26.csv`)
confirma que **no era un juicio pesimista: era un artefacto mecánico**. Cinco defectos que se multiplican.

### Defecto 1 — g∞ = 0% en 23 de 36 (EL MAYOR)
Con r=9,70% y g∞=0, el término de Gordon fija el múltiplo terminal en **1/0,097 = 10,3×** owner earnings.
Con g∞=2,32% sube a 13,4×. Visa, Hermès, ASML, TSM y Union Pacific llevaban g∞=0.
Ninguna empresa élite del mundo cotiza a 10× FCF; el motor decidía "cara" antes de mirar el negocio.
Peor: la regla de asignación no era económica sino de disponibilidad de datos
(*"0% cuando el ROIIC no es medible con la ventana de 4 años"*).

### Defecto 2 — r = 9,70% plana, aplicando el candado B AL REVÉS
CLAUDE.md, candado B: *"WACC siempre bottom-up de mercado, PROHIBIDO heredarlo de un tier de calidad"*.
El motor lo leyó como *"prohibido calcular WACC por empresa"* y usó bono 10a (4,70%) + prima fija
inventada (5,00%) para las 36. **La prohibición es contra derivar la tasa de la CALIDAD; el mandato es
derivarla del MERCADO, empresa por empresa.** El candado estaba invertido en el código.
Consecuencia colateral grave: hubo **knock-outs ejecutados con la tasa equivocada** (Waste Management
cayó por "ROIC 8,2% < 9,70%" cuando su WACC real ronda 6,5-7%).

### Defecto 3 — owner earnings = CFO − capex TOTAL − SBC
Castiga estructuralmente a quien construye activos y premia a quien los alquila. Nvidia es *fabless*:
su capex de fábrica está en el balance de TSMC. Por eso el mismo instrumento dice NVDA −24% y TSM +250%
— no son dos lecturas, es la misma fórmula vista desde los dos lados.
Evidencia GOOGL: owner earnings 2021-2025 = 51,3 / 40,5 / 47,4 / 50,0 / 46,2 mil M$ (**planos**),
mientras el NOPAT crecía al **19,9% anual** y los ingresos al 12,5%. Toda la diferencia es capex de
crecimiento tratado como coste puro. Amazon salía con owner earnings **negativos** (−11.800M).

### Defecto 4 — g0 anclado en un punto del ciclo
NVDA entró con **g0 = 83,4%**, "verificado al alza" sobre dos trimestres de pico de escasez.
UNP con 2,0%, OTIS 1,6%, AZO 3,3% — suelos. El motor extrapolaba picos y suelos como estado estacionario.
Nadie comprobó que la senda de NVDA implicaba ingresos del año final **2,7× los actuales**.

### Defecto 5 — margen de seguridad exigido demasiado alto (25/30/40%)
Diagnóstico de Felipe: *"es lo que hizo que perdiera oportunidades"*. Con un motor que además
infravaloraba por los defectos 1-4, el doble filtro hacía imposible comprar nada nunca.

---

## 1 · La tasa de descuento (r) — candado B, ahora en su sentido correcto

| Componente | Regla v3 |
|---|---|
| **Construcción** | WACC CAPM bottom-up completo, **empresa por empresa**. Sin excepciones. |
| **Suelo / techo** | **NINGUNO.** "CAPM real sin piso" (decisión de Felipe). Si sale 6,8% o 13,4%, se publica. |
| **rf** | Bono soberano a 10 años **de la moneda de reporte**, spot fechado al cierre del ejercicio. UST 4,70% (24-ago-2026, FRED DGS10) sólo para las que reportan en USD. |
| **ERP** | **Implícito de mercado, fechado** (~4,2-4,5% EEUU a ago-2026), no la prima fija de 5,00% inventada. Es dato de mercado, que es lo que el candado B exige. |
| **Prima de país** | Sobre el ERP, ponderada por **exposición de INGRESOS**, no por sede. Crítico en TSM (Taiwán). |
| **Beta** | **LA MENOR de dos, declarando ambas** (regla v3.1, tras el piloto): (a) desapalancada del sector re-apalancada a la estructura de la empresa a valor de mercado; (b) beta propia 5a mensual ajustada Blume (0,67·β + 0,33). **Motivo:** en el piloto la sectorial cobró a Alphabet 1,40 cuando su propio mercado le cobra 1,155, y a NVDA 1,60 cuando su propia beta es 2,21. Ningún método de beta debe castigar ni premiar de forma sistemática. |
| **Coste de deuda** | **Coste MARGINAL de emitir hoy**, no el cupón heredado (regla v3.1). El abogado del diablo demostró en UNP que usar el cupón medio en vez del 5,10-5,60% de emisión actual abarataba la tasa. |
| **Estructura de capital** | A valor de MERCADO. **Si hay caja neta → WACC = coste del equity**, y la caja entra aparte en el puente EV→equity. No se mete deuda neta negativa en la fórmula. |

## 2 · El numerador — owner earnings normalizado

| Componente | Regla v3 |
|---|---|
| **Capex** | **Separado en mantenimiento y crecimiento con evidencia.** Método: capital incremental por dólar de ingreso (regresión 5-10 años); se cruza con la divulgación de la empresa donde exista. Sólo el de **mantenimiento** resta del flujo. |
| **SBC** | **Dilución neta real**, no el gasto contable: recompras destinadas a neutralizar la emisión, o aumento neto de acciones × precio. Es lo que sale del bolsillo del dueño. |
| **Base** | **Normalizada a mitad de ciclo**: margen medio de 7 años aplicado a los ingresos ACTUALES. No la media de flujos históricos (subestima al que crece), no el último año (mide el punto del ciclo). |
| **Márgenes en la senda** | Revierten a la media histórica de 7 años **salvo defensa evidenciada en filing** de por qué el nivel actual es el nuevo estructural. Simétrico: también sube a los deprimidos (MTD, Straumann). |
| **Leases** | Arrendamientos capitalizados **dentro de la deuda neta** del puente EV→equity (ORLY, AZO, OTIS, Hermès). |

### Casos donde la fórmula estándar no aplica
- **Roll-ups (CSU, Adyen):** la M&A **es** el capex. Se resta del flujo y genera el crecimiento vía ROIIC sobre capital desplegado en adquisiciones.
- **GOOGL, AMZN:** valoración **por partes (SOTP)** — segmentos con economías incompatibles, cada uno con su tasa y su senda, sumados.
- **Float (ADP, CME, V/MA):** separar el resultado de float del operativo y valorarlos con tasas distintas.

## 3 · El motor de crecimiento — DCF explícito a 10 años

Se retira el fade geométrico de parámetro único (φ=0,87 sobre g0). Sustituido por:

**Senda en tres tramos evidenciados, año por año:**
- **Años 1-2:** guía de la empresa + backlog / RPO contratado. Etiqueta HECHO.
- **Años 3-5:** CAGR sostenible, defendido contra capacidad instalada y TAM.
- **Años 6-10:** convergencia lineal a g∞.

**g∞ = PIB nominal de largo plazo ponderado por geografía de ingresos** (~4,0-4,5% USD; ~2,8-3,2% EUR/JPY/CHF), **con tope duro en r − 2pp**. Ninguna empresa crece más que su economía para siempre.

### Los dos candados nuevos del motor
- **CANDADO TAM (bloqueante).** Un agente debe demostrar que los ingresos del año 10 caben en el mercado direccionable: cuota implicada ≤ cuota máxima defendible, y para silicio/fábricas también **capacidad física** (obleas, HBM). Si no cabe, la senda se recorta hasta que quepa. *Es el candado que habría matado el NVDA de −24,5%.*
- **CANDADO DE REINVERSIÓN (bloqueante).** El crecimiento debe estar **financiado**: el capex de crecimiento de los años previos, al ROIIC histórico, tiene que producir la g proyectada. Cierra el agujero del "crecimiento gratis".

## 4 · Salida — tres cifras, no una

1. **DCF INVERSO como titular:** *"el precio de hoy exige X% anual durante 10 años; lo evidenciado en filing es Y%"*. No requiere creer en mi VI.
2. **Banda de VI/acción** bajista / base / alcista, con el precio situado dentro o fuera.
3. **TIR esperada a 10 años** comprando hoy a este precio bajo la senda evidenciada.

### Triangulación obligatoria — las cuatro
- Múltiplo (EV/FCF, EV/EBIT) contra el percentil de su **propia** historia de 10 años.
- **Earnings yield − rf** de su moneda (la lectura Buffett: prima contra bono).
- Múltiplo de **pares del mismo mecanismo** (V↔MA, ORLY↔AZO, CDNS↔SNPS, MCO↔SPGI).
- Precio pagado por **adquirentes e insiders** con dinero propio (no vesting).

## 5 · Piso de resolución — candado C, ahora aplicado de verdad

**NO DECIDIBLE es BLOQUEANTE.** Si mover ±2pp la tasa y ±2pp el crecimiento de los años 3-5 hace que la
empresa cruce de "cara" a "barata", **no se publica cifra puntual ni posición en el ranking de valor**:
se publica la banda y la etiqueta NO DECIDIBLE. Estimación: afectará a 8-14 de las 36.

## 6 · Presentación — dos rankings, nunca fusionados

- **Ranking de CALIDAD: ordinal 1-36.** Resiste el ruido (validado ρ=0,969 entre dos rondas ciegas de ocho jueces). Se publica ordenado.
- **Valor: en CUBOS**, nunca ordinal — DESCUENTO CLARO / PRECIO JUSTO / PRIMA / NO DECIDIBLE.
- **Ficha completa por empresa**: senda año a año, WACC desglosado, crecimiento implicado vs evidenciado, caso bajista, las 4 triangulaciones.

## 7 · Margen de seguridad — RECALIBRADO

| | Antes | **Después** |
|---|---|---|
| Bloque 1 (Indestructibles) | 25% | **9%** |
| Bloque 2 (Núcleo) | 30% | **18%** |
| Bloque 3 (Frontera) | 40% | **27%** |

**Motivo (Felipe, 26-ago):** *"es demasiado, es lo que hizo que perdiera oportunidades — comprar calidad
a un precio justo"*. Es el giro Munger sobre Graham. El candado A (veto bloqueante de `abogado-diablo`
en sesión limpia) sigue siendo obligatorio antes de toda COMPRA: el margen más bajo **no** relaja ese veto.

## 8 · Arquitectura de agentes — 4 papeles por empresa (144 en la tanda completa)

| Agente | Mandato | Entrega |
|---|---|---|
| **A · FLUJO** | Owner earnings normalizado a mitad de ciclo; capex separado mantenimiento/crecimiento con evidencia; SBC como dilución neta; leases en deuda neta; casos especiales (SOTP, roll-up, float). | Flujo base año 0 en moneda de reporte, con cada ajuste trazado a filing. |
| **B · TASA** | WACC bottom-up sin piso: rf de su moneda, ERP implícito fechado, prima de país por ingresos, beta sectorial re-apalancada, coste de deuda real, caja neta → coste del equity. | WACC con **cada componente desglosado y con fuente**. |
| **C · SENDA** | 10 años explícitos en tres tramos; g∞ = PIB nominal con tope r−2pp; **candado TAM bloqueante**; **candado de reinversión bloqueante**; márgenes revirtiendo a media 7a. DCF directo + DCF inverso + TIR. | Senda año a año, VI banda, crecimiento implicado, TIR. |
| **D · ABOGADO DEL DIABLO** | **Sesión limpia**, no ve el razonamiento de A/B/C, sólo sus números. Mandato único: **refutar a la baja** la senda y el margen normalizado. Además ejecuta las 4 triangulaciones. | Caso bajista evidenciado + VI bajista + las 4 triangulaciones. |

**Prueba de simetría (candado A aplicado a la valoración, no sólo a la compra):** el agente D existe
porque todas las correcciones 1-5 empujan los valores **hacia arriba**. Sin adversario dedicado, el
riesgo es fabricar el documento espejo — irrealmente optimista — y repetir el error con el signo cambiado.

## 9 · Datos vivos y disciplina de fuente

- **Precios**: todos al mismo **cierre fechado**, nunca intradía. Comparabilidad entre las 36.
- **FX**: los 5 tipos (EUR, JPY, CHF, CAD, GBp) al mismo cierre que los precios, declarados.
- **Moneda**: cada empresa se descuenta en **su moneda de reporte** con el rf soberano de esa moneda; el VI se convierte a USD sólo al final. Descontar yenes con una tasa en dólares es un error de dimensión.
- **Las 7 de fuente única no auditada** (Hermès, Constellation, HOYA, OBIC, Adyen, Straumann, Keyence): **un agente extra por empresa buscando segunda fuente primaria** (informe anual local, registro mercantil, 20-F, folleto). Si aparece, dejan de estar degradadas. Si no, cifra DEGRADADA → veredicto máximo VIGILAR.

## 10 · Alcance — reapertura de knock-outs contaminados

Los knock-outs ejecutados contra la tasa plana de 9,70% quedan **anulados y se reabren**: toda empresa
eliminada por "ROIC < coste de capital" se recalcula con su WACC bottom-up real y se readmite si sobrevive.
Casos identificados: **WM** (ROIC 8,2% vs WACC real ~6,5-7%) y **ZTS**. Pendiente auditar el resto del
universo de 485 por el mismo motivo. **El instrumento roto no sólo valoró mal: también expulsó mal.**

## 11 · Orden de ejecución

1. **PILOTO DE 3 con contraste conocido** — GOOGL (Buffett compra), NVDA (Felipe dice que está cara), UNP (+588%, el absurdo mayor). 12 agentes. Si el motor nuevo resiste el olfato de Felipe, se calibra y se sigue.
2. Las 33 restantes, 4 agentes cada una.
3. Reapertura de knock-outs contaminados.
4. Entregables: **CSV auditable con todos los inputs** (obligatorio) + PDF con el diseño del 26-ago + este documento de recalibración + 36 fichas Markdown.

## 12 · Lo que este motor sigue sin resolver

- El TAM casi nunca es un HECHO verificable en filing; el candado TAM descansa en la mejor estimación disponible, declarada como INFERENCIA.
- La separación mantenimiento/crecimiento del capex es la corrección más difícil y la más discrecional de las cinco. Es donde volverá a colarse el sesgo si vuelve a colarse.
- El candado B4 sigue CERRADO: nada de lo que produzca este motor autoriza una compra por sí solo.

---
### Registro de recalibración v3.1 — mismo día, tras el piloto de 3
| Pieza | Antes (v3.0) | Después (v3.1) | Motivo |
|---|---|---|---|
| Beta | sectorial re-apalancada, siempre | **la menor de sectorial y propia-Blume**, ambas declaradas | El piloto expuso que la sectorial cobra a GOOGL más riesgo del que su propio mercado le cobra (1,40 vs 1,155), y a NVDA menos (1,60 vs 2,21). Un solo método sesga en direcciones opuestas según la empresa. |
| Coste de deuda | rendimiento de emisiones vivas o gasto/deuda media | **coste marginal de emitir hoy** | `abogado-diablo` sobre UNP: el cupón heredado subestimaba la tasa frente al 5,10-5,60% real de emisión. |

### Resultado del piloto de 3 (2026-08-26)
| | VI viejo | VI v3 | VI del diablo | Precio exige | Evidenciado | Ruido |
|---|---|---|---|---|---|---|
| **NVDA** | $279,5 (−24,5%) | **$116,8 (+80,7%)** | $73,9 | 21,7% | 11,5% | DECIDIBLE |
| **GOOGL** | $94,6 (+262%) | **$137,0 (+150%)** | $94,7 | 23,3% | 10,2% | DECIDIBLE |
| **UNP** | $45,5 (+588%) | **$200,2 (+56%)** | $113,3 | 8,4% | 2,1% | **NO DECIDIBLE** |

Tres lecciones medidas:
1. **El candado TAM dio la vuelta a NVDA entera.** Su senda sin techo daba 1,23 billones $ de ingresos en el año 10 = 41% del mercado mundial de semiconductores; nadie ha pasado nunca del ~20% (Intel 15-16%, Samsung 12%). Recorte del 27% aplicado.
2. **El candado C mordió por primera vez:** UNP salió NO DECIDIBLE (VI de $127 a $375 con ±2pp de tasa).
3. **El abogado del diablo refutó los TRES números.** Los agentes de senda salen con optimismo sistemático medido: sin el cuarto agente, este motor habría fabricado el documento espejo.

*v3.1 — 2026-08-26. Recalibración aprobada por Felipe tras 28 preguntas cerradas. Recalibración anterior: 2026-08-21 (v2).*
