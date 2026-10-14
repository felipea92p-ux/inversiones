# -*- coding: utf-8 -*-
"""
MAKE CHARTS · TESIS ULTRA DUOL v4
Genera los 17 PNGs (dpi=150) para la tesis Economist-style de Duolingo.
Carga data/charts_spec.json y usa chart_style + paleta_qg.

Nombres de salida EXACTOS (charts/):
  c_radar, c_ew, c_colapso, c_ingresos_fcf, c_dau, c_decel, c_moat,
  c_matriz, c_fuerzas, c_tam, c_dcf, c_zonas, c_sens, c_mgmt,
  c_inversores, c_riesgos, c_proy

Ejecutar:  cd Tesis_DUOL_v4_src && python3 make_charts_duol.py
"""
import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from matplotlib.colors import LinearSegmentedColormap

import chart_style as CS
from paleta_qg import PALETA as P

# Trata '$' como literal en TODO texto (evita el parser mathtext con dobles '$')
plt.rcParams["text.parse_math"] = False

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC_PATH = os.path.join(HERE, "data", "charts_spec.json")
with open(SPEC_PATH, encoding="utf-8") as f:
    SPEC = json.load(f)

FUENTE = ("Fuente: filings DUOL, carta accionistas Q1 FY26, "
          "sistema QG-Seilern + val-mos. Elaboración propia.")

FIGSIZE = (7.2, 4.2)


def coma(x, dec=1):
    """Formatea número con coma decimal española."""
    return f"{x:.{dec}f}".replace(".", ",")


# ---------------------------------------------------------------------
# 1. c_radar
# ---------------------------------------------------------------------
def c_radar():
    d = SPEC["radar_11_reglas"]
    ejes = d["ejes"]
    n = len(ejes)
    labels = [f"{e['regla']}\n{e['nombre'].split('/')[0]}" for e in ejes]
    scores = [e["score"] for e in ejes]
    maxes = [e["max"] for e in ejes]

    ang = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    ang += ang[:1]
    sc = scores + scores[:1]
    mx = maxes + maxes[:1]

    fig = plt.figure(figsize=FIGSIZE)
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 16)

    ax.plot(ang, mx, color=P["azul_cielo"], lw=1.1, ls="--", alpha=0.9,
            label="Máximo por regla")
    ax.fill(ang, sc, color=P["azul"], alpha=0.28)
    ax.plot(ang, sc, color=P["azul"], lw=2.0, label="Score DUOL")

    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(labels, fontsize=7.0, color=P["tinta"])
    ax.set_yticks([5, 10, 15])
    ax.set_yticklabels(["5", "10", "15"], fontsize=6.5, color=P["gris"])
    ax.grid(color=P["gris_linea"], lw=0.6, alpha=0.9)
    ax.spines["polar"].set_color(P["gris_linea"])
    ax.legend(loc="upper right", bbox_to_anchor=(1.16, 1.12), fontsize=7,
              frameon=False)

    fig.subplots_adjust(top=0.78, bottom=0.08, left=0.06, right=0.88)
    CS.deco(ax,
            "Radar QG-Seilern · DUOL 80,8/100 (Alta convicción)",
            "11 reglas de calidad: score (azul) contra el máximo alcanzable (línea discontinua)",
            FUENTE, fig=fig)
    CS.save(fig, "c_radar")


# ---------------------------------------------------------------------
# 2. c_ew
# ---------------------------------------------------------------------
def c_ew():
    d = SPEC["early_warning"]
    kpis = d["kpis"]
    color_estado = {
        "verde": P["verde"],
        "ambar": P["ocre"],
        "rojo": P["rojo_oscuro"],
        "gris_no_divulgado": P["gris"],
        "gris": P["gris"],
    }
    txt_estado = {
        "verde": "VERDE", "ambar": "ÁMBAR", "rojo": "ROJO",
        "gris_no_divulgado": "N/D", "gris": "N/D",
    }

    n = len(kpis)
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, n)
    ax.axis("off")

    row_h = 1.0
    for i, k in enumerate(kpis):
        y = n - 1 - i
        est = k["estado"]
        col = color_estado.get(est, P["gris"])
        if i % 2 == 0:
            ax.add_patch(Rectangle((0, y), 100, row_h, color=P["panel"],
                                   alpha=0.55, zorder=0))
        ax.text(1.5, y + row_h / 2, k["kpi"], va="center", ha="left",
                fontsize=7.2, color=P["tinta"], zorder=2)
        ax.text(64, y + row_h / 2, k["valor_actual"], va="center", ha="left",
                fontsize=6.9, color=P["gris"], zorder=2)
        ax.add_patch(Rectangle((90.5, y + 0.18), 8.5, row_h - 0.36,
                               color=col, zorder=2))
        ax.text(94.75, y + row_h / 2, txt_estado.get(est, "N/D"),
                va="center", ha="center", fontsize=6.2, color="white",
                fontweight="bold", zorder=3)

    ax.text(1.5, n + 0.12, "KPI", fontsize=7.2, ha="left",
            color=P["azul_noche"], fontweight="bold")
    ax.text(64, n + 0.12, "VALOR ACTUAL", fontsize=7.2, ha="left",
            color=P["azul_noche"], fontweight="bold")
    ax.text(94.75, n + 0.12, "ESTADO", fontsize=7.2, ha="center",
            color=P["azul_noche"], fontweight="bold")

    fig.subplots_adjust(top=0.80, bottom=0.06, left=0.02, right=0.98)
    CS.deco(ax,
            "Cuadro Early-Warning · semáforo de KPIs",
            "Disparador maestro: bookings cc < +3% dos trimestres seguidos = tesis falsada",
            FUENTE, fig=fig)
    CS.save(fig, "c_ew")


