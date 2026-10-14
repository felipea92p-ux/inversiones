# -*- coding: utf-8 -*-
"""Gráficos MA — datos literales del dossier fuente 2026-09-04_UltraTesis_MA_metodo12_borrador.md
Ningún número aquí está inventado ni recalculado: son citas directas del Paso 5 y del Paso 9."""
import numpy as np
import matplotlib.pyplot as plt
import chart_style as cs
from paleta_qg import PALETA as P

OUTDIR = "charts"

# ─────────────────────────────────────────────────────────────────────────
# 01 · Beta: convergencia y outlier (Paso 9)
# ─────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
fuentes = ["stockanalysis.com", "Yahoo Finance", "Visa\n(mismo negocio)", "GuruFocus\n(outlier)", "Investing.com\n(5Y)"]
betas = [0.74, 0.76, 0.76, 0.58, 0.82]
colores = [P["azul"], P["azul"], P["verde"], P["rojo_oscuro"], P["ocre"]]
x = np.arange(len(fuentes))
bars = ax.bar(x, betas, color=colores, width=0.58, zorder=3)
for xi, b in zip(x, betas):
    ax.text(xi, b + 0.02, f"{b:.2f}".replace(".", ","), ha="center", va="bottom",
            fontsize=9.5, fontweight="bold", color=P["tinta"])
ax.set_xticks(x); ax.set_xticklabels(fuentes, fontsize=8.4)
ax.set_ylim(0, 0.95)
ax.set_ylabel("Beta (5 años)")
cs.deco(ax, "El beta que ancla el WACC no está triangulado con certeza",
        "Convergencia entre tres fuentes en 0,74-0,76 frente a dos outliers no reconciliados",
        "Fuente: stockanalysis.com, Yahoo Finance, GuruFocus, Investing.com — citados en Paso 9 del dossier, 3-sep-2026.",
        fig, flag_y=0.94)
plt.tight_layout(rect=[0, 0.14, 1, 0.84])
cs.save(fig, "01_beta_fuentes", OUTDIR)

# ─────────────────────────────────────────────────────────────────────────
# 02 · Rango de valor intrínseco (piso de resolución) vs precio actual
# ─────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 3.6))
lo, hi = 590, 730
precio = 580.98
ax.barh([0], [hi - lo], left=[lo], height=0.42, color=P["azul_cielo"], zorder=3,
        edgecolor=P["azul_noche"], linewidth=1.0)
ax.axvline(precio, color=P["rojo"], lw=2.2, zorder=4, linestyle="--", ymax=0.72)
ax.text(precio, 0.46, "PRECIO HOY: 580,98", color=P["rojo"], fontsize=9.5, fontweight="bold",
        ha="center", va="bottom")
ax.text(lo, -0.30, f"{lo}", color=P["azul_noche"], fontsize=9.5, fontweight="bold", ha="center", va="top")
ax.text(hi, -0.30, f"{hi}", color=P["azul_noche"], fontsize=9.5, fontweight="bold", ha="center", va="top")
ax.text((lo + hi) / 2, 0, "RANGO RAZONABLE\nDE VALOR INTRÍNSECO", ha="center", va="center",
        fontsize=8.6, color=P["azul_noche"], fontweight="bold")
ax.set_xlim(560, 760)
ax.set_ylim(-0.45, 0.55)
ax.set_yticks([])
ax.set_xlabel("US dólares por acción")
cs.deco(ax, "El precio de hoy cae en el borde inferior del rango, no claramente dentro ni fuera",
        "Piso de resolución del DCF explícito a 10 años, WACC central 7,7-7,8% (Paso 9)",
        "Fuente: dossier de valoración, Paso 9 — sensibilidad al crecimiento terminal perpetuo, 3-sep-2026.",
        fig)
plt.tight_layout(rect=[0, 0.14, 1, 0.88])
cs.save(fig, "02_valor_intrinseco_vs_precio", OUTDIR)

