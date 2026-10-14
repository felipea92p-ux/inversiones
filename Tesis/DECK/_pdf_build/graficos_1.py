# -*- coding: utf-8 -*-
"""GRÁFICOS 1 · ULTRA TESIS DECK · c01–c04
Nivel 2 (el negocio) y arranque del nivel 3 (los números).
Cifras EXCLUSIVAMENTE de DATOS.md. Ninguna se calcula fuera de ahí salvo
las derivadas triviales que el propio DATOS.md ya deja escritas.
"""
import sys; sys.path.insert(0, "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build")
import os
os.chdir("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build")

import numpy as np, matplotlib.pyplot as plt
from chart_style import deco, save
from paleta_qg import PALETA as P

MENOS = "−"          # signo menos tipográfico (DejaVu Serif lo cubre)


def num(v, dec=1):
    """1234.5 -> '1.234,5' (convención española)."""
    s = f"{v:,.{dec}f}"
    return s.replace(",", "@").replace(".", ",").replace("@", ".")


def pc(v, dec=1, signo=True):
    s = f"{v:+.{dec}f}" if signo else f"{v:.{dec}f}"
    return s.replace(".", ",").replace("-", MENOS) + "%"


# ═══════════════════════════════════════════════════════════════════
# c01 · EL MAPA DEL DINERO — los mismos 5.472,3 M, contados tres veces
# ═══════════════════════════════════════════════════════════════════
def c01_mapa_dinero():
    TOTAL = 5472.3
    filas = [
        ("POR MARCA", [
            ("HOKA",           2587.3,  15.9, P["azul"],       "#FFFFFF"),
            ("UGG",            2738.8,   8.2, P["azul_acero"], "#FFFFFF"),
            ("Otras",           146.2, -33.9, P["rojo_oscuro"], "#FFFFFF")]),
        ("POR CANAL", [
            ("Mayorista",      3208.1,  12.3, P["azul"],       "#FFFFFF"),
            ("Venta directa",  2264.2,   6.3, P["azul_cielo"], P["tinta"])]),
        ("POR GEOGRAFÍA", [
            ("Estados Unidos", 3191.5,   0.2, P["ocre"],       "#FFFFFF"),
            ("Internacional",  2280.8,  26.8, P["verde"],      "#FFFFFF")]),
    ]
    PARADOS = {"Estados Unidos", "Otras"}   # los dos trozos que no se mueven

    fig, ax = plt.subplots(figsize=(7.2, 4.08))
    fig.subplots_adjust(top=0.775, bottom=0.085, left=0.205, right=0.99)

    ys = [2.0, 1.0, 0.0]
    H = 0.56
    for y, (_, segs) in zip(ys, filas):
        izq = 0.0
        for nom, val, var, col, tcol in segs:
            ax.barh(y, val, left=izq, height=H, color=col,
                    edgecolor=P["fondo"], linewidth=1.6, zorder=3)
            centro = izq + val / 2.0
            if val / TOTAL > 0.10:                      # cabe la etiqueta dentro
                ax.text(centro, y + 0.145, nom, ha="center", va="center",
                        fontsize=9.6, fontweight="bold", color=tcol, zorder=4)
                ax.text(centro, y - 0.012, num(val) + " M", ha="center", va="center",
                        fontsize=9.2, color=tcol, zorder=4)
                alerta = nom in PARADOS
                ax.text(centro, y - 0.168,
                        pc(var) + ("   ·   prácticamente plano" if alerta else ""),
                        ha="center", va="center", fontsize=8.8,
                        style="normal" if alerta else "italic",
                        fontweight="bold" if alerta else "normal",
                        color=tcol, zorder=4)
            izq += val

    # el segmento que no cabe: "Otras", el que se está muriendo
    ax.annotate("Otras marcas\n" + num(146.2) + " M   " + pc(-33.9),
                xy=(5460, 2.10), xytext=(5570, 2.34),
                ha="left", va="center", fontsize=8.9, color=P["rojo_oscuro"],
                fontweight="bold", linespacing=1.5,
                arrowprops=dict(arrowstyle="-", lw=0.9, color=P["rojo_oscuro"],
                                connectionstyle="angle,angleA=0,angleB=90,rad=3"))

    # la línea que demuestra que las tres filas suman lo mismo
    ax.plot([TOTAL, TOTAL], [-0.48, 2.42], ls=(0, (2, 3)), lw=1.0,
            color=P["gris_medio"], zorder=2)
    ax.text(TOTAL + 60, -0.40, num(TOTAL) + " M", ha="left", va="center",
            fontsize=8.6, style="italic", color=P["gris"])

    ax.set_yticks(ys)
    ax.set_yticklabels([f[0] for f in filas], fontsize=10, fontweight="bold",
                       color=P["tinta"])
    ax.set_xticks([])
    ax.set_xlim(0, 7200)
    ax.set_ylim(-0.62, 2.62)

    deco(ax,
         "Los mismos 5.472,3 millones, contados de tres maneras",
         "Ingresos de FY2026 por marca, por canal y por geografía · en dos de los tres cortes hay un trozo parado",
         "10-K FY2026 · EDGAR 0001628280-26-037664 · 8-K 21-may-2026")
    ax.grid(False)
    ax.spines["bottom"].set_visible(False)
    save(fig, "c01_mapa_dinero")


