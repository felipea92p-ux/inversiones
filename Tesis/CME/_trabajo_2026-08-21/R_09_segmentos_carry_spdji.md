# REFUTACIÓN ADVERSARIAL — DIMENSIÓN 9
## "Anatomía del beneficio: carry sobre colateral, S&P DJI, datos de mercado"

**Refutador en contexto limpio · 21 de agosto de 2026 · CME 275,01 USD**
**Documento atacado:** `/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/CME/_trabajo_2026-08-21/09_segmentos_carry_spdji.md`

---

## VEREDICTO: **DEGRADADO**

La tesis central del dossier **aguanta**: el carry es un peaje de ~30 pb sobre el efectivo, la "escalada de retención" del 7,0 % al 8,9 % es un artefacto del denominador, y S&P DJI está en libros de CME a 1.400 M contra una marca auditada de 4.914 M en los libros del comprador contractualmente obligado. **Verifiqué contra EDGAR todas y cada una de las cifras estructurales y todas reproducen** — algunas al céntimo. Las citas textuales son literales (con una excepción de forma).

Pero **tres afirmaciones concretas son FALSAS**, y una de ellas es precisamente la que el dossier señala en mayúsculas como *"LA LAGUNA MÁS IMPORTANTE DE ESTA DIMENSIÓN"*: el dato existe, está publicado, y está **en el mismo 10-Q que el dossier cita quince veces**.

---

# PARTE I — LO QUE SE ROMPE

## R-1. **FALSO** — "Sobre el 55 % del colateral que custodia, CME no gana absolutamente nada / ni un céntimo"

El dossier apoya esta frase en una cita correcta pero **truncada en su alcance**:

> "Securities deposited by the clearing firms are not reflected on the consolidated financial statements and the clearing house **does not earn any interest** on these deposits."
> {CME 10-K FY2025, Nota 4 — Performance Bonds and Guaranty Fund Contributions. VERIFICADO literal}

La frase dice que CME no gana **INTERESES**. No dice que no gane nada. En el **mismo 10-K**, Nota 3 — Revenue Recognition:

> "**Collateral management fees are charged to clearing firms that have collateral on deposit with the clearing house to meet their minimum performance bond and guaranty fund obligations on the exchange. These fees are calculated based on daily collateral balances.**"
> {CME 10-K FY2025, Nota 3 — Revenue Recognition, "Other". VERIFICADO literal}

Y la columna que el dossier llama "no efectivo" se titula en la propia tabla del 10-K **"Non-Cash Deposits and IEF Funds"**, siendo IEF el *Interest Earning Facility* — un programa **propiedad de CME**:

> "...money market funds or through **CME's Interest Earning Facility (IEF) program**."
> {CME 10-K FY2025, Nota 4. VERIFICADO literal}

**Consecuencia cuantitativa:** la estimación estrella de la sección A.6 —"volver del 45,5 % al 32,6 % de efectivo costaría ~137 M USD anuales"— es una cifra **bruta**, no neta. Parte de esos 137 M se recuperaría vía collateral management fees sobre el colateral que se desplazaría a valores. CME no desglosa el importe (va dentro de "Other revenues": 436,4 / 431,7 / 326,7 M en 2025/2024/2023, VERIFICADO), de modo que la magnitud del error no es acotable — pero la afirmación categórica **"no gana absolutamente nada"** es falsa contra fuente primaria.

---

## R-2. **FALSO** — "El ARPC por línea de producto CME no lo publica y no aparece en ningún filing… ES LA LAGUNA MÁS IMPORTANTE DE ESTA DIMENSIÓN"

Este es el hallazgo más valioso de la refutación. El dossier afirma dos veces que **"CME no publica ingresos por línea de producto"** y construye toda la sección D.4 como una tabla de **SUPUESTOS** sobre el ARPC de índices (0,678 / 0,600 / 0,500 / 0,450).

**CME sí publica ingresos de compensación por línea de producto**, en la nota de desagregación de ingresos, en el mismo 10-Q del 2T-2026 (accession 0001156375-26-000047) que el dossier utiliza para todo lo demás:

| (M USD) | 2T-2026 | 2T-2025 | 1S-2026 | 1S-2025 |
|---|---:|---:|---:|---:|
| Interest rates | 433,0 | 461,6 | 954,2 | 897,9 |
| **Equity indexes** | **324,0** | **301,6** | **639,6** | **605,8** |
| Foreign exchange | 49,8 | 52,4 | 106,6 | 105,8 |
| Agricultural commodities | 183,8 | 174,7 | 351,3 | 339,0 |
| Energy | 187,0 | 217,4 | 450,7 | 433,8 |
| Metals | 76,7 | 85,1 | 195,1 | 156,0 |
| BrokerTec fixed income | 40,1 | 37,1 | 80,3 | 72,9 |
| EBS foreign exchange | 33,8 | 37,5 | 70,2 | 72,7 |
| Interest Rate Swap | 24,3 | 20,6 | 47,1 | 41,4 |

