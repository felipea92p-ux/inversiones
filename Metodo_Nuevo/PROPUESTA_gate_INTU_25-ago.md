# PROPUESTA — gate de INTU antes del 25-ago-2026

**No he tocado `gates.md`.** Se propone y tú apruebas. Quedan **tres días**.
Evidencia completa en `intu_gate.json`. Precio: **367,00 USD** (cierre 21-ago-2026, IBKR).
Posición: 24 acciones · 8.808 USD · **6,0% del NAV** · coste medio 262,23 (**+39,9%**).

---

## 1. LO PRIMERO: el gate que se iba a sellar estaba ROTO, y el fallo era fatal

Se construyó un gate sobre el **Online Ecosystem ex-Mailchimp del Q4** con umbral en **≤19% → vender
las 24 acciones**. Un agente adversarial lo atacó por seis vías antes de sellarlo y **lo rompió en
cuatro**. El fallo central, con aritmética verificada contra EDGAR:

> **El umbral de venta total estaba POR ENCIMA del techo de la guía.** Si Intuit cumple exactamente lo
> que prometió el 20-may-2026, el dato sale entre **16,7% y 18,4%** → el gate **vende el 100% de la
> posición por cumplir la guía**.

El error aritmético: se proyectó *"GBS FY guiado ~16%, luego el Q4 cae en 15-17%"* ignorando que **los
9M ya corren al +17,1%**. Para que el año cierre en ~16%, el Q4 tiene que crecer **por debajo** de 16%.

Despeje inverso, que lo dice sin ambigüedad:
- Umbral ≤19% ⟺ Total Q4 ≤ **$4.290M** (+12,0%). **El techo de la guía es $4.280M (+11,7%).**
  El gatillo estaba **10 millones por encima del techo guiado**.
- Umbral ≥23% ⟺ Total Q4 ≥ $4.365M (+13,9%) — **batir el techo por 2,1 puntos**. No era "el extremo
  alto de lo guiado": estaba **fuera** de lo guiado.

**Es el error de BKNG replicado y amplificado.** En Booking el gatillo caía *dentro* de la banda de
guía; aquí caía *por encima del techo*.

---

## 2. Los otros tres fallos, porque cada uno enseña algo

**Se puede gamear, y la empresa ya lo hizo.** Efectivo el **1-ago-2025** —el primer día del ejercicio
que el gate mide— Intuit combinó Consumer, Credit Karma y ProTax en un solo segmento y recasteó las
cifras (10-Q Q3 FY26, nota 12). Eso **dispara automáticamente** el candado del gate secundario
("si reasigna unidades de reporte → recortar a la mitad"): falso positivo garantizado por un hecho
benigno publicado hace nueve meses. Además **Intuit ya retiró la guía ex-Mailchimp**: la daba el
21-ago-2025 y el 20-nov-2025, y dejó de darla el 26-feb-2026 y el 20-may-2026. Precedente directo y
reciente de retirar la métrica exacta sobre la que se apoyaba el gate. Y "excluding Mailchimp" es
**no-GAAP sin conciliación numérica**: Intuit nunca publica los ingresos de Mailchimp, así que el dato
no es auditable ni reconstruible desde los estados financieros.

**No tiene resolución — viola el candado C.** El intervalo de predicción del dato es de **±6 puntos**
(redondeo de la guía Consumer 4,1 pp · tamaño de Mailchimp 5,4 pp · Desktop 1,7 pp · varianza del beat
0-4 pp · redondeo del propio dato 1 pp). **Las bandas del gate medían 3 puntos cada una.** Traducido:
*el gate no mide el motor del negocio — mide el tamaño del beat de Intuit sobre su propia guía
trimestral*, que es gestión de expectativas, no información.

**La mitad de la métrica es macro, no cuota.** El Online Ecosystem son dos patas: QuickBooks Online
Accounting (3.732M en 9M = **51%**, suscripción, test de cuota legítimo) y **Online Services (3.583M =
49%**, que escala con el volumen de transacciones de las pymes y con los tipos de interés). Casi la
mitad del umbral se mueve con el gasto de las pymes de EE.UU. Y ya se está moviendo: Online Services
19% (FY25) → 17% → 18% → **15%** (Q3 FY26). **Es la misma clase de error que el gatillo de TurboTax,
solo que enterrado en la mitad de la métrica en vez de a la vista.**

---

## 3. Y el hallazgo que hace que todo lo anterior importe menos de lo que parece

> **En las tres ramas del gate —16,7%, 20% o 24%— el precio sigue un 44% por encima de tu zona de
> compra.** Los tres tramos que fijaste (298 / 280 / ≤266) están los tres por debajo del mercado. No
> hay un solo nivel de compra vigente que el precio no haya dejado atrás.
>
> **Un gate cuyo desenlace no altera la respuesta a "¿la comprarías hoy?" no es un gate: es un
> aplazamiento con mejor letra.**

