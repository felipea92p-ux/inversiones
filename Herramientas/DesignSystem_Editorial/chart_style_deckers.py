# -*- coding: utf-8 -*-
"""CHART STYLE · editorial cálido (referencia Deckers) — sin banda de título propia,
sin rejilla, barras planas, leyenda de fuente centrada debajo. Prueba para ESLOY."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from paleta_deckers import PALETA as P

plt.rcParams.update({
    "font.family": "DejaVu Serif", "font.size": 9.5,
    "figure.facecolor": P["fondo"], "axes.facecolor": P["fondo"],
    "savefig.facecolor": P["fondo"], "text.color": P["tinta"],
    "axes.labelcolor": P["gris"], "xtick.color": P["tinta"], "ytick.color": P["gris"]})


def deco(ax, fuente, fig=None):
    """Sin título ni flag — solo fuente al pie, sin rejilla, sin spines salvo la base."""
    fig = fig or (ax[0].figure if isinstance(ax, (list, np.ndarray)) else ax.figure)
    fig.text(0.5, 0.015, fuente, fontsize=7.6, style="italic", ha="center", color=P["gris"])
    for a in (ax if isinstance(ax, (list, np.ndarray)) else [ax]):
        if a.name == "polar":
            continue
        a.grid(False)
        a.set_axisbelow(True)
        for s in ["top", "right", "left"]:
            a.spines[s].set_visible(False)
        a.spines["bottom"].set_color(P["gris_linea"])
        a.spines["bottom"].set_linewidth(0.8)
        a.tick_params(length=0)


def save(fig, name, outdir="charts"):
    import os
    os.makedirs(outdir, exist_ok=True)
    fig.savefig(f"{outdir}/{name}.png", dpi=150)
    plt.close(fig)
