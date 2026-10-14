# -*- coding: utf-8 -*-
"""
BRIEFING DE PORTAFOLIO · 22 junio 2026
Metodología QG + VALUE + BUFFETT. Construye el PDF final en el Desktop.
Lee briefing_data.json (datos numéricos) + prosa de síntesis embebida.
"""
import json
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (Spacer, Paragraph, NextPageTemplate, PageBreak,
                                Table, TableStyle, KeepTogether)
from qg_design import (BriefingDoc, STY, SectionFlag, callout, kpi_row,
                       data_table, img, CoverFlowable, HRule, C, PAGE_W, MARGIN)
import qg_charts as ch

DATA = json.load(open('/tmp/qg_briefing/briefing_data.json'))
D = {d['ticker']: d for d in DATA}
W = PAGE_W - 2 * MARGIN

def P(t, s='body'): return Paragraph(t, STY[s])
def money(x): return f"${x:,.0f}" if x and x >= 100 else (f"${x:,.1f}" if x else "n/d")

ACT_COL = {'AÑADIR': C['azul'], 'MANTENER': C['ocre'], 'REDUCIR': C['rojo_oscuro'], 'SALIR': C['rojo']}
def act(a):
    st = ParagraphStyle('act', fontName='Helvetica-Bold', fontSize=7.6, leading=9,
                        textColor=ACT_COL.get(a, C['tinta']))
    return Paragraph(a, st)

# ============================================================ CHARTS
ALL = [(d['ticker'], d['qg_score']) for d in DATA]
ch.chart_ranking_qg(ALL)
ch.chart_margin_safety([(d['ticker'], d['margin_of_safety_pct']) for d in DATA])
ch.chart_quality_value_map([(d['ticker'], d['qg_score'], d['margin_of_safety_pct']) for d in DATA])
ch.chart_pnl([(d['ticker'], d['pnl']) for d in DATA])
ch.chart_reanalysis('ADBE', 195, 215, 365, 505)
ch.chart_reanalysis('DUOL', 127, 97, 190, 337)
ch.chart_reanalysis('INTU', 267, 284, 370, 498)

story = []

# ============================================================ PORTADA
story.append(CoverFlowable(
    titulo=['Briefing de', 'Portafolio'],
    ticker_line='18 POSICIONES · QUALITY GROWTH + VALUE + BUFFETT',
    tagline=['Ranking, veredicto por posición y plan de rebalanceo.',
             'Re-análisis obligatorio de ADBE, DUOL e INTU (caída de tesis).'],
    kpis=[('10.7', 'QG medio / 13.5'), ('15 / 18', 'infravaloradas'),
          ('+18%', 'margen medio'), ('3', 'en alerta -20%')],
    meta_items=[('FECHA', '22 jun 2026'), ('PRECIOS', 'cierre 18-jun-2026'),
                ('MARCO', 'QG + VALUE'), ('HORIZONTE', '5-10 años')],
))
story.append(NextPageTemplate('content'))
story.append(PageBreak())

# ============================================================ RESUMEN 30 SEG
story.append(SectionFlag('El portafolio en treinta segundos', 'Lo que el tablero dice antes de entrar en detalle'))
story.append(Spacer(1, 8))
story.append(kpi_row([('10.7/13.5', 'Calidad QG media'), ('10 de 18', 'en el núcleo (≥10.8)'),
                      ('+18%', 'margen de seguridad medio'), ('1', 'venta por encaje (BABA)')]))
story.append(Spacer(1, 9))
story.append(P('<b>El veredicto en una línea.</b> Tienes una cartera de calidad genuinamente alta '
  '(QG medio 10,7/13,5; diez nombres en el núcleo) y, tras las correcciones del último año, '
  'mayoritariamente <b>infravalorada</b>: 15 de 18 posiciones cotizan por debajo de su valor intrínseco. '
  'La acción no es revolucionar nada, sino <b>tres ajustes quirúrgicos</b>: añadir en dos joyas baratas de máxima calidad '
  '(<b>NFLX</b> y <b>SPGI</b>), recortar dos ganadoras que ya cotizan por encima de su valor (<b>AXP</b> y <b>ABNB</b>), '
  'y salir del único error de <i>encaje</i> con el marco (<b>BABA</b>). Las tres posiciones que dispararon el gatillo '
  'de re-análisis —ADBE, DUOL e INTU— <b>no son trampas de valor</b>: son de-rating de múltiplo con fundamentales intactos. '
  'Ninguna ha disparado un trigger de venta total. Pero dos tienen condiciones falsables a la vuelta de la esquina.'))
