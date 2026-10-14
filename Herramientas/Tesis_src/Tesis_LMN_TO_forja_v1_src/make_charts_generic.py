# -*- coding: utf-8 -*-
"""Gráficos genéricos · Ultra Tesis forja · lee chartdata.json y produce 3 charts.
Uso: python3 make_charts_generic.py <chartdata.json>"""
import sys, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import chart_style as cs
from paleta_qg import PALETA as C

cd = json.load(open(sys.argv[1], encoding="utf-8"))
MON = cd.get("moneda", "US$").replace("USD", "US$").replace("CHF", "CHF ").replace("GBp", "GBp ").replace("CAD", "C$")
precio = cd["precio"]

def fmt(v):
    if v >= 1000:
        return f"{v:,.0f}".replace(",", ".")
    return f"{v:,.2f}".rstrip("0").rstrip(".") if v < 100 else f"{v:.0f}"

# ── c1 · anclajes de valoración ────────────────────────────────────────────
anc = sorted(cd["anclajes"], key=lambda a: a["valor"])
colores_pool = [C["rojo_oscuro"], C["terracota"], C["azul"], C["verde"], C["azul_acero"]]
fig, ax = plt.subplots(figsize=(9.2, 4.2 + 0.25*len(anc)))
y = np.arange(len(anc))
vals = [a["valor"] for a in anc]
ax.barh(y, vals, color=[colores_pool[i % len(colores_pool)] for i in range(len(anc))], height=0.58, zorder=3)
for i, a in enumerate(anc):
    ax.text(a["valor"] + max(vals)*0.015, i, MON + fmt(a["valor"]), va="center", fontsize=10,
            color=C["tinta"], fontweight="bold")
ax.axvline(precio, color=C["rojo"], lw=2.2, zorder=4)
ax.text(precio, len(anc) - 0.25, f"Precio hoy {MON}{fmt(precio)}", color=C["rojo"], fontsize=9.5,
        fontweight="bold", ha="center")
ax.set_yticks(y); ax.set_yticklabels([a["nombre"] for a in anc], fontsize=9.5)
ax.set_xlim(0, max(max(vals), precio) * 1.22); ax.invert_yaxis()
mos = cd["mos_pct"]
cs.deco(ax, "Los anclajes de valoración y el precio",
        f"MoS oficial del documento: {str(mos).replace('.', ',')}% · DCF propio r=9%, terminal=3%, owner earnings (FCF−SBC)",
        "Tesis-forja " + cd["ticker"] + " · templada por loop adversarial · " + cd.get("veredicto", ""), fig)
cs.save(fig, "c1_anclajes")

# ── c2 · mapa de zonas ─────────────────────────────────────────────────────
zonas = [(cd.get("zona_comprar_agresivo"), "COMPRAR AGRESIVO (MoS≥40% + 2 señales de extremo)", C["verde"], "-"),
         (cd.get("zona_comprar_inicial"), "COMPRAR INICIAL (MoS≥25% + candados resueltos)", C["azul_noche"], "-"),
         (cd.get("zona_banda_min"), "banda gatillo-doble (inferior)", C["azul_noche"], ":"),
         (cd.get("zona_banda_max"), "banda gatillo-doble (superior)", C["tinta"], ":"),
         (cd.get("zona_reanalisis"), "re-análisis intensivo", C["ocre"], "--")]
zonas = [(v, l, c, ls) for v, l, c, ls in zonas if v]
niveles = [v for v, *_ in zonas] + [precio] + [a["valor"] for a in anc]
lo, hi = min(niveles)*0.82, max(niveles)*1.12
fig, ax = plt.subplots(figsize=(9.2, 5.0))
ax.set_xlim(0, 10); ax.set_ylim(lo, hi)
for v, lbl, col, ls in zonas:
    ax.axhline(v, color=col, ls=ls, lw=1.6, zorder=4)
    ax.text(0.35, v + (hi-lo)*0.012, f"{MON}{fmt(v)} · {lbl}", fontsize=8.6, color=col, fontweight="bold", zorder=5)
ax.axhline(precio, color=C["rojo"], lw=2.4, zorder=5)
ax.text(0.35, precio + (hi-lo)*0.012, f"PRECIO HOY · {MON}{fmt(precio)}", fontsize=9.2, color=C["rojo"], fontweight="bold", zorder=6)
for a in anc:
    ax.axhline(a["valor"], color=C["gris"], ls="--", lw=1.0, zorder=3)
    ax.text(9.65, a["valor"] + (hi-lo)*0.012, a["nombre"], fontsize=7.8, color=C["gris"], ha="right", zorder=5)
ax.set_xticks([]); ax.set_ylabel(MON + " por acción", fontsize=9.5)
cs.deco(ax, "El mapa de zonas — dónde actuar y dónde esperar",
        "Zonas derivadas del conservador con los candados del estándar (MoS≥25%/40%); se re-derivan con cada resultado trimestral",
        "Tesis-forja " + cd["ticker"] + " · la agresión se gana con precio, no con entusiasmo", fig)
cs.save(fig, "c2_zonas")

# ── c3 · DCF inverso: lo que el precio exige vs. la referencia ────────────
g = cd["g_implicito_pct"]; ref = cd.get("crecimiento_referencia_pct")
fig, ax = plt.subplots(figsize=(9.2, 4.2))
sistema = [("Microsoft", 13.8), ("Visa", 11.8), ("Mastercard", 9.5), ("Intuit", 4.5)]
labels = [s[0] for s in sistema] + [cd["nombre_corto"]]
vals3 = [s[1] for s in sistema] + [g]
cols3 = [C["azul_acero"]]*4 + [C["rojo"]]
orden = np.argsort(vals3)[::-1]
labels = [labels[i] for i in orden]; vals3 = [vals3[i] for i in orden]; cols3 = [cols3[i] for i in orden]
bars = ax.bar(labels, vals3, 0.52, color=cols3, zorder=3)
for b, v in zip(bars, vals3):
    ax.text(b.get_x() + b.get_width()/2, v + 0.3, f"{v}%".replace(".", ","), ha="center",
            fontsize=10.5, fontweight="bold", color=C["tinta"])
if ref:
    ax.axhline(ref, color=C["verde"], lw=1.8, ls="--", zorder=2)
    ax.text(len(labels)-0.5, ref + 0.35, cd.get("crecimiento_referencia_nota", "referencia") + f": {str(ref).replace('.', ',')}%",
            fontsize=8.4, color=C["verde"], fontweight="bold", ha="right")
ax.set_ylim(0, max(vals3 + [ref or 0]) * 1.25)
ax.set_ylabel("Crecimiento implícito a 10 años (%, r=9%)", fontsize=9)
cs.deco(ax, "Lo que el precio de hoy ya exige — contra las demás tesis del sistema",
        "DCF inverso, mismo protocolo en todas: r=9%, terminal=3%, owner earnings = FCF−SBC",
        "Cálculo propio · sistema tesis-forja, jul-2026", fig)
cs.save(fig, "c3_dcf")

print("3 charts OK -> charts/ (" + cd["ticker"] + ")")
