# -*- coding: utf-8 -*-
"""Ensamblador · ULTRA TESIS NARRATIVA LARGA — genérico por ticker.

Monta un caps_<ticker>.json (13 capítulos + costura) sobre el motor de la casa
y escribe el PDF en _Ultra Tesis/.

    python3 build_narrativa.py caps_intu.json
    python3 build_narrativa.py caps_intu.json --charts charts --out /ruta/salida.pdf

TODA la identidad del documento vive en el bloque "documento" del JSON.
Este archivo no contiene prosa ni datos de ninguna empresa — igual que motor_qg.py.

Contrato del JSON: ../references/narrativa-pdf.md

Historia: nació como build_narrativa.py de Visa (2026-07-11) y de Intuit
(2026-07-13), copiado a mano y con la identidad incrustada en el código. En la
versión de Intuit las 12 frases de costura NO salieron en el PDF: los ids de
`costura.transiciones` no coincidían con los de `capitulos`, y el `if cid in
TRANS` fallaba en silencio. De ahí que aquí toda discrepancia sea un error duro.
"""
import os, sys, json, argparse
from reportlab.platypus import (Spacer, PageBreak, NextPageTemplate, Paragraph,
                                Table, TableStyle, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from pypdf import PdfReader

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import motor_qg as M
from motor_qg import C

RAIZ = os.environ.get("QG_INVESTMENTS") or os.path.expanduser(
    "~/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS")

CALLOUT_OK = {"PAUSA REFLEXIVA", "LECCIÓN TRANSFERIBLE", "CASO HISTÓRICO"}
BLOQUES_OK = {"parrafo", "h2", "callout", "cita", "tabla"}
META_DEFECTO = ["Un recorrido por los nueve pasos de una tesis de convicción"]


# ── validación ─────────────────────────────────────────────────────────────
class ErrorContrato(SystemExit):
    def __init__(self, fallos):
        cuerpo = "\n".join(f"  · {f}" for f in fallos)
        super().__init__(
            f"\nERROR DE CONTRATO · {len(fallos)} fallo(s) en el JSON\n{cuerpo}\n\n"
            "Contrato: Skills/tesis-forja/references/narrativa-pdf.md\n")


def validar(data, dir_charts):
    """Revienta ante cualquier discrepancia. Nada de degradar en silencio."""
    f = []

    doc = data.get("documento")
    if not isinstance(doc, dict):
        raise ErrorContrato(["falta el bloque 'documento' (¿JSON de la era pre-genérica?)"])
    for k in ("ticker", "empresa", "mercado", "version", "fecha_larga", "tagline", "entradilla"):
        if not doc.get(k):
            f.append(f"documento.{k} vacío o ausente")
    kpis = doc.get("kpis") or []
    if len(kpis) != 3:
        f.append(f"documento.kpis debe tener exactamente 3 entradas (tiene {len(kpis)})")
    for i, k in enumerate(kpis):
        if not (isinstance(k, (list, tuple)) and len(k) == 3):
            f.append(f"documento.kpis[{i}] debe ser [valor, ETIQUETA, subnota]")

    caps = data.get("capitulos") or []
    if not caps:
        f.append("'capitulos' vacío")
    ids, vistos = [], set()
    for i, c in enumerate(caps):
        cid = c.get("id")
        if not cid:
            f.append(f"capitulos[{i}] sin 'id'")
            continue
        if cid in vistos:
            f.append(f"id de capítulo duplicado: '{cid}'")
        vistos.add(cid)
        ids.append(cid)
        if not c.get("titulo"):
            f.append(f"capítulo '{cid}' sin 'titulo'")
        bloques = c.get("bloques")
        if not bloques:
            f.append(f"capítulo '{cid}' sin bloques")
            continue
        for j, b in enumerate(bloques):
            t = b.get("tipo")
            if t not in BLOQUES_OK:
                f.append(f"'{cid}'.bloques[{j}]: tipo '{t}' desconocido "
                         f"(válidos: {', '.join(sorted(BLOQUES_OK))})")
            elif t == "callout" and b.get("clase") not in CALLOUT_OK:
                f.append(f"'{cid}'.bloques[{j}]: callout.clase '{b.get('clase')}' inválida "
                         f"(válidas: {', '.join(sorted(CALLOUT_OK))})")
            elif t == "tabla" and not (b.get("encabezados") or b.get("filas")):
                f.append(f"'{cid}'.bloques[{j}]: tabla sin 'encabezados' ni 'filas'")
            elif t in ("parrafo", "h2", "cita") and not b.get("texto"):
                f.append(f"'{cid}'.bloques[{j}]: '{t}' sin 'texto'")

    # ── el bug de INTU: ids de costura que no casan con ningún capítulo ──
    for t in (data.get("costura") or {}).get("transiciones", []):
        tid = t.get("id")
        if tid not in vistos:
            f.append(f"costura: id '{tid}' no corresponde a ningún capítulo. "
                     f"Debe ser uno de: {', '.join(ids)}")
        if not t.get("frase"):
            f.append(f"costura['{tid}'] sin 'frase'")

    # ── gráficos: id válido + png existente (antes se tragaba el fallo) ──
    for cid, nombre in (data.get("graficos") or {}).items():
        if cid not in vistos:
            f.append(f"graficos: '{cid}' no corresponde a ningún capítulo")
        if nombre and not os.path.isfile(os.path.join(dir_charts, f"{nombre}.png")):
            f.append(f"graficos['{cid}']: no existe {dir_charts}/{nombre}.png")

    if f:
        raise ErrorContrato(f)


# ── helpers de render ──────────────────────────────────────────────────────
TAGS = ["<b>", "</b>", "<i>", "</i>", "<br/>"]


def safe(t):
    if not t:
        return ""
    t = str(t)
    hold = {}
    for k, tag in enumerate(TAGS):
        h = f"\x00{k}\x00"; hold[h] = tag; t = t.replace(tag, h)
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for h, tag in hold.items():
        t = t.replace(h, tag)
    return t


def _estilos():
    return {
        "trans": ParagraphStyle("trans", fontName="Serif-I", fontSize=10, leading=14,
                                textColor=C["gris"], spaceBefore=2, spaceAfter=8),
        "cita": ParagraphStyle("cita", fontName="Serif-I", fontSize=11.5, leading=16.5,
                               textColor=C["tinta"], leftIndent=6, rightIndent=6),
        "cita_aut": ParagraphStyle("cita_aut", fontName="Sans-B", fontSize=8.5, leading=11,
                                   textColor=C["rojo"], leftIndent=6, spaceBefore=4),
    }


def cita(texto, autor, ST):
    inner = [Paragraph(safe(texto), ST["cita"])]
    if autor:
        inner.append(Paragraph("— " + safe(autor), ST["cita_aut"]))
    body = Table([[x] for x in inner], colWidths=[14.8 * cm])
    body.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 12),
                              ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                              ("TOPPADDING", (0, 0), (-1, -1), 8),
                              ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    box = Table([["", body]], colWidths=[0.14 * cm, 14.8 * cm])
    box.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, -1), C["rojo"]),
                             ("BACKGROUND", (1, 0), (1, -1), C["panel"]),
                             ("LEFTPADDING", (0, 0), (-1, -1), 0),
                             ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                             ("TOPPADDING", (0, 0), (-1, -1), 0),
                             ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                             ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    return KeepTogether([Spacer(1, 6), box, Spacer(1, 8)])


