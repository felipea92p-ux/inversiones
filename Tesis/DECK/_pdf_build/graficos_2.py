# -*- coding: utf-8 -*-
"""GRÁFICOS 2 · ULTRA TESIS DECK — c05, c06, c07, c08.

c05_dos_marcas       · §7 · márgenes de segmento UGG contra HOKA, FY2024-FY2026
c06_hoka_coste       · §7 · lo que HOKA gasta por cada dólar nuevo, indexado a 100
c07_empuje_tiron     · §8 · mayorista contra venta directa por marca, FY2026
c08_margen_incremental · §6 · incremental 41,6 → 36,1 → 17,2 contra el margen medio

Todas las cifras salen de DATOS.md y de ningún otro sitio.
"""
import sys; sys.path.insert(0, "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build")
import os
os.chdir("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build")

import numpy as np, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from chart_style import deco, save
from paleta_qg import PALETA as P

ACC = "acc. 0001628280-26-037664"


# ══════════════════════════════════════════════════════════════════════════
# c05 · LAS DOS MARCAS: la que crece pierde margen, la que no crece lo defiende
# ══════════════════════════════════════════════════════════════════════════
def c05_dos_marcas():
    anios = ["FY2024", "FY2025", "FY2026"]
    x = np.arange(3)

    ugg_op,  hoka_op = [35.9, 39.6, 38.2], [39.8, 38.0, 35.2]
    ugg_br,  hoka_br = [56.1, 59.6, 59.3], [57.7, 57.5, 56.9]

    fig, (a1, a2) = plt.subplots(
        1, 2, figsize=(7.2, 4.2), gridspec_kw={"width_ratios": [1.55, 1.0]})
    fig.subplots_adjust(top=0.775, bottom=0.195, left=0.062, right=0.975, wspace=0.24)

    # ── panel izquierdo · margen OPERATIVO de segmento ────────────────────
    a1.plot(x, ugg_op,  "-o", color=P["azul"], lw=2.6, ms=7,
            label="UGG · margen operativo", zorder=4)
    a1.plot(x, hoka_op, "-o", color=P["rojo_oscuro"], lw=2.6, ms=7,
            label="HOKA · margen operativo", zorder=4)

    off_ugg  = [(-0.62, "top", -0.16, "right"), (+0.62, "bottom", 0.0, "center"),
                (+0.62, "bottom", 0.0, "center")]
    off_hoka = [(-0.62, "top"),    (-0.62, "top"),    (-0.62, "top")]
    for i in range(3):
        d, va, ddx, hha = off_ugg[i]
        a1.text(x[i] + ddx, ugg_op[i] + d, f"{ugg_op[i]:.1f}%".replace(".", ","),
                ha=hha, va=va, fontsize=9.2, color=P["azul"], fontweight="bold")
        d, va = off_hoka[i]
        a1.text(x[i], hoka_op[i] + d, f"{hoka_op[i]:.1f}%".replace(".", ","),
                ha="center", va=va, fontsize=9.2, color=P["rojo_oscuro"], fontweight="bold")

    # el cruce: 35,9 + t·3,7 = 39,8 − t·1,8  ⇒  t = 0,709
    tc, yc = 0.7091, 35.9 + 0.7091 * 3.7
    a1.plot([tc], [yc], "o", ms=11, mfc="none", mec=P["tinta"], mew=1.6, zorder=6)
    a1.annotate("Aquí se cruzan:\nUGG adelanta a HOKA",
                xy=(tc, yc - 0.30), xytext=(-0.74, 33.05),
                fontsize=8.8, color=P["tinta"], ha="left", va="bottom",
                arrowprops=dict(arrowstyle="-|>", color=P["tinta"], lw=1.1,
                                shrinkA=6, shrinkB=3,
                                connectionstyle="arc3,rad=0.28"))

    a1.annotate("", xy=(2.30, 39.8), xytext=(2.30, 35.2),
                arrowprops=dict(arrowstyle="<->", color=P["rojo_oscuro"], lw=1.3))
    a1.text(2.37, 37.5, "HOKA\n−460 pb", fontsize=8.8, color=P["rojo_oscuro"],
            fontweight="bold", ha="left", va="center")
    a1.annotate("", xy=(-0.09, 35.9), xytext=(-0.09, 38.2),
                arrowprops=dict(arrowstyle="<->", color=P["azul"], lw=1.3))
    a1.text(-0.16, 37.05, "UGG\n+230 pb", fontsize=8.8, color=P["azul"],
            fontweight="bold", ha="right", va="center")

    a1.set_xticks(x); a1.set_xticklabels(anios, fontsize=9.4)
    a1.set_xlim(-0.80, 3.05); a1.set_ylim(32.8, 42.6)
    a1.set_yticks([34, 36, 38, 40, 42])
    a1.set_yticklabels(["34%", "36%", "38%", "40%", "42%"], fontsize=8.6)
    a1.legend(frameon=False, loc="upper left", fontsize=8.8,
              handlelength=1.6, borderaxespad=0.2)
    a1.text(0.0, 1.045, "M A R G E N   O P E R A T I V O   D E   S E G M E N T O",
            transform=a1.transAxes, fontsize=8.0, color=P["gris"], fontweight="bold")

    # ── panel derecho · margen BRUTO ──────────────────────────────────────
    a2.plot(x, ugg_br,  "-o", color=P["azul"], lw=2.2, ms=6, zorder=4)
    a2.plot(x, hoka_br, "-o", color=P["rojo_oscuro"], lw=2.2, ms=6, zorder=4)

    br_off = {"ugg": [(-0.42, "top"), (+0.42, "bottom"), (+0.42, "bottom")],
              "hoka": [(+0.42, "bottom"), (-0.42, "top"), (-0.42, "top")]}
    for i in range(3):
        d, va = br_off["ugg"][i]
        a2.text(x[i], ugg_br[i] + d, f"{ugg_br[i]:.1f}".replace(".", ","),
                ha="center", va=va, fontsize=8.8, color=P["azul"], fontweight="bold")
        d, va = br_off["hoka"][i]
        a2.text(x[i], hoka_br[i] + d, f"{hoka_br[i]:.1f}".replace(".", ","),
                ha="center", va=va, fontsize=8.8, color=P["rojo_oscuro"], fontweight="bold")

    a2.set_xticks(x); a2.set_xticklabels(anios, fontsize=9.4)
    a2.set_xlim(-0.42, 2.42); a2.set_ylim(54.4, 61.6)
    a2.set_yticks([55, 57, 59, 61])
    a2.set_yticklabels(["55%", "57%", "59%", "61%"], fontsize=8.6)
    a2.text(0.0, 1.045, "M A R G E N   B R U T O", transform=a2.transAxes,
            fontsize=8.0, color=P["gris"], fontweight="bold")

    fig.text(0.062, 0.050,
             "El margen bruto de HOKA apenas se mueve en dos años: −80 pb. Lo que HOKA pierde no lo pierde\n"
             "fabricando ni vendiendo barato — lo pierde en gasto comercial (SG&A).",
             fontsize=8.8, color=P["rojo"], style="italic", ha="left", va="bottom",
             linespacing=1.5)

    deco(a1,
         "La marca que crece pierde margen; la que no crece lo defiende",
         "Deckers por segmento, FY2024-FY2026. HOKA cede 460 puntos básicos de margen operativo; UGG gana 230.",
         "10-K FY2026 · nota 13 de segmentos · EDGAR 0001628280-26-037664",
         fig=fig)
    deco(a2, "", "", "", fig=fig)   # rejilla y ejes del segundo panel
    save(fig, "c05_dos_marcas")


