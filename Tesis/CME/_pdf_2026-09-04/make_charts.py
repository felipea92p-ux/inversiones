# -*- coding: utf-8 -*-
"""Gráficos CME · Ultra Tesis método 12 pasos · 2026-09-04
Todos los datos son literales del dossier fuente
(2026-09-04_UltraTesis_CME_metodo12_borrador.md). Cero cifras inventadas.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from chart_style import deco, save
from paleta_qg import PALETA as P

# ── (a) Rango de valor intrínseco vs. precio actual ─────────────────────
def c01_valor():
    fig, ax = plt.subplots(figsize=(11.2, 5.0))
    cats = ["BAJISTA PROPIO\nWACC 9,5% · g~2,5-3%\n(no centinela)",
            "PISO CONSERVADOR\nWACC 9,0% / g 3,5%",
            "CASO BASE\nWACC 7,5% / g 3,5%\n(confianza degradada)",
            "BETA CRUDO 0,27\nWACC 5,9% / g 3,5%\n(RECHAZADO, Paso 9)"]
    vals = [154, 258, 357, 599]
    cols = [P["rojo_oscuro"], P["azul_acero"], P["azul"], P["gris_medio"]]
    hatches = [None, None, "//", "xx"]
    bars = ax.bar(range(4), vals, color=cols, width=0.56)
    for b, h in zip(bars, hatches):
        if h:
            b.set_hatch(h)
            b.set_edgecolor(P["fondo"])
    for i, v in enumerate(vals):
        ax.text(i, v + 12, f"{v} US$", ha="center", fontsize=11.5, fontweight="bold", color=cols[i])
    # precio actual
    ax.axhline(280, color=P["rojo"], lw=2.2, ls="--")
    ax.text(3.5, 292, "PRECIO HOY ~280 US$\n(278-281)", fontsize=8.6, color=P["rojo"],
            fontweight="bold", ha="right")
    # anclas del gate vigente
    ax.axhline(235, color=P["ocre"], lw=1.4, ls=":")
    ax.text(-0.46, 240, "ancla gate 235", fontsize=7.6, color="#8a6508", fontweight="bold", va="bottom")
    ax.axhline(200, color=P["ocre"], lw=1.4, ls=":")
    ax.text(-0.46, 205, "ancla gate 200", fontsize=7.6, color="#8a6508", fontweight="bold", va="bottom")
    ax.set_xticks(range(4))
    ax.set_xticklabels(cats, fontsize=7.9)
    ax.set_ylabel("valor por acción (US$)")
    ax.set_ylim(0, 660)
    fig.subplots_adjust(top=0.74, bottom=0.20, left=0.075, right=0.98)
    deco(ax, "El bajista cae bajo el ancla de entrada; el alcista depende de un beta rechazado",
         "DCF a 10 años, owner earnings TTM ≈4.113 M US$. El caso base usa un g terminal de 3,5% marcado como "
         "no verificado mecánicamente (Paso 10, Golpe 2).",
         "Fuente: dossier CME método 12 pasos, Paso 9 y Paso 10 (2026-09-04). Precio y anclas de gate: nota de contexto de cartera.",
         fig)
    save(fig, "01_valor_intrinseco")


# ── (c) Sensibilidad del valor al WACC, a g terminal fijo ───────────────
def c02_wacc():
    wacc = np.array([9.0, 7.5, 6.9, 5.9])
    val = np.array([258, 357, 401, 599])
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    ax.plot(wacc, val, "-", color=P["azul"], lw=2.2, zorder=3)
    ax.scatter(wacc[:3], val[:3], s=95, color=P["azul_noche"], zorder=4)
    ax.scatter(wacc[3], val[3], s=140, marker="X", color=P["rojo_oscuro"], zorder=6)
    for x, y, lab in zip(wacc, val, ["9,0%\n(piso)", "7,5%\n(caso base)", "6,9%\n(tasas −80pb)", "5,9% (beta crudo,\nRECHAZADO)"]):
        ax.annotate(f"{y} US$", (x, y), (x, y + 26), ha="center", fontsize=9, fontweight="bold",
                    color=P["rojo_oscuro"] if y == 599 else P["azul_noche"], zorder=7)
        dy = -95 if y == 599 else -42
        ax.annotate(lab, (x, y), (x, y + dy), ha="center", fontsize=7.6, color=P["gris"], zorder=4)
    ax.axvspan(7.0, 9.0, color=P["ocre"], alpha=0.18)
    ax.text(8.0, 615, "banda de trabajo\ndefendible 7%-9%", ha="center", fontsize=8.2,
            color="#8a6508", fontweight="bold")
    ax.axhline(280, color=P["rojo"], lw=1.8, ls="--")
    ax.text(6.65, 305, "precio hoy ~280 US$ (278-281)", fontsize=8.2, color=P["rojo"], fontweight="bold", ha="center")
    ax.set_xlabel("WACC empleado (%)")
    ax.set_ylabel("valor por acción (US$)")
    ax.invert_xaxis()
    ax.set_ylim(120, 660)
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.08, right=0.97)
    deco(ax, "El valor casi se triplica moviendo solo el WACC, a un g terminal fijo",
         "Con un spread WACC−g de apenas 2,4 puntos (escenario de beta crudo), el múltiplo terminal implícito "
         "salta a ~43x owner earnings del año 10, frente a ~19x en el piso de 9,0%.",
         "Fuente: dossier CME método 12 pasos, Paso 9 (2026-09-04). Los 4 puntos usan g terminal = 3,5%; "
         "sin malla de g independiente en la fuente, no se construye (candado de no inventar cifras).",
         fig)
    save(fig, "02_wacc_sensibilidad")


# ── (d) Beta de CME frente a pares inmediatos ────────────────────────────
def c03_beta():
    nombres = ["CME", "CBOE", "ICE", "NDAQ"]
    betas = [0.27, 0.41, 0.93, 0.97]
    cols = [P["rojo_oscuro"], P["azul_acero"], P["azul"], P["azul_pro"]]
    fig, ax = plt.subplots(figsize=(11.2, 4.4))
    bars = ax.bar(nombres, betas, color=cols, width=0.5)
    for b, v in zip(bars, betas):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.025, f"{v:.2f}", ha="center",
                fontsize=11, fontweight="bold", color=P["tinta"])
    ax.axhline(0.70, color=P["ocre"], lw=1.8, ls=":")
    ax.text(0.65, 0.735, "ancla sectorial ~0,70 (usada si el beta propio falla)", fontsize=7.8,
            color="#8a6508", fontweight="bold", ha="center")
    ax.axhline(1.00, color=P["gris"], lw=1.4, ls="--")
    ax.text(0.65, 1.035, "techo conservador 1,00", fontsize=7.8, color=P["gris"], fontweight="bold", ha="center")
    ax.set_ylabel("beta (5 años, datos de mercado)")
    ax.set_ylim(0, 1.12)
    fig.subplots_adjust(top=0.76, bottom=0.12, left=0.08, right=0.97)
    deco(ax, "La beta de CME es un valor atípico incluso dentro de su propio sector",
         "0,27 deja el spread entre el coste de equity y la propia deuda AA- de CME por debajo de 1 punto — "
         "implausible para el accionista, que es acreedor residual (Paso 9).",
         "Fuente: dossier CME método 12 pasos, Paso 7 y Paso 9 (2026-09-04); Yahoo Finance / stockanalysis.com. "
         "Uso exclusivamente técnico para construir el WACC — no es comparación de mérito de inversión (Candado C).",
         fig)
    save(fig, "03_beta_pares")


# ── (e) El motor de reinversión: capex vs. D&A, 2021-2025 ────────────────
def c04_motor():
    years = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
    capex = [127.2, 89.7, 76.4, 94.0, 83.5]
    da = [147.8, 134.9, 126.0, 115.1, 107.5]
    roic = [7, 8, 10, 11, 12]
    x = np.arange(5)
    fig, ax = plt.subplots(figsize=(11.2, 4.7))
    ax2 = ax.twinx()
    w = 0.34
    ax.bar(x - w/2, capex, width=w, color=P["azul_acero"], label="Capex total")
    ax.bar(x + w/2, da, width=w, color=P["terracota"], label="D&A de mantenimiento")
    for i in range(5):
        ax.text(x[i] - w/2, capex[i] + 3, f"{capex[i]:.0f}", ha="center", fontsize=7.6, color=P["azul_noche"])
        ax.text(x[i] + w/2, da[i] + 3, f"{da[i]:.0f}", ha="center", fontsize=7.6, color="#7a4a3a")
    ax2.plot(x, roic, "-o", color=P["verde"], lw=2.0, ms=6, zorder=5)
    for i in range(5):
        ax2.text(x[i], roic[i] + 0.6, f"{roic[i]}%", ha="center", fontsize=8.4, fontweight="bold", color=P["verde"])
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylabel("US$ millones")
    ax2.set_ylabel("ROIC contable (%)", color=P["verde"])
    ax2.set_ylim(0, 16)
    ax.set_ylim(0, 170)
    ax.legend(loc="upper right", frameon=False, fontsize=8.4)
    fig.subplots_adjust(top=0.76, bottom=0.12, left=0.08, right=0.90)
    deco(ax, "Capex por debajo de la depreciación los cinco años: el framework mecánico da g negativo",
         "El ROIC mejora igual (7%→12%): el crecimiento no viene de capex capitalizado (Paso 5). El motor "
         "alternativo no está probado en bajo volumen (Paso 10, Golpe 2).",
         "Fuente: dossier CME método 12 pasos, Paso 5 (2026-09-04), sobre los cinco 10-K FY2021-FY2025.",
         fig)
    save(fig, "04_motor_reinversion")


if __name__ == "__main__":
    c01_valor()
    c02_wacc()
    c03_beta()
    c04_motor()
    print("4 gráficos generados en charts/")
