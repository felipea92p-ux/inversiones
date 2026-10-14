# -*- coding: utf-8 -*-
"""Charts for the ULTRA QG deliverable (Economist palette, cream bg)."""
import sys, os, json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["text.parse_math"] = False

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))  # _ACTIVE
from paleta_qg import PALETA as P

data = json.load(open(os.path.join(HERE, "ultra_data.json"), encoding="utf-8"))

def flag_title(fig, title, sub="", ty=0.945, sy=0.905):
    fig.patches.append(plt.Rectangle((0.035, sy - 0.02), 0.012, (ty - sy) + 0.055,
                                     transform=fig.transFigure, color=P["rojo"], zorder=5))
    fig.text(0.06, ty, title, fontsize=13, fontweight="bold", color=P["tinta"],
             family="DejaVu Sans", va="center")
    if sub:
        fig.text(0.06, sy, sub, fontsize=8.5, style="italic", color=P["gris"], va="center")

def clean(ax):
    ax.set_facecolor(P["fondo"])
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(P["gris_linea"])
    ax.tick_params(colors=P["gris"], labelsize=8)
    ax.xaxis.grid(True, color=P["gris_linea"], lw=0.6, alpha=0.7)
    ax.set_axisbelow(True)

# ---------------------------------------------------------------- funnel
def chart_funnel():
    stages = [
        ("Screen mundial (jun-2026)", 600),
        ("Universo corrida /100 (2-jul)", 77),
        ("Candidatura ULTRA: top-30 + sweep 6", 36),
        ("Piso critico R1/R3/R4 sin compensacion", 21),
        ("Gates: 6/6 o una sola FALLA", 7),
        ("ULTRA-ALFA (6/6 + red team)", 1),
    ]
    fig, ax = plt.subplots(figsize=(7.4, 3.6), dpi=200)
    fig.patch.set_facecolor(P["fondo"])
    clean(ax)
    ax.xaxis.grid(False)
    ys = range(len(stages))[::-1]
    import math
    vals = [math.log10(v) + 0.35 for _, v in stages]
    cols = [P["azul_cielo"], P["azul_acero"], P["azul"], P["azul_noche"], P["ocre"], P["rojo"]]
    for y, (lab, v), w, c in zip(ys, stages, vals, cols):
        ax.barh(y, w, height=0.62, color=c)
        ax.text(w + 0.05, y, f"{v:,}".replace(",", "."), va="center", ha="left",
                fontsize=10, fontweight="bold", color=P["tinta"])
        ax.text(-0.05, y, lab, va="center", ha="right", fontsize=8.6, color=P["tinta"])
    ax.set_yticks([]); ax.set_xticks([])
    ax.set_xlim(-3.6, 3.6)
    fig.subplots_adjust(left=0.44, right=0.96, top=0.86, bottom=0.06)
    flag_title(fig, "El embudo ULTRA: de 600 a 1",
               "Cada corte es acumulativo; escala logaritmica. Solo CME sobrevive los 6 gates y el red team.")
    fig.savefig(os.path.join(HERE, "c_funnel_ultra.png"), facecolor=P["fondo"])
    plt.close(fig)