# ══════════════════════════════════════════════════════════════════════════
# c06 · LO QUE HOKA GASTA POR CADA DÓLAR NUEVO
# ══════════════════════════════════════════════════════════════════════════
def c06_hoka_coste():
    x = np.arange(3)
    series = [
        ("Ingresos",             [100, 124, 143], P["azul"],        2.9, 143, -8.0),
        ("Marketing",            [100, 129, 150], P["azul_acero"],  2.1, 150, +8.0),
        ("Nóminas",              [100, 135, 174], P["terracota"],   2.1, 174,  0.0),
        ("Alquiler y ocupación", [100, 160, 278], P["rojo_oscuro"], 2.6, 278,  0.0),
    ]

    fig, ax = plt.subplots(figsize=(7.2, 4.21))
    fig.subplots_adjust(top=0.775, bottom=0.145, left=0.062, right=0.985)

    ax.axhline(100, color=P["gris_linea"], lw=1.2, zorder=1)
    ax.fill_between(x, series[0][1], series[3][1], color=P["rojo_oscuro"],
                    alpha=0.075, lw=0, zorder=1)

    for nombre, v, col, lw, fin, dy in series:
        ax.plot(x, v, "-o", color=col, lw=lw, ms=6.4, zorder=4)
        ax.text(2.09, fin + dy, f"{nombre}   {fin}", fontsize=9.2, color=col,
                fontweight="bold", ha="left", va="center")

    ax.text(0.09, 272,
            "Todo lo que queda por encima de la línea\n"
            "de ingresos —la zona sombreada— es\n"
            "margen que se va.",
            fontsize=9.2, color=P["rojo_oscuro"], ha="left", va="top",
            style="italic", linespacing=1.5)

    ax.set_xticks(x)
    ax.set_xticklabels(["FY2024", "FY2025", "FY2026"], fontsize=9.6)
    ax.set_xlim(-0.14, 3.02)
    ax.set_ylim(82, 300)
    ax.set_yticks([100, 150, 200, 250, 300])
    ax.tick_params(axis="y", labelsize=8.6)

    deco(ax,
         "Los tres costes de HOKA crecen más rápido que sus ingresos",
         "Base 100 en FY2024. El alquiler crece casi el doble de rápido que las ventas; las nóminas, un 74% en dos años.",
         "10-K FY2026 · nota 13 de segmentos · EDGAR 0001628280-26-037664")
    save(fig, "c06_hoka_coste")


