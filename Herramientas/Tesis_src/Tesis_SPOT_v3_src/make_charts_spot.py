# -*- coding: utf-8 -*-
"""
MAKE CHARTS · SPOT (Spotify) — Tesis Ultra Quality Growth v3
Genera los PNGs estilo Economist en charts/ (dpi=150) usando chart_style.

Reglas de la casa aplicadas:
 - NUNCA dos '$' en un titulo/subtitulo (mathtext). Guard: text.parse_math=False.
 - Coma decimal espaniola en etiquetas numericas.
 - Todo grafico usa chart_style.deco(ax, titulo, sub, fuente, fig=fig).
 - fig ~ (7.2, 4.2); fig.subplots_adjust(top=0.80); chart_style.save(fig, "c_xxx").
 - Colores: base=azul, alerta=rojo_oscuro, positivo=verde, umbral/PWFV=rojo dashed,
   HOY/precio=tinta solid, neutral=ocre.
 - OJO SPOT: reporta en EUR, cotiza en USD. Cada eje declara su moneda.
"""
import json
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.lines import Line2D

import chart_style
from chart_style import deco, save
from paleta_qg import PALETA as P

plt.rcParams["text.parse_math"] = False

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "data", "charts_spec.json"), encoding="utf-8") as f:
    SPEC = json.load(f)

FUENTE = ("Fuente: 20-F FY2025 y 6-K Q1 2026 de Spotify (SEC EDGAR), IFPI, "
          "sistema QG-Seilern + val-mos. Elaboracion propia.")
FIGSIZE = (7.2, 4.2)


def com(x, dec=1):
    """Formatea numero con coma decimal espaniola."""
    return f"{x:.{dec}f}".replace(".", ",")


def new_fig(polar=False, figsize=None):
    fs = figsize or FIGSIZE
    if polar:
        fig, ax = plt.subplots(figsize=fs, subplot_kw={"projection": "polar"})
    else:
        fig, ax = plt.subplots(figsize=fs)
    fig.subplots_adjust(top=0.80)
    return fig, ax


def _estado_col(e):
    return {"verde": P["verde"], "ambar": P["ocre"],
            "rojo": P["rojo_oscuro"], "gris": P["gris"]}.get(e, P["gris"])


# ─────────────────────────────────────────────────────────────────────────────
# 1. c_radar — Radar QG-Seilern 11 reglas
# ─────────────────────────────────────────────────────────────────────────────
def c_radar():
    d = SPEC["radar"]
    labels = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11"]
    # normaliza a escala 0-10 para que el poligono sea comparable entre reglas
    vals = [v / p * 10.0 for v, p in zip(d["puntos"], d["pesos"])]
    n = len(vals)
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    ang += ang[:1]
    score = vals + vals[:1]
    maxline = [10.0] * (n + 1)

    fig, ax = new_fig(polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 10)
    ax.plot(ang, maxline, color=P["gris_medio"], lw=1.0, ls="--", alpha=0.8)
    ax.fill(ang, maxline, color=P["gris_linea"], alpha=0.20)
    ax.plot(ang, score, color=P["azul"], lw=2.0)
    ax.fill(ang, score, color=P["azul"], alpha=0.35)
    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(labels, fontsize=8.5, color=P["tinta"])
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=6.5, color=P["gris_medio"])
    ax.tick_params(pad=2)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_radar")


# ─────────────────────────────────────────────────────────────────────────────
# 2. c_tier — Sensibilidad del score al juicio sobre R1
# ─────────────────────────────────────────────────────────────────────────────
def c_tier():
    d = SPEC["tier_sensibilidad"]
    lecturas = d["lecturas"]
    corte = d["corte"]

    fig, ax = new_fig()
    xs = np.arange(len(lecturas))
    vals = [l["score"] for l in lecturas]
    cols = [_estado_col(l["estado"]) for l in lecturas]
    ax.bar(xs, vals, width=0.55, color=cols, zorder=3)
    for x, v in zip(xs, vals):
        ax.text(x, v + 0.7, com(v, 1), ha="center", va="bottom",
                fontsize=9, fontweight="bold", color=P["tinta"], zorder=4)
    ax.axhline(corte, color=P["rojo"], lw=1.4, ls="--", zorder=2)
    ax.text(len(lecturas) - 0.45, corte + 0.4, f"corte de tier: {corte}",
            ha="right", va="bottom", fontsize=7.4, color=P["rojo"], style="italic")
    ax.set_xticks(xs)
    ax.set_xticklabels([l["etiqueta"] for l in lecturas], fontsize=7.6)
    ax.set_ylim(0, max(vals) * 1.22)
    ax.set_ylabel("Score de calidad /100", fontsize=8)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_tier")