# ─────────────────────────────────────────────────────────────────────────
# 03 · DCF explícito: sensibilidad al crecimiento terminal perpetuo
# ─────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.8))
g_term = [2.0, 2.5, 3.0, 3.5, 4.5]
val = [590, 630, 675, 730, 900]
ax.plot(g_term, val, marker="o", color=P["azul"], lw=2.4, markersize=7, zorder=3)
for gx, vy in zip(g_term, val):
    etiqueta = f"{vy}+" if gx == 4.5 else f"{vy}"
    ax.annotate(etiqueta, (gx, vy), textcoords="offset points", xytext=(0, 10),
                ha="center", fontsize=9.2, fontweight="bold", color=P["azul_noche"])
ax.axhline(580.98, color=P["rojo"], lw=1.8, linestyle="--", zorder=2)
ax.text(4.4, 580.98 + 8, "precio hoy: 580,98", color=P["rojo"], fontsize=8.6,
        ha="right", fontweight="bold")
ax.annotate("DCF inverso: el escenario\nque iguala el precio de hoy\nimplica g terminal ≈ 2,0%\n(≈ PIB nominal, sin prima)",
            xy=(2.0, 590), xytext=(2.55, 480), fontsize=8.2, color=P["gris"],
            arrowprops=dict(arrowstyle="->", color=P["gris"], lw=1.0))
ax.set_xlabel("Crecimiento terminal perpetuo asumido (%)")
ax.set_ylabel("Valor implícito por acción (US$)")
ax.set_xlim(1.7, 4.8)
ax.set_ylim(450, 950)
cs.deco(ax, "El valor de Mastercard es extremadamente sensible al crecimiento a perpetuidad",
        "DCF explícito a 10 años, owner earnings base 2025 = US$16.562M, WACC central 7,8% (Paso 9)",
        "Fuente: dossier de valoración, Paso 9, tabla de sensibilidad al g terminal — 3-sep-2026.",
        fig)
plt.tight_layout(rect=[0, 0.14, 1, 0.88])
cs.save(fig, "03_dcf_sensibilidad_g", OUTDIR)

# ─────────────────────────────────────────────────────────────────────────
# 04 · Motor de reinversión: tasa de reinversión (lumpy) vs ROIC (Paso 5)
# ─────────────────────────────────────────────────────────────────────────
fig, ax1 = plt.subplots(figsize=(9.4, 4.8))
years = [2021, 2022, 2023, 2024, 2025]
reinv = [53.4, 4.0, 0.3, 19.9, 0.7]
roic = [61.1, 76.7, 80.9, 79.9, 93.3]
x = np.arange(len(years))
ax1.bar(x, reinv, color=P["azul_cielo"], width=0.5, zorder=3, label="Tasa de reinversión")
for xi, r in zip(x, reinv):
    ax1.text(xi, r + 1.5, f"{r:.1f}".replace(".", ",") + "%", ha="center", fontsize=8.4,
              color=P["azul_noche"], fontweight="bold")
ax1.set_ylim(0, 100)
ax1.set_ylabel("Tasa de reinversión (%)", color=P["azul_noche"])
ax1.set_xticks(x); ax1.set_xticklabels(years)

ax2 = ax1.twinx()
ax2.plot(x, roic, color=P["rojo"], marker="o", lw=2.4, markersize=7, zorder=4)
for xi, rc in zip(x, roic):
    ax2.text(xi, rc + 2.2, f"{rc:.1f}".replace(".", ",") + "%", ha="center", fontsize=8.4,
              color=P["rojo"], fontweight="bold")
ax2.set_ylim(0, 100)
ax2.set_ylabel("ROIC (%)", color=P["rojo"])
ax2.spines["top"].set_visible(False)
ax2.tick_params(length=0)