story.append(P('<b>Los tres puntos críticos a recordar.</b>', 'body'))
story.append(P('<b>1 · Las caídas son de precio, no de negocio — pero con relojes en marcha.</b> '
  'ADBE (−25%), DUOL (−20%) e INTU (−19%) cayeron por compresión de múltiplo y miedo a la IA, no por colapso de ingresos o márgenes. '
  'Sin embargo, ADBE tiene la guía de ARR orgánico recortada y al CFO saliendo; INTU se juega su tesis en la guía FY2027 de <b>agosto 2026</b>. '
  'Son oportunidades <i>con vigilancia</i>, no compras a ciegas.'))
story.append(P('<b>2 · El único error real es de tipo, no de timing.</b> BABA reprueba el marco por calidad (58% QG, riesgo estructural VIE), '
  'no por estar cara. Vender no es admitir una pérdida —está +7%— sino corregir un encaje equivocado y liberar capital para calidad verificada.'))
story.append(P('<b>3 · Las verdaderas "caras" son tus ganadoras.</b> Las únicas posiciones con margen de seguridad <b>negativo</b> '
  'son AXP (−10%) y ABNB (−20%): el precio ya superó el valor. La disciplina del marco exige recortarlas en fuerza, '
  'igual que exige promediar a la baja en las castigadas de calidad.'))
story.append(callout('El espejo del sesgo de disposición',
  'Estás dispuesto a defender el promedio a la baja en DUOL o ADBE porque "el negocio sigue intacto". '
  'La pregunta incómoda: ¿aplicas la misma frialdad para <b>recortar</b> AXP (+119%) y ABNB (+39%) ahora que cotizan por encima de su valor? '
  'El instinto vende lo que sube y abraza lo que baja. El marco ordena exactamente lo contrario cuando el precio cruza el valor intrínseco.',
  kind='PAUSA'))

# ============================================================ CÓMO LEER
story.append(SectionFlag('Cómo está construido este tablero', 'Reglas de lectura y límites del dato'))
story.append(Spacer(1, 8))
story.append(P('Cada posición se ha re-leído desde su <b>Tesis Ultra</b> existente, de donde salen el score Seilern ponderado (sobre 13,5; '
  'R1, R3 y R4 pesan 1,5×) y el valor intrínseco del DCF ponderado por tres escenarios. Sobre ese valor se ha calculado el '
  '<b>margen de seguridad actual</b> contra el precio de cierre del 18 de junio de 2026, obtenido en vivo. '
  'El margen es <b>(valor justo − precio) / valor justo</b>: positivo significa que el mercado pide menos que el valor estimado.'))
story.append(P('<b>Cuatro veredictos posibles.</b> <font color="#2A5A7E"><b>AÑADIR</b></font> (calidad de núcleo + descuento real, sin trigger), '
  '<font color="#B8860B"><b>MANTENER</b></font> (tesis intacta pero precio sin margen claro o calidad sub-núcleo), '
  '<font color="#8C1410"><b>REDUCIR</b></font> (margen de seguridad negativo: el precio superó el valor), '
  '<font color="#C60C2A"><b>SALIR</b></font> (la posición reprueba el marco por calidad). '
  'El score es un <i>filtro</i>, no un veredicto: descarta, no compra. La decisión la toma la combinación calidad + precio.'))
story.append(callout('La calidad filtra; el precio decide',
  'Un score de 12/13,5 no es una orden de compra: NFLX y MA son de élite, pero solo NFLX cotiza en zona de ganga. '
  'Y un score sub-umbral no es una orden de venta: MSFT puntúa 71% y se mantiene porque el negocio no se ha roto y cotiza con descuento. '
  'Vender por calidad (BABA) es distinto de recortar por precio (AXP, ABNB).', kind='LECCION'))
story.append(P('<b>Límite honesto del dato.</b> Los valores intrínsecos son los de cada tesis (HECHO sobre el documento); '
  'los precios son de mercado a 18-jun-2026 (HECHO); los múltiplos a precio actual son re-escalados, no recalculados con BPA en vivo (INFERENCIA). '
  'Netflix refleja su <i>split</i> 10:1 de noviembre 2025 (cotiza ~$77, no ~$770). Esto no es asesoría registrada.'))
story.append(PageBreak())