# ═══════════════════════════════════════════════════════════════════
# c02 · LA ZAPATILLA DE 150 — qué queda de cada dólar que entra
# ═══════════════════════════════════════════════════════════════════
def c02_zapatilla_margenes():
    # (etiqueta eje, importe, tipo, color, texto de la etiqueta, % sobre 150)
    pasos = [
        ("Precio de\nventa",              150.00, "total", P["azul_noche"],  "150,00", "100%"),
        ("Coste del\nproducto",           -63.45, "resta", P["rojo_oscuro"], MENOS + "63,45", "42,3%"),
        ("Margen\nbruto",                  86.55, "total", P["verde"],       "86,55", "57,7%"),
        ("Gastos de\nestructura\n(SG&A)",   -51.93, "resta", P["rojo_oscuro"], MENOS + "51,93", "34,6%"),
        ("Beneficio\noperativo",           34.62, "total", P["azul"],        "34,62", "23,08%"),
        ("Impuestos\ny otros",             -6.55, "resta", P["rojo_oscuro"], MENOS + "6,55", "4,4%"),
        ("Beneficio\nneto",                28.07, "total", P["rojo"],        "28,07", "18,7%"),
    ]

    fig, ax = plt.subplots(figsize=(7.2, 4.21))
    fig.subplots_adjust(top=0.765, bottom=0.195, left=0.075, right=0.985)

    W = 0.74
    nivel = 0.0          # altura acumulada tras cada paso
    tops = []
    for i, (_, imp, tipo, col, txt, ppc) in enumerate(pasos):
        if tipo == "total":
            base, alto, nivel = 0.0, imp, imp
        else:
            base, alto = nivel + imp, -imp        # barra flotante hacia abajo
            nivel = nivel + imp
        ax.bar(i, alto, bottom=base, width=W, color=col,
               edgecolor=P["fondo"], linewidth=1.2, zorder=3)
        tops.append(base + alto if tipo == "total" else base + alto)

        if tipo == "total":
            ax.text(i, imp + 20.0, txt, ha="center", va="center", fontsize=11.5,
                    fontweight="bold", color=col, zorder=4)
            ax.text(i, imp + 6.5, ppc, ha="center", va="center", fontsize=8.8,
                    style="italic", color=P["gris"], zorder=4)
        elif alto > 20:                            # cabe dentro de la barra
            ax.text(i, base + alto / 2 + 5.5, txt, ha="center", va="center",
                    fontsize=11.5, fontweight="bold", color="#FFFFFF", zorder=4)
            ax.text(i, base + alto / 2 - 6.5, ppc, ha="center", va="center",
                    fontsize=8.8, style="italic", color="#F2ECDC", zorder=4)
        else:                                      # demasiado corta: fuera
            ax.text(i, base + alto + 20.0, txt, ha="center", va="center", fontsize=11.5,
                    fontweight="bold", color=col, zorder=4)
            ax.text(i, base + alto + 6.5, ppc, ha="center", va="center", fontsize=8.8,
                    style="italic", color=P["gris"], zorder=4)

    # conectores: el techo de un paso es el techo del siguiente
    puentes = [(0, 1, 150.00), (1, 2, 86.55), (2, 3, 86.55),
               (3, 4, 34.62), (4, 5, 34.62), (5, 6, 28.07)]
    for a, b, y in puentes:
        ax.plot([a + W / 2, b - W / 2], [y, y], ls=(0, (2, 2.4)), lw=1.0,
                color=P["gris_medio"], zorder=2)

    ax.set_xticks(range(len(pasos)))
    ax.set_xticklabels([p[0] for p in pasos], fontsize=9.2, color=P["tinta"],
                       linespacing=1.45)
    ax.set_yticks([0, 30, 60, 90, 120, 150])
    ax.set_yticklabels(["0", "30", "60", "90", "120", "150"], fontsize=8.6)
    ax.set_ylabel("dólares por par vendido", fontsize=8.8)
    ax.set_xlim(-0.66, 6.66)
    ax.set_ylim(0, 182)

    deco(ax,
         "De cada 150 dólares que paga un cliente, a Deckers le quedan 28,07",
         "Cascada con los márgenes reales de FY2026: bruto 57,7% · operativo 23,08% · neto 18,7%",
         "10-K FY2026 · EDGAR 0001628280-26-037664")
    save(fig, "c02_zapatilla_margenes")


