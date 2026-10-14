# -*- coding: utf-8 -*-
"""Gráficos · Ultra Tesis DSG (Descartes Systems Group) · 2026-09-04
Todas las cifras provienen literalmente del dossier verificado
(2026-09-04_UltraTesis_DSG_metodo12_borrador.md). Cero recálculo:
donde el dossier declara una discrepancia sin reconciliar, el gráfico
la muestra tal cual, con nota.
"""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save
from paleta_qg import PALETA as P

# ─────────────────────────────────────────────────────────────────
# 01 · Rango de valor (DCF caso base) vs EV de mercado — Sección 12
# ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11.2, 4.3))
ev_lo, ev_hi = 2300, 3500
ev_mkt = 6400
ax.barh([1], [ev_hi - ev_lo], left=[ev_lo], height=0.5, color=P["azul"])
ax.scatter([ev_mkt], [1], marker="D", s=150, color=P["rojo"], zorder=5)
ax.annotate("US$2.300-3.500M", (np.mean([ev_lo, ev_hi]), 1), xytext=(0, 20),
            textcoords="offset points", ha="center", fontsize=10,
            fontweight="bold", color=P["tinta"])
ax.annotate("EV mercado\nUS$6.400M", (ev_mkt, 1), xytext=(0, -42),
            textcoords="offset points", ha="center", fontsize=9.2,
            color=P["rojo"], fontweight="bold")
ax.annotate("brecha: −45% a −64%", (np.mean([ev_hi, ev_mkt]), 1.3),
            ha="center", fontsize=8.6, style="italic", color=P["gris"])
ax.annotate("", xy=(ev_mkt, 1.2), xytext=(ev_hi, 1.2),
            arrowprops=dict(arrowstyle="-|>", color=P["gris"], lw=1.1))
ax.set_xlim(1800, 7000)
ax.set_ylim(0.35, 1.75)
ax.set_yticks([])
ax.set_xlabel("Enterprise Value (millones de US$)")
fig.subplots_adjust(top=.74, bottom=.16, left=.055, right=.97)
deco(ax, "Lo que paga el mercado frente a lo que arroja el DCF",
     "Caso base: crecimiento 10-12% (años 1-4) desacelerando a 3-4% (años 8-10), ROIC 13-15%, WACC 9%",
     "Fuente: Paso 9 del dossier verificado, DSG · EV/EBITDA actual ≈18,7-20x, EV/Revenue 8,48x")
save(fig, "01_valor_vs_precio")

# ─────────────────────────────────────────────────────────────────
# 02 · Crecimiento orgánico: la desaceleración de 3 años y el salto
# ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11.2, 4.5))
periodos = ["FY22", "FY23", "FY24", "FY25", "FY26", "Q1 FY27"]
crec = [13.9, 7.2, 9.0, 5.0, 3.9, 11.1]
colores = [P["azul_acero"]] * 5 + [P["rojo"]]
bars = ax.bar(periodos, crec, color=colores, width=0.58)
for b, v in zip(bars, crec):
    ax.annotate(f"{v:.1f}%", (b.get_x() + b.get_width() / 2, v), xytext=(0, 4),
                textcoords="offset points", ha="center", fontsize=9, fontweight="bold",
                color=P["tinta"])
ax.axhline(9, color=P["verde"], lw=1.3, ls="--")
ax.axhline(6, color=P["rojo_oscuro"], lw=1.3, ls="--")
ax.text(5.55, 9.4, "≥9% en ambos → refuta salto transitorio", fontsize=7.8,
        color=P["verde"], ha="right", style="italic")
ax.text(5.55, 6.4, "<6% → confirma reversión", fontsize=7.8,
        color=P["rojo_oscuro"], ha="right", style="italic")
ax.set_ylabel("Crecimiento orgánico interanual")
ax.set_ylim(0, 15.5)
fig.subplots_adjust(top=.72, bottom=.11, left=.07, right=.97)
deco(ax, "Tres años de desaceleración, y un salto que aún no se explica del todo",
     "Serie corregida (misma convención FY22-FY26) · Q1 FY27 coincide con volatilidad arancelaria / fin del de minimis",
     "Fuente: Paso 5 del dossier verificado, DSG (MD&A / 6-K, re-derivado por verificación adversarial)")
save(fig, "02_crecimiento_organico")

# ─────────────────────────────────────────────────────────────────
# 03 · Dónde fue el capital reinvertido en FY26 (~95% del NOPAT)
# ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11.2, 4.4))
conceptos = ["Capex", "3GTMS", "Finale\n(neto)", "Idelic"]
montos = [5.7, 112.7, 39.2, 25.3]
colores2 = [P["gris_medio"], P["rojo"], P["azul"], P["azul_acero"]]
bars = ax.bar(conceptos, montos, color=colores2, width=0.5)
for b, v in zip(bars, montos):
    ax.annotate(f"US${v:.1f}M", (b.get_x() + b.get_width() / 2, v), xytext=(0, 4),
                textcoords="offset points", ha="center", fontsize=9.2, fontweight="bold",
                color=P["tinta"])
