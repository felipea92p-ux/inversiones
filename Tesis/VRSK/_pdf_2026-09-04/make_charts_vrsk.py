# -*- coding: utf-8 -*-
"""Gráficos VRSK · Ultra Tesis · 2026-09-04
Todas las cifras provienen literalmente del dossier fuente
(2026-09-04_UltraTesis_VRSK_metodo12_borrador.md). Ninguna se recalcula
ni se interpola: donde la fuente da un rango, se dibuja el rango; donde
da un punto, se dibuja un punto. No hay gráfico de "sensibilidad WACC"
clásico (valor en función de varios puntos de WACC) porque el dossier
no reporta valor a más de un WACC — solo el WACC central (7,1%) usado
en las tres cajas de escenario. En su lugar, 04_wacc_build muestra la
construcción bottom-up del propio WACC (beta, coste de equity, coste
de deuda, mezcla), que sí está completamente documentada.
"""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save, P

OUTDIR = "charts"

# ── 01 · Rango de valor vs. precio ──────────────────────────────────────
def c01():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    filas = ["BULL\nreaceleración 7-9%, margen 60-61%",
             "BASE\nglide 5%→6%→4% terminal",
             "BEAR\ndeceleración a 2-3%, margen 55%",
             "CONSENSO SELL-SIDE\n19 analistas, 19-ago-2026"]
    lo   = [360, 207, 125, 195]
    hi   = [375, 272, 130, 275]
    mid  = [None, 230, None, 237.71]  # solo se marca el punto central donde el dossier lo da
    cols = [P["verde"], P["azul"], P["rojo_oscuro"], P["gris_medio"]]
    y = np.arange(len(filas))[::-1]
    for i, (a, b, c) in enumerate(zip(lo, hi, cols)):
        ax.barh(y[i], b - a, left=a, height=0.5, color=c, alpha=.85, zorder=3)
        ax.text(a - 7, y[i], f"{a:,.0f}".replace(",", "."), ha="right", va="center",
                fontsize=8.6, color=c, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.12", fc=P["fondo"], ec="none"))
        ax.text(b + 7, y[i], f"{b:,.0f}".replace(",", "."), ha="left", va="center",
                fontsize=8.6, color=c, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.12", fc=P["fondo"], ec="none"))
    if mid[1] is not None:
        ax.scatter([mid[1]], [y[1]], marker="D", s=55, color=P["azul_noche"], zorder=5)
        ax.text(mid[1], y[1] + 0.32, f"centro ~{mid[1]:.0f}", ha="center", fontsize=7.6,
                color=P["azul_noche"], fontweight="bold")
    if mid[3] is not None:
        ax.scatter([mid[3]], [y[3]], marker="D", s=55, color=P["tinta"], zorder=5)
        ax.text(mid[3], y[3] + 0.32, f"media {mid[3]:.2f}", ha="center", fontsize=7.6,
                color=P["tinta"], fontweight="bold")
    ax.axvline(185.79, color=P["rojo"], lw=2.3, ls="--", zorder=4)
    ax.text(185.79, max(y) + 0.95, "PRECIO HOY\n185,79 US$ (4-sep-2026)",
            ha="center", va="bottom", fontsize=9, color=P["rojo"], fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.2", fc=P["fondo"], ec="none"))
    ax.set_yticks(y); ax.set_yticklabels(filas, fontsize=8.4)
    ax.set_xlim(90, 400); ax.set_xlabel("US$ por acción")
    ax.set_ylim(-0.7, max(y) + 1.3)
    fig.subplots_adjust(top=.80, bottom=.13, left=.235, right=.97)
    deco(ax, "El precio de hoy cae entre el caso BEAR y el caso BASE",
         "Rangos de los tres escenarios del DCF explícito a 10 años (WACC central 7,1%) y del consenso de 19 analistas.",
         "Fuente: dossier de valoración VRSK, Paso 9 (DCF explícito) y S&P Global Market Intelligence, 19-ago-2026.", fig)
    save(fig, "01_rango_valor", OUTDIR)

# ── 02 · El motor de crecimiento: fórmula vs. realidad ──────────────────
def c02():
    fig, ax = plt.subplots(figsize=(11.2, 4.2))
    filas = ["g ingenuo por fórmula\n(reinversión 41% × ROIC ~33%)",
             "g orgánico observado\nFY2021-FY2025 (anual)",
             "valle trimestral\nQ1-Q4 2025 / Q1-2026",
             "rebote Q2-2026\n(un solo trimestre)"]
    lo  = [13, 5.8, 4.7, 5.8]
    hi  = [14, 8.7, 5.2, 5.8]
    cols = [P["terracota"], P["azul"], P["rojo_oscuro"], P["ocre"]]
    y = np.arange(len(filas))[::-1]
    for i, (a, b, c) in enumerate(zip(lo, hi, cols)):
        w = max(b - a, 0.12)
        ax.barh(y[i], w, left=a, height=0.5, color=c, alpha=.85, zorder=3)
        lab = f"{a:.1f}%" if a == b else f"{a:.1f}%–{b:.1f}%"
        ax.text(b + 0.35, y[i], lab, ha="left", va="center", fontsize=9,
                color=c, fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels(filas, fontsize=8.6)
    ax.set_xlim(0, 17); ax.set_xlabel("crecimiento anualizado (%)")
    ax.set_ylim(-0.7, max(y) + 0.9)
    fig.subplots_adjust(top=.78, bottom=.15, left=.30, right=.97)
    deco(ax, "El 13-14% de la fórmula no es lo que le pasa a Verisk",
         "El ROIC agregado (31-37%) está inflado por décadas de activos ya amortizados; el capex de crecimiento real ronda cero en 2024-2025.",
         "Fuente: dossier VRSK, Paso 5 (motor de reinversión), verificado línea por línea contra 10-K FY2021-FY2025 y comunicados de resultados.", fig)
    save(fig, "02_motor_crecimiento", OUTDIR)

# ── 03 · Supuestos del DCF, por escenario ────────────────────────────────
def c03():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.4))
    esc = ["BEAR", "BASE", "BULL"]
    cols = [P["rojo_oscuro"], P["azul"], P["verde"]]
    g_lo = [2, 5, 7]; g_hi = [3, 6, 9]
    for i, (lo, hi, c) in enumerate(zip(g_lo, g_hi, cols)):
        a1.bar(i, hi - lo, bottom=lo, color=c, width=.55, alpha=.88)
        a1.text(i, hi + 0.25, f"{lo}-{hi}%", ha="center", fontsize=9, fontweight="bold", color=c)
    a1.axhline(4.0, color=P["tinta"], lw=1.8, ls="--")
    a1.axhline(3.3, color=P["tinta"], lw=1.8, ls="--")
    a1.fill_between([-0.5, 2.5], 3.3, 4.0, color=P["gris_claro"], alpha=.9, zorder=0)
    a1.text(2.5, 3.65, " implícito en el\n precio de hoy\n (DCF inverso)\n 3,3%-4,0%",
            fontsize=7.2, color=P["gris"], va="center", ha="left", style="italic")
    a1.set_xticks(range(3)); a1.set_xticklabels(esc, fontsize=9, fontweight="bold")
    a1.set_ylabel("crecimiento de ingresos a 10 años (%)"); a1.set_xlim(-0.6, 3.3); a1.set_ylim(0, 11)
    m_lo = [55, 56.5, 60]; m_hi = [55, 59.5, 61]
    for i, (lo, hi, c) in enumerate(zip(m_lo, m_hi, cols)):
        h = max(hi - lo, 0.35)
        a2.bar(i, h, bottom=lo, color=c, width=.55, alpha=.88)
        lab = f"{lo}%" if lo == hi else f"{lo}→{hi}%"
        a2.text(i, hi + 0.35, lab, ha="center", fontsize=9, fontweight="bold", color=c)
    a2.set_xticks(range(3)); a2.set_xticklabels(esc, fontsize=9, fontweight="bold")
    a2.set_ylabel("margen EBITDA terminal (%)"); a2.set_xlim(-0.6, 2.6); a2.set_ylim(50, 65)
    fig.subplots_adjust(top=.74, bottom=.13, left=.08, right=.98, wspace=.28)
    deco([a1, a2], "Lo que cada escenario tiene que ser cierto para pagarse solo",
         "Izquierda: crecimiento de ingresos supuesto a 10 años. Derecha: margen EBITDA terminal. El precio de hoy exige un crecimiento cercano al caso BEAR.",
         "Fuente: dossier VRSK, Paso 9 (DCF explícito a 10 años, WACC central 7,1%, y DCF inverso Rappaport-Mauboussin).", fig)
    save(fig, "03_supuestos_dcf", OUTDIR)

# ── 04 · Construcción del WACC, de abajo hacia arriba ────────────────────
def c04():
    fig, ax = plt.subplots(figsize=(11.2, 4.0))
    filas = ["Beta (5 años, mensual)", "Coste de equity (CAPM)",
             "Coste de deuda después de impuestos", "WACC bottom-up (E/V 84% · D/V 16%)"]
    lo = [0.65, 7.4, 3.3, 6.8]
    hi = [0.70, 7.9, 4.6, 7.4]
    unidad = ["beta", "%", "%", "%"]
    cols = [P["azul_cielo"], P["azul"], P["azul_acero"], P["azul_noche"]]
    y = np.arange(len(filas))[::-1]
    for i, (a, b, c) in enumerate(zip(lo, hi, cols)):
        ax.barh(y[i], b - a, left=a, height=0.5, color=c, alpha=.88, zorder=3)
        u = unidad[i]
        suf = "" if u == "beta" else "%"
        lab = f"{a:.2f}{suf}–{b:.2f}{suf}" if u == "beta" else f"{a:.1f}%–{b:.1f}%"
        ax.text(b + 0.05 * (max(hi) - min(lo)) / 8, y[i], lab, ha="left", va="center",
                fontsize=9, color=c, fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels(filas, fontsize=8.8)
    ax.set_xlim(0, 9.5); ax.set_xlabel("rango (beta en la fila 1; % en las demás)")
    ax.set_ylim(-0.7, max(y) + 0.9)
    fig.subplots_adjust(top=.78, bottom=.15, left=.34, right=.97)
    deco(ax, "Un WACC cruzado por tres fuentes, no adoptado de un tier",
         "Beta 0,66 en dos fuentes independientes (Yahoo Finance y S&P Global); WACC final 7,0-7,1% central, casi idéntico al 7,14% de stockanalysis.com.",
         "Fuente: dossier VRSK, Paso 9 (Candado B: WACC siempre bottom-up de mercado). UST 10a ≈4,76-4,78% (3/4-sep-2026); ERP 4,0-4,5% (Damodaran, 2026).", fig)
    save(fig, "04_wacc_build", OUTDIR)

# ── 05 · Comparación con pares ───────────────────────────────────────────
def c05():
    fig, axs = plt.subplots(2, 2, figsize=(11.2, 7.4))
    tick = ["VRSK", "MCO", "SPGI", "CSGP*"]
    cols = [P["rojo"], P["azul"], P["azul_acero"], P["gris_medio"]]

    def bars(ax, vals, ttl, fmt="{:.1f}%"):
        vmax, vmin = max(vals), min(vals)
        pad = max(abs(vmax), abs(vmin)) * 0.20
        top = vmax + pad if vmax > 0 else pad
        bot = vmin - pad if vmin < 0 else 0
        b = ax.bar(range(4), vals, color=cols, width=.6, zorder=3)
        for i, v in enumerate(vals):
            ax.text(i, v + (pad * 0.28 if v >= 0 else -pad * 0.28),
                    fmt.format(v), ha="center", va="bottom" if v >= 0 else "top",
                    fontsize=8.6, fontweight="bold", color=cols[i])
        ax.set_xticks(range(4)); ax.set_xticklabels(tick, fontsize=8.8, fontweight="bold")
        ax.set_ylim(bot, top)
        ax.set_title(ttl, fontsize=9, color=P["gris"], style="italic", loc="left")
        ax.axhline(0, color=P["gris_linea"], lw=0.8)

    bars(axs[0, 0], [-34.7, -4.4, -20.6, -66.4], "Variación de cap. bursátil vs. FY2025")
    bars(axs[0, 1], [5.5, 11.7, 9.7, 22.0], "Crecimiento de ingresos TTM (VRSK: OCC ~5-6%)")
    bars(axs[1, 0], [18.6, 22.6, 17.5, 31.5], "EV/EBITDA", fmt="{:.1f}x")
    bars(axs[1, 1], [5.1, 3.5, 4.3, 1.8], "FCF yield")
    fig.subplots_adjust(top=.83, bottom=.07, left=.07, right=.97, hspace=.42, wspace=.22)
    deco(list(axs.flat), "El más barato del cluster porque fue el que más cayó",
         "* CSGP en fase de inversión agresiva (Homes.com): comparación de calidad de negocio poco limpia. Datos a sep-2026.",
         "Fuente: dossier VRSK, Paso 9 (tabla de pares) — no es un ranking de candidatas, es contexto de valoración (Candado C).", fig)
    save(fig, "05_pares", OUTDIR)

if __name__ == "__main__":
    for f in (c01, c02, c03, c04, c05):
        f()
    print("Gráficos VRSK generados en", OUTDIR)
