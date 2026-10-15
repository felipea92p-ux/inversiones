# ADENDA PROPUESTA a `gates.md` — ORCL (15-oct-2026)
**Estado: BORRADOR. NO está aplicada a `gates.md`; la aprueba o rechaza Felipe (como las adendas del 6-sep y 14-sep, que siguen pendientes). Se ajusta tras el Candado A.**
Origen: `Tesis/ORCL/2026-10-14_UltraTesis_ORCL_metodo12.md` (veredicto provisional) y `Tesis/ORCL/_trabajo_2026-10-14/wf1_informes/vigia.md` §6. Un solo token `[CADUCA: AAAA-MM-DD]` por línea viva, para que el candado de la fila 23 sea ejecutable por `grep`.

## A insertar en «C. GATES ACTIVOS»

### ORCL — primera tesis bajo el método nuevo (14-oct-2026), NO por precio (caso de compra archivado 12 meses)
**Posición viva (IBKR, 15-oct-2026):** 9 acc., coste medio 129,97, 0,86% del NAV (134.096,74 USD). Comprada el 14-oct-2026 18:58Z a 129,855, 4 h 22 min antes del sello del Paso 0, sin tesis y con el candado B4 cerrado (registro tardío: ver borrador de diario).
**Veredicto (provisional hasta el Candado A):** NO por precio. Test del hoy: NO. Valor ponderado 71–94 USD (NO DECIDIBLE como punto, σ ≈26); primer tramo 52–68; mínimo de cierre de 24 m 114,99 (24-jul-2026): la prueba de alcanzabilidad FALLA en toda la banda. Compra nueva 0% del NAV. Alternativa real: efectivo (7.718 USD, 5,76%) al 5,21%, o recortar MELI. `[CADUCA: 2027-10-14]`
**Archivo del caso de compra, no de la posición** (Acta B4, Cruce 5): no suspende este gate, el test del hoy, el trigger de drawdown ni la revisión de la posición viva.

**Gate de la posición (tres factores; SUPUESTO sin backtest; lectura en el 8-K/10-Q del 2T FY27, ≈10-dic-2026; se activa con cualquiera de sus condiciones):**
- **A. Contraparte y ejecución:** OCI trimestral <8,0 B **o** RPO a la baja secuencial sin atribución.
- **B. Anualidad:** soporte ≤−3% cc **o** ≤−1% cc por tercer trimestre sin cifra de migración a cloud.
- **C. Coste de capital:** emisión a 10 años ≥7,5% **o** rebaja de dos agencias **o** nuevo ATM/preferente ≥15.000 M antes de 31-may-2027.
**0–1 factores ⇒ mantener la vigilancia (0,86%), no añadir, revisar tras el 3T FY27. ≥2 factores ⇒ salir del lote en la primera sesión posterior (puerta 1: «motor apagado»).** `[CADUCA: 2026-12-10]`
**Falsador del caso bajista (tres de cuatro, con fecha):** OCI FY27 ≥36.000 M con margen ≥55% sostenido; FCF positivo en un trimestre de FY28 sin prepagos con componente financiero; rating estable o al alza y emisión a 10 años ≤UST + 150 pb; segundo y tercer cliente de IA nombrados en filing con ≥10% del RPO cada uno. Si ocurren: reabrir el expediente hacia arriba. `[CADUCA: 2028-06-30]`
**Predicciones P1–P5 para el 2T FY27:** OCI 8,3–9,3 B (<8,0 B activa M2); RPO ≥664 B; «net cash outlay» ≥15 B con FCF negativo; acciones ≥3.024 M sin ATM ≥15 B; soporte ≤−1% cc. Detalle en §13 de la tesis.
**Decisiones de Felipe pendientes (sin ellas la puerta 1 no es decidible):** ERP único (4,20% o 3,70%); β que define «motor apagado» (60 m o 36 m); convención SBC/FCF con FCF negativo; mantener o salir de las 9 acc.

### Trigger nuevo propuesto — concentración de la cadena de IA/capex y contraparte común (OpenAI)
Cadena ancha (TSM 8,5% + GOOGL 8,4% + AMZN 6,7% + MSFT 2,4% + ORCL 0,9%) = **26,9% del NAV** (IBKR 15-oct) frente al tope de 20% que la Recalibración v2 (fila 16) fijó para la cadena de contraparte de IA; lectura estricta de cadena OpenAI (MSFT + ORCL) 3,2%. NVDA ya no está en cartera. **El tope de concentración sigue sin escribirse: debe escribirse antes de cualquier tramo nuevo de ORCL o de cualquier otro nombre de esa cadena.** `[CADUCA: 2026-11-20]`

## Excepción al candado que muerde (Recalibración v2, fila 23) — formato obligatorio
*paso:* 12 · *candado:* fila 23 («mientras exista una caducidad vencida sin cerrar, la sesión no puede producir ningún veredicto nuevo ni abrir expediente nuevo») · *antes:* ningún veredicto nuevo con caducidades vencidas abiertas · *después:* veredicto ORCL emitido con las cinco todavía abiertas · *motivo:* decisión expresa de Felipe del 14-oct-2026 («Solo hazlo!», sellada en `declaraciones_felipe_2026-10-14.txt`). Cuarta tesis consecutiva emitida con el candado vencido (NVDA 13-oct, DUOL 13-oct, AXP 14-oct, ORCL 14-oct): el candado no ha mordido ni una vez desde el 21-ago.

## Las cinco caducidades vencidas, con su acción mínima de cierre (del vigía)
| Gate | Vencida desde | Acción mínima de cierre | Quién |
|---|---|---|---|
| DUOL (gate roto 5-ago) | 28-ago (47 d) | Aprobar por escrito el gate propuesto el 13-oct (renovación 2/2, `[CADUCA: 2026-11-04]`) o ejecutar el recorte | Felipe |
| MELI (orden del 24-ago: vender 4 acc.; 20,5% frente al tope de 15%) | ~31-ago (51 d) | Ejecutar las 4 acc. o anular la orden por escrito | Felipe |
| MSFT (gate roto 29-jul) | 29-jul (77 d) | Renovación escrita con fecha `[CADUCA: 2026-10-29]` (8-K 1T FY27 ≈28-oct); tesis nueva imposible antes por fila 22 | Felipe |
| FDS (Gate 1: comunicado del 30-sep) | 30-sep (14 d) | Leer el 8-K del 30-sep, registrar la lectura del Gate 1 y renovar (1/2) | Asistente + Felipe |
| Decisión abierta nº9 (candado de competencia biotech) | 30-sep (14 d) | Declarar si selló; si no, cerrar como «veto confirmado por no-sellado» | Felipe |

## Notas
- El calendario de lecturas, la fila 22 (sin veredicto en las 10 sesiones previas a un reporte: ventana desde ≈23/25-nov) y el pre-registro de P1–P5 están en la tesis §9 y §13.
- Esta adenda no cambia ningún parámetro del método. No toca la Frontera Dato/Juicio (C6) ni el test de alcanzabilidad.
