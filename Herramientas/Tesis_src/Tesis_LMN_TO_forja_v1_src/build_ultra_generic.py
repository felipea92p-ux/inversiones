# -*- coding: utf-8 -*-
"""Ensamblador genérico · ULTRA TESIS (narrativa larga) → _Ultra Tesis/Tesis_Ultra_<T>_v1.pdf
Uso: python3 build_ultra_generic.py <caps.json> <chartdata.json> <out.pdf>"""
import os, json, sys
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from pypdf import PdfReader
import motor_qg as M
from motor_qg import C

CAPS_PATH, CD_PATH, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
data = json.load(open(CAPS_PATH, encoding="utf-8"))
cd = json.load(open(CD_PATH, encoding="utf-8"))
CAPS = data["capitulos"]
TRANS = {t["id"]: t["frase"] for t in (data.get("costura") or {}).get("transiciones", [])}
NOTA_GLOBAL = (data.get("costura") or {}).get("nota_global", "")

M.configurar(
    titulo=cd["nombre_corto"].upper() + " (" + cd["subtitulo_bolsa"] + ")",
    badge="ULTRA TESIS · " + cd["ticker"],
    pie="Ultra Tesis Quality Growth · uso personal · " + cd["ticker"] + " · v1 (2026-07-14)",
    cabecera="ULTRA TESIS · TESIS-FORJA",
)

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

CALLOUT_OK = {"PAUSA REFLEXIVA","LECCIÓN TRANSFERIBLE","CASO HISTÓRICO",
              "PAUSA REFLEXIVA","LECCION TRANSFERIBLE","CASO HISTORICO"}
NORMALIZA = {"LECCION TRANSFERIBLE":"LECCIÓN TRANSFERIBLE","CASO HISTORICO":"CASO HISTÓRICO"}
def render_bloque(b):
    tipo = b.get("tipo")
    if tipo == "parrafo":
        return [M.p(safe(b.get("texto","")), "cuerpo"), Spacer(1,3)]
    if tipo == "h2":
        return [Spacer(1,6), M.p(safe(b.get("texto","")), "h2"), Spacer(1,2)]
    if tipo == "callout":
        cl = b.get("clase","")
        cl = NORMALIZA.get(cl, cl)
        if cl not in {"PAUSA REFLEXIVA","LECCIÓN TRANSFERIBLE","CASO HISTÓRICO"}:
            cl = "LECCIÓN TRANSFERIBLE"
        return [M.callout(cl, safe(b.get("texto","")))]
    if tipo == "cita":
        return [cita(b.get("texto",""), b.get("autor"))]
    if tipo == "tabla":
        r = render_tabla(b);  return r if r else []
    return [M.p(safe(b.get("texto","")), "cuerpo")]

CHART = {'valoracion':'c1_anclajes', 'decision':'c2_zonas', 'percepcion':'c3_dcf'}
USADOS = set()

def portada():
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=30, leading=33, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12.5, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13, leading=18, textColor=C["gris"])
    meta = ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])
    return [Spacer(1, 1.7*cm),
        Paragraph(safe(cd["nombre_corto"].upper()), nombre),
        Paragraph(safe(cd["subtitulo_bolsa"] + " · " + cd.get("tagline","")), tick),
        Spacer(1,14),
        Paragraph(safe(cd["parrafo_portada"]), tag),
        Spacer(1,20),
        M.kpi_panel([
            (safe(cd["kpi1_valor"]), safe(cd["kpi1_etiqueta"]), safe(cd["kpi1_sub"])),
            (safe(cd["kpi2_valor"]), safe(cd["kpi2_etiqueta"]), safe(cd["kpi2_sub"])),
            (safe(cd["kpi3_valor"]), safe(cd["kpi3_etiqueta"]), safe(cd["kpi3_sub"])),
        ]),
        Spacer(1,16), M.hr(),
        Paragraph("<b>14 de julio de 2026</b> &nbsp;·&nbsp; Un recorrido por los nueve pasos de una tesis de "
                  "convicción &nbsp;·&nbsp; Calidad " + safe(cd.get("calidad","—")) + " &nbsp;·&nbsp; Horizonte 5-10 años", meta),
        M.hr(),
        Paragraph("Documento de decisión y de aprendizaje del sistema <b>tesis-forja</b>. Forjado con "
                  "investigación multi-agente sobre fuentes primarias y templado por revisión adversarial "
                  "multi-lente. No es asesoría financiera personalizada; la decisión final es de Felipe.", M.S["nota"]),
        NextPageTemplate("Normal"), PageBreak()]

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

tmp = "/tmp/_ultra_pass1_" + cd["ticker"].replace(".","_") + ".pdf"
d1 = M.Doc(tmp); d1.build(story())
n = len(PdfReader(tmp).pages)
print("Pass 1:", n, "paginas")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
USADOS.clear()
d2 = M.Doc(OUT); d2.num_pages = n; d2.build(story())
print("PDF final:", OUT, f"({n} paginas)")
if NOTA_GLOBAL: print("Nota del editor:", NOTA_GLOBAL)