# ============================================================ RANKING
story.append(SectionFlag('Ranking por calidad QG', 'Las diez reglas de Seilern, puntuadas sobre 13,5'))
story.append(Spacer(1, 6))
story.append(img('/tmp/qg_briefing/c_ranking.png', W * 0.74))
story.append(Spacer(1, 4))
story.append(P('Diez de las dieciocho superan el umbral de núcleo (10,8 = 80%). El podio —<b>MA (12,55), NFLX (12,40), SPGI (12,10), V (11,90)</b>— '
  'son máquinas de capital-ligero con foso de red o de datos. En la base, <b>BABA (7,80)</b> está veintidós puntos por debajo del umbral: '
  'no es un problema de precio, es un problema de <i>encaje</i> con el marco. MSFT, SPOT, ABNB y ADBE quedan algo por debajo del umbral por '
  'fallos concretos no perdonados (intensidad de capital, SBC, o deceleración), lo que no les quita la condición de mantener.', 'body'))
story.append(PageBreak())

# ============================================================ TABLA MAESTRA
story.append(SectionFlag('El tablero completo', 'Calidad, valor, posición y veredicto en una vista'))
story.append(Spacer(1, 6))
order = sorted(DATA, key=lambda d: -d['qg_score'])
rows = []
for d in order:
    mos = d['margin_of_safety_pct']
    mos_p = Paragraph(f"{mos:+.0f}%", ParagraphStyle('m', fontName='Helvetica-Bold', fontSize=8,
                      textColor=(C['verde'] if mos >= 10 else (C['rojo_oscuro'] if mos < 0 else C['ocre']))))
    pnl_p = Paragraph(f"{d['pnl']:+.0f}%", ParagraphStyle('p', fontName='Times-Roman', fontSize=8,
                      textColor=(C['azul'] if d['pnl'] >= 0 else C['rojo_oscuro'])))
    rows.append([d['ticker'], f"{d['qg_score']:.2f}", money(d['fair_value_usd']),
                 money(d['current_price_usd']), mos_p, d['price_zone'], pnl_p, act(d['final_action'])])
cw = [W*0.085, W*0.075, W*0.115, W*0.115, W*0.10, W*0.155, W*0.10, W*0.16]
story.append(data_table(['Ticker', 'QG', 'V. justo', 'Precio', 'Margen', 'Zona', 'P&L', 'Veredicto'],
                        rows, cw, align_center_cols=[1, 2, 3, 5]))
story.append(Spacer(1, 6))
story.append(P('<font size=8><i>Valor justo = DCF ponderado de la tesis. Margen = (valor − precio)/valor sobre cierre 18-jun-2026. '
  'P&L = rentabilidad acumulada del usuario. ABNB reescalado a 13,5 (la tesis lo puntuó sobre 11,5).</i></font>', 'small'))
story.append(Spacer(1, 10))
story.append(img('/tmp/qg_briefing/c_margin.png', W * 0.78))
story.append(Spacer(1, 4))
story.append(P('El margen de seguridad ordena la cartera en tres bloques. <b>Doce</b> nombres cotizan con descuento de doble dígito '
  '(de ADBE +45% a GOOGL +12%): es ahí donde vive el valor. <b>Cuatro</b> rondan el valor justo con margen modesto o nulo '
  '(SPOT y V +16%, BRK-B +8%, TSM 0%): mantener, no perseguir. Y solo <b>dos</b> cotizan en negativo —AXP −10% y ABNB −20%—: '
  'el precio ya superó al valor. Que apenas dos de dieciocho estén caras confirma que el reto de esta cartera no es la sobrevaloración, '
  'sino <i>dónde concentrar la compra</i> entre tanta calidad descontada.'))
story.append(PageBreak())

# ============================================================ MAPA CALIDAD x VALOR
story.append(SectionFlag('Mapa calidad × valor', 'Dónde comprar más, dónde solo mantener, de qué salir'))
story.append(Spacer(1, 6))
story.append(img('/tmp/qg_briefing/c_qvmap.png', W * 0.74))
story.append(Spacer(1, 4))
story.append(P('El cuadrante que importa es el <b>superior derecho</b>: calidad de núcleo (por encima de la línea roja 10,8) <i>y</i> margen de seguridad positivo. '
  'Ahí viven NFLX, SPGI, MA, BKNG, AMZN, MELI, V y GOOGL — el corazón sano de la cartera. '
  'A la <b>derecha pero abajo</b> (barato y sub-núcleo) están ADBE, MSFT y DUOL: descuento real con una marca de calidad que vigilar. '
  'A la <b>izquierda</b> (margen negativo) caen AXP y ABNB: buena calidad, pero el precio ya se comió el valor — recortar. '
  'BABA queda sola: ni calidad suficiente ni descuento que compense el riesgo estructural.'))