# ---------------------------------------------------------------------
# 3. c_colapso
# ---------------------------------------------------------------------
def c_colapso():
    d = SPEC["colapso_precio_multiplo"]
    serie = d["serie_precio"]
    fechas = [s["fecha"] for s in serie]
    precios = [s["precio"] for s in serie]
    x = list(range(len(serie)))

    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.plot(x, precios, color=P["azul"], lw=2.0, marker="o", ms=5,
            mfc=P["azul"], mec=P["fondo"], zorder=3)

    ax.scatter([x[0]], [precios[0]], s=70, color=P["rojo_oscuro"], zorder=4)
    ax.annotate(f"ATH {coma(precios[0], 2)}", (x[0], precios[0]),
                xytext=(6, -4), textcoords="offset points",
                fontsize=7.5, color=P["rojo_oscuro"], fontweight="bold")
    ax.scatter([x[-1]], [precios[-1]], s=70, color=P["tinta"], zorder=4)
    ax.annotate(f"HOY {coma(precios[-1], 2)}", (x[-1], precios[-1]),
                xytext=(-8, 16), textcoords="offset points",
                fontsize=7.5, color=P["tinta"], fontweight="bold", ha="right")

    for i in (1, 2, 3):
        s = serie[i]
        ax.annotate(s["hito"], (x[i], precios[i]),
                    xytext=(8, 12), textcoords="offset points",
                    fontsize=6.4, color=P["gris"],
                    arrowprops=dict(arrowstyle="-", color=P["gris_linea"],
                                    lw=0.7))

    ax.set_xticks(x)
    ax.set_xticklabels([f[:7] for f in fechas], fontsize=7, color=P["gris"])
    ax.set_ylabel("Precio (US$)", fontsize=8)
    ax.set_ylim(0, 600)

    caja = "Compresión de múltiplo\nP/S  30x  ->  7,9x\nfwd P/E  130x  ->  48x"
    ax.text(0.62, 0.60, caja, transform=ax.transAxes, fontsize=7.4,
            color=P["tinta"], va="top", ha="left",
            bbox=dict(boxstyle="round,pad=0.5", fc=P["panel"],
                      ec=P["gris_linea"], lw=0.8))

    fig.subplots_adjust(top=0.80, bottom=0.12, left=0.10, right=0.97)
    CS.deco(ax,
            "El -77% es de-rating de MÚLTIPLO, no de fundamentales",
            "Precio de US$544,93 (ATH) a US$125,76 (HOY) mientras ingresos y FCF subían",
            FUENTE, fig=fig)
    CS.save(fig, "c_colapso")


# ---------------------------------------------------------------------
# 4. c_ingresos_fcf
# ---------------------------------------------------------------------
def c_ingresos_fcf():
    d = SPEC["ingresos_fcf_historico"]
    anios = d["anios"]
    rev = d["revenue_m"]
    fcf = d["fcf_m"]
    x = np.arange(len(anios))
    w = 0.38

    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.bar(x - w / 2, rev, w, color=P["azul"], label="Ingresos (US$M)")
    ax.bar(x + w / 2, fcf, w, color=P["verde"], label="FCF (US$M)")

    for xi, v in zip(x - w / 2, rev):
        ax.text(xi, v + 12, f"{v:,.0f}".replace(",", "."), ha="center",
                fontsize=6.8, color=P["azul"])
    for xi, v in zip(x + w / 2, fcf):
        ax.text(xi, v + 12, f"{v:,.0f}".replace(",", "."), ha="center",
                fontsize=6.8, color=P["verde"])

    ax.set_xticks(x)
    ax.set_xticklabels(anios, fontsize=8)
    ax.set_ylabel("US$ millones", fontsize=8)
    ax.set_ylim(0, 1150)
    ax.legend(loc="upper left", fontsize=7.5, frameon=False)

    fig.subplots_adjust(top=0.80, bottom=0.10, left=0.10, right=0.97)
    CS.deco(ax,
            "Ingresos y FCF FY21-FY25",
            "ingresos +40%/año mientras la acción cayó -77%",
            FUENTE, fig=fig)
    CS.save(fig, "c_ingresos_fcf")