{CME 10-Q 2T-2026, Nota 3 — Revenue Recognition, tabla de desagregación. VERIFICADO línea a línea}
{Serie anual equivalente: 10-K FY2025, Nota 3 — Equity indexes **1.170,4 / 1.095,3 / 1.036,4** en 2025/2024/2023. VERIFICADO}

Cruzando con el ADV por línea que el propio dossier ya usa, **el ARPC de índices es directamente calculable**:

| Periodo | Ingreso índices (M) | Contratos (M) | **ARPC índices** | Licencia/contrato | **Licencia como % del ingreso de índices** |
|---|---:|---:|---:|---:|---:|
| 2T-2025 | 301,6 | 475,0 | **0,6350** | 0,2025 | **31,9 %** |
| **2T-2026** | 324,0 | 535,3 | **0,6053 (−4,7 %)** | 0,2038 | **33,7 %** |
| 1S-2025 | 605,8 | 962,7 | 0,6293 | 0,2003 | 31,8 % |
| **1S-2026** | 639,6 | 1.063,2 | **0,6016 (−4,4 %)** | 0,2031 | **33,8 %** |
| FY2024 | 1.095,3 | 1.725,4 | 0,6348 | 0,2060 | 32,4 % |
| FY2025 | 1.170,4 | 1.859,9 | 0,6293 | 0,1995 | 31,7 % |

**Validación del método:** aplicando exactamente el mismo procedimiento al agregado (ingresos de compensación menos BrokerTec, EBS e IRS, que no están en el ADV de futuros) obtengo **0,6779** para el 2T-2026 y **0,6901** para el 2T-2025, frente a los **0,678 y 0,690 publicados por CME**. El método reproduce la cifra oficial a cuatro decimales. El ARPC de índices de 0,6053 es tan sólido como el agregado.

**Qué cambia:** la tabla de escenarios de D.4 se colapsa a un solo renglón. El escenario "0,600" que el dossier trata como hipótesis es el **dato real**. La conclusión cualitativa del dossier ("la línea de índices es dilutiva en cuanto el ARPC baja de ~0,60") sobrevive — y de hecho se confirma: el ARPC de índices está **exactamente en el umbral y cayendo al 4,7 % interanual**. Pero el dossier declaró incalculable, y elevó a "pregunta directa a relaciones con inversores", un número que está impreso en el filing que cita.

---

## R-3. **FALSO / AUTOCONTRADICTORIO** — "El punto de ruptura está en Fed funds ~1,5 %: por debajo de ahí el spread de 30 pb ya no cabe dentro del rendimiento bruto"

Esta es la frase que el dossier propone convertir en **gate de falsificación** en `gates.md`. Está mal especificada por tres vías independientes:

1. **Aritmética.** Con Fed funds al 1,5 % el rendimiento bruto es ~150 pb. 30 pb es el 20 % de 150 pb. Caben de sobra. La retención del 20 % sería *inferior* al 31,2 % que CME retuvo en 2021.
2. **Autocontradicción.** El propio Escenario 2 del dossier (sección A.5) dice, para Fed funds 1,63 %: *"30,4 pb (cabe, apurado)"*. La tesis del texto y la tabla del mismo apartado se contradicen.
3. **Evidencia empírica en contra.** En 2022, con Fed funds medio del 1,69 % y rendimiento bruto de 146,7 pb, CME retuvo **18,9 pb** — cuando había sitio para 30. No fue una restricción, fue una elección. {10-K FY2022, MD&A: bruto 2.169,5 M, distribuido 1.889,7 M. VERIFICADO literal}

Con el propio modelo del dossier, el acantilado se sitúa **por debajo del ~1 % de Fed funds**, no en el 1,5 %. El gate propuesto, tal como está escrito, dispararía una alarma en un nivel de tipos donde la partida todavía vale ~250 M/año (el 4,7 % del beneficio antes de impuestos normalizado).

---

# PARTE II — LO QUE QUEDA DEGRADADO

## D-1. "Seis observaciones consecutivas" son cuatro

El hallazgo clave dice: *"Seis observaciones consecutivas (2023, 2024, 2025, 1S-2025, 1S-2026) caen entre 29,3 y 32,2 pb"*. Se anuncian **seis** y se enumeran **cinco**. Y de esas cinco, **1S-2025 está contenido dentro de FY2025**: no es una observación independiente. Observaciones independientes reales: **2023, 2024, 2025 y 1S-2026 = cuatro**.

## D-2. La precisión de "±1,5 pb" es un artefacto de la convención de promediado

Reconstruí el spread con los saldos trimestrales de XBRL (`us-gaap:GoodFaithAndMarginDepositsWithBrokerDealers`) y **reproduje exactamente** los saldos medios del dossier (131.727 / 147.868 / 110.793 / 93.738 / 134.089 / 120.583 / 160.934). El cálculo es honesto. Pero es **frágil a la convención**:

