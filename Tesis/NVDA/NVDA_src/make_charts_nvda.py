# -*- coding: utf-8 -*-
"""Gráficos NVDA — Tesis Ultra QG (método 12 pasos). Paleta y furniture Economist."""
import numpy as np
import matplotlib.pyplot as plt
import chart_style as CS
from paleta_qg import PALETA as P

# ── 1. Ingresos por plataforma FY21-FY26 (barras apiladas) ──────────────
years = ["FY21", "FY22", "FY23", "FY24", "FY25", "FY26"]
dc     = np.array([6696, 10613, 15005, 47525, 115186, 193737])
gaming = np.array([7759, 12462, 9067, 10447, 11350, 16042])
proviz = np.array([1053, 2111, 1544, 1553, 1878, 3191])
auto   = np.array([536, 566, 903, 1091, 1694, 2349])
oem    = np.array([631, 1162, 455, 306, 389, 619])

fig, ax = plt.subplots(figsize=(9.6, 5.4))
bottom = np.zeros(6)
for serie, color, label in [
    (dc, P["azul"], "Data Center"),
    (gaming, P["azul_cielo"], "Gaming"),
    (proviz, P["terracota"], "Pro. Visualization"),
    (auto, P["verde"], "Automotive"),
    (oem, P["ocre"], "OEM & Other"),
]:
    ax.bar(years, serie, bottom=bottom, color=color, label=label, width=0.62)
    bottom += serie

for i, tot in enumerate(bottom):
    ax.text(i, tot + 3500, f"{tot/1000:,.0f}B".replace(",", "."), ha="center",
            fontsize=9, fontweight="bold", color=P["tinta"])

ax.set_ylim(0, 235000)
ax.set_yticks([0, 50000, 100000, 150000, 200000])
ax.set_yticklabels(["0", "50B", "100B", "150B", "200B"])
ax.legend(loc="upper left", frameon=False, fontsize=8.4, ncol=1)
CS.deco(ax, "De empresa de GPU a infraestructura de IA en cinco años",
        "Ingresos por plataforma de mercado, USD millones — FY2021 a FY2026",
        "Fuente: 10-K NVIDIA FY2021-FY2026, EDGAR CIK 0001045810 (HECHO)", fig=fig)
fig.subplots_adjust(top=0.80, bottom=0.08, left=0.07, right=0.98)
CS.save(fig, "01_ingresos_segmento")

# ── 2. Trayectoria de margen bruto: real vs. guiado, el giro del ciclo ──
fig, ax = plt.subplots(figsize=(9.6, 4.8))
trims = ["Q3\nFY26", "Q4\nFY26", "Q1\nFY27", "Q2\nFY27", "Q3\nFY27\n(guiado)", "Q4\nFY27\n(piso guiado)"]
real  = [73.4, 75.0, 74.9, 75.0, None, None]
guia  = [None, None, None, None, 74.0, 71.5]
x = np.arange(len(trims))

ax.plot(x[:4], real[:4], marker="o", color=P["azul"], lw=2.4, ms=7, label="Margen bruto GAAP real")
ax.plot(x[3:5], [75.0, 74.0], marker="o", color=P["rojo_oscuro"], lw=2.0, ms=7,
        ls="--", label="Guía Q3 FY27")
ax.plot(x[4:6], [74.0, 71.5], marker="D", color=P["rojo_oscuro"], lw=2.0, ms=7, ls="--")
ax.axhspan(71, 72, color=P["rojo_oscuro"], alpha=0.10)
ax.text(4.5, 71.9, "piso guiado 71-72%\n(escasez HBM/DRAM)", fontsize=7.6,
        color=P["rojo_oscuro"], ha="center", style="italic")
for i, v in enumerate(real[:4]):
    ax.text(i, v + 0.35, f"{v}%".replace(".", ","), ha="center", fontsize=8.6, color=P["tinta"])
ax.set_xticks(x); ax.set_xticklabels(trims, fontsize=8.2)
ax.set_ylim(68, 78)
ax.legend(loc="lower left", frameon=False, fontsize=8.4)
CS.deco(ax, "La primera caída de margen guiada de toda la serie",
        "Margen bruto GAAP, % de ingresos — Q3 FY2026 a Q4 FY2027 (guiado)",
        "Fuente: 8-K NVIDIA, CFO Commentary EX-99.2, Q3 FY26 a Q2 FY27 (HECHO); guía Q3-Q4 FY27 (HECHO, declarado en la llamada)",
        fig=fig)
fig.subplots_adjust(top=0.78, bottom=0.14, left=0.07, right=0.98)
CS.save(fig, "02_margen_trayectoria")

# ── 3. Trayectoria de ingresos: guía real + 3 escenarios de desvanecimiento ──
fig, ax = plt.subplots(figsize=(9.6, 5.6))

anios = ["FY26", "FY27", "FY28", "FY29", "FY30", "FY31"]
x = np.arange(len(anios))

