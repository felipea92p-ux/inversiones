# -*- coding: utf-8 -*-
"""Gráficos · Tesis-Forja Intuit (INTU) v4 · paleta y estilo de la casa."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import chart_style as cs
from paleta_qg import PALETA as C

# ── c1 · Cuatro anclajes, un precio (base FY2025) ──────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
esc = [("EPV · suelo sin crecimiento", 167, C["rojo_oscuro"]),
       ("Bajista propio (erosión IA amplia)", 274, C["terracota"]),
       ("Conservador (ancla del MoS)", 354, C["azul"]),
       ("FY2026E ajustado · conservador", 456, C["verde"])]
y = np.arange(len(esc))
vals = [e[1] for e in esc]
ax.barh(y, vals, color=[e[2] for e in esc], height=0.58, zorder=3)
for i, (n, v, c) in enumerate(esc):
    ax.text(v + 6, i, f"US\\${v}", va="center", fontsize=10, color=C["tinta"], fontweight="bold")
ax.axvline(290, color=C["rojo"], lw=2.2, zorder=4)
ax.text(290, 3.75, "Precio hoy US\\$290 (17,7x)", color=C["rojo"], fontsize=9.5, fontweight="bold", ha="center")
ax.set_yticks(y); ax.set_yticklabels([e[0] for e in esc], fontsize=9.5)
ax.set_xlim(0, 500); ax.invert_yaxis()
cs.deco(ax, "Cuatro anclajes, un precio", "Base FY2025 (owner earnings \\$4.115M) salvo la última fila, que ya incorpora 9 meses reales de FY2026",
        "DCF inverso propio, r=9%, terminal=3% · tesis-forja v4, templada en 3 rondas adversariales", fig)
cs.save(fig, "c1_anclajes")

# ── c2 · Mapa de zonas ──────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 5.4))
ax.set_xlim(0, 10); ax.set_ylim(140, 400)
def banda(y0, y1, color, alpha=0.35):
    ax.axhspan(y0, y1, xmin=0.04, xmax=0.96, color=color, alpha=alpha, zorder=2)
banda(354, 400, C["rojo"], 0.12)
banda(301, 354, C["ocre"], 0.16)
banda(266, 301, C["azul_cielo"], 0.30)
banda(212, 266, C["azul"], 0.30)
banda(140, 212, C["verde"], 0.30)
lineas = [(354, "Conservador \\$354 (ancla del MoS, base FY2025)", C["azul_noche"], "--", 1.8),
          (301, "\\$266-301 · banda gatillo-doble (el precio YA está aquí)", C["tinta"], ":", 1.4),
          (290, "PRECIO HOY · \\$290 (MoS +18,1% vs conservador)", C["rojo"], "-", 2.4),
          (266, "≤\\$266 · COMPRAR_INICIAL (MoS≥25%, requiere ronda 4+ y G1/G2/G3 limpios)", C["azul_noche"], "-", 1.6),
          (212, "≤\\$212 · COMPRAR_AGRESIVO (MoS≥40% + 2 señales de extremo)", C["verde"], "-", 1.6),
          (167, "EPV \\$167 · suelo sin crecimiento", C["gris"], "--", 1.2)]
for yv, lbl, c, ls, lw in lineas:
    ax.axhline(yv, color=c, ls=ls, lw=lw, zorder=4)
    ax.text(0.35, yv + 3, lbl, fontsize=8.6, color=c, fontweight="bold", zorder=5)
ax.text(9.6, 388, "RE-ANÁLISIS\nYA ACTIVO\n(precio dentro\nde la banda)", fontsize=8.8, color=C["rojo_oscuro"],
        fontweight="bold", ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.4", fc=C["panel"], ec=C["rojo_oscuro"], lw=1.2))
ax.set_xticks([]); ax.set_ylabel("US$ por acción", fontsize=9.5)
cs.deco(ax, "El mapa de zonas — el precio ya cruzó la primera banda", "A diferencia de V/MA/MSFT, aquí el precio de mercado ya entró en la banda de re-análisis intensivo",
        "Tesis-Forja v4 · zonas derivadas del conservador (MoS≥25%/40%) · templadas en 3 rondas adversariales", fig)
cs.save(fig, "c2_zonas")

# ── c3 · Una década que casi cuadruplicó ingresos ──────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
anos = ["FY16","FY17","FY18","FY19","FY20","FY21","FY22","FY23","FY24","FY25"]
ing = [4.694, 5.196, 6.025, 6.784, 7.679, 9.633, 12.726, 14.368, 16.285, 18.831]
mg = [26.5, 27.3, 25.9, 27.3, 28.3, 26.0, 20.2, 21.9, 22.3, 26.1]
sbc = [6.0, None, None, 5.9, 5.7, 7.8, 10.3, 11.9, 11.9, 10.4]
x = np.arange(len(anos))
ax.bar(x, ing, 0.56, color=C["azul"], zorder=3, label="Ingresos totales")
ax.set_xticks(x); ax.set_xticklabels(anos, fontsize=8.8)
ax.set_ylabel("US$ miles de millones", fontsize=9)
ax2 = ax.twinx()
ax2.plot(x, mg, color=C["rojo"], lw=2.0, marker="o", ms=4, label="Margen operativo GAAP (%)", zorder=4)
ax2.set_ylim(0, 42); ax2.set_ylabel("Margen operativo (%)", fontsize=9)
ax2.grid(False)
ax.legend(loc="upper left", fontsize=8.6, frameon=False)
ax2.legend(loc="lower right", fontsize=8.6, frameon=False)
ax.text(6, 13.5, "el valle: M&A\n(Credit Karma dic-20,\nMailchimp nov-21)\ndigiriéndose", fontsize=7.8,
        color=C["gris"], ha="center", style="italic")
cs.deco(ax, "Una década que casi cuadruplicó ingresos (CAGR 16,7%)", "El margen operativo cayó del 28,3% al 20,2% mientras Intuit digería Credit Karma y Mailchimp — y ya se recuperó a 26,1%",
        "10-K FY2016/FY2019/FY2022/FY2025, SEC EDGAR · verificado al decimal en 3 rondas adversariales", fig)
cs.save(fig, "c3_serie")

# ── c4 · El patrón quirúrgico: DIY se erosiona, lo asistido no (todavía) ──
fig, ax = plt.subplots(figsize=(9.2, 4.6))
cats = ["TurboTax\nOnline units", "Cuota de\ne-files", "Credit Karma\n(Q3 FY26 real)", "QuickBooks Online\nAccounting"]
vals = [-2, -1, 15, 22]
cols = [C["rojo_oscuro"], C["rojo_oscuro"], C["ocre"], C["verde"]]
bars = ax.bar(cats, vals, color=cols, width=0.55, zorder=3)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width()/2, v + (1.2 if v >= 0 else -2.2),
            f"{v:+d}%" if abs(v) < 10 else f"{v:+d}%", ha="center", fontsize=11, fontweight="bold", color=C["tinta"])
ax.axhline(0, color=C["tinta"], lw=1.0)
ax.set_ylim(-8, 28)
ax.set_ylabel("Variación interanual (%)", fontsize=9)
ax.text(2.5, -6, "Nota: unidades/cuota de TurboTax son puntos porcentuales, no % de variación", fontsize=7.6,
        color=C["gris"], ha="center", style="italic")
cs.deco(ax, "El patrón es quirúrgico, no generalizado", "El DIY puro (TurboTax) ya pierde terreno; Credit Karma desacelera pero crece; QuickBooks sostiene pricing power",
        "Comunicado de resultados Q3 FY2026 (20-may-2026) · 10-Q Q3 FY2026 · tesis-forja v4", fig)
cs.save(fig, "c4_patron")

# ── c5 · El precio de hoy exige el crecimiento más bajo de las 4 tesis ────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
tesis = ["Microsoft\n(MSFT)", "Visa\n(V)", "Mastercard\n(MA)", "Intuit\n(INTU)"]
g_impl = [13.8, 11.8, 9.5, 4.5]
guia = [None, None, None, 13.5]
cols = [C["azul_acero"], C["azul_acero"], C["azul_acero"], C["rojo"]]
bars = ax.bar(tesis, g_impl, 0.5, color=cols, zorder=3)
for b, v in zip(bars, g_impl):
    ax.text(b.get_x() + b.get_width()/2, v + 0.35, f"{v}%".replace(".", ","), ha="center",
            fontsize=11, fontweight="bold", color=C["tinta"])
ax.axhline(13.5, color=C["verde"], lw=1.8, ls="--", zorder=2)
ax.text(3, 14.3, "guía propia de Intuit FY2026: +13-14%", fontsize=8.6, color=C["verde"],
        fontweight="bold", ha="right")
ax.set_ylim(0, 17)
ax.set_ylabel("Crecimiento de FCF implícito a 10 años (%, r=9%)", fontsize=9)
cs.deco(ax, "El precio de hoy exige el crecimiento más bajo de las cuatro tesis", "DCF inverso, mismo protocolo en las 4: r=9%, terminal=3%, owner earnings = FCF−SBC",
        "Cálculo propio, tesis-forja v1-v4 · V/MA/MSFT/INTU, jul-2026", fig)
cs.save(fig, "c5_comparativo")

# ── c6 · ROIC: el bache de la digestión, y la salida ──────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.4))
anos6 = ["FY20","FY21","FY22","FY23","FY24","FY25"]
roic = [20.65, 17.64, 9.30, 8.53, 10.69, 14.40]
x6 = np.arange(len(anos6))
ax.plot(x6, roic, color=C["azul"], lw=2.4, marker="o", ms=7, zorder=4)
ax.fill_between(x6, 7.9, 9.9, color=C["ocre"], alpha=0.25, zorder=2, label="Rango de WACC estimado (7,9-9,9%)")
for xi, v in zip(x6, roic):
    ax.text(xi, v + 0.9, f"{v}%".replace(".", ","), ha="center", fontsize=9, fontweight="bold", color=C["tinta"])
ax.axvspan(1.5, 3.5, color=C["rojo_oscuro"], alpha=0.08, zorder=1)
ax.text(2.5, 4, "digestión Credit Karma (dic-20)\n+ Mailchimp (nov-21)", fontsize=8, color=C["rojo_oscuro"],
        ha="center", style="italic")
ax.set_xticks(x6); ax.set_xticklabels(anos6, fontsize=9.5)
ax.set_ylim(0, 24)
ax.set_ylabel("ROIC (%)", fontsize=9)
ax.legend(loc="upper right", fontsize=8.4, frameon=False)
cs.deco(ax, "El bache de la digestión, y la salida", "ROIC cayó casi hasta tocar el WACC durante la integración de M&A — y ya se recuperó a una brecha clara de +5-6pts",
        "stock-analysis-on.net (NOPAT/capital invertido) · WACC de terceros (gurufocus/alphaspread/valuesense)", fig)
cs.save(fig, "c6_roic")

# ── c7 · El colapso del precio, con fechas ─────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
fechas = ["jul-25\n(máximo)", "20-may-26\n(guía + recorte)", "21-may-26\n(-20% en 1 día)", "13-jul-26\n(hoy)"]
precios = [813.70, 340, 274, 290.00]
x7 = np.arange(len(fechas))
ax.plot(x7, precios, color=C["rojo_oscuro"], lw=2.2, marker="o", ms=8, zorder=4)
for xi, v in zip(x7, precios):
    ax.text(xi, v + 28, f"US\\${v:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            ha="center", fontsize=9.5, fontweight="bold", color=C["tinta"])
ax.set_xticks(x7); ax.set_xticklabels(fechas, fontsize=8.8)
ax.set_ylim(0, 900)
ax.set_ylabel("US$ por acción", fontsize=9)
ax.text(1.5, 720, "−64% de punta a punta — la acción peor del S&P 500 en 2026", fontsize=9.5,
        color=C["rojo_oscuro"], fontweight="bold", ha="center",
        bbox=dict(boxstyle="round,pad=0.4", fc=C["panel"], ec=C["rojo_oscuro"], lw=1.2))
cs.deco(ax, "Un año que borró dos tercios del precio", "El profit warning del 20-may-2026 y la investigación de fraude de valores del día siguiente marcan el quiebre",
        "StockAnalysis.com / Google Finance (fetch directo, 13-jul-2026) · comunicados oficiales de Intuit", fig)
cs.save(fig, "c7_colapso")

print("7 charts OK → charts/")