# ══════════════════════════════════════════════════════════════════════════
# c07 · EMPUJE CONTRA TIRÓN
# ══════════════════════════════════════════════════════════════════════════
def c07_empuje_tiron():
    grupos = ["HOKA", "UGG", "Grupo Deckers"]
    mayor  = [18.2, 12.7, 12.3]
    dtc    = [12.0,  3.6,  6.3]
    x, w = np.arange(3), 0.32

    fig, ax = plt.subplots(figsize=(7.2, 4.29))
    fig.subplots_adjust(top=0.745, bottom=0.135, left=0.06, right=0.975)

    b1 = ax.bar(x - w / 2, mayor, w, color=P["rojo_oscuro"], zorder=3)
    b2 = ax.bar(x + w / 2, dtc,   w, color=P["azul"], zorder=3)

    for xi, v in zip(x - w / 2, mayor):
        ax.text(xi, v + 0.45, f"+{v:.1f}%".replace(".", ","), ha="center", va="bottom",
                fontsize=9.6, color=P["rojo_oscuro"], fontweight="bold")
    for xi, v in zip(x + w / 2, dtc):
        ax.text(xi, v + 0.45, f"+{v:.1f}%".replace(".", ","), ha="center", va="bottom",
                fontsize=9.6, color=P["azul"], fontweight="bold")

    # la brecha de UGG, medida fuera de las barras para que se lea
    xg = 1.42
    ax.plot([1 - w, xg], [12.7, 12.7], color=P["rojo"], lw=1.0, ls=":", zorder=5)
    ax.plot([1.0,   xg], [3.6,  3.6],  color=P["rojo"], lw=1.0, ls=":", zorder=5)
    ax.annotate("", xy=(xg, 3.6), xytext=(xg, 12.7),
                arrowprops=dict(arrowstyle="<->", color=P["rojo"], lw=1.7))
    ax.text(xg - 0.06, 8.15, "9,1\npuntos", fontsize=9.8, color=P["rojo"],
            fontweight="bold", ha="right", va="center", linespacing=1.35)
    ax.text(1.0, 15.3,
            "UGG: 9,1 puntos de brecha.\nEl mayorista crece 3,5 veces\nmás rápido que el canal propio",
            fontsize=9.2, color=P["rojo"], fontweight="bold", ha="center", va="bottom",
            linespacing=1.45)

    ax.set_xticks(x); ax.set_xticklabels(grupos, fontsize=10.4)
    ax.set_xlim(-0.55, 2.55); ax.set_ylim(0, 21.7)
    ax.set_yticks([0, 5, 10, 15, 20])
    ax.set_yticklabels(["0%", "5%", "10%", "15%", "20%"], fontsize=8.8)
    ax.legend([b1, b2],
              ["Mayorista · el EMPUJE del fabricante", "Venta directa · el TIRÓN del consumidor"],
              frameon=False, loc="lower center", bbox_to_anchor=(0.5, 1.005), ncol=2,
              fontsize=9.0, handlelength=1.5, columnspacing=2.0, borderpad=0.0)

    deco(ax,
         "En UGG el mayorista crece 3,5 veces más rápido que el canal propio",
         "Crecimiento de ingresos en FY2026 por canal y por marca. En las tres columnas el mayorista va por delante.",
         "10-K FY2026 · EDGAR 0001628280-26-037664 · 8-K 21-may-2026")
    save(fig, "c07_empuje_tiron")