# ─────────────────────────────────────────────────────────────────────────────
# 3. c_escalabilidad — El nudo R1: quien se queda el euro marginal
# ─────────────────────────────────────────────────────────────────────────────
def c_escalabilidad():
    d = SPEC["escalabilidad"]
    emp = d["empresas"]

    fig, ax = new_fig()
    xs = np.arange(len(emp))
    variable = [e["coste_variable"] for e in emp]
    resto = [100 - v for v in variable]
    ax.bar(xs, variable, width=0.55, color=P["rojo_oscuro"], zorder=3,
           label="Coste de contenido / variable (% del ingreso)")
    ax.bar(xs, resto, width=0.55, bottom=variable, color=P["azul_acero"], zorder=3,
           label="Margen bruto disponible")
    for x, v in zip(xs, variable):
        ax.text(x, v / 2, com(v, 0) + "%", ha="center", va="center",
                fontsize=8.5, color=P["fondo"], fontweight="bold", zorder=4)
    for x, v, r in zip(xs, variable, resto):
        ax.text(x, v + r / 2, com(r, 0) + "%", ha="center", va="center",
                fontsize=8.5, color=P["fondo"], fontweight="bold", zorder=4)
    ax.set_xticks(xs)
    ax.set_xticklabels([e["nombre"] for e in emp], fontsize=7.8)
    ax.set_ylim(0, 108)
    ax.set_ylabel("% del ingreso", fontsize=8)
    ax.legend(fontsize=7, loc="lower center", ncol=2, frameon=False,
              facecolor=P["fondo"], edgecolor="none", framealpha=0.85)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_escalabilidad")


# ─────────────────────────────────────────────────────────────────────────────
# 4. c_margen — Descomposicion de la mejora de margen bruto
# ─────────────────────────────────────────────────────────────────────────────
def c_margen():
    d = SPEC["margen"]
    pasos = d["pasos"]

    fig, ax = new_fig()
    acc = 0.0
    for i, s in enumerate(pasos):
        val = s["delta"]
        if s.get("tipo") == "total":
            ax.bar(i, s["valor"], width=0.55, color=P["azul_noche"], zorder=3)
            ax.text(i, s["valor"] + 0.5, com(s["valor"], 1) + "%", ha="center",
                    va="bottom", fontsize=8.2, fontweight="bold", color=P["tinta"])
            acc = s["valor"]
        else:
            col = P["verde"] if val >= 0 else P["rojo_oscuro"]
            ax.bar(i, val, bottom=acc, width=0.55, color=col, zorder=3)
            # positivos: etiqueta encima del tope; negativos: debajo del suelo del tramo
            y_lab = (acc + val + 0.45) if val >= 0 else (acc + val - 0.45)
            ax.text(i, y_lab, ("+" if val >= 0 else "") + com(val, 1) + "pp",
                    ha="center", va="bottom" if val >= 0 else "top",
                    fontsize=7.8, color=P["tinta"])
            acc += val
    ax.set_xticks(range(len(pasos)))
    ax.set_xticklabels([s["etiqueta"] for s in pasos], fontsize=7.2, rotation=18, ha="right")
    ax.set_ylabel("Margen bruto (%)", fontsize=8)
    ax.set_ylim(0, max(max(s.get("valor", 0) for s in pasos), acc) * 1.25)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_margen")


# ─────────────────────────────────────────────────────────────────────────────
# 5. c_ingresos_fcf — Ingresos y flujo de caja libre
# ─────────────────────────────────────────────────────────────────────────────
def c_ingresos_fcf():
    d = SPEC["ingresos_fcf"]
    yrs = d["anios"]

    fig, ax = new_fig()
    xs = np.arange(len(yrs))
    ax.bar(xs, d["ingresos"], width=0.55, color=P["azul"], zorder=3, label="Ingresos (miles de M EUR)")
    ax2 = ax.twinx()
    ax2.plot(xs, d["fcf"], color=P["rojo"], lw=2.2, marker="o", ms=4.5, zorder=4,
             label="FCF (miles de M EUR)")
    ax2.axhline(0, color=P["gris_medio"], lw=0.8, ls=":")
    for x, v in zip(xs, d["fcf"]):
        ax2.text(x, v + 0.12, com(v, 2), ha="center", va="bottom",
                 fontsize=7.2, color=P["rojo"], fontweight="bold")
    ax.set_xticks(xs)
    ax.set_xticklabels(yrs, fontsize=8)
    ax.set_ylabel("Ingresos (miles de M EUR)", fontsize=8)
    ax2.set_ylabel("FCF (miles de M EUR)", fontsize=8, color=P["rojo"])
    ax2.tick_params(colors=P["rojo"], labelsize=7.5)
    ax2.grid(False)
    for s in ["top", "right", "left"]:
        ax2.spines[s].set_visible(False)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, fontsize=7, loc="upper left", frameon=False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_ingresos_fcf")