# ---------------------------------------------------------------------
# 5. c_dau
# ---------------------------------------------------------------------
def c_dau():
    d = SPEC["dau_paid_historico"]
    st = d["series_trimestrales"]
    dau = st["dau_m"][0]
    mau = st["mau_m"][0]
    paid = st["paid_subs_m"][0]
    pen = st["penetracion_pagada_pct"][0]

    cats = ["MAU", "DAU", "Pagos"]
    vals = [mau, dau, paid]
    cols = [P["azul_cielo"], P["azul"], P["verde"]]

    fig, ax = plt.subplots(figsize=FIGSIZE)
    bars = ax.bar(cats, vals, width=0.55, color=cols)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 2, f"{coma(v)} M",
                ha="center", fontsize=8, color=P["tinta"], fontweight="bold")

    ax.set_ylabel("Millones de usuarios", fontsize=8)
    ax.set_ylim(0, 155)

    ax.text(0.98, 0.62,
            f"Penetración pagada\n{coma(pen)}%  (pagos / MAU)",
            transform=ax.transAxes, ha="right", va="top", fontsize=8,
            color=P["tinta"],
            bbox=dict(boxstyle="round,pad=0.5", fc=P["panel"],
                      ec=P["gris_linea"], lw=0.8))
    ax.text(0.98, 0.36,
            "Nota: DUOL no divulga serie\nhistórica de cohortes / ARPU / churn.",
            transform=ax.transAxes, ha="right", va="top", fontsize=6.8,
            style="italic", color=P["gris"])

    fig.subplots_adjust(top=0.80, bottom=0.10, left=0.10, right=0.97)
    CS.deco(ax,
            "Engagement en máximos · Q1 FY26",
            "DAU +21% e/e, suscriptores pagos +21%, penetración pagada 9,1%",
            FUENTE, fig=fig)
    CS.save(fig, "c_dau")


# ---------------------------------------------------------------------
# 6. c_decel
# ---------------------------------------------------------------------
def c_decel():
    rev_g = SPEC["ingresos_fcf_historico"]["revenue_growth_pct"]
    anios = SPEC["ingresos_fcf_historico"]["anios"]

    periodos = anios + ["Q1 FY26", "FY26 GUÍA", "Q2 FY26 GUÍA"]
    bookings = [None] * 5 + [14, 10.5, 5.8]
    revenue = list(rev_g) + [27, 16.1, None]
    es_guia = [False] * 5 + [False, True, True]

    x = np.arange(len(periodos))
    w = 0.38

    fig, ax = plt.subplots(figsize=(7.6, 4.2))

    def fmt(v):
        return (coma(v, 0) if float(v).is_integer() else coma(v)) + "%"

    for xi in range(len(periodos)):
        v = revenue[xi]
        if v is None:
            continue
        g = es_guia[xi]
        off = w / 2 if bookings[xi] is not None else 0
        ax.bar(xi + off, v, w, color=P["azul"],
               hatch="//" if g else None,
               edgecolor=P["fondo"] if g else "none")
        ax.text(xi + off, v + 0.8, fmt(v), ha="center", fontsize=6.6,
                color=P["azul"])

    for xi in range(len(periodos)):
        v = bookings[xi]
        if v is None:
            continue
        g = es_guia[xi]
        ax.bar(xi - w / 2, v, w, color=P["rojo_oscuro"],
               hatch="//" if g else None,
               edgecolor=P["fondo"] if g else "none")
        ax.text(xi - w / 2, v + 0.8, fmt(v), ha="center", fontsize=6.6,
                color=P["rojo_oscuro"])

    for xi in range(len(periodos)):
        if es_guia[xi]:
            ax.text(xi, -4.5, "GUÍA", ha="center", fontsize=6.2,
                    color=P["gris"], style="italic")

    ax.set_xticks(x)
    ax.set_xticklabels(periodos, fontsize=6.8)
    ax.set_ylabel("Crecimiento interanual (%)", fontsize=8)
    ax.set_ylim(0, 60)

    leg = [
        Line2D([0], [0], marker="s", color="none", markerfacecolor=P["azul"],
               markersize=8, label="Revenue / ingresos (rezagado)"),
        Line2D([0], [0], marker="s", color="none",
               markerfacecolor=P["rojo_oscuro"], markersize=8,
               label="Bookings (adelantado)"),
    ]
    ax.legend(handles=leg, loc="upper right", fontsize=7, frameon=False)

    fig.subplots_adjust(top=0.80, bottom=0.16, left=0.09, right=0.97)
    CS.deco(ax,
            "La señal bajista: bookings (adelantado) desacelera bajo revenue (rezagado)",
            "Histórico = crecimiento de ingresos; Q1 FY26 reportado; FY26 y Q2 FY26 son GUÍA de la compañía",
            FUENTE, fig=fig)
    CS.save(fig, "c_decel")


