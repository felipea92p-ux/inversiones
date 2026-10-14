# -*- coding: utf-8 -*-
"""GRÁFICOS 4 · ULTRA TESIS DECKERS OUTDOOR (NYSE: DECK) · 25-ago-2026
c13_tir_alternativas · c14_escalera_precios · c15_colapso_2022 · c16_dos_precedentes
Todas las cifras salen de DATOS.md. Nada se inventa aquí.
"""
import sys; sys.path.insert(0, "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build")
import os
os.chdir("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build")

import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D
from chart_style import deco, save
from paleta_qg import PALETA as P

MENOS = "−"   # signo menos tipográfico


def sub_dos_lineas(fig):
    """A 7,2 pulgadas el subtítulo de deco() ya no cabe en una línea. deco() lo
    ancla por la línea base, así que al partirlo en dos la PRIMERA línea sube y
    pisa el titular. Lo reanclamos por arriba, sin tocar chart_style.py."""
    for t in fig.texts:
        if abs(t.get_fontsize() - 8.6) < 1e-6:
            t.set_verticalalignment("top")
            x, y = t.get_position()
            t.set_position((x, y + 0.022))
            return


def es(x, dec=1):
    """Formato español: punto de millar, coma decimal."""
    s = f"{abs(x):,.{dec}f}".replace(",", "@").replace(".", ",").replace("@", ".")
    return (MENOS if x < 0 else "") + s


# ═══════════════════════════════════════════════════════════════════════
# c13 · LA TIR CONTRA LAS ALTERNATIVAS
# ═══════════════════════════════════════════════════════════════════════
def c13():
    filas = [  # (etiqueta, TIR %, valor por acción, color)   de arriba a abajo
        ("Celda más dura\nbase 865  ·  1,63% → 0,00%",           8.80,  "81,50",  P["rojo_oscuro"]),
        ("Suelo duro, central\nbase 947  ·  5,50% → 0,00%",      11.14, "100,71", P["azul_acero"]),
        ("La que GOBIERNA, central\nbase 947  ·  5,50% → 2,32%", 12.75, "121,36", P["azul"]),
        ("Cuarentena, central\nbase 947  ·  5,50% → 4,30%",      14.15, "152,79", P["ocre"]),
        ("Celda más alta\nbase 1.016  ·  14,69% → 4,30%",        18.80, "232,59", P["verde"]),
    ]
    fig, ax = plt.subplots(figsize=(7.2, 4.075))
    fig.subplots_adjust(top=0.750, bottom=0.155, left=0.315, right=0.975)

    y = np.arange(len(filas))[::-1]
    for yi, (_, tir, val, col) in zip(y, filas):
        ax.barh(yi, tir, height=0.54, color=col, zorder=3)
        caja = dict(facecolor=P["fondo"], edgecolor="none", pad=1.4)
        ax.text(tir + 0.35, yi + 0.11, f"{es(tir, 2)}%", va="center", ha="left",
                fontsize=10.5, fontweight="bold", color=col, bbox=caja, zorder=6)
        ax.text(tir + 0.35, yi - 0.19, f"valor {val} USD", va="center", ha="left",
                fontsize=7.8, style="italic", color=P["gris"], bbox=caja, zorder=6)

    # Líneas de referencia
    ax.axvline(4.70, color=P["verde"], lw=1.6, ls=(0, (1, 1.6)), zorder=4)
    ax.axvline(9.70, color=P["rojo"], lw=1.8, ls="--", zorder=4)
    ax.text(4.56, len(filas) - 0.32, "Tesoro 10 años  4,70%  ", fontsize=8.4,
            color=P["verde"], ha="right", va="bottom", fontweight="bold")
    ax.text(9.86, len(filas) - 0.32, "Tasa exigida del método  9,70%", fontsize=8.4,
            color=P["rojo"], ha="left", va="bottom", fontweight="bold")

    # La única celda que no llega
    ax.annotate("la única celda que no\nalcanza la tasa exigida",
                xy=(8.75, 3.80), xytext=(15.6, 3.60),
                fontsize=8.4, style="italic", color=P["rojo_oscuro"], ha="left",
                va="center", zorder=7,
                bbox=dict(facecolor=P["fondo"], edgecolor="none", pad=1.5),
                arrowprops=dict(arrowstyle="->", color=P["rojo_oscuro"], lw=1.1,
                                connectionstyle="arc3,rad=-0.20"))

    ax.set_yticks(y)
    ax.set_yticklabels([f[0] for f in filas], fontsize=8.4, color=P["tinta"])
    ax.set_ylim(-0.60, len(filas) - 0.02)
    ax.set_xlim(0, 25.0)
    ax.set_xticks(range(0, 23, 2))
    ax.set_xticklabels([f"{v}%" for v in range(0, 23, 2)], fontsize=8.4)
    ax.set_xlabel("TIR anual a diez años comprando hoy a 88,73 USD por acción",
                  fontsize=8.6, labelpad=8)

    deco(ax,
         "Todas las lecturas baten al efectivo; la más dura no llega a la tasa exigida",
         "TIR a diez años por celda del motor, comprando a 88,73 USD. Base = owner\n"
         "earnings en millones; crecimiento inicial → terminal.",
         "10-K FY2026 · EDGAR 0001628280-26-037664 · H.15 24-ago-2026")
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=P["gris_linea"], lw=0.6, alpha=0.9)
    ax.set_axisbelow(True)
    sub_dos_lineas(fig)
    save(fig, "c13_tir_alternativas")


