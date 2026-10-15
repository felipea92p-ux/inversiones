# V_R5_moat_historia — Verificación adversarial de R5_moat_historia (foso e historia de ORCL, Paso 3)

**Verificador:** agente `verificador` (contexto limpio, solo fuentes primarias). **Fecha:** 2026-10-15 (trabajo 2026-10-14/15). **Objeto:** 36 hechos de `R5_moat_historia.md`, priorizados por lo que sostiene el juicio de foso. **Mandato:** refutar, no confirmar.

**Resultado global:** 22 CONFIRMADOS, 1 REFUTADO (R5-06: la caracterización "doce años encogiéndose" de licencias nuevas; la aritmética de extremos −49,7 % sí se sostiene), 13 DEGRADADOS (casi todos por lo mismo: el corpus local solo contiene 10-K FY25/FY26, 10-Q, 8-K y companyfacts, y desde este entorno sec.gov, data.sec.gov, FRED y db-engines.com no son alcanzables; todo lo que el lector leyó en 10-K FY11–FY24 o en el 10-K FY1994 de Oracle Systems y no aparece en companyfacts queda DEGRADADO, no refutado).

**Acceso a red (declarado):** `curl` por el proxy a www.sec.gov / data.sec.gov / fred / treasury.gov devuelve `CONNECT tunnel failed, response 403`; `WebFetch` a sec.gov y db-engines.com devuelve `getaddrinfo ENOTFOUND`. No pude abrir ningún filing fuera de `edgar_txt/`. `WebSearch` solo se usó como pista (nunca eleva a HECHO); sus resúmenes citan texto que parece proceder de filings de EDGAR de 1993-94, pero no pude abrirlos.

**Qué es "segunda fuente primaria" aquí:** (a) filings distintos que reportan la misma cifra (p. ej. 10-K FY14, FY15 y FY16 para licencias FY14; 10-K + 8-K + 10-Q para FY26), y (b) `companyfacts.json` (XBRL de cada 10-K, etiquetas sin dimensión). Aviso de método: companyfacts **no contiene** datos dimensionales, así que ni soporte/licencias de FY18–FY22 ni márgenes por segmento son reproducibles desde él; solo las etiquetas obsoletas `LicensesRevenue` y `MaintenanceRevenue` (FY08–FY17) llevan esas líneas.

Fuentes consultadas por mí (todas locales, `edgar_txt/`): 10-K FY26 (accn 0001193125-26-277521, 2026-06-22), 10-K FY25 (0000950170-25-087926, 2025-06-18), 10-Q 1T FY27 (0001193125-26-389274, 2026-09-11), 8-K de resultados 2025-09-09, 2025-12-10, 2026-03-10, 2026-06-10, 2026-09-10, DEF 14A 2025/2026, `companyfacts.json` (CIK 0001341439, 10-K FY10 a FY26). Búsqueda de cadenas sobre los documentos locales de `edgar_txt/`. Código propio: `scratchpad/v5/verif_r5.py` y `scratchpad/v5/dump.py` (volcado de companyfacts con accession y fecha de presentación).

---

## Veredictos por hecho

### R5-01 · Soporte: "substantially all" compran y renuevan; precio = % de la licencia neta, facturado por adelantado, a opción del cliente, ~1 año (a1, a2)
- **Fuentes:** 10-K FY26 (2026-06-22) Item 1 "Oracle Software Support": "Substantially all of our customers opt to purchase software support contracts when they purchase these software licenses… Substantially all software support customers renew their support contracts with us upon expiration"; Item 7: "Software support contracts are generally: priced as a percentage of the net fees paid by the customer to purchase a software license; billed in advance… renewed at the customer's option; and recognized as revenues ratably… generally one year". 10-K FY25 (2025-06-18) Nota de políticas: "License support contracts are generally priced as a percentage of the net cloud license and on-premise license fees. Substantially all of our customers elect to purchase and renew their license support contracts annually"; y lista como expectativa prospectiva "that substantially all of our customers will renew their license support contracts upon expiration".
- **Veredicto: CONFIRMADO** (dos 10-K consecutivos, redacción coincidente).
- **Implicación:** la afirmación "se repite sin cambios desde FY2011" (a2) NO la verifiqué (los 10-K FY11–FY20 no están en el corpus): esa parte es DEGRADADA. Lo que sí está primario: la mecánica del peaje (% de la licencia, prepago, opcional) y que Oracle solo la cuantifica con el adverbio "substantially". Es una afirmación cualitativa de la propia empresa, no una métrica medida.

### R5-02 · Oracle no publica tasa de renovación ni attach rate (a3)
- **Fuentes:** búsqueda de `renewal rate | attach rate | retention rate | churn` sobre los documentos locales de `edgar_txt/`: 2 coincidencias, ambas en Item 1A (10-K FY25 y FY26): "may affect our renewal rates for software support". Ninguna en 8-K, 10-Q ni DEF 14A. Ninguna cifra numérica de renovación.
- **Veredicto: CONFIRMADO** (ausencia).
- **Implicación:** la tasa real de renovación es laguna dura. Matiz de exactitud: el lector dice que la búsqueda en el DEF 14A de "retention" dio 0; "retention" sí aparece (retención de talento, L5514). La sustancia no cambia.