# ------------------------------------------------- score vs grado
def chart_score_grado():
    comp = sorted(data["companies"], key=lambda c: c["score"], reverse=True)
    GC = {"ULTRA_ALPHA": P["rojo"], "CASI_ULTRA": P["azul"], "FUERA": P["gris_linea"]}
    fig, ax = plt.subplots(figsize=(7.4, 5.6), dpi=200)
    fig.patch.set_facecolor(P["fondo"])
    clean(ax)
    ys = range(len(comp))[::-1]
    for y, c in zip(ys, comp):
        col = GC.get(c["grado"], P["gris_medio"])
        ax.barh(y, c["score"], height=0.68, color=col)
        nfall = len(c["fallas"])
        tag = "6/6" if nfall == 0 else f"{nfall} FALLA" + ("S" if nfall > 1 else "")
        tcol = P["tinta"] if c["grado"] != "FUERA" else P["gris"]
        ax.text(c["score"] + 0.4, y, f"{str(c['score']).replace('.', ',')}  ·  {tag}",
                va="center", fontsize=7.6, color=tcol,
                fontweight="bold" if c["grado"] == "ULTRA_ALPHA" else "normal")
        ax.text(-0.6, y, f"{c['name']}", va="center", ha="right", fontsize=8.2,
                color=P["tinta"], fontweight="bold" if c["grado"] != "FUERA" else "normal")
    ax.set_yticks([]); ax.set_xlim(0, 138)
    ax.set_xticks([0, 25, 50, 75, 85, 100])
    ax.axvline(85, color=P["ocre"], lw=1.0, ls=(0, (4, 3)), zorder=1)
    ax.text(85, len(comp) - 0.1, "Nucleo QG >= 85", fontsize=7, color=P["ocre"],
            ha="center", va="bottom", fontweight="bold")
    import matplotlib.patches as mp
    handles = [mp.Patch(color=P["rojo"], label="ULTRA-ALFA (indestructible)"),
               mp.Patch(color=P["azul"], label="CASI-ULTRA (1 falla)"),
               mp.Patch(color=P["gris_linea"], label="FUERA (2+ fallas)")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.045),
              ncol=3, fontsize=7.5, frameon=False, labelcolor=P["tinta"])
    fig.subplots_adjust(left=0.24, right=0.97, top=0.88, bottom=0.10)
    flag_title(fig, "Calidad no es indestructibilidad",
               "Score qg-seilern /100 (largo de la barra) vs veredicto ULTRA (color). Mastercard: 91,2 y FUERA.")
    fig.savefig(os.path.join(HERE, "c_score_grado.png"), facecolor=P["fondo"])
    plt.close(fig)

# ------------------------------------------------- gates fallados (que mata)
def chart_gate_kills():
    from collections import Counter
    cnt = Counter()
    for c in data["companies"]:
        for f in c["fallas"]:
            cnt[f] += 1
    labels = {
        "G1": "G1 Decada perdida",
        "G2": "G2 Ataque tecnologico activo",
        "G3": "G3 Irremplazabilidad sistemica",
        "G4": "G4 Golpe regulatorio",
        "G5": "G5 Punto unico de fallo",
        "G6": "G6 Test del tiempo (15 anios)",
    }
    order = [k for k, _ in cnt.most_common()]
    fig, ax = plt.subplots(figsize=(7.4, 2.9), dpi=200)
    fig.patch.set_facecolor(P["fondo"])
    clean(ax)
    ys = range(len(order))[::-1]
    for y, g in zip(ys, order):
        ax.barh(y, cnt[g], height=0.6, color=P["rojo_oscuro"] if g == "G3" else P["azul_acero"])
        ax.text(cnt[g] + 0.15, y, str(cnt[g]), va="center", fontsize=10,
                fontweight="bold", color=P["tinta"])
        ax.text(-0.25, y, labels[g], va="center", ha="right", fontsize=8.6, color=P["tinta"])
    ax.set_yticks([]); ax.set_xticks([])
    ax.set_xlim(-8.5, 18.5)
    fig.subplots_adjust(left=0.02, right=0.97, top=0.76, bottom=0.08)
    flag_title(fig, "Que gate mata a quien",
               "Numero de empresas (de 21) que fallan cada gate. G3 lo fallan 16 - todos los duopolios entre ellas.",
               ty=0.93, sy=0.845)
    fig.savefig(os.path.join(HERE, "c_gate_kills.png"), facecolor=P["fondo"])
    plt.close(fig)

chart_funnel()
chart_score_grado()
chart_gate_kills()
print("charts ok:", [f for f in os.listdir(HERE) if f.endswith(".png")])
