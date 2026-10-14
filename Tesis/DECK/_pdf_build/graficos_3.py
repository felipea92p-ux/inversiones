# -*- coding: utf-8 -*-
"""GRÁFICOS 3 · ULTRA TESIS DECK · c09, c10, c11, c12.

c09_promesas          — guía inicial contra realizado (margen operativo)
c10_cascada_oe        — la cascada de owner earnings, 1.182,0 -> 947,1
c11_matriz_valoracion — mapa de calor 3x4 de la matriz que gobierna
c12_dcf_inverso       — crecimiento implícito en el precio contra el guiado

Todas las cifras salen de DATOS.md. Ninguna se inventa ni se redondea distinto.
"""
import sys; sys.path.insert(0, "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build")
import os
os.chdir("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS/Tesis/DECK/_pdf_build")

import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.ticker import FuncFormatter
from chart_style import deco, save
from paleta_qg import PALETA as P


# ─────────────────────────────────────────────────────────────────────
# utilidades de formato español (coma decimal, punto de millar)
# ─────────────────────────────────────────────────────────────────────
def es(x, dec=1):
    s = f"{x:,.{dec}f}"
    return s.replace(",", " ").replace(".", ",").replace(" ", ".")


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


def pct(x, dec=1, signo=False):
    s = es(abs(x), dec) + "%"
    if signo:
        s = ("+" if x >= 0 else "−") + s
    elif x < 0:
        s = "−" + s
    return s


# ═════════════════════════════════════════════════════════════════════
# c09 · PROMESAS CONTRA ENTREGAS
# ═════════════════════════════════════════════════════════════════════
def c09_promesas():
    fig, ax = plt.subplots(figsize=(7.2, 4.154))
    fig.subplots_adjust(top=0.760, bottom=0.150, left=0.088, right=0.975)

    grupos = ["FY2024\n(guía del 25-may-2023)",
              "FY2025\n(guía del 23-may-2024)",
              "FY2027\n(guía del 21-may-2026)"]
    guia = [18.00, 19.50, 21.50]
    real = [21.63, 23.65, 25.00]          # el tercero NO es un dato: es la tasa base
    x = np.arange(3)
    w = 0.42
    xg = x - w / 2 - 0.02
    xr = x + w / 2 + 0.02

    ax.bar(xg, guia, w, color=P["azul_cielo"], edgecolor=P["azul_noche"],
           linewidth=0.7, zorder=3)
    ax.bar(xr[:2], real[:2], w, color=P["azul"], edgecolor=P["azul_noche"],
           linewidth=0.7, zorder=3)
    # el tercero: hueco y punteado — todavía no ha ocurrido
    ax.bar(xr[2], real[2], w, facecolor="none", edgecolor=P["azul"],
           linewidth=1.7, linestyle=(0, (4, 2.4)), zorder=3)

    # etiquetas DENTRO de cada barra
    for i in range(3):
        ax.text(xg[i], guia[i] - 1.0, pct(guia[i], 1), ha="center", va="top",
                fontsize=10.5, fontweight="bold", color=P["azul_noche"], zorder=4)
        ax.text(xg[i], guia[i] - 2.7, "guía inicial", ha="center", va="top",
                fontsize=8.2, color=P["azul_noche"], zorder=4)
    for i in range(2):
        ax.text(xr[i], real[i] - 1.0, pct(real[i], 2), ha="center", va="top",
                fontsize=10.5, fontweight="bold", color=P["fondo"], zorder=4)
        ax.text(xr[i], real[i] - 2.7, "realizado", ha="center", va="top",
                fontsize=8.2, color=P["fondo"], zorder=4)
    ax.text(xr[2], real[2] - 1.0, "por ver", ha="center", va="top",
            fontsize=10.5, fontweight="bold", color=P["azul"], zorder=4)
    # la nota va FUERA de la barra punteada: dentro ya no cabe a esta escala
    ax.text(xr[2] + 0.26, 22.6, "si se repitiera\nla tasa base: ~25%",
            ha="left", va="center", fontsize=7.8, style="italic",
            color=P["gris"], zorder=4)

    # diferenciales
    for i, d in enumerate(["+363 pb", "+415 pb"]):
        ax.annotate("", xy=(xr[i], real[i] + 0.25), xytext=(xg[i], guia[i] + 0.25),
                    arrowprops=dict(arrowstyle="-|>", color=P["verde"], lw=1.6,
                                    shrinkA=1, shrinkB=1,
                                    connectionstyle="arc3,rad=-0.30"))
        ax.text(x[i], real[i] + 2.2, d, ha="center", va="bottom",
                fontsize=12.5, fontweight="bold", color=P["verde"])
    ax.text(x[2], real[2] + 2.2, "abierto", ha="center", va="bottom",
            fontsize=12.5, fontweight="bold", color=P["ocre"])

    ax.set_xticks(x)
    ax.set_xticklabels(grupos, fontsize=9.2, color=P["tinta"])
    ax.set_xlim(-0.62, 3.14)
    ax.set_ylim(0, 30.0)
    ax.set_ylabel("margen operativo del grupo", fontsize=8.8)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pct(v, 0)))

    deco(ax,
         "Dos de dos: esta dirección guía bajo y bate alto, y el tercero sigue abierto",
         "Margen operativo: guía inicial de mayo contra lo realizado. FY2026 no aparece\n"
         "porque la dirección retiró la guía anual por los aranceles.",
         "8-K de mayo 2023-2026 · 10-K FY2026 · EDGAR 0001628280-26-037664",
         fig=fig)
    sub_dos_lineas(fig)
    save(fig, "c09_promesas")