### R5-03 · Margen del segmento soporte 86 % (FY11) → 91 % (FY16) y "% del margen total" 70 % → 86 % (a-tabla de márgenes)
- **Fuentes:** esas tablas viven en 10-K FY11–FY16, que no están en el corpus ni son alcanzables; companyfacts no tiene márgenes por segmento. Prueba de coherencia propia con XBRL (OI, I+D, amortización de companyfacts): margen de soporte FY16 = 0,91 × 18.861 = 17.164; si es el 86 % del margen total, margen total = 19.958 M. Pero OI 12.604 + I+D 5.787 + amortización 1.638 = **20.029 M**, y a eso hay que sumar G&A, reestructuración y gastos de adquisición, que son partidas positivas de conciliación. Mismo problema en FY11 (total implícito 18.178 vs OI+I+D+amort 18.980). Es decir, el "% del margen total" del lector es incompatible con la conciliación a OI salvo que "total margin" se defina neto de asignaciones que no puedo ver.
- **Veredicto: DEGRADADO** (no reproducible; coherencia interna dudosa en la fila del porcentaje del total).
- **Implicación:** el 86→91 % de margen del soporte es una cifra de 10-K antiguos que el valorador no debe usar como HECHO hasta reabrir la nota de segmentos FY16 y FY11. El "% del margen total" (70→86 %) es el dato más frágil: no se sostiene contra la conciliación a resultado operativo. Oracle dejó de desglosarlo en FY17, así que el margen actual del soporte es inobservable en primaria.

### R5-04 · Serie de soporte FY11 14.796 … FY26 19.804; +8,8 % FY14→FY26 (0.2, 0.3)
- **Fuentes:** companyfacts `MaintenanceRevenue` (10-K FY12 a FY17): 14.796 (FY11, reportada en 10-K FY12 y FY13), 16.210, 17.142, 18.206 (FY14: 10-K FY14, FY15 y FY16), 18.847, 18.861, **19.229** (FY17). 10-K FY25: 19.426 (FY23), 19.609 (FY24), 19.523 (FY25). 10-K FY26: 19.609 / 19.523 / 19.804. Aritmética propia: 19.804/18.206 − 1 = **+8,78 %**; FY14→FY17 +5,62 %.
- **Veredicto: CONFIRMADO** (extremos y puntos FY11–FY17 y FY23–FY26 por filings distintos). Diferencia menor: el lector pone 19.230 para FY17; XBRL dice 19.229 (1 M$, redondeo).
- **Implicación:** reserva que el lector no declara: desde FY23 la línea de soporte incluye ingresos de Cerner (adquirida 2022-06-08; el propio lector dice que aportó 5,9 B en FY23, de los que 2,2 B servicios y 0,14 B hardware). Esos ≈3,6 B caen en las líneas de cloud/licencia/soporte sin desglose. Por tanto el "+8,8 %" mezcla soporte orgánico de Oracle e inorgánico de Cerner, y la meseta 19,4–19,8 B de FY23–FY26 podría esconder un soporte orgánico a la baja. Con el corpus no puedo separarlo. Además es nominal en USD (cc FY26: −1 %). FY18–FY22 (19.779, 19.365) son DEGRADADOS: no están en companyfacts ni en los 10-K locales.

### R5-05 · Licencias nuevas FY14 9.416 → FY26 4.737 = −49,7 % (0.3, c3)
- **Fuentes:** FY14 = 9.416: companyfacts `LicensesRevenue` reportada en 10-K FY14 (2014-06-26, 0001193125-14-251351), 10-K FY15 (0001193125-15-235239) y 10-K FY16 (0001193125-16-628942). FY26 = 4.737: 10-K FY26 (Item 7 y Nota de ingresos), 8-K 2026-06-10 y 8-K 2026-09-10 (tabla trimestral: 766+939+1.150+1.881 = 4.736, redondeo), y 4.737 en 10-Q 1T FY27 (comparativo). Aritmética propia: 4.737/9.416 − 1 = **−49,69 %**; CAGR −5,56 %.
- **Veredicto: CONFIRMADO** (aritmética de extremos).
- **Implicación:** los extremos no son estrictamente la misma línea. FY14 es "new software licenses" (pre-ASC 606, pre-reorganización); FY26 es "Software license", que según el 10-K FY25 son licencias perpetuas "used for cloud-based, on-premise and other IT environments" (incluye licencias que se llevan a cloud, "BYOL"). El corte FY17/FY18 (reorganización + ASC 606; el total FY17 se reexpresó de 37.728 a 37.792 y FY18 de 39.831 a 39.383) no se puede aislar para licencias con el corpus. Úsese "≈ −50 % entre dos definiciones próximas", no "serie homogénea".

### R5-06 · "El motor… lleva doce años encogiéndose"; "captación nueva en licencia reducida a la mitad en doce años" (0.3, c3)
- **Fuentes:** puntos verificados: FY14 9.416; FY15 8.535; FY16 7.276; FY17 6.418 (companyfacts); FY23 5.779 (10-K FY25); FY24 5.081, **FY25 5.201 (+2,4 %; el 10-K FY25 dice +2 % USD, +3 % cc)**; FY26 4.737. Tramos propios: FY14→FY17 **−31,8 %**; FY17→FY23 −10,0 %; FY23→FY26 −18,0 %; FY25→FY26 −8,9 %. Con las cifras del propio lector no verificables (FY20 5.127, FY22 5.878): FY14→FY20 −45,6 %, **FY20→FY22 +14,6 %**, FY20→FY26 −7,6 %.
- **Veredicto: REFUTADO** como caracterización. No hay doce años de caída continua: hay un desplome FY14→FY17 (−32 %, verificado), seis años (FY17→FY23) de descenso lento (−10 %), un repunte en FY25 (+2,4 %) y otra caída en FY24 (−12,1 %) y FY26 (−8,9 %). El nivel FY23–FY26 (5,8 → 4,7 B) vs el de FY17 (6,4 B) es −10 % a −26 %, no −50 %: dos tercios del recorte (−31,8 de −49,7 puntos porcentuales sobre la base FY14) ya estaban hechos en FY17.
- **Implicación (cifra corregida):** "licencias −49,7 % FY14→FY26, de los cuales −31,8 % ocurrieron en FY14–FY17; desde FY17 el descenso acumulado es −26,2 % (6.418→4.737)". La lectura "motor que se apaga de forma sostenida" no está soportada; la lectura "escalón a la baja en la transición 2014-17 y erosión irregular después" sí. El dato nuevo relevante es la aceleración reciente: FY26 −9 % (−10 % cc) y 1T FY27 −15 % (−14 % cc), con Oracle atribuyendo la caída a la migración a cloud (ver R5-10).

