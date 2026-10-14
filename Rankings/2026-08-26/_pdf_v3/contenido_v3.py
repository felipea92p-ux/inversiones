# -*- coding: utf-8 -*-
"""Contenido del PDF consolidado — motor de valoracion v3.1."""
import json, os, html
import motor_qg as M
from reportlab.platypus import PageBreak, Spacer
from reportlab.lib.units import cm

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open(os.path.join(BASE, 'Valor_Intrinseco_v3_36.json')))
FILAS = sorted(D['filas'], key=lambda z: z['calidad_ordinal'])
BYT = {f['ticker']: f for f in FILAS}

def e(s): return html.escape(str(s if s is not None else '')).replace('\n', ' ')
def pc(v, d=1, sign=False):
    if v is None: return '—'
    s = f'{v*100:+.{d}f}%' if sign else f'{v*100:.{d}f}%'
    return s.replace('.', ',')
def usd(v, d=1):
    if v is None: return '—'
    return f'{v:,.{d}f}'.replace(',', ' ').replace('.', ',')
def big(v):
    if v is None: return '—'
    a = abs(v)
    for u, s in ((1e12,'B'), (1e9,'mM'), (1e6,'M')):
        if a >= u: return f'{v/u:,.1f}{s}'.replace('.', ',')
    return usd(v, 0)

CUBOS = ['DESCUENTO CLARO', 'PRECIO JUSTO', 'PRIMA', 'NO DECIDIBLE']
BLQ = {1: 'INDESTRUCTIBLES', 2: 'NÚCLEO', 3: 'FRONTERA'}

# ─────────────────────────────────────────────────────────────────────
def portada():
    n_desc = sum(1 for f in FILAS if f['cubo'] == 'DESCUENTO CLARO')
    n_nd   = sum(1 for f in FILAS if f['cubo'] == 'NO DECIDIBLE')
    st = [Spacer(1, 5.6*cm), M.p('LOS 36 DE ULTRACALIDAD', 'h_seccion')]
    st += [M.p('Valor intrínseco reconstruido — motor v3.1, una tasa y una senda por empresa', 'h_sub')]
    st += [M.kpi_panel([
        ('151', 'AGENTES', 'flujo · tasa · senda · abogado del diablo, uno por papel y por empresa'),
        (f'{n_desc}/36', 'CON DESCUENTO', 'bajo margen exigido 9% / 18% / 27%'),
        (f'{n_nd}/36', 'NO DECIDIBLE', 'el ruido supera la resolución del instrumento'),
    ])]
    st += [Spacer(1, 0.8*cm), M.p(
        'Este documento sustituye al del 26-ago-2026, que declaraba caras a 34 de 36 empresas con primas de hasta '
        '<b>+588%</b>. Aquella lectura no era un juicio pesimista: era un <b>artefacto mecánico</b> de cinco defectos '
        'del motor. Aquí cada empresa lleva su propio WACC construido de mercado, su propia senda de diez años '
        'contrastada contra el mercado direccionable, y un adversario en sesión limpia cuyo único mandato era '
        'refutarla a la baja.', 'cuerpo')]
    st += [M.p('Documento de método dentro del marco propio de Felipe. No es asesoramiento de inversión personalizado y no '
        'soy asesor registrado. El candado B4 sigue cerrado: nada de lo que sigue autoriza una compra por sí solo. '
        'Cifras vivas fechadas al 26-ago-2026; caducan.', 'nota')]
    return st + [PageBreak()]