| Año | Spread con **5 cierres** (dossier) | Spread con **4 trimestres del año** | Spread sobre **saldo de cierre** |
|---|---:|---:|---:|
| 2021 | 4,1 | 3,8 | 3,4 |
| 2022 | 18,9 | 19,3 | 20,7 |
| 2023 | **32,2** | **34,0** | **39,5** |
| 2024 | **29,3** | **29,0** | **27,7** |
| 2025 | **30,7** | **28,8** | **25,7** |
| 1S-2025 | **30,2** | **27,7** | **25,6** |
| 1S-2026 | **30,4** | **30,3** | **31,0** |
| **Rango 2023-1S26** | **2,9 pb** | **6,3 pb** | **13,9 pb** |

La **dirección** de la conclusión sobrevive a las tres convenciones: no hay proporcionalidad con el tipo, y no hay tendencia al alza en la retención en puntos básicos. Eso es lo que sostiene la refutación del expediente previo y **aguanta**. Lo que no aguanta es la retórica: *"±1,5 pb"*, *"menos del 10 % de dispersión"*, *"una constante de ingeniería, no un mercado"*. Con una convención igual de defendible la dispersión es del 22 % de la media; con saldos de cierre, del 47 %.

## D-3. "151 pb" y "cuatro años" no son el mismo periodo

Fed funds medio verificado contra FRED DFF (descarga propia): 2023 **5,0259 %**, 2024 **5,1422 %**, 2025 **4,2118 %**, 1S-2026 **3,6355 %**. La caída **2023 → 1S-2026 es de 140 pb**. Los 151 pb requieren arrancar en el pico de 2024, que son **dos años y medio**, no cuatro. El veredicto en una frase dice literalmente *"estable dentro de ±1,5 pb durante cuatro años consecutivos con los Fed funds cayendo del 5,14 % al 3,63 %"* — mezcla la ventana de cuatro años con el recorrido de dos y medio.

## D-4. La fórmula de sensibilidad publicada no reproduce su propia tabla

El dossier escribe: `spread = mín(30,4 ; 4,1 + 7,42 × FF%)`. Aplicada:

| FF | Fórmula escrita | Tabla del dossier |
|---:|---:|---:|
| 2,63 % | 23,6 pb | **23,0 pb** |
| 1,63 % | 16,2 pb | **15,6 pb** |
| 0,63 % | 8,8 pb | **8,2 pb** |
| 1,69 % (validación 2022) | 16,6 pb | **16,1 pb** |

La tabla sigue en realidad `4,1 + 7,4085 × (FF − 0,08)` — interpolación entre los dos anclajes. Los **resultados** de la tabla son internamente correctos (verifiqué los nueve escenarios de la Tabla 4 y todos cuadran con esa fórmula); lo que está mal transcrito es la fórmula, incluido el punto que se presenta como "validación fuera de muestra".

Y esa validación es generosa: un único punto fuera de muestra con **15 % de error** (predice 16,1 pb, observado 18,9 pb) no es "aceptable" para un modelo del que cuelga un gate de falsificación.

## D-5. La Tabla 4 mezcla dos denominadores; la Tabla 1 y la Tabla 9 discrepan sobre el mismo número

- En la Tabla 4, las filas de **tipos** calculan el % sobre un pretax reducido por la pérdida de carry (`5.287,9 − Δ`): 370/(5.287,9−119) = 7,16 % ✓. Las filas de **saldo** no lo reducen: 440/5.287,9 = 8,33 % (el dossier dice 8,35 %). Dos metodologías en la misma tabla, sin nota.
- El carry TTM de 474,1 M aparece como **8,48 % del pretax** en la Tabla 1 (sobre 5.594,0, sin normalizar) y como **8,97 %** en la Tabla 9 (sobre 5.287,9, normalizado). Ambos cálculos son correctos; conviven sin advertencia en el mismo documento.

## D-6. Dos recuentos de acciones distintos en la misma sección

El dossier anota bajo la Tabla 5: *"(360,310 M de acciones diluidas medias, {10-K FY2025, cuenta de resultados})"*. Esa cifra es correcta como hecho (VERIFICADO: diluted weighted average **360.310** miles en FY2025). **Pero no produce las cifras por acción de esa tabla.**

- 4.914 / 360,310 = **13,64**, no 13,67.
- 5.024 / 360,310 = **13,94**, no 13,97.
- 3.514 / 360,310 = **9,75**, no 9,77.

Los valores publicados salen de dividir por **359,58 M**, que es el número real de acciones en circulación: *"359,576,125 shares of Class A common stock"* al 8-jul-2026 {10-Q 2T-2026, portada. VERIFICADO}. Es decir: el dossier **usó el número correcto y citó el incorrecto** en el por acción, y luego usó el incorrecto (360,310) para la capitalización del EV.

