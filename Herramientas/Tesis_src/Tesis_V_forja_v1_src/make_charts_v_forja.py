# -*- coding: utf-8 -*-
"""Gráficos · Tesis-Forja Visa (V) v4.1 · paleta y estilo de la casa."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import chart_style as cs
from paleta_qg import PALETA as C

# ── c1 · Escenarios con probabilidades ────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
esc = [("Severo (R1+R2)", 202, "10%", C["rojo_oscuro"]),
       ("Bajista moderado", 244, "17,5%", C["terracota"]),
       ("Conservador (ancla MoS)", 260, "32,5%", C["ocre"]),
       ("Base (indicador con fade)", 322, "30%", C["azul"]),
       ("Alcista propio", 357, "10%", C["verde"])]
y = np.arange(len(esc))
vals = [e[1] for e in esc]
ax.barh(y, vals, color=[e[3] for e in esc], height=0.62, zorder=3)
for i, (n, v, p, c) in enumerate(esc):
    ax.text(v + 4, i, f"\\${v} · P={p}", va="center", fontsize=9.5, color=C["tinta"], fontweight="bold")
ax.axvline(348.97, color=C["rojo"], lw=2.2, zorder=4)
ax.text(348.97, 4.62, "Precio hoy \\$348,97", color=C["rojo"], fontsize=9.5, fontweight="bold", ha="center")
ax.axvline(280, color=C["azul_noche"], lw=1.6, ls="--", zorder=4)
ax.text(280, -0.62, "EV ponderado \\$280", color=C["azul_noche"], fontsize=9, ha="center")
ax.set_yticks(y); ax.set_yticklabels([e[0] for e in esc], fontsize=9.5)
ax.set_xlim(0, 435); ax.invert_yaxis()
cs.deco(ax, "Cinco escenarios, un precio", "Valor por acción (base honesta \\$19,7B de owner earnings, r=9%) · probabilidades ancladas a la cohorte",
        "DCF propio reproducible · probabilidades capadas a la tasa base (base+alcista = 40%)", fig)
cs.save(fig, "c1_escenarios")

# ── c2 · Mapa de zonas ────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 5.4))
ax.set_xlim(0, 10); ax.set_ylim(95, 395)
def banda(y0, y1, color, alpha=0.35):
    ax.axhspan(y0, y1, xmin=0.04, xmax=0.96, color=color, alpha=alpha, zorder=2)
banda(330, 395, C["rojo"], 0.14)
banda(263, 330, C["ocre"], 0.18)
banda(221, 263, C["azul_cielo"], 0.30)
banda(195, 221, C["azul"], 0.30)
banda(156, 195, C["verde"], 0.30)
banda(100, 156, C["verde"], 0.52)
lineas = [(348.97, "PRECIO HOY · \\$348,97 (33,4x owner earnings)", C["rojo"], "-", 2.4),
          (260, "Conservador \\$260 (ancla del MoS)", C["azul_noche"], "--", 1.8),
          (263, "≤\\$263 · re-análisis intensivo (3:1 canónico — trabajo, no capital)", C["tinta"], ":", 1.4),
          (221, "\\$195-221 · banda gatillo-doble (el precio abre, el fundamental decide)", C["azul_noche"], ":", 1.2),
          (195, "≤\\$195 · COMPRAR INICIAL no-CALIENTE (MoS ≥25%) · \\$182 si CALIENTE", C["azul_noche"], "-", 1.6),
          (156, "≤\\$156 · COMPRAR AGRESIVO (MoS ≥40% + 2 señales de extremo)", C["verde"], "-", 1.6),
          (116, "EPV \\$116 · suelo sin crecimiento — el 65% del precio es crecimiento futuro", C["gris"], "--", 1.2)]
for yv, lbl, c, ls, lw in lineas:
    ax.axhline(yv, color=c, ls=ls, lw=lw, zorder=4)
    ax.text(0.35, yv + 3, lbl, fontsize=8.8, color=c, fontweight="bold", zorder=5)
ax.text(9.6, 372, "ZONAS HOY:\nCONGELADAS\n(G6/G6-bis sin armar)", fontsize=9, color=C["rojo_oscuro"],
        fontweight="bold", ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.4", fc=C["panel"], ec=C["rojo_oscuro"], lw=1.2))
ax.set_xticks([]); ax.set_ylabel("US$ por acción", fontsize=9.5)
cs.deco(ax, "El mapa de zonas — dinámico y congelado a la vez", "Se re-deriva con cada 10-Q re-corriendo el DCF conservador; se descongela armando G6/G6-bis con dato primario",
        "Tesis-Forja v4.1 · zonas derivadas de los candados del estándar (MoS sobre conservador, asimetría canónica, techo 25x)", fig)
cs.save(fig, "c2_zonas")

# ── c3 · Serie de 10 años ─────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
anos = ["FY15","FY16","FY17","FY18","FY19","FY20","FY21","FY22","FY23","FY24","FY25"]
ing = [13.88, 15.08, 18.36, 20.61, 22.98, 21.85, 24.11, 29.31, 32.65, 35.93, 40.00]
fcf = [6.17, 5.05, 8.50, 12.00, 12.03, 9.70, 14.52, 17.88, 19.70, 18.69, 21.58]
x = np.arange(len(anos))
ax.bar(x - 0.21, ing, 0.42, color=C["azul"], label="Ingresos netos", zorder=3)
ax.bar(x + 0.21, fcf, 0.42, color=C["azul_cielo"], label="Free cash flow", zorder=3)
ax.set_xticks(x); ax.set_xticklabels(anos, fontsize=8.6)
ax.set_ylabel("US$ miles de millones", fontsize=9)
ax2 = ax.twinx()
mg = [65.3, 52.3, 66.2, 62.9, 65.3, 64.5, 65.6, 64.2, 64.3, 65.7, 60.0]
ax2.plot(x, mg, color=C["rojo"], lw=2.0, marker="o", ms=4, label="Margen operativo GAAP (%)", zorder=4)
ax2.set_ylim(40, 75); ax2.set_ylabel("Margen operativo (%)", fontsize=9)
ax2.grid(False)
ax.legend(loc="upper left", fontsize=8.6, frameon=False)
ax2.legend(loc="lower right", fontsize=8.6, frameon=False)
cs.deco(ax, "Una década sin maquillaje", "Ingresos +11,2% CAGR · FCF +13,3% · margen clavado en 62-68% (FY16 y FY25: cargos identificables)",
        "SEC XBRL + 10-K FY2015-FY2025, verificado al decimal por doble pasada adversarial", fig)
cs.save(fig, "c3_serie")

# ── c4 · El patrón A2A y su grieta ────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
cats = ["Brasil\ndébito", "Brasil\ncrédito tarjeta", "India\ndébito", "India\ncrédito (mercado)*"]
vals = [0.2, 14.5, -67, 164]
cols = [C["rojo_oscuro"], C["verde"], C["rojo_oscuro"], C["ocre"]]
bars = ax.bar(cats, vals, color=cols, width=0.58, zorder=3)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width()/2, v + (7 if v >= 0 else -13),
            f"{v:+.1f}%".replace(".", ","), ha="center", fontsize=10, fontweight="bold", color=C["tinta"])
ax.axhline(0, color=C["tinta"], lw=1.0)
ax.set_ylim(-95, 240)
ax.text(3, 105, "*capturado en gran parte por\nRuPay-on-UPI — Visa excluida\npor diseño de NPCI", fontsize=8.6,
        color=C["rojo_oscuro"], ha="center",
        bbox=dict(boxstyle="round,pad=0.35", fc=C["panel"], ec=C["gris_linea"]))
ax.set_ylabel("Crecimiento (%)", fontsize=9)
cs.deco(ax, "El asalto A2A es quirúrgico — con una grieta", "Donde Pix/UPI escalan, el débito muere; el crédito resiste en Brasil y en India lo captura el propio riel A2A",
        "BCB/ABECS (feb-2026) · RBI/NPCI (may-2026) · corrección de la ronda adversarial 1", fig)
cs.save(fig, "c4_a2a")

# ── c5 · La compresión silenciosa (R1) ────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.4))
xs = [2015, 2017, 2019, 2025]
ys = [17.1, 19.9, 21.2, 28.3]
ax.plot(xs, ys, color=C["azul"], lw=2.4, marker="o", ms=6, zorder=4, label="Incentives / ingreso bruto")
xe = [2025, 2026, 2027, 2028, 2029, 2030, 2031]
ye_r = [28.3 + 1.1*i for i in range(7)]
ye_l = [28.3 + 0.5*i for i in range(7)]
ax.plot(xe, ye_r, color=C["rojo_oscuro"], lw=1.4, ls=":", zorder=3, label="Extrapolación ritmo década (~1,1pt/año)")
ax.plot(xe, ye_l, color=C["gris"], lw=1.4, ls=":", zorder=3, label="Extrapolación ritmo reciente (~0,5pt/año)")
ax.axhline(29.5, color=C["ocre"], lw=1.6, ls="--"); ax.text(2015.2, 29.8, "ÁMBAR G1: 29,5% (la primera ficha del dominó)", fontsize=8.8, color=C["ocre"], fontweight="bold")
ax.axhline(31.0, color=C["rojo"], lw=1.8); ax.text(2015.2, 31.3, "ROJO G1: 31% — tesis de pricing power rota", fontsize=8.8, color=C["rojo"], fontweight="bold")
ax.set_xlim(2014.6, 2031.4); ax.set_ylim(15, 36)
ax.set_ylabel("% del ingreso bruto", fontsize=9)
ax.legend(loc="lower right", fontsize=8.4, frameon=False)
cs.deco(ax, "R1 · La compresión silenciosa cruza su umbral por simple extrapolación", "Lo que Visa devuelve a bancos y mega-comercios por lealtad: de 17,1% a 28,3% del bruto en una década",
        "10-K FY2015/FY2017/FY2019 y release FY2025 · G1 vigilado TRIMESTRALMENTE en cada 10-Q", fig)
cs.save(fig, "c5_incentives")

print("5 charts OK → charts/")