# ═════════════════════════════════════════════════════════════════════
# c10 · LA CASCADA DE OWNER EARNINGS  (el gráfico central del documento)
# ═════════════════════════════════════════════════════════════════════
def c10_cascada_oe():
    fig, ax = plt.subplots(figsize=(7.2, 4.267))
    fig.subplots_adjust(top=0.755, bottom=0.185, left=0.098, right=0.985)

    BASE = 850.0
    pasos = [
        ("Flujo de\noperaciones",      1182.0, "total"),
        ("Capex",                       -84.6, "paso"),
        ("Flujo de\ncaja libre",       1097.3, "total"),
        ("Compen-\nsación en\nacciones",   -44.8, "paso"),
        ("Impuestos\nde reten-\nción",      -8.4, "paso"),
        ("Ingresos\nfinancieros",       -49.0, "corr"),
        ("Calendario\nfiscal",          -48.0, "corr"),
        ("OWNER\nEARNINGS",             947.1, "total"),
    ]
    col = {"total": P["azul"], "paso": P["azul_cielo"], "corr": P["rojo_oscuro"]}

    cur, tops, bots = 0.0, [], []
    for _, v, tipo in pasos:
        if tipo == "total":
            bot, top, cur = BASE, v, v
        else:
            top, bot = cur, cur + v
            cur = bot
        tops.append(top); bots.append(bot)

    for i, (nom, v, tipo) in enumerate(pasos):
        ax.bar(i, tops[i] - bots[i], bottom=bots[i], width=0.62,
               color=col[tipo], edgecolor=P["azul_noche"], linewidth=0.7, zorder=3)
        if i < len(pasos) - 1:
            y = tops[i] if tipo == "total" else bots[i]
            ax.plot([i + 0.31, i + 1 - 0.31], [y, y], color=P["gris_medio"],
                    lw=0.9, ls=(0, (2.5, 2)), zorder=2)

    ax.axhline(947.1, color=P["gris_medio"], lw=0.9, ls=(0, (3, 3)), zorder=1)

    for i, (nom, v, tipo) in enumerate(pasos):
        if tipo == "total":
            ax.text(i, tops[i] + 9, es(v, 1), ha="center", va="bottom",
                    fontsize=11.4, fontweight="bold", color=P["azul_noche"])
        else:
            c = P["rojo_oscuro"] if tipo == "corr" else P["gris"]
            ax.text(i, tops[i] + 9, "−" + es(abs(v), 1), ha="center", va="bottom",
                    fontsize=9.8, fontweight="bold", color=c)

    # llave sobre las dos correcciones del cruce, en la zona alta libre
    y0, y1 = 1092, 1105
    ax.plot([4.62, 4.62, 6.38, 6.38], [y0, y1, y1, y0], color=P["rojo_oscuro"],
            lw=1.2, zorder=4)
    ax.text(5.5, 1112, "ángel: la caja no se cuenta dos veces\n"
                       "diablo: el calendario fiscal no se repite",
            ha="center", va="bottom", fontsize=8.2, style="italic",
            color=P["rojo_oscuro"])
    ax.text(5.10, 1163, "las dos correcciones del cruce adversarial",
            ha="center", va="bottom", fontsize=9.0, fontweight="bold",
            color=P["rojo_oscuro"])

    # el recorte total, a la derecha
    ax.add_patch(FancyArrowPatch((7.62, 947.1), (7.62, 1182.0), arrowstyle="<|-|>",
                                 mutation_scale=11, color=P["tinta"], lw=1.3, zorder=5))
    ax.text(7.50, (947.1 + 1182.0) / 2, "−234,9 M\n−19,9%", ha="right", va="center",
            fontsize=9.6, fontweight="bold", color=P["tinta"],
            bbox=dict(facecolor=P["fondo"], edgecolor="none", pad=1.6), zorder=6)

    ax.set_xticks(range(len(pasos)))
    ax.set_xticklabels([p[0] for p in pasos], fontsize=8.6, color=P["tinta"])
    for i, (nom, v, tipo) in enumerate(pasos):
        if tipo == "total":
            ax.get_xticklabels()[i].set_fontweight("bold")
            ax.get_xticklabels()[i].set_color(P["azul_noche"])
        elif tipo == "corr":
            ax.get_xticklabels()[i].set_color(P["rojo_oscuro"])
    ax.set_xlim(-0.62, 7.82)
    ax.set_ylim(BASE, 1250)
    ax.set_ylabel("millones de dólares  (eje truncado en 850)", fontsize=8.8)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: es(v, 0)))

    deco(ax,
         "De 1.182,0 a 947,1: lo que le queda al dueño tras el cruce adversarial",
         "Cascada de owner earnings de FY2026, en millones de dólares. Los dos últimos\n"
         "pasos son las correcciones que cambian el veredicto.",
         "10-K FY2026 · EDGAR 0001628280-26-037664",
         fig=fig)
    sub_dos_lineas(fig)
    save(fig, "c10_cascada_oe")


