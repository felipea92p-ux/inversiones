# -*- coding: utf-8 -*-
"""
MAKE CHARTS · INTU (Intuit) — Tesis Ultra Quality Growth v6
Genera 18 PNGs estilo Economist en charts/ (dpi=150) usando chart_style.

Reglas de la casa aplicadas:
 - NUNCA dos '$' en un titulo/subtitulo (mathtext). Guard: text.parse_math=False.
 - Coma decimal espaniola en etiquetas numericas (76,8 · 275,35 · +22%).
 - Todo grafico usa chart_style.deco(ax, titulo, sub, fuente, fig=fig).
 - fig ~ (7.2, 4.2); fig.subplots_adjust(top=0.80); chart_style.save(fig, "c_xxx").
 - Colores: base=azul, alerta=rojo_oscuro, positivo=verde, umbral/PWFV=rojo dashed,
   HOY/precio=tinta solid, neutral=ocre.
"""
import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
from matplotlib.lines import Line2D

import chart_style
from chart_style import deco, save
from paleta_qg import PALETA as P

# GUARD contra mathtext (dos '$' garabatean el texto)
plt.rcParams["text.parse_math"] = False

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "data", "charts_spec.json"), encoding="utf-8") as f:
    SPEC = json.load(f)
with open(os.path.join(HERE, "data", "analysis.json"), encoding="utf-8") as f:
    ANALYSIS = json.load(f)

FUENTE = ("Fuente: filings INTU, press release Q3 FY26, sistema QG-Seilern + val-mos. "
          "Elaboracion propia.")
FIGSIZE = (7.2, 4.2)


def com(x, dec=1):
    """Formatea numero con coma decimal espaniola."""
    s = f"{x:.{dec}f}"
    return s.replace(".", ",")


def new_fig(polar=False):
    if polar:
        fig, ax = plt.subplots(figsize=FIGSIZE, subplot_kw={"projection": "polar"})
    else:
        fig, ax = plt.subplots(figsize=FIGSIZE)
    fig.subplots_adjust(top=0.80)
    return fig, ax


# ─────────────────────────────────────────────────────────────────────────────
# 1. c_radar — Radar QG-Seilern 11 reglas
# ─────────────────────────────────────────────────────────────────────────────
def c_radar():
    d = SPEC["radar_11_reglas"]
    labels = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11"]
    vals = d["valores"]
    maxv = d["max_por_regla"]
    n = len(vals)
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    ang += ang[:1]
    score = vals + vals[:1]
    maxline = [maxv] * n + [maxv]

    fig, ax = new_fig(polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, maxv)
    ax.plot(ang, maxline, color=P["gris_medio"], lw=1.0, ls="--", alpha=0.8)
    ax.fill(ang, maxline, color=P["gris_linea"], alpha=0.20)
    ax.plot(ang, score, color=P["azul"], lw=2.0)
    ax.fill(ang, score, color=P["azul"], alpha=0.35)
    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(labels, fontsize=8.5, color=P["tinta"])
    ax.set_yticks([3, 6, 9, 12])
    ax.set_yticklabels([str(t) for t in [3, 6, 9, 12]], fontsize=6.5, color=P["gris_medio"])
    ax.tick_params(pad=2)

    deco(ax, "Radar QG-Seilern · INTU 76,8/100 (Alta conviccion)",
         "Poligono azul = score por regla; linea discontinua = maximo 13,5 por regla",
         FUENTE, fig=fig)
    save(fig, "c_radar")


# ─────────────────────────────────────────────────────────────────────────────
# 2. c_ew — Dashboard early-warning semaforo
# ─────────────────────────────────────────────────────────────────────────────
def c_ew():
    d = SPEC["early_warning"]
    kpis = d["kpis"]
    col = {"verde": P["verde"], "ambar": P["ocre"], "rojo": P["rojo_oscuro"], "gris": P["gris"]}
    txt_estado = {"verde": "VERDE", "ambar": "AMBAR", "rojo": "ROJO", "gris": "SIN DATO"}

    fig, ax = new_fig()
    ax.axis("off")
    n = len(kpis)
    row_h = 1.0
    y0 = n * row_h
    for i, k in enumerate(kpis):
        y = y0 - (i + 1) * row_h
        c = col.get(k["estado"], P["gris"])
        # fila alterna sutil
        if i % 2 == 0:
            ax.add_patch(Rectangle((0, y), 10, row_h, color=P["gris_claro"], alpha=0.5, zorder=0))
        # nombre KPI
        ax.text(0.15, y + row_h / 2, k["kpi"], va="center", ha="left",
                fontsize=7.6, color=P["tinta"], zorder=2)
        # celda semaforo
        ax.add_patch(Rectangle((6.30, y + 0.18), 0.95, row_h - 0.36, color=c, zorder=2))
        ax.text(6.775, y + row_h / 2, txt_estado[k["estado"]], va="center", ha="center",
                fontsize=6.2, color=P["fondo"], fontweight="bold", zorder=3)
        # valor actual
        val = k["valor"].replace(".", ",")
        ax.text(7.45, y + row_h / 2, val, va="center", ha="left",
                fontsize=7.0, color=P["gris"], style="italic", zorder=2)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, y0)

    deco(ax, "Semaforo early-warning · KPIs SaaS",
         "5 verdes con dato · 1 ambar (TurboTax) · 1 sensor faltante (retadores IA) -> sizing probatorio 3-5%",
         FUENTE, fig=fig)
    save(fig, "c_ew")


