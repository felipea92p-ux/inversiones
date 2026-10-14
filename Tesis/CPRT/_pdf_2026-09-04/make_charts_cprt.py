# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis CPRT v1. Todos los datos verificados en el documento
fuente (2026-09-04_UltraTesis_CPRT_metodo12_borrador.md), a su vez trazable a
10-K FY2021-25 (EDGAR CIK 0000900075), DEF 14A 2025-10-24, 10-Q filed 2026-05-29
y 2026-08-04, y comunicados 8-K de RB Global / Ritchie Bros."""
import numpy as np, matplotlib.pyplot as plt
from chart_style import deco, save, P

# ── 01 · Rango de valor intrínseco vs. precio actual ────────────────────
def c01():
    cat = ["BAJISTA\npropio", "BASE PROPIO\n(DCF variable)", "BASE RÉPLICA\nfuente (7,4% flat)", "ALCISTA\npropio"]
    centro = [21.5, 30.0, 33.4, 39.7]
    lo = [None, 28.8, 32.0, None]
    hi = [None, 31.5, 35.0, None]
    cols = [P["rojo_oscuro"], P["azul"], P["azul_acero"], P["verde"]]
    x = np.arange(4)
    fig, ax = plt.subplots(figsize=(11.2, 5.0))
    ax.bar(x, centro, color=cols, width=0.56, zorder=3)
    for i in range(4):
        if lo[i] is not None:
            ax.plot([x[i], x[i]], [lo[i], hi[i]], color=P["tinta"], lw=1.6, zorder=4)
            ax.plot([x[i]-0.09, x[i]+0.09], [lo[i], lo[i]], color=P["tinta"], lw=1.6, zorder=4)
            ax.plot([x[i]-0.09, x[i]+0.09], [hi[i], hi[i]], color=P["tinta"], lw=1.6, zorder=4)
        ax.text(x[i], centro[i]+1.3, f"{centro[i]:.1f}".replace(".", ",") + " US$",
                ha="center", fontsize=11, fontweight="bold", color=cols[i])
    notas = ["g 2% · WACC 10,0%\nterminal 2,5%", "g 3%→6-7,5%→5%\nCAGR 5,8%",
             "g 7,4% flat\nWACC bottom-up", "g 8,5% · WACC 9,4%\nterminal 4,0%"]
    for i in range(4):
        ax.text(x[i], 2.3, notas[i], ha="center", fontsize=7.2, color="white", style="italic")
    ax.axhline(33.86, color=P["rojo"], lw=2.2, ls="--", zorder=5)
    ax.text(3.44, 34.6, "PRECIO HOY\n33,86 US$", fontsize=9, color=P["rojo"], fontweight="bold", ha="right")
    ax.set_xticks(x); ax.set_xticklabels(cat, fontsize=8.6)
    ax.set_ylabel("valor intrínseco por acción (US$)"); ax.set_ylim(0, 45); ax.set_xlim(-0.65, 3.85)
    fig.subplots_adjust(top=0.76, bottom=0.13, left=0.075, right=0.97)
    deco(ax, "Ningún caso central deja margen de seguridad real",
         "El caso base que replica el 7,4% del documento fuente con WACC bottom-up cae prácticamente sobre el precio de hoy; el caso base propio queda por debajo.",
         "Fuente: Paso 9 del documento fuente (DCF explícito e inverso, WACC bottom-up 9,4%-10,0%) y objeción 3a del Paso 10 sobre el caso bajista.", fig)
    save(fig, "01_valor_intrinseco")

# ── 02 · Compresión de margen: consolidado y por segmento ───────────────
def c02():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.6))
    # Panel 1: consolidado FY2021 vs FY2025
    yrs1 = ["FY2021", "FY2025"]
    cons = [42.2, 36.5]
    a1.bar(range(2), cons, color=[P["azul_cielo"], P["rojo_oscuro"]], width=0.5)
    for i, v in enumerate(cons):
        a1.text(i, v+0.8, f"{v:.1f}".replace(".", ",")+"%", ha="center", fontsize=11, fontweight="bold",
                color=P["azul_noche"] if i == 0 else P["rojo_oscuro"])
    a1.text(0.5, 44.5, "−570 pb en 4 años", ha="center", fontsize=8.6, color=P["rojo_oscuro"], fontweight="bold")
    a1.set_xticks(range(2)); a1.set_xticklabels(yrs1, fontsize=9)
    a1.set_ylabel("margen operativo consolidado (%)"); a1.set_ylim(0, 48)
    a1.set_title("Consolidado (4 años)", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)
    # Panel 2: US vs Internacional FY2023 vs FY2025
    yrs2 = ["FY2023", "FY2025"]
    us = [42.9, 38.4]; intl = [17.4, 27.3]
    xw = np.arange(2); w = 0.32
    a2.bar(xw - w/2, us, w, color=P["azul"], label="EE.UU. (núcleo)")
    a2.bar(xw + w/2, intl, w, color=P["verde"], label="Internacional")
    for i in range(2):
        a2.text(xw[i]-w/2, us[i]+0.9, f"{us[i]:.1f}".replace(".", ",")+"%", ha="center", fontsize=8.6, fontweight="bold", color=P["azul"])
        a2.text(xw[i]+w/2, intl[i]+0.9, f"{intl[i]:.1f}".replace(".", ",")+"%", ha="center", fontsize=8.6, fontweight="bold", color=P["verde"])
    a2.set_xticks(xw); a2.set_xticklabels(yrs2, fontsize=9)
    a2.set_ylim(0, 48)
    a2.set_title("Por segmento (2 años)", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)
    a2.legend(frameon=False, fontsize=8.2, loc="upper center")
    fig.subplots_adjust(top=0.74, bottom=0.12, wspace=0.22)
    deco([a1, a2], "El margen se comprime en el negocio central mientras mejora en el internacional",
         "Consolidado: Nota 14 “Segments”, 10-K FY2021-25. La compresión EE.UU. coincide con el ratio Facility Ops/Ingresos subiendo de 40,5% a 42,7% en el mismo período.",
         "Fuente: 10-K FY2021, FY2023 y FY2025 (Nota 14, Segments), CIK 0000900075. El dato intermedio FY2024 (~41,2%) usado por el abogado del diablo no fue verificado en esta síntesis.", fig)
    save(fig, "02_margen_segmentos")

# ── 03 · Trayectoria de crecimiento del DCF explícito propio ─────────────
def c03():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    cat = ["Año 1", "Años intermedios\n(rango)", "Año 10\n(converge)"]
    centro = [3.0, 6.75, 5.0]
    lo = [None, 6.0, None]; hi = [None, 7.5, None]
    x = np.arange(3)
    ax.bar(x, centro, color=[P["azul_cielo"], P["azul"], P["azul_acero"]], width=0.5, zorder=3)
    ax.plot([x[1], x[1]], [lo[1], hi[1]], color=P["tinta"], lw=1.8, zorder=4)
    ax.plot([x[1]-0.08, x[1]+0.08], [lo[1], lo[1]], color=P["tinta"], lw=1.8, zorder=4)
    ax.plot([x[1]-0.08, x[1]+0.08], [hi[1], hi[1]], color=P["tinta"], lw=1.8, zorder=4)
    for i in range(3):
        lab = f"{centro[i]:.1f}".replace(".0", "").replace(".", ",") + "%"
        if i == 1: lab = "6-7,5%"
        ax.text(x[i], centro[i]+0.35, lab, ha="center", fontsize=11, fontweight="bold", color=P["azul_noche"])
    ax.axhline(5.8, color=P["ocre"], lw=2, ls="--")
    ax.text(2.35, 6.05, "CAGR implícito a 10 años: 5,8%", fontsize=8.6, color="#8a6508", fontweight="bold", ha="right")
    ax.axhline(7.4, color=P["rojo"], lw=2, ls="--")
    ax.text(2.35, 7.65, "7,4% del documento fuente (“conservador, no heroico”)", fontsize=8.6, color=P["rojo"], fontweight="bold", ha="right")
    ax.set_xticks(x); ax.set_xticklabels(cat, fontsize=9.2)
    ax.set_ylabel("crecimiento anual de owner earnings (%)"); ax.set_ylim(0, 9)
    fig.subplots_adjust(top=0.76, bottom=0.12, left=0.08)
    deco(ax, "El caso base propio empieza bajo y nunca llega a validar el 7,4%",
         "Arranca en 3% (reflejando el -0,4% interanual de los 9 meses fiscales FY2026), acelera hacia el motor de reinversión y converge a un terminal moderado.",
         "Fuente: Paso 9 del documento fuente, DCF explícito a 10 años sobre owner earnings. El 3,5% de crecimiento a perpetuidad (Gordon) para el valor terminal es un supuesto distinto, no mostrado aquí.", fig)
    save(fig, "03_dcf_trayectoria")

# ── 04 · Copart frente a RB Global (dueña de IAA) ────────────────────────
def c04():
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(11.2, 4.2))
    labs = ["Copart", "RB Global\n(IAA)"]
    ingresos = [4.65, 4.59]
    a1.bar(range(2), ingresos, color=[P["azul"], P["gris_medio"]], width=0.55)
    for i, v in enumerate(ingresos):
        a1.text(i, v+0.08, f"{v:.2f}".replace(".", ",")+" mM", ha="center", fontsize=9, fontweight="bold")
    a1.set_xticks(range(2)); a1.set_xticklabels(labs, fontsize=8.6)
    a1.set_ylabel("ingresos (US$ miles de millones)"); a1.set_ylim(0, 5.6)
    a1.set_title("Escala\n(casi idéntica)", fontsize=9, fontweight="bold", color=P["azul_noche"], pad=6)

    margen = [33, 8.3]
    a2.bar(range(2), margen, color=[P["azul"], P["gris_medio"]], width=0.55)
    for i, v in enumerate(margen):
        a2.text(i, v+0.9, f"{v:.1f}".replace(".", ",")+"%", ha="center", fontsize=9, fontweight="bold")
    a2.set_xticks(range(2)); a2.set_xticklabels(labs, fontsize=8.6)
    a2.set_ylim(0, 40)
    a2.set_title("Margen neto\n(más de 4x)", fontsize=9, fontweight="bold", color=P["azul_noche"], pad=6)

    evfcf = [22.5, 27]
    a3.bar(range(2), evfcf, color=[P["azul"], P["gris_medio"]], width=0.55)
    a3.text(0, evfcf[0]+0.6, "22-23x", ha="center", fontsize=9, fontweight="bold")
    a3.text(1, evfcf[1]+0.6, "~27x", ha="center", fontsize=9, fontweight="bold")
    a3.set_xticks(range(2)); a3.set_xticklabels(labs, fontsize=8.6)
    a3.set_ylim(0, 32)
    a3.set_title("EV/FCF\n(Copart, más barato)", fontsize=9, fontweight="bold", color=P["azul_noche"], pad=6)

    fig.subplots_adjust(top=0.72, bottom=0.13, wspace=0.35)
    deco([a1, a2, a3], "Misma escala, cuatro veces el margen, múltiplo menor",
         "No es un problema de tamaño: con ingresos casi idénticos, Copart convierte muchísimo más en beneficio y cotiza más barato por flujo de caja.",
         "Fuente: 10-Q RB Global 30-jun-2026 (filed 2026-08-04) y cifras propias de Copart, Paso 9 del documento fuente. OPENLANE (ex-KAR) queda fuera por no competir ya en salvage.", fig)
    save(fig, "04_pares")

# ── 05 · El motor de reinversión: cuatro bases, un rango honesto ────────
def c05():
    fig, ax = plt.subplots(figsize=(11.2, 5.0))
    cat = ["Dossier knock-outs\n(proxy “D” solo)", "Corrección adversarial\n(D&A completo, NOPAT)",
           "Dossier valoración\n(D&A completo,\nowner earnings)", "Promedio 5 años FY21-25\n(proxy “D” solo)"]
    centro = [8.6, 7.9, 5.9, 9.3]
    lo = [None, None, 4.4, 6.7]; hi = [None, None, 7.4, 12.4]
    x = np.arange(4)
    ax.axhspan(5, 8, color=P["verde"], alpha=0.14, zorder=1)
    ax.text(-0.55, 5.35, "rango defendible (síntesis honesta): 5%-8%", fontsize=7.8, color="#546b2e", fontweight="bold", ha="left", zorder=6)
    cols = [P["azul_cielo"], P["azul"], P["azul_acero"], P["gris_medio"]]
    ax.bar(x, centro, color=cols, width=0.5, zorder=3)
    for i in range(4):
        if lo[i] is not None:
            ax.plot([x[i], x[i]], [lo[i], hi[i]], color=P["tinta"], lw=1.7, zorder=4)
            ax.plot([x[i]-0.08, x[i]+0.08], [lo[i], lo[i]], color=P["tinta"], lw=1.7, zorder=4)
            ax.plot([x[i]-0.08, x[i]+0.08], [hi[i], hi[i]], color=P["tinta"], lw=1.7, zorder=4)
        lab = f"{lo[i]:.1f}-{hi[i]:.1f}".replace(".", ",") if lo[i] is not None else f"{centro[i]:.1f}".replace(".", ",") + "%"
        ax.text(x[i], (hi[i] if hi[i] is not None else centro[i]) + 0.65, lab, ha="center", fontsize=9.4, fontweight="bold", color=P["azul_noche"])
    ax.axhline(7.4, color=P["rojo"], lw=2, ls="--", zorder=5)
    ax.text(1.15, 9.15, "7,4% citado como “conservador, no heroico” — cae en la mitad-alta del rango, no en el centro",
            fontsize=7.9, color=P["rojo"], fontweight="bold", ha="left")
    ax.set_xticks(x); ax.set_xticklabels(cat, fontsize=7.9)
    ax.set_ylabel("g resultante = tasa de reinversión × ROIC incremental (%)")
    ax.set_ylim(0, 15); ax.set_xlim(-0.6, 3.6)
    fig.subplots_adjust(top=0.76, bottom=0.15, left=0.08, right=0.97)
    deco(ax, "Cuatro formas de medir el motor, un rango que no es tan cómodo como parece",
         "Con la corrección de D&A completo incorporada, el crecimiento sostenible defendible cae en 5%-8% — y el 7,4% citado vive en el extremo alto, no en el medio.",
         "Fuente: Paso 5 del documento fuente, tabla de tasa de reinversión × ROIC incremental sobre 10-K FY2021-25. ROIC incremental de 15%-25% es SUPUESTO explícito, no dato observado.", fig)
    save(fig, "05_motor_reinversion")

for f in [c01, c02, c03, c04, c05]:
    f(); print("ok", f.__name__)