story.append(callout('No confundas barato con bueno, ni bueno con comprable',
  'ADBE es lo más barato del tablero (+45%) pero su calidad cayó a 9,75 y está en probación: barato no basta. '
  'MA es lo de mayor calidad (12,55) pero solo +20% de margen en zona de acumulación, no de ganga: bueno no es siempre "comprar más". '
  'La compra agresiva pide las dos cosas a la vez — y hoy eso es NFLX y SPGI.', kind='LECCION'))
story.append(PageBreak())

# ============================================================ VEREDICTO POR POSICION
story.append(SectionFlag('Veredicto por posición', 'Qué hacer con cada una, y por qué'))
story.append(Spacer(1, 6))

def verdict_block(title, color_hex, items):
    story.append(P(f'<font color="{color_hex}"><b>{title}</b></font>', 'h2'))
    vr = []
    for tk in items:
        d = D[tk]
        reason = str(d.get('action_reason') or '').strip()
        if not reason and d.get('reanalysis'):
            reason = str(d['reanalysis'].get('recommendation', ''))
        reason = reason.replace('&', 'y').replace('<', ' ').replace('>', ' ')
        if len(reason) > 240: reason = reason[:237] + '…'
        vr.append([Paragraph(f"<b>{tk}</b>", STY['td_b']),
                   Paragraph(f"QG {d['qg_score']:.1f} · margen {d['margin_of_safety_pct']:+.0f}%", STY['td']),
                   Paragraph(reason, STY['td'])])
    t = Table(vr, colWidths=[W*0.10, W*0.22, W*0.68])
    t.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'),
                           ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),5),
                           ('LINEBELOW',(0,0),(-1,-2),0.4,C['gris_linea'])]))
    story.append(t)
    story.append(Spacer(1, 6))

verdict_block('AÑADIR — calidad de núcleo con descuento real', '#2A5A7E', ['NFLX', 'SPGI'])
verdict_block('REDUCIR — el precio superó el valor', '#8C1410', ['AXP', 'ABNB'])
verdict_block('SALIR — reprueba el marco por calidad', '#C60C2A', ['BABA'])
story.append(PageBreak())
verdict_block('MANTENER — tesis intacta, sin margen para perseguir', '#B8860B',
              ['MA', 'V', 'BKNG', 'AMZN', 'GOOGL', 'TSM', 'MELI', 'MSFT', 'SPOT', 'BRK-B', 'ADBE', 'DUOL', 'INTU'])
story.append(P('<font size=8><i>ADBE, DUOL e INTU se mantienen pero entran en el re-análisis detallado de las páginas siguientes: '
  'su "mantener" lleva condiciones falsables, no es pasivo.</i></font>', 'small'))
story.append(PageBreak())

# ============================================================ TOP 3 INFRAVALORADAS
story.append(SectionFlag('Top 3 más infravaloradas', 'Mayor margen de seguridad sobre el valor intrínseco'))
story.append(Spacer(1, 6))
top_under = sorted(DATA, key=lambda d: -d['margin_of_safety_pct'])[:3]
for i, d in enumerate(top_under, 1):
    story.append(P(f'<b>{i}. {d["ticker"]} — {d["company"].split(",")[0].split("—")[0].strip()}</b> '
      f'· margen <font color="#6C7E48"><b>{d["margin_of_safety_pct"]:+.0f}%</b></font> · QG {d["qg_score"]:.2f} · zona {d["price_zone"]}', 'h3'))
    story.append(P(d.get('one_line', ''), 'body'))
story.append(Spacer(1, 4))
story.append(P('<b>El matiz de calidad.</b> Por margen puro el podio es ADBE (+45%), NFLX (+34%) y DUOL (+33%). '
  'Pero ajustado por calidad, la joya más limpia es <b>NFLX</b> (calidad de élite 12,4 <i>y</i> ganga), seguida de <b>SPGI</b> (12,1; +33%) y <b>MELI</b> (10,8; +29%). '
  'ADBE encabeza el descuento porque está <i>en probación</i>: su precio descuenta una Adobe casi estancada, lo que es una asimetría atractiva pero no exenta de riesgo. '
  'La conclusión operativa: el descuento más accionable hoy, sin condición previa, es <b>NFLX y SPGI</b>.'))