# ─────────────────────────────────────────────────────────────────────
def veredicto():
    st = M.flag_titulo('Veredicto primero', 'Qué cambió cuando el instrumento empezó a medir')
    nv = BYT.get('NVDA'); gg = BYT.get('GOOGL'); un = BYT.get('UNP')
    st += [M.callout('PAUSA REFLEXIVA',
        f'<b>Nvidia se dio la vuelta entera: de −24,5% de descuento a {pc(nv["premio"],1,True) if nv else "—"} de prima.</b> '
        'No la movió la tasa — la movió el candado que faltaba. Su senda sin techo implicaba ingresos en el año diez '
        'equivalentes al 41% del mercado mundial de semiconductores, cuando ninguna empresa ha superado nunca el ~20% '
        '(Intel hizo techo en 15-16%, Samsung en 12%). Era la única «barata» del documento anterior.')]
    st += [M.p(
        '<b>El motor viejo no valoraba: capitalizaba.</b> Con g∞ = 0% en 23 de las 36 y r = 9,70% plana, el múltiplo '
        'terminal quedaba clavado en 10,3× owner earnings para todas — Visa, Hermès, ASML y Union Pacific incluidas. '
        'Ninguna empresa élite del mundo cotiza a 10× su flujo libre, así que el instrumento decidía «cara» antes de '
        'mirar el negocio. La prueba está en el contrafactual: cambiando <i>sólo</i> esos dos parámetros, con el mismo '
        'owner earnings y la misma senda, el valor de Union Pacific se multiplica por 4,43 y el de Otis por 4,11.', 'cuerpo')]
    st += [M.p(
        '<b>El candado B se estaba aplicando invertido.</b> El marco ordena «WACC siempre bottom-up de mercado, prohibido '
        'heredarlo de un tier de calidad». El motor lo leyó como «prohibido calcular WACC por empresa» y usó bono más '
        'prima fija para las 36. La prohibición es contra derivar la tasa de la calidad; el mandato es derivarla del '
        'mercado, empresa por empresa. Corregido: las tasas de este documento van de '
        f'{pc(min(f["wacc"] for f in FILAS if f["wacc"]),2)} a {pc(max(f["wacc"] for f in FILAS if f["wacc"]),2)}.', 'cuerpo')]
    st += [M.p(
        '<b>Y expulsó tan mal como valoró.</b> 54 empresas del universo cayeron citando «ROIC por debajo del coste de '
        'capital», y ese coste de capital era el 9,70% inventado. Seis de ellas superan un WACC plausible con capital '
        'incremental que crea valor. Ocho más cayeron porque su ROIIC no era medible en una ventana de cuatro años — '
        'un hueco de dato, no una economía rota. Entre esas ocho están L\'Oréal y Linde.', 'cuerpo')]
    if gg and un:
        st += [M.p('<b>Lo que el motor corregido NO dice.</b> No produjo gangas. Las tres del piloto siguen caras y el '
        'abogado del diablo refutó los tres números — los agentes de senda salieron con optimismo sistemático medido. '
        'Lo que cambió es que ahora las razones son atacables una por una, con su filing al lado, en vez de ser una '
        'constante disfrazada de veredicto.', 'cuerpo')]
    return st + [PageBreak()]

