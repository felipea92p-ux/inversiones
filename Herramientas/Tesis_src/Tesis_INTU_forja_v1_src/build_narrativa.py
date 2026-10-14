# -*- coding: utf-8 -*-
"""Ensamblador · ULTRA TESIS INTUIT (narrativa larga) → _Ultra Tesis/Tesis_Ultra_INTU_v1.pdf
Lee caps_intu.json (13 capítulos ya reordenados) y lo monta en el motor de la casa."""
import os, json, sys
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from pypdf import PdfReader
import motor_qg as M
from motor_qg import C

data = json.loads(open("caps_intu.json", encoding="utf-8").read())
CAPS = data["capitulos"]
TRANS = {t["id"]: t["frase"] for t in data.get("costura", {}).get("transiciones", [])}

M.configurar(
    titulo="INTUIT INC. (NASDAQ: INTU)",
    badge="ULTRA TESIS · INTU",
    pie="Ultra Tesis Quality Growth · uso personal · Intuit (INTU) · v1 (2026-07-13)",
    cabecera="ULTRA TESIS · TESIS-FORJA",
)

# ── estilos extra ──────────────────────────────────────────────────────────
ST_TRANS = ParagraphStyle("trans", fontName="Serif-I", fontSize=10, leading=14, textColor=C["gris"],
                          spaceBefore=2, spaceAfter=8)
ST_CITA = ParagraphStyle("cita", fontName="Serif-I", fontSize=11.5, leading=16.5, textColor=C["tinta"],
                         leftIndent=6, rightIndent=6)
ST_CITA_AUT = ParagraphStyle("cita_aut", fontName="Sans-B", fontSize=8.5, leading=11, textColor=C["rojo"],
                             leftIndent=6, spaceBefore=4)

TAGS = ["<b>", "</b>", "<i>", "</i>", "<br/>"]
def safe(t):
    if not t: return ""
    t = str(t)
    hold = {}
    for k, tag in enumerate(TAGS):
        h = f"\x00{k}\x00"; hold[h] = tag; t = t.replace(tag, h)
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for h, tag in hold.items(): t = t.replace(h, tag)
    return t

def cita(texto, autor=None):
    inner = [Paragraph(safe(texto), ST_CITA)]
    if autor: inner.append(Paragraph("— " + safe(autor), ST_CITA_AUT))
    body = Table([[x] for x in inner], colWidths=[14.8*cm])
    body.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),12),("RIGHTPADDING",(0,0),(-1,-1),10),
                              ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8)]))
    box = Table([["", body]], colWidths=[0.14*cm, 14.8*cm])
    box.setStyle(TableStyle([("BACKGROUND",(0,0),(0,-1),C["rojo"]),
                             ("BACKGROUND",(1,0),(1,-1),C["panel"]),
                             ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                             ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
                             ("VALIGN",(0,0),(-1,-1),"TOP")]))
    return KeepTogether([Spacer(1,6), box, Spacer(1,8)])

def render_tabla(b):
    enc = b.get("encabezados") or []
    filas = b.get("filas") or []
    if not enc and filas: enc, filas = filas[0], filas[1:]
    if not enc: return None
    ncol = len(enc)
    total = 16.2
    if ncol >= 3:
        w0 = total*0.30
        rest = (total-w0)/(ncol-1)
        widths = [w0] + [rest]*(ncol-1)
    else:
        widths = [total/ncol]*ncol
    tdata = [[safe(c) for c in enc]] + [[safe(c) for c in row] for row in filas]
    out = []
    if b.get("titulo_tabla"):
        out.append(M.p("<b>"+safe(b["titulo_tabla"])+"</b>", "h3"))
        out.append(Spacer(1,3))
    out.append(M.tabla(tdata, [w*cm for w in widths], font_sz=8.3))
    out.append(Spacer(1,6))
    return out

CALLOUT_OK = {"PAUSA REFLEXIVA","LECCIÓN TRANSFERIBLE","CASO HISTÓRICO"}
def render_bloque(b):
    tipo = b.get("tipo")
    if tipo == "parrafo":
        return [M.p(safe(b.get("texto","")), "cuerpo"), Spacer(1,3)]
    if tipo == "h2":
        return [Spacer(1,6), M.p(safe(b.get("texto","")), "h2"), Spacer(1,2)]
    if tipo == "callout":
        cl = b.get("clase") if b.get("clase") in CALLOUT_OK else "LECCIÓN TRANSFERIBLE"
        return [M.callout(cl, safe(b.get("texto","")))]
    if tipo == "cita":
        return [cita(b.get("texto",""), b.get("autor"))]
    if tipo == "tabla":
        r = render_tabla(b);  return r if r else []
    return [M.p(safe(b.get("texto","")), "cuerpo")]