def render_tabla(b, ancho_col1=0.30):
    enc = b.get("encabezados") or []
    filas = b.get("filas") or []
    if not enc and filas:
        enc, filas = filas[0], filas[1:]
    ncol, total = len(enc), 16.2
    if ncol >= 3:
        w0 = total * ancho_col1
        widths = [w0] + [(total - w0) / (ncol - 1)] * (ncol - 1)
    else:
        widths = [total / ncol] * ncol
    tdata = [[safe(c) for c in enc]] + [[safe(c) for c in row] for row in filas]
    out = []
    if b.get("titulo_tabla"):
        out += [M.p("<b>" + safe(b["titulo_tabla"]) + "</b>", "h3"), Spacer(1, 3)]
    out += [M.tabla(tdata, [w * cm for w in widths], font_sz=8.3), Spacer(1, 6)]
    return out


def render_bloque(b, ST, ancho_col1):
    tipo = b.get("tipo")
    if tipo == "parrafo":
        return [M.p(safe(b.get("texto", "")), "cuerpo"), Spacer(1, 3)]
    if tipo == "h2":
        return [Spacer(1, 6), M.p(safe(b.get("texto", "")), "h2"), Spacer(1, 2)]
    if tipo == "callout":
        return [M.callout(b["clase"], safe(b.get("texto", "")))]
    if tipo == "cita":
        return [cita(b.get("texto", ""), b.get("autor"), ST)]
    if tipo == "tabla":
        return render_tabla(b, ancho_col1)
    return []