hecho_guiado = [215.9, 403.8, None, None, None, None]   # FY26 real, FY27 est (3/4 HECHO)
bear = [215.9, 403.8, 585.5, 702.6, 772.9, 819.2]
base = [215.9, 403.8, 686.5, 926.8, 1112.1, 1245.6]
bull = [215.9, 403.8, 706.6, 1024.6, 1311.5, 1547.6]

ax.plot(x, hecho_guiado, marker="o", color=P["tinta"], lw=2.6, ms=8, zorder=5,
        label="Real (FY26) + estimado FY27 (HECHO Q1-Q3, INFERENCIA Q4)")
ax.plot(x[1:], bull[1:], marker="^", color=P["verde"], lw=2.0, ms=6, ls="--", label="BULL — supera la guía (75%/FY28)")
ax.plot(x[1:], base[1:], marker="s", color=P["azul"], lw=2.4, ms=6.5, ls="--", label="BASE — la guía tal cual (70%/FY28)")
ax.plot(x[1:], bear[1:], marker="v", color=P["rojo_oscuro"], lw=2.0, ms=6, ls="--", label="BEAR — bajo la guía (45%/FY28)")

ax.annotate("Q3 FY27 guiado:\n108.000M ±2%", xy=(1, 403.8), xytext=(1.15, 520),
            fontsize=7.6, color=P["gris"], style="italic",
            arrowprops=dict(arrowstyle="->", color=P["gris"], lw=0.8))
ax.annotate("FY28: +70% guiado\npor la propia NVIDIA\n(\"supply constrained\")", xy=(2, base[2]),
            xytext=(2.25, base[2]-260), fontsize=7.6, color=P["azul"], style="italic",
            arrowprops=dict(arrowstyle="->", color=P["azul"], lw=0.8))

ax.axhline(3500, color=P["ocre"], lw=1.4, ls=":",
           label="TAM de industria citado por Kress: 3-4 billones USD/año hacia 2030 (toda la industria)")

ax.set_xticks(x); ax.set_xticklabels(anios, fontsize=9.5)
ax.set_ylabel("Ingresos anuales (miles de M USD)", fontsize=8.6)
ax.set_ylim(0, 3900)
ax.legend(loc="upper left", frameon=False, fontsize=7.6)
CS.deco(ax, "La guía real de NVIDIA, y tres formas de desvanecerla después",
        "Ingresos anuales por escenario, USD miles de millones — FY26 real a FY31 (~2030-31)",
        "Fuente: HECHO 10-Q/8-K NVIDIA FY26-Q2FY27 y guía Q3FY27/FY28 (26-ago-2026); FY29+ INFERENCIA propia (DCF §12)",
        fig=fig)
fig.subplots_adjust(top=0.80, bottom=0.09, left=0.09, right=0.97)
CS.save(fig, "03_trayectoria_escenarios")

# ── 4. Precio justo por escenario, banda de WACC, vs. precio de hoy ──────
fig, ax = plt.subplots(figsize=(9.6, 5.0))
escenarios = ["BEAR\n45%→3% · margen 33%", "BASE\n70%→3% · margen 39%", "BULL\n75%→3% · margen 44%", "Precio de hoy"]
lo = [83.84, 149.49, 215.40, 227.66]
hi = [100.00, 180.12, 261.52, 227.66]
colors = [P["rojo_oscuro"], P["azul"], P["verde"], P["tinta"]]
y = np.arange(len(escenarios))

for i in range(len(escenarios)):
    if hi[i] != lo[i]:
        ax.barh(i, hi[i]-lo[i], left=lo[i], color=colors[i], height=0.5, alpha=0.85)
        label = f"{lo[i]:.0f}-{hi[i]:.0f} USD"
    else:
        ax.barh(i, 4, left=225.66, color=colors[i], height=0.5)
        label = "227,66 USD (hoy)"
    ax.text(hi[i] + 5, i, label, va="center", fontsize=9,
            color=P["tinta"], fontweight="bold")

ax.axvline(227.66, color=P["tinta"], lw=1.4, ls="-", alpha=0.6)
ax.set_yticks(y); ax.set_yticklabels(escenarios, fontsize=9)
ax.set_xlim(0, 300)
ax.set_xlabel("USD por acción", fontsize=8.6)
ax.invert_yaxis()
CS.deco(ax, "Solo superando su propia guía, NVIDIA justifica el precio de hoy",
        "Precio justo por escenario (banda de WACC 12,35%-14,04%), DCF de 3 etapas anclado en guía real",
        "Fuente: cálculo propio sobre guía HECHO de NVIDIA (8-K 26-ago-2026) + desvanecimiento y TAM de industria propios",
        fig=fig)
fig.subplots_adjust(top=0.80, bottom=0.10, left=0.18, right=0.90)
CS.save(fig, "04_escenarios_valor")

print("4 gráficos generados en charts/")