Con una única base consistente y datos vivos:
- Capitalización = 359,576 × 275,01 = **98.882 M** (no 99.089)
- Deuda a 30-jun-2026 = **3.424,2 M** {10-Q, balance. VERIFICADO} — el dossier usó 3.422,3, que es la de **31-dic-2025**, mientras tomaba la caja de 30-jun-2026 (2.144,2, VERIFICADO). EV con fechas mezcladas.
- EV = 98.882 + 3.424,2 − 2.144,2 = **100.162 M** → **22,72×** EBIT TTM, no 22,8×.

Impacto económico: **nulo** (0,2 %). Impacto sobre la confianza en el resto de la aritmética: no nulo, porque es el tipo de descuadre que un lector no puede detectar sin rehacer la división.

## D-7. Dos bases distintas de "colateral total", usadas indistintamente

Verifiqué la tabla del 10-K FY2025 (Nota 4):

| (M) | Cash 2025 | No-cash 2025 |
|---|---:|---:|
| **Performance bonds** | **156.187,7** | **186.748,9** |
| Guaranty fund contributions | 2.736,1 | 8.474,3 |
| Cross-margin arrangements | 304,1 | 456,5 |
| Other | 428,2 | 2,1 |
| **Total** | **159.656,1** | **195.681,8** |

La Tabla 3 del dossier (152.060 → 342.936,6; CAGR **+14,52 %**; % en efectivo **45,5 %**; correlaciones) usa **solo la fila "Performance bonds"**. La frase con la que refuta al expediente previo —*"El colateral total a 31-dic-2025 era de 355.337,9 M"*— usa el **Total**. Ambas cifras son correctas y las verifiqué en el filing. Pero son bases distintas y el documento no lo advierte: sobre la base ancha el % en efectivo de 2025 es **44,9 %**, no 45,5 %, y el saldo de efectivo que alimenta el cálculo del spread (159.656,1, del balance) no es el de la tabla del mix (156.187,7).

## D-8. "Motor SECULAR ligado al interés abierto" es INFERENCIA etiquetada como HECHO

**Todas las correlaciones del dossier reproducen** en mi recálculo independiente sobre FRED VIXCLS y los saldos XBRL:

| Estadístico | Dossier | Mi recálculo |
|---|---:|---:|
| corr(colateral total, VIX medio anual), n=7 | −0,187 | **−0,1875** |
| corr(colateral total, tiempo), n=7 | +0,973 | **+0,9732** |
| corr(efectivo trimestral, VIX del trimestre) | +0,455 | **+0,4549** |
| corr(efectivo trimestral, tiempo) | +0,805 | **+0,8052** |
| corr(Δ% trimestral efectivo, ΔVIX) | +0,561 | **+0,557** |
| CAGR colateral 2019-2025 | +14,52 % | **+14,516 %** |
| VIX medio 2019-2025 | 15,39 / 29,25 / 19,66 / 25,64 / 16,85 / 15,55 / 18,93 | **idénticos** |

La aritmética es impecable. La **inferencia** no lo es:

1. **n = 7.** Un coeficiente de −0,187 con siete observaciones tiene un p-valor de ~0,69 e intervalo de confianza aproximado de −0,83 a +0,63. No permite afirmar "el colateral no depende de la volatilidad" como HECHO. Permite afirmar "no encuentro relación con este tamaño muestral", que es otra cosa.
2. **corr(nivel, tiempo) = +0,973 con n=7 es casi tautológico**: dos series crecientes cualesquiera dan eso. No es evidencia de mecanismo.
3. **CME no publica ninguna serie de interés abierto en su 10-K** (lo comprobé: solo menciones cualitativas). La atribución del 14,5 % anual al interés abierto no está anclada en dato. Y el mecanismo que sí publica el 10-K apunta en la dirección contraria: *"the clearing firms' collateral requirements are sized to cover **at least one business day of anticipated price movements**"* {Nota 4, VERIFICADO literal} — es decir, volatilidad × posiciones × nocional. El S&P 500 aproximadamente dobló entre 2019 y 2025; parte del 14,5 % es simple revalorización del nocional.

## D-9. El "deterioro silencioso" de la licencia S&P se apoya en un solo año y en una comparación cruzada

Cifras verificadas literalmente: *"S&P Dow Jones Indices LLC earned **$193 million, $192 million and $174 million** of revenue under the terms of the License Agreement"* {SPGI 10-K FY2025, Nota 14 — Related Party Transactions. VERIFICADO}.

Pero el dossier compara ese +0,5 % de 2025 contra el **ADV de índices total (+8,2 %)**, que incluye Nasdaq y Russell. La comparación correcta es contra el **ingreso de índices de CME**, ahora que sabemos que está publicado:

| Año | Licencia a S&P DJI (M) | Ingreso de índices de CME (M) | **S&P DJI / ingreso índices** |
|---|---:|---:|---:|
| 2023 | 174 | 1.036,4 | **16,79 %** |
| 2024 | 192 | 1.095,3 | **17,53 %** |
| 2025 | 193 | 1.170,4 | **16,49 %** |