ax.set_ylabel("Millones de US$")
ax.set_ylim(0, 128)
fig.subplots_adjust(top=.72, bottom=.11, left=.07, right=.97)
deco(ax, "El 96% de lo reinvertido en FY26 fue a tres compras sin ROIC individual conocido",
     "Suman US$177,2M frente a 151,6 millones de \"M&A neto\" reportado — discrepancia sin reconciliar, mostrada tal cual",
     "Fuente: Paso 5 y Golpe 2 (Paso 10) del dossier verificado, DSG")
save(fig, "03_capital_allocation_fy26")

# ─────────────────────────────────────────────────────────────────
# 04 · Sensibilidad WACC → años de crecimiento de doble dígito exigidos
# ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11.2, 3.8))
escenarios = ["Beta de regresión baja (WACC 5,5%-6,5%)\nprohibido por el Candado B",
              "WACC bottom-up (9%-10,5%)\nvigente tras el Golpe 3"]
lo = [5, 8]
hi = [6, 10]
y = [0, 1]
colores3 = [P["gris_medio"], P["rojo"]]
for yi, l, h, c in zip(y, lo, hi, colores3):
    ax.barh([yi], [h - l], left=[l], height=0.45, color=c)
    ax.annotate(f"{l}-{h} años", (np.mean([l, h]), yi), xytext=(0, 13),
                textcoords="offset points", ha="center", fontsize=9.5,
                fontweight="bold", color=P["tinta"])
ax.set_yticks(y)
ax.set_yticklabels(escenarios, fontsize=8.8)
ax.set_xlabel("Años de crecimiento de doble dígito (10-12%) exigidos por el precio actual")
ax.set_xlim(0, 12)
ax.set_ylim(-0.55, 1.55)
fig.subplots_adjust(top=.68, bottom=.16, left=.30, right=.97)
deco(ax, "Cuánto tiempo tiene que durar el crecimiento para justificar el precio de hoy",
     "Ventana empírica típica de ventaja competitiva en software vertical mid-cap: 5-7 años (referencia cualitativa)",
     "Fuente: Paso 9 / Golpe 3 (Paso 10) del dossier verificado, DSG — DCF inverso, g terminal 2,5%")
save(fig, "04_sensibilidad_wacc")

# ─────────────────────────────────────────────────────────────────
# 05 · Contexto de pares: ¿problema de categoría o de empresa?
# ─────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11.2, 4.6))
nombres = ["Descartes (orgánico FY26)", "Descartes (orgánico Q1 FY27)",
           "Manhattan Associates (SaaS/cloud)", "Kinaxis (cloud)",
           "e2open (FY2024, previo a\nser absorbida por WiseTech)"]
lo2 = [3.9, 11.1, 24, 16, -4.2]
hi2 = [3.9, 11.1, 26, 20, -4.2]
colores4 = [P["azul_acero"], P["rojo"], P["verde"], P["verde"], P["rojo_oscuro"]]
for i, (l, h, c) in enumerate(zip(lo2, hi2, colores4)):
    if h > l:
        ax.barh([i], [h - l], left=[l], height=0.55, color=c)
        lab = f"{l:.0f}-{h:.0f}%"
        xpos = np.mean([l, h])
    else:
        ax.barh([i], [abs(l)], left=[min(l, 0)], height=0.55, color=c)
        lab = f"{l:.1f}%"
        xpos = l
    ax.annotate(lab, (xpos, i), xytext=(0, 13), textcoords="offset points",
                ha="center", fontsize=9, fontweight="bold", color=P["tinta"])
ax.axvline(0, color=P["gris_linea"], lw=0.9)
ax.set_yticks(range(len(nombres)))
ax.set_yticklabels(nombres, fontsize=8.8)
ax.set_xlabel("Crecimiento de ingresos interanual, último dato público")
ax.invert_yaxis()
fig.subplots_adjust(top=.70, bottom=.11, left=.24, right=.97)
deco(ax, "La desaceleración de Descartes no parece ser un problema de categoría",
     "Pares sanos (Manhattan, Kinaxis) batieron guía con crecimiento cloud fuerte; e2open cayó financiándose con deuda, no con caja",
     "Fuente: Paso 4 y Paso 9 (contexto de pares, Candado C — sin ranking) del dossier verificado, DSG")
save(fig, "05_pares_crecimiento")

print("Gráficos generados en charts/")