# ─────────────────────────────────────────────────────────────────────────────
# 3. c_colapso — Colapso de precio + de-rating de multiplo
# ─────────────────────────────────────────────────────────────────────────────
def c_colapso():
    d = SPEC["colapso_precio_multiplo"]
    ath = d["precio_max"]
    hoy = d["precio_actual"]
    caida = d["caida_pct"]

    fig, ax = new_fig()
    x = [0, 1]
    y = [ath, hoy]
    ax.plot(x, y, color=P["tinta"], lw=2.2, marker="o", markersize=7, zorder=3)
    ax.scatter([0], [ath], color=P["azul"], s=70, zorder=4)
    ax.scatter([1], [hoy], color=P["rojo_oscuro"], s=70, zorder=4)
    ax.text(0, ath + 25, f"ATH {com(ath, 2)}", ha="center", va="bottom",
            fontsize=8.5, color=P["azul"], fontweight="bold")
    ax.text(1, hoy - 35, f"HOY {com(hoy, 2)}", ha="center", va="top",
            fontsize=8.5, color=P["rojo_oscuro"], fontweight="bold")
    # flecha drawdown
    ax.annotate(f"{com(caida, 0)}%", xy=(0.5, (ath + hoy) / 2),
                xytext=(0.5, (ath + hoy) / 2 + 90), ha="center",
                fontsize=13, color=P["rojo_oscuro"], fontweight="bold")
    ax.annotate("", xy=(0.52, hoy + 20), xytext=(0.52, ath - 20),
                arrowprops=dict(arrowstyle="->", color=P["rojo_oscuro"], lw=1.4))
    # caja compresion de multiplo
    caja = (f"Compresion de MULTIPLO, no de fundamentales\n"
            f"P/E  {d['pe_historico']:.0f}x  ->  {com(d['pe_actual'],1)}x\n"
            f"EV/EBITDA  {d['ev_ebitda_historico']:.0f}x  ->  {com(d['ev_ebitda_actual'],1)}x\n"
            f"(rev +15%, op margin 20% -> 27%, FCF 7,76B)")
    ax.text(0.62, ath - 5, caja, ha="left", va="top", fontsize=7.4,
            color=P["tinta"], family="DejaVu Serif",
            bbox=dict(boxstyle="round,pad=0.5", fc=P["panel"], ec=P["gris_linea"], lw=0.8))

    ax.set_xlim(-0.35, 1.7)
    ax.set_ylim(150, 900)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Pico 2021", "Hoy (jul-2026)"], fontsize=8)
    ax.set_ylabel("Precio por accion (US$)", fontsize=8)

    deco(ax, "El castigo es de multiplo, no de negocio",
         "INTU cayo -66% desde 813,70 mientras ingresos, margenes y FCF subian",
         FUENTE, fig=fig)
    save(fig, "c_colapso")


# ─────────────────────────────────────────────────────────────────────────────
# 4. c_ingresos_fcf — Ingresos + FCF FY21-FY25 (dual bars)
# ─────────────────────────────────────────────────────────────────────────────
def c_ingresos_fcf():
    d = SPEC["ingresos_fcf_historico"]
    per = d["periodos"][:5]   # FY21-FY25 (excluye TTM para claridad)
    rev = d["revenue"][:5]
    fcf = d["fcf"][:5]

    fig, ax = new_fig()
    x = np.arange(len(per))
    w = 0.38
    b1 = ax.bar(x - w / 2, rev, w, color=P["azul"], label="Ingresos")
    b2 = ax.bar(x + w / 2, fcf, w, color=P["verde"], label="Flujo de caja libre")
    for xi, v in zip(x - w / 2, rev):
        ax.text(xi, v + 0.2, com(v, 1), ha="center", va="bottom", fontsize=7, color=P["azul"])
    for xi, v in zip(x + w / 2, fcf):
        ax.text(xi, v + 0.2, com(v, 1), ha="center", va="bottom", fontsize=7, color=P["verde"])
    ax.set_xticks(x)
    ax.set_xticklabels(per, fontsize=8)
    ax.set_ylabel("US$ miles de millones", fontsize=8)
    ax.set_ylim(0, max(rev) * 1.18)
    ax.legend(loc="upper left", fontsize=7.5, frameon=False)

    deco(ax, "Ingresos y FCF suben mientras la accion cayo -66%",
         "Revenue FY21-25 casi se duplica; FCF crece ~18% anual — el negocio no se rompio",
         FUENTE, fig=fig)
    save(fig, "c_ingresos_fcf")


