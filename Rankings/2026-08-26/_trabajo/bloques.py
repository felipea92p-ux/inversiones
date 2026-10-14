#!/usr/bin/env python3
"""Construccion de los 36 en 3 bloques. SIN SCORES.
La calidad es PUERTA (define bloque y margen exigido); el precio es ORDEN dentro del bloque."""
import json, csv
D={o['ticker']:o for o in json.load(open('Rankings/2026-08-26/_trabajo/pasada1_v3.json'))}
DCF={o['ticker']:o for o in json.load(open('Rankings/2026-08-26/_trabajo/dcf_inv.json'))}
M={r['ticker']:r for r in csv.DictReader(open('Rankings/2026-08-26/_trabajo/maestra.csv',encoding='utf-8'))}
R=0.0970

# ---- VECTORES ABIERTOS, con su fecha y su fuente. Salidos del arbitraje contra filing del 26-ago.
VECTOR={
 'V':    ('DOJ antitrust contra el monopolio de red en debito, demanda sept-2024, EN DISCOVERY desde 2026. Provision por litigios 2.562 M$ en FY25 contra 462 M$ en FY24.','RELOJ ARRANCADO'),
 'GOOGL':('Primer ataque estructural al buscador en veinte anios; la cuota de information discovery ya cae.','RELOJ ARRANCADO'),
 'MSCI':('8-K 28-ene-2026 (acc. 0001408198-26-000008): licencia BlackRock extendida a 2035 con tarifa ligada al TER. Basis point fee 2,44 -> 2,28 en cuatro trimestres, aceleracion x5. Segundo tramo el 1-ene-2027 SIN CUANTIFICAR (Exhibit 10.1 redactado). BlackRock 9,8% -> 11,8% del ingreso.','GRIETA MEDIDA'),
 'NVDA': ('8-K 17-ago-2026 (acc. 0001045810-26-000069): garantias de valor residual con SB Energy, inquilino filial de OpenAI, tope acumulado 105.000 M$. Seis meses antes el 10-K decia "no hemos suscrito ningun acuerdo de financiacion". FUENTE UNICA: el 10-Q que lo corroboraria aun no existe. Ademas top-3 clientes 54% del revenue (10-Q Q1 FY27).','GRIETA MEDIDA - DEGRADADA por fuente unica'),
 'VEEV': ('Fin del acuerdo de distribucion con Salesforce (sept-2025); AstraZeneca y Novartis ya migradas a Salesforce Life Sciences Cloud (marzo-2026).','GRIETA MEDIDA'),
 'ISRG': ('Medtronic Hugo despejada por FDA el 3-dic-2025 (K250725) pero SOLO PARA UROLOGIA; J&J Ottava De Novo el 21-jul-2026 (DEN250068) solo abdomen superior, y J&J no lo ha declarado en NINGUN filing SEC. Crecimiento de procedimientos EE.UU. 16% (Q3 25) -> 14% (Q1 26) -> 12% (Q2 26).','RELOJ ARRANCADO - amenaza MENOR de lo que decia el archivo'),
 'MSFT': ('Gate propio roto el 29-jul-2026: owner earnings FY2026 54.582 M contra umbral 55.000. Capex +79,6% (64.551 -> 115.948 M). FCF -3,3% interanual, primera caida en anios.','GRIETA MEDIDA'),
 'TSM':  ('Riesgo de jurisdiccion unica (R6, al VALOR no a la tasa). Top-2 clientes ~36% y deteriorandose. Capex 52-56.000 M$ para 2026.','RIESGO DE COLA'),
 'AAPL': ('Dos rentas bajo riesgo regulatorio: el pago de Google por buscador por defecto y la comision de la App Store.','RELOJ ARRANCADO'),
 'ASML': ('China 33% de ventas en 2025 bajo controles de exportacion cambiantes; TSMC via Taiwan 30-45%.','RIESGO DE COLA'),
 'MA':   ('Rieles A2A, pagos en tiempo real y stablecoins. SIN observable de arranque fechado — esa es la diferencia con Visa.','VECTOR SIN RELOJ'),
 'AMZN': ('Owner earnings NEGATIVOS (-11.800 M) por capex de IA de 131.800 M. La formula FCF-SBC con capex TOTAL no separa mantenimiento de crecimiento: DEFINICION ROTA, no veredicto.','DATO DEGRADADO'),
 'MELI': ('Owner earnings declarados corruptos por factor 5,4x-11,4x en el propio archivo (el CFO incluye el flotante del libro de credito). Margen operativo 12,7% -> 11,1% -> 6,9%.','DATO DEGRADADO'),
 'SPGI': ('Goodwill 60% del activo por la megafusion IHS Markit: el denominador no permite decidir. ROIC medido 9,2%.','NO DECIDIBLE'),
 'CSU.TO':('Sucesion (Leonard dejo la presidencia oct-2025) y crecimiento organico ~4%: el motor es comprado, no propio.','VECTOR SIN RELOJ'),
 'CME':  ('ROIC 9,56% falla el knock-out por 14 pb, dentro del error de medicion. FMX/DTCC atacan el netting.','AL FILO'),
 'ZTS':  ('Precio DESAPARECIO del puente de crecimiento en 2T-26; dermatologia -15,9%; guia FY26 recortada de +2/+5% a -3/-1% en dos tandas. Elanco Pet Health +12% y Merck Companion Animal +7% el mismo trimestre.','MECANISMO ROTO'),
 'NOW':  ('10-Q 23-jul-2026: margen operativo Q2 4,1% contra 11,1%; ~11.000 M$ de M&A en 8 meses (Armis 7.600, Veeza 1.200, Moveworks 2.407); deuda 1.491 -> 7.517 M$. Socio federal 13% del ingreso.','GRIETA MEDIDA'),
 'INTU': ('Gate resuelto 25-ago-2026: 2 de 5 pruebas fallan (unidades TurboTax -2%; guia FY27 +8,54% contra umbral 9,0%). Posicion ya cerrada por Felipe.','GATE DISPARADO'),
 'AVGO': ('Un distribuidor = 42% del revenue (10-Q Q2 FY26) contra 29% el anio anterior. VMware no se reporta por separado: la tesis precio-vs-unidades NO ES FALSABLE con filings.','GRIETA MEDIDA'),
 'IDXX': ('Gasto discrecional de duenos de mascotas; visitas same-store ~-2%.','VECTOR SIN RELOJ'),
 'REL.L':('Reinversion neta 15-18% del NOPAT a ROIC 15,4% implica g de 2,3-2,8%, contra el 7% subyacente que promete la narrativa.','TECHO ESTRUCTURAL'),
 'RMS.PA':('Ninguno. 7 de 8 jueces la ponen primera con sigma 0,35, el mayor acuerdo del ejercicio. Correccion del 26-ago: capex 7,26% de ventas (NO 9-10%) y el "6-7% de crecimiento de capacidad" NO EXISTE en fuente primaria.','SIN VECTOR'),
 'CDNS': ('Duopolio EDA. Falta la cicatriz nombrada de 2008-09 que exige la puerta G4.','VECTOR SIN RELOJ'),
 'MANH': ('SBC ~10% de ventas y creciente; internacional ~23%; transicion de CEO fundador feb-2025.','VECTOR SIN RELOJ'),
 'BKNG': ('Capital empleado NEGATIVO: el compounding por accion lo fabrica la recompra sobre patrimonio negativo. Desintermediacion por agregadores de IA.','ALTERNA + VECTOR'),
 'TYL':  ('ROIC 10,8%, apenas por encima de r. ~95% de ingresos en EE.UU.','MARGEN ESTRECHO'),
 'VRSK': ('TAM ya penetrado, organico ~7%, 83% de ingresos en EE.UU. Maquina de caja, no reinvertidora.','TECHO ESTRUCTURAL'),
 'NFLX': ('Sin costes de cambio altos ni efecto red puro: la ventaja es escala de contenido que exige ~18.000 M$/anio de reinversion perpetua.','VECTOR SIN RELOJ'),
 'WST':  ('El destock de 2022-2024 comprimio el margen operativo ~700 pb sin que aumentara la capacidad competitiva. Un cliente = 15,8% de las ventas.','GRIETA MEDIDA'),
 '4684.T':('87% del activo es caja y valores: el capital invertido es negativo si se depura. Concentracion ~100% Japon, internacional <1%.','CAJA OCIOSA'),
 'DB1.DE':('Balance bancario (activo 297.156 contra patrimonio 11.829). Discrepancia interna SIN RESOLVER en el informe auditado: papel comercial 996 contra 100 M.','NO COMPARABLE'),
 'ADYEN.AS':('ROIC NO CALCULABLE: denominador negativo. Oscila entre -16,1% y +153,7% segun el criterio de caja.','NO RANKEABLE POR ROIC'),
 '6861.T':('ROIC 13,8% u 84,6% segun se depure o no 2,98 billones de yenes de cartera. Punto ciego abierto: intangibles x4,6 sin explicacion en el yuho auditado.','CRITERIO DECIDE'),
 'NEM.DE':('Goodwill 50,3% del activo. Crecimiento organico anual NO PUBLICADO pese a ser KPI de retribucion.','DATO AUSENTE'),
 'STMN.SW':('La M&A (Neodent/ClearCorrect) inflo goodwill y comprimio el ROCE reportado de 35% a ~17%.','GRIETA CONTABLE'),
 'DSG.TO':('Goodwill 54,1% del activo. Organico NO DISPONIBLE: cero apariciones de "organic" en el 40-F.','DATO AUSENTE'),
 'TOI.V':('ACCIONES REALES 129.841.819, no 83.338.874: hay 46,5M de Exchangeable Units. Todo multiplo publicado sobre 83,3M subestima la capitalizacion un 56%.','DATO MAL PUBLICADO'),
 'MC.PA':('Organico -1%; Moda y Marroquineria -5%.','CONTRACCION MEDIDA'),
 'MTD':  ('Crecimiento mid-single-digit, por debajo del doble digito; el motor es la recompra, no la reinversion.','TECHO ESTRUCTURAL'),
}
json.dump(VECTOR,open('Rankings/2026-08-26/_trabajo/vectores.json','w'),ensure_ascii=False,indent=1)
print('vectores documentados:',len(VECTOR))