# ═══════════════════════════════════════════════════════════════════
# c03 · NOPAT CONTRA CAPITAL INVERTIDO, Y EL ROIC QUE SALE DE AHÍ
# ═══════════════════════════════════════════════════════════════════
def c03_roic_capital():
    fy     = ["FY2022", "FY2023", "FY2024", "FY2025", "FY2026"]
    nopat  = [452.0, 506.5, 719.6, 916.2, 975.1]
    capital= [915.2, 1046.6, 885.1, 888.2, 965.6]
    roic   = [49.4, 48.4, 81.3, 103.2, 101.0]

    x = np.arange(len(fy)); W = 0.36
    fig, ax = plt.subplots(figsize=(7.2, 4.08))
    fig.subplots_adjust(top=0.735, bottom=0.115, left=0.085, right=0.915)

    b1 = ax.bar(x - W / 2, nopat, W, color=P["azul"], zorder=3,
                label="Beneficio operativo tras impuestos (NOPAT)")
    b2 = ax.bar(x + W / 2, capital, W, color=P["azul_cielo"], zorder=3,
                label="Capital invertido en el negocio")

    for xi, v in zip(x - W / 2, nopat):      # dentro de la barra: la línea del ROIC pasa por encima
        ax.text(xi, v - 32, num(v), ha="center", va="top", fontsize=8.8,
                fontweight="bold", color="#FFFFFF", zorder=5)
    dx_cap = [0.0, 0.0, 0.09, 0.0, 0.0]     # FY2024: apartarse de la marca del ROIC
    for xi, v, ddx in zip(x + W / 2, capital, dx_cap):
        ax.text(xi + ddx, v + 26, num(v), ha="center", va="bottom", fontsize=8.6,
                color=P["gris"], zorder=4)

    ax2 = ax.twinx()
    ax2.plot(x, roic, color=P["rojo"], lw=2.1, marker="o", ms=6.0,
             mfc=P["fondo"], mec=P["rojo"], mew=1.8, zorder=6, label="ROIC (eje derecho)")
    ax2.axhline(100, ls="--", lw=1.15, color=P["rojo"], alpha=0.55, zorder=2)
    # en FY2022-FY2023 la línea va por debajo de las barras: la etiqueta se desplaza
    # al hueco que queda sobre la barra de NOPAT para no morder la barra de capital
    for i, (xi, v) in enumerate(zip(x, roic)):
        dx = -0.18 if i < 3 else 0.0
        ax2.text(xi + dx, v + 5.6, pc(v, 1, False), ha="center", va="bottom", fontsize=8.8,
                 fontweight="bold", color=P["rojo"], zorder=7,
                 bbox=dict(facecolor=P["fondo"], edgecolor="none", pad=1.6))

    # la idea del gráfico, dicha donde no estorba
    ax.text(0.015, 0.975,
            "Desde FY2025 la barra azul supera a la gris:\n"
            "Deckers gana en un año, después de impuestos,\n"
            "más de lo que tiene invertido en el negocio entero.",
            transform=ax.transAxes, ha="left", va="top", fontsize=8.8,
            linespacing=1.55, color=P["tinta"])

    ax.set_xticks(x); ax.set_xticklabels(fy, fontsize=9.6, color=P["tinta"])
    ax.set_ylim(0, 1660); ax2.set_ylim(0, 140)
    ax.set_yticks([0, 300, 600, 900, 1200])
    ax.set_yticklabels([num(v, 0) for v in [0, 300, 600, 900, 1200]], fontsize=8.6)
    ax.set_ylabel("millones de dólares", fontsize=8.8)
    ax2.set_yticks([0, 25, 50, 75, 100, 125])
    ax2.set_yticklabels([pc(v, 0, False) for v in [0, 25, 50, 75, 100, 125]],
                        fontsize=8.6, color=P["rojo"])
    ax2.set_ylabel("ROIC · beneficio por 100 de capital", fontsize=8.8,
                   color=P["rojo"])
    for s in ax2.spines.values():
        s.set_visible(False)
    ax2.tick_params(length=0)
    ax.set_xlim(-0.62, 4.62)

    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="lower center", bbox_to_anchor=(0.5, 1.005),
              ncol=2, frameon=False, fontsize=8.5, handlelength=1.5,
              columnspacing=1.8, labelspacing=0.45, borderpad=0.0)

    deco(ax,
         "Desde FY2025 el beneficio de un año supera al capital invertido",
         "NOPAT contra capital invertido, FY2022-FY2026, y el ROIC que resulta de dividir uno por otro",
         "10-K FY2022-FY2026 · EDGAR 0001628280-26-037664")
    save(fig, "c03_roic_capital")