def portada(doc, ST):
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=doc.get("tam_nombre", 32),
                            leading=doc.get("tam_nombre", 32) + 3, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12.5, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=13, leading=18, textColor=C["gris"])
    meta = ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])
    sep = " &nbsp;·&nbsp; "
    linea_meta = f"<b>{safe(doc['fecha_larga'])}</b>" + sep + sep.join(
        safe(s) for s in (doc.get("meta") or META_DEFECTO))
    return [
        Spacer(1, 1.7 * cm),
        Paragraph(safe(doc["empresa"]), nombre),
        Paragraph(f"{safe(doc['mercado'])}: {safe(doc['ticker'])} · {safe(doc['tagline'])}", tick),
        Spacer(1, 14),
        Paragraph(safe(doc["entradilla"]), tag),
        Spacer(1, 20),
        M.kpi_panel([tuple(k) for k in doc["kpis"]]),
        Spacer(1, 16), M.hr(),
        Paragraph(linea_meta, meta),
        M.hr(),
        Paragraph(safe(doc.get("nota", "")), M.S["nota"]),
        NextPageTemplate("Normal"), PageBreak()]


def construir_story(data, dir_charts):
    """Story completa. Estado local: se puede llamar dos veces sin contaminarse."""
    ST = _estilos()
    doc = data["documento"]
    caps = data["capitulos"]
    trans = {t["id"]: t["frase"] for t in (data.get("costura") or {}).get("transiciones", [])}
    graficos = data.get("graficos") or {}
    ancho_col1 = doc.get("ancho_col1", 0.30)

    o = portada(doc, ST)
    usados = set()
    for n, cap in enumerate(caps):
        cid = cap["id"]
        o += M.flag_titulo(safe(cap["titulo"]), safe(cap.get("subtitulo", "")))
        if n > 0 and cid in trans:
            o += [Paragraph("<i>" + safe(trans[cid]) + "</i>", ST["trans"])]
        bloques = cap["bloques"]
        grafico = graficos.get(cid)
        if grafico in usados:
            grafico = None
        pos = max(0, len(bloques) - 1) if grafico else -1
        for i, b in enumerate(bloques):
            if i == pos and grafico:
                o += [Spacer(1, 4), M.chart(os.path.join(dir_charts, f"{grafico}.png")), Spacer(1, 6)]
                usados.add(grafico)
            o += render_bloque(b, ST, ancho_col1)
        o += [PageBreak()]
    return o


# ── main ───────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description="Ensambla una Ultra Tesis narrativa desde caps_<ticker>.json")
    ap.add_argument("caps", help="ruta al caps_<ticker>.json")
    ap.add_argument("--charts", default=None, help="carpeta de PNGs (defecto: charts/ junto al JSON)")
    ap.add_argument("--out", default=None, help="PDF de salida (defecto: documento.salida o derivado)")
    a = ap.parse_args()

    base = os.path.dirname(os.path.abspath(a.caps))
    dir_charts = a.charts or os.path.join(base, "charts")
    with open(a.caps, encoding="utf-8") as fh:
        data = json.load(fh)

    validar(data, dir_charts)
    doc = data["documento"]

    salida = a.out or doc.get("salida") or \
        f"_Ultra Tesis/Tesis_Ultra_{doc['ticker']}_{doc['version']}.pdf"
    if not os.path.isabs(salida):
        salida = os.path.join(RAIZ, salida)

    M.configurar(
        titulo=f"{doc['empresa']} ({doc['mercado']}: {doc['ticker']})",
        badge=f"ULTRA TESIS · {doc['ticker']}",
        pie=(f"Ultra Tesis Quality Growth · uso personal · {doc.get('empresa_corta', doc['empresa'])} "
             f"({doc['ticker']}) · {doc['version']} ({doc.get('fecha', doc['fecha_larga'])})"),
        cabecera=doc.get("cabecera", "ULTRA TESIS · TESIS-FORJA"),
    )

    tmp = os.path.join("/tmp", f"_narr_{doc['ticker']}_pass1.pdf")
    M.Doc(tmp).build(construir_story(data, dir_charts))
    n = len(PdfReader(tmp).pages)
    print(f"Pase 1: {n} páginas")

    os.makedirs(os.path.dirname(salida), exist_ok=True)
    d2 = M.Doc(salida)
    d2.num_pages = n
    d2.build(construir_story(data, dir_charts))

    caps = data["capitulos"]
    trans = (data.get("costura") or {}).get("transiciones", [])
    print(f"PDF final: {salida} ({n} páginas)")
    print(f"  capítulos: {len(caps)} · costuras: {len(trans)} · "
          f"gráficos: {sum(1 for v in (data.get('graficos') or {}).values() if v)}")
    nota = (data.get("costura") or {}).get("nota_global")
    if nota:
        print(f"Nota del editor: {nota}")


if __name__ == "__main__":
    main()
