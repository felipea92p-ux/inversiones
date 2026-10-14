# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis NEM v1. Todos los datos ya verificados en el
borrador de síntesis metodo-12-pasos (2026-09-04) -- sin recalcular, solo
visualizar lo ya evidenciado en los Pasos 5 y 9."""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save, P

FUENTE_BASE = "Fuente: sintesis Metodo QG 12 pasos, Ultra Tesis NEM 2026-09-04 (Pasos 5 y 9), sobre Geschaftsberichte 2021-2025 e informe 2T-2026 de Nemetschek SE."

# -- 01 · Rango de valor (DCF) frente al precio de hoy -----------------------
def c01():
    escenarios = ["BEAR\n(10%->3%, WACC 7,5%)", "BASE\n(14%->4%, WACC 6,5%)", "BULL\n(16%->6%, WACC 5,5%)"]
    valores = [100, 171, 325]
    cols = [P["rojo_oscuro"], P["azul"], P["verde"]]
    fig, ax = plt.subplots(figsize=(11.2, 5.0))
    b = ax.bar(range(3), valores, color=cols, width=0.52, zorder=3)
    for i, v in enumerate(valores):
        ax.text(i, v + 8, f"{v} EUR", ha="center", fontsize=11.5, fontweight="bold", color=cols[i])
    ax.axhspan(63, 68, color=P["ocre"], alpha=0.30, zorder=2)
    ax.text(2.42, 65.5, "precio hoy\n63-68 EUR", fontsize=8.4, color=P["tinta"], fontweight="bold",
            va="center", ha="left")
    ax.set_xticks(range(3)); ax.set_xticklabels(escenarios, fontsize=8.8)
    ax.set_ylabel("valor por accion (EUR)")
    ax.set_ylim(0, 360); ax.set_xlim(-0.6, 3.0)
    fig.subplots_adjust(top=0.74, bottom=0.14, left=0.08, right=0.97)
    deco(ax, "Incluso el escenario BEAR queda muy por encima del precio de hoy",
         "Los tres escenarios usan mi rango bottom-up (hasta 7,5%). Con el WACC del emisor/mercado (9,9-11,9%) el resultado cambia del todo.",
         FUENTE_BASE, fig)
    save(fig, "01_rango_valor_vs_precio")

# -- 02 · El motor: crecimiento observado vs. g de reinversion x ROIC -------
def c02():
    anos = ["2022", "2023", "2024\n(GoCanvas)", "2025", "Promedio\n'normal'\n(22-23-25)"]
    obs = [17.7, 6.2, 16.9, 19.7, 14.5]
    g_impl = [9.5, 7.5, None, 7.0, 7.5]  # centro de rango; 2024 no aplicable
    x = np.arange(5); w = 0.34
    fig, ax = plt.subplots(figsize=(11.2, 4.8))
    ax.bar(x - w/2, obs, w, color=P["azul"], label="Crecimiento de ingresos observado", zorder=3)
    for i, v in enumerate(obs):
        ax.text(x[i] - w/2, v + 0.5, f"{v:.1f}".replace(".", ",") + "%", ha="center", fontsize=8.2,
                fontweight="bold", color=P["azul"])
    for i, v in enumerate(g_impl):
        if v is None:
            ax.text(x[i] + w/2, 2.2, "formula no\naplicable\n(escalon M&A)", ha="center", fontsize=7.0,
                    color=P["gris"], style="italic")
        else:
            ax.bar(x[i] + w/2, v, w, color=P["ocre"], zorder=3,
                   label="g implicito (reinversion x ROIC)" if i == 0 else None)
            ax.text(x[i] + w/2, v + 0.5, f"{v:.1f}".replace(".", ",") + "%", ha="center", fontsize=8.2,
                    fontweight="bold", color=P["ocre"])
    ax.set_xticks(x); ax.set_xticklabels(anos, fontsize=8.2)
    ax.set_ylabel("% anual"); ax.set_ylim(0, 24)
    ax.legend(frameon=False, fontsize=8.4, loc="upper left")
    fig.subplots_adjust(top=0.74, bottom=0.14, left=0.08, right=0.97)
    deco(ax, "El crecimiento real supera de forma consistente al de la formula",
         "La brecha (obs. ~14,5-19,7% frente a formula ~6-9%) la explican saltos de M&A discretos, no reinversion organica suave.",
         FUENTE_BASE, fig)
    save(fig, "02_motor_crecimiento")

# -- 03 · Triangulacion del WACC: tres fuentes independientes ---------------
def c03():
    filas = [
        ("Bottom-up propio\n(CAPM, beta bruto XETRA)", 5.4, 7.5, P["azul"]),
        ("Mercado, DCF inverso\n(precio hoy 63-75 EUR)", 10.7, 11.9, P["rojo"]),
        ("Emisor / PwC\n(test de deterioro 2022-2025)", 9.9, 13.9, P["azul_noche"]),
    ]
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    for i, (lab, lo, hi, col) in enumerate(filas):
        ax.plot([lo, hi], [i, i], color=col, lw=7, solid_capstyle="round", zorder=3)
        ax.text((lo+hi)/2, i + 0.28, f"{lo:.1f}".replace(".", ",") + "% - " + f"{hi:.1f}".replace(".", ",") + "%",
                ha="center", fontsize=9.2, fontweight="bold", color=col)
    ax.set_yticks(range(3)); ax.set_yticklabels([f[0] for f in filas], fontsize=8.6)
    ax.set_xlabel("WACC despues de impuestos (%)")
    ax.set_xlim(4.5, 15.5); ax.set_ylim(-0.6, 2.9)
    ax.axvspan(9.9, 11.9, color=P["gris_claro"], zorder=1)
    fig.subplots_adjust(top=0.74, bottom=0.16, left=0.30, right=0.97)
    deco(ax, "Dos fuentes ajenas al analisis propio convergen muy por encima del rango bottom-up",
         "El emisor (test de deterioro PwC) y el mercado (DCF inverso) coinciden en 9,9%-11,9%, muy por encima de mi rango bottom-up.",
         FUENTE_BASE, fig)
    save(fig, "03_triangulacion_wacc")

# -- 04 · DCF inverso: WACC implicito segun el precio pagado ----------------
def c04():
    precios = [63, 68, 75]
    wacc_impl = [11.9, 11.4, 10.7]
    fig, ax = plt.subplots(figsize=(11.2, 4.8))
    ax.axhspan(5.4, 7.5, color=P["azul_cielo"], alpha=0.35, zorder=1)
    ax.text(76.3, 6.45, "mi rango\nbottom-up", fontsize=7.6, color=P["azul"], ha="left", va="center")
    ax.axhspan(9.9, 13.9, color=P["gris_claro"], zorder=1)
    ax.text(76.3, 11.9, "rango del\nemisor/PwC", fontsize=7.6, color=P["gris"], ha="left", va="center")
    ax.plot(precios, wacc_impl, "-o", color=P["rojo"], lw=2.4, ms=9, zorder=3)
    for x, y in zip(precios, wacc_impl):
        ax.text(x, y + 0.35, f"{y:.1f}".replace(".", ",") + "%", ha="center", fontsize=9.4,
                fontweight="bold", color=P["rojo"])
    ax.set_xticks(precios); ax.set_xticklabels([f"{p} EUR" for p in precios], fontsize=9.2)
    ax.set_xlabel("precio pagado por accion"); ax.set_ylabel("WACC que ese precio exige (%)")
    ax.set_xlim(60, 90); ax.set_ylim(4.5, 15.5)
    fig.subplots_adjust(top=0.74, bottom=0.14, left=0.09, right=0.85)
    deco(ax, "Al precio de hoy, el mercado ya exige un WACC fuera de mi rango bottom-up",
         "A que WACC iguala el precio de hoy el EV de mercado, dado el crecimiento guiado: a 63 EUR, 11,9%; a 75 EUR, 10,7%.",
         FUENTE_BASE, fig)
    save(fig, "04_dcf_inverso_precio")

# -- 05 · Beta: NEM frente a los pares cotizados en EE.UU. ------------------
def c05():
    fig, ax = plt.subplots(figsize=(11.2, 4.2))
    filas = [
        ("Nemetschek\n(beta bruto, XETRA 5 anios)", 0.51, 0.53, P["rojo"]),
        ("Bentley Systems\n(beta propio, el par mas cercano)", 0.98, 0.98, P["azul_noche"]),
        ("4 pares EE.UU.\n(beta Hamada re-apalancado)", 0.74, 1.36, P["azul"]),
    ]
    for i, (lab, lo, hi, col) in enumerate(filas):
        if lo == hi:
            ax.scatter([lo], [i], s=140, color=col, zorder=4)
            ax.text(lo, i + 0.30, f"{lo:.2f}".replace(".", ","), ha="center", fontsize=9.2,
                    fontweight="bold", color=col)
        else:
            ax.plot([lo, hi], [i, i], color=col, lw=7, solid_capstyle="round", zorder=3)
            ax.text((lo+hi)/2, i + 0.30, f"{lo:.2f}-{hi:.2f}".replace(".", ","), ha="center",
                    fontsize=9.2, fontweight="bold", color=col)
    ax.set_yticks(range(3)); ax.set_yticklabels([f[0] for f in filas], fontsize=8.4)
    ax.set_xlabel("beta"); ax.set_xlim(0.3, 1.55); ax.set_ylim(-0.6, 2.9)
    fig.subplots_adjust(top=0.74, bottom=0.16, left=0.33, right=0.97)
    deco(ax, "El beta que el mercado aleman mide para NEM es el mas bajo de todo el grupo comparable",
         "Los cuatro pares en EE.UU., re-apalancados, tienen un beta mayor: el de XETRA parece reflejar liquidez baja, no menor riesgo.",
         FUENTE_BASE, fig)
    save(fig, "05_beta_pares")

if __name__ == "__main__":
    c01(); c02(); c03(); c04(); c05()
    print("5 graficos generados en charts/")
