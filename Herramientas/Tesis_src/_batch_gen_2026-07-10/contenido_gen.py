# -*- coding: utf-8 -*-
"""Parametric Ultra Tesis contenido builder. Given a merged company dict (numbers, both axes)
and a narrative dict (prose sections), returns a story() list of flowables in the house style.
Focused-but-complete depth: portada, resumen, cuadro de mando, negocio, moat+radar, calidad,
gestion, riesgos, valoracion+charts, nueve inversores, premortem, cierre."""
from reportlab.platypus import Spacer, PageBreak, NextPageTemplate, Paragraph
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
import motor_qg as M
from motor_qg import C

RULES = ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11"]
RULE_NAME = {
 "R1":"Escalabilidad","R2":"Industria","R3":"Liderazgo","R4":"Moat","R5":"Crec. orgánico",
 "R6":"Diversificación","R7":"ROIC / capital","R8":"Balance","R9":"Cuentas","R10":"Gestión","R11":"Impacto"}
RMAX = {"R1":15,"R3":15,"R4":15}

def _es(x, d=1):
    try:
        return f"{x:.{d}f}".replace(".", ",")
    except Exception:
        return str(x)

def sp(h=6):
    return Spacer(1, h)

def paras(txt, style="cuerpo"):
    """Split a prose block on double newline into paragraphs."""
    out = []
    for blk in str(txt).split("\n\n"):
        blk = blk.strip()
        if blk:
            out.append(M.p(blk, style))
    return out