# ---------------------------------------------------------------------
# 7. c_moat
# ---------------------------------------------------------------------
def c_moat():
    capas = [
        ("Marca / búho (Duo)", 3, P["azul_cielo"]),
        ("Gamificación-hábito (conductual)", 8, P["azul"]),
        ("Librería + datos / test A-B", 6, P["azul_acero"]),
        ("Efectos de red / DET", 4, P["verde"]),
    ]
    capas_sorted = sorted(capas, key=lambda c: c[1])
    labels = [c[0] for c in capas_sorted]
    anios = [c[1] for c in capas_sorted]
    cols = [c[2] for c in capas_sorted]
    y = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=FIGSIZE)
    bars = ax.barh(y, anios, color=cols, height=0.62)
    for b, v in zip(bars, anios):
        ax.text(v + 0.15, b.get_y() + b.get_height() / 2, f"{v} años",
                va="center", fontsize=8, color=P["tinta"], fontweight="bold")

    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=7.6)
    ax.set_xlabel("Años estimados de defensa", fontsize=8)
    ax.set_xlim(0, 10)
    ax.grid(axis="x", color=P["gris_linea"], lw=0.6, alpha=0.9)

    fig.subplots_adjust(top=0.80, bottom=0.13, left=0.28, right=0.95)
    CS.deco(ax,
            "El foso conductual es ortogonal al contenido",
            "La IA comoditiza el contenido; el hábito gamificado (racha, notificaciones) es lo que la IA no replica",
            FUENTE, fig=fig)
    CS.save(fig, "c_moat")


# ---------------------------------------------------------------------
# 8. c_matriz
# ---------------------------------------------------------------------
def c_matriz():
    comp = [
        ("Duolingo", 9.5, 9.3, 10),
        ("Babbel", 5.5, 5.0, 6),
        ("Busuu", 4.2, 4.5, 4),
        ("Rosetta Stone", 4.8, 3.2, 5),
        ("Memrise", 3.5, 4.0, 3),
        ("Pimsleur", 3.0, 3.5, 3),
        ("Tutor IA (ChatGPT/Gemini)", 8.5, 2.8, 8),
    ]
    fig, ax = plt.subplots(figsize=FIGSIZE)
    for nombre, ex, ey, marca in comp:
        if nombre == "Duolingo":
            col = P["azul"]
        elif "IA" in nombre:
            col = P["rojo_oscuro"]
        else:
            col = P["azul_acero"]
        ax.scatter(ex, ey, s=marca * 60, color=col, alpha=0.75,
                   edgecolor=P["fondo"], lw=1.0, zorder=3)
        dy = 0.55 if nombre != "Tutor IA (ChatGPT/Gemini)" else -0.95
        va = "bottom" if dy > 0 else "top"
        ax.text(ex, ey + dy, nombre, ha="center", va=va, fontsize=6.8,
                color=P["tinta"], zorder=4)

    ax.set_xlim(0, 11)
    ax.set_ylim(0, 11)
    ax.set_xlabel("Escala / distribución  ->", fontsize=8)
    ax.set_ylabel("Engagement / hábito  ->", fontsize=8)
    ax.grid(color=P["gris_linea"], lw=0.6, alpha=0.9)
    ax.axhline(6, color=P["gris_linea"], lw=0.6, ls=":")
    ax.axvline(6, color=P["gris_linea"], lw=0.6, ls=":")
    ax.text(10.6, 10.6, "Dominante", ha="right", va="top", fontsize=7,
            style="italic", color=P["gris"])

    fig.subplots_adjust(top=0.80, bottom=0.12, left=0.09, right=0.97)
    CS.deco(ax,
            "Posicionamiento competitivo · la burbuja = fuerza de marca",
            "Duolingo domina arriba-derecha; el tutor IA tiene escala pero engagement bajo (sin hábito)",
            FUENTE, fig=fig)
    CS.save(fig, "c_matriz")


# ---------------------------------------------------------------------
# 9. c_fuerzas
# ---------------------------------------------------------------------
def c_fuerzas():
    d = SPEC["cinco_fuerzas"]
    fuerzas = d["fuerzas"]
    total = d["total"]
    mx = d["max"]

    def corto(nombre):
        return nombre.split("(")[0].strip()
    labels = [corto(f["fuerza"]) for f in fuerzas]
    vals = [f["valor"] for f in fuerzas]

    n = len(fuerzas)
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    ang += ang[:1]
    v = vals + vals[:1]

    fig = plt.figure(figsize=FIGSIZE)
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 5)

    ax.fill(ang, v, color=P["rojo_oscuro"], alpha=0.22)
    ax.plot(ang, v, color=P["rojo_oscuro"], lw=2.0)

    ax.scatter([ang[0]], [vals[0]], s=90, color=P["rojo"], zorder=5)
    ax.annotate("Sustitutos IA = 5", (ang[0], vals[0]),
                xytext=(6, 6), textcoords="offset points",
                fontsize=7.2, color=P["rojo"], fontweight="bold")

    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(labels, fontsize=6.8, color=P["tinta"])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=P["gris"])
    ax.grid(color=P["gris_linea"], lw=0.6, alpha=0.9)
    ax.spines["polar"].set_color(P["gris_linea"])

    fig.subplots_adjust(top=0.78, bottom=0.08, left=0.10, right=0.90)
    CS.deco(ax,
            "Cinco Fuerzas de Porter · presión competitiva",
            f"Mayor = más presión; total {total}/{mx}; la amenaza de sustitutos IA domina el marco",
            FUENTE, fig=fig)
    CS.save(fig, "c_fuerzas")


