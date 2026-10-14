# -*- coding: utf-8 -*-
"""CHART STYLE · Economist-style matplotlib setup for QG documents.
Import this at the top of any make_charts_<ticker>.py file.

KNOWN PITFALLS (learned the hard way — do not repeat):
1. NEVER put two or more '$' characters in a title/subtitle string:
   matplotlib parses $...$ as mathtext and garbles the text. Write
   "12,1B operativos (US$)" instead of "$12,1B operativos a $1,5B".
   Single '$' inside f-string data labels (ax.text) is fine.
2. Keep ONE thousands-separator convention per document. House style:
   US format for dollar amounts ($1,950), Spanish decimal comma for
   percentages in labels (−9,8%). Enforce with .replace(".", ",") only
   on percentage strings, never on dollar figures.
3. Charts must share the page's cream background: rcParams below handle
   it, but never override facecolor to white.
4. Save at dpi=150, embed at 15-17 cm width via motor_qg.chart().
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from paleta_qg import PALETA as P

plt.rcParams.update({
    "font.family": "DejaVu Serif", "font.size": 9,
    "figure.facecolor": P["fondo"], "axes.facecolor": P["fondo"],
    "savefig.facecolor": P["fondo"], "axes.edgecolor": P["gris_linea"],
    "text.color": P["tinta"], "axes.labelcolor": P["gris"],
    "xtick.color": P["gris"], "ytick.color": P["gris"]})


def deco(ax, titulo, sub, fuente, fig=None, flag_y=0.985):
    """Economist furniture: red flag, bold serif title, italic subtitle,
    italic source line, horizontal-only hairline grid, no spines but X."""
    fig = fig or (ax[0].figure if isinstance(ax, (list, np.ndarray)) else ax.figure)
    fig.patches.append(Rectangle((0.012, flag_y - 0.012), 0.055, 0.022,
                       transform=fig.transFigure, color=P["rojo"], zorder=5))
    fig.text(0.012, flag_y - 0.075, titulo, fontsize=12, fontweight="bold",
             family="DejaVu Serif", ha="left", color=P["tinta"])
    fig.text(0.012, flag_y - 0.125, sub, fontsize=8.6, style="italic",
             ha="left", color=P["gris"])
    fig.text(0.012, 0.012, fuente, fontsize=7.2, style="italic",
             ha="left", color=P["gris"])
    for a in (ax if isinstance(ax, (list, np.ndarray)) else [ax]):
        if a.name == "polar":          # radar: no cartesian spines
            continue
        a.grid(axis="y", color=P["gris_linea"], lw=0.6, alpha=0.9)
        a.set_axisbelow(True)
        for s in ["top", "right", "left"]:
            a.spines[s].set_visible(False)
        a.spines["bottom"].set_color(P["gris_linea"])
        a.tick_params(length=0)


def save(fig, name, outdir="charts"):
    import os
    os.makedirs(outdir, exist_ok=True)
    fig.savefig(f"{outdir}/{name}.png", dpi=150)
    plt.close(fig)


# Recommended series order (most to least prominent):
ORDEN_SERIES = [P["azul"], P["azul_acero"], P["azul_pro"] if "azul_pro" in P else P["azul_cielo"],
                P["azul_cielo"], P["verde"], P["terracota"], P["ocre"]]

# Semantic colors:
#   escenario pesimista / negativo / alerta -> P["rojo_oscuro"]
#   escenario base / serie principal        -> P["azul"]
#   escenario optimista / positivo          -> P["verde"]
#   umbral / línea clave / PWFV             -> P["rojo"] (dashed)
#   "HOY" / precio actual                   -> P["tinta"] (solid)
#   zona neutral / HOLD                     -> P["ocre"]