# ═══════════════════════════════════════════════════════════════════════
# c14 · LA ESCALERA DE PRECIOS
# ═══════════════════════════════════════════════════════════════════════
def c14():
    # Reparto de los 105 cierres semanales por bandas, derivado de los recuentos
    # acumulados y de los percentiles publicados en DATOS.md.
    bandas = [(81.50, 82.49, 2, False), (82.49, 88.73, 5, False),
              (88.73, 91.02, 2, False), (91.02, 95.18, 3, False),
              (95.18, 101.18, 14, True), (101.18, 108.53, 27, True),
              (108.53, 217.16, 52, True)]

    fig, (axh, ax) = plt.subplots(1, 2, figsize=(7.2, 4.40), sharey=True,
                                  gridspec_kw={"width_ratios": [1.0, 2.55], "wspace": 0.05})
    fig.subplots_adjust(top=0.745, bottom=0.150, left=0.098, right=0.975)

    # ── Panel izquierdo: distribución empírica de los 105 cierres ──────
    # Las etiquetas de recuento van SEPARADAS a mano: las bandas altas son tan
    # estrechas que, centradas, el 14 y el 27 se pisaban entre sí y sobre la barra.
    yrot = {14: 95.4, 27: 107.2, 52: 162.8}
    for lo, hi, n, rotula in bandas:
        col = P["azul_cielo"] if lo >= 91.02 else P["azul_noche"]
        axh.add_patch(Rectangle((0, lo), n, hi - lo, facecolor=col,
                                edgecolor=P["fondo"], lw=0.8, zorder=3))
        if rotula:
            axh.text(n + 2.2, yrot[n], str(n), fontsize=8.0, va="center",
                     ha="left", color=P["gris"], zorder=5)
    axh.set_xlim(0, 66)                 # de izquierda a derecha: 0, 20, 40
    axh.set_xticks([0, 20, 40])
    axh.tick_params(labelsize=7.8)
    axh.set_xlabel("cierres semanales\n(105 en 24 meses)", fontsize=8.0, labelpad=6)

    # ── Zona de compra, en los dos paneles ────────────────────────────
    for a in (axh, ax):
        a.axhspan(48.54, 66.75, color=P["rojo"], alpha=0.085, zorder=1)

    # ── Panel derecho: la escalera ────────────────────────────────────
    # A esta escala la altura útil son ~2,0 px por dólar: un rótulo de 8,6 pt pide
    # 9 dólares de holgura. 91,02 y 88,73 sólo distan 2,29, así que el rótulo de
    # N2 NO cabe junto a su línea: desplazado en horizontal caía sobre la línea de
    # 100,71, que lo tachaba. Se saca a la banda muerta entre 100,71 y 121,36 y se
    # ata a su línea con una flecha. El resto lleva su desplazamiento calculado.
    CAJA = dict(facecolor=P["fondo"], edgecolor="none", alpha=0.88, pad=1.4)
    N2 = P["terracota"]          # color propio de N2: no se confunde con nada más
    niveles = [
        (152.79, "valor central, cuarentena",       P["ocre"],       1.5, "--",          0.40,  2.0),
        (121.36, "valor central, LA QUE GOBIERNA",  P["azul"],       2.4, "-",           0.40,  2.0),
        (100.71, "valor central, suelo duro",       P["azul_acero"], 1.8, "-",           0.40,  2.5),
        (88.73,  "PRECIO HOY",                      P["tinta"],      2.2, "-",           0.40,  1.8),
        # N2 va DESPUÉS de 88,73 para quedar por encima: con lw 3,0 la de 88,73 se
        # la comía entera. Raya larga y color propio para que se distinga a 2,29 USD.
        (91.02,  None,                              N2,              1.7, (0, (6, 2.4)), None,  None),
        (66.75,  "N3 · PRIMER TRAMO",               P["rojo"],       3.0, "-",           0.40,  2.0),
        (48.54,  "N3 · tramo pleno",                P["rojo"],       1.6, "--",          0.40, -11.6),
    ]
    for v, txt, col, lw, ls, xt, dy in niveles:
        ax.axhline(v, color=col, lw=lw, ls=ls, zorder=4)
        if txt is None:
            continue
        neg = "bold" if v in (88.73, 66.75, 121.36) else "normal"
        ax.text(xt, v + dy, f"{es(v, 2)}  ·  {txt}", fontsize=8.6,
                color=col, ha="left", va="bottom", fontweight=neg, zorder=6,
                bbox=CAJA)

    # Marcador triangular en el margen derecho: remata la línea de N2 y la separa
    # a ojo de la de 88,73, con la que comparte casi el mismo píxel.
    ax.plot([9.72], [91.02], marker="<", ms=6.0, color=N2, zorder=7, clip_on=False)
    # El rótulo de N2, en la banda muerta entre 100,71 y 121,36, atado por flecha.
    ax.annotate("91,02  ·  N2, no adoptado", xy=(7.55, 91.30), xytext=(6.10, 109.0),
                fontsize=8.6, color=N2, ha="left", va="baseline", zorder=7,
                bbox=CAJA,
                arrowprops=dict(arrowstyle="->", color=N2, lw=1.1, shrinkB=1.0,
                                connectionstyle="arc3,rad=-0.26"))

    # Flecha del hueco entre el precio y el tramo 1
    ax.annotate("", xy=(9.48, 88.73), xytext=(9.48, 66.75),
                arrowprops=dict(arrowstyle="<->", color=P["rojo_oscuro"], lw=1.3))
    ax.text(9.30, 77.7, "32,9% por encima\ndel tramo 1", fontsize=8.2, ha="right",
            va="center", style="italic", color=P["rojo_oscuro"], zorder=6,
            bbox=dict(facecolor=P["fondo"], edgecolor="none", alpha=0.85, pad=1.4))
    ax.text(0.40, 53.6, "ZONA DE COMPRA · 0 de 105 cierres",
            fontsize=8.6, color=P["rojo_oscuro"], fontweight="bold", va="bottom",
            zorder=6)
    ax.text(5.00, 36.9, "caso archivado 12 meses", fontsize=8.6,
            color=P["rojo_oscuro"], fontweight="bold", va="bottom", zorder=6)

    # Bloque de lectura del histograma: arriba a la izquierda del panel de la
    # escalera, el único hueco de verdad vacío (por encima de 152,79 no hay nada).
    ax.text(0.02, 0.985, "mínimo de 24 meses:  81,50",
            transform=ax.transAxes, fontsize=8.2, ha="left", va="top",
            style="italic", color=P["rojo_oscuro"], zorder=6,
            bbox=dict(facecolor=P["fondo"], edgecolor="none", alpha=0.85, pad=2.2))
    ax.text(0.02, 0.925, "12 cierres por debajo de 95,18\n7 por debajo del precio de hoy\n"
            "2 por debajo de 82,49",
            transform=ax.transAxes, fontsize=8.0, ha="left", va="top",
            color=P["gris"], zorder=6,
            bbox=dict(facecolor=P["fondo"], edgecolor="none", alpha=0.85, pad=2.2))

    ax.set_xlim(0, 10)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.set_ylim(34, 232)
    ax.set_yticks(range(40, 221, 20))
    axh.set_ylabel("Precio por acción, USD", fontsize=8.8, labelpad=8)
    axh.tick_params(axis="y", labelsize=8.4)

    deco([axh, ax],
         "La zona de compra está por debajo de todo lo que ha existido en dos años",
         "Los 105 cierres semanales (27-ago-2024 a 24-ago-2026) contra la escalera de valor.\n"
         "Las bandas del histograma son los umbrales publicados, de amplitud desigual.",
         "IBKR conid 268376 · 10-K FY2026 · EDGAR 0001628280-26-037664",
         fig=fig)
    ax.grid(axis="y", color=P["gris_linea"], lw=0.6, alpha=0.55)
    sub_dos_lineas(fig)
    save(fig, "c14_escalera_precios")