cs.deco(ax1, "Reinversión errática, ROIC alto y estable: el motor clásico no explica todo el crecimiento",
        "Tasa de reinversión promedio ponderada 5 años ≈13,1% · ROIC promedio simple ≈78,4% · g implícito ≈10,3%",
        "Fuente: dossier de hechos, Paso 5 — reconstruido desde cero contra XBRL crudo, 3-sep-2026.",
        fig)
plt.tight_layout(rect=[0, 0.14, 1, 0.88])
cs.save(fig, "04_motor_reinversion", OUTDIR)

# ─────────────────────────────────────────────────────────────────────────
# 05 · Trayectoria de crecimiento: real vs guía vs g mecánico implícito
# ─────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
cats = ["CAGR NOPAT\n2021→2025 real", "CAGR ingresos\n2023→2025 real", "Guía FY2026\n(management)", "g implícito\n(motor Paso 5)"]
vals = [15.65, 14.3, 11.5, 10.3]
colores = [P["azul"], P["azul_acero"], P["ocre"], P["rojo_oscuro"]]
labels_txt = ["≈15,6-15,7%", "≈14,3%", "≈11-12%\n(\"high end of\nlow double digits\")", "≈10,3%"]
x = np.arange(len(cats))
ax.bar(x, vals, color=colores, width=0.55, zorder=3)
for xi, v, lb in zip(x, vals, labels_txt):
    ax.text(xi, v + 0.4, lb, ha="center", va="bottom", fontsize=8.2, fontweight="bold", color=P["tinta"])
ax.set_xticks(x); ax.set_xticklabels(cats, fontsize=8.4)
ax.set_ylim(0, 20)
ax.set_ylabel("Tasa anual (%)")
cs.deco(ax, "La guía de management ya apunta hacia el techo mecánico, no hacia el histórico",
        "El g implícito del motor de reinversión infra-explica el pasado, pero se acerca a la guía futura",
        "Fuente: 8-K FY2025, transcript Q2 2026, dossier de hechos Paso 5 — 3-sep-2026.",
        fig)
plt.tight_layout(rect=[0, 0.14, 1, 0.88])
cs.save(fig, "05_crecimiento_trayectoria", OUTDIR)

# ─────────────────────────────────────────────────────────────────────────
# 06 · Comparación con el par estructural más cercano: Visa
# ─────────────────────────────────────────────────────────────────────────
fig, (axL, axR) = plt.subplots(1, 2, figsize=(9.4, 4.4))
empresas = ["Mastercard", "Visa"]
margenes = [57.6, 67.0]
axL.bar(empresas, margenes, color=[P["azul"], P["azul_acero"]], width=0.5, zorder=3)
for i, m in enumerate(margenes):
    axL.text(i, m + 1.2, f"{m:.1f}".replace(".", ",") + "%", ha="center", fontsize=9.5,
              fontweight="bold", color=P["tinta"])
axL.set_ylim(0, 80)
axL.set_title("Margen operativo GAAP", fontsize=9.6, color=P["tinta"], fontweight="bold")

multiplos = [31.3, 33.1]
axR.bar(empresas, multiplos, color=[P["azul"], P["azul_acero"]], width=0.5, zorder=3)
for i, m in enumerate(multiplos):
    axR.text(i, m + 0.6, f"{m:.1f}".replace(".", ",") + "x", ha="center", fontsize=9.5,
              fontweight="bold", color=P["tinta"])
axR.set_ylim(0, 40)
axR.set_title("Múltiplo EV / FCF", fontsize=9.6, color=P["tinta"], fontweight="bold")

cs.deco([axL, axR], "Visa y Mastercard cotizan como el mismo tipo de activo",
        "Beta idéntico (0,76) en la misma fuente — juntas caras o juntas razonables, no una más barata que la otra",
        "Fuente: dossier de valoración, Paso 9 — comparación cualitativa sin ranking (Candado C), 3-sep-2026.",
        fig)
plt.tight_layout(rect=[0, 0.14, 1, 0.88])
cs.save(fig, "06_pares_comparacion", OUTDIR)

print("Gráficos generados en", OUTDIR)