### R5-07 · Ratio soporte/licencia: 1,6x (FY11), 1,93x (FY14), 4,18x (FY26)
- **Fuentes:** aritmética propia: 18.206/9.416 = 1,934; 19.804/4.737 = **4,181**; FY11 14.796/9.235 = 1,602 (cifra del 10-K FY12) o 14.796/8.980 = 1,648 con la reexpresión del 10-K FY13 (`LicensesRevenue` FY11: 9.235 en 10-K FY12, 8.980 en 10-K FY13).
- **Veredicto: CONFIRMADO.**
- **Implicación:** ver hallazgo extra 1: la serie de licencias FY11/FY12 cambió de base entre el 10-K FY12 y el FY13.

### R5-08 · 5,4 B$ de ingreso cloud anualizado de clientes de soporte que migraron (3 años hasta FY26); 4,3 B$ hasta FY25 (a9, 0.4)
- **Fuentes:** 10-K FY26 Item 1 (2026-06-22): "During the past three fiscal years, customers with annual software support contracts that migrated to the Oracle Cloud contributed to the increase in annualized cloud revenue by $5.4 billion" y "we are in the early stages of what we expect will be a material migration". 10-K FY25 Item 1 (2025-06-18): "…increase in annualized cloud services revenue by $4.3 billion".
- **Veredicto: CONFIRMADO** (cita exacta, dos 10-K).
- **Implicación:** la cifra mide **ingreso cloud ganado** (anualizado, run-rate, ventana móvil de 3 años: FY23–25 vs FY24–26), NO el soporte perdido. El 10-K no cuantifica cuánto soporte se dio de baja por esas migraciones ni el efecto neto. Como orden de magnitud, 5,4 B es el 27 % del soporte anual de 19,8 B, pero no es "canibalización" medida. El soporte en cc −1 % (R5-09) es lo único observado del lado de la pérdida.

### R5-09 · Soporte FY26 19.804 (−1 % cc, +1 % USD); FY25 0 % cc; serie trimestral cc 1T26 −1 %, 2T26 0 %, 3T26 0 %, 4T26 −1 %, 1T27 −1 % (a4, e)
- **Fuentes:** 10-K FY26 Item 7 tabla: "Software support 19,804 | 1% | −1% | 19,523". 10-K FY25: "License support 19,523 | 0% | 0% | 19,609". 8-K 2025-09-09, 2025-12-10, 2026-03-10, 2026-06-10, 2026-09-10 (tablas "Constant Currency Revenue Growth Rates"): FY26 (1T–4T–año) −1 %, 0 %, 0 %, −1 %, −1 %; 1T FY27 −1 %. 10-Q 1T FY27: "Software support 4,895 | −1% | −1% | 4,955".
- **Veredicto: CONFIRMADO** (5 8-K + 10-K FY25/FY26 + 10-Q).
- **Implicación:** ninguna sobre el dato. Todos los porcentajes son redondeados al entero.

### R5-10 · "Soporte −1 % cc dos trimestres seguidos" (observable de que el reloj arrancó; e)
- **Fuentes:** cc: 4T FY26 −1 %, 1T FY27 −1 % (8-K 2026-06-10 y 2026-09-10). Importes sin redondear (8-K): FY25 4.896/4.869/4.797/4.961; FY26 4.955/4.938/4.969/4.943; 1T FY27 4.895. Variación USD propia: 1T26 +1,21 %, 2T26 +1,42 %, 3T26 +3,59 %, **4T26 −0,36 %, 1T27 −1,21 %**. 8-K 2026-09-10: "Software revenues were down 3% to $5.5 billion, reflecting our customers' continuing migration from on-premises software to the Cloud" (5.550 vs 5.721 = −2,99 %).
- **Veredicto: CONFIRMADO** (dos trimestres negativos consecutivos en cc y en USD; el segundo supera el redondeo en USD).
- **Implicación:** el observable propuesto se cumple en sentido técnico, pero (i) el 4T FY26 en USD es −0,36 %, dentro de lo que el redondeo llama "0 %/−1 %"; (ii) Oracle atribuye por escrito la caída del conjunto software a la migración a cloud, no a una pérdida de clientes: el filing no permite separar "salida" de "traslado". El test (b) del lector (soporte + cloud infra) sigue siendo la forma de distinguirlo, y no se puede calcular con el corpus porque la infraestructura cloud mezcla clientes nuevos y migrados.

### R5-11 · Licencias FY26 −9 % USD / −10 % cc; 1T FY27 −15 %; FY24 −12 %; "cc negativo dos años (FY24, FY26)" (a4, e)
- **Fuentes:** 10-K FY26: "Software license 4,737 | −9% | −10% | 5,201". 10-Q 1T FY27: "Software license 655 | −15% | −14% | 766". 8-K 2026-06-10: cc trimestral FY26 −13 %, −23 %, −2 %, −6 %. FY24: 5.081 vs 5.779 = −12,1 % USD (10-K FY25). FY25: +2 % USD, +3 % cc (10-K FY25).
- **Veredicto: CONFIRMADO** (FY26, 1T FY27 y FY24 en USD).
- **Implicación:** el −12 % de FY24 es USD; no verifiqué su valor cc. El "cc negativo dos años" del lector omite que FY25 fue **positivo** (+3 % cc): los dos años negativos no son consecutivos. El −15 % es USD (cc −14 %).