# ═══════════════════════════════════════════════════════════════════════
# c15 · EL COLAPSO DE FLUJO DE FY2022
# ═══════════════════════════════════════════════════════════════════════
def c15():
    fy = ["FY2019", "FY2020", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025", "FY2026"]
    fcf = [330.4, 253.8, 564.0, 121.4, 456.4, 943.8, 958.3, 1097.3]
    rev = [2020.4, 2132.7, 2545.6, 3150.3, 3627.3, 4287.8, 4985.6, 5472.3]
    x = np.arange(len(fy))

    fig, ax = plt.subplots(figsize=(7.2, 4.211))
    fig.subplots_adjust(top=0.750, bottom=0.215, left=0.092, right=0.905)
    ax2 = ax.twinx()
    # twinx dibuja ax2 ENCIMA de ax: sin esto la línea de ingresos tacha la
    # etiqueta "564,0" del flujo de FY2021. Se invierte el orden y se transparenta
    # el fondo de ax; la línea nunca cae por debajo de una barra, así que no la tapa.
    ax.set_zorder(ax2.get_zorder() + 1)
    ax.patch.set_visible(False)

    cols = [P["rojo_oscuro"] if f == "FY2022" else P["azul"] for f in fy]
    ax.bar(x, fcf, width=0.60, color=cols, zorder=3)
    for xi, v in zip(x, fcf):
        ax.text(xi, v + 26, es(v), ha="center", va="bottom", fontsize=8.4,
                color=P["rojo_oscuro"] if v == 121.4 else P["gris"],
                fontweight="bold" if v == 121.4 else "normal", zorder=6,
                bbox=dict(facecolor=P["fondo"], edgecolor="none", pad=1.0))

    ax2.plot(x, rev, color=P["ocre"], lw=2.2, marker="o", ms=5.0,
             mfc=P["fondo"], mec=P["ocre"], mew=1.6, zorder=5)
    for xi, v in zip(x, rev):
        ax2.text(xi, v + 175, es(v), ha="center", va="bottom", fontsize=7.8,
                 color=P["ocre"])

    # El bloque rojo se va al hueco de arriba a la izquierda: donde estaba se
    # solapaba con la serie de ingresos, que a esta escala sube por ese hueco.
    ax.annotate("", xy=(2.92, 245), xytext=(2.52, 1000),
                arrowprops=dict(arrowstyle="->", color=P["rojo_oscuro"], lw=1.3,
                                connectionstyle="arc3,rad=0.20"))
    ax.text(-0.46, 1625, MENOS + "78,5% de flujo con los ingresos +23,8%",
            fontsize=10.5, fontweight="bold", color=P["rojo_oscuro"],
            ha="left", va="top")
    ax.text(-0.46, 1500, "reconstrucción de inventario de +228,6 M\n"
            "conversión CFO/neto 38,2% contra una media\n"
            "del 122,7%; recuperó el pico en dos ejercicios",
            fontsize=8.2, style="italic", color=P["gris"], ha="left", va="top")

    ax.set_ylim(0, 1640)
    ax.set_yticks(range(0, 1201, 200))
    ax2.set_ylim(0, 6355)
    ax2.set_yticks(range(0, 6001, 1000))
    ax.set_xticks(x); ax.set_xticklabels(fy, fontsize=8.8)
    ax.set_ylabel("Flujo de caja libre, millones", fontsize=8.8, labelpad=8)
    ax2.set_ylabel("Ingresos, millones", fontsize=8.8, labelpad=10, color=P["ocre"])
    ax2.tick_params(axis="y", colors=P["ocre"], labelsize=8.4, length=0)
    ax.tick_params(axis="y", labelsize=8.4)
    for s in ("top", "left", "right", "bottom"):
        ax2.spines[s].set_visible(False)
    ax2.grid(False)

    # La leyenda baja fuera del lienzo de datos: arriba a la izquierda ahora vive
    # el bloque rojo, y dentro del gráfico ya no queda un hueco limpio para ella.
    ax.legend(handles=[Patch(color=P["azul"], label="Flujo de caja libre (izq.)"),
                       Patch(color=P["rojo_oscuro"], label="FY2022, el ciclo que sí vale"),
                       Line2D([], [], color=P["ocre"], lw=2.2, marker="o", ms=5,
                              mfc=P["fondo"], label="Ingresos (der.)")],
              loc="upper center", bbox_to_anchor=(0.5, -0.115), ncol=3,
              frameon=False, fontsize=8.0, handlelength=1.5, columnspacing=1.5)

    deco(ax,
         "La ciclicidad de Deckers no vive en el beneficio: vive en el circulante",
         "Flujo de caja libre e ingresos, FY2019-FY2026, en millones de dólares. El peor\n"
         "año de caja de la década fue el mejor año de ventas.",
         "10-K FY2026 · EDGAR 0001628280-26-037664 · 10-K FY2021 a FY2024",
         fig=fig)
    sub_dos_lineas(fig)
    save(fig, "c15_colapso_2022")


# ═══════════════════════════════════════════════════════════════════════
# c16 · LOS DOS PRECEDENTES: EL QUE NO VALE
# ═══════════════════════════════════════════════════════════════════════
def c16():
    fy = ["FY2015", "FY2016", "FY2017", "FY2018", "FY2019"]
    rep = [224.4, 162.1, -1.9, 222.6, 327.3]
    lim = [224.4, 162.1, 116.1, 222.6, 327.3]
    x = np.arange(len(fy))

    fig, ax = plt.subplots(figsize=(7.2, 4.211))
    fig.subplots_adjust(top=0.750, bottom=0.215, left=0.098, right=0.975)

    # La ventana de la caída, sombreada de FY2015 a FY2017: los dos porcentajes
    # del rótulo son de esa ventana, no del último salto. Sin esta banda el rótulo
    # quedaba colgado entre FY2016 y FY2017 e invitaba a leerlo como FY2016→FY2017.
    ax.axvspan(-0.34, 2.34, color=P["gris_linea"], alpha=0.30, zorder=0)

    cols = [P["rojo_oscuro"] if f == "FY2017" else P["azul"] for f in fy]
    ax.bar(x, rep, width=0.52, color=cols, zorder=3)

    # El deterioro, sombreado
    ax.add_patch(Rectangle((2 - 0.26, -1.9), 0.52, 118.0, facecolor=P["rojo_oscuro"],
                           alpha=0.18, hatch="///", edgecolor=P["rojo_oscuro"],
                           lw=1.1, zorder=4))

    ax.plot(x, lim, color=P["verde"], lw=2.0, ls="--", marker="D", ms=6.0,
            mfc=P["fondo"], mec=P["verde"], mew=1.6, zorder=6)

    for xi, v in zip(x, rep):
        if v < 0:
            continue
        ax.text(xi, v + 11, es(v), ha="center", va="bottom", fontsize=8.6,
                color=P["gris"])
    ax.text(2, -34, MENOS + "1,9  reportado", ha="center", va="center", fontsize=8.6,
            color=P["rojo_oscuro"], fontweight="bold")
    ax.text(1.86, 126, "116,1", ha="center", va="bottom", fontsize=8.6,
            color=P["verde"], fontweight="bold", zorder=7,
            bbox=dict(facecolor=P["fondo"], edgecolor="none", pad=1.0))

    ax.axhline(0, color=P["gris"], lw=1.0, zorder=5)

    # El bloque se va al hueco de arriba a la izquierda: donde estaba tachaba la
    # etiqueta de FY2018 y la línea del EBIT limpio.
    ax.annotate("118,0 M de deterioro del fondo de comercio y la patente\n"
                "de Sanuk — marca ya vendida en agosto de 2024",
                xy=(2.30, 78), xytext=(1.55, 330),
                fontsize=8.8, color=P["rojo_oscuro"], ha="center", va="top",
                arrowprops=dict(arrowstyle="->", color=P["rojo_oscuro"], lw=1.2,
                                connectionstyle="arc3,rad=-0.34"))

    # Los dos porcentajes van anclados al ARRANQUE de la ventana (FY2015) y la
    # declaran por escrito. Antes iban centrados en x=1,25 —entre FY2016 y FY2017—
    # y se leían como el salto de un año, que sería otra cifra.
    ax.text(-0.30, 392, "Reportado, de FY2015 a FY2017:  " + MENOS + "100,9%",
            fontsize=10.5, fontweight="bold", color=P["rojo_oscuro"], ha="left")
    ax.text(-0.30, 356, "Limpio de deterioros:  " + MENOS + "48,3%", fontsize=10.5,
            fontweight="bold", color=P["verde"], ha="left")

    ax.set_xticks(x); ax.set_xticklabels(fy, fontsize=8.8)
    ax.set_xlim(-0.42, 4.42)
    ax.set_ylim(-70, 432)
    ax.set_yticks(range(0, 351, 50))
    ax.set_ylabel("EBIT, millones de dólares", fontsize=8.8, labelpad=8)
    ax.tick_params(axis="y", labelsize=8.4)

    # La leyenda baja fuera del lienzo: dentro pisaba la barra de FY2015 y el
    # rótulo de "−1,9 reportado".
    ax.legend(handles=[Patch(color=P["azul"], label="EBIT reportado"),
                       Line2D([], [], color=P["verde"], lw=2.0, ls="--", marker="D",
                              ms=5, mfc=P["fondo"], label="EBIT limpio del deterioro"),
                       Patch(facecolor=P["rojo_oscuro"], alpha=0.18, hatch="///",
                             edgecolor=P["rojo_oscuro"], label="El deterioro: 118,0 M no monetarios")],
              loc="upper center", bbox_to_anchor=(0.5, -0.095), ncol=3,
              frameon=False, fontsize=7.8, handlelength=1.5, columnspacing=1.4)

    deco(ax,
         "Aquel desplome fue casi todo un apunte contable, no un ciclo de demanda",
         "EBIT en millones de dólares, FY2015-FY2019. En el mismo tramo los ingresos cayeron\n"
         "un 4,5%, el beneficio bruto un 1,4%, y la venta directa no cayó ni un solo año.",
         "10-K FY2018 · datos seleccionados y nota de segmentos",
         fig=fig)
    sub_dos_lineas(fig)
    save(fig, "c16_dos_precedentes")


# ═══════════════════════════════════════════════════════════════════════
# c17 · LA CONSTRUCCIÓN DE LA TASA  (§13)
# ═══════════════════════════════════════════════════════════════════════
def c17():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(7.2, 4.15),
                                   gridspec_kw={"width_ratios": [1.0, 1.42],
                                                "wspace": 0.30})
    fig.subplots_adjust(top=0.750, bottom=0.215, left=0.052, right=0.975)

    # ── Panel izquierdo: la tasa, pieza a pieza ───────────────────────
    axL.barh(0, 4.70, height=0.46, color=P["azul"], zorder=3)
    axL.barh(0, 5.00, left=4.70, height=0.46, color=P["rojo"], zorder=3)
    axL.text(2.35, 0, "Tesoro 10 años\n4,70%", ha="center", va="center",
             fontsize=7.8, color=P["fondo"], fontweight="bold", zorder=5)
    axL.text(7.20, 0, "prima fija\n+5,00 pp", ha="center", va="center",
             fontsize=7.8, color=P["fondo"], fontweight="bold", zorder=5)
    axL.text(9.70, 0.35, "= 9,70%", ha="right", va="bottom", fontsize=12.5,
             fontweight="bold", color=P["tinta"])

    # El TIPS y la inflación implícita, por debajo de la barra
    axL.plot([2.38, 2.38], [-0.23, -0.62], color=P["verde"], lw=1.4, zorder=4)
    axL.text(2.30, -0.68, "TIPS 10 años\n2,38%", ha="center", va="top",
             fontsize=7.6, color=P["verde"], fontweight="bold")
    axL.annotate("", xy=(2.38, -1.28), xytext=(4.70, -1.28),
                 arrowprops=dict(arrowstyle="<|-|>", mutation_scale=8,
                                 color=P["ocre"], lw=1.2))
    axL.text(3.54, -1.38, "inflación implícita 2,32%\n(será la g-infinito)",
             ha="center", va="top", fontsize=7.6, color=P["ocre"],
             fontweight="bold")

    axL.set_xlim(0, 11.4)
    axL.set_ylim(-2.05, 1.00)
    axL.set_yticks([])
    axL.set_xticks(range(0, 11, 2))
    axL.set_xticklabels([f"{v}%" for v in range(0, 11, 2)], fontsize=8.0)
    axL.set_xlabel("tasa anual", fontsize=8.4, labelpad=6)

    # ── Panel derecho: qué pasa si la tasa fuese otra ─────────────────
    tasas = [("r 9,70%\n(la del método)", 121.36, P["azul"]),
             ("r 10,88%",                  105.95, P["azul_acero"]),
             ("r 11,70%",                   97.54, P["ocre"])]
    for i, (lab, v, col) in enumerate(tasas):
        axR.bar(i, v, width=0.50, color=col, zorder=3)
        axR.text(i, v + 3.0, es(v, 2), ha="center", va="bottom", fontsize=10.5,
                 fontweight="bold", color=col, zorder=5)

    # la línea se corta antes del rótulo para no tacharlo
    axR.plot([-0.60, 2.66], [88.73, 88.73], color=P["tinta"], lw=2.2, zorder=4)
    axR.text(3.52, 88.73, "precio\nde hoy\n88,73", ha="right", va="center",
             fontsize=8.4, fontweight="bold", color=P["tinta"], zorder=6,
             linespacing=1.3)

    axR.set_xticks(range(3))
    axR.set_xticklabels([t[0] for t in tasas], fontsize=8.4, color=P["tinta"])
    axR.set_xlim(-0.60, 3.56)
    axR.set_ylim(0, 152)
    axR.set_yticks(range(0, 141, 20))
    axR.tick_params(axis="y", labelsize=8.0)
    axR.set_ylabel("valor central por acción, USD", fontsize=8.4, labelpad=6)

    deco([axL, axR],
         "La tasa no se elige: sale del Tesoro más una prima fija de cinco puntos",
         "Tasa exigida del método, construida pieza a pieza, y lo que valdría la acción si la tasa\n"
         "fuese otra. La prima de cinco puntos es fija y no depende de la calidad de la empresa.",
         "H.15 24-ago-2026 · motor propio",
         fig=fig)
    axL.grid(axis="y", visible=False)
    sub_dos_lineas(fig)
    save(fig, "c17_construccion_tasa")