# ---------------------------------------------------------------------
# 10. c_tam
# ---------------------------------------------------------------------
def c_tam():
    d = SPEC["tam_sam_som"]
    capas = d["capas"]
    niveles = [c["nivel"] for c in capas]
    vals = [c["valor_usd_b"] for c in capas]
    etiq = [c["etiqueta"] for c in capas]
    cols = [P["azul_cielo"], P["azul_acero"], P["azul"]]

    fig, ax = plt.subplots(figsize=FIGSIZE)
    maxv = max(vals)
    y_positions = [2, 1, 0]
    for y, niv, v, et, col in zip(y_positions, niveles, vals, etiq, cols):
        left = (maxv - v) / 2
        ax.add_patch(Rectangle((left, y - 0.35), v, 0.7, color=col, zorder=3))
        ax.text(maxv / 2, y, f"{niv}   US$ {coma(v)} B",
                ha="center", va="center", fontsize=8.5, color="white",
                fontweight="bold", zorder=4)
        ax.text(maxv / 2, y - 0.30, et, ha="center", va="top",
                fontsize=6.6, color=P["gris"], zorder=4)

    ax.set_xlim(-2, maxv + 2)
    ax.set_ylim(-0.7, 2.6)
    ax.axis("off")

    fig.subplots_adjust(top=0.80, bottom=0.06, left=0.04, right=0.96)
    CS.deco(ax,
            "Embudo de mercado · TAM -> SAM -> SOM",
            "Mercado online de idiomas 2030 (US$54,8 B) hasta captura DUOL de década (US$3,4 B)",
            FUENTE, fig=fig)
    CS.save(fig, "c_tam")


# ---------------------------------------------------------------------
# 11. c_dcf
# ---------------------------------------------------------------------
def c_dcf():
    d = SPEC["dcf_3_escenarios"]
    esc = d["escenarios"]
    precio = d["precio_actual"]
    ponderado = d["valor_ponderado_dcf"]
    nombres = [e["nombre"] for e in esc]
    valores = [e["valor_accion"] for e in esc]
    probs = [e["prob"] for e in esc]
    cols = [P["rojo_oscuro"], P["azul"], P["verde"]]

    x = np.arange(len(esc))
    fig, ax = plt.subplots(figsize=FIGSIZE)
    bars = ax.bar(x, valores, width=0.55, color=cols)
    for b, v, pr in zip(bars, valores, probs):
        ax.text(b.get_x() + b.get_width() / 2, v + 4, f"US$ {v}",
                ha="center", fontsize=8, color=P["tinta"], fontweight="bold")
        ax.text(b.get_x() + b.get_width() / 2, v / 2,
                f"{int(round(pr * 100))}%", ha="center", va="center",
                fontsize=8.5, color="white", fontweight="bold")

    ax.axhline(ponderado, color=P["rojo"], lw=1.6, ls="--", zorder=4)
    ax.text(len(esc) - 0.55, ponderado + 3, f"Ponderado {ponderado}",
            fontsize=7.2, color=P["rojo"], ha="right")
    ax.axhline(precio, color=P["tinta"], lw=1.6, ls="-", zorder=4)
    ax.text(-0.45, precio + 3, f"HOY {coma(precio, 2)}", fontsize=7.2,
            color=P["tinta"], ha="left")

    ax.set_xticks(x)
    ax.set_xticklabels(nombres, fontsize=8)
    ax.set_ylabel("Valor por acción (US$)", fontsize=8)
    ax.set_ylim(0, 250)

    ax.text(0.02, 0.94, "Nota: PWFV honesto ~140 (Base honesto g~7-8%)",
            transform=ax.transAxes, fontsize=6.8, style="italic",
            color=P["gris"], va="top")

    fig.subplots_adjust(top=0.80, bottom=0.10, left=0.10, right=0.97)
    CS.deco(ax,
            "DCF owner earnings · valor por acción a 3 escenarios",
            "Conservador / Base / Optimista con probabilidades; precio HOY muy por debajo del ponderado",
            FUENTE, fig=fig)
    CS.save(fig, "c_dcf")