# ══════════════════════════════════════════════════════════════════════════
# c08 · MARGEN OPERATIVO INCREMENTAL
# ══════════════════════════════════════════════════════════════════════════
def c08_margen_incremental():
    etiq  = ["FY2023 → FY2024", "FY2024 → FY2025", "FY2025 → FY2026"]
    inc   = [41.6, 36.1, 17.2]
    medio = [21.6, 23.7, 23.1]
    x, w  = np.arange(3), 0.56
    cols  = [P["azul"], P["azul"], P["rojo_oscuro"]]

    fig, ax = plt.subplots(figsize=(7.2, 4.21))
    fig.subplots_adjust(top=0.675, bottom=0.25, left=0.062, right=0.985)

    ax.bar(x, inc, w, color=cols, zorder=3)
    ax.plot(x, medio, "--o", color=P["rojo"], lw=2.0, ms=7, zorder=5)

    for i, (xi, v, c) in enumerate(zip(x, inc, cols)):
        dentro = (i == 2)      # la tercera cae bajo la línea: la cifra va DENTRO de la barra
        ax.text(xi, v - 1.4 if dentro else v + 1.1, f"{v:.1f}%".replace(".", ","),
                ha="center", va="top" if dentro else "bottom",
                fontsize=11.0, color=P["fondo"] if dentro else c, fontweight="bold")
    # etiquetas del margen medio: crema cuando caen sobre la barra, rojo cuando no
    ax.text(0.0, 20.3, "21,6%", ha="center", va="top", fontsize=9.2,
            color=P["fondo"], fontweight="bold")
    ax.text(1.0, 22.4, "23,7%", ha="center", va="top", fontsize=9.2,
            color=P["fondo"], fontweight="bold")
    ax.text(1.90, 24.6, "23,1%", ha="right", va="bottom", fontsize=9.2,
            color=P["rojo"], fontweight="bold")

    fig.text(0.062, 0.055,
             "Por primera vez la barra cae POR DEBAJO de la línea: cada dólar nuevo aporta menos margen\n"
             "que el negocio que ya existía. Eso es una estructura que revierte.",
             fontsize=9.0, color=P["rojo_oscuro"], ha="left", va="bottom",
             linespacing=1.5)

    ax.set_xticks(x); ax.set_xticklabels(etiq, fontsize=9.8)
    ax.set_xlim(-0.62, 2.92); ax.set_ylim(0, 50)
    ax.set_yticks([0, 10, 20, 30, 40, 50])
    ax.set_yticklabels(["0%", "10%", "20%", "30%", "40%", "50%"], fontsize=8.8)

    ax.legend(handles=[
        Patch(facecolor=P["azul"], label="Margen operativo incremental (ΔEBIT ÷ ΔIngresos)"),
        Patch(facecolor=P["rojo_oscuro"], label="El ejercicio en que se rompe"),
        Line2D([0], [0], color=P["rojo"], lw=2.0, ls="--", marker="o", ms=6,
               label="Margen operativo medio del ejercicio")],
        frameon=False, loc="lower center", bbox_to_anchor=(0.5, 1.005), ncol=1,
        fontsize=8.8, handlelength=1.7, borderpad=0.0, labelspacing=0.5)

    deco(ax,
         "Por cada dólar nuevo de ventas, Deckers ya sólo se queda 17 céntimos",
         "Margen operativo incremental de cada ejercicio contra el margen operativo medio de ese mismo ejercicio.",
         "10-K FY2026 · EDGAR 0001628280-26-037664")
    save(fig, "c08_margen_incremental")


if __name__ == "__main__":
    c05_dos_marcas()
    c06_hoka_coste()
    c07_empuje_tiron()
    c08_margen_incremental()
    print("OK · c05, c06, c07, c08 generados en charts/")