El ratio es **estable en torno al 17 %**. 2025 no es un deterioro estructural: es una **reversión desde el máximo de 2024**, año en el que la licencia S&P creció el 10,3 % contra un ingreso de índices que creció el 5,7 % — exactamente al revés de la tesis. Dos observaciones consecutivas de signo opuesto no son una tendencia.

Y la atribución del residual es frágil: el dossier imputa el +8,9 % del "resto" a Nasdaq/Russell, cuando la propia definición del 10-K de esa línea dice: *"This expense also includes **royalty fees and broker rebates on energy and metals products**, as well as revenue sharing on cleared swaps contracts and some new product launches"*. En 2025 el **ADV de metales subió el 34 % y el ingreso de metales el 24,8 %** {10-K FY2025, VERIFICADO}. Los royalties de metales explican por sí solos una parte indeterminada del +8,9 % que el dossier atribuye al mix de índices.

## D-10. Cherry-picking de ventana en el argumento del mix

El dossier cita *"E-mini S&P 500 +2 %, E-mini Nasdaq 100 +32 %"*. Verificado. Pero **la misma fila de la misma tabla del mismo 10-Q** da también el semestre: **E-mini S&P +3 %, E-mini Nasdaq 100 +20 %**. Se eligió el trimestre con la brecha más ancha para sostener un argumento presentado como estructural y plurianual.

## D-11. "Es un reparto de BENEFICIOS, no un royalty por contrato" — hay dos fuentes primarias y solo se citó una

SPGI dice *"a share of the profits from the trading and clearing"*. **CME dice otra cosa, en el mismo párrafo del 10-K del que el dossier extrae los plazos de la licencia:**

> "**We pay the applicable third-party a revenue share under the terms of these licensing agreements.**"
> {CME 10-K FY2025, Item 1 — "Licensing Agreements". VERIFICADO literal}

El dossier convierte la palabra de SPGI en la base de una "protección estructural del margen que el caso bajista no contempla", y omite que la contraparte de ese mismo contrato lo llama reparto de **ingresos** en su propio filing. La conclusión económica sobrevive por otra vía (tanto un revenue share como un profit share se auto-ajustan a la baja con la micronización del ARPC), pero la afirmación está apoyada en la única de las dos fuentes que le conviene.

*(A favor del dossier: encontré una frase que NO citó y que refuerza su cálculo del "vuelve el 27 %": "The entire amount of this revenue is included in our consolidated statement of income and **the portion related to the 27% noncontrolling interest is removed in net income attributable to noncontrolling interests**." {SPGI 10-K FY2025, Nota 14, VERIFICADO}. El mecanismo de retorno está explícito en el filing.)*

## D-12. "Ningún filing lo dice" — el filing lo dice

El dossier lista en "lo que no pude verificar": *"Si CME tiene poder contractual para fijar unilateralmente el spread de 30 pb sobre el colateral, o si es una negociación periódica con las firmas compensadoras. **Ningún filing lo dice.** Es la pregunta que decide si los 30 pb son un precio administrado o un equilibrio de mercado."*

Está en la Nota 4 del 10-K FY2025, tres frases antes del párrafo que el dossier cita dos veces:

> "Any interest earned on these investments accrues to CME and is included in investment income on the consolidated statements of income. **CME may distribute any interest earned on these investments to the clearing firms at its discretion.**"
> {CME 10-K FY2025, Nota 4. VERIFICADO literal}

Y en el MD&A:

> "Other income (expense) includes expenses related to the distribution of **a portion** of interest earned on performance bond collateral reinvestment to the clearing firms…"
> {CME 10-K FY2025, Item 7. VERIFICADO literal}

**Es un precio administrado, discrecional y unilateral.** Esto tiene dos consecuencias que el dossier no puede seguir esquivando:

1. Refuerza la lectura **alcista** que el dossier descarta explícitamente ("el alcista que la use como prueba de poder de fijación de precios comete el error simétrico"). Si la distribución es discrecional y CME ha sostenido ~30 pb durante cuatro ejercicios, eso **es** poder de fijación de precios, aunque no lo haya subido.
2. Desmonta el mecanismo narrado para 2021 ("no caben 30 pb en un pastel de 13"): CME distribuyó 119,6 de 173,9 M **por elección**, no por imposibilidad. La cota inferior de 54,3 M es un hecho; la explicación mecánica de por qué, no.

## D-13. Contra-evidencia pública omitida: poder de precios en datos de mercado

El dossier cita la subida de 85 a 105 USD/mes por dispositivo como *"una subida del +23,5 % de golpe"*. **La frase inmediatamente siguiente en el mismo 10-K de FY2019, que no se cita, es:**

> "The increase was partially offset by **a reduction in revenue due to modest declines in screen counts** due to cost-cutting initiatives at member firms."
> {CME 10-K FY2019, MD&A. VERIFICADO literal}