# ═══════════════════════════════════════════════════════════════════════
# c18 · LOS CUATRO TOPES DE g-CERO  (§14)
# ═══════════════════════════════════════════════════════════════════════
def c18():
    topes = [("reinversión\n× ROIC",      1.63,  P["rojo_oscuro"]),
             ("CAGR ingresos\n3 años",   14.69,  P["azul_cielo"]),
             ("CAGR ingresos\n5 años",   16.54,  P["azul_cielo"]),
             ("CAGR NOPAT\n3 años",      24.40,  P["azul_cielo"])]

    fig, ax = plt.subplots(figsize=(7.2, 4.15))
    fig.subplots_adjust(top=0.750, bottom=0.255, left=0.088, right=0.975)

    # La banda de lo que guía la propia empresa, y el central adoptado
    ax.axhspan(7.10, 8.00, color=P["ocre"], alpha=0.22, zorder=1)
    ax.axhline(5.50, color=P["rojo"], lw=1.8, ls="--", zorder=4)

    for i, (lab, v, col) in enumerate(topes):
        ax.bar(i, v, width=0.52, color=col, zorder=3)
        ax.text(i, v + 0.55, es(v, 2) + "%", ha="center", va="bottom",
                fontsize=10.5, fontweight="bold", color=col, zorder=5)

    # El mínimo vinculante, señalado sobre su propia columna (zona vacía)
    ax.plot([0, 0], [4.60, 10.15], color=P["rojo_oscuro"], lw=0.9,
            ls=(0, (2.5, 2)), zorder=4)
    ax.text(0, 10.45, "el mínimo vinculante\ny el que esta tesis rompe",
            ha="center", va="bottom", fontsize=8.2, style="italic",
            fontweight="bold", color=P["rojo_oscuro"], zorder=6,
            bbox=dict(facecolor=P["fondo"], edgecolor="none", alpha=0.85, pad=1.6))

    # El central adoptado, rotulado SOBRE su propia línea y no sólo en la leyenda.
    # El margen derecho se ensancha hasta 4,40 para que el rótulo caiga en hueco
    # limpio, a la derecha de la última columna, y no encima de ninguna barra.
    ax.text(4.34, 5.02, "5,50%\nel central adoptado", ha="right", va="top",
            fontsize=8.4, fontweight="bold", color=P["rojo"], linespacing=1.30,
            zorder=6, bbox=dict(facecolor=P["fondo"], edgecolor="none",
                                alpha=0.85, pad=1.6))

    ax.set_xticks(range(4))
    ax.set_xticklabels([t[0] for t in topes], fontsize=8.6, color=P["tinta"])
    ax.set_xlim(-0.60, 4.40)
    ax.set_ylim(0, 30)
    ax.set_yticks(range(0, 31, 5))
    ax.set_yticklabels([f"{v}%" for v in range(0, 31, 5)], fontsize=8.4)
    ax.set_ylabel("tope de g-cero, anual", fontsize=8.6, labelpad=8)

    ax.legend(handles=[
        Patch(color=P["rojo_oscuro"], label="reinversión × ROIC: el mínimo vinculante"),
        Patch(color=P["ocre"], alpha=0.30, label="guía FY2027: +7,1% a +8,0%"),
        Patch(color=P["azul_cielo"], label="los otros tres estimadores"),
        Line2D([], [], color=P["rojo"], lw=1.8, ls="--",
               label="5,50% · el central adoptado")],
        loc="upper center", bbox_to_anchor=(0.5, -0.135), ncol=2,
        frameon=False, fontsize=8.0, handlelength=1.6, columnspacing=2.0)

    deco(ax,
         "Tres estimadores pasan del catorce por ciento y uno dice uno y medio",
         "Candidatos a tope del crecimiento inicial (g-cero), en porcentaje anual. El método obliga\n"
         "a quedarse con el mínimo, y ese mínimo es el que aquí se rompe: se adopta el 5,50%.",
         "10-K FY2026 · EDGAR 0001628280-26-037664 · 8-K 21-may-2026",
         fig=fig)
    sub_dos_lineas(fig)
    save(fig, "c18_topes_crecimiento")


if __name__ == "__main__":
    c13(); c14(); c15(); c16(); c17(); c18()
    print("OK · c13 c14 c15 c16 c17 c18")