# ---------------------------------------------------------------------
# 12. c_zonas
# ---------------------------------------------------------------------
def c_zonas():
    d = SPEC["mapa_zonas"]
    precio = d["precio_actual"]
    pwfv = d["pwfv_valor"]
    pwfv_h = d["pwfv_honesto"]
    epv = d["epv_floor"]
    pt = d["pt_consenso"]
    gatillo = d["precio_mos25_sobre_140"]

    x0, x1 = 70, 240
    fig, ax = plt.subplots(figsize=(7.6, 3.6))

    bandas = [
        (70, 80, P["verde"], "GANGA"),
        (115, 130, P["azul_cielo"], "OPORTUNIDAD"),
        (130, 176, P["ocre"], "PRECIO JUSTO"),
        (191, 240, P["rojo_oscuro"], "CARO"),
    ]
    yb, hb = 0.35, 0.30
    for lo, hi, col, nombre in bandas:
        ax.add_patch(Rectangle((lo, yb), hi - lo, hb, color=col, alpha=0.55,
                               zorder=2))
        ax.text((lo + hi) / 2, yb + hb / 2, nombre, ha="center", va="center",
                fontsize=7.0, color=P["tinta"], fontweight="bold", zorder=3)

    ax.plot([x0, x1], [yb, yb], color=P["gris_linea"], lw=1.0, zorder=1)

    marcadores = [
        (epv, "EPV 80", P["verde"], "up"),
        (pt, f"PT consenso {coma(pt, 0)}", P["gris"], "down"),
        (gatillo, f"Gatillo tramo {gatillo}", P["rojo"], "up"),
        (precio, f"HOY {coma(precio, 2)}", P["tinta"], "down"),
        (pwfv_h, f"PWFV honesto {pwfv_h}", P["azul"], "up"),
        (pwfv, f"PWFV {pwfv}", P["azul_noche"], "down"),
    ]
    for val, lab, col, direc in marcadores:
        if direc == "up":
            ax.plot([val, val], [yb + hb, yb + hb + 0.10], color=col, lw=1.4,
                    zorder=4)
            ax.scatter([val], [yb + hb + 0.10], s=28, color=col, zorder=5)
            ax.text(val, yb + hb + 0.14, lab, ha="center", va="bottom",
                    fontsize=6.6, color=col, fontweight="bold")
        else:
            ax.plot([val, val], [yb - 0.10, yb], color=col, lw=1.4, zorder=4)
            ax.scatter([val], [yb - 0.10], s=28, color=col, zorder=5)
            ax.text(val, yb - 0.14, lab, ha="center", va="top",
                    fontsize=6.6, color=col, fontweight="bold")

    for tick in range(80, 241, 20):
        ax.text(tick, yb - 0.30, str(tick), ha="center", va="top",
                fontsize=6.2, color=P["gris"])
    ax.text((x0 + x1) / 2, yb - 0.40, "Precio por acción (US$)", ha="center",
            va="top", fontsize=7.2, color=P["gris"])

    ax.set_xlim(x0 - 4, x1 + 4)
    ax.set_ylim(-0.10, 1.05)
    ax.axis("off")

    fig.subplots_adjust(top=0.80, bottom=0.04, left=0.03, right=0.97)
    CS.deco(ax,
            "Zonas de valoración — HOY en la frontera OPORTUNIDAD/PRECIO JUSTO",
            "EPV suelo 80 · gatillo de tramo 105 · HOY 125,76 · PWFV honesto 140 · PWFV 153",
            FUENTE, fig=fig)
    CS.save(fig, "c_zonas")


# ---------------------------------------------------------------------
# 13. c_sens
# ---------------------------------------------------------------------
def c_sens():
    d = SPEC["sensibilidad_wacc_terminal"]
    waccs = d["wacc_pct"]
    growths = d["growth_oe_pct"]
    matriz = d["matriz_valor_accion"]
    precio = d["precio_actual"]

    M = np.zeros((len(waccs), len(growths)))
    for i, w in enumerate(waccs):
        row = next(r for r in matriz if abs(r["wacc"] - w) < 1e-6)
        M[i, 0] = row["g6"]
        M[i, 1] = row["g8"]
        M[i, 2] = row["g10"]

    cmap = LinearSegmentedColormap.from_list(
        "warm", [P["fondo"], P["ocre"], P["azul"]])

    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    ax.imshow(M, cmap=cmap, aspect="auto", origin="upper")

    ax.set_xticks(range(len(growths)))
    ax.set_xticklabels([f"{g}%" for g in growths], fontsize=8)
    ax.set_yticks(range(len(waccs)))
    ax.set_yticklabels([f"{coma(w)}%" for w in waccs], fontsize=8)
    ax.set_xlabel("Crecimiento owner earnings", fontsize=8)
    ax.set_ylabel("WACC", fontsize=8)

    vmin, vmax = M.min(), M.max()
    for i in range(len(waccs)):
        for j in range(len(growths)):
            val = M[i, j]
            tcol = "white" if val > (vmin + vmax) / 2 else P["tinta"]
            ax.text(j, i, f"{int(val)}", ha="center", va="center",
                    fontsize=10, color=tcol, fontweight="bold")

    def cell(wacc, g):
        return growths.index(g), waccs.index(wacc)
    jb, ib = cell(8.5, 10)
    ax.add_patch(Rectangle((jb - 0.5, ib - 0.5), 1, 1, fill=False,
                           edgecolor=P["rojo"], lw=2.4, zorder=5))
    ax.text(jb, ib + 0.34, "BASE", ha="center", va="center", fontsize=6.2,
            color=P["rojo"], fontweight="bold", zorder=6)
    jh, ih = cell(8.5, 8)
    ax.add_patch(Rectangle((jh - 0.5, ih - 0.5), 1, 1, fill=False,
                           edgecolor=P["tinta"], lw=2.0, ls="--", zorder=5))
    ax.text(jh, ih + 0.34, "HONESTO", ha="center", va="center", fontsize=6.0,
            color=P["tinta"], fontweight="bold", zorder=6)

    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)

    fig.subplots_adjust(top=0.80, bottom=0.12, left=0.12, right=0.97)
    CS.deco(ax,
            "Sensibilidad del valor por acción · WACC x crecimiento OE",
            f"Base (8,5%; 10%) = US$175 · Honesto (8,5%; 8%) = US$154 · precio HOY US${coma(precio, 0)}",
            FUENTE, fig=fig)
    CS.save(fig, "c_sens")