def build_story(cd, nar, chartsdir="charts"):
    ck = cd["ck"]
    v = cd["val"]
    ccy = v["price_ccy"]
    price = v["price_today"]
    pwfv = v["pwfv"]
    zone = v["zone"]
    ver = v["veredicto"]
    mos = v["mos_actual_pct"]
    mos_ex = v["mos_exigido_pct"]
    disc = v["price_vs_pwfv_pct"]  # positive = prima
    # margin label: mos actual is negative when overpriced
    mos_lbl = f"{_es(mos,1)}%"

    def ch(name, w=16.4):
        return M.chart(f"{chartsdir}/{name}.png", w)

    story = []

    # ── PORTADA ──
    nombre = ParagraphStyle("nm", fontName="Serif-B", fontSize=30, leading=33, textColor=C["tinta"])
    tick = ParagraphStyle("tk", fontName="Sans-B", fontSize=12, leading=16, textColor=C["rojo"])
    tag = ParagraphStyle("tg", fontName="Serif-I", fontSize=12, leading=16.5, textColor=C["gris"])
    meta = ParagraphStyle("meta", fontName="Serif", fontSize=9.5, leading=13, textColor=C["tinta"])
    fn = ParagraphStyle("fn", fontName="Serif-I", fontSize=8, leading=11, textColor=C["gris"])
    zona_txt = f"vs {ccy} {_es(price,0)} hoy · zona {zone}"
    if disc >= 0:
        margen_val = f"&minus;{_es(abs(disc),0)}%"; margen_lbl = "PRIMA sobre VALOR"
    else:
        margen_val = f"+{_es(abs(disc),0)}%"; margen_lbl = "MARGEN vs VALOR"
    story += [Spacer(1, 1.9*cm),
        Paragraph(cd["name"].upper(), nombre),
        Paragraph(f"{cd['exchange']} &nbsp;·&nbsp; {cd['sector']}", tick),
        sp(12),
        Paragraph(nar["tagline"], tag),
        sp(18),
        M.kpi_panel([
            (f"{_es(cd['qg_score'],1)}/100", "CALIDAD QG", f"tier {cd['qg_tier']}"),
            (f"{ccy} {_es(pwfv,0)}", "VALOR (PWFV)", zona_txt),
            (margen_val, margen_lbl, f"MoS {mos_lbl} → {ver}"),
        ]),
        sp(14), M.hr(),
        Paragraph(f"<b>10 de julio de 2026</b> &nbsp;·&nbsp; Precio {ccy} {_es(price,2)} &nbsp;·&nbsp; "
                  f"Horizonte 5–10 años &nbsp;·&nbsp; Tesis Ultra nueva (candidato Top 30 QG)", meta),
        M.hr(),
        Paragraph("Eje CALIDAD (sistema qg-seilern de 11 reglas, re-verificado adversarialmente el 10-jul-2026) "
                  "y eje PRECIO (val-mos: detector de trampas, PWFV, DCF inverso, MoS por tier, candados) "
                  "calculados por separado y cruzados solo al final. Uso personal; no es asesoría de inversión "
                  "registrada.", fn),
        NextPageTemplate("Normal"), PageBreak()]

    # ── RESUMEN ──
    story += M.flag_titulo("Resumen en treinta segundos", "La pregunta operativa, los dos ejes y un veredicto")
    story += paras(nar["resumen"])
    # quick scorecard mini-table
    story += [sp(4), M.tabla([
        ["Eje", "Resultado", "Lectura"],
        ["CALIDAD (qg-seilern)", f"{_es(cd['qg_score'],1)}/100 · {cd['qg_tier']}", "qué tan buen negocio es"],
        ["PRECIO (val-mos)", f"zona {zone} · MoS {mos_lbl} vs {int(mos_ex)}% exigido", "si el precio de hoy da margen"],
        ["VEREDICTO", ver, f"gatillo de compra ~{ccy} {_es(v['buy_trigger_price'],0)}"],
    ], [4.6*cm, 6.6*cm, 5.2*cm], font_sz=8.4)]
    story += [PageBreak()]

    # ── CUADRO DE MANDO ──
    story += M.flag_titulo("Cuadro de mando", "Estado, detector y triggers falsables")
    det = v["detector_veredicto"]
    story += [M.tabla([
        ["Bloque", "Estado"],
        ["Tier de calidad (congelado)", f"{cd['qg_tier']} — {_es(cd['qg_score'],1)}/100"],
        ["Detector de trampas de valor", f"{det}"],
        ["DCF inverso (g implícito)", f"{_es(v['dcf_inverse_g_implied_pct'],1)}% → {v['dcf_inverse_class']}"],
        ["Múltiplo owner earnings", f"{_es(v['multiple_owner_earnings'],1)}x"],
        ["Zona de precio", f"{zone} (prima/descuento {_es(disc,1)}% vs PWFV)"],
        ["Asimetría riesgo/beneficio", v["asimetria"][:120]],
        ["Veredicto val-mos", ver],
    ], [5.6*cm, 10.8*cm], font_sz=8.4)]
    story += [sp(4), M.p("<b>Trigger falsable (precio + KPI).</b>", "h3")]
    story += paras(v["falsable"])
    story += [PageBreak()]

    # ── NEGOCIO ──
    story += M.flag_titulo("El negocio", "Cómo gana dinero, de dónde viene y dónde está parado")
    story += paras(nar["negocio"])
    story += [PageBreak()]

    # ── MOAT + radar ──
    story += M.flag_titulo("El foso", "Naturaleza y durabilidad de la ventaja competitiva")
    story += paras(nar["moat"])
    story += [sp(6), ch(f"radar_{ck}"), sp(4)]
    story += [PageBreak()]

    # ── CALIDAD ──
    story += M.flag_titulo("Eje calidad · las once reglas", f"Por qué {_es(cd['qg_score'],1)}/100 y tier {cd['qg_tier']}")
    story += paras(nar["calidad"])
    # 11-rule table
    filas = [["Regla", "Nota", "Regla", "Nota"]]
    half = 6
    left = RULES[:6]; right = RULES[6:]
    for i in range(6):
        lr = left[i]
        lcell = f"{lr} {RULE_NAME[lr]}"
        lval = f"{_es(cd['qg_scores'][lr],1)}/{RMAX.get(lr,10)}"
        if i < len(right):
            rr = right[i]
            rcell = f"{rr} {RULE_NAME[rr]}"; rval = f"{_es(cd['qg_scores'][rr],1)}/{RMAX.get(rr,10)}"
        else:
            rcell = ""; rval = ""
        filas.append([lcell, lval, rcell, rval])
    story += [sp(4), M.tabla(filas, [5.4*cm, 2.0*cm, 5.4*cm, 2.0*cm], font_sz=8.2)]
    story += [M.callout("PAUSA REFLEXIVA",
        "Este score mide <b>CALIDAD</b> del negocio, no valoración ni margen de seguridad. Score alto "
        "&ne; comprar — el eje precio se resuelve aparte, en la sección de valoración.")]
    story += [PageBreak()]

    # ── GESTION ──
    story += M.flag_titulo("Gestión y asignación de capital", "Track record, alineación e incentivos")
    story += paras(nar["gestion"])
    story += [PageBreak()]

    # ── RIESGOS ──
    story += M.flag_titulo("Riesgos y cómo se vería el deterioro", "Lo que rompería la tesis")
    story += paras(nar["riesgos"])
    tr = nar.get("top_riesgos") or []
    if tr:
        filas = [["#", "Riesgo estructural"]]
        for i, r in enumerate(tr, 1):
            filas.append([str(i), r])
        story += [sp(4), M.tabla(filas, [1.0*cm, 15.4*cm], font_sz=8.4)]
    story += [PageBreak()]

    # ── VALORACION + charts ──
    story += M.flag_titulo("Eje valoración · precio vs valor", f"PWFV {ccy} {_es(pwfv,0)} · zona {zone} · {ver}")
    story += paras(nar["valoracion"])
    story += [sp(6), ch(f"dcf_{ck}"), sp(6), ch(f"zonas_{ck}"), sp(4)]
    story += [M.p(f"<b>Owner earnings.</b> {v['owner_earnings_note']}", "nota")]
    story += [PageBreak()]

    # ── NUEVE INVERSORES ──
    story += M.flag_titulo("El panel de los nueve", "Cómo votaría cada superinversor ante este caso")
    story += paras(nar["inversores"])
    il = nar.get("inversor_lineas") or []
    if il:
        filas = [["Inversor", "Veredicto"]]
        for line in il:
            if ":" in line:
                who, verd = line.split(":", 1)
                filas.append([who.strip(), verd.strip()])
            else:
                filas.append(["", line])
        story += [sp(4), M.tabla(filas, [3.4*cm, 13.0*cm], font_sz=8.4)]
    story += [PageBreak()]

    # ── PRE-MORTEM ──
    story += M.flag_titulo("Pre-mortem y triggers", "Si esta tesis fracasa en cinco años, ¿por qué?")
    story += paras(nar["premortem"])
    story += [PageBreak()]

    # ── CIERRE ──
    story += M.flag_titulo("Qué queda por saber", "La pieza que más cambiaría el veredicto")
    story += paras(nar["cierre"])
    story += [sp(6), M.p("Documento de uso personal — no constituye asesoría de inversión registrada. "
        "Los dos ejes (CALIDAD vía qg-seilern · VALORACIÓN vía val-mos) se calcularon por separado y solo "
        "se cruzan en el veredicto final. Un score de calidad alto no es una orden de compra.", "nota")]

    return story