# ─────────────────────────────────────────────────────────────────────────────
# 5. c_segments — Mix por segmento + crecimiento
# ─────────────────────────────────────────────────────────────────────────────
def c_segments():
    d = SPEC["segmentos_mix"]
    lineas = d["lineas"]
    nombres = ["Small Business\n(QuickBooks+Mailchimp)", "Consumer\n(TurboTax)",
               "Credit Karma", "ProTax"]
    pesos = [l["peso_rev_pct"] for l in lineas]
    growth = [l["growth_pct"] for l in lineas]

    fig, ax = new_fig()
    x = np.arange(len(lineas))
    cols = [P["azul"], P["azul_acero"], P["azul_cielo"], P["ocre"]]
    bars = ax.bar(x, pesos, 0.6, color=cols)
    for xi, p, g in zip(x, pesos, growth):
        ax.text(xi, p + 0.8, f"{p:.0f}% peso", ha="center", va="bottom",
                fontsize=7.2, color=P["tinta"])
        ax.text(xi, p / 2, f"+{g:.0f}%\ncrec.", ha="center", va="center",
                fontsize=7.6, color=P["fondo"], fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(nombres, fontsize=7)
    ax.set_ylabel("% de ingresos", fontsize=8)
    ax.set_ylim(0, max(pesos) * 1.28)

    # anotacion QBO destacada
    ax.text(0, max(pesos) * 1.15, "QuickBooks Online Accounting +22% (precio+clientes+mix)",
            ha="left", va="center", fontsize=7.5, color=P["rojo"], fontweight="bold")

    deco(ax, "El nucleo QuickBooks crece +22% pese al miedo IA",
         "Small Business es el 58% del mix; Credit Karma +32% es el mas rapido",
         FUENTE, fig=fig)
    save(fig, "c_segments")


# ─────────────────────────────────────────────────────────────────────────────
# 6. c_decel — Desaceleracion de ingresos + Rule of 40
# ─────────────────────────────────────────────────────────────────────────────
def c_decel():
    d = SPEC["decel_rule40"]
    per = d["periodos"]
    growth = d["revenue_growth_pct"]
    r40 = d["rule_of_40"]
    umbral = d["umbral_rule40"]

    fig, ax = new_fig()
    x = np.arange(len(per))
    bars = ax.bar(x, growth, 0.55, color=P["azul"], label="Crecimiento ingresos %")
    for xi, g in zip(x, growth):
        ax.text(xi, g + 0.8, com(g, 1) if g % 1 else f"{g:.0f}", ha="center", va="bottom",
                fontsize=7, color=P["azul"])
    ax.set_ylabel("Crecimiento ingresos (%)", fontsize=8, color=P["azul"])
    ax.set_ylim(0, max(growth) * 1.25)

    ax2 = ax.twinx()
    ax2.plot(x, r40, color=P["verde"], lw=2.0, marker="o", markersize=6,
             label="Rule of 40", zorder=5)
    for xi, r in zip(x, r40):
        ax2.text(xi, r + 1.5, f"{r:.0f}", ha="center", va="bottom",
                 fontsize=7, color=P["verde"], fontweight="bold")
    ax2.axhline(umbral, color=P["rojo"], ls="--", lw=1.3)
    ax2.text(len(per) - 0.5, umbral + 1, f"Umbral 40", ha="right", va="bottom",
             fontsize=7, color=P["rojo"], style="italic")
    ax2.set_ylabel("Rule of 40 (crec. + margen FCF)", fontsize=8, color=P["verde"])
    ax2.set_ylim(0, 75)
    ax2.grid(False)
    for s in ["top", "left"]:
        ax2.spines[s].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.tick_params(length=0, colors=P["verde"])

    ax.set_xticks(x)
    ax.set_xticklabels(per, fontsize=7.5)

    deco(ax, "El crecimiento desacelera, pero la Rule of 40 sigue intacta",
         "Rev crece +10% (Q3 FY26); Rule of 40 ~52, muy por encima del umbral 40",
         FUENTE, fig=fig)
    save(fig, "c_decel")


# ─────────────────────────────────────────────────────────────────────────────
# 7. c_moat — Anios de defensa por capa de foso (DERIVADO)
# ─────────────────────────────────────────────────────────────────────────────
def c_moat():
    # DERIVADO: no esta en el spec. Anios de defensa estimados por capa.
    capas = ["Marca de confianza",
             "Switching costs QuickBooks\n(embebido PYMEs+contadores)",
             "Complejidad tributaria/\nregulatoria (TurboTax)",
             "Datos propietarios + IA"]
    anios = [4, 10, 8, 6]
    # color por durabilidad: mas anios = mas durable (verde), menos = ocre
    def dur_color(a):
        if a >= 9:
            return P["verde"]
        if a >= 7:
            return P["azul"]
        if a >= 5:
            return P["azul_acero"]
        return P["ocre"]
    cols = [dur_color(a) for a in anios]

    fig, ax = new_fig()
    y = np.arange(len(capas))
    ax.barh(y, anios, 0.6, color=cols)
    for yi, a in zip(y, anios):
        ax.text(a + 0.15, yi, f"~{a} anios", va="center", ha="left",
                fontsize=8, color=P["tinta"], fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels(capas, fontsize=7.6)
    ax.invert_yaxis()
    ax.set_xlabel("Anios estimados de defensa del foso", fontsize=8)
    ax.set_xlim(0, max(anios) * 1.25)
    ax.grid(axis="x", color=P["gris_linea"], lw=0.6, alpha=0.9)
    ax.grid(axis="y", visible=False)

    deco(ax, "El foso vive en los switching costs y la complejidad regulatoria",
         "QuickBooks embebido (~10 anios) y la maranha tributaria (~8) son las capas mas duraderas",
         FUENTE, fig=fig)
    save(fig, "c_moat")


# ─────────────────────────────────────────────────────────────────────────────
# 8. c_matriz — Matriz competitiva (DERIVADO)
# ─────────────────────────────────────────────────────────────────────────────
def c_matriz():
    # DERIVADO: coords 0-10. x=escala/distribucion, y=switching costs/atrincheramiento.
    # label_pos: "in" (dentro burbuja) o desplazamiento (dx,dy) para etiqueta externa.
    players = [
        ("Intuit /\nQuickBooks", 8.6, 8.6, 2200, P["azul"], "in"),
        ("Xero", 5.5, 6.5, 900, P["azul_acero"], "in"),
        ("FreshBooks", 3.5, 4.5, 500, P["azul_cielo"], (0, -0.75)),
        ("Wave", 3.0, 2.8, 400, P["ocre"], (0, 0.7)),
        ("H&R Block", 6.2, 4.0, 700, P["terracota"], "in"),
        ("IRS Direct File", 4.5, 1.5, 550, P["rojo_oscuro"], (0, -0.72)),
        ("Agentes IA\ncontabilidad", 2.3, 1.7, 600, P["rojo_oscuro"], (0, 0.9)),
    ]
    fig, ax = new_fig()
    for name, x, y, s, c, lp in players:
        ax.scatter(x, y, s=s, color=c, alpha=0.75, edgecolor=P["tinta"], lw=0.6, zorder=3)
        if lp == "in":
            ax.text(x, y, name, ha="center", va="center", fontsize=6.3,
                    color=P["fondo"] if c in (P["azul"], P["rojo_oscuro"], P["azul_acero"]) else P["tinta"],
                    fontweight="bold", zorder=4)
        else:
            dx, dy = lp
            ax.text(x + dx, y + dy, name, ha="center", va="center", fontsize=6.4,
                    color=P["tinta"], fontweight="bold", zorder=4)
    # cuadrante dominante
    ax.axvline(5, color=P["gris_linea"], lw=0.8, ls=":")
    ax.axhline(5, color=P["gris_linea"], lw=0.8, ls=":")
    ax.text(5.2, 9.6, "Dominante ->", ha="left", va="top", fontsize=7,
            color=P["verde"], style="italic")
    ax.text(0.4, 0.4, "Bajo coste / bajo lock-in", ha="left", va="bottom", fontsize=7,
            color=P["gris"], style="italic")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel("Escala / distribucion  ->", fontsize=8)
    ax.set_ylabel("Switching costs / atrincheramiento  ->", fontsize=8)

    deco(ax, "Intuit domina la esquina de escala + atrincheramiento",
         "IRS Direct File y agentes IA atacan por abajo (bajo coste, bajo lock-in); burbuja = fuerza de marca",
         FUENTE, fig=fig)
    save(fig, "c_matriz")


# ─────────────────────────────────────────────────────────────────────────────
# 9. c_fuerzas — Cinco fuerzas de Porter (pentagono)
# ─────────────────────────────────────────────────────────────────────────────
def c_fuerzas():
    d = SPEC["cinco_fuerzas"]
    v = d["valores"]
    labels = ["Nuevos\nentrantes", "Poder\nproveedores", "Poder\nclientes",
              "Sustitutos\n(IA + IRS Direct File)", "Rivalidad"]
    vals = [v["nuevos_entrantes"], v["poder_proveedores"], v["poder_clientes"],
            v["sustitutos"], v["rivalidad"]]
    total = d["total_sobre_25"]
    n = len(vals)
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    ang += ang[:1]
    vv = vals + vals[:1]

    fig, ax = new_fig(polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 5)
    ax.plot(ang, vv, color=P["azul"], lw=2.0)
    ax.fill(ang, vv, color=P["azul"], alpha=0.30)
    # destacar sustitutos (indice 3)
    ax.scatter([ang[3]], [vals[3]], color=P["rojo_oscuro"], s=90, zorder=6)
    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(labels, fontsize=7.6, color=P["tinta"])
    # colorea la etiqueta de sustitutos
    xt = ax.get_xticklabels()
    xt[3].set_color(P["rojo_oscuro"])
    xt[3].set_fontweight("bold")
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=P["gris_medio"])
    ax.tick_params(pad=4)

    deco(ax, "Industria atractiva, un solo vertice estirado: sustitutos",
         f"1=favorable, 5=adverso · presion total {com(total,1)}/25 · la IA/IRS Direct File ataca el 30-40% del value pool",
         FUENTE, fig=fig)
    save(fig, "c_fuerzas")


# ─────────────────────────────────────────────────────────────────────────────
# 10. c_tam — Embudo TAM / SAM / SOM
# ─────────────────────────────────────────────────────────────────────────────
def c_tam():
    d = SPEC["tam_sam_som"]
    # TAM software puro ~40; SAM ~105; SOM ~35. Nota: TAM<SAM aqui por definicion del spec
    # (TAM software puro estrecho vs SAM ampliado). Los ordenamos por magnitud de embudo logico
    # usando el titular Intuit 327 como TAM amplio y bajando.
    titular = d["titular_intuit"]  # 327
    niveles = [("TAM titular Intuit", titular, P["azul_cielo"]),
               ("SAM defendible", d["sam"], P["azul_acero"]),
               ("TAM software puro", d["tam"], P["azul"]),
               ("SOM realista", d["som"], P["verde"])]
    # ordenar descendente
    niveles = sorted(niveles, key=lambda t: -t[1])

    fig, ax = new_fig()
    y = np.arange(len(niveles))[::-1]
    maxw = niveles[0][1]
    for yi, (name, val, c) in zip(y, niveles):
        left = (maxw - val) / 2
        ax.barh(yi, val, 0.62, left=left, color=c)
        ax.text(maxw / 2, yi, f"{name}: {val:.0f}", ha="center", va="center",
                fontsize=8, color=P["fondo"], fontweight="bold")
    ax.set_xlim(0, maxw * 1.05)
    ax.set_yticks([])
    ax.set_xlabel("Tamanio de mercado (US$ miles de millones)", fontsize=8)
    ax.grid(axis="x", color=P["gris_linea"], lw=0.6, alpha=0.9)

    deco(ax, "El embudo realista: SOM ~35B vs titular 327B",
         "TAM software puro ~40B; SAM defendible ~105B; SOM realista 30-40B (~6% del titular Intuit)",
         FUENTE, fig=fig)
    save(fig, "c_tam")


# ─────────────────────────────────────────────────────────────────────────────
# 11. c_dcf — DCF 3 escenarios vs precio
# ─────────────────────────────────────────────────────────────────────────────
def c_dcf():
    d = SPEC["dcf_3_escenarios"]
    esc = d["escenarios"]
    precio = d["precio_actual"]
    ponderado = d["esperado_ponderado"]
    nombres = [e["nombre"] for e in esc]
    valores = [e["valor_accion"] for e in esc]
    probs = [e["prob_pct"] for e in esc]
    cols = [P["rojo_oscuro"], P["azul"], P["verde"]]  # conservador/base/optimista

    fig, ax = new_fig()
    x = np.arange(len(esc))
    bars = ax.bar(x, valores, 0.55, color=cols)
    for xi, v, p in zip(x, valores, probs):
        ax.text(xi, v + 6, f"{com(v,0)}", ha="center", va="bottom",
                fontsize=8.5, color=P["tinta"], fontweight="bold")
        ax.text(xi, v / 2, f"prob {p}%", ha="center", va="center",
                fontsize=7.5, color=P["fondo"], fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(nombres, fontsize=8.5)
    ax.set_ylabel("Valor por accion (US$)", fontsize=8)
    ax.set_ylim(0, max(valores) * 1.18)

    # precio HOY (tinta solid) — por debajo INCLUSO del conservador
    ax.axhline(precio, color=P["tinta"], lw=1.8)
    ax.text(len(esc) - 0.5, precio - 12, f"HOY {com(precio,2)}", ha="right", va="top",
            fontsize=8, color=P["tinta"], fontweight="bold")
    # ponderado (linea dashed azul)
    ax.axhline(ponderado, color=P["azul"], lw=1.3, ls="--")
    ax.text(0, ponderado + 6, f"Esperado ponderado {com(ponderado,0)}", ha="left", va="bottom",
            fontsize=7.5, color=P["azul"], style="italic")
    # nota PWFV honesto ~450
    ax.text(len(esc) - 0.5, max(valores) * 1.10, "PWFV honesto ~450",
            ha="right", va="top", fontsize=7.5, color=P["rojo"], style="italic")

    deco(ax, "Deep value: hasta el escenario conservador esta sobre el precio",
         "Valor/accion por escenario vs precio HOY 275,35 — el mercado paga menos que el caso conservador (394)",
         FUENTE, fig=fig)
    save(fig, "c_dcf")


# ─────────────────────────────────────────────────────────────────────────────
# 12. c_zonas — Mapa de zonas de valoracion
# ─────────────────────────────────────────────────────────────────────────────
def c_zonas():
    d = SPEC["mapa_zonas"]
    precio = d["precio_actual"]
    epv = d["epv_suelo"]
    pt = d["pt_consenso"]
    pwfv_central = d["pwfv_central"]
    pwfv_opt = d["pwfv_optimista"]
    u = d["umbrales_precio_sobre_pwfv_central_450"]

    # bandas: GANGA (< ganga 337) / OPORTUNIDAD (337-382) / PRECIO JUSTO (382-405) / CARO (>405)
    # (basado en umbrales sobre PWFV central 450)
    fig, ax = new_fig()
    xmin, xmax = 150, 540
    bandas = [
        (xmin, u["ganga"], P["verde"], "GANGA"),
        (u["ganga"], u["oportunidad"], P["azul_acero"], "OPORTUNIDAD"),
        (u["oportunidad"], u["razonable"], P["ocre"], "PRECIO JUSTO"),
        (u["razonable"], xmax, P["rojo_oscuro"], "CARO"),
    ]
    yb = 0.35
    for x0, x1, c, name in bandas:
        ax.add_patch(Rectangle((x0, 0), x1 - x0, yb, color=c, alpha=0.55, zorder=1))
        # bandas anchas -> etiqueta horizontal centrada; bandas estrechas -> vertical
        if (x1 - x0) >= 55:
            ax.text((x0 + x1) / 2, yb / 2, name, ha="center", va="center",
                    fontsize=7.2, color=P["fondo"], fontweight="bold", zorder=2)
        else:
            ax.text((x0 + x1) / 2, yb / 2, name, ha="center", va="center",
                    rotation=90, fontsize=6.2, color=P["fondo"], fontweight="bold", zorder=2)

    # marcadores
    def marca(x, label, color, dy, ls="-"):
        ax.plot([x, x], [0, yb + 0.32 + dy], color=color, lw=1.6, ls=ls, zorder=4)
        ax.text(x, yb + 0.34 + dy, label, ha="center", va="bottom",
                fontsize=7.2, color=color, fontweight="bold", zorder=5)

    marca(epv, f"EPV\n{com(epv,0)}", P["gris"], 0.0)
    marca(precio, f"HOY\n{com(precio,2)}", P["tinta"], 0.30)
    marca(pwfv_central, f"PWFV honesto\n~{com(pwfv_central,0)}", P["rojo"], 0.0, ls="--")
    marca(pt, f"PT consenso\n{com(pt,2)}", P["azul"], 0.30)
    marca(pwfv_opt, f"PWFV\n{com(pwfv_opt,0)}", P["rojo_oscuro"], 0.0)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(0, 1.7)
    ax.set_yticks([])
    ax.set_xlabel("Precio por accion (US$)", fontsize=8)
    ax.grid(axis="y", visible=False)

    deco(ax, "Zonas de valoracion — HOY en GANGA (~35-40% MoS)",
         "Precio 275,35 muy por debajo del PWFV honesto ~450 y del suelo de zona GANGA (337)",
         FUENTE, fig=fig)
    save(fig, "c_zonas")


# ─────────────────────────────────────────────────────────────────────────────
# 13. c_sens — Heatmap sensibilidad WACC x growth
# ─────────────────────────────────────────────────────────────────────────────
def c_sens():
    d = SPEC["sensibilidad_wacc_terminal"]
    filas = d["filas_wacc"]
    waccs = [f["wacc_pct"] for f in filas]
    growth = [f["growth_implicito_pct"] for f in filas]
    pwfv = [f["pwfv_aprox"] for f in filas]
    precio = d["precio_actual"]
    fair = d["wacc_fair"]

    fig, ax = new_fig()
    # matriz 1 columna de PWFV por WACC (con growth implicito como segunda info)
    arr = np.array(pwfv).reshape(-1, 1)
    im = ax.imshow(arr, cmap="YlOrRd", aspect="auto",
                   extent=[0, 1, len(filas) - 0.5, -0.5])
    for i, (w, g, pv) in enumerate(zip(waccs, growth, pwfv)):
        gtxt = ("+" if g > 0 else "") + com(g, 1)
        ax.text(0.5, i, f"PWFV {pv:.0f}\ng.impl. {gtxt}%", ha="center", va="center",
                fontsize=7.6, color=P["tinta"], fontweight="bold")
    ax.set_yticks(range(len(filas)))
    ax.set_yticklabels([f"WACC {com(w,1)}%" for w in waccs], fontsize=8)
    ax.set_xticks([])
    ax.set_xlim(0, 1)

    # marcar fila base/fair (9.5%)
    idx_fair = waccs.index(fair)
    ax.add_patch(Rectangle((0, idx_fair - 0.5), 1, 1, fill=False,
                           edgecolor=P["azul"], lw=2.5, zorder=5))
    ax.text(1.06, idx_fair, "<- WACC fair 9,5%\n(g. implicito +0,5% plano)",
            ha="left", va="center", fontsize=7.2, color=P["azul"], fontweight="bold")
    # honest cell 8.5 (piso, titular -1.5%)
    idx_piso = waccs.index(8.5)
    ax.add_patch(Rectangle((0, idx_piso - 0.5), 1, 1, fill=False,
                           edgecolor=P["rojo_oscuro"], lw=1.6, ls="--", zorder=5))
    ax.text(1.06, idx_piso, "<- piso 8,5% (titular -1,5%)",
            ha="left", va="center", fontsize=7.0, color=P["rojo_oscuro"], style="italic")
    ax.set_xlim(0, 2.1)

    deco(ax, "Sensibilidad: incluso al WACC fair el PWFV (450) triplica al precio",
         f"Precio HOY 275,35 queda muy por debajo de TODAS las filas (min PWFV {min(pwfv):.0f}) — colchon en cualquier WACC",
         FUENTE, fig=fig)
    save(fig, "c_sens")


# ─────────────────────────────────────────────────────────────────────────────
# 14. c_mgmt — Radar de gestion (6 dims /5)
# ─────────────────────────────────────────────────────────────────────────────
def c_mgmt():
    d = SPEC["management_radar"]
    labels = ["Ejecucion\noperativa", "Asignacion\ncapital", "Alineacion/\nskin-in-game",
              "Gobernanza", "Transparencia", "Vision\nestrategica"]
    vals = d["valores"]
    n = len(vals)
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    ang += ang[:1]
    vv = vals + vals[:1]
    maxline = [5] * n + [5]

    fig, ax = new_fig(polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 5)
    ax.plot(ang, maxline, color=P["gris_medio"], lw=1.0, ls="--", alpha=0.7)
    ax.plot(ang, vv, color=P["azul"], lw=2.0)
    ax.fill(ang, vv, color=P["azul"], alpha=0.32)
    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(labels, fontsize=7.4, color=P["tinta"])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=P["gris_medio"])
    ax.tick_params(pad=4)

    deco(ax, "Gestion y gobernanza",
         "Ejecucion elite (5/5); asignacion de capital y skin-in-game penalizadas (Mailchimp, ventas netas, CEO+Chair)",
         FUENTE, fig=fig)
    save(fig, "c_mgmt")


# ─────────────────────────────────────────────────────────────────────────────
# 15. c_retorno — Retorno al accionista (recompras + dividendos)
# ─────────────────────────────────────────────────────────────────────────────
def c_retorno():
    d = SPEC["retorno_accionista"]
    per = d["periodos"]
    rec = d["recompras"]
    div = d["dividendos"]

    fig, ax = new_fig()
    x = np.arange(len(per))
    b1 = ax.bar(x, rec, 0.55, color=P["azul"], label="Recompras")
    b2 = ax.bar(x, div, 0.55, bottom=rec, color=P["verde"], label="Dividendos")
    for xi, r, dv in zip(x, rec, div):
        tot = r + dv
        ax.text(xi, tot + 0.1, com(tot, 1), ha="center", va="bottom",
                fontsize=7, color=P["tinta"])
    ax.set_xticks(x)
    ax.set_xticklabels(per, fontsize=8)
    ax.set_ylabel("US$ miles de millones", fontsize=8)
    ax.set_ylim(0, (max(r + dv for r, dv in zip(rec, div))) * 1.22)
    ax.legend(loc="upper left", fontsize=7.5, frameon=False)

    ax.text(0.02, 0.86, "Capital devuelto TTM ~6,3B (~80% del FCF)\nRecompra a precio deprimido (-66%)",
            transform=ax.transAxes, ha="left", va="top", fontsize=7.4,
            color=P["gris"], style="italic")

    deco(ax, "Recompras 5,0B + dividendos 1,3B: ~80% del FCF devuelto",
         "Recompras 1,4B -> 5,0B; dividendos 0,65B -> 1,3B — recomprando a la accion deprimida",
         FUENTE, fig=fig)
    save(fig, "c_retorno")


# ─────────────────────────────────────────────────────────────────────────────
# 16. c_inversores — 9 inversores legendarios (DERIVADO)
# ─────────────────────────────────────────────────────────────────────────────
def c_inversores():
    # DERIVADO: conviccion 1-5, veredicto BUY/HOLD/PASS.
    inv = [
        ("Benjamin Graham", 3, "HOLD"),
        ("Warren Buffett", 4, "BUY"),
        ("Charlie Munger", 4, "BUY"),
        ("Philip Fisher", 4, "BUY"),
        ("Peter Lynch", 4, "BUY"),
        ("John Templeton", 4, "BUY"),
        ("Howard Marks", 3, "BUY"),
        ("Peter Seilern", 3, "BUY"),
        ("Terry Smith", 3, "HOLD"),
    ]
    col = {"BUY": P["verde"], "HOLD": P["ocre"], "PASS": P["rojo_oscuro"]}
    # ordenar por conviccion desc para efecto visual
    inv = sorted(inv, key=lambda t: -t[1])

    fig, ax = new_fig()
    y = np.arange(len(inv))[::-1]
    for yi, (name, conv, verd) in zip(y, inv):
        ax.barh(yi, conv, 0.62, color=col[verd])
        ax.text(conv + 0.08, yi, f"{verd} {conv}", va="center", ha="left",
                fontsize=7.4, color=P["tinta"], fontweight="bold")
        ax.text(-0.1, yi, name, va="center", ha="right", fontsize=7.6, color=P["tinta"])
    ax.set_yticks([])
    ax.set_xlim(0, 6)
    ax.set_xlabel("Conviccion (1-5)", fontsize=8)
    ax.grid(axis="x", color=P["gris_linea"], lw=0.6, alpha=0.9)

    # leyenda
    handles = [Line2D([0], [0], marker="s", color="none", markerfacecolor=col[k],
                      markersize=9, label=k) for k in ["BUY", "HOLD", "PASS"]]
    ax.legend(handles=handles, loc="lower right", fontsize=7, frameon=False)

    deco(ax, "Nueve inversores · sesgo comprador a precio de ganga",
         "A ~13x owner earnings y en zona GANGA, 7 de 9 se inclinan a comprar; Graham y Smith en HOLD",
         FUENTE, fig=fig)
    save(fig, "c_inversores")


# ─────────────────────────────────────────────────────────────────────────────
# 17. c_riesgos — Heatmap de riesgos prob x impacto
# ─────────────────────────────────────────────────────────────────────────────
def c_riesgos():
    d = SPEC["riesgos_heatmap"]
    riesgos = d["riesgos"]

    fig, ax = new_fig()
    # cuadrante rojo top-right (prob>=3.5 & impacto>=3.5)
    ax.add_patch(Rectangle((3.5, 3.5), 2, 2, color=P["rojo_oscuro"], alpha=0.16, zorder=0))
    # grid de fondo 1-5
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.grid(color=P["gris_linea"], lw=0.5, alpha=0.7)

    # Agrupar por coordenada (prob, impacto) para fan-out determinista de solapes
    from collections import defaultdict
    grupos = defaultdict(list)
    for i, r in enumerate(riesgos, 1):
        grupos[(r["prob"], r["impacto"])].append((i, r))

    ids_ordenados = [None] * len(riesgos)
    for (pp, im), items in grupos.items():
        k = len(items)
        for j, (i, r) in enumerate(items):
            perm = r.get("perdida_permanente", False)
            c = P["rojo_oscuro"] if perm else P["azul"]
            if k == 1:
                dx, dy = 0.0, 0.0
            else:
                # separar horizontalmente los que comparten celda
                dx = (j - (k - 1) / 2) * 0.24
                dy = 0.0
            ax.scatter(pp + dx, im + dy, s=200, color=c, alpha=0.85,
                       edgecolor=P["tinta"], lw=0.7, zorder=3)
            ax.text(pp + dx, im + dy, f"R{i}", ha="center", va="center",
                    fontsize=7.0, color=P["fondo"], fontweight="bold", zorder=4)
            corta = r["riesgo"]
            if len(corta) > 50:
                corta = corta[:47] + "..."
            ids_ordenados[i - 1] = f"R{i}: {corta}"

    ax.set_xlabel("Probabilidad (1-5)", fontsize=8)
    ax.set_ylabel("Impacto (1-5)", fontsize=8)

    # leyenda de ids en panel derecho, despejada de la linea de fuente
    leyenda = "\n".join(ids_ordenados)
    fig.text(0.535, 0.20, leyenda, ha="left", va="bottom", fontsize=5.7,
             color=P["gris"], family="DejaVu Serif")
    fig.subplots_adjust(top=0.80, right=0.52, bottom=0.14)

    # marca rojo=perdida permanente
    handles = [
        Line2D([0], [0], marker="o", color="none", markerfacecolor=P["rojo_oscuro"],
               markersize=9, label="Perdida permanente"),
        Line2D([0], [0], marker="o", color="none", markerfacecolor=P["azul"],
               markersize=9, label="Recuperable"),
    ]
    ax.legend(handles=handles, loc="upper left", fontsize=6.5, frameon=False)

    deco(ax, "Mapa de riesgos: el cuadrante rojo (alto-alto) esta vacio",
         "El unico riesgo de perdida permanente (R1: agentes IA en libro mayor) tiene prob baja (2)",
         FUENTE, fig=fig)
    save(fig, "c_riesgos")


# ─────────────────────────────────────────────────────────────────────────────
# 18. c_proy — Fan chart proyeccion 5 anios
# ─────────────────────────────────────────────────────────────────────────────
def c_proy():
    d = SPEC["proyeccion_5y"]
    precio = d["precio_actual"]
    esc = d["escenarios"]
    epv = SPEC["mapa_zonas"]["epv_suelo"]
    pwfv = ANALYSIS["val"]["pwfv_valor"]  # 450

    # mapear escenarios
    cons = next(e for e in esc if e["nombre"] == "Conservador")
    base = next(e for e in esc if e["nombre"] == "Base")
    opt = next(e for e in esc if e["nombre"] == "Optimista")

    anios = np.array([2026, 2027, 2028, 2029, 2030, 2031])
    t = np.linspace(0, 1, len(anios))

    def path(v_term):
        cagr = (v_term / precio) ** (1 / (len(anios) - 1)) - 1
        return precio * (1 + cagr) ** np.arange(len(anios))

    p_cons = path(cons["valor_terminal"])
    p_base = path(base["valor_terminal"])
    p_opt = path(opt["valor_terminal"])

    fig, ax = new_fig()
    # banda sombreada entre conservador y optimista
    ax.fill_between(anios, p_cons, p_opt, color=P["azul_cielo"], alpha=0.25, zorder=1)
    ax.plot(anios, p_opt, color=P["verde"], lw=1.8, marker="o", markersize=4,
            label=f"Optimista ({com(opt['valor_terminal'],0)})")
    ax.plot(anios, p_base, color=P["azul"], lw=2.2, marker="o", markersize=4,
            label=f"Base ({com(base['valor_terminal'],0)})")
    ax.plot(anios, p_cons, color=P["rojo_oscuro"], lw=1.8, marker="o", markersize=4,
            label=f"Conservador ({com(cons['valor_terminal'],0)})")

    # etiquetas terminales
    ax.text(anios[-1] + 0.08, p_opt[-1], com(opt["valor_terminal"], 0),
            va="center", ha="left", fontsize=7.5, color=P["verde"], fontweight="bold")
    ax.text(anios[-1] + 0.08, p_base[-1], com(base["valor_terminal"], 0),
            va="center", ha="left", fontsize=7.5, color=P["azul"], fontweight="bold")
    ax.text(anios[-1] + 0.08, p_cons[-1], com(cons["valor_terminal"], 0),
            va="center", ha="left", fontsize=7.5, color=P["rojo_oscuro"], fontweight="bold")

    # PWFV horizontal
    ax.axhline(pwfv, color=P["rojo"], ls="--", lw=1.3)
    ax.text(anios[0], pwfv + 8, f"PWFV honesto ~{com(pwfv,0)}", ha="left", va="bottom",
            fontsize=7.2, color=P["rojo"], style="italic")
    # EPV floor
    ax.axhline(epv, color=P["gris"], ls=":", lw=1.2)
    ax.text(anios[0], epv - 8, f"Suelo EPV {com(epv,0)}", ha="left", va="top",
            fontsize=7.0, color=P["gris"], style="italic")
    # precio actual
    ax.scatter([anios[0]], [precio], color=P["tinta"], s=55, zorder=6)
    ax.text(anios[0], precio - 12, f"HOY {com(precio,2)}", ha="left", va="top",
            fontsize=7.5, color=P["tinta"], fontweight="bold")
    # catalizador FY27
    ax.axvline(2026.9, color=P["ocre"], ls="--", lw=1.0, alpha=0.8)
    ax.text(2026.9, ax.get_ylim()[1] * 0.98, "Guia FY27\n~ago-2026", ha="center", va="top",
            fontsize=6.6, color=P["ocre"], style="italic")

    ax.set_xlim(2025.8, 2031.6)
    ax.set_ylim(150, max(p_opt) * 1.10)
    ax.set_xticks(anios)
    ax.set_xticklabels([str(a) for a in anios], fontsize=7.5)
    ax.set_ylabel("Precio por accion (US$)", fontsize=8)
    ax.legend(loc="upper left", fontsize=7, frameon=False)

    deco(ax, "Proyeccion 5 anios: los tres caminos parten desde 275,35",
         "Escenario base ~522 (CAGR ~14%); catalizador binario en la guia FY27 (~agosto 2026)",
         FUENTE, fig=fig)
    save(fig, "c_proy")


# ─────────────────────────────────────────────────────────────────────────────
def main():
    funcs = [
        c_radar, c_ew, c_colapso, c_ingresos_fcf, c_segments, c_decel,
        c_moat, c_matriz, c_fuerzas, c_tam, c_dcf, c_zonas, c_sens,
        c_mgmt, c_retorno, c_inversores, c_riesgos, c_proy,
    ]
    ok, fail = [], []
    for fn in funcs:
        try:
            fn()
            ok.append(fn.__name__)
            print(f"[OK]  {fn.__name__}")
        except Exception as e:
            fail.append((fn.__name__, str(e)))
            print(f"[FAIL] {fn.__name__}: {e}")
    print(f"\nGenerados {len(ok)}/{len(funcs)}")
    if fail:
        print("FALLOS:")
        for n, e in fail:
            print(f"  - {n}: {e}")


if __name__ == "__main__":
    main()