# ─────────────────────────────────────────────────────────────────────
def defectos():
    st = M.flag_titulo('Los cinco defectos', 'Qué estaba roto, y qué lo sustituye')
    filas = [['#', 'Defecto del motor anterior', 'Corrección v3.1'],
      ['1', 'g∞ = 0% en 23 de 36 empresas. Con r=9,70% eso fija el múltiplo terminal en <b>10,3×</b> owner earnings para '
            'todas. La regla que lo asignaba no era económica sino de disponibilidad de dato: «0% cuando el ROIIC no es '
            'medible con la ventana de 4 años».',
            'g∞ = <b>PIB nominal de largo plazo</b> ponderado por la geografía de sus ingresos (~4,0-4,5% USD; ~2,8-3,2% '
            'EUR/CHF/GBP; ~2,2-2,6% JPY), con tope duro en r−2pp. Ninguna empresa crece más que su economía para siempre.'],
      ['2', 'r = 9,70% plana para las 36 (bono 4,70% + prima fija inventada 5,00%). Ningún agente calculó un WACC. '
            'Se aplicaba el candado B al revés.',
            '<b>WACC bottom-up por empresa, sin piso ni techo.</b> rf soberano de su moneda, ERP implícito de mercado '
            'fechado, prima de país por exposición de ingresos, beta = la menor entre sectorial re-apalancada y propia '
            'ajustada Blume, coste marginal de emitir hoy. Caja neta → WACC = coste del equity.'],
      ['3', 'Owner earnings = CFO − capex <b>TOTAL</b> − SBC. Castiga a quien construye activos y premia a quien los '
            'alquila: Nvidia es fabless y su capex de fábrica está en el balance de TSMC. Amazon salía con owner '
            'earnings negativos.',
            'Capex <b>separado en mantenimiento y crecimiento con evidencia</b> (capital incremental por dólar de ingreso, '
            'cruzado con divulgación y con depreciación de estado estacionario). Sólo el de mantenimiento resta. SBC '
            'como <b>dilución neta real</b>, no como gasto contable. Leases dentro de la deuda neta.'],
      ['4', 'g0 anclado en un punto del ciclo. Nvidia entró con <b>g0 = 83,4%</b>, «verificado al alza» sobre dos '
            'trimestres de pico de escasez. Nadie comprobó que la senda implicaba ingresos 2,7× los actuales.',
            '<b>DCF explícito a 10 años en tres tramos</b>: guía y backlog contratado (años 1-2), CAGR sostenible '
            'defendido contra capacidad y TAM (3-5), convergencia lineal a g∞ (6-10). Márgenes revirtiendo a media de '
            '7 años salvo defensa de filing. Y dos candados bloqueantes nuevos: <b>TAM</b> y <b>reinversión</b>.'],
      ['5', 'Margen de seguridad exigido de 25% / 30% / 40%. Con un motor que además infravaloraba, el doble filtro '
            'hacía imposible comprar nada: <b>0 de 36</b> pasaban.',
            'Recalibrado a <b>9% / 18% / 27%</b> — «comprar calidad a un precio justo». El candado A (veto bloqueante '
            'del abogado del diablo en sesión limpia) sigue obligatorio antes de toda compra: el margen más bajo no '
            'relaja ese veto.'],
    ]
    st += [M.tabla(filas, [0.8*cm, 7.7*cm, 8.1*cm], font_sz=7.9)]
    st += [M.callout('LECCIÓN TRANSFERIBLE',
        'Los cinco defectos se multiplicaban entre sí, y todos empujaban en la misma dirección. Por eso el resultado no '
        'parecía un error sino una opinión: un instrumento sesgado de forma consistente produce un veredicto coherente, '
        'y la coherencia se confunde con la verdad. La señal de alarma no fue una cifra concreta — fue que 34 de 36 '
        'empresas salieran caras y que la única barata fuera la de crecimiento más extremo.')]
    return st + [PageBreak()]

# ─────────────────────────────────────────────────────────────────────
def ranking_calidad():
    st = M.flag_titulo('Ranking de calidad', 'Ordinal 1-36 · durabilidad del mecanismo, sin precio dentro')
    st += [M.p('Este orden resiste el ruido: se validó con ρ=0,969 entre dos rondas independientes de ocho jueces '
        'ciegos. Es el único de los dos ejes que se publica ordenado — el de valor va en cubos, porque el ruido del '
        'instrumento no distingue entre vecinos.', 'nota')]
    for b in (1, 2, 3):
        sub = [f for f in FILAS if f['bloque'] == b]
        if not sub: continue
        st += [M.p(f'BLOQUE {b} — {BLQ[b]} · margen exigido {pc(sub[0]["margen_exigido"],0)}', 'h2')]
        filas = [['#', 'Empresa', 'Nvl', 'Mecanismo', 'Vector abierto']]
        for f in sub:
            filas.append([str(f['calidad_ordinal']),
                          f'<b>{e(f["ticker"])}</b><br/>{e(f["nombre"])}',
                          str(f['nivel_mecanismo']), e(f['mecanismo'])[:230], e(f['vector'])[:250]])
        st += [M.tabla(filas, [0.9*cm, 2.7*cm, 1.15*cm, 5.5*cm, 6.35*cm], font_sz=7.4)]
    return st + [PageBreak()]