CHART = {'apertura':'c7_colapso', 'premortem':'c4_patron', 'negocio':'c3_serie',
         'industria':'c5_comparativo', 'moat':None, 'numeros':'c6_roic',
         'gestion':None, 'percepcion':'c5_comparativo', 'valoracion':'c1_anclajes',
         'riesgos':'c4_patron', 'decision':'c2_zonas', 'temperamento':None, 'aprendizaje':'c2_zonas'}
USADOS = set()

# ── PORTADA ────────────────────────────────────────────────────────────────
def portada():
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=32, leading=35, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12.5, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13, leading=18, textColor=C["gris"])
    meta = ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])
    return [Spacer(1, 1.7*cm),
        Paragraph("INTUIT INC.", nombre),
        Paragraph("NASDAQ: INTU · El puente asediado", tick),
        Spacer(1,14),
        Paragraph("Cayó 64% desde su máximo — la peor acción del S&amp;P 500 en 2026. Y sin embargo es la única "
                  "de cuatro tesis de este sistema (junto a Visa, Mastercard y Microsoft) cuyo escenario "
                  "conservador propio da un margen de seguridad positivo. El precio de hoy exige apenas 4,5% "
                  "de crecimiento a diez años — la cifra más baja del sistema, muy por debajo de lo que Intuit "
                  "guía (13-14%) y de lo que ha demostrado hacer durante una década (16,7% compuesto). Esta no "
                  "es la pregunta de si el número es real (lo es); es la de si el riesgo que lo produjo — la "
                  "sustitución de TurboTax por inteligencia artificial, ya parcialmente confirmada por la "
                  "propia compañía — es transitorio o estructural.", tag),
        Spacer(1,20),
        M.kpi_panel([
            ("VIGILAR", "VEREDICTO · 0 %", "el máximo pesimismo exige la máxima cautela"),
            ("US$354", "VALOR CONSERVADOR", "vs US$290,00 hoy · margen +18,1% (base FY2025)"),
            ("≤US$266", "COMPRA INICIAL", "MoS≥25% · pendiente de resultados FY2026 (31-jul-2026)"),
        ]),
        Spacer(1,16), M.hr(),
        Paragraph("<b>13 de julio de 2026</b> &nbsp;·&nbsp; Un recorrido por los nueve pasos de una tesis de "
                  "convicción &nbsp;·&nbsp; Calidad 3,8/5 &nbsp;·&nbsp; Horizonte 5-10 años", meta),
        M.hr(),
        Paragraph("Documento de decisión y de aprendizaje del sistema <b>tesis-forja</b>. Forjado con "
                  "investigación multi-agente sobre fuentes primarias, templado por un loop de tres rondas "
                  "adversariales que retiró dos cifras fabricadas de una versión anterior. No es asesoría "
                  "financiera personalizada; la decisión final es de Felipe.", M.S["nota"]),
        NextPageTemplate("Normal"), PageBreak()]

# ── ensamblar ──────────────────────────────────────────────────────────────
def story():
    o = portada()
    for cap in CAPS:
        cid = cap.get("id","")
        o += M.flag_titulo(safe(cap.get("titulo","")), safe(cap.get("subtitulo","")))
        if cid in TRANS and cid != CAPS[0].get("id"):
            o += [Paragraph("<i>"+safe(TRANS[cid])+"</i>", ST_TRANS)]
        bloques = cap.get("bloques", [])
        chart_name = CHART.get(cid)
        if chart_name in USADOS:
            chart_name = None
        chart_at = max(0, len(bloques)-1) if chart_name else -1
        for i, b in enumerate(bloques):
            if i == chart_at and chart_name:
                try:
                    o += [Spacer(1,4), M.chart(f"charts/{chart_name}.png"), Spacer(1,6)]
                    USADOS.add(chart_name)
                except Exception: pass
            o += render_bloque(b)
        o += [PageBreak()]
    return o

OUT = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/"
       "INVESTMENTS/_Ultra Tesis/Tesis_Ultra_INTU_v1.pdf")
tmp = "/tmp/_intu_narr_pass1.pdf"
d1 = M.Doc(tmp); d1.build(story())
n = len(PdfReader(tmp).pages)
print("Pass 1:", n, "páginas")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
USADOS.clear()
d2 = M.Doc(OUT); d2.num_pages = n; d2.build(story())
print("PDF final:", OUT, f"({n} páginas)")
print("Nota del editor:", data.get("costura",{}).get("nota_global",""))