### R5-12 · Composición de ingresos FY26: cloud 33.989 (51 %; FY25 43 %, FY24 37 %); apps 15.888, infra 18.101; recurrente 79,9 % (a4-a7, a15)
- **Fuentes:** 10-K FY26 Item 1 y Nota de desagregación: cloud applications 15.888 / 14.272 / 12.934; cloud infrastructure 18.101 / 10.234 / 6.840; total cloud 33.989 / 24.506 / 19.774; software 4.737 y 19.804; cloud & software 58.530. Companyfacts `Revenues`: 67.357 / 57.399 / 52.961. Aritmética propia: 58.530 − 4.737 − 19.804 = 33.989 = 15.888 + 18.101; (33.989+19.804)/67.357 = **79,86 %**; apps/cloud 46,7 % / 58,2 % / 65,4 %.
- **Veredicto: CONFIRMADO.**
- **Implicación:** "recurrente 79,9 %" incluye infraestructura cloud de IA por consumo/contrato (no solo suscripción), así que no es comparable con el "recurrente" del foso de soporte.

### R5-13 · Margen del negocio cloud & software FY24 64 %, FY25 63 %, FY26 59 %; gastos de cloud & software +56 % (16.850 vs 10.827), +5,7 B de infraestructura (c4, d)
- **Fuentes:** 10-K FY25 (2025-06-18): "Total Margin % 63% | 64%" (FY25, FY24); 10-K FY26: "Total Margin % 59% | 63%"; ingresos 58.530, gastos totales 24.062, margen 34.468 (=58,9 %); FY25 30.930/49.230 = 62,8 %. Línea "Cloud and software (1) 16,850 | 56% | 54% | 10,827" y MD&A: "…a $5.7 billion increase in infrastructure expenses".
- **Veredicto: CONFIRMADO** (FY24–FY26).
- **Implicación:** el 16.850 vs 10.827 es la línea de coste de cloud & software; el gasto total del negocio (con ventas y marketing) sube +31,5 % (24.062 vs 18.300). Citar el +56 % como "gastos del negocio" sobrerrepresenta; es la línea de coste de prestación.

### R5-14 · Margen cloud & software FY18 67 %, FY19 66 %, FY20 66 %, FY21 68 %, FY22 67 %, FY23 64 % (c4)
- **Fuentes:** requiere 10-K FY18–FY23, no presentes en el corpus; companyfacts no tiene márgenes por segmento.
- **Veredicto: DEGRADADO.**
- **Implicación:** el contraste "67 % (FY18) → 59 % (FY26)" solo tiene verificados los tres últimos puntos. Además compara definiciones distintas del negocio (FY18 "cloud and license", FY26 "cloud and software" con infraestructura de IA y Cerner). Es una pista, no una tendencia homogénea.

### R5-15 · Crisis 1990-91: ingresos FY90–FY94, pérdida FY91 (12.401 k$), beneficio operativo 135.341→17.907, deuda a corto 42.501→180.065 (×4,2) (c1)
- **Fuentes:** 10-K FY1994 de Oracle Systems (CIK 777676, accn 0000891618-94-000150): no está en el corpus y sec.gov no es alcanzable. Reproduje la aritmética del lector con código propio: crecimientos +12,2 %, +14,6 %, +27,5 %, +33,2 %; margen operativo 14,8 % → 1,7 %; deuda ×4,24. Pista externa (SECUNDARIO, no eleva): resumen de una búsqueda que cita a Tech Monitor (1991): pérdida de 12,4 M$ "on turnover up 12% to $1,028m", coincidente con 12.401 y 1.027.949.
- **Veredicto: DEGRADADO** (las cifras son internamente coherentes y la pista coincide, pero no pude leer la fuente primaria).
- **Implicación:** nada contradice el relato (pérdida con ingresos creciendo +12 %: problema de calidad de ingresos/caja, no de demanda). Pero para Li Lu no debe citarse como HECHO verificado por mí.

### R5-16 · SEC, demandas, SOP 91-1, causa contable, Henley (c1)
- **Fuentes:** ídem (10-K FY1994 no alcanzable). Pista (SECUNDARIO): una búsqueda devuelve enlaces a documentos de Oracle Systems en EDGAR (10-Q FY1994 0000891618-94-000093; 10-K FY1994) con texto que dice que la SEC presentó demanda el 1993-09-24, que se aprobó sentencia consentida el 1993-10-20 con multa civil de 100.000 $ pagada el 1993-10-27, sin admitir culpa, periodo de estados inexactos agosto 1989–noviembre 1990, y acuerdo de clase de 23,25 M$ para compradores del 1989-07-11 al 1990-09-26. No pude abrir esos documentos.
- **Veredicto: DEGRADADO.**
- **Implicación:** la **laguna 9 del lector ("texto primario del acuerdo con la SEC: solo prensa") probablemente es falsa**: parece estar en los propios filings de Oracle de 1994 (probablemente el 10-K FY1994 que el lector tiene en su sesión). Corresponde al lector releer el 10-K FY1994 y subir esos datos a HECHO si están. La causa (reconocimiento de licencias al firmar, doble facturación) y la cifra de adopción de SOP 91-1 (43,47 M$) siguen sin primaria verificada por mí.

### R5-17 · Ingresos totales planos FY14→FY20: 38.275 → 39.068 (+2,1 %) (c4)
- **Fuentes:** companyfacts `Revenues`: FY14 38.275 (10-K FY14, FY15, FY16); `RevenueFromContractWithCustomer…` FY20 39.068 (10-K FY20, FY21, FY22). Aritmética propia: **+2,07 %**.
- **Veredicto: CONFIRMADO.**
- **Implicación:** base mixta: FY14 pre-ASC 606 vs FY20 post-606 (el total FY17 se reexpresó +64 M$, FY18 −448 M$). La tabla c4 del lector pone FY18 = 39.831 (base antigua) junto a FY19 = 39.506 (base nueva): aparenta −0,8 % FY18→FY19, cuando like-for-like (39.383→39.506) es +0,3 %. No cambia la conclusión de ingresos planos.