Es decir: el único punto de precio anclado en filing viene acompañado, en el mismo párrafo, de la evidencia de atrición de unidades. Eso es exactamente el riesgo de elasticidad que el dossier menciona después de forma cualitativa, y estaba disponible como HECHO.

## D-14. Contra-evidencia pública omitida: el perímetro de la licencia del S&P 500

El dossier concluye: *"la licencia exclusiva del S&P 500 no vence… no hay ventana en la que un competidor pueda pujar… pueden lanzar un perpetuo sobre un índice sintético, **pero no sobre el S&P 500**."*

La cita es literal y correcta. **El alcance del contrato, en la frase inmediatamente anterior a la citada, no lo es:**

> "…we have a license agreement (S&P License Agreement) for certain S&P stock indices… in connection with the creation, marketing, trading, clearing and promoting of **futures contracts and/or options on futures contracts** that are indexed to certain S&P stock indices."
> {CME 10-K FY2025, Item 1. VERIFICADO literal}

La exclusividad cubre **futuros y opciones sobre futuros**, no todo derivado sobre el S&P 500. Las opciones sobre el índice liquidadas en efectivo (el complejo SPX, incluido el 0DTE) son un mercado licenciado por S&P a otra bolsa y no pasan por CME. Y el propio 10-K, en el **mismo párrafo del que se extrae la cita del 5 %**, advierte de lo contrario de lo que el dossier concluye:

> "…we cannot guarantee that others will not succeed in creating stock index futures based on information similar to that which we own or have obtained by license, or that market participants will not increasingly use other instruments, **including securities and options based on the S&P, Dow Jones, Nasdaq or FTSE Russell indices**, to manage or speculate on U.S. stock risks…"
> {CME 10-K FY2025, Item 1. VERIFICADO literal}

El foso existe y es real. Su perímetro es más estrecho que el que el dossier dibuja.

## D-15. Higiene de citas: una paráfrasis presentada entre comillas

El dossier escribe entre comillas y con fuente:

> "Effective July 1, 2026, we have four reportable segments: Market Intelligence, Ratings, Energy and Indices. The results of Mobility are included through June 30, 2026."

El texto real del SPGI 10-Q 2T-2026 es:

> "Effective July 1, 2026, **our operations consist of** four reportable segments: **S&P Global Ratings ("Ratings"), S&P Dow Jones Indices ("Indices"), S&P Global Energy ("Energy") and S&P Global Market Intelligence ("Market Intelligence")**."

…y la segunda frase citada aparece **después de una lista de cuatro viñetas descriptivas**, no a continuación. El contenido es correcto; la forma no. Es la única cita de las quince que verifiqué que no es literal.

## D-16. Detalles menores verificados con desviación

- **5.024 M a 30-jun-2026**: el saldo **total** de NCI rescatable es 5.024; la nota precisa *"As of June 30, 2026, **$5,022 million** relates to our redeemable noncontrolling interest in the Indices business"*. Desviación de 2 M. (A 31-dic-2025 el total era 4.917 y la parte de Índices 4.914 — la atribución del dossier es limpia.)
- **"1.400 M en libros"**: el 10-K dice *"$1.4 billion"*. La precisión de tres cifras significativas es del dossier, no del filing.
- **Kalshi/MerQube, contrato US500 perpetuo presentado a la CFTC el 18-ago-2026**: no verificable con los filings de esta dimensión. Queda como dato heredado sin anclaje en este dossier.

---

# PARTE III — LO QUE INTENTÉ ROMPER Y **AGUANTA**

Esto vale tanto como las refutaciones. Ataqué lo siguiente con fuente primaria y **no se rompió**:

### 1. La serie completa del carry — **VERIFICADA LITERALMENTE, cifra por cifra**

| Año | Bruto | Distribuido | Neto | Documento verificado |
|---|---:|---:|---:|---|
| 2021 | 173,9 | 119,6 | 54,3 | 10-K FY2022, MD&A ✓ |
| 2022 | 2.169,5 | 1.889,7 | 279,8 | 10-K FY2022 y FY2023, MD&A ✓ |
| 2023 | 5.073,9 | 4.717,5 | 356,4 | 10-K FY2023, MD&A ✓ |
| 2024 | 3.943,8 | 3.669,4 | 274,4 | 10-K FY2025, Nota 4 ✓ |
| 2025 | 5.253,6 | 4.842,5 | 411,1 | 10-K FY2025, Nota 4 ✓ |
| 1S-2025 | 2.361,2 | 2.179,3 | 181,9 | 10-Q 2T-2026 ✓ |
| 1S-2026 | 2.759,8 | 2.514,9 | 244,9 | 10-Q 2T-2026 ✓ |
| 2T-2026 | 1.388,8 | 1.265,7 | 123,1 | 10-Q 2T-2026 ✓ |

*(Dato adicional que el dossier no usa y que verifiqué: 2T-2025 bruto 1.487,6 / distribuido 1.374,5 → neto 113,1.)*

