# -*- coding: utf-8 -*-
"""Gráficos adicionales · Tesis-Forja Visa narrativa · c6-c9."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import chart_style as cs
from paleta_qg import PALETA as C

# ── c9 · Anatomía del swipe: ¿quién se lleva el 2,35%? ─────────────────────
fig, ax = plt.subplots(figsize=(9.2, 3.1))
# de cada 2,35% del swipe de crédito EE.UU.
seg = [("Interchange → banco EMISOR", 1.75, C["azul_noche"]),
       ("Margen del adquirente/procesador", 0.35, C["azul_acero"]),
       ("Fees de red → VISA (~25 pb netos)", 0.25, C["rojo"])]
left = 0
for nombre, val, col in seg:
    ax.barh(0, val, left=left, color=col, height=0.5, zorder=3, edgecolor=C["fondo"], linewidth=1.5)
    ax.text(left + val/2, 0, f"{val:.2f}%".replace(".", ","), va="center", ha="center",
            color=C["fondo"], fontsize=10, fontweight="bold")
    left += val
ax.set_xlim(0, 2.35); ax.set_ylim(-0.8, 0.8); ax.set_yticks([])
ax.set_xlabel("% de la compra (swipe medio de crédito EE.UU., ~2,35%)", fontsize=9)
for nombre, val, col in seg:
    pass
ax.legend([plt.Rectangle((0,0),1,1,color=c) for _,_,c in seg],
          [n for n,_,c in seg], loc="upper center", bbox_to_anchor=(0.5, -0.42),
          ncol=1, fontsize=8.6, frameon=False)
ax.annotate("De cada US$100 que gastas,\nVisa se lleva ~US$0,24", xy=(2.28, 0), xytext=(2.28, 0.55),
            fontsize=9, color=C["rojo"], fontweight="bold", ha="right",
            bbox=dict(boxstyle="round,pad=0.35", fc=C["panel"], ec=C["rojo"], lw=1.0))
cs.deco(ax, "La anatomía del swipe — el peaje que nadie ve", "El ~2,35% que paga el comercio NO es de Visa: la mayoría es interchange del banco emisor. Visa cobra un pellizco de red.",
        "10-K FY2025 (Visa fija el interchange «independientemente del ingreso que recibe») · Nilson/MPC 2024", fig)
cs.save(fig, "c9_takerate")

# ── c6 · DCF inverso: ¿qué crecimiento está ya en el precio? ───────────────
BASE = 19.7; MKT = 657.4; GT = 0.03; N = 10
def pv(g, r):
    s = sum(BASE*(1+g)**t/(1+r)**t for t in range(1, N+1))
    term = BASE*(1+g)**N*(1+GT)/(r-GT)/(1+r)**N
    return s + term
def implied_g(r):
    lo, hi = -0.02, 0.30
    for _ in range(80):
        mid = (lo+hi)/2
        if pv(mid, r) < MKT: lo = mid
        else: hi = mid
    return (lo+hi)/2
rs = np.linspace(0.075, 0.105, 25)
gs = [implied_g(r)*100 for r in rs]
fig, ax = plt.subplots(figsize=(9.2, 4.6))
ax.plot(rs*100, gs, color=C["rojo"], lw=2.6, zorder=5, label="Crecimiento de FCF exigido por el precio de hoy")
ax.axhspan(7.0, 8.5, color=C["verde"], alpha=0.16, zorder=1)
ax.axhspan(8.5, 12.0, color=C["ocre"], alpha=0.14, zorder=1)
ax.axhline(8.5, color=C["azul_noche"], lw=1.3, ls="--", zorder=3)
ax.text(7.55, 8.7, "Escenario CONSERVADOR: +8,5%", fontsize=8.6, color=C["azul_noche"])
ax.axhline(12.0, color=C["verde"], lw=1.3, ls="--", zorder=3)
ax.text(7.55, 12.2, "Nuestro escenario ALCISTA: +12%", fontsize=8.6, color=C["verde"])
g9 = implied_g(0.09)*100
ax.scatter([9.0], [g9], s=90, color=C["rojo"], zorder=6)
ax.annotate(f"A r=9% el precio\nexige +{g9:.1f}%".replace(".", ","), xy=(9.0, g9), xytext=(9.35, g9-2.2),
            fontsize=9, color=C["rojo"], fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=C["rojo"]))
ax.set_xlabel("Tasa de descuento (r, %)", fontsize=9)
ax.set_ylabel("Crecimiento de FCF a 10 años implícito (%)", fontsize=9)
ax.set_xlim(7.4, 10.6); ax.set_ylim(5, 16)
ax.legend(loc="upper left", fontsize=8.6, frameon=False)
cs.deco(ax, "El DCF inverso — la pregunta correcta", "No «¿cuánto vale?» sino «¿qué crecimiento ya está en el precio?». Y lo que está, cae pegado a nuestro propio alcista.",
        "DCF inverso reproducible sobre base honesta de owner earnings US$19,7B, terminal 3% · calculado 10-jul-2026", fig)
cs.save(fig, "c6_reverse_dcf")

# ── c7 · El consejo de las 9 escuelas ─────────────────────────────────────
escuelas = [("Seilern / Terry Smith", 8.5, "COMPRAR"),
            ("Buffett-Munger", 8.0, "PARCIAL"),
            ("Philip Fisher", 8.0, "PARCIAL"),
            ("Cuant / Kelly", 6.5, "PARCIAL"),
            ("Howard Marks", 8.0, "VIGILAR"),
            ("Peter Lynch", 7.0, "VIGILAR"),
            ("Benjamin Graham", 9.0, "PASO"),
            ("John Templeton", 8.0, "PASO"),
            ("John Bogle", 8.0, "PASO")]
colmap = {"COMPRAR": C["verde"], "PARCIAL": C["azul_acero"], "VIGILAR": C["ocre"], "PASO": C["rojo_oscuro"]}
fig, ax = plt.subplots(figsize=(9.2, 5.0))
y = np.arange(len(escuelas))[::-1]
for yi, (n, conv, voto) in zip(y, escuelas):
    ax.barh(yi, conv, color=colmap[voto], height=0.6, zorder=3)
    ax.text(conv+0.12, yi, f"{voto} · {str(conv).replace('.',',')}", va="center", fontsize=8.8,
            color=C["tinta"], fontweight="bold")
ax.set_yticks(y); ax.set_yticklabels([n for n,_,_ in escuelas], fontsize=9.2)
ax.set_xlim(0, 11.5); ax.set_xlabel("Convicción en su propio marco (0-10)", fontsize=9)
handles = [plt.Rectangle((0,0),1,1,color=colmap[k]) for k in ["COMPRAR","PARCIAL","VIGILAR","PASO"]]
ax.legend(handles, ["Comprar ya","Media posición","Vigilar","Pasar"], loc="lower right", fontsize=8.4, frameon=False, ncol=2)
cs.deco(ax, "El consejo de los maestros — una fractura sana", "Cuatro comprarían algo, dos vigilarían, tres pasarían. Que un panel brillante se divida es información, no ruido.",
        "Panel adversarial de 9 escuelas de inversión sobre la tesis de Visa · 10-jul-2026", fig)
cs.save(fig, "c7_panel")

# ── c8 · El foso por capas ────────────────────────────────────────────────
capas = [("Red de dos caras\n(credenciales × aceptación)", 50, "Routing por decreto (DOJ, CCCA)", C["azul_noche"]),
         ("Aceptación universal\n(la marca, la confianza)", 20, "Fin del honor-all-cards (MDL)", C["azul"]),
         ("Lock-in de emisores\n(la capa CARA: incentives)", 15, "Capital One-Discover; R1", C["ocre"]),
         ("VAS + Visa Direct\n(switching costs compuestos)", 15, "Ejecución; competencia", C["verde"])]
fig, ax = plt.subplots(figsize=(9.2, 3.4))
left = 0
for nombre, pct, amenaza, col in capas:
    ax.barh(0, pct, left=left, color=col, height=0.42, zorder=3, edgecolor=C["fondo"], linewidth=2)
    ax.text(left+pct/2, 0, f"{pct}%", va="center", ha="center", color=C["fondo"], fontsize=11, fontweight="bold")
    ax.text(left+pct/2, 0.42, nombre, va="bottom", ha="center", color=C["tinta"], fontsize=7.8, fontweight="bold")
    ax.text(left+pct/2, -0.42, "▲ "+amenaza, va="top", ha="center", color=C["rojo_oscuro"], fontsize=7.2)
    left += pct
ax.set_xlim(0, 100); ax.set_ylim(-1.1, 1.1); ax.set_yticks([]); ax.set_xticks([])
cs.deco(ax, "El foso no es un bloque: son cuatro capas con vidas distintas", "Cada capa defiende una parte del valor y la ataca una amenaza distinta. Tratar el foso como un número único es no entenderlo.",
        "Reparto aproximado de valor defendido · cada capa con su amenaza específica y su gatillo de vigilancia", fig)
cs.save(fig, "c8_moat_capas")

print("4 charts extra OK → charts/ (c6, c7, c8, c9)")
