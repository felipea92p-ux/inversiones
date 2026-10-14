# -*- coding: utf-8 -*-
"""Actualización de gráficos TRI, 2026-09-08 — SOLO los que muestran un número que
cambió materialmente hoy (beta / WACC / valor intrínseco / gatillo).
Regenera 03_sensibilidad_wacc.png (añade el punto de hoy) y crea 07_gatillo_hoy.png
(nuevo — el margen de 69 centavos). Cero cifras inventadas: todo viene literalmente
de la sección "Actualización 2026-09-08" del dossier fuente."""
import numpy as np, matplotlib.pyplot as plt
from chart_style import deco, save, P

# ── 03 · Sensibilidad del valor a un solo WACC (g terminal fijo en 3,0%) ──
# Igual que 2026-09-04, con el punto de la corrección de beta de hoy añadido
# como una serie SEPARADA (metodología distinta: DCF paralelo de punto único).
def c03():
    fig, ax = plt.subplots(figsize=(11.2, 4.9))
    wacc = [6.0, 7.25, 8.5]
    lo   = [220, 150, 115]
    hi   = [220, 155, 120]
    mid  = [(a+b)/2 for a, b in zip(lo, hi)]
    for w, l, h in zip(wacc, lo, hi):
        if l != h:
            ax.plot([w, w], [l, h], color=P["azul"], lw=7, solid_capstyle="round", alpha=.45, zorder=2)
    ax.plot(wacc, mid, "-o", color=P["azul"], lw=2.2, ms=9, zorder=5,
            label="DCF de rango (Paso 9, 4-sep)")
    etiquetas_val = ["US$ 220", "US$ 150-155", "US$ 115-120"]
    for w, m, et in zip(wacc, mid, etiquetas_val):
        ax.text(w, m+10, et, ha="center", fontsize=9.6, fontweight="bold", color=P["azul_noche"])
    etiquetas_w = ["~6,0%\n(mecánico,\nbeta 0,17-0,33)", "~7,25%\n(punto medio,\ncaso base ORIGINAL)",
                   "~8,5%\n(escrutado,\ncaso base RECALCULADO)"]
    for w, et in zip(wacc, etiquetas_w):
        ax.text(w, 85, et, ha="center", fontsize=7.4, color=P["gris"])

    # Punto de HOY: ejercicio paralelo de un solo punto (beta 0,40 -> WACC 6,42% -> valor 146,47)
    ax.plot([6.42], [146.47], "D", color=P["rojo"], ms=11, zorder=6,
            label="Ejercicio paralelo de hoy (beta 0,40, otra serie de owner earnings)")
    ax.annotate("HOY: beta 0,40 → WACC 6,42%\nvalor US$146,47 (otro DCF, otra\nserie de owner earnings)\ngatillo US$109,85 — YA CRUZADO",
                xy=(6.45, 150), xytext=(6.85, 205),
                fontsize=7.6, color=P["rojo"], fontweight="bold", ha="left",
                bbox=dict(boxstyle="round,pad=0.35", fc=P["fondo"], ec=P["rojo"], lw=0.8),
                arrowprops=dict(arrowstyle="-|>", color=P["rojo"], lw=1.4))

    ax.axhspan(102.62, 102.62, color=P["ocre"], alpha=0)  # placeholder, real line below
    ax.axhline(102.62, color=P["tinta"], lw=1.3, ls=":", zorder=3)
    ax.text(8.9, 106.5, "PRECIO DE HOY  US$102,62", fontsize=8.6, color=P["tinta"], fontweight="bold",
            va="bottom", ha="right")
    ax.set_xlabel("WACC usado en el DCF (%)"); ax.set_ylabel("valor por acción (US$)")
    ax.set_xlim(5.5, 9.2); ax.set_ylim(75, 240)
    ax.legend(loc="upper right", fontsize=7.6, frameon=False)
    fig.subplots_adjust(top=.72, bottom=.13, left=.075, right=.97)
    deco(ax, "Un parámetro mueve el valor de 220 a 115 dólares — y hoy casi lo hizo otra vez",
         "El punto de hoy usa un DCF paralelo con su propia serie de owner earnings: converge en diagnóstico, no en cifra, con el DCF de rango.",
         "Fuente: Paso 9.4 del dossier TRI (4-sep) y Actualización 2026-09-08 (ejercicio de verificación cruzada, 8-sep).", fig)
    save(fig, "03_sensibilidad_wacc")

# ── 07 · El margen que se evapora: 0,69 US$ decide el veredicto de hoy ────
def c07():
    fig, ax = plt.subplots(figsize=(11.2, 5.0))
    betas = [0.40, 0.45]
    gatillos = [109.85, 103.31]  # 103.31 = 102.62 + 0.69, aritmética directa del propio dossier
    colores = [P["azul"], P["rojo_oscuro"]]
    x = np.array([0, 1.15])
    ax.bar(x, [g - 90 for g in gatillos], bottom=90, color=colores, width=.6, zorder=3)
    for i, (b, g) in enumerate(zip(betas, gatillos)):
        col = P["azul_noche"] if i == 0 else P["rojo_oscuro"]
        ax.text(x[i], g + 1.6, f"gatillo US$ {g:.2f}".replace(".", ","), ha="center", fontsize=11.5,
                fontweight="bold", color=col)
        ax.text(x[i], 91.5, f"beta {b:.2f}".replace(".", ","), ha="center", fontsize=10, color="white",
                fontweight="bold")
    ax.axhline(102.62, color=P["tinta"], lw=1.6, ls="--", zorder=4)
    ax.text(1.85, 102.62, " precio de hoy\n US$ 102,62", fontsize=8.8, color=P["tinta"], fontweight="bold",
            va="center", ha="left")
    ax.text(x[0], 96.2, "margen sobre el precio:\nUS$ 7,23 (6,6%)", ha="center", fontsize=8.8,
            color=P["azul_noche"], fontweight="bold")
    ax.text(x[1], 96.2, "margen sobre el precio:\nUS$ 0,69 (0,7%)", ha="center", fontsize=8.8,
            color=P["rojo_oscuro"], fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(["Beta 0,40\n(usado en la 1ª lectura de hoy)",
                         "Beta 0,45\n(extremo conservador, misma banda)"], fontsize=9.2)
    ax.set_xlim(-0.75, 2.55)
    ax.set_ylabel("gatillo de compra (US$/acción)")
    ax.set_ylim(90, 120)
    fig.subplots_adjust(top=.72, bottom=.15, left=.085, right=.97)
    deco(ax, "0,05 de beta borran el 90% del margen de compra",
         "El “COMPRAR” de la primera lectura de hoy dependía de elegir 0,40 y no 0,45 — dos betas igual de defendibles dentro de la misma banda de estimación.",
         "Fuente: Actualización 2026-09-08 del dossier TRI — segundo abogado del diablo, Golpe 1 (sección 13).", fig)
    save(fig, "07_gatillo_hoy")

for f in [c03, c07]:
    f(); print("ok", f.__name__)