### 2. El error de unidades del expediente previo — **CONFIRMADO EXACTO**
244,9 / 2.196,1 (net income 1S-2026) = **11,15 %**; 244,9 / 2.838,6 (pretax 1S-2026) = **8,63 %**. Ambos denominadores verificados en el 10-Q. La acusación de mezcla numerador-pretax con denominador-post-tax es correcta al decimal.

### 3. La refutación central (spread plano, retención % como artefacto) — **AGUANTA BAJO LAS TRES CONVENCIONES**
Reproduje los siete saldos medios exactamente desde XBRL. La retención de 7,02 / 6,96 / 7,83 / 8,87 % reproduce. Y bajo cualquiera de las tres convenciones de promediado, el spread en pb **no muestra tendencia alcista** mientras el porcentaje de retención sí. La conclusión —"CME no ha subido su comisión sobre el colateral"— sobrevive a mi mejor intento de romperla.

### 4. La refutación del margen operativo — **VERIFICADA ÍNTEGRA**
FY2023 61,58 % · FY2024 64,13 % · FY2025 64,86 % · 1T-25 67,47 % · 2T-25 66,74 % · 1S-25 67,10 % · 1T-26 69,66 % · 2T-26 64,89 % · 1S-26 67,39 %. Todos reproducen desde XBRL `Revenues` y `OperatingIncomeLoss`. La acusación de cherry-picking por mezcla de periodicidad al expediente previo es **correcta**.

### 5. El puente exacto del 2T-2026 — **VERIFICADO LÍNEA A LÍNEA**
Las diez líneas de la Tabla 8 coinciden con el 10-Q sin una sola desviación, y el total cuadra en −22,2 M.

### 6. La tabla de colateral efectivo/no efectivo 2019-2025 — **VERIFICADA EN CINCO 10-K DISTINTOS**
35.597,3/116.462,7 (FY2020) · 83.923,5/124.573,7 (FY2020) · 151.094,8/70.005,3 (FY2021) · 132.653,7/94.127,2 (FY2023) · 87.285,5/180.866,3 (FY2023) · 96.036,4/191.241,1 (FY2025) · 156.187,7/186.748,9 (FY2025). Exactas.

### 7. Todo el bloque de S&P Global — **VERIFICADO, INCLUIDA LA PARTE QUE SOSPECHÉ QUE ESTABA MAL**
- *"As of December 31, 2025, $4,914 million relates to our redeemable noncontrolling interest in the Indices business"* ✓ literal. **Sospeché que el 4.914 (solo Índices) se comparaba con un 5.024 total contaminado; NO es así**: el total a 31-dic-2025 es 4.917 y a 30-jun-2026 es 5.024 con 5.022 de Índices. La parte no-Índices es de 3 M. La comparación es limpia.
- WACC 10,8 %, crecimiento terminal 2,2 %, sensibilidad ±135/108 M ✓ literal.
- Put: *"CME Group and CGIS **has the right at any time to sell, and we are obligated to buy, at least 20 %** of their share"* ✓ literal, más *"we would generally be required to purchase the interest at fair value on the date of redemption"* ✓ — el put **sí** es a valor razonable.
- *"after **December 31, 2017**"* ✓ — está en el MD&A de SPGI (no en la Nota 9 que cita el dossier, pero está).
- Beneficio atribuible al NCI rescatable: 241 / 285 / 317 (2023/24/25) y 153 / 197 (1S-25 / 1S-26) ✓ literales.
- Segmento Indices: ingresos 1.403 / 1.628 / 1.850 y beneficio operativo 925 / 1.103 / 1.271 ✓; 1S-2025 891/624 y 1S-2026 1.053/745 ✓. Márgenes 65,93 / 67,75 / 68,70 / 70,03 / 70,75 % ✓. TTM 2.012 / 1.392 / 69,18 % ✓.
- Related party 193 / 192 / 174 M ✓ literal.
- CME Nota 7: 27 % de participación y *"$1.4 billion"* ✓.
- Mobility Global / MBGL / NYSE / 1 por 1 / registro 15-jun-2026 / efectiva 1-jul-2026 ✓ literales.

### 8. Los términos de las licencias — **VERIFICADOS LITERALES**
Umbral del 5 %, extensión de hasta diez años, exclusividad del S&P 500 hasta un año antes de la terminación, Dow Jones con término inicial hasta 30-jun-2026 y renovación automática quinquenal "so long as there is open interest", Nasdaq hasta 2039, Russell hasta 2037. **Todo literal.**

### 9. La serie de datos de mercado y todas sus citas — **VERIFICADA**
406,5 / 391,8 / 449,6 / 518,5 / 545,4 / 576,9 / 610,9 / 663,7 / 710,2 / 803,1 y los ingresos totales 2016-2025, todos desde XBRL y los estados de resultados. CAGR +7,86 % ✓. Las citas del riesgo *"12% of our total revenues"*, de los revendedores (*"approximately 30 % … and approximately 32 % in 2023"*) y de la subida a 105 desde 85 USD ✓ literales. *(Extra verificado: la serie de concentración es 45 % en 2017, 41 % en 2018, 37 % en 2019 — una desconcentración de una década.)*