---

## 4. PROPUESTA — dos decisiones separadas, y solo una depende del martes

### A · El recorte de 24 a 12 acciones NO depende del dato. Se ejecuta por precio.

Justificado **hoy**, sin esperar al martes:
- Precio 367,00 contra una zona de compra propia de **≤255** (+44%).
- La tesis vigente es la del 26-jul, que **su propio autor marcó como "sunk cost disfrazado de todavía"**
  y que **nunca invirtió la carga de la prueba** — el test del hoy ya falla hoy, con datos de hoy.
- Sacarlo del gate lo blinda contra tres cosas a la vez: el sesgo de disposición, el gap de apertura del
  miércoles y la renegociación del martes.

**Acción: vender 12 acciones. Posición de 24 → 12 (de 6,0% a ~3,0% del NAV).**

### B · Lo que el dato del 25-ago decide es solo qué pasa con las 12 restantes

Umbrales **recalibrados sobre el despeje real** (neutro = cumplimiento exacto de guía = **17,6%**, no
21-24% como decía el gate roto). Con un intervalo de ±6 pp solo caben dos ramas informativas:

| Dato (OE ex-Mailchimp, Q4) | Significado | Acción con las 12 |
|---|---|---|
| **≤12%** | Fallo real contra el compromiso público (Total Q4 ≈ $4.155M, miss de ~2,5 pp bajo el suelo guiado) | **Vender las 12. Posición a cero.** |
| **13% – 24%** | **NO INFORMATIVO** — declarado por escrito ahora, antes de ver el dato | **Mantener 12, sin ampliar.** Revisión por precio, no por trimestre. |
| **≥25%** | Fuerza real (batir el techo guiado en ~3 pp, el tamaño del beat de Q1 FY26) | **Mantener 12, sin ampliar.** |

**Si Intuit no publica el ex-Mailchimp** (ya retiró su versión prospectiva): mismos umbrales trasladados
**2,5 pp abajo** sobre el Online Ecosystem all-in. La brecha fue 5 → 4 → 4 → 3 pp y es decreciente.

### C · Reglas de ejecución, corregidas

- **Orden a mercado en la apertura del miércoles 26-ago. Punto.** El límite "no peor de −1,5% del cierre
  del 25" **se auto-bloquea**: el comunicado sale *tras el cierre*, así que un dato malo abre con gap
  muy superior y la orden quedaría colgada justo en el único escenario donde manda vender.
- **Se elimina la caducidad del 30-sep** tal como estaba escrita: su condición de escape era *"que
  Felipe escriba una tesis nueva"*, y **un gate no puede tener como condición de liberación un acto del
  decisor** — escribir la tesis el 29-sep evitaba el recorte.
- **Se elimina el modificador de Consumer**: confundía tres métricas que Intuit trata por separado
  (*total TurboTax Online units*, *TurboTax Online paying units*, y la tabla nueva anunciada). El martes
  habría que interpretar, e interpretar es renegociar.
- **Candado de deterioro de goodwill**: se conserva, con la ruta corregida — se lee en el **balance
  condensado** (13.982M al 30-abr-2026), **no** en la conciliación no-GAAP; esa línea solo aparece en el
  glosario boilerplate. Para *intangibles adquiridos* **no es medible el 25-ago**: el balance da el neto
  y no distingue deterioro de amortización ordinaria.

---

## 5. LECTURAS AMABLES PROHIBIDAS — escritas antes de ver el dato

Lección de DUOL, donde el gate se rompió y aparecieron tres lecturas benignas a posteriori:

1. *"El ex-Mailchimp cae porque Mailchimp ya no pesa"* — la métrica ya lo excluye por construcción.
2. *"Q4 es estacionalmente flojo en GBS"* — se compara contra el mismo Q4 del año anterior.
3. *"Los 300-340M del cargo por la reducción del 17% de plantilla distorsionan"* — el umbral es de
   crecimiento de **ingresos**; ningún cargo lo toca.
4. *"El Investor Day del 17-sep dará contexto"* — el gate vence el 25-ago y una presentación no es
   fuente contable.
5. *"Ya lleva +39,9%, vender es pagar impuestos"* — efecto disposición, ya marcado como encendido.
6. *"Un trimestre no hace tendencia"* — es el **cuarto** punto de la serie (26% → 25% → 22% → ?).

---

## 6. LO QUE ESTA PROPUESTA NO RESUELVE

- **El agente de métricas del workflow falló** (error de API). El redactor y el adversario fueron a los
  filings por su cuenta y verificaron la métrica en cuatro comunicados consecutivos, así que la cadena
  está cubierta — pero no por la vía que se diseñó.
- **La decisión A es tuya.** Vender 12 acciones hoy por precio, sin esperar al martes, es la
  recomendación; no la ejecuto yo y no debe ejecutarse sin que la apruebes.