### R5-18 · Licencias FY18–FY22 (6.190; 5.855; 5.127; 5.399; 5.878), soporte FY21 19.779 y FY22 19.365, "licencias −45,6 % y soporte +8,6 % FY14→FY20/21", margen "new software licenses" 31 %→6 % (c4)
- **Fuentes:** requieren 10-K FY18–FY23 y FY11–FY16 (nota de segmentos); no están en companyfacts (sin dimensión) ni en el corpus local. Aritmética del lector reproducida: 5.127/9.416 = −45,55 %; 19.779/18.206 = +8,64 %.
- **Veredicto: DEGRADADO.**
- **Implicación:** el −45,6 % depende de FY20 = 5.127 y el +8,6 % de FY21 = 19.779, ambos no verificados. Los extremos verificados (FY14→FY17 −31,8 %, FY14→FY17 soporte +5,6 %) ya cuentan la misma historia con menos fuerza. Nótese que FY22 19.365 < FY21 19.779 (−2,1 % USD) según el lector, es decir, soporte decreciente antes de Cerner (no verificable).

### R5-19 · Cerner: ingresos 5.765 M$ (2021) y múltiplo 4,9x ventas (c5)
- **Fuentes:** el 5.765 sale de companyfacts de Cerner (CIK 804753), no en corpus. Segunda vía propia desde Oracle: companyfacts `BusinessAcquisitionsProFormaRevenue` FY22 (10-K FY23, 2023-06-20) 48.218 vs ingresos reales FY22 42.440 → diferencia **5.778 M$**; y FY23 pro forma 50.065 vs real 49.954 → 111 M$ de las 7 primeras jornadas (anualizado ≈ 5.790). Caja neta pagada FY23 (`PaymentsToAcquireBusinessesNetOfCashAcquired`, 10-K FY23/24/25) **27.721 M$**. Múltiplos propios: 28,2/5,778 = 4,88x; 28,2/5,765 = 4,89x; caja neta/5,778 = 4,80x.
- **Veredicto: CONFIRMADO** (ingreso ≈ 5,8 B por vía independiente; múltiplo 4,8–4,9x).
- **Implicación:** el 28,2 B exacto va en R5-20. El múltiplo es robusto al rango 4,8–4,9x. Un documento previo de la carpeta (`orcl_v3_2026-07-09.txt`) usa "28,3 B"; es coherente: 28,2 B en efectivo + 55 M$ de premios asumidos ≈ 28,26 B.

### R5-20 · Cerner: precio 28,2 B, goodwill 18,6 B, intangibles 12,0 B, pasivos netos 2,4 B, puente 15,7 B, deuda asumida 1,6 B, cierre 2022-06-08 (c5)
- **Fuentes:** primario verificado: `GoodwillAcquiredDuringPeriod` FY23 = **18.618 M$** (10-K FY23 y FY24); deuda de Cerner asumida **1.600 M$** a fecha 2022-06-08 (10-Q 2T/3T/1T FY23, `…NoncurrentLiabilitiesLongTermDebt`); goodwill 43.811 (FY22) → 62.261 (FY23) = +18.450. Aritmética: 18,6 + 12,0 − 2,4 = 28,2. No verificados: precio total 28,2 B en texto, 12,0 B de intangibles, 2,4 B de pasivos, puente de 15,7 B (notas de 10-K FY22/23/24, no locales).
- **Veredicto: DEGRADADO** (goodwill, deuda asumida y fecha CONFIRMADOS; el resto no reproducible).
- **Implicación:** ninguna refutación; la cuadratura 18,6+12,0−2,4 = 28,2 es coherente con el XBRL de caja pagada (27,7 B netos de caja adquirida). Para citarlo como HECHO hay que leer la Nota 2 del 10-K FY23/FY24.

### R5-21 · Fondo de comercio 62.261 M$ (FY26) y sin deterioro FY23–FY26 (c5)
- **Fuentes:** companyfacts `Goodwill`: 62.261 a 2026-05-31 (10-K FY26 y 10-Q 1T FY27), 62.207 (FY25), 62.230 (FY24), 62.261 (FY23); `GoodwillImpairmentLoss` = **0** en FY23, FY24, FY25 y FY26 (cada uno reportado por 2-3 10-K). 10-K FY26 Nota 2 políticas: "Our most recent goodwill impairment analysis was performed on March 1, 2026 and did not result in a goodwill impairment charge. We did not recognize impairment charges in fiscal 2025 or 2024." Tabla de goodwill por segmento FY26: Cloud and Software 57.114; Hardware 2.732; Services 2.415. (Único deterioro de goodwill en la serie: 186 M$ en FY15.)
- **Veredicto: CONFIRMADO.**
- **Implicación:** el hecho no sirve como prueba de que Cerner funcionó. (i) El goodwill se asigna a tres segmentos operativos; el de Cerner (18.618 = 29,9 % del total; 32,6 % del segmento Cloud and Software) está mezclado con ≈38,5 B de otros negocios, y el 10-K no declara unidades de reporte, ni margen entre valor razonable y libros, ni tasa de descuento de la prueba; (ii) la política permite una evaluación solo cualitativa ("optional assessment"), y el 10-K no dice si la prueba de marzo de 2026 fue cualitativa o cuantitativa. Ausencia de deterioro es consistente con "Cerner va bien" y con "Cerner va mal pero queda cubierta por el crecimiento de OCI en la misma unidad". No refuta ni confirma la hipótesis de sobrepago.