### 10. Estadística y series externas — **RECALCULADAS DE FORMA INDEPENDIENTE Y COINCIDENTES**
Todas las correlaciones (−0,1875 / +0,9732 / +0,4549 / +0,8052 / +0,557), el CAGR (+14,516 %), las medias anuales de VIX y las de Fed funds (5,0259 / 5,1422 / 4,2118 / 4,33 / 3,6355). Coinciden.

### 11. La aritmética de sensibilidad — **LOS NUEVE ESCENARIOS CUADRAN**
Base 489, −100 pb → 370, −200 → 251, −300 → 132, ZIRP → 66; saldo −10/−15/−25 % → 440/416/367; combinado → 213. Todos reproducen (con la fórmula real, no con la escrita).

### 12. Lo que **no** conseguí romper aunque lo intenté con ganas
- Busqué que el 4.914 fuera un total contaminado. No lo es.
- Busqué que el segmento Indices de SPGI fuera mucho mayor que la JV, para invalidar el múltiplo de 13,1×. **Cruce independiente:** 317 M atribuidos al NCI del 27 % implican una JV de ~1.174 M de beneficio en 2025 contra 1.271 M de beneficio operativo del segmento — la JV es ~92 % del segmento. La objeción no prospera; el múltiplo de 13,1× es defendible.
- Busqué que la validación cruzada CME 200,1 / SPGI 197 fuera una coincidencia de niveles. Lo es en parte (las tasas de crecimiento divergen +6,9 % vs +28,8 % por el efecto OSTTRA), pero el dossier ya lo explica y el nivel es la magnitud relevante.
- Busqué que los saldos medios estuvieran mal calculados. No lo están: reproducen al millón.

---

# PARTE IV — QUÉ HAY QUE CAMBIAR ANTES DE USAR ESTA DIMENSIÓN

1. **Borrar** "sobre el 55 % del colateral CME no gana nada". Sustituir por: "sobre el 55 % del colateral CME no gana **intereses**, aunque sí cobra collateral management fees calculadas sobre saldos diarios de colateral, de importe no desglosado". Y marcar los ~137 M del riesgo de mix como **cota superior bruta**.
2. **Borrar** la laguna del ARPC por línea. Sustituir por el dato: **ARPC de índices 0,6053 USD en 2T-2026 (−4,7 % interanual), licencia = 33,7 % del ingreso bruto de la línea (31,9 % un año antes)**. Esto *fortalece* el caso bajista sobre el margen incremental con un dato duro en lugar de un supuesto.
3. **Reescribir el gate.** No es "Fed funds < 1,5 %". Con el propio modelo del dossier el acantilado está **por debajo del ~1 %**; entre el 1,5 % y el 1,0 % el daño es de 250-300 M/año, doloroso pero acotado. Un gate mal fijado dispara falsos positivos.
4. **Rebajar la retórica del spread**: de "constante de ingeniería ±1,5 pb" a "orden de magnitud de 30 pb sin tendencia respecto a los tipos, con una dispersión de entre 3 y 14 pb según cómo se promedie el saldo". La conclusión no cambia; la falsa precisión sí debe irse.
5. **Unificar una sola base de acciones (359,58 M, portada del 10-Q) y una sola fecha de deuda (3.424,2 M, 30-jun-2026).** EV = 100.162 M, EV/EBIT TTM = 22,7×.
6. **Degradar de HECHO a INFERENCIA**: "motor secular ligado al interés abierto" (n=7, sin serie de OI publicada), "cada dólar a S&P DJI vuelve al 27 %" (correcto en mecanismo, pero es una inferencia sobre margen incremental de SPDJI), y "el deterioro silencioso del mix S&P→Nasdaq" (un año, comparación cruzada, residual contaminado por metales).
7. **Añadir la frase que decide el debate de poder de precios:** *"CME may distribute any interest earned on these investments to the clearing firms at its discretion"*. Es el dato que el dossier declaró inexistente y es el más importante de toda la sección A.

---

**Fuentes primarias descargadas y verificadas por el refutador (EDGAR, 21-ago-2026):**
CME 10-K FY2025 `0001156375-26-000009` · CME 10-Q 2T-2026 `0001156375-26-000047` · CME 10-K FY2023 `0001156375-24-000010` · CME 10-K FY2022 `0001156375-23-000020` · CME 10-K FY2021 `0001156375-22-000076` · CME 10-K FY2020 `0001156375-21-000020` · CME 10-K FY2019 `0001156375-20-000013` · SPGI 10-K FY2025 `0000064040-26-000013` · SPGI 10-Q 2T-2026 `0000064040-26-000045` · SEC XBRL companyfacts CIK 0001156375 · FRED DFF y VIXCLS.
**Todas las accession numbers del apéndice del dossier son correctas.**