# ─────────────────────────────────────────────────────────────────────
def cubos_valor():
    st = M.flag_titulo('El precio frente al valor', 'En cubos, nunca ordinal — el candado C lo prohíbe')
    st += [M.p('La cifra que decide no es el valor intrínseco: es <b>lo que el precio de hoy exige</b> frente a lo que '
        'el filing evidencia. No requiere creer en mi número. Cuando la caja de sensibilidad (±2pp de tasa, ±2pp de '
        'crecimiento en los años 3-5) hace que la empresa cruce de cara a barata, no se publica cifra puntual: se '
        'publica NO DECIDIBLE.', 'cuerpo')]
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'charts', 'exige_vs_evidencia.png')
    if os.path.exists(p): st += [M.chart(p, 16.6)]
    for c in CUBOS:
        sub = [f for f in FILAS if f['cubo'] == c]
        if not sub: continue
        sub.sort(key=lambda z: (z['premio'] if z['premio'] is not None else 99))
        st += [M.p(f'{c} — {len(sub)} de 36', 'h2')]
        filas = [['Empresa', 'Bl.', 'Precio', 'VI banda (US$)', 'Prima', 'Exige', 'Evid.', 'TIR', 'Gatillo']]
        for f in sub:
            filas.append([f'<b>{e(f["ticker"])}</b>', str(f['bloque']), usd(f['precio']),
                f'{usd(f["vi_bajista"])} · <b>{usd(f["vi_base"])}</b> · {usd(f["vi_alcista"])}',
                pc(f['premio'], 0, True), pc(f['exige']), pc(f['evidenciado']),
                pc(f['tir_10a']), usd(f['precio_gatillo'])])
        st += [M.tabla(filas, [2.2*cm, 0.8*cm, 1.8*cm, 4.5*cm, 1.7*cm, 1.5*cm, 1.4*cm, 1.3*cm, 1.6*cm], font_sz=7.6)]
    st += [M.p('«Exige» = CAGR de diez años que el precio de hoy necesita bajo el WACC propio de esa empresa. «Evid.» = '
        'el crecimiento que sostiene su filing. «Gatillo» = precio de entrada bajo la senda evidenciada y el margen de '
        'su bloque — no autoriza compra: el candado A sigue siendo bloqueante.', 'nota')]
    return st + [PageBreak()]