# ═══════════════════════════════════════════════════════════════════
# c04 · EL CRUCE — donde el beneficio se separa de las ventas
# ═══════════════════════════════════════════════════════════════════
def c04_cruce_lineas():
    trim = ["jun-24", "sep-24", "dic-24", "mar-25", "jun-25",
            "sep-25", "dic-25", "mar-26", "jun-26"]
    ing  = [22.1, 20.1, 17.1, 6.5, 16.9, 9.1, 7.1, 9.6, 5.7]
    ebit = [87.8, 35.8, 16.3, 20.5, 24.5, 7.0, 8.3, -9.9, -6.0]
    x = np.arange(len(trim))

    fig, ax = plt.subplots(figsize=(7.2, 4.14))
    fig.subplots_adjust(top=0.765, bottom=0.115, left=0.098, right=0.985)

    ax.axhspan(-31, 0, color=P["rojo_oscuro"], alpha=0.085, zorder=1)
    ax.axhline(0, ls="--", lw=1.3, color=P["rojo"], zorder=2)

    ax.plot(x, ing, color=P["azul"], lw=2.2, marker="o", ms=5.4, mfc=P["fondo"],
            mec=P["azul"], mew=1.7, zorder=5, label="Crecimiento de los ingresos")
    ax.plot(x, ebit, color=P["rojo_oscuro"], lw=2.2, marker="s", ms=5.4, mfc=P["fondo"],
            mec=P["rojo_oscuro"], mew=1.7, zorder=6, label="Crecimiento del beneficio operativo (EBIT)")

    # el cruce, interpolado entre dic-25 (+8,3%) y mar-26 (−9,9%)
    xc = 6 + 8.3 / (8.3 + 9.9)
    ax.plot([xc, xc], [-31, 30], ls=(0, (1.6, 2.6)), lw=1.1, color=P["gris_medio"], zorder=3)
    ax.text(xc, 32.5, "el cruce", ha="center", va="bottom", fontsize=8.8,
            style="italic", color=P["gris"])

    ax.text(0.06, -24.2,
            "por debajo de esta línea el beneficio operativo NO crece: cae",
            ha="left", va="center", fontsize=8.4, style="italic", color=P["rojo_oscuro"])

    ax.text(0, 91.5, pc(87.8), ha="center", va="bottom", fontsize=8.8,
            fontweight="bold", color=P["rojo_oscuro"])
    ax.text(0, 26.2, pc(22.1), ha="center", va="bottom", fontsize=8.8,
            fontweight="bold", color=P["azul"])
    ax.text(8, 9.6, pc(5.7), ha="center", va="bottom", fontsize=8.8,
            fontweight="bold", color=P["azul"])
    ax.text(8.38, -13.0, "mar-2026   " + pc(-9.9) + "\njun-2026   " + pc(-6.0),
            ha="right", va="top", fontsize=8.9,
            fontweight="bold", color=P["rojo_oscuro"], linespacing=1.55)

    ax.set_xticks(x); ax.set_xticklabels(trim, fontsize=9.2, color=P["tinta"])
    ax.set_yticks([-20, 0, 20, 40, 60, 80])
    ax.set_yticklabels([pc(v, 0, False) for v in [-20, 0, 20, 40, 60, 80]], fontsize=8.6)
    ax.set_ylabel("variación interanual", fontsize=8.8)
    ax.set_xlim(-0.42, 8.42); ax.set_ylim(-31, 99)

    ax.legend(loc="upper right", frameon=False, fontsize=8.8, handlelength=1.8,
              labelspacing=0.6)

    deco(ax,
         "Dos trimestres seguidos de beneficio cayendo con las ventas subiendo",
         "Crecimiento interanual de ingresos y de EBIT, de jun-2024 a jun-2026 · el ejercicio cierra el 31 de marzo",
         "10-K FY2026 · 10-Q jun-2026 · EDGAR 0000910521-26-000022")
    save(fig, "c04_cruce_lineas")


if __name__ == "__main__":
    c01_mapa_dinero()
    c02_zapatilla_margenes()
    c03_roic_capital()
    c04_cruce_lineas()
    print("OK · 4 gráficos generados en charts/")
