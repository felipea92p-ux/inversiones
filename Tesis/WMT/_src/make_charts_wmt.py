# -*- coding: utf-8 -*-
"""Gráficos de la Tesis Ultra QG — Walmart (WMT). Datos ya calculados en el
documento de 12 pasos (Tesis/WMT/2026-09-12_UltraTesis_WMT_metodo12_borrador.md).
Cero recálculo aquí — solo visualización."""
import numpy as np
import matplotlib.pyplot as plt
import chart_style as cs
from paleta_qg import PALETA as P

FUENTE_EDGAR = "Fuente: 10-K FY2026 (SEC EDGAR, Accession 0000104169-26-000055, 2026-03-13) · cálculo propio sobre líneas HECHO."
FUENTE_MERCADO = "Fuente: precio 11-sep-2026 (stockanalysis.com); Treasury 10Y 11-sep-2026; Damodaran ERP ene-2026 · cálculo propio (Paso 9)."

# ── Gráfico 1: DCF inverso — g exigido por el precio vs. g mecánico ──────
fig, ax = plt.subplots(figsize=(9.4, 5.3))
wacc = np.array([6.6, 7.0, 7.3])
g_exigido = np.array([15.3, 16.8, 17.8])
bars = ax.bar(wacc.astype(str), g_exigido, width=0.55, color=P["azul"], zorder=3,
              label="g exigido por el precio de hoy (DCF inverso, 10a + fade 3%)")
for x, y in zip(range(len(wacc)), g_exigido):
    ax.text(x, y + 0.4, f"{y:.1f}%", ha="center", fontsize=9.5, fontweight="bold",
            color=P["tinta"])

ax.axhspan(0.3, 2.0, color=P["verde"], alpha=0.28, zorder=1,
           label="g mecánico honesto (Paso 5, revisado tras Candado A): 0,3%-2%")
ax.axhline(8.3, color=P["gris_medio"], linestyle=":", lw=1.6, zorder=2)
ax.text(2.05, 8.3 + 0.4, "g mecánico original (8,3%) —\ndescartado en el Paso 10",
        fontsize=7.6, style="italic", color=P["gris_medio"], ha="right")

ax.set_ylim(0, 20.5)
ax.set_xlabel("WACC de mercado usado (%)", fontsize=9, color=P["gris"])
ax.set_ylabel("Crecimiento anual de owner earnings exigido a 10 años (%)", fontsize=9)
ax.legend(loc="upper left", fontsize=7.8, frameon=False)
cs.deco(ax, "El precio de hoy exige un motor que la empresa no muestra",
        "WMT: g exigido por el DCF inverso (Paso 9.3) vs. el g mecánico del propio motor de reinversión (Paso 5)",
        FUENTE_MERCADO, fig=fig)
fig.subplots_adjust(top=0.78, bottom=0.13, left=0.10, right=0.97)
cs.save(fig, "wmt_dcf_inverso")

# ── Gráfico 2: Owner earnings — la mejora de FY26 pierde tracción ───────
fig, ax = plt.subplots(figsize=(9.4, 5.3))
anios = ["FY2024", "FY2025", "FY2026"]
oe = [13.027, 9.891, 11.320]
colores = [P["azul_cielo"], P["azul_acero"], P["azul"]]
bars = ax.bar(anios, oe, width=0.5, color=colores, zorder=3)
for x, y in zip(range(len(anios)), oe):
    ax.text(x, y + 0.25, f"US${y:,.1f}B".replace(",", "."), ha="center",
            fontsize=9.5, fontweight="bold", color=P["tinta"])

ax.annotate("H1 FY2027 (semestre más reciente, earnings release):\ncapex +24% YoY, FCF cae US$1.400M YoY\npese a que el OCF operativo SUBIÓ US$1.400M",
            xy=(2, 11.320), xytext=(1.15, 5.2),
            fontsize=8.0, style="italic", color=P["rojo_oscuro"],
            ha="left", va="top",
            arrowprops=dict(arrowstyle="->", color=P["rojo_oscuro"], lw=1.3))

ax.set_ylim(0, 15.5)
ax.set_ylabel("Owner earnings = OCF − capex − SBC (US$, miles de millones)", fontsize=9)
cs.deco(ax, "Owner earnings: +14,4% en FY26, con la primera señal de reversión ya visible",
        "WMT: FCF (OCF − capex) menos compensación en acciones (SBC), FY24-FY26",
        FUENTE_EDGAR, fig=fig)
fig.subplots_adjust(top=0.78, bottom=0.10, left=0.10, right=0.97)
cs.save(fig, "wmt_owner_earnings")

# ── Gráfico 3: ROIC vs WACC de mercado ──────────────────────────────────
fig, ax = plt.subplots(figsize=(9.4, 5.3))
anios = ["FY2025", "FY2026"]
roic_lo = [15.9, 14.5]   # con arrendamientos operativos
roic_hi = [17.6, 16.1]   # sin arrendamientos operativos
x = np.arange(len(anios))
w = 0.32
ax.bar(x - w/2, roic_lo, width=w, color=P["azul_acero"], zorder=3, label="ROIC (con arrendamientos operativos en capital invertido)")
ax.bar(x + w/2, roic_hi, width=w, color=P["azul"], zorder=3, label="ROIC (sin arrendamientos operativos)")
for xi, (lo, hi) in enumerate(zip(roic_lo, roic_hi)):
    ax.text(xi - w/2, lo + 0.3, f"{lo:.1f}%", ha="center", fontsize=8.6, color=P["tinta"])
    ax.text(xi + w/2, hi + 0.3, f"{hi:.1f}%", ha="center", fontsize=8.6, color=P["tinta"])

ax.axhspan(6.6, 7.3, color=P["rojo"], alpha=0.22, zorder=1, label="WACC de mercado bottom-up (Candado B): 6,6%-7,3%")
ax.set_xticks(x); ax.set_xticklabels(anios)
ax.set_ylim(0, 20)
ax.set_ylabel("ROIC / WACC (%)", fontsize=9)
ax.legend(loc="upper right", fontsize=7.8, frameon=False)
cs.deco(ax, "Sin knock-out: el ROIC dobla holgadamente al costo de capital",
        "WMT: ROIC (NOPAT / capital invertido) vs. WACC de mercado, FY2025-FY2026",
        FUENTE_EDGAR, fig=fig)
fig.subplots_adjust(top=0.78, bottom=0.10, left=0.10, right=0.97)
cs.save(fig, "wmt_roic_wacc")

print("3 gráficos generados en charts/")