# ═════════════════════════════════════════════════════════════════════
# c11 · LA MATRIZ QUE GOBIERNA  (g-infinito 2,32%)
# ═════════════════════════════════════════════════════════════════════
def c11_matriz_valoracion():
    PRECIO = 88.73
    vals = np.array([[97.20, 100.31, 111.85, 156.22],
                     [105.32, 108.73, 121.36, 169.94],
                     [112.12, 115.78, 129.32, 181.44]])
    filas = ["Base 865\n(margen 20,5%)", "Base 947\n(central)", "Base 1.016\n(ángel)"]
    cols = ["1,63%\n(literal)", "2,50%\n(diablo)", "5,50%\n(central)", "14,69%\n(tope)"]

    fig, ax = plt.subplots(figsize=(7.2, 4.292))
    fig.subplots_adjust(top=0.755, bottom=0.210, left=0.150, right=0.845)

    cmap = LinearSegmentedColormap.from_list(
        "crema_azul", [P["fondo"], "#CDDCE4", P["azul_cielo"], P["azul"], P["azul_noche"]])
    norm = Normalize(vmin=PRECIO, vmax=vals.max())
    im = ax.imshow(vals, cmap=cmap, norm=norm, aspect="auto")

    for i in range(vals.shape[0]):
        for j in range(vals.shape[1]):
            v = vals[i, j]
            claro = norm(v) > 0.52
            destacada = (i == 1 and j == 2)
            ax.text(j, i - 0.06, es(v, 2), ha="center", va="center",
                    fontsize=15.5 if destacada else 13.2, fontweight="bold",
                    color=P["fondo"] if claro else P["tinta"], zorder=6)
            ax.text(j, i + 0.255, "+" + pct(v / PRECIO * 100 - 100, 1),
                    ha="center", va="center", fontsize=7.8, style="italic",
                    color=P["gris_claro"] if claro else P["gris"], zorder=6)
    # la celda que gobierna
    ax.add_patch(Rectangle((1.5, 0.5), 1, 1, fill=False, edgecolor=P["rojo"],
                           linewidth=3.0, zorder=5))
    # el rótulo va montado sobre el filo del recuadro, como una pestaña
    ax.text(2, 0.5, "LA QUE GOBIERNA", ha="center", va="center", fontsize=8.6,
            fontweight="bold", color=P["rojo"], zorder=7,
            bbox=dict(facecolor=P["fondo"], edgecolor="none", pad=1.8))

    ax.set_xticks(range(4)); ax.set_xticklabels(cols, fontsize=9.2, color=P["tinta"])
    ax.set_yticks(range(3)); ax.set_yticklabels(filas, fontsize=9.2, color=P["tinta"])
    ax.set_xlabel("crecimiento de los diez primeros años (g-cero)\n"
                  "en cursiva, cuánto está por encima del precio",
                  fontsize=8.8, labelpad=7)
    ax.set_ylabel("base de owner earnings, en millones", fontsize=8.8, labelpad=7)
    for s in ax.spines.values():
        s.set_visible(False)

    # barra de color: el precio de hoy es el suelo de toda la escala
    cb = fig.colorbar(im, ax=ax, fraction=0.038, pad=0.035)
    cb.outline.set_visible(False)
    cb.ax.tick_params(labelsize=7.8, length=0, colors=P["gris"])
    cb.set_ticks([100, 120, 140, 160, 180])
    cb.ax.set_yticklabels(["100", "120", "140", "160", "180"])
    cb.ax.axhline(PRECIO, color=P["rojo"], lw=4.0, clip_on=False)
    # el rótulo del precio se ancla a la FIGURA, no a la barra: así no arranca en la
    # misma x que las etiquetas de la escala ni pisa el tick de 100.
    fig.text(0.995, 0.088, "la línea roja de la barra\nes el precio de hoy, 88,73:\n"
             "el suelo de toda la escala",
             ha="right", va="bottom", fontsize=7.8, fontweight="bold",
             color=P["rojo"], linespacing=1.35)

    deco(ax,
         "Ni una sola celda de la matriz que gobierna cae por debajo del precio",
         "Valor por acción en dólares, con g-infinito al 2,32% y tasa exigida del 9,70%.\n"
         "La más barata de las doce ya está un 9,5% por encima del precio.",
         "Motor propio sobre 10-K FY2026 · EDGAR 0001628280-26-037664 · H.15",
         fig=fig)
    ax.grid(False)                      # deco() reactiva la cuadrícula: aquí estorba
    sub_dos_lineas(fig)
    save(fig, "c11_matriz_valoracion")


