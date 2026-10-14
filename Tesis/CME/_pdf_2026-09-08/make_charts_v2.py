# -*- coding: utf-8 -*-
"""Gráficos CME · Ultra Tesis método 12 pasos · actualización 2026-09-08
Regenera SOLO los tres gráficos que muestran un número que cambió
materialmente con la corrección de beta/WACC del 8-sep (01, 02, 03).
El 04 (motor de reinversión) no depende de beta/WACC y se reutiliza tal cual
del build del 4-sep-2026.
Todos los datos son literales del dossier fuente + la Actualización 2026-09-08.
Cero cifras inventadas.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from chart_style import deco, save
from paleta_qg import PALETA as P

# ── (a) Rango de valor intrínseco vs. precio actual — con la corrección de hoy ──
def c01_valor():
    fig, ax = plt.subplots(figsize=(11.6, 5.2))
    cats = ["BAJISTA PROPIO\nWACC 9,5% · g~2,5-3%\n(no centinela, 4-sep)",
            "PISO CONSERVADOR\nWACC 9,0% / g 3,5%\n(4-sep)",
            "CORREGIDO HOY\nbeta 0,65 · WACC 7,61%\n(cross-validación 8-sep)",
            "CASO BASE\nWACC 7,5% / g 3,5%\n(4-sep, confianza degradada)",
            "BETA CRUDO 0,27\nWACC 5,9% / g 3,5%\n(RECHAZADO, Paso 9)"]
    vals = [154, 258, 338.79, 357, 599]
    cols = [P["rojo_oscuro"], P["azul_acero"], P["rojo"], P["azul"], P["gris_medio"]]
    hatches = [None, None, None, "//", "xx"]
    bars = ax.bar(range(5), vals, color=cols, width=0.58)
    for b, h in zip(bars, hatches):
        if h:
            b.set_hatch(h)
            b.set_edgecolor(P["fondo"])
    for i, v in enumerate(vals):
        lab = f"{v:.2f} US$".replace(".", ",") if v == 338.79 else f"{v:.0f} US$"
        ax.text(i, v + 12, lab, ha="center", fontsize=11, fontweight="bold", color=cols[i])
    # precio actual (8-sep-2026) — todas las líneas de referencia se etiquetan
    # apiladas a la derecha (fuera de las columnas de barras) para no chocar
    # con las etiquetas de valor de las barras BAJISTA PROPIO / PISO CONSERVADOR,
    # cuya altura (154 / 258) cae justo dentro de esta banda 150-290.
    ax.axhline(279.81, color=P["rojo"], lw=2.2, ls="--")
    ax.text(4.48, 300, "PRECIO HOY 279,81 US$\n(8-sep-2026)", fontsize=8.4, color=P["rojo"],
            fontweight="bold", ha="right", va="bottom")
    # gatillo de compra recalculado hoy (MoS 30% sobre 338,79)
    ax.axhline(237.15, color=P["rojo_oscuro"], lw=1.6, ls="-.")
    ax.text(4.48, 230, "gatillo recalculado hoy 237,15\n(MoS 30% s/ 338,79)", fontsize=7.3,
            color=P["rojo_oscuro"], fontweight="bold", ha="right", va="top")
    # anclas del gate vigente en gates.md — dos tramos, una sola etiqueta
    ax.axhline(235, color=P["ocre"], lw=1.4, ls=":")
    ax.axhline(200, color=P["ocre"], lw=1.4, ls=":")
    ax.text(4.48, 180, "ancla gate 235 / 200 (dos tramos)", fontsize=7.4, color="#8a6508",
            fontweight="bold", ha="right", va="top")
    ax.set_xticks(range(5))
    ax.set_xticklabels(cats, fontsize=7.3)
    ax.set_ylabel("valor por acción (US$)")
    ax.set_ylim(0, 660)
    fig.subplots_adjust(top=0.74, bottom=0.20, left=0.075, right=0.98)
    deco(ax, "Con el beta corregido, el valor cae dentro de la banda 7-9% ya prevista, lejos del beta crudo",
         "El descuento aparente se comprime de −37,9% a −17,4% — insuficiente frente al 30% que exige el "
         "Bloque 2 para gatillar compra.",
         "Fuente: dossier CME método 12 pasos, Paso 9 (2026-09-04) y Actualización 2026-09-08 (cross-validación "
         "independiente). Precio y anclas de gate: nota de contexto de cartera / gates.md.",
         fig)
    save(fig, "01_valor_intrinseco")


# ── (c) Sensibilidad del valor al WACC — con el punto corregido de hoy ──
def c02_wacc():
    wacc = np.array([9.0, 7.61, 7.5, 6.9, 5.9])
    val = np.array([258, 338.79, 357, 401, 599])
    fig, ax = plt.subplots(figsize=(11.6, 4.8))
    orden = np.argsort(-wacc)
    ax.plot(wacc[orden], val[orden], "-", color=P["azul"], lw=1.6, zorder=2, alpha=0.55)
    ax.scatter([9.0, 7.5, 6.9, 5.9], [258, 357, 401, 599], s=90, color=P["azul_noche"], zorder=4)
    ax.scatter([5.9], [599], s=140, marker="X", color=P["gris_medio"], zorder=6)
    ax.scatter([7.61], [338.79], s=170, marker="*", color=P["rojo"], zorder=8,
               edgecolor=P["tinta"], linewidth=0.6)
    etiquetas = {9.0: ("9,0%\n(piso, 4-sep)", -42, P["azul_noche"]),
                 7.5: ("7,5%\n(caso base, 4-sep)", -42, P["azul_noche"]),
                 6.9: ("6,9%\n(tasas −80pb, 4-sep)", -42, P["azul_noche"]),
                 5.9: ("5,9% (beta crudo,\nRECHAZADO)", -95, P["gris_medio"])}
    for x, (lab, dy, col) in etiquetas.items():
        y = val[list(wacc).index(x)]
        ax.annotate(f"{y:.0f} US$", (x, y), (x, y + 26), ha="center", fontsize=8.6, fontweight="bold",
                    color=col, zorder=7)
        ax.annotate(lab, (x, y), (x, y + dy), ha="center", fontsize=7.3, color=P["gris"], zorder=4)
    ax.annotate("338,79 US$", (7.61, 338.79), (7.61, 338.79 + 30), ha="center", fontsize=9.2,
                fontweight="bold", color=P["rojo"], zorder=9)
    ax.annotate("beta 0,65 corregido\nWACC 7,61% (8-sep)", (7.61, 338.79), (7.61, 338.79 - 70),
                ha="center", fontsize=7.6, color=P["rojo"], fontweight="bold", zorder=9)
    ax.axvspan(7.0, 9.0, color=P["ocre"], alpha=0.16)
    ax.text(8.0, 615, "banda de trabajo\ndefendible 7%-9% (4-sep)", ha="center", fontsize=8.0,
            color="#8a6508", fontweight="bold")
    ax.axhline(279.81, color=P["rojo"], lw=1.6, ls="--", alpha=0.8)
    ax.text(6.5, 300, "precio hoy 279,81 US$ (8-sep-2026)", fontsize=7.8, color=P["rojo"],
            fontweight="bold", ha="center")
    ax.set_xlabel("WACC empleado (%)")
    ax.set_ylabel("valor por acción (US$)")
    ax.invert_xaxis()
    ax.set_ylim(120, 660)
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.08, right=0.97)
    deco(ax, "El beta corregido aterriza justo dentro de la banda que el 4-sep ya llamaba defendible",
         "7,61% no es un número nuevo y ajeno: es la validación independiente, un lote de empresas distinto, "
         "de la misma banda 7%-9% que el documento original ya defendía frente al beta crudo.",
         "Fuente: dossier CME método 12 pasos, Paso 9 (2026-09-04) y Actualización 2026-09-08. Los puntos de "
         "4-sep usan g terminal = 3,5%; el punto de 8-sep es una construcción independiente (ver sección 12).",
         fig)
    save(fig, "02_wacc_sensibilidad")


# ── (d) Beta de CME frente a pares — con la corrección promedio de hoy ──
def c03_beta():
    nombres = ["CME\n(crudo)", "CBOE", "ICE", "NDAQ", "CME\n(corregido)"]
    betas = [0.27, 0.41, 0.93, 0.97, 0.65]
    cols = [P["gris_medio"], P["azul_acero"], P["azul"], P["azul_pro"], P["rojo"]]
    fig, ax = plt.subplots(figsize=(11.6, 4.7))
    bars = ax.bar(nombres, betas, color=cols, width=0.52)
    bars[0].set_hatch("xx"); bars[0].set_edgecolor(P["fondo"])
    bars[4].set_hatch("--"); bars[4].set_edgecolor(P["fondo"])
    for b, v in zip(bars, betas):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.025, f"{v:.2f}".replace(".", ","), ha="center",
                fontsize=11, fontweight="bold", color=P["tinta"])
    ax.axhline(0.66, color=P["ocre"], lw=1.8, ls=":")
    ax.text(1.55, 0.695, "beta sectorial Damodaran «Investments & Asset\nManagement» 0,66 (ene-2026) — valida "
            "el promedio", fontsize=7.5, color="#8a6508", fontweight="bold", ha="center")
    ax.axhline(1.00, color=P["gris"], lw=1.2, ls="--")
    ax.text(0.4, 1.03, "techo conservador 1,00 (4-sep)", fontsize=7.4, color=P["gris"], fontweight="bold", ha="left")
    ax.set_ylabel("beta (5 años, datos de mercado)")
    ax.set_ylim(0, 1.12)
    fig.subplots_adjust(top=0.74, bottom=0.12, left=0.08, right=0.97)
    deco(ax, "CME era el beta más bajo de sus 4 pares directos — el promedio de los 4 lo corrige a 0,65",
         "El beta crudo (0,27) ignoraba que la propia tesis llama a FMX «el riesgo competitivo más serio en "
         "dos décadas». Corregido = promedio de los 4 pares, validado contra Damodaran.",
         "Fuente: Actualización 2026-09-08 (cross-validación, 5 tesis en paralelo); Damodaran/NYU Stern "
         "(ene-2026). Uso técnico para el WACC — no es mérito de inversión (Candado C).",
         fig)
    save(fig, "03_beta_pares")


if __name__ == "__main__":
    c01_valor()
    c02_wacc()
    c03_beta()
    print("3 gráficos regenerados en charts/ (01, 02, 03). El 04 se reutiliza del 4-sep-2026 sin cambios.")