# ─────────────────────────────────────────────────────────────────────────────
# 6. c_segments — Premium vs Ad-Supported
# ─────────────────────────────────────────────────────────────────────────────
def c_segments():
    d = SPEC["segmentos"]
    yrs = d["anios"]

    fig, ax = new_fig()
    xs = np.arange(len(yrs))
    ax.bar(xs, d["premium"], width=0.55, color=P["azul"], zorder=3, label="Premium")
    ax.bar(xs, d["ads"], width=0.55, bottom=d["premium"], color=P["terracota"],
           zorder=3, label="Ad-Supported")
    for x, p, a in zip(xs, d["premium"], d["ads"]):
        tot = p + a
        ax.text(x, tot + tot * 0.015, com(a / tot * 100, 1) + "% ads",
                ha="center", va="bottom", fontsize=6.8, color=P["gris"], style="italic")
    ax.set_xticks(xs)
    ax.set_xticklabels(yrs, fontsize=8)
    ax.set_ylabel("Ingresos (miles de M EUR)", fontsize=8)
    ax.legend(fontsize=7.4, loc="upper left", frameon=False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_segments")


# ─────────────────────────────────────────────────────────────────────────────
# 7. c_cohortes — Economia por cohorte (obligatorio Media/suscripcion)
# ─────────────────────────────────────────────────────────────────────────────
def c_cohortes():
    d = SPEC["cohortes"]
    regs = d["regiones"]

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(7.2, 4.2))
    fig.subplots_adjust(top=0.78, wspace=0.32)

    xs = np.arange(len(regs))
    arpu = [r["arpu"] for r in regs]
    axL.bar(xs, arpu, width=0.6, color=P["azul"], zorder=3)
    for x, v in zip(xs, arpu):
        axL.text(x, v + max(arpu) * 0.02, com(v, 2), ha="center", va="bottom",
                 fontsize=7.4, fontweight="bold", color=P["tinta"])
    axL.set_xticks(xs)
    axL.set_xticklabels([r["nombre"] for r in regs], fontsize=7, rotation=18, ha="right")
    axL.set_title("ARPU Premium por region (EUR/mes)", fontsize=8.6,
                  fontweight="bold", color=P["tinta"], pad=6)

    yrs = d["mix"]["anios"]
    x2 = np.arange(len(yrs))
    axR.plot(x2, d["mix"]["arpu_global"], color=P["rojo"], lw=2.2, marker="o", ms=4)
    axR.set_xticks(x2)
    axR.set_xticklabels(yrs, fontsize=7.4)
    axR.set_title("ARPU global: la erosion por mix (EUR/mes)", fontsize=8.6,
                  fontweight="bold", color=P["tinta"], pad=6)
    for x, v in zip(x2, d["mix"]["arpu_global"]):
        axR.text(x, v + 0.03, com(v, 2), ha="center", va="bottom",
                 fontsize=6.8, color=P["gris"])

    deco([axL, axR], d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_cohortes")


# ─────────────────────────────────────────────────────────────────────────────
# 8. c_moat — Capas del foso y anios de defensa
# ─────────────────────────────────────────────────────────────────────────────
def c_moat():
    d = SPEC["moat"]
    capas = d["capas"]

    fig, ax = new_fig()
    ys = np.arange(len(capas))
    anios = [c["anios"] for c in capas]
    cols = [_estado_col(c["estado"]) for c in capas]
    ax.barh(ys, anios, height=0.55, color=cols, zorder=3)
    for y, c in zip(ys, capas):
        ax.text(c["anios"] + 0.25, y, c["defensa"], va="center", ha="left",
                fontsize=7.2, color=P["gris"], style="italic")
    ax.set_yticks(ys)
    ax.set_yticklabels([c["nombre"] for c in capas], fontsize=7.6)
    ax.invert_yaxis()
    ax.set_xlabel("Anios de defensa estimados", fontsize=8)
    ax.set_xlim(0, max(anios) * 1.45)
    ax.grid(axis="x", color=P["gris_linea"], lw=0.6)
    ax.grid(axis="y", visible=False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_moat")


# ─────────────────────────────────────────────────────────────────────────────
# 9. c_cuota — Cuota global de suscriptores por plataforma
# ─────────────────────────────────────────────────────────────────────────────
def c_cuota():
    d = SPEC["cuota"]
    pl = d["plataformas"]

    fig, ax = new_fig()
    xs = np.arange(len(pl))
    vals = [p["cuota"] for p in pl]
    cols = [P["azul"] if p.get("foco") else P["gris_medio"] for p in pl]
    ax.bar(xs, vals, width=0.58, color=cols, zorder=3)
    for x, p in zip(xs, pl):
        ax.text(x, p["cuota"] + 0.6, com(p["cuota"], 1) + "%", ha="center",
                va="bottom", fontsize=8, fontweight="bold", color=P["tinta"])
        ax.text(x, -max(vals) * 0.09, p["tipo"], ha="center", va="top",
                fontsize=6.4, color=P["gris"], style="italic")
    ax.set_xticks(xs)
    ax.set_xticklabels([p["nombre"] for p in pl], fontsize=7.4)
    ax.set_ylim(0, max(vals) * 1.2)
    ax.set_ylabel("Cuota global de suscriptores (%)", fontsize=8)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_cuota")


# ─────────────────────────────────────────────────────────────────────────────
# 10. c_matriz — Matriz de posicionamiento competitivo
# ─────────────────────────────────────────────────────────────────────────────
def c_matriz():
    d = SPEC["matriz"]
    comp = d["competidores"]

    fig, ax = new_fig()
    for c in comp:
        col = P["rojo"] if c.get("foco") else P["azul_acero"]
        r = 0.052 if c.get("foco") else 0.038
        ax.add_patch(Circle((c["x"], c["y"]), r * 10, color=col,
                            alpha=0.85 if c.get("foco") else 0.6, zorder=3))
        ax.text(c["x"], c["y"] - 0.55, c["nombre"], ha="center", va="top",
                fontsize=7.2, color=P["tinta"],
                fontweight="bold" if c.get("foco") else "normal", zorder=4)
    ax.axvline(5, color=P["gris_linea"], lw=0.8, ls="--")
    ax.axhline(5, color=P["gris_linea"], lw=0.8, ls="--")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xlabel(d["eje_x"], fontsize=8)
    ax.set_ylabel(d["eje_y"], fontsize=8)
    ax.grid(axis="y", visible=False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_matriz")


# ─────────────────────────────────────────────────────────────────────────────
# 11. c_fuerzas — Cinco fuerzas de Porter (radar /25)
# ─────────────────────────────────────────────────────────────────────────────
def c_fuerzas():
    d = SPEC["fuerzas"]
    fz = d["fuerzas"]
    labels = [f["nombre"] for f in fz]
    vals = [f["score"] for f in fz]
    n = len(vals)
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    ang += ang[:1]
    sc = vals + vals[:1]

    fig, ax = new_fig(polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 5)
    ax.plot(ang, [5] * (n + 1), color=P["gris_medio"], lw=1.0, ls="--", alpha=0.7)
    ax.plot(ang, sc, color=P["rojo_oscuro"], lw=2.0)
    ax.fill(ang, sc, color=P["rojo_oscuro"], alpha=0.32)
    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(labels, fontsize=7.2, color=P["tinta"])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=P["gris_medio"])

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_fuerzas")


# ─────────────────────────────────────────────────────────────────────────────
# 12. c_tam — Embudo TAM / SAM / SOM
# ─────────────────────────────────────────────────────────────────────────────
def c_tam():
    d = SPEC["tam"]
    niveles = d["niveles"]

    fig, ax = new_fig()
    ax.axis("off")
    n = len(niveles)
    maxv = max(x["valor"] for x in niveles)
    for i, lv in enumerate(niveles):
        w = lv["valor"] / maxv
        y = n - i - 1
        x0 = (1 - w) / 2
        col = [P["azul_noche"], P["azul"], P["azul_acero"], P["verde"]][i % 4]
        ax.add_patch(Rectangle((x0, y + 0.12), w, 0.72, color=col, zorder=3))
        ax.text(0.5, y + 0.48, f"{lv['nombre']}  ·  {lv['label']}", ha="center",
                va="center", fontsize=8.4, color=P["fondo"], fontweight="bold", zorder=4)
        if lv.get("nota"):
            ax.text(1.02, y + 0.48, lv["nota"], ha="left", va="center",
                    fontsize=6.9, color=P["gris"], style="italic", zorder=4)
    ax.set_xlim(0, 1.42)
    ax.set_ylim(0, n)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_tam")


# ─────────────────────────────────────────────────────────────────────────────
# 13. c_precios — Poder de precio latente: SPOT vs NFLX
# ─────────────────────────────────────────────────────────────────────────────
def c_precios():
    d = SPEC["precios"]
    yrs = d["anios"]
    xs = np.arange(len(yrs))

    fig, ax = new_fig()
    ax.plot(xs, d["spot"], color=P["azul"], lw=2.3, marker="o", ms=4.5, label="Spotify Premium (US$/mes)")
    ax.plot(xs, d["nflx"], color=P["rojo_oscuro"], lw=2.3, marker="s", ms=4.5, label="Netflix estandar (US$/mes)")
    for x, v in zip(xs, d["spot"]):
        ax.text(x, v - 0.75, com(v, 2), ha="center", va="top", fontsize=6.8, color=P["azul"])
    for x, v in zip(xs, d["nflx"]):
        ax.text(x, v + 0.45, com(v, 2), ha="center", va="bottom", fontsize=6.8, color=P["rojo_oscuro"])
    ax.set_xticks(xs)
    ax.set_xticklabels(yrs, fontsize=7.6)
    ax.set_ylabel("Precio mensual (US$)", fontsize=8)
    ax.legend(fontsize=7.4, loc="upper left", frameon=False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_precios")


# ─────────────────────────────────────────────────────────────────────────────
# 14. c_dcf — DCF en tres escenarios
# ─────────────────────────────────────────────────────────────────────────────
def c_dcf():
    d = SPEC["dcf"]
    esc = d["escenarios"]

    fig, ax = new_fig()
    xs = np.arange(len(esc))
    vals = [e["valor"] for e in esc]
    cols = [P["rojo_oscuro"], P["azul"], P["verde"]]
    ax.bar(xs, vals, width=0.5, color=cols[:len(esc)], zorder=3)
    for x, e in zip(xs, esc):
        ax.text(x, e["valor"] + max(vals) * 0.02, "US$" + com(e["valor"], 0),
                ha="center", va="bottom", fontsize=9, fontweight="bold", color=P["tinta"])
        ax.text(x, -max(vals) * 0.075, f"prob. {int(e['prob'] * 100)}%",
                ha="center", va="top", fontsize=7.2, color=P["gris"], style="italic")
    ax.axhline(d["precio_hoy"], color=P["tinta"], lw=1.6, zorder=4)
    ax.text(len(esc) - 0.4, d["precio_hoy"] + max(vals) * 0.015,
            "HOY US$" + com(d["precio_hoy"], 2), ha="right", va="bottom",
            fontsize=7.6, color=P["tinta"], fontweight="bold")
    ax.axhline(d["ponderado"], color=P["rojo"], lw=1.5, ls="--", zorder=4)
    ax.text(0.05, d["ponderado"] + max(vals) * 0.015,
            "ponderado US$" + com(d["ponderado"], 0), ha="left", va="bottom",
            fontsize=7.6, color=P["rojo"], fontweight="bold")
    ax.set_xticks(xs)
    ax.set_xticklabels([e["nombre"] for e in esc], fontsize=8)
    ax.set_ylim(0, max(vals) * 1.2)
    ax.set_ylabel("Valor por accion (US$)", fontsize=8)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_dcf")


# ─────────────────────────────────────────────────────────────────────────────
# 15. c_zonas — Mapa de zonas de valoracion con HOY
# ─────────────────────────────────────────────────────────────────────────────
def c_zonas():
    d = SPEC["zonas"]
    pwfv = d["pwfv"]
    xmin, xmax = d["xmin"], d["xmax"]

    bandas = [
        (xmin, pwfv * 0.75, P["verde"], "GANGA"),
        (pwfv * 0.75, pwfv * 0.85, P["azul_acero"], "OPORTUNIDAD"),
        (pwfv * 0.85, pwfv * 1.15, P["ocre"], "PRECIO JUSTO"),
        (pwfv * 1.15, pwfv * 1.35, P["terracota"], "CARO"),
        (pwfv * 1.35, xmax, P["rojo_oscuro"], "BURBUJA"),
    ]

    fig, ax = new_fig()
    yb = 0.35
    for x0, x1, c, name in bandas:
        if x1 <= x0:
            continue
        ax.add_patch(Rectangle((x0, 0), x1 - x0, yb, color=c, alpha=0.55, zorder=1))
        rot, fs = (0, 7.2) if (x1 - x0) >= (xmax - xmin) * 0.13 else (90, 6.0)
        ax.text((x0 + x1) / 2, yb / 2, name, ha="center", va="center",
                rotation=rot, fontsize=fs, color=P["fondo"], fontweight="bold", zorder=2)

    def marca(x, label, color, dy, ls="-"):
        ax.plot([x, x], [0, yb + 0.30 + dy], color=color, lw=1.7, ls=ls, zorder=4)
        ax.text(x, yb + 0.32 + dy, label, ha="center", va="bottom",
                fontsize=7.2, color=color, fontweight="bold", zorder=5)

    for m in d["marcas"]:
        if not (xmin <= m["x"] <= xmax):
            continue          # marca fuera del rango dibujado: no dejar la etiqueta flotando
        marca(m["x"], m["label"], {"tinta": P["tinta"], "rojo": P["rojo"],
                                   "gris": P["gris"], "verde": P["verde"],
                                   "azul": P["azul"]}.get(m["color"], P["tinta"]),
              m.get("dy", 0.0), m.get("ls", "-"))

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(0, 1.75)
    ax.set_yticks([])
    ax.set_xlabel("Precio por accion (US$)", fontsize=8)
    ax.grid(axis="y", visible=False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_zonas")


# ─────────────────────────────────────────────────────────────────────────────
# 16. c_sens — Heatmap sensibilidad WACC x crecimiento terminal
# ─────────────────────────────────────────────────────────────────────────────
def c_sens():
    d = SPEC["sensibilidad"]
    M = np.array(d["matriz"], dtype=float)
    waccs, gs = d["waccs"], d["terminales"]
    precio = d["precio_hoy"]

    fig, ax = new_fig()
    im = ax.imshow(M, cmap="RdYlGn", aspect="auto", vmin=M.min(), vmax=M.max())
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            v = M[i, j]
            ax.text(j, i, com(v, 0), ha="center", va="center", fontsize=7.6,
                    color=P["tinta"],
                    fontweight="bold" if v >= precio else "normal")
    ax.set_xticks(range(len(gs)))
    ax.set_xticklabels([com(g, 1) + "%" for g in gs], fontsize=7.6)
    ax.set_yticks(range(len(waccs)))
    ax.set_yticklabels([com(w, 1) + "%" for w in waccs], fontsize=7.6)
    ax.set_xlabel("Crecimiento terminal", fontsize=8)
    ax.set_ylabel("WACC", fontsize=8)
    ax.grid(False)
    cb = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
    cb.ax.tick_params(labelsize=6.5)
    cb.outline.set_visible(False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_sens")


# ─────────────────────────────────────────────────────────────────────────────
# 17. c_dcfinv — DCF inverso: que crecimiento descuenta el precio
# ─────────────────────────────────────────────────────────────────────────────
def c_dcfinv():
    d = SPEC["dcf_inverso"]
    barras = d["barras"]

    fig, ax = new_fig()
    ys = np.arange(len(barras))
    vals = [b["valor"] for b in barras]
    cols = [_estado_col(b.get("estado", "gris")) for b in barras]
    ax.barh(ys, vals, height=0.55, color=cols, zorder=3)
    for y, b in zip(ys, barras):
        ax.text(b["valor"] + max(vals) * 0.015, y, com(b["valor"], 1) + "%",
                va="center", ha="left", fontsize=8, fontweight="bold", color=P["tinta"])
    ax.axvline(d["implicito"], color=P["rojo"], lw=1.6, ls="--", zorder=4)
    ax.text(d["implicito"], len(barras) - 0.35,
            "  implicito en el precio: " + com(d["implicito"], 1) + "%",
            va="center", ha="left", fontsize=7.4, color=P["rojo"],
            fontweight="bold", style="italic")
    ax.set_yticks(ys)
    ax.set_yticklabels([b["nombre"] for b in barras], fontsize=7.6)
    ax.invert_yaxis()
    ax.set_xlabel("Crecimiento anual de ingresos, anios 1-5 (%)", fontsize=8)
    ax.set_xlim(0, max(vals) * 1.28)
    ax.grid(axis="x", color=P["gris_linea"], lw=0.6)
    ax.grid(axis="y", visible=False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_dcfinv")


# ─────────────────────────────────────────────────────────────────────────────
# 18. c_mgmt — Radar de management (6 dimensiones)
# ─────────────────────────────────────────────────────────────────────────────
def c_mgmt():
    d = SPEC["management"]
    dims = d["dimensiones"]
    labels = [x["nombre"] for x in dims]
    vals = [x["score"] for x in dims]
    n = len(vals)
    ang = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    ang += ang[:1]
    sc = vals + vals[:1]

    fig, ax = new_fig(polar=True)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 5)
    ax.plot(ang, [5] * (n + 1), color=P["gris_medio"], lw=1.0, ls="--", alpha=0.7)
    ax.plot(ang, sc, color=P["azul"], lw=2.0)
    ax.fill(ang, sc, color=P["azul"], alpha=0.32)
    ax.set_xticks(ang[:-1])
    ax.set_xticklabels(labels, fontsize=6.9, color=P["tinta"])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=P["gris_medio"])

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_mgmt")


# ─────────────────────────────────────────────────────────────────────────────
# 19. c_retorno — Retorno al accionista y dilucion
# ─────────────────────────────────────────────────────────────────────────────
def c_retorno():
    d = SPEC["retorno"]
    yrs = d["anios"]
    xs = np.arange(len(yrs))

    fig, ax = new_fig()
    ax.bar(xs, d["recompras"], width=0.55, color=P["verde"], zorder=3,
           label="Recompras (M EUR)")
    ax.bar(xs, [-s for s in d["sbc"]], width=0.55, color=P["rojo_oscuro"], zorder=3,
           label="SBC (M EUR, negativo)")
    ax.axhline(0, color=P["gris_medio"], lw=0.9)
    ax2 = ax.twinx()
    ax2.plot(xs, d["acciones"], color=P["tinta"], lw=2.0, marker="o", ms=4,
             label="Acciones diluidas (M)")
    ax2.set_ylabel("Acciones diluidas (M)", fontsize=8)
    ax2.grid(False)
    for s in ["top", "right", "left"]:
        ax2.spines[s].set_visible(False)
    ax.set_xticks(xs)
    ax.set_xticklabels(yrs, fontsize=8)
    ax.set_ylabel("M EUR", fontsize=8)
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, fontsize=6.8, loc="upper left", ncol=1,
              frameon=True, facecolor=P["fondo"], edgecolor="none", framealpha=0.85)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_retorno")


# ─────────────────────────────────────────────────────────────────────────────
# 20. c_inversores — Panel de los nueve veredictos
# ─────────────────────────────────────────────────────────────────────────────
def c_inversores():
    d = SPEC["inversores"]
    inv = d["panel"]
    col_v = {"BUY": P["verde"], "HOLD": P["ocre"], "PASS": P["rojo_oscuro"]}

    fig, ax = new_fig(figsize=(7.2, 4.6))
    ys = np.arange(len(inv))
    vals = [i["conviccion"] for i in inv]
    cols = [col_v.get(i["veredicto"], P["gris"]) for i in inv]
    ax.barh(ys, vals, height=0.6, color=cols, zorder=3)
    for y, i in zip(ys, inv):
        ax.text(i["conviccion"] + 0.15, y, i["veredicto"], va="center", ha="left",
                fontsize=7.2, fontweight="bold", color=col_v.get(i["veredicto"], P["gris"]))
    ax.set_yticks(ys)
    ax.set_yticklabels([i["nombre"] for i in inv], fontsize=7.6)
    ax.invert_yaxis()
    ax.set_xlim(0, 10.8)
    ax.set_xlabel("Nivel de conviccion (0-10)", fontsize=8)
    ax.grid(axis="x", color=P["gris_linea"], lw=0.6)
    ax.grid(axis="y", visible=False)
    ax.legend(handles=[Line2D([0], [0], color=col_v[k], lw=6, label=k)
                       for k in ["BUY", "HOLD", "PASS"]],
              fontsize=7, loc="lower right", frameon=False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_inversores")


# ─────────────────────────────────────────────────────────────────────────────
# 21. c_riesgos — Heatmap probabilidad x impacto
# ─────────────────────────────────────────────────────────────────────────────
def c_riesgos():
    d = SPEC["riesgos"]
    rs = d["riesgos"]

    fig, ax = new_fig()
    for i in range(1, 6):
        for j in range(1, 6):
            sc = i * j
            c = P["verde"] if sc <= 6 else (P["ocre"] if sc <= 12 else P["rojo_oscuro"])
            ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, color=c, alpha=0.16, zorder=1))
    for r in rs:
        ax.plot(r["impacto"], r["probabilidad"], "o", ms=9,
                color=P["rojo"] if r["impacto"] * r["probabilidad"] >= 12 else P["azul"], zorder=4)
        ax.text(r["impacto"], r["probabilidad"] + 0.22, r["id"], ha="center", va="bottom",
                fontsize=7.4, fontweight="bold", color=P["tinta"], zorder=5)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel("Impacto (1-5)", fontsize=8)
    ax.set_ylabel("Probabilidad (1-5)", fontsize=8)
    ax.grid(color=P["gris_linea"], lw=0.5)

    leg = "  ·  ".join(f"{r['id']}: {r['nombre']}" for r in rs)
    fig.text(0.012, 0.045, leg, fontsize=6.3, style="italic", color=P["gris"], ha="left")

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_riesgos")


# ─────────────────────────────────────────────────────────────────────────────
# 22. c_proy — Proyeccion a 5 anios en tres escenarios
# ─────────────────────────────────────────────────────────────────────────────
def c_proy():
    d = SPEC["proyeccion"]
    yrs = d["anios"]
    xs = np.arange(len(yrs))

    fig, ax = new_fig()
    for nombre, serie, col in [("Conservador", d["conservador"], P["rojo_oscuro"]),
                               ("Base", d["base"], P["azul"]),
                               ("Optimista", d["optimista"], P["verde"])]:
        ax.plot(xs, serie, color=col, lw=2.2, marker="o", ms=4, label=nombre)
        ax.text(xs[-1] + 0.08, serie[-1], "US$" + com(serie[-1], 0), va="center",
                ha="left", fontsize=7.4, color=col, fontweight="bold")
    ax.axhline(d["precio_hoy"], color=P["tinta"], lw=1.3, ls=":", zorder=2)
    ax.text(0, d["precio_hoy"] * 1.02, "HOY US$" + com(d["precio_hoy"], 2),
            ha="left", va="bottom", fontsize=7.2, color=P["tinta"], style="italic")
    ax.set_xticks(xs)
    ax.set_xticklabels(yrs, fontsize=8)
    ax.set_xlim(-0.2, len(yrs) - 0.35)
    ax.set_ylabel("Precio por accion (US$)", fontsize=8)
    ax.legend(fontsize=7.4, loc="upper left", frameon=False)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_proy")


# ─────────────────────────────────────────────────────────────────────────────
# 23. c_ew — Semaforo early-warning
# ─────────────────────────────────────────────────────────────────────────────
def c_ew():
    d = SPEC["early_warning"]
    kpis = d["kpis"]
    txt = {"verde": "VERDE", "ambar": "AMBAR", "rojo": "ROJO", "gris": "SIN DATO"}

    fig, ax = new_fig(figsize=(7.2, 4.4))
    ax.axis("off")
    n = len(kpis)
    row_h = 1.0
    y0 = n * row_h
    for i, k in enumerate(kpis):
        y = y0 - (i + 1) * row_h
        c = _estado_col(k["estado"])
        if i % 2 == 0:
            ax.add_patch(Rectangle((0, y), 10, row_h, color=P["gris_claro"], alpha=0.5, zorder=0))
        ax.text(0.15, y + row_h / 2, k["kpi"], va="center", ha="left",
                fontsize=7.4, color=P["tinta"], zorder=2)
        ax.add_patch(Rectangle((5.85, y + 0.18), 0.95, row_h - 0.36, color=c, zorder=2))
        ax.text(6.325, y + row_h / 2, txt[k["estado"]], va="center", ha="center",
                fontsize=6.1, color=P["fondo"], fontweight="bold", zorder=3)
        ax.text(7.00, y + row_h / 2, k["valor"].replace(".", ","), va="center", ha="left",
                fontsize=6.9, color=P["gris"], style="italic", zorder=2)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, y0)

    deco(ax, d["titulo"], d["sub"], FUENTE, fig=fig)
    save(fig, "c_ew")


def main():
    fns = [c_radar, c_tier, c_escalabilidad, c_margen, c_ingresos_fcf, c_segments,
           c_cohortes, c_moat, c_cuota, c_matriz, c_fuerzas, c_tam, c_precios,
           c_dcf, c_zonas, c_sens, c_dcfinv, c_mgmt, c_retorno, c_inversores,
           c_riesgos, c_proy, c_ew]
    ok, fail = [], []
    for f in fns:
        try:
            f()
            ok.append(f.__name__)
        except Exception as e:
            fail.append((f.__name__, repr(e)))
    print(f"OK ({len(ok)}): {', '.join(ok)}")
    if fail:
        print(f"FALLARON ({len(fail)}):")
        for n, e in fail:
            print("  -", n, "→", e)


if __name__ == "__main__":
    main()