# ─────────────────────────────────────────────────────────────────────
def ficha(f):
    st = [M.p(f'{f["calidad_ordinal"]} · {e(f["nombre"])} <font size="10">({e(f["ticker"])})</font>', 'h_seccion')]
    st += [M.p(f'Bloque {f["bloque"]} · {BLQ[f["bloque"]]} · nivel {f["nivel_mecanismo"]} · '
               f'<b>{f["cubo"]}</b> · reporta en {e(f["moneda"])}', 'h_sub')]
    tab = [['Tasa (WACC bottom-up)', '', 'Flujo (owner earnings)', ''],
      ['WACC', f'<b>{pc(f["wacc"],2)}</b> <font size="7">(viejo 9,70%)</font>', 'OE normalizado', f'<b>{big(f["oe_normalizado"])}</b>'],
      ['rf + ERP + país', f'{pc(f["rf"],2)} + {pc(f["erp"],2)} + {pc(f["prima_pais"],2)}', 'OE mecánico viejo', big(f['oe_mecanico'])],
      ['Beta usada', f'{f["beta_usada"] if f["beta_usada"] else "—"} <font size="7">(sect. {f["beta_sector"]} / propia {f["beta_propia"]})</font>',
       'Capex mant. / crec.', f'{big(f["capex_mant"])} / {big(f["capex_crec"])}'],
      ['Coste equity / deuda', f'{pc(f["coste_equity"],2)} / {pc(f["coste_deuda"],2)}', '% capex crecimiento', pc(f['pct_capex_crecimiento'],0)],
      ['Caja neta', 'sí — WACC = Ke' if f['caja_neta'] else f'no · peso deuda {pc(f["peso_deuda"],0)}',
       'SBC gasto → dilución', f'{big(f["sbc_gasto"])} → {big(f["sbc_dilucion"])}'],
      ['g∞', f'<b>{pc(f["g_inf"],2)}</b> <font size="7">(viejo {pc(f["ginf_viejo"],2)})</font>', 'Margen norm. / últ.', f'{pc(f["margen_norm"])} / {pc(f["margen_ult"])}'],
      ['Múltiplo terminal', f'<b>{usd(f["multiplo_terminal"])}×</b> <font size="7">(viejo 10,3-13,4×)</font>', 'ROIIC histórico', pc(f['roiic_hist'])],
    ]
    st += [M.tabla(tab, [3.5*cm, 4.8*cm, 3.6*cm, 4.5*cm], font_sz=7.6)]
    ver = [['Precio', 'VI bajista', 'VI BASE', 'VI alcista', 'VI del diablo', 'Prima', 'TIR 10a'],
           [f'<b>{usd(f["precio"])}</b>', usd(f['vi_bajista']), f'<b>{usd(f["vi_base"])}</b>', usd(f['vi_alcista']),
            usd(f['vi_diablo']), f'<b>{pc(f["premio"],0,True)}</b>', pc(f['tir_10a'])]]
    st += [M.tabla(ver, [2.2*cm, 2.4*cm, 2.4*cm, 2.4*cm, 2.6*cm, 2.2*cm, 2.2*cm], font_sz=8.2)]
    st += [M.p(f'<b>DCF inverso.</b> El precio de hoy exige <b>{pc(f["exige"])}</b> anual durante diez años bajo un WACC '
        f'de {pc(f["wacc"],2)}. Lo evidenciado en filing es <b>{pc(f["evidenciado"])}</b>. '
        f'Brecha: {pc((f["exige"] or 0)-(f["evidenciado"] or 0),1,True)}.', 'cuerpo')]
    if f.get('tam_pasa') is not None:
        cuota = f'{pc(f["tam_cuota"],1)} de cuota implicada frente a un techo defendible de {pc(f["tam_cuota_max"],1)}'
        st += [M.p(f'<b>Candado TAM.</b> Ingresos implicados en el año 10: {big(f["tam_ingr10"])} — {cuota}. '
            + ('Pasa.' if f['tam_pasa'] else 'NO PASA.') + ' ' + e(f.get('tam_recorte'))[:420], 'cuerpo')]
    if f.get('reinv_pasa') is not None:
        st += [M.p(f'<b>Candado de reinversión.</b> La senda exige un ROIIC de {pc(f["roiic_implicado"])} frente al '
            f'{pc(f["roiic_hist"])} histórico. ' + ('Pasa.' if f['reinv_pasa'] else 'NO PASA — tesis DEGRADADA.'), 'cuerpo')]
    if f['ruido'] == 'NO DECIDIBLE':
        st += [M.callout('PAUSA REFLEXIVA', f'<b>NO DECIDIBLE.</b> Con ±2pp de tasa el valor va de '
            f'{usd(f["vi_wacc_mas2"])} a {usd(f["vi_wacc_menos2"])} US$ y cruza el veredicto. No se publica cifra '
            'puntual ni posición en el ranking de valor: el candado C lo prohíbe.')]
    if f.get('caso_bajista'):
        st += [M.p('El caso bajista, en sesión limpia', 'h3')]
        st += [M.p(e(f['caso_bajista'])[:1400], 'cuerpo')]
    if f.get('veredicto_diablo'):
        st += [M.callout('LECCIÓN TRANSFERIBLE', e(f['veredicto_diablo'])[:900])]
    if f.get('fuente_unica'):
        txt = ('Se halló segunda fuente primaria auditada: la cifra deja de estar degradada.'
               if f.get('segunda_fuente_hallada') else
               'NO se halló segunda fuente primaria auditada: <b>cifra DEGRADADA</b>, veredicto máximo VIGILAR.')
        st += [M.p(f'<b>Fuente única.</b> {txt}', 'nota')]
    return st + [PageBreak()]