story.append(callout('El descuento es la consecuencia, no la causa',
  'Comprar ADBE solo porque "cayó 45%" es anclarse al precio. La pregunta correcta no es cuánto bajó, sino si el valor de $353 sigue siendo defendible. '
  'En NFLX y SPGI el valor no está en disputa; en ADBE sí, y por eso su descuento mayor exige primero una confirmación operativa.', kind='PAUSA'))
story.append(PageBreak())

# ============================================================ TOP 3 RIESGO
story.append(SectionFlag('Top 3 de riesgo · acción inmediata', 'Lo que exige una decisión esta semana, no el próximo trimestre'))
story.append(Spacer(1, 6))
risk_cards = [
 ('BABA', 'SALIR ahora', '#C60C2A',
  'Es el único nombre que reprueba el marco por <b>calidad</b> (58% QG, 22 puntos bajo el umbral), no por precio. '
  'El riesgo no es de valoración sino estructural y permanente: la estructura VIE significa que no posees acciones de la empresa operativa china, sino un contrato. '
  'Trampa de valor clásica. Acción: salir de forma ordenada y reciclar el capital hacia calidad verificada (NFLX/SPGI). Está +7%: no hay coste fiscal doloroso ni orgullo que defender.'),
 ('ADBE', 'No disparar el tramo agresivo', '#8C1410',
  'Tu propia tesis fijó una regla: "añadir con fuerza si cae bajo $200, <i>sin deterioro fundamental</i>". El precio cumple ($195) pero la <b>condición no</b>: '
  'la guía de ARR orgánico se recortó ~$480M y el CFO salió abruptamente a Marvell cuatro días tras el reporte. El re-análisis lo confirma como oportunidad, no trampa, '
  'pero con vigilancia elevada. Acción: <b>mantener</b>, <b>no</b> ejecutar el tramo de compra agresiva todavía; esperar a que el ARR neto nuevo confirme suelo (1-2 trimestres).'),
 ('INTU', 'Definir hoy la regla de agosto', '#B8860B',
  'La pieza de información que decide la tesis —la guía FY2027— <b>aún no existe</b>: llega en agosto 2026 con el Q4. El moat fue rebajado de Wide a Narrow y la saturación de unidades está confirmada '
  '(clientes de pago +5% vs 8-10% sano; el crecimiento es 100% precio). Acción: dejar por escrito el gatillo antes de que llegue el dato — '
  'si la guía confirma 5-10%, <b>reducir</b> a 0-2% sin apego; si sostiene doble dígito, añadir un tercio.'),
]
for tk, head, col, body in risk_cards:
    story.append(P(f'<font color="{col}"><b>{tk} — {head}</b></font>', 'h3'))
    story.append(P(body, 'body'))
    story.append(Spacer(1, 3))
story.append(P('<b>Segundo nivel de vigilancia (precio, no calidad):</b> AXP y ABNB cotizan por encima de su valor (margen −10% y −20%). '
  'No es urgente como BABA, pero son las candidatas naturales a recorte para financiar las compras de NFLX y SPGI — vender fuerza para comprar valor.'))
story.append(PageBreak())

