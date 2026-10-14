# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis TRI, método de 12 pasos (2026-09-04).
Todos los datos vienen literalmente del dossier fuente
2026-09-04_UltraTesis_TRI_metodo12_borrador.md — cero cifras inventadas o recalculadas."""
import numpy as np, matplotlib.pyplot as plt
from chart_style import deco, save, P
from matplotlib.patches import Rectangle

# ── 01 · El valor intrínseco antes y después del Paso 10 ─────────────────
def c01():
    fig, ax = plt.subplots(figsize=(11.2, 4.9))
    # (y, x0, x1, color, label, open_ended)
    filas = [
        (0, 140, 150, P["azul_cielo"], "Caso base ORIGINAL (Paso 9.8)\nWACC punto medio ~7,25-7,5%"),
        (1, 115, 120, P["azul"],       "Caso base RECALCULADO (Paso 10)\nWACC escrutado ~8,5%"),
        (2, 103, 106, P["tinta"],      "PRECIO DE HOY\n(sept-2026)"),
        (3, 60,  65,  P["terracota"],  "Caso bajista ORIGINAL (Paso 9.8)\nWACC 10%, decaimiento uniforme"),
    ]
    for y, x0, x1, col, lab in filas:
        ax.barh([y], [x1-x0], left=[x0], height=.52, color=col, zorder=3)
        ax.text((x0+x1)/2, y, f"{x0}-{x1}", ha="center", va="center", fontsize=9.2,
                fontweight="bold", color="white" if col != P["tinta"] else "white", zorder=4)
    # Fila 4: caso bajista recalculado, abierto hacia la izquierda (sin cifra nueva)
    ax.barh([4], [65-60], left=[60], height=.52, color=P["rojo_oscuro"], alpha=.55, zorder=3,
            hatch="////", edgecolor=P["rojo_oscuro"])
    ax.annotate("", xy=(44, 4), xytext=(59, 4),
                arrowprops=dict(arrowstyle="-|>", color=P["rojo_oscuro"], lw=2.2))
    ax.text(41.5, 4, "peor —\nsin cifra\nnueva", ha="right", va="center", fontsize=7.6,
            color=P["rojo_oscuro"], fontweight="bold")
    etiquetas = [lab for _, _, _, _, lab in filas] + \
        ["Caso bajista RECALCULADO (Paso 10)\nriesgo discontinuo, dirección no cuantificada"]
    ax.set_yticks([0, 1, 2, 3, 4])
    ax.set_yticklabels(etiquetas, fontsize=8.0)
    ax.set_xlim(20, 165)
    ax.set_xlabel("valor por acción (US$)")
    ax.axvline(104.5, color=P["tinta"], lw=1.1, ls=":", zorder=2)
    fig.subplots_adjust(top=.72, bottom=.13, left=.30, right=.97)
    deco(ax, "El Paso 10 no rompe la tesis: la encoge por los dos lados",
         "Mismo modelo, mismo dossier — sólo cambia qué WACC del propio rango bottom-up se usa como caso base.",
         "Fuente: Paso 9.4, Paso 9.8 y Paso 10 (Golpe 3) del dossier TRI, método de 12 pasos, 2026-09-04.", fig)
    save(fig, "01_valor_intrinseco")

# ── 02 · Trayectoria de supuestos del DCF a 10 años ───────────────────────
def c02():
    anos = np.arange(1, 11)
    crecimiento = np.linspace(8.0, 3.5, 10)
    margen = np.linspace(27.2, 29.0, 10)
    fig, ax = plt.subplots(figsize=(11.2, 4.6)); ax2 = ax.twinx()
    ax.plot(anos, crecimiento, "-o", color=P["azul"], lw=2.4, ms=6, label="Crecimiento de ingresos supuesto (%)")
    ax2.plot(anos, margen, "-s", color=P["verde"], lw=2.4, ms=6, label="Margen operativo supuesto (%)")
    ax.text(1, 8.35, "8,0%", ha="center", fontsize=8.6, color=P["azul"], fontweight="bold")
    ax.text(10, 3.15, "3,5%", ha="center", fontsize=8.6, color=P["azul"], fontweight="bold")
    ax2.text(1, 26.85, "27,2%", ha="center", fontsize=8.6, color=P["verde"], fontweight="bold")
    ax2.text(10, 29.35, "29,0%", ha="center", fontsize=8.6, color=P["verde"], fontweight="bold")
    ax.axvspan(6, 10, color=P["ocre"], alpha=.14)
    ax.text(8, 8.35, "años 6-10: sin explicar qué\nreemplaza la pista de M&A\n(agotada ~2028) — Golpe 2", ha="center",
            fontsize=7.4, color="#8a6508", fontweight="bold")
    ax.set_xlabel("año del DCF"); ax.set_ylabel("crecimiento de ingresos (%)", color=P["azul"])
    ax2.set_ylabel("margen operativo (%)", color=P["verde"])
    ax.set_ylim(3, 9); ax2.set_ylim(26.5, 29.8); ax.set_xticks(anos)
    ax2.grid(False)
    fig.subplots_adjust(top=.74, bottom=.13, left=.08, right=.90)
    deco([ax], "El DCF usa una desaceleración suave, no la g de 11-15% del Paso 5",
         "Trayectoria ilustrativa interpolada entre los dos extremos declarados (Paso 9.4): el dossier no publica cifras año a año.",
         "Fuente: Paso 9.4 del dossier TRI (marcador de posición razonable, no resultado definitivo), 2026-09-04.", fig)
    save(fig, "02_dcf_trayectoria")

# ── 03 · Sensibilidad del valor a un solo WACC (g terminal fijo en 3,0%) ──
def c03():
    fig, ax = plt.subplots(figsize=(11.2, 4.7))
    wacc = [6.0, 7.25, 8.5]
    lo   = [220, 150, 115]
    hi   = [220, 155, 120]
    mid  = [(a+b)/2 for a, b in zip(lo, hi)]
    for w, l, h in zip(wacc, lo, hi):
        if l != h:
            ax.plot([w, w], [l, h], color=P["azul"], lw=7, solid_capstyle="round", alpha=.45, zorder=2)
    ax.plot(wacc, mid, "-o", color=P["azul"], lw=2.2, ms=9, zorder=5)
    etiquetas_val = ["US$ 220", "US$ 150-155", "US$ 115-120"]
    for w, m, et in zip(wacc, mid, etiquetas_val):
        ax.text(w, m+10, et, ha="center", fontsize=10, fontweight="bold", color=P["azul_noche"])
    etiquetas_w = ["~6,0%\n(mecánico,\nbeta 0,17-0,33)", "~7,25%\n(punto medio,\ncaso base ORIGINAL)",
                   "~8,5%\n(escrutado,\ncaso base RECALCULADO)"]
    for w, et in zip(wacc, etiquetas_w):
        ax.text(w, 92, et, ha="center", fontsize=7.6, color=P["gris"])
    ax.axhspan(103, 106, color=P["ocre"], alpha=.20, zorder=1)
    ax.text(5.62, 114.5, "PRECIO DE HOY  US$103-106", fontsize=8.6, color="#8a6508", fontweight="bold",
            va="bottom", ha="left")
    ax.set_xlabel("WACC usado en el DCF (%)"); ax.set_ylabel("valor por acción (US$)")
    ax.set_xlim(5.5, 9.2); ax.set_ylim(88, 240)
    fig.subplots_adjust(top=.74, bottom=.15, left=.075, right=.97)
    deco(ax, "Un solo parámetro mueve el valor de 220 a 115 dólares",
         "Sensibilidad a WACC con crecimiento terminal fijo en 3,0% — el único que el dossier calcula; no hay grilla WACC×g en la fuente.",
         "Fuente: Paso 9.4 del dossier TRI, tabla de sensibilidad, 2026-09-04.", fig)
    save(fig, "03_sensibilidad_wacc")

# ── 04 · Múltiplos frente a los pares citados (contexto, no ranking) ──────
def c04():
    nom = ["Wolters Kluwer", "RELX", "TRI", "LSEG"]
    ev  = [7.8, 15.68, 16.5, 16.83]  # TRI: "~16,5-17x, estimación propia" -> usamos extremo inferior 16.5 con barra hasta 17
    ev_hi = [7.8, 15.68, 17.0, 16.83]
    crec = ["Orgánico +5%\n(1S-26)", "Underlying +7%\n(FY25)", "Big3 orgánico\n+10% (2T-26)", "Orgánico +8,4%\n(1S-26, récord)"]
    cols = [P["azul_acero"], P["azul_acero"], P["rojo"], P["azul_acero"]]
    x = np.arange(4)
    fig, ax = plt.subplots(figsize=(11.2, 4.7))
    for i in range(4):
        if ev[i] != ev_hi[i]:
            ax.bar(x[i], ev_hi[i], color=cols[i], width=.52, alpha=.35, zorder=2)
        ax.bar(x[i], ev[i], color=cols[i], width=.52, zorder=3)
        etiqueta_val = f"{ev[i]:.2f}x".replace(".", ",") if ev[i] == ev_hi[i] else f"{ev[i]:.1f}-{ev_hi[i]:.1f}x".replace(".", ",")
        ax.text(x[i], ev_hi[i]+.5, etiqueta_val, ha="center", fontsize=10, fontweight="bold", color=P["azul_noche"])
        ax.text(x[i], -2.6, crec[i], ha="center", fontsize=7.6, color=P["gris"])
    ax.text(3.85, 5.5, "Clarivate: ingresos −5,5% (2T-26),\nEV/EBITDA n/d — el peer roto\nde este universo", fontsize=7.2,
            color=P["rojo_oscuro"], ha="right", style="italic")
    ax.set_xticks(x); ax.set_xticklabels(nom, fontsize=9.2)
    ax.set_ylabel("EV/EBITDA (veces)"); ax.set_ylim(-4.5, 20)
    fig.subplots_adjust(top=.76, bottom=.20, left=.08)
    deco(ax, "TRI no cotiza barata frente a su comparable más sano",
         "En múltiplos relativos no hay descuento — el «gran margen de seguridad» vive sólo dentro del DCF de WACC bajo (Paso 9.7).",
         "Fuente: Paso 9.7 del dossier TRI — comunicados de resultados de cada emisor, jul-ago-2026. Comparación de contexto, nunca ranking (Candado C).", fig)
    save(fig, "04_multiplos_pares")

# ── 05 · El motor de reinversión se diluye ────────────────────────────────
def c05():
    anos = ["2023", "2024", "2025"]
    ratio = [94, 88, 76]
    roic  = [15.8, 14.9, 14.5]
    x = np.arange(3)
    fig, ax = plt.subplots(figsize=(11.2, 4.6)); ax2 = ax.twinx()
    ax.bar(x, ratio, color=P["azul_cielo"], width=.5, zorder=3, label="(Capex+M&A) / FCF")
    ax2.plot(x, roic, "-o", color=P["rojo"], lw=2.6, ms=9, zorder=5, label="ROIC total (proxy)")
    for i in range(3):
        ax.text(x[i], ratio[i]+2.5, f"{ratio[i]}%", ha="center", fontsize=9.4, fontweight="bold", color=P["azul_noche"])
        ax2.text(x[i], roic[i]+0.35, f"{roic[i]}%".replace(".", ","), ha="center", fontsize=9.4, fontweight="bold", color=P["rojo"])
    ax.set_xticks(x); ax.set_xticklabels(anos, fontsize=9.4)
    ax.set_ylabel("(Capex + M&A) / FCF"); ax2.set_ylabel("ROIC total, proxy (%)", color=P["rojo"])
    ax.set_ylim(0, 110); ax2.set_ylim(13, 17.5)
    ax2.grid(False)
    fig.subplots_adjust(top=.74, bottom=.12, left=.08, right=.90)
    deco([ax], "Reinvierte cada vez menos, y con retorno cada vez más bajo",
         "La propia empresa atribuye la caída de ROIC “principalmente al impacto de adquisiciones” (D25, Apéndice D, p.82).",
         "Fuente: Paso 5 del dossier TRI — 40-F FY2023/FY2025, capex y M&A cash pagado.", fig)
    save(fig, "05_motor_reinversion")

# ── 06 · El susto que un beta de 0,20 no explica ──────────────────────────
def c06():
    fig, ax = plt.subplots(figsize=(11.2, 4.7))
    ax.bar([0], [218], color=P["azul"], width=.45, zorder=3)
    ax.bar([1], [104.5], color=P["rojo_oscuro"], width=.45, zorder=3)
    ax.text(0, 222, "US$ 218", ha="center", fontsize=12, fontweight="bold", color=P["azul"])
    ax.text(1, 108.5, "US$ 103-106", ha="center", fontsize=12, fontweight="bold", color=P["rojo_oscuro"])
    ax.annotate("", xy=(1, 150), xytext=(0, 150), arrowprops=dict(arrowstyle="-|>", color=P["tinta"], lw=1.6))
    ax.text(0.5, 156, "-52% / -53% desde el pico\n-27% en lo que va de 2026", ha="center", fontsize=9.2,
            fontweight="bold", color=P["tinta"])
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Pico\njul-2025", "Hoy\nsept-2026"], fontsize=9.6)
    ax.set_ylabel("precio por acción (US$)"); ax.set_ylim(0, 250)
    ax.text(1.62, 60, "1-feb-2026: peor caída diaria\ncomo empresa pública, -15,83%\n(Barchart). Prensa cruzada sitúa\nel lanzamiento de plugins legales\nde Anthropic en torno al\n3-feb-2026, con TRI cayendo\nentre -15,8% y -18% intradía\nen esa ventana\n\nDías después: +14% en una\nsesión, cuando Anthropic elogió\npúblicamente el producto",
            fontsize=7.6, color=P["gris"], va="center",
            bbox=dict(boxstyle="round,pad=0.4", fc=P["panel"], ec=P["gris_linea"]))
    fig.subplots_adjust(top=.76, bottom=.13, left=.08, right=.62)
    deco(ax, "Una beta de 0,17-0,33 no puede generar este movimiento",
         "El riesgo dominante de esta tesis es un evento de sustitución tecnológica idiosincrático, no covarianza con el mercado.",
         "Fuente: Paso 3 y Paso 9.2 del dossier TRI — Barchart 2026, Seeking Alpha feb-2026, cobertura de prensa cruzada.", fig)
    save(fig, "06_precio_shock")

for f in [c01, c02, c03, c04, c05, c06]:
    f(); print("ok", f.__name__)