def fichas():
    st = M.flag_titulo('Las 36, una por una', 'Monólogo evidenciado: tasa, flujo, senda, adversario')
    st += [M.p('Cada ficha lleva el WACC desglosado componente a componente, el owner earnings normalizado frente al '
        'mecánico anterior, los dos candados bloqueantes con sus números, y el caso bajista de un agente que trabajó '
        'en sesión limpia sin ver el razonamiento de los otros tres.', 'cuerpo'), PageBreak()]
    for f in FILAS: st += ficha(f)
    return st

# ─────────────────────────────────────────────────────────────────────
def comparativa():
    st = M.flag_titulo('Motor viejo contra motor nuevo', 'Empresa por empresa, cuánto movió la corrección')
    filas = [['Empresa', 'VI viejo', 'Prima vieja', 'VI v3.1', 'Prima nueva', 'Factor', 'g∞ viejo', 'g∞ nuevo', 'WACC']]
    for f in sorted(FILAS, key=lambda z: -(z['factor_vs_viejo'] or 0)):
        filas.append([f'<b>{e(f["ticker"])}</b>', usd(f['vi_viejo']), pc(f['premio_viejo'],0,True),
            usd(f['vi_base']), pc(f['premio'],0,True),
            f'<b>×{f["factor_vs_viejo"]}</b>' if f['factor_vs_viejo'] else '—',
            pc(f['ginf_viejo'],2), pc(f['g_inf'],2), pc(f['wacc'],2)])
    st += [M.tabla(filas, [2.3*cm, 1.9*cm, 2.0*cm, 1.9*cm, 2.1*cm, 1.6*cm, 1.6*cm, 1.6*cm, 1.6*cm], font_sz=7.6)]
    return st + [PageBreak()]

def knockouts():
    import csv as _c
    p = os.path.join(BASE, 'KnockOuts_contaminados_tasa_2026-08-26.csv')
    if not os.path.exists(p): return []
    rows = list(_c.DictReader(open(p)))
    st = M.flag_titulo('El instrumento también expulsó mal', 'Knock-outs ejecutados contra una tasa inventada')
    st += [M.p('54 empresas del universo cayeron citando «ROIC por debajo del coste de capital», y ese coste de capital '
        'era el 9,70% plano. Waste Management cayó con ROIC 8,2% cuando su WACC real bottom-up ronda el 6,5-7%. '
        'El triaje siguiente es una heurística de cribado (INFERENCIA, no HECHO): sirve para decidir a quién dedicar '
        'agentes, no para readmitir a nadie. La readmisión exige el agente de tasa por empresa.', 'cuerpo')]
    for grupo, tit in ((('True',), 'REABRIR — el ROIC supera un WACC plausible y el capital incremental crea valor'),
                       (('',), 'REVISAR — cayeron por ROIIC no medible en ventana de 4 años: hueco de dato, no economía'),
                       (('False',), 'MUERTAS DE VERDAD — el ROIIC negativo las mata con cualquier tasa')):
        sub = [r for r in rows if r['reabrir'] in grupo]
        if not sub: continue
        st += [M.p(tit, 'h2')]
        if grupo == ('False',):
            st += [M.p(', '.join(f'<b>{e(r["ticker"])}</b> ({pc(float(r["roic"]),1)})' for r in sub), 'cuerpo')]
        else:
            filas = [['Ticker', 'Entidad', 'ROIC', 'ROIIC', 'Brecha vs 9,70%']]
            for r in sub:
                ri = r['roiic']
                filas.append([f'<b>{e(r["ticker"])}</b>', e(r['entidad']), pc(float(r['roic']),1),
                              pc(float(ri),1) if ri else 'no medible', pc(float(r['brecha_vs_970']),1,True)])
            st += [M.tabla(filas, [2.0*cm, 7.0*cm, 2.2*cm, 2.6*cm, 2.8*cm], font_sz=7.8)]
    st += [M.callout('CASO HISTÓRICO',
        'Dos empresas cayeron del universo por la misma regla de disponibilidad de dato que fijaba g∞ = 0%: su ROIIC no '
        'era medible en una ventana de cuatro años. Son L\'Oréal y Linde. Un hueco de datos las echó de la lista, y de '
        'haber sobrevivido, el otro defecto las habría valorado a 10,3× su flujo. La pregunta de cierre de todo '
        'documento de este método — ¿qué pieza de información, si apareciera mañana, más cambiaría este veredicto? — '
        'aquí tiene respuesta incómoda: la pieza ya estaba, y era el propio motor.')]
    return st + [PageBreak()]