### R5-22 · Aportación de Cerner a Oracle en FY23: 5,9 B$ (2,2 B servicios; 0,14 B hardware) (c5)
- **Fuentes:** 10-K FY23 Item 7, no local. Coherencia con el pro forma propio (R5-19: ≈5,8 B anualizado antes del cierre).
- **Veredicto: DEGRADADO.**
- **Implicación:** el orden de magnitud es plausible; la cifra exacta y su desglose no están verificados. Es la base de la afirmación "ingreso FY23 ≈ +2 % vs 2021".

### R5-23 · Servicios −198 M$ (FY25) y +510 M$ (FY26) (c5)
- **Fuentes:** 10-K FY25 Item 7: "Total services revenues decreased by $198 million… was due to a decrease in revenues in each of our primary services offerings". 10-K FY26 Item 7: "Total services revenues increased by $510 million… primarily due to increases in our consulting services revenues".
- **Veredicto: CONFIRMADO** (cifras y citas).
- **Implicación:** estas dos cifras están en la tabla de Cerner del lector pero son los **servicios totales** de Oracle; el filing atribuye el aumento FY26 a consultoría, no a Oracle Health. No son evidencia sobre Cerner.

### R5-24 · Guía de Oracle Health a doble dígito en FY27; Oracle Health no desglosado (c5)
- **Fuentes:** 8-K 2026-06-10 (Ellison/Magouyrk): "We expect this new AI patient care management system to push the growth rate of the overall Oracle Health business to double-digits in fiscal year 2027". 10-K FY26: "Oracle Health" aparece solo como línea de producto (Item 1) y fundación; no hay ingreso de Oracle Health en MD&A ni en Nota de segmentos. 10-Q 1T FY27: sin mención.
- **Veredicto: CONFIRMADO.**
- **Implicación:** la guía "doble dígito" es una expectativa cualitativa sin base numérica; implica que hoy Oracle Health crece menos de dos dígitos, sin cifra. Laguna 2 del lector confirmada: no hay forma primaria de medir el retorno de los 28 B.

### R5-25 · Incidentes de ciberseguridad: "have not had a material impact" (FY25, FY26) (c5)
- **Fuentes:** 10-K FY25 Item 1C (L2558): "During fiscal 2025, Oracle experienced cybersecurity incidents that, to date, have not had a material impact"; 10-K FY26 Item 1C (L2714): ídem para fiscal 2026.
- **Veredicto: CONFIRMADO.**
- **Implicación:** el filing no nombra el incidente de Oracle Health; ver R5-26.

