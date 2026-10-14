# Fase 3 — Metodo completo (12 pasos, Candados A y B reales) sobre las 25 finalistas (2026-09-07)

**Resultado central: 0 de 25 llego a COMPRAR_PROPUESTO.**

**Actualizacion 2026-09-07 (segunda pasada):** se resolvieron los 2 pendientes de dato especifico. RELX era un error de campo del agente (el cuerpo del expediente ya decia NO_COMPRAR_TODAVIA) -- corregido sin investigacion nueva. ADYEN.AS SI tenia un dato real pendiente (la cifra de caja libre EUR 4,9bn vs 12,4bn) -- se investigo con 3 agentes (segunda fuente primaria + verificador + tercera fuente de mercado), la cifra de EUR 4,9bn subio de NO_VERIFICABLE a HECHO, el escenario "barato" (12,4bn) quedo descartado por error de categoria contable, y el veredicto subio a NO_COMPRAR_TODAVIA. Detalle completo anexado al final de `Fase3_Tesis_Completas/ADYEN.AS_tesis_completa.md`.

| Veredicto | Cuenta |
|---|---|
| NO_COMPRAR_TODAVIA (calidad solida, precio no lo permite hoy) | 24 |
| NO (abogado-diablo: mecanismo del moat/reinversion roto, y precio ya sobre el escenario bajista) | 1 -- **NVDA** |
| COMPRAR_PROPUESTO | 0 |
| NO_DECIDIBLE | 0 -- ya no quedan pendientes de dato especifico |

## El hallazgo de fondo: el WACC rapido de Fase 1/2 no era confiable

En las 25, el WACC bottom-up real (Candado B: beta citada con fuente y fecha, costo de deuda real, prima pais) resulto DISTINTO -- casi siempre mas alto -- que la aproximacion rapida 7-9% usada para llegar hasta el universo de 60/25. Ejemplos: Adyen 11,8% real vs 7-9% aproximado; Keyence 8,7% real (con ajuste explicito por sesgo de beta-baja-en-maximos) vs 7-9%. Esto confirma exactamente por que el Candado B existe -- comprar con el WACC rapido habria significado un margen de error real y sistematico, casi siempre a favor de pagar de mas.

## NVDA: unico veredicto NO (no solo 'todavia no')

El abogado-diablo, en sesion limpia, devolvio RECHAZA_MECANISMO_CENTRAL -- no una simple objecion de precio. Dos de sus objeciones atacan directamente el mecanismo del moat (el testigo de CUDA como barrera tiene 5-7 anos y no se reconfirmo contra la migracion activa a ASIC propio de Google/Amazon/Meta; NVLink Fusion es tan legible como concesion defensiva como refuerzo del moat) y una desmonta el motor de reinversion (los ~463.000M USD en compromisos fuera de balance mezclan COGS futuro obligatorio con capital de crecimiento real -- error de categoria). Ademas el precio de hoy (229,49) ya esta POR ENCIMA del escenario bajista propio (126,20) -- sin margen de seguridad en absoluto. Bajo el marco: un negocio extraordinario carisimo es 'no comprar todavia'; aqui el candado objeta el mecanismo mismo, no solo el precio -- eso es la definicion de NO. Ningun knock-out binario disparo (esto no es un STOP mecanico) y la calidad cruda (ROIC 55-80%, margen 71-75%) sigue siendo real -- pero el mecanismo que la sostiene no se defendio.

Nota de proceso: NVDA es la unica de las 25 marcada NO en vez de NO_COMPRAR_TODAVIA -- por diseño del metodo, NO es 'final, sin apelacion' cuando proviene de knock-out o moat roto. Sigue pendiente el sello personal de Felipe en los Pasos 1/6/7 antes de que sea un veredicto real, pero la objecion de mecanismo (no solo de precio) es lo que la separa claramente del resto.

## Los 2 NO_DECIDIBLE

**ADYEN.AS** y **RELX** -- el abogado-diablo encontro una pieza especifica del WACC o del motor de reinversion que no se pudo cerrar con los datos disponibles en este pase. Ver el archivo de cada una para el dato exacto que falta.

## Las 24 NO_COMPRAR_TODAVIA

