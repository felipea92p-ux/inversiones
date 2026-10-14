# -*- coding: utf-8 -*-
"""Gráfico nuevo de la actualización 2026-09-08 — el único número que cambió
materialmente hoy: el ejercicio adicional de recálculo de beta incorporando
la ventana de pánico de IA (7-may-2026). Datos citados literalmente de la
sección "Actualización 2026-09-08" del documento fuente.
Ningún número aquí está inventado.
"""
import numpy as np
import chart_style as cs
import matplotlib.pyplot as plt
from paleta_qg import PALETA as P


def gbp(x, dec=1):
    return f"{x:.{dec}f}".replace(".", ",")


# ─────────────────────────────────────────────────────────────────────────
# 7) El recálculo de beta del 8-sep: tres números, y por qué ninguno mueve
#    el veredicto — el problema de fondo es la asimetría, no el beta.
# ─────────────────────────────────────────────────────────────────────────
def chart_beta_recalculo():
    fig, ax = plt.subplots(figsize=(11.2, 5.8))
    fig.subplots_adjust(top=.68, bottom=.30, left=.30, right=.90)

    filas = [
        ("Beta original del documento\n(4-sep, heredado sin desapalancar)", 0.64, 0.64, P["gris_medio"]),
        ("Beta bottom-up Hamada\n(adoptado para el WACC, 7,5-8,5%)", 0.75, 0.85, P["azul"]),
        ("Beta recalculado 8-sep\n(incl. ventana de pánico IA, 7-may-2026)", 0.342, 0.342, P["rojo_oscuro"]),
    ]
    labels = [f[0] for f in filas]
    lo = [f[1] for f in filas]
    hi = [f[2] for f in filas]
    colores = [f[3] for f in filas]
    y = np.arange(len(filas))[::-1]
    for yi, a, b, c in zip(y, lo, hi, colores):
        if a == b:
            ax.plot(a, yi, "o", color=c, markersize=13, zorder=3)
            ax.text(a + 0.025, yi, f"{a:.3f}".replace(".", ","),
                    va="center", fontsize=9.2, color=P["tinta"], fontweight="bold")
        else:
            ax.plot([a, b], [yi, yi], color=c, lw=7, solid_capstyle="round", zorder=3)
            ax.text(b + 0.025, yi, f"{a:.2f}–{b:.2f}".replace(".", ","), va="center",
                    fontsize=9.2, color=P["tinta"], fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8.6)
    ax.set_xlim(0, 1.0)
    ax.set_xlabel("Beta")
    ax.axvline(0.64, color=P["gris_linea"], lw=1, ls=":")

    fig.text(0.50, 0.155,
              "Tratado ingenuamente como señal: -43,4% de descuento implícito adicional.\n"
              "Decisión de Felipe (8-sep-2026): el veredicto NO no cambia — la asimetría del Paso 9\n"
              "(-37% downside vs +11-18% upside) es independiente del beta que se use.",
              fontsize=8.6, style="italic", ha="center", color=P["vino"])

    cs.deco(ax, "El pánico de IA hizo el beta MÁS bajo, no más alto — y no cambió nada",
            "Ejercicio de recálculo de beta del 8-sep-2026, solo por completitud documental (no reabre el veredicto)",
            "Fuente: Actualización 2026-09-08 del documento fuente. Patrón inverso al de CME/TRI/CSU.TO, "
            "donde el mismo ejercicio sí subió el beta.")
    cs.save(fig, "07_beta_recalculo_8sep")


if __name__ == "__main__":
    chart_beta_recalculo()
    print("Gráfico 07 generado en charts/")