# ---------------------------------------------------------------------
# 14. c_mgmt
# ---------------------------------------------------------------------
def c_mgmt():
    d = SPEC["management_radar"]
    dims = d["dimensiones"]

    def corto(nombre):
        return nombre.split("(")[0].strip()
    labels = [corto(x["dim"]) for x in dims]
    vals = [x["valor"] for x in dims]

    n = len(dims)
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    ang += ang[:1]
    v = vals + vals[:1]

    fig = plt.figure(figsize=FIGSIZE)
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 5)

    ax.fill(ang, v, color=P["azul"], alpha=0.26)
    ax.plot(ang, v, color=P["azul"], lw=2.0)
    for a, val in zip(ang[:-1], vals):
        ax.text(a, val + 0.30, str(val), ha="center", va="center",
                fontsize=7, color=P["azul_noche"], fontweight="bold")

    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(labels, fontsize=6.5, color=P["tinta"])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=P["gris"])
    ax.grid(color=P["gris_linea"], lw=0.6, alpha=0.9)
    ax.spines["polar"].set_color(P["gris_linea"])

    fig.subplots_adjust(top=0.78, bottom=0.08, left=0.14, right=0.86)
    CS.deco(ax,
            "Gestión y gobernanza · R10 neto 7/10",
            "Fundadores con skin-in-the-game y ejecución fuerte; lastre en gobernanza dual-class y SBC",
            FUENTE, fig=fig)
    CS.save(fig, "c_mgmt")


# ---------------------------------------------------------------------
# 15. c_inversores
# ---------------------------------------------------------------------
def c_inversores():
    data = [
        ("Graham", "PASS", 2),
        ("Buffett", "HOLD", 3),
        ("Munger", "HOLD", 3),
        ("Fisher", "BUY", 4),
        ("Lynch", "HOLD", 3),
        ("Templeton", "BUY", 3),
        ("Marks", "HOLD", 3),
        ("Seilern", "HOLD", 3),
        ("Smith", "HOLD", 3),
    ]
    col_verd = {"BUY": P["verde"], "HOLD": P["ocre"], "PASS": P["rojo_oscuro"]}

    data_rev = list(reversed(data))
    nombres = [n for n, _, _ in data_rev]
    convicc = [c for _, _, c in data_rev]
    veredictos = [v for _, v, _ in data_rev]
    cols = [col_verd[v] for v in veredictos]
    y = np.arange(len(data_rev))

    fig, ax = plt.subplots(figsize=FIGSIZE)
    bars = ax.barh(y, convicc, color=cols, height=0.62)
    for b, v, ver in zip(bars, convicc, veredictos):
        ax.text(v + 0.08, b.get_y() + b.get_height() / 2, f"{ver} · {v}/5",
                va="center", fontsize=7.2, color=P["tinta"])

    ax.set_yticks(y)
    ax.set_yticklabels(nombres, fontsize=7.8)
    ax.set_xlabel("Convicción (1-5)", fontsize=8)
    ax.set_xlim(0, 5.6)
    ax.grid(axis="x", color=P["gris_linea"], lw=0.6, alpha=0.9)

    leg = [
        Line2D([0], [0], marker="s", color="none", markerfacecolor=P["verde"],
               markersize=8, label="BUY"),
        Line2D([0], [0], marker="s", color="none", markerfacecolor=P["ocre"],
               markersize=8, label="HOLD"),
        Line2D([0], [0], marker="s", color="none",
               markerfacecolor=P["rojo_oscuro"], markersize=8, label="PASS"),
    ]
    ax.legend(handles=leg, loc="lower right", fontsize=7, frameon=False, ncol=3)

    fig.subplots_adjust(top=0.80, bottom=0.12, left=0.12, right=0.95)
    CS.deco(ax,
            "Nueve inversores · consenso HOLD con divergencia en los bordes",
            "Fisher y Templeton compran el crecimiento; Graham pasa por precio/gobernanza",
            FUENTE, fig=fig)
    CS.save(fig, "c_inversores")