### R5-26 · Brecha Oracle Health 2025 (servidores legados Cerner, demanda colectiva, ~20 M de personas), VA (10 B→16 B$, vencimiento 2028), cita de Catz "−1 a −2 puntos" (c5)
- **Fuentes:** solo prensa (Becker's, Fierce, BankInfoSecurity, Nextgov); ningún filing local lo nombra. El 10-K FY26 no menciona la demanda colectiva ni el contrato de VA.
- **Veredicto: DEGRADADO.**
- **Implicación:** no usar en el juicio de foso como HECHO. La cita de Catz (dic-2024, 2T FY25) debería buscarse en transcripción oficial; no está en el corpus.

### R5-27 · SAP: S/4HANA solo sobre HANA; Business Suite 7 (AnyDB, incluida Oracle) con mantenimiento principal hasta fin de 2027 y extendido hasta 2030 (+2 pp); "las instancias Oracle bajo SAP salen de soporte" (c2, e)
- **Fuentes:** ningún filing de Oracle en el corpus trata esta fecha ni cuantifica instancias de Oracle DB bajo SAP. Una búsqueda web (SECUNDARIO) devuelve páginas de prensa/analistas y el newsroom de SAP con las fechas 2027 y 2030; no encontré el texto del 20-F de SAP. Sin acceso a EDGAR.
- **Veredicto: DEGRADADO** (solo prensa/anuncios de empresa; ninguna fuente primaria de filings).
- **Implicación:** además de la falta de primaria, la frase "las instancias Oracle bajo SAP salen de soporte" es un salto lógico: el fin de mantenimiento de Business Suite 7 afecta a la **aplicación de SAP**, no al soporte de la base de datos de Oracle, que es contrato aparte (con Oracle o vía licencia de ejecución de SAP). El mecanismo correcto es otro: al migrar a S/4HANA el cliente **abandona** la licencia y el soporte de Oracle DB. El tamaño de la base expuesta es laguna sin dato (laguna 4 del lector, confirmada). La fecha 2027/2030 debe llevar etiqueta SECUNDARIO en la tesis.

### R5-28 · Ausencias en los 10-K: ni "HANA", "Postgres" ni "Rimini" en FY25/FY26; SAP como competidor; "open source alternatives" como factor de riesgo; Oracle ofrece MySQL HeatWave (a20, c2, c3)
- **Fuentes:** búsqueda de cadenas sobre 10-K FY25 y FY26: 0 coincidencias de HANA, Postgres, Rimini; "SAP SE" en la lista de competidores; Item 1A: "the adoption of open source alternatives to commercial software by enterprise software customers"; "open source" también aparece en 1A como riesgo de código de terceros. PeopleSoft/JDE/Siebel aparecen solo como productos.
- **Veredicto: CONFIRMADO** (FY25 y FY26).
- **Implicación:** la afirmación ampliada "HANA 0 menciones en 10-K FY11–FY26" no es verificable (los demás 10-K no están en el corpus): DEGRADADA. Oracle no cita ninguna base de datos concreta como amenaza, solo una categoría genérica.

### R5-29 · Cuotas y tamaño del mercado de bases de datos: Gartner 2023 (103,2 B, Oracle +4,5 % vs mercado +13 %), 2024 (119,7 B), DB-Engines (Oracle #1, 1.122 pts; PostgreSQL #4), Stack Overflow 2025 (PostgreSQL 55,6 %) (c3)
- **Fuentes:** ningún filing local contiene cuota de mercado, ranking ni cifra de Gartner/IDC/DB-Engines (búsqueda de `market share | Gartner | IDC | DB-Engines | database market` sobre los documentos locales: sin coincidencia relevante; únicas coincidencias son boilerplate de compensación). El único posicionamiento del propio 10-K FY26 es una autodescripción: "Oracle AI Database is the world's most popular enterprise database". db-engines.com no alcanzable.
- **Veredicto: DEGRADADO** (todo SECUNDARIO, sin primaria).
- **Implicación:** el lector lo etiquetó SECUNDARIO. Lo elevo a regla: **ninguna cifra de cuota de mercado de bases de datos puede entrar en la tesis como HECHO**. La frase "crece muy por debajo del mercado DBMS" no tiene soporte primario; el 10-K FY26 no la cuantifica ni la niega.

### R5-30 · Crecimiento del "multicloud database revenue": +1.529 % (1T FY26), +531 % (3T FY26), +404 % (4T FY26); base en dólares no revelada (a18)
- **Fuentes:** 8-K 2025-09-09: "MultiCloud database revenue from Amazon, Google and Microsoft grew at the incredible rate of 1,529% in Q1"; 8-K 2026-03-10: "Multicloud Database Revenue up 531% in USD"; 8-K 2026-06-10: "The Oracle Multicloud AI Database grew 404% in Q4—making it our fastest growing business ever". Ningún importe en dólares en ningún 8-K/10-K/10-Q.
- **Veredicto: CONFIRMADO.**
- **Implicación:** omisión del lector relevante: la métrica **no se reportó en el 8-K de 2T FY26 (2025-12-10) ni en el de 1T FY27 (2026-09-10)**, ni aparece en el 10-Q 1T FY27 (búsqueda "multicloud": sin cifra). Tres trimestres de cinco. La aceleración/deceleración (1.529 → 531 → 404) es sobre una base que crece, y el último trimestre disponible no la repite. No usarla como evidencia de tracción absoluta.

### R5-31 · Fechas GA de Database@Azure (2023-12-13), @Google (2024-09-09), @AWS (2025-07-08) (a19)
- **Fuentes:** notas de prensa de oracle.com según el lector; ningún filing local las fecha. 
- **Veredicto: DEGRADADO.**
- **Implicación:** el 10-K FY26 sí describe las ofertas multicloud (R5-32), no las fechas.

### R5-32 · Citas del 10-K FY26 sobre portabilidad, multicloud como riesgo, Autonomous y Exadata (a11-a14)
- **Fuentes:** 10-K FY26 Item 1: "Oracle's Multicloud Database offerings… run Oracle AI Database services, Oracle Autonomous AI Database and Oracle Zero Data Loss Autonomous Recovery Service within other hyperscale cloud IT environments"; "connectable among differing deployment models to enable interoperability and extensibility to easily move workloads among the Oracle Cloud, multicloud and other IT environments"; Autonomous AI Database "consumption-based pricing… lower costs by paying only for resources used"; "Oracle Exadata Database Machine… optimized for Oracle AI Database to achieve higher performance, scalability and availability at a lower cost". Item 1A: "OCI's multicloud services work with a number of our competitors' products, including Micro…" y que esa estrategia "could lead our customers to migrate away from our cloud offerings".
- **Veredicto: CONFIRMADO.**
- **Implicación:** son afirmaciones de diseño y marketing de la empresa, no evidencia de ventaja medida (p. ej. "lower cost" no tiene cifra).

### R5-33 · Riesgos 1A y datos de contexto del foso: precio del soporte, concentración OCI, arrendamientos, RPO 638 B, 87 % del crecimiento desde Américas, 11,9 M ft² subarrendados (d, e, f)
- **Fuentes:** 10-K FY26 Item 1A: "Our software support fees… are generally priced as a percentage of our net software license fees… Our competitors may offer lower pricing on their support offerings, which could put pressure on us to further discount our offerings"; "we could be locked into multi-year commitments for excess data center space and related capital expenditures, as well as associated financings, without receiving corresponding revenue"; "the terms, renewal options and pricing adjustments in our long-term data center leases typically do not align with the duration and pricing of customer contracts". MD&A: "The Americas, the EMEA and the Asia Pacific regions contributed 87%, 6% and 7%… to the constant currency revenue growth for this business". Companyfacts `RevenueRemainingPerformanceObligation`: **638.000 M$** (2026-05-31, 10-K FY26), 664.000 (2026-08-31, 10-Q).
- **Veredicto: CONFIRMADO.**
- **Implicación:** el pasaje "In certain OCI offerings, we are more concentrated among a number of large customers" que el lector cita en d no lo localicé con la cadena "more concentrated" (0 coincidencias en 10-K FY26); la sustancia de la concentración está en 1A pero la cita literal debe revisarse. 

### R5-34 · Casos públicos de salida (Amazon ~7.500 BD/75 PB, Alibaba, Salesforce), Rimini, precios de lista y uplift del soporte, Java por empleado (b, d)
- **Fuentes:** AWS News Blog, 36Kr, Fortune, The Register, consultoras de licenciamiento; ningún filing local los trata. 
- **Veredicto: DEGRADADO** (todo SECUNDARIO).
- **Implicación:** el lector lo etiquetó SECUNDARIO y lo declaró. Se confirma que la cuantificación del coste de cambio no existe en primaria (nota de método del lector) y que "Amazon tardó varios años y dejó apps de terceros sin migrar" es una cita de un blog del cliente que se va, no un dato de Oracle. El "peaje" de 22 % de soporte y el uplift 3–8 % no están en los filings: solo "% of net license fees" (R5-01).

### R5-35 · Recuentos de clientes: Fusion ERP ~5.500 y NetSuite >15.000 (8-K 2018-09-17); NetSuite >43.000 y Fusion ~8.200 (2026) (a16, a17)
- **Fuentes:** el 8-K de 2018 no está en el corpus (no alcanzable); las cifras de 2026 son prensa. Ningún 8-K/10-K/10-Q de 2025-26 da número de clientes de Fusion o NetSuite (búsqueda local).
- **Veredicto: DEGRADADO.**
- **Implicación:** la afirmación a15 (el 10-K no da número de clientes de Fusion/NetSuite) sí es cierta en el corpus; el foso de aplicaciones carece de métrica primaria vigente.

### R5-36 · Aritmética derivada del lector: soporte/ingresos totales FY11 41,5 %, FY14 47,6 %, FY16 50,9 %, FY17 51,0 %, FY21 48,9 %, FY23 38,9 %, FY26 29,4 %; cloud 33.989; hardware 3.084 = 5 % (a7, a8)
- **Fuentes:** recálculo propio con companyfacts y 10-K: 14.796/35.622 = 41,5 %; 18.206/38.275 = 47,6 %; 18.861/37.047 = 50,9 %; 19.229/37.728 = 51,0 %; 19.779/40.479 = 48,9 %; 19.426/49.954 = 38,9 %; 19.804/67.357 = 29,4 %; hardware 3.084/67.357 = 4,6 % (el 10-K redondea "5 %").
- **Veredicto: CONFIRMADO** (aritmética; FY21 depende de 19.779, no verificado, ver R5-18).
- **Implicación:** la caída del peso del soporte (51 % → 29 %) refleja sobre todo el crecimiento de cloud, no un soporte menguante (el soporte nominal creció +3,0 % entre FY17 y FY26).

---

## Hallazgos extra (errores de etiqueta, aritmética, omisiones)

1. **Rupturas de base en las series de licencias y totales (el lector no las declara).** `LicensesRevenue` FY11 es 9.235 en el 10-K FY12 pero 8.980 en el 10-K FY13; FY12 es 9.906 y luego 9.451. La tabla c4 mezcla ambas: la fila FY12→FY13 (9.906→9.411) parece −5,0 %, cuando en base homogénea (9.451→9.411) es −0,4 %. Igual con ASC 606: total FY17 37.728 vs 37.792 reexpresado; FY18 39.831 vs 39.383; el lector coloca FY18 = 39.831 junto a FY19 = 39.506. Corregir en c4: usar una sola base por tramo.
2. **Contaminación de Cerner en soporte/licencias desde FY23.** El lector sitúa 3,6 B de Cerner en categorías de cloud/licencia/soporte (5,9 − 2,2 − 0,14) pero no avisa de que la serie de soporte FY23→FY26 no es orgánica. El soporte orgánico de Oracle puede estar cayendo más de lo que muestra −1 % cc. Pedir al lector el desglose del 10-K FY23 (Item 7) para acotar.
3. **Atribución de la caída por la propia empresa.** El 8-K 2026-09-10 dice que el descenso del software "refleja la migración continua de software on-premises a la nube". El lector argumenta (c3) que "Oracle no atribuye la caída de licencias a open source" citando 9–10; es cierto y debería citar este 8-K. Sin embargo la atribución es un enunciado de gestión, no una medición.
4. **Métrica multicloud intermitente** (R5-30): reportada 3 de 5 trimestres.
5. **Salto lógico en el calendario SAP** (R5-27): la fecha 2027/2030 describe el mantenimiento de la aplicación SAP, no el soporte de Oracle DB.
6. **Anomalía en "% del margen total"** (R5-03): no cuadra con la conciliación a resultado operativo.
7. **Test de deterioro** (R5-21): no discrimina Cerner dentro de un segmento de 57 B de goodwill.
8. **Laguna 9 probablemente falsa** (R5-16): el acuerdo SEC de 1993 parece estar en filings de Oracle de 1994; el lector debe reabrirlo.
9. **Cita no localizada** (R5-33): "In certain OCI offerings, we are more concentrated among a number of large customers" no aparece literalmente en el 10-K FY26 local (cadena "more concentrated": 0 coincidencias).
10. **Rotulación del 5,4 B** (R5-08): el mandato lo llama "canibalización de soporte"; el filing lo describe como ingreso cloud anualizado ganado, sin dato del soporte dado de baja.
11. **Pequeñas discrepancias numéricas:** soporte FY17 19.229 (XBRL) vs 19.230 (lector); hardware 4,6 % vs "5 %" (redondeo del 10-K).

## Resumen para el juicio de foso (Paso 3), sin score ni veredicto de compra

- **Confirmado en primaria:** el contrato de soporte (renovación "substantially all", % de licencia, prepago); soporte estable en 19,4–19,8 B (FY23–FY26) y −1 % cc en los dos últimos trimestres; licencias −9 % (FY26) y −15 % (1T FY27); 5,4 B de ingreso cloud anualizado procedente de la base de soporte; margen cloud & software 63 %→59 %; goodwill sin deterioro; Cerner a 4,8–4,9x ventas.
- **No confirmado (DEGRADADO):** márgenes del soporte 86–91 %, todo el relato 1990-91 en cifras, la serie FY18–FY22, el calendario SAP, cualquier cuota de mercado de bases de datos, casos de salida y precios de lista.
- **Refutado:** "doce años encogiéndose" (la mitad del recorte de licencias ocurrió en FY14–FY17).

## Archivos del verificador
- `/tmp/claude-0/-home-user-inversiones/f725650c-7737-5af8-a093-7033a43429ae/scratchpad/v5/verif_r5.py` — reproducción de toda la aritmética citada arriba.
- `/tmp/claude-0/-home-user-inversiones/f725650c-7737-5af8-a093-7033a43429ae/scratchpad/v5/dump.py` — volcado de etiquetas de companyfacts con accession y fecha de presentación.