| Ticker | Empresa | Abogado-diablo | WACC bottom-up (resumen) |
|---|---|---|---|
| ADYEN.AS | Adyen N.V. | OBJECIONES_SIN_RESOLVER | Actualizado 2026-09-07: asimetria de la caja resuelta ~1,06:1, desfavorable — ver `Fase3_Tesis_Completas/ADYEN.AS_tesis_completa.md` |
| RELX | RELX Group | OBJECIONES_SIN_RESOLVER | WACC 7,6% bottom-up (campo corregido — el cuerpo del expediente siempre dijo esto) |
| 7974.T | Nintendo Co., Ltd. | OBJECIONES_SIN_RESOLVER | FÓRMULA: WACC = (E/V)×Ke + (D/V)×Kd×(1-T)... |
| ADP | Automatic Data Processing | OBJECIONES_SIN_RESOLVER | **Veredicto de la casilla WACC: 7,9%–8,3%, punto central ≈8,0% — botto... |
| VEEV | Veeva Systems | OBJECIONES_SIN_RESOLVER | **Ke = Rf + β×ERP + prima_país = 4,79% + (0,97 × 4,46%) + 0% = 4,79% +... |
| CFR.SW | Compagnie Financiere Richemont | OBJECIONES_SIN_RESOLVER | ... |
| 6861.T | Keyence | OBJECIONES_SIN_RESOLVER | VEREDICTO: WACC final = 8,7% (rango defendible 8,1%–9,1%; el cálculo n... |
| ASML | ASML Holding | OBJECIONES_SIN_RESOLVER | **WACC = 9,1%** (9,12% exacto), bottom-up de mercado, sin heredar ning... |
| TSM | TSMC | OBJECIONES_SIN_RESOLVER | VEREDICTO: WACC bottom-up = 11,4% central (rango honesto 10,7%-11,9%) ... |
| 6146.T | Disco Corporation | OBJECIONES_SIN_RESOLVER | WACC = 8,12% ≈ 8,1%, construido 100% bottom-up de mercado, sin heredar... |
| LRCX | Lam Research | OBJECIONES_SIN_RESOLVER | WACC = 13,9% (primario), rango de sensibilidad 11,6%-13,9% según fuent... |
| RMS.PA | Hermès | OBJECIONES_SIN_RESOLVER | WACC final = 7,8% central, banda defendible 7,2%–8,3% (NO un punto úni... |
| KLAC | KLA Corporation | OBJECIONES_SIN_RESOLVER | **WACC final: 11,3%** (rango de sensibilidad razonable 10,7%-11,9% seg... |
| COST | Costco | OBJECIONES_SIN_RESOLVER | VEREDICTO: WACC bottom-up = 8,3% (banda defendible 8,0%-8,6%), reconst... |
| RACE | Ferrari | OBJECIONES_SIN_RESOLVER | VEREDICTO DEL WACC: 7,6% (EUR, bottom-up, reconstruido desde cero — NO... |
| VRTX | Vertex Pharmaceuticals | RECHAZA_MECANISMO_CENTRAL | VEREDICTO: WACC = 9,3% (rango defendible 9,2%-9,4%; la sensibilidad al... |
| CDNS | Cadence Design | RECHAZA_MECANISMO_CENTRAL | WACC final = 10,0% (rango de sensibilidad 9,8%-10,3% según beta emplea... |
| 6920.T | Lasertec | OBJECIONES_SIN_RESOLVER | VEREDICTO: el WACC bottom-up da ~9,2% central (rango defendible 8,2%-1... |
| ASM.AS | ASM International | OBJECIONES_SIN_RESOLVER | VEREDICTO: WACC = 10,25% (= Costo de Equity puro; peso de deuda = 0%).... |
| MSFT | Microsoft | OBJECIONES_SIN_RESOLVER | WACC = We×Ke + Wd×Kd×(1-t), CONSTRUIDO DE CERO, sin heredar nada de ti... |
| LIN | Linde plc | OBJECIONES_SIN_RESOLVER | WACC final = 8,5% (rango defendible 8,0%-8,6%), CANDADO B cumplido — r... |
| PME.AX | Pro Medicus | OBJECIONES_SIN_RESOLVER | WACC = Ke (D/V=0, deuda cero verificada triple en Informe Anual FY2026... |
| MCO | Moody's | OBJECIONES_SIN_RESOLVER | VEREDICTO: WACC = 9,96% (~10,0%) — bottom-up, de mercado, ninguna cifr... |
| IDXX | IDEXX Labs | OBJECIONES_SIN_RESOLVER | WACC = [E/(D+E)]×Ke + [D/(D+E)]×Kd×(1-t)... |

De estas, **VRTX y CDNS** tuvieron abogado-diablo = RECHAZA_MECANISMO_CENTRAL (como NVDA) pero el sintetizador las mantuvo en NO_COMPRAR_TODAVIA en vez de NO -- en ambos casos porque la objecion del abogado fue sobre un dato puntual sin cerrar (ROIIC marginal irresoluble, mezcla de periodos en la prueba de resiliencia), no una prueba empirica de que el moat esta roto. Vale la pena que revises esos dos casos con mas atencion que el resto -- estan en la frontera entre 'todavia no' y 'no'.

## Archivos

- `Fase3_Tesis_Completas/<TICKER>_tesis_completa.md` -- expediente completo de las 25 (Pasos 0-12), con las objeciones literales del abogado-diablo y el borrador de diario.
- `11_Fase3_Veredictos_25.csv` -- resumen tabular de las 25.

## Pendiente de Felipe (las 25)

Los Pasos 1 (circulo de competencia), 6 (gestion e incentivos) y 7 (percepcion variante) no los puede firmar un agente. Cada archivo trae su 'pendiente_de_felipe' especifico. Ninguna de las 25 es una compra real hasta ese sello.

## Estado del proyecto completo

480 empresas -> 60 (Fase 1, sourcing) -> 25 (Fase 2, pase ligero) -> 25 con metodo completo (Fase 3, mas la resolucion del dato pendiente de Adyen) -> **0 compras**. No quedan pendientes de dato especifico y fechable en ninguna de las 25 -- lo unico que falta en cada una es el sello personal de Felipe (Pasos 1, 6, 7 y 11). El universo queda documentado para revisitar cuando el precio se mueva.
