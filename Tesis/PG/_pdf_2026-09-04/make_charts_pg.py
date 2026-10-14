# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis PG. Todos los datos tomados literalmente del
borrador método-12 (2026-09-04); ningún número se recalcula aquí."""
import numpy as np, matplotlib.pyplot as plt
from chart_style import deco, save, P
from matplotlib.patches import Rectangle

PRECIO_LO, PRECIO_HI = 146.44, 146.70
PRECIO_MID = (PRECIO_LO + PRECIO_HI) / 2

# ── 01 · El motor de reinversión: reinvierte 23 veces más, crece menos ──
def c01():
    years = [2021, 2022, 2023, 2024, 2025, 2026]
    reinv = [0.35, 2.38, 2.39, 2.88, 5.68, 7.98]
    roic  = [21.0, 21.0, 20.0, 20.0, 21.0, 21.5]
    gder  = [0.07, 0.50, 0.48, 0.58, 1.19, 1.72]
    organ = [None, None, 7.0, 4.0, 2.0, 1.0]

    fig, ax = plt.subplots(figsize=(11.2, 4.8))
    ax2 = ax.twinx()
    x = np.arange(6)
    ax.bar(x, reinv, color=P["azul_cielo"], width=.5, label="Tasa de reinversión (Capex−D&A / NOPAT)", zorder=2)
    for i, v in enumerate(reinv):
        ax.text(i, v + .22, f"{v:.2f}".replace(".", ",") + "%", ha="center", fontsize=7.6,
                color=P["azul_noche"], fontweight="bold")
    ax.plot(x, gder, "-o", color=P["azul"], lw=2.4, ms=6, zorder=4, label="g derivado (reinversión × ROIC)")
    xo = [i for i, v in enumerate(organ) if v is not None]
    yo = [v for v in organ if v is not None]
    ax.plot(xo, yo, "--s", color=P["rojo"], lw=2.2, ms=6.5, zorder=4, label="Crecimiento orgánico reportado (8-K)")
    for i, v in zip(xo, yo):
        ax.text(i, v + .35, f"+{v:.0f}%", ha="center", fontsize=8.2, color=P["rojo"], fontweight="bold")
    ax2.plot(x, roic, ":D", color=P["gris_medio"], lw=1.8, ms=5, zorder=3, label="ROIC (eje derecho)")
    ax.annotate("convergen en\nFY2026: ~1,7%",
                (5, 1.72), (4.05, 4.6), fontsize=8.2, color=P["azul_noche"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=P["azul_noche"], lw=1.2))
    ax.set_xticks(x); ax.set_xticklabels([f"FY{y}" for y in years], fontsize=8.6)
    ax.set_ylabel("tasa de reinversión / g / crecimiento orgánico (%)"); ax.set_ylim(-0.3, 9.2)
    ax2.set_ylabel("ROIC (%)", color=P["gris_medio"]); ax2.set_ylim(0, 30)
    ax2.grid(False)
    for s in ["top", "left"]: ax2.spines[s].set_visible(False)
    h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7.6, loc="upper left")
    fig.subplots_adjust(top=.75, bottom=.12, left=.075, right=.925)
    deco(ax, "Reinvierte 23 veces más y crece menos: el ROIC no sube, solo el capital",
         "La tasa de reinversión sube monótonamente 6 años seguidos; el ROIC se mantiene plano ~20-21%; el crecimiento reportado cae hasta encontrarse con el g del motor.",
         "Fuente: 10-K FY2021-FY2026 (NOPAT, Capex, D&A, ROIC), 8-K trimestrales (crecimiento orgánico no-GAAP). Elaboración propia, Paso 5 del método.", fig)
    save(fig, "01_motor_reinversion")

# ── 02 · La palanca de precio se apagó ──────────────────────────────────
def c02():
    years = [2023, 2024, 2025, 2026]
    precio = [9, 4, 1, 0]
    organico = [7, 4, 2, 1]
    x = np.arange(4); w = .34
    fig, ax = plt.subplots(figsize=(11.2, 4.4))
    ax.bar(x - w/2, precio, w, color=P["rojo"], label="Contribución del PRECIO (puntos)")
    ax.bar(x + w/2, organico, w, color=P["azul"], label="Crecimiento orgánico TOTAL reportado (puntos)")
    for i in range(4):
        ax.text(x[i]-w/2, precio[i]+.18, f"+{precio[i]}", ha="center", fontsize=9, fontweight="bold", color=P["rojo"])
        ax.text(x[i]+w/2, organico[i]+.18, f"+{organico[i]}", ha="center", fontsize=9, fontweight="bold", color=P["azul"])
    ax.axhline(0, color=P["tinta"], lw=.9)
    ax.set_xticks(x); ax.set_xticklabels([f"FY{y}" for y in years], fontsize=9)
    ax.set_ylabel("puntos porcentuales"); ax.set_ylim(-0.6, 10.5)
    ax.legend(frameon=False, fontsize=8.6, loc="upper right")
    ax.annotate("las tres palancas\n(volumen/precio/mix)\nllegan a cero en Q4",
                (3, 0), (2.15, 6.6), fontsize=8.2, color=P["gris"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=P["gris_medio"], lw=1.1))
    fig.subplots_adjust(top=.75, bottom=.12, left=.075)
    deco(ax, "Casi todo el crecimiento de tres años vino de subir precio, y esa palanca ya llegó a cero",
         "Contribución de precio vs. crecimiento orgánico total, por año fiscal. FY2023-FY2025 crecieron casi enteramente por precio, no por volumen.",
         "Fuente: comunicados de resultados (8-K) y transcripciones de la llamada de resultados de P&G, FY2023-FY2026.", fig)
    save(fig, "02_precio_apagado")

# ── 03 · Rango de valor frente al precio de hoy ──────────────────────────
def c03():
    fig, ax = plt.subplots(figsize=(11.2, 5.0))
    bandas = [
        ("Zona de entrada\nrevisada (Paso 11)",            80,  100, P["verde"]),
        ("Caso base corregido\n(Paso 10.2, g del motor)",  105, 115, P["azul"]),
        ("«Base» original con g de\nguía — YA NO VIGENTE",  135, 140, P["gris_medio"]),
        ("Requerido para justificar\nel precio de hoy (g≈4%)", 146, 147, P["vino"]),
        ("Optimista (retorno a\ncrecimiento equilibrado)",  150, 157, P["terracota"]),
    ]
    for i, (lab, lo, hi, col) in enumerate(bandas):
        ax.barh(i, hi - lo, left=lo, color=col, height=.55, zorder=3)
        ancho = hi - lo
        if ancho >= 8:
            ax.text((lo+hi)/2, i, f"{lo:.0f}-{hi:.0f} US$", ha="center", va="center",
                    fontsize=8.6, fontweight="bold", color="white")
        else:
            ax.text((lo+hi)/2, i - 0.62, f"{lo:.0f}-{hi:.0f} US$", ha="center", va="center",
                    fontsize=8.6, fontweight="bold", color=col)
    ax.axvline(PRECIO_MID, color=P["rojo"], lw=2.4, ls="--", zorder=2)
    ax.text(PRECIO_MID + 2.2, -0.85, f"PRECIO HOY\n{PRECIO_LO:.2f}-{PRECIO_HI:.2f} US$",
            ha="left", va="center", fontsize=9, fontweight="bold", color=P["rojo"])
    ax.set_yticks(range(len(bandas))); ax.set_yticklabels([b[0] for b in bandas], fontsize=8.6)
    ax.set_xlim(70, 172); ax.set_ylim(-1.2, len(bandas)-0.4)
    ax.set_xlabel("dólares por acción")
    ax.invert_yaxis()
    fig.subplots_adjust(top=.72, bottom=.12, left=.235, right=.97)
    deco(ax, "El precio de hoy calza exactamente con «lo que hay que creer», no con lo que el motor sostiene",
         "El precio actual está pegado al escenario que exige ~4% de crecimiento sostenido — un número que ninguna fuente primaria respalda hoy.",
         "Fuente: Paso 9.2 (DCF explícito) y Paso 10.2 (adjudicación del abogado-diablo) del método-12, borrador 2026-09-04.", fig)
    save(fig, "03_valor_vs_precio")

# ── 04 · Un mismo WACC, dos valores muy distintos: lo que mueve el precio es g ──
def c04():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    esc = ["Pesimista\nWACC 7,5% · g 1,5%", "Base original\nWACC 7,0% · g 2,5%",
           "Requerido p/ precio hoy\nWACC 7,5% · g≈4,0%", "Optimista\nWACC 6,5% · g 3,0-3,5%"]
    lo  = [100, 135, 146, 150]
    hi  = [105, 140, 147, 157]
    mid = [(a+b)/2 for a, b in zip(lo, hi)]
    cols = [P["rojo_oscuro"], P["gris_medio"], P["vino"], P["verde"]]
    x = np.arange(4)
    for i in range(4):
        ax.bar(i, hi[i]-lo[i], bottom=lo[i], color=cols[i], width=.55, zorder=3)
        ax.text(i, hi[i]+3, f"{lo[i]}-{hi[i]} US$", ha="center", fontsize=9.4, fontweight="bold", color=cols[i])
    ax.axhline(PRECIO_MID, color=P["rojo"], lw=2.0, ls="--", zorder=4)
    ax.text(3.55, PRECIO_MID+3, "PRECIO HOY 146,57 US$", fontsize=8.2, color=P["rojo"], fontweight="bold", ha="right")
    ax.set_xticks(x); ax.set_xticklabels(esc, fontsize=8.0); ax.set_ylim(85, 172)
    ax.set_ylabel("valor por acción (US$)")
    ax.annotate("mismo WACC (7,5%),\nvalor casi 45 US$ más alto\nsolo por cambiar g",
                (0.5, 130), (0.15, 155), fontsize=8.0, color=P["azul_noche"], fontweight="bold")
    fig.subplots_adjust(top=.76, bottom=.15, left=.075)
    deco(ax, "El WACC apenas se mueve (6,5%-7,5%); el valor se mueve porque cambia el crecimiento supuesto",
         "Las columnas 1 y 3 comparten casi el mismo WACC (7,5%) y difieren en 41-42 US$ únicamente por el supuesto de g.",
         "Fuente: tabla del Paso 9.2 (DCF explícito a 10 años), borrador método-12 PG, 2026-09-04. Sin recálculo: las cuatro filas ya existían en el dossier.", fig)
    save(fig, "04_sensibilidad_wacc_g")

# ── 05 · PG contra sus pares nombrados ───────────────────────────────────
def c05():
    empresas = ["P&G", "Unilever", "Colgate", "Kimberly-\nClark*", "Church &\nDwight"]
    pe   = [22.2, 13.1, 35.0, 20.8, 31.7]
    roic = [21.5, 15.8, 45.6, 25.4, 14.0]
    cre  = [1.0, 1.9, 5.2, 0.7, 2.7]
    dy   = [2.98, 3.43, 2.39, 4.88, 1.25]
    cols = [P["rojo"], P["gris_medio"], P["gris_medio"], P["gris_medio"], P["gris_medio"]]

    fig, axs = plt.subplots(2, 2, figsize=(11.2, 7.6))
    datasets = [(axs[0,0], pe,   "P/E trailing (veces)", "{:.1f}x"),
                (axs[0,1], roic, "ROIC (%)",              "{:.1f}%"),
                (axs[1,0], cre,  "Crecimiento orgánico reciente (%)", "+{:.1f}%"),
                (axs[1,1], dy,   "Dividend yield (%)",    "{:.2f}%")]
    for ax, vals, tit, fmt in datasets:
        ax.bar(range(5), vals, color=cols, width=.6)
        for i, v in enumerate(vals):
            ax.text(i, v + max(vals)*.03, fmt.format(v), ha="center", fontsize=8.0, fontweight="bold",
                    color=cols[i] if cols[i] != P["rojo"] else P["rojo"])
        ax.set_xticks(range(5)); ax.set_xticklabels(empresas, fontsize=7.6)
        ax.set_title(tit, fontsize=9.4, fontweight="bold", color=P["azul_noche"], pad=6)
        ax.set_ylim(0, max(vals)*1.22)
    fig.subplots_adjust(top=.80, bottom=.08, hspace=.55, wspace=.22, left=.075, right=.975)
    deco(list(axs.flat), "Segundo mejor ROIC del grupo, pero el crecimiento más lento de todos",
         "PG paga prima de calidad (ROIC, balance) mientras entrega hoy la métrica de crecimiento más débil del set de pares nombrado.",
         "Fuente: Paso 9.5 del borrador método-12 PG (2026-09-04). *Kimberly-Clark en transformación (adquisición Kenvue, 8-K 3-nov-2025): múltiplos probablemente incorporan descuento de integración.", fig, flag_y=.965)
    save(fig, "05_comparacion_pares")

if __name__ == "__main__":
    c01(); c02(); c03(); c04(); c05()
    print("Listo: 5 gráficos generados en charts/")
