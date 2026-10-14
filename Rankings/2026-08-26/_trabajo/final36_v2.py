#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LOS 36 v2 — MECANISMO COMO PUERTA. Reconstruido el 26-ago tras el rechazo de Felipe
('moats gigantes, fosos mas duraderos') y los veredictos de los agentes de mecanismo.
La puerta es la taxonomia de durabilidad del juicio ciego (rho 0,969); el dinero solo veta
(knock-outs); el precio es columna informativa DEGRADADA (B4 cerrado, motor no discrimina)."""
import json, csv
D={o['ticker']:o for o in json.load(open('Rankings/2026-08-26/_trabajo/pasada1_v3.json'))}
DCF={o['ticker']:o for o in json.load(open('Rankings/2026-08-26/_trabajo/dcf_inv.json'))}

# nivel = taxonomia 1-7 del juicio ciego. bloque por mecanismo; dinero solo veta.
L=[
# --- BLOQUE 1: mecanismo 1-4 verificado, SIN reloj arrancado, knock-outs superados ---
(1,'RMS.PA','Hermès International',1,'Escasez de fabricación propia: el exceso de demanda se convierte en lista de espera y precio, nunca en descuento','SIN VECTOR. 7/8 jueces primera, σ=0,35, el mayor acuerdo del ejercicio. Corrección 26-ago: capex 7,26% (no 9-10%); el «6-7% de capacidad» no existe en el URD','ROIC 52,0% (55,8% ex-sobretasa) · URD 2025 auditado PwC/GT'),
(1,'MA','Mastercard',2,'Red de coordinación de dos lados: para irse hay que mover comercios y bancos emisores a la vez','VECTOR SIN RELOJ: A2A/stablecoins sin observable de arranque fechado — la diferencia exacta con Visa','ROIC 51,0% · ROIIC 79% · 10-K FY2025 acc. 0001141391-26-000013'),
(1,'ASML','ASML Holding',3,'Ausencia de destino: 100% de EUV, 90-94% de litografía; 30 años y 2.000+ patentes de ventaja','RIESGO DE COLA exógeno (China 33% de ventas bajo controles cambiantes; TSMC vía Taiwán) — no es reloj del mecanismo','ROIC 60,8% · 20-F, reporta en EUR'),
(1,'TRI','Thomson Reuters',3,'Westlaw + West Key Number System (35M de clasificaciones) + KeyCite: el precedente legal está indexado en SU taxonomía','Sin caducidad encontrada. Q2-26 orgánico +8%, Big 3 +10%, guía SUBIDA (6-K 5-ago-2026). Candor declarado: su informe nombra «displacement from our own customers»','ROIC 12,0% (gw 56% del capital, declarado) · 40-F'),
(1,'REL.L','RELX',3,'LexisNexis Risk (datasets propietarios) + Elsevier: la revista es la moneda con la que un científico cobra su carrera','Sin caducidad encontrada. H1-26 subyacente +7%, Legal +10% ACELERANDO justo donde el relato de IA la mata (6-K 23-jul-2026)','ROIC 24,0% · 20-F en EDGAR acc. 0001104659-26-017277'),
(1,'UNP','Union Pacific',3,'26.294 millas de derecho de paso EN PROPIEDAD que nadie va a volver a expropiar','Vector regulatorio abierto sin reloj del mecanismo: STB (reciprocal switching); fusión NS en abeyance desde 28-may-2026','ROIC 11,9% · 10-K FY2025 acc. 0000100885-26-000037'),
(1,'ORLY',"O'Reilly Automotive",3,'El mecánico necesita la pieza en 30 minutos: 32 CDs con >156.000 SKUs de acceso mismo día, ~50% profesional','Sin caducidad: el 10-K NO menciona el vehículo eléctrico ni una vez. Parque 286M vehículos, edad media 12,6 años','ROIC 35,0% · gw 12% · 10-K acc. 0000898173-26-000009'),
(1,'AZO','AutoZone',3,'Misma red: 133 mega-hubs con 80-110.000 SKUs; programa comercial en 6.098 tiendas','EV nombrado como riesgo SIN fecha ni cifra. Más débil que ORLY: 31,7% comercial vs ~50%','ROIC 27,4% · gw 3% · 10-K acc. 0001104659-25-102611'),
(1,'OTIS','Otis Worldwide',4,'2,5M de ascensores con inspección legalmente obligatoria + densidad de ruta irreplicable localmente','Servicio = 91% del beneficio de segmento; la cartera creció y expandió margen mientras el equipo nuevo caía −8% dos años. Retención no publicada (DEGRADADO)','ROIC 48,4% (gw 71% del capital, declarado) · 10-K acc. 0001781335-26-000011'),
(1,'GE','GE Aerospace',5,'Certificado de tipo FAA + 80.000 motores instalados: la pieza caliente no tiene alternativa PMA','RPO de servicios 163.029 M$ (85,6% del total), 69% reconocible en 10 años — la única cuya contabilidad auditada cubre la ventana completa','ROIC 19,5% · 10-K acc. 0000040545-26-000008'),
(1,'MCO',"Moody's (MIS)",5,'Licencia NRSRO + issuer-pays: MIS margen 68,3% y 74% del beneficio operativo','Sin caducidad encontrada. Defectos declarados: el «requisito de dos ratings» NO está en el 10-K (narrativa); MA (26% restante) es nivel 7','ROIC 19,8% (gw 61%, declarado) · 10-K'),
(1,'GOOGL','Alphabet',4,'Escala reinvertible + gravedad de datos: búsqueda, YouTube, Android, Cloud — cuatro redes que se alimentan','RELOJ DECLARADO: primer ataque estructural al buscador en 20 años. Se queda en B1 por lo que el ciego midió dos veces (nivel 4 estable, 12/12) y porque el ataque aún no tiene firma en ingresos','ROIC 34,4% · gw 11%'),
# --- BLOQUE 2: economia elite con UN reloj fechado o una medida clave degradada ---
(2,'V','Visa',2,'Misma coordinación de dos lados que Mastercard, a mayor escala','RELOJ ARRANCADO Y FECHADO: demanda DOJ (sept-2024) contra el monopolio de red en débito, EN DISCOVERY desde 2026; provisión por litigios 2.562 M$ FY25 vs 462 FY24','ROIC 37,1% · portada iXBRL 5 clases'),
(2,'MSFT','Microsoft',2,'Identidad corporativa (Entra/AD) + Office como formato + gravedad de datos Azure: se renueva por procurement','GRIETA PROPIA MEDIDA: gate de OE roto el 29-jul-2026 (54.582M < 55.000M umbral); capex +79,6%; primer FCF en caída en años','ROIC 21,7% · 10-K FY2026 acc. 0001193125-26-323660'),
(2,'AAPL','Apple',4,'2.300M de dispositivos con datos, cuentas y hábitos atados al ecosistema','DOS RELOJES REGULATORIOS sobre rentas (pago de Google por defecto; comisión App Store) — erosionan márgenes, no el mecanismo','ROIC 137% (capital empleado 0,32× ventas) · gw 7%'),
(2,'TSM','Taiwan Semiconductor',3,'Casi-monopolio de manufactura de vanguardia: 74-77% del ingreso en nodos ≤7nm; el cliente no tiene destino alternativo','R6 JURISDICCIÓN ÚNICA (al valor, no a la tasa) + top-2 clientes ~36% y deteriorándose + capex 52-56.000M','ROIC 34,6% · 20-F, reporta en TWD'),
(2,'CME','CME Group',3,'Monopolio regulado de futuros de tasas de EEUU; red de liquidez auto-reforzante con ahorro de netting','FMX/DTCC atacan exactamente el netting. Balance de cámara: ROIC declarado NO COMPARABLE (garantías de clientes dentro)','margen NOPAT ~48% s/ventas · ruta cámara declarada'),
(2,'CSU.TO','Constellation Software',4,'Máquina de M&A con hurdle 25-30% TIR sobre software vertical fragmentado; empleados compran acciones con su dinero','Sucesión (Leonard dejó la presidencia oct-2025) y orgánico ~4%: el motor es comprado. SBC = CERO verificado por ausencia','ROIC 20,6% con la fórmula del método (el ~10% era OTRA definición) · FS auditados KPMG'),
(2,'CDNS','Cadence Design',3,'Duopolio EDA: cambiar de flujo a mitad de diseño arriesga un tape-out de cientos de millones','Sin reloj del mecanismo. DATO DEGRADADO: goodwill 117% del capital empleado — capital ex-goodwill NEGATIVO; el ROIC no es interpretable','ROIC 38,0% (no interpretable, declarado) · gw 117%'),
(2,'ISRG','Intuitive Surgical',5,'Base instalada 11k sistemas + entrenamiento del cirujano + 85% ingreso recurrente (def. propia; 76% ex-leasing)','RELOJ ARRANCADO PERO MENOR DE LO DICHO: Hugo despejada SOLO urología (K250725, 510(k)); Ottava solo abdomen superior, sin filing de J&J. Procedimientos EEUU 16%→14%→12%','ROIC 24,8% · caja 8.626M sin deuda'),
(2,'7741.T','HOYA',3,'Dos cuellos de botella de ciencia de materiales: mask blanks EUV (cuasi-monopolio) + sustratos HDD + lentes','Dato de cuota NO citable (no está en filings). El único hecho fechado de la ventana es el MEJOR trimestre de su historia: +16% ingresos, +30% beneficio, recompra 2,99%','ROIC 23,8% publicado (43,5% ex-caja) · tanshin 31-jul-2026 · FUENTE ÚNICA no-US'),
(2,'AMZN','Amazon',5,'Doble foso: AWS (coste de cambio de arquitectura) + marketplace/Prime (coordinación)','DATO ROTO DECLARADO: owner earnings NEGATIVOS (−11.800M) porque FCF−SBC con capex total no separa mantenimiento de crecimiento en ciclo de IA. Es defecto de fórmula, no veredicto','ROIC 13,1% · KO-4 formal declarado'),
(2,'SPGI','S&P Global',3,'Duopolio NRSRO + el S&P 500 como estándar civilizatorio + costes de cambio en Market Intelligence','Mecanismo estable en el ciego (12/12, subiendo). ROIC 9,1% NO DECIDIBLE: goodwill IHS Markit = 85% del capital empleado contamina el denominador','ROIC no decidible (declarado) · 52 años subiendo dividendo'),
(2,'ADP','ADP',3,'Nómina + cumplimiento fiscal multi-jurisdicción; retención de ingresos 92,1%','DEFECTO DECLARADO: 23,6% del EBIT es interés sobre float de clientes (1.355M/5.730M) — eso es duración, no foso','ROIC 46,3% · 10-K FY26 5-ago-2026'),
# --- BLOQUE 3: foso real y grande con grieta YA medida, o sin resolucion del instrumento ---
(3,'NVDA','Nvidia',6,'CUDA + ecosistema de desarrolladores + integración chip-software-networking: foso auténtico HOY','GRIETA MEDIDA: top-3 clientes 54% del revenue (10-Q Q1 FY27); garantías 105.000M ligadas a OpenAI (8-K 17-ago, FUENTE ÚNICA); sus mayores clientes construyen silicio propio','ROIC 65,9% · convicción alta a 3 años, baja a 10'),
(3,'MSCI','MSCI',6,'El índice como estándar + retención 95,3% — la franquicia sigue incrustada','LA TARIFA DEJÓ DE SER SUYA: basis point fee 2,44→2,28 acelerando ×5 tras la enmienda BlackRock; 2º tramo 1-ene-2027 SIN CUANTIFICAR; BlackRock 19,8% del segmento Index','ROIC 32,9% (gw 85%, declarado) · 8-K acc. 0001408198-26-000008'),
(3,'VEEV','Veeva Systems',6,'Vault GxP: la revalidación regulatoria es el candado (54% de suscripciones) — NO refutado','EL CANDADO COMERCIAL SÍ SE ROMPIÓ: Salesforce +AstraZeneca/Novartis migradas; suscripción comercial +16,9%→+10,6% en 5 trimestres; soporte CRM adelantado a 31-dic-2029','ROIC 83,4% (gw 52%) · 10-K FY26 20-mar-2026'),
(3,'IDXX','IDEXX',6,'Razor-blade veterinario: ~80% recurrente + candado de compromisos de ~5.000M (la «exclusividad» NO está en el 10-K)','GRIETA MEDIDA: visitas clínicas EEUU −2% en 2025 y guiadas a caer igual en 2026; IDEXX crece +6% same-store contra +2% de la clínica — le quita margen al veterinario; instrumentos −19,5% Q2','ROIC 46,9% · gw 19% · 10-K acc. 0000874716-26-000038'),
(3,'WST','West Pharmaceutical',5,'El tapón está nombrado en el expediente del fármaco: cambiar obliga a re-presentar datos de equivalencia','CANDADO REVOCABLE POR SU PROPIO 10-K: si la regulación redujera la carga de datos, «competitive pressure would increase». GLP-1 oral nombrado como amenaza; 1 cliente = 15,8%; HVP estancado en 60% tres años','ROIC 16,5% · gw 4%'),
(3,'MTD','Mettler-Toledo',5,'Base instalada calificada GxP con servicio y consumible atados (~25% servicio)','GRIETA EN EL PRECIO: devolvió 28M de recargos arancelarios — parte del «pricing power» de 2025 era arancel; FY24 orgánico fue CERO ex-partidas; su 10-K admite límites para repercutir costes','ROIC 24,4% · gw 29%'),
(3,'6861.T','Keyence',4,'Venta directa consultiva + catálogo de sensórica: margen operativo 51% sostenido, deuda cero','EL CRITERIO DECIDE EL NÚMERO: ROIC 13,8% u 84,6% según se depure la cartera de 2,98 billones ¥. Punto ciego: intangibles ×4,6 sin explicación en el yuho auditado','margen op. 51,0% · yuho Deloitte 15-jun-2026 · FUENTE ÚNICA no-US'),
(3,'4684.T','OBIC',4,'ERP implantado con empleados propios y atado a la regulación fiscal japonesa: margen operativo 65,7%','CAJA OCIOSA: 87% del activo es caja y valores (capital invertido NEGATIVO si se depura); 100% Japón, internacional <1%. El mecanismo es fuerte; el capital no trabaja','margen op. 65,7% · deuda cero · yuho 23-jun-2026 · FUENTE ÚNICA no-US'),
(3,'STMN.SW','Straumann',5,'Coste de cambio clínico del implantólogo + formación + 35% de cuota global','GRIETA CONTABLE: la M&A (Neodent/ClearCorrect) comprimió el ROCE reportado de 35% a ~17%; el núcleo sigue élite pero opacado. Orgánico +8,9% real (CER)','ROIC 19,7% (23,5% core) · AR 2025 · FUENTE ÚNICA no-US'),
(3,'VRSK','Verisk Analytics',2,'Candado de coordinación LITERAL en su 10-K: los datos contributivos siguen «unless the data contributor chooses to opt out… no cost to us»','El mismo 10-K: «we do not own the information». Y crece al 3,9-4,3%: el más lento del grupo de datos. Máquina de caja, no reinvertidora','ROIC 23,0% · gw 42%'),
(3,'CPRT','Copart',2,'Coordinación aseguradoras ↔ pool global de compradores + suelo con licencia irreplicable','SIN CANDADO CONTRACTUAL («no assurance that our existing agreements will not be canceled»); 81% de unidades de UNA clase de cliente cuya decisión la toma una fórmula ajena; 9M FY26: ingresos −0,2%','ROIC 22,5% · gw 8% — el denominador más limpio del ejercicio'),
(3,'ADYEN.AS','Adyen',4,'Plataforma única de pagos construida in-house; coste de cambio enterprise; 100% orgánico','NO RANKEABLE POR ROIC: denominador negativo (−16% a +154% según criterio de caja). Net revenue +18%; EBITDA 53%. Entra por mecanismo, con el dato declarado','ROIC no calculable (declarado) · AR 2025 · FUENTE ÚNICA no-US'),
]
FUERA=[
 ('ADBE','Decisión de Felipe: bajo asedio de la IA. Registro del dato: el ataque NO tiene firma en filings (+11,97% y +12,68% los dos últimos trimestres, ARR 25.200M) — queda fuera por juicio del dueño del método, con el desacuerdo del dato declarado'),
 ('ZTS','Mecanismo de precios ROTO y medido: el precio desapareció del puente 2T-26; guía FY26 recortada a −3/−1%; Elanco Pet Health +12% y Merck CA +7% el mismo trimestre. 0/8 en el ciego'),
 ('WM','Knock-out: ROIC 8,2% < 9,70% sobre capital total. El mecanismo (vertederos a 38 años) es élite; el retorno no llega. Sin apelación (M-6)'),
 ('COST','Fuera del alcance del instrumento: rotación alta con margen NOPAT 2,5%; la ruta alterna no mide este modelo. No es un veredicto de calidad'),
 ('DECK','Nivel 7: permiso cultural. Su propia tesis (25-ago) lo escribe: «depende de que la dirección siga eligiendo margen sobre volumen cada trimestre». HOKA +23,6%→+15,9%→+7,7% con margen −460pb. Y YA SE ROMPIÓ UNA VEZ: 24,9% de margen (2010) → pérdida operativa (2017) con ventas +87%'),
 ('NOW','Grieta medida: margen operativo Q2 4,1% vs 11,1%; ~11.000M de M&A en 8 meses; deuda ×5. El foso se está recomprando'),
 ('FICO','El reloj YA SE EJECUTÓ: FHFA + Fannie/Freddie aceptan VantageScore 4.0 (SEL-2026-04, 22-abr-2026). Y su 10-Q posterior declara «no material changes» en riesgos'),
 ('INTU','Gate propio disparado (unidades TurboTax −2%); TurboTax guiado a +2/+3% desde +7%. Matiz declarado: el umbral de guía cayó DENTRO del rango (error de diseño del gate)'),
 ('ACN','Su propio 10-K niega el mecanismo: contratos cancelables con aviso corto, RPO 0,55 años, atrición 14%. Bookings −2%, Managed Services −16%'),
 ('BKNG','Capital empleado negativo (el compounding lo fabrica la recompra) + desintermediación IA + su múltiplo autorizado exigía la pieza 1 en cuarentena'),
 ('NFLX','El foso hay que recomprarlo: ~18.000M/año de contenido a perpetuidad. Nivel 7-8 estable en el ciego'),
 ('AVGO','Un distribuidor = 42% del revenue (vs 29%); VMware no se reporta separado — la tesis de cosecha no es falsable'),
 ('MELI','Fuerte con reloj, no ultra: resultado operativo −17,2% con ingresos +49,8%; mora 90+ = 18,7%; Argentina 42% de la contribución. OE cruza cero según la base'),
 ('DUOL','Sin mecanismo: 82% del ingreso pasa por Apple/Google; altas de pago 600k→200k; bookings +7,8% vs ingresos +18,3%. Gate de venta roto y sin ejecutar (21 días)'),
 ('SNPS','Duopolio EDA real pero NO DECIDIBLE: ROIC 2,0% con goodwill Ansys 65% del capital; ventana contaminada 2-3 años'),
 ('MSFT-gemelo: BR','Broadridge: peaje regulado PERO la tarifa la fija el NYSE (literal en su 10-K) y el margen ya se comprime (ingresos +9%, EBT +5%)'),
]
rows=[]
orden={1:0,2:0,3:0}
for b,t,nom,niv,mec,vec,dato in L:
    o=D.get(t,{}); d=DCF.get(t,{})
    orden[b]+=1
    rows.append({'bloque':b,'orden':orden[b],'ticker':t,'nombre':nom,'nivel_mecanismo':niv,
      'mecanismo':mec,'vector_y_reloj':vec,'dato_clave':dato,
      'roic':o.get('roic'),'gw_sobre_capital':o.get('gw_sobre_capital'),
      'ev_oe':o.get('ev_sobre_oe'),'brecha_pp_informativa':d.get('brecha_pp'),
      'sens_C3':d.get('ratio_sens'),'mkt_cap_usd':o.get('mkt_cap'),
      'fuente':'EDGAR' if t in D and o.get('nopat_ult') else 'PRIMARIA no-US / ruta declarada'})
with open('Rankings/2026-08-26/Los36_QG_v2_2026-08-26.csv','w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump({'filas':rows,'fuera':FUERA},open('Rankings/2026-08-26/_trabajo/final36_v2.json','w'),ensure_ascii=False,indent=1,default=str)
NOM={1:'INDESTRUCTIBLES',2:'NÚCLEO',3:'FRONTERA'}
for b in (1,2,3):
    print(f"\n=== BLOQUE {b} — {NOM[b]} ===")
    for r in [x for x in rows if x['bloque']==b]:
        br=r['brecha_pp_informativa']
        print(f"  {r['orden']:>2}. {r['ticker']:9} niv{r['nivel_mecanismo']}  {r['nombre']:<26} "
              f"{('ROIC '+format(r['roic']*100,'.0f')+'%' if r['roic'] else 'ROIC n/d'):>10}  "
              f"{('brecha '+format(br,'+.0f')+'pp' if isinstance(br,(int,float)) else ''):>14}")
print(f"\nFUERA con motivo: {len(FUERA)}")