# ═════════════════════════════════════════════════════════════════════
# c12 · DCF INVERSO
# ═════════════════════════════════════════════════════════════════════
def c12_dcf_inverso():
    fig, ax = plt.subplots(figsize=(7.2, 4.154))
    fig.subplots_adjust(top=0.760, bottom=0.225, left=0.108, right=0.975)

    ax.axhspan(-6.6, 0, color=P["rojo_oscuro"], alpha=0.05, zorder=0)

    ax.bar(0, -3.07, 0.52, color=P["rojo_oscuro"], edgecolor=P["azul_noche"],
           linewidth=0.7, zorder=3)
    ax.bar(1, 5.50, 0.52, color=P["azul"], edgecolor=P["azul_noche"],
           linewidth=0.7, zorder=3)
    ax.bar(2, 7.00, 0.52, color=P["verde"], edgecolor=P["azul_noche"],
           linewidth=0.7, zorder=3)
    ax.bar(2, 2.00, 0.52, bottom=7.00, color=P["verde"], alpha=0.35,
           edgecolor=P["verde"], linewidth=1.0, hatch="///", zorder=3)

    ax.axhline(0, color=P["tinta"], lw=1.8, zorder=4)

    ax.text(0, -3.07 - 0.45, "−3,07%", ha="center", va="top",
            fontsize=13.5, fontweight="bold", color=P["rojo_oscuro"])
    ax.text(1, 5.50 + 0.40, "+5,50%", ha="center", va="bottom",
            fontsize=13.5, fontweight="bold", color=P["azul"])
    ax.text(2, 9.00 + 0.40, "+7,0% a +9,0%", ha="center", va="bottom",
            fontsize=13.5, fontweight="bold", color=P["verde"])
    # la distancia entre lo que se paga y lo que se promete
    ax.add_patch(FancyArrowPatch((2.70, -3.07), (2.70, 8.00), arrowstyle="<|-|>",
                                 mutation_scale=11, color=P["tinta"], lw=1.3, zorder=5))
    ax.text(2.82, 3.30, "de 10 a 12 puntos\nde distancia entre\nlo que paga el\n"
                        "mercado y lo que\npromete la empresa",
            ha="left", va="center", fontsize=8.6, color=P["tinta"])

    ax.text(1.05, -5.55, "por debajo de esta línea, el negocio encoge",
            ha="left", va="center", fontsize=8.6, style="italic", color=P["rojo_oscuro"])

    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["Lo que descuenta\nel precio de hoy\n(88,73 dólares)",
                        "El central de\nesta tesis\n(ya absorbe el\nreseteo de FY2027)",
                        "Lo que guía\nla propia Deckers\npara FY2028-FY2030\n"
                        "(\"high-single-digit\")"],
                       fontsize=8.8, color=P["tinta"])
    ax.set_xlim(-0.62, 4.10)
    ax.set_ylim(-6.6, 11.6)
    ax.set_yticks([-6, -3, 0, 3, 6, 9])
    ax.set_ylabel("owner earnings: crecimiento anual", fontsize=8.8)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: pct(v, 0, signo=(v != 0))))

    deco(ax,
         "El mercado paga por un negocio que encoge y la empresa promete crecer",
         "Crecimiento anual implícito a diez años. El precio de hoy sólo se justifica si\n"
         "los owner earnings caen un 3,07% cada año durante una década.",
         "DCF inverso propio · 10-K FY2026 · EDGAR 0001628280-26-037664 · 8-K 21-may-2026",
         fig=fig)
    sub_dos_lineas(fig)
    save(fig, "c12_dcf_inverso")


if __name__ == "__main__":
    c09_promesas()
    c10_cascada_oe()
    c11_matriz_valoracion()
    c12_dcf_inverso()
    print("OK · c09, c10, c11, c12 generados en charts/")