# ============================================================ RE-ANALISIS (ADBE, DUOL, INTU)
def reanalysis_section(tk, headline):
    d = D[tk]; r = d.get('reanalysis') or {}
    story.append(SectionFlag(f'Re-análisis: {tk} — {d["company"].split(",")[0].split("—")[0].strip()}', headline))
    story.append(Spacer(1, 6))
    story.append(kpi_row([(f"{d['qg_score']:.2f}", 'QG hoy / 13.5'),
                          (money(d['current_price_usd']), 'precio jun-2026'),
                          (money(d['fair_value_usd']), 'valor justo base'),
                          (f"{d['margin_of_safety_pct']:+.0f}%", 'margen de seguridad')]))
    story.append(Spacer(1, 8))
    diag = str(r.get('drop_diagnosis', '')).replace('&', 'y')
    story.append(P('<b>Diagnóstico de la caída.</b> ' + diag, 'body'))
    # chart + fundamentals side by side
    funda = str(r.get('fundamentals_changed', '')).replace('&', 'y')
    cell_txt = [P('<b>Qué cambió en el negocio</b>', 'h3'), P(funda, 'body')]
    cimg = img(f'/tmp/qg_briefing/c_re_{tk}.png', W * 0.40)
    tbl = Table([[cimg, cell_txt]], colWidths=[W*0.42, W*0.58])
    tbl.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING',(1,0),(1,0),10)]))
    story.append(tbl)
    story.append(Spacer(1, 6))
    # bull / bear two columns
    bull = str(r.get('bull_case', '')).replace('&', 'y')
    bear = str(r.get('bear_case', '')).replace('&', 'y')
    bb = Table([[P('<font color="#2A5A7E"><b>El caso alcista</b></font>', 'h3'),
                 P('<font color="#8C1410"><b>El caso bajista</b></font>', 'h3')],
                [P(bull, 'body_l'), P(bear, 'body_l')]],
               colWidths=[W*0.5, W*0.5])
    bb.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                            ('BACKGROUND',(0,0),(-1,-1),C['panel']),
                            ('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),
                            ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),8),
                            ('LINEAFTER',(0,0),(0,-1),3,C['fondo'])]))
    story.append(bb)
    story.append(Spacer(1, 8))
    rec = str(r.get('recommendation', '')).replace('&', 'y')
    story.append(callout(f"Recomendación · convicción {r.get('conviction','')} · QG re-puntuado {r.get('qg_score_now','')}/13.5",
                         rec, kind='ALERTA'))
    story.append(PageBreak())

reanalysis_section('ADBE', 'Oportunidad con vigilancia elevada, no trampa de valor — pero el juez salió ambiguo')
reanalysis_section('DUOL', 'Oportunidad, no trampa: el patrón Amazon de invertir en vez de romperse')
reanalysis_section('INTU', 'Oportunidad fina y frágil: value-con-condición que se decide en agosto')

# ============================================================ REBALANCEO
story.append(SectionFlag('Plan de rebalanceo', 'Concreto, secuenciado, falsable'))
story.append(Spacer(1, 6))
story.append(P('<b>La lógica:</b> liberar capital de lo que reprueba (BABA) y de lo que se encareció (AXP, ABNB), '
  'y desplegarlo en lo que combina calidad de núcleo y descuento real <i>sin</i> condición previa (NFLX, SPGI). '
  'El resto de la pólvora se reserva para compras condicionadas a gatillos.'))
reb = [
 ['1', 'SALIR', 'BABA', 'Vender la posición completa', 'Reprueba el marco (QG 58%, riesgo VIE). Reciclar capital.'],
 ['2', 'REDUCIR', 'ABNB', 'Recortar ~⅓', 'Margen −20% (la más cara). Calidad de núcleo, pero el precio superó el valor.'],
 ['3', 'REDUCIR', 'AXP', 'Recortar ~¼–⅓', 'Margen −10% y falla umbral Seilern. Recorte de fuerza, no por la ganancia.'],
 ['4', 'CAPAR', 'TSM', 'No añadir; capar por tamaño', 'A valor justo (margen 0%) y con cola binaria de Taiwán: gestionar el tamaño, no perseguir.'],
 ['5', 'AÑADIR', 'NFLX', 'Compra inmediata', 'Calidad 12,4 + ganga (+34%). El despliegue más limpio del tablero.'],
 ['6', 'AÑADIR', 'SPGI', 'Compra en tramos en zona $400-460', 'Calidad 12,1 + margen +33%, pegada al umbral de compra agresiva.'],
 ['7', 'PÓLVORA', 'ADBE', 'Esperar confirmación de ARR', 'Tramo agresivo solo si el ARR neto nuevo recupera y se nombra CEO sólido.'],
 ['8', 'PÓLVORA', 'DUOL', 'Promediar solo bajo $95', 'Segundo tramo en/bajo el DCF conservador, donde el margen es máximo.'],
 ['9', 'PÓLVORA', 'INTU', 'Decidir tras la guía de agosto', 'Doble dígito → añadir ⅓; 5-10% → reducir a 0-2%.'],
]
rrows = []
for n, a, tk, what, why in reb:
    rrows.append([n, act(a) if a in ACT_COL else Paragraph(f'<b>{a}</b>', STY['td_b']),
                  Paragraph(f'<b>{tk}</b>', STY['td_b']), Paragraph(what, STY['td']), Paragraph(why, STY['td'])])