# ---------------------------------------------------------------------
# 16. c_riesgos
# ---------------------------------------------------------------------
def c_riesgos():
    d = SPEC["riesgos_heatmap"]
    riesgos = d["riesgos"]

    fig, ax = plt.subplots(figsize=(7.4, 4.4))

    ax.add_patch(Rectangle((3.5, 3.5), 2.0, 2.0, color=P["rojo_oscuro"],
                           alpha=0.14, zorder=0))
    ax.add_patch(Rectangle((0.5, 0.5), 5, 5, fill=False,
                           edgecolor=P["gris_linea"], lw=0.8, zorder=0))

    for r in riesgos:
        px, py = r["prob"], r["impacto"]
        sev = px * py
        if sev >= 16:
            col = P["rojo_oscuro"]
        elif sev >= 9:
            col = P["ocre"]
        else:
            col = P["verde"]
        ax.scatter(px, py, s=520, color=col, alpha=0.85, zorder=3,
                   edgecolor=P["fondo"], lw=1.2)
        ax.text(px, py, r["id"].replace("R-", ""), ha="center", va="center",
                fontsize=8, color="white", fontweight="bold", zorder=4)

    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel("Probabilidad  ->", fontsize=8)
    ax.set_ylabel("Impacto  ->", fontsize=8)
    ax.grid(color=P["gris_linea"], lw=0.5, alpha=0.7)
    ax.text(5.4, 5.4, "Zona crítica", ha="right", va="top", fontsize=7,
            style="italic", color=P["rojo_oscuro"])

    leyenda = "\n".join(f"{r['id']}  {r['riesgo'][:40]}" for r in riesgos)
    ax.text(1.03, 0.5, leyenda, transform=ax.transAxes, fontsize=6.0,
            va="center", ha="left", color=P["gris"], family="DejaVu Sans")

    fig.subplots_adjust(top=0.80, bottom=0.12, left=0.07, right=0.60)
    CS.deco(ax,
            "Mapa de calor de riesgos · probabilidad x impacto",
            "Los riesgos de disrupción IA y de-rating de valoración cargan la esquina crítica",
            FUENTE, fig=fig)
    CS.save(fig, "c_riesgos")


# ---------------------------------------------------------------------
# 17. c_proy
# ---------------------------------------------------------------------
def c_proy():
    d = SPEC["proyeccion_5y"]
    precio = d["precio_actual"]
    pwfv_h = d["pwfv_honesto"]
    gatillo = d["gatillo_tramo1"]
    epv = d["suelo_condicional_epv"]
    esc = d["escenarios"]

    anios = [2026, 2027, 2028, 2029, 2030, 2031]
    x = np.arange(len(anios))

    def path(central_2031, lo_2031, hi_2031):
        central = np.linspace(precio, central_2031, len(anios))
        lo = np.linspace(precio, lo_2031, len(anios))
        hi = np.linspace(precio, hi_2031, len(anios))
        return central, lo, hi

    estilos = {
        "Bajista": P["rojo_oscuro"],
        "Base": P["azul"],
        "Alcista": P["verde"],
    }

    fig, ax = plt.subplots(figsize=FIGSIZE)
    for e in esc:
        col = estilos[e["nombre"]]
        lo, hi = e["rango_2031"]
        central, plo, phi = path(e["central_2031"], lo, hi)
        ax.fill_between(x, plo, phi, color=col, alpha=0.14, zorder=1)
        ax.plot(x, central, color=col, lw=2.0, zorder=3,
                label=f"{e['nombre']} ({int(round(e['prob'] * 100))}%)")
        ax.text(x[-1] + 0.08, central[-1], f"{e['central_2031']}",
                fontsize=7.2, color=col, va="center", fontweight="bold")

    ax.axhline(pwfv_h, color=P["rojo"], lw=1.4, ls="--", zorder=2)
    ax.text(0.05, pwfv_h + 4, f"PWFV honesto {pwfv_h}", fontsize=6.8,
            color=P["rojo"])
    ax.axhline(epv, color=P["verde"], lw=1.0, ls=":", zorder=2)
    ax.text(0.05, epv + 4, f"Suelo EPV {epv}", fontsize=6.8, color=P["verde"])

    ax.scatter([0], [precio], s=55, color=P["tinta"], zorder=5)
    ax.text(0.05, precio - 12, f"HOY {coma(precio, 2)}", fontsize=6.8,
            color=P["tinta"], fontweight="bold")
    ax.scatter([0], [gatillo], s=45, color=P["rojo"], zorder=5)
    ax.text(0.05, gatillo - 12, f"Gatillo tramo1 {gatillo}", fontsize=6.6,
            color=P["rojo"])

    ax.set_xticks(x)
    ax.set_xticklabels(anios, fontsize=8)
    ax.set_ylabel("Valor intrínseco / acción (US$)", fontsize=8)
    ax.set_ylim(40, 310)
    ax.set_xlim(-0.3, len(anios) - 0.4)
    ax.legend(loc="upper left", fontsize=7, frameon=False)

    fig.subplots_adjust(top=0.80, bottom=0.10, left=0.10, right=0.96)
    CS.deco(ax,
            "Proyección del valor intrínseco a 5 años (2026-2031)",
            "Tres escenarios con rango sombreado; PWFV honesto 140 y suelo EPV 80 como anclas",
            FUENTE, fig=fig)
    CS.save(fig, "c_proy")


# ---------------------------------------------------------------------
def main():
    funcs = [
        c_radar, c_ew, c_colapso, c_ingresos_fcf, c_dau, c_decel, c_moat,
        c_matriz, c_fuerzas, c_tam, c_dcf, c_zonas, c_sens, c_mgmt,
        c_inversores, c_riesgos, c_proy,
    ]
    errores = []
    for fn in funcs:
        try:
            fn()
            print(f"OK  {fn.__name__}")
        except Exception as exc:
            errores.append((fn.__name__, repr(exc)))
            print(f"ERR {fn.__name__}: {exc!r}")
    if errores:
        print("\n=== ERRORES ===")
        for name, e in errores:
            print(f"  {name}: {e}")
    else:
        print("\nTodos los charts generados sin errores.")


if __name__ == "__main__":
    main()