def limites():
    nd = [f['ticker'] for f in FILAS if f['cubo'] == 'NO DECIDIBLE']
    deg = [f['ticker'] for f in FILAS if f.get('fuente_unica') and f.get('sigue_degradada')]
    st = M.flag_titulo('Límites declarados', 'Lo que este documento no prueba')
    P = M.p
    st += [P('• <b>El candado B4 sigue CERRADO.</b> Nada de este documento es ejecutable como orden de compra. '
        'El veto bloqueante de <font face="Serif-B">abogado-diablo</font> en sesión limpia sigue siendo obligatorio '
        'antes de toda COMPRA, y el margen de seguridad más bajo (9/18/27%) no lo relaja: lo hace más necesario.', 'cuerpo')]
    if nd: st += [P(f'• <b>{len(nd)} empresas salieron NO DECIDIBLE</b> ({", ".join(nd)}): el ruido de la caja de '
        'sensibilidad supera la resolución del instrumento. No llevan cifra puntual ni posición en el cubo de valor.', 'cuerpo')]
    st += [P('• <b>La separación de capex entre mantenimiento y crecimiento es la corrección más discrecional de las '
        'cinco</b>, y es por donde volvería a colarse el sesgo. En Alphabet, la regresión contemporánea que el método '
        'exige falló (R²=0,13) porque el capex adelanta al ingreso 1-3 años; hubo que anclar en depreciación de estado '
        'estacionario. Cada ficha declara qué ruta usó.', 'cuerpo')]
    st += [P('• <b>El TAM casi nunca es un HECHO verificable en filing.</b> El candado que dio la vuelta a Nvidia '
        'descansa en la mejor estimación disponible, declarada como INFERENCIA. Es bloqueante y es discutible a la vez: '
        'esas dos cosas no se contradicen, pero hay que decirlas juntas.', 'cuerpo')]
    if deg: st += [P(f'• <b>Siguen con cifra DEGRADADA por fuente única</b> ({", ".join(deg)}): no se halló un segundo '
        'documento primario auditado que cruce las magnitudes que sostienen la valoración. Veredicto máximo VIGILAR.', 'cuerpo')]
    st += [P('• <b>Los agentes de senda salieron con optimismo sistemático medido.</b> El abogado del diablo refutó el '
        'número de los tres del piloto. Ese cuarto agente es lo único que impidió que este documento fuera el espejo '
        'del anterior: irrealmente optimista, el mismo error con el signo cambiado.', 'cuerpo')]
    st += [P('• <b>La venta de DUOL sigue ordenada sin ejecutar</b>, y el gate roto de MSFT del 29-jul sigue abierto. '
        'Se declaran aquí porque existe una caducidad vencida sin cerrar.', 'cuerpo')]
    st += [M.callout('CASO HISTÓRICO',
        'La lección que sobrevive a este documento no es sobre ninguna empresa. Es que un instrumento sesgado de forma '
        'consistente no se delata por parecer erróneo — se delata por parecer coherente. Durante un día entero, «34 de '
        '36 están caras» pasó por juicio de mercado en vez de por lo que era: dos números mal puestos, multiplicados '
        'entre sí, treinta y seis veces.')]
    return st