story.append(Spacer(1, 4))
story.append(data_table(['#', 'Acción', 'Pos.', 'Qué hacer', 'Por qué'],
                        rrows, [W*0.05, W*0.13, W*0.09, W*0.30, W*0.43]))
story.append(Spacer(1, 8))
story.append(callout('La secuencia importa',
  'Primero vender (BABA, ABNB, AXP): genera la liquidez. Después comprar lo incondicional (NFLX, SPGI). '
  'La pólvora condicional (ADBE, DUOL, INTU) se despliega contra gatillos escritos, no contra el impulso de "está barato". '
  'Si ejecutas las compras antes que las ventas, acabas sobre-invertido y sin disciplina.', kind='LECCION'))
story.append(PageBreak())

# ============================================================ P&L + TRIGGERS + CIERRE
story.append(SectionFlag('Rendimiento y disciplina de salida', 'De dónde vienes y qué te haría cambiar de opinión'))
story.append(Spacer(1, 6))
story.append(img('/tmp/qg_briefing/c_pnl.png', W * 0.70))
story.append(Spacer(1, 4))
story.append(P('Las grandes ganadoras (TSM +551%, NFLX +183%, SPOT +140%, AMZN +126%) confirman que la selección de calidad funciona en horizonte largo. '
  'El gatillo metodológico de −20% lo cruzaron ADBE y DUOL, e INTU lo roza (−19%): de ahí su re-análisis obligatorio, ya resuelto como "mantener con condiciones". '
  'Ninguna de las tres mostró deterioro de fundamentales suficiente para vender.'))
story.append(P('<b>Triggers maestros de la cartera (falsables).</b>', 'h3'))
story.append(P('· <b>ADBE</b>: reducir si el ARR neto nuevo cae otro trimestre y el margen operativo amenaza el 40%. Volver a añadir si el ARR orgánico re-acelera.<br/>'
  '· <b>INTU</b>: regla escrita para agosto 2026 — guía FY2027 en 5-10% → reducir a 0-2%; doble dígito → añadir ⅓.<br/>'
  '· <b>DUOL</b>: vender si el DAU crece por debajo del 15%, la penetración de pago cae bajo 8,5% o el margen bruto baja del 65%.<br/>'
  '· <b>TSM</b>: la única cola irrecuperable — movilización geopolítica o pérdida de liderazgo de proceso. Capar tamaño preventivamente.<br/>'
  '· <b>AXP / ABNB</b>: si el margen de seguridad sigue negativizándose, ampliar el recorte.', 'body'))
story.append(callout('La pre-mortem de la cartera',
  'Imagina que dentro de cinco años esta cartera decepcionó. La causa más probable no será NFLX ni SPGI: será haber mantenido BABA por inercia, '
  'haber promediado a la baja en ADBE antes de que confirmara, o haber dejado correr AXP y ABNB por encima del valor "porque venían ganando". '
  'Los tres errores son evitables hoy con las decisiones de este briefing.', kind='PREMORTEM'))
story.append(P('<b>Conexión con tu sistema.</b> Esta cartera de calidad-crecimiento es el motor patrimonial que complementa tu negocio (CAYLA) '
  'y tu horizonte de 5-10 años. La disciplina que aquí aplicas —vender el error de encaje, recortar lo caro, comprar la calidad castigada— '
  'es la misma que separa al inversor que compone del que solo participa. El score filtró; el precio decidió; ahora ejecuta.', 'body'))
story.append(Spacer(1, 8))
story.append(HRule())
story.append(P('<font size=7.5><i>Advertencias finales. HECHO: scores y valores intrínsecos provienen de las Tesis Ultra existentes; precios de mercado a 18-jun-2026. '
  'INFERENCIA: múltiplos a precio actual re-escalados, no recalculados con BPA en vivo; veredictos de síntesis del autor. '
  'SUPUESTO: los DCF asumen los escenarios de cada tesis. El score Seilern admite lectura estricta vs ponderada por calidad; aquí se usa la ponderada (denominador 13,5). '
  'ABNB reescalado desde 11,5. Documento de uso personal, metodología QG + VALUE + BUFFETT; no es asesoría de inversión registrada.</i></font>', 'small'))

# ============================================================ BUILD
doc = BriefingDoc('/tmp/qg_briefing/Briefing_Portafolio_22jun2026.pdf',
                  company_title='Briefing de portafolio · 22-jun-2026')
doc.build(story)
print('BRIEFING construido OK')
