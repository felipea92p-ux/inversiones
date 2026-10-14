# -*- coding: utf-8 -*-
"""Parametric chart generator for Ultra Tesis (13-company batch). One set per company.
Produces the core universal charts from a company data dict. House Economist palette."""
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import chart_style as CS
from paleta_qg import PALETA as P

RULES = ["R1","R2","R3","R4","R5","R6","R7","R8","R9","R10","R11"]
RULE_LABELS = {
 "R1":"Escala","R2":"Industria","R3":"Liderazgo","R4":"Moat","R5":"Crec.org",
 "R6":"Diversif","R7":"ROIC","R8":"Balance","R9":"Cuentas","R10":"Gestión","R11":"Impacto"}
RULE_MAX = {"R1":15,"R3":15,"R4":15}

def _pct_es(x, d=0):
    return f"{x:.{d}f}".replace(".", ",")

def radar_seilern(cd, outdir):
    """11-rule Seilern radar, normalized to each rule's max."""
    scores = cd["qg_scores"]
    vals = [scores[r]/RULE_MAX.get(r,10) for r in RULES]
    labels = [f"{RULE_LABELS[r]}" for r in RULES]
    ang = np.linspace(0, 2*np.pi, len(RULES), endpoint=False).tolist()
    vals2 = vals + vals[:1]; ang2 = ang + ang[:1]
    fig = plt.figure(figsize=(7.6, 5.4))
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.plot(ang2, vals2, color=P["azul"], lw=1.8)
    ax.fill(ang2, vals2, color=P["azul"], alpha=0.18)
    # reference ring at 0.7 (Alta convicción threshold-ish)
    ax.plot(ang2, [0.7]*len(ang2), color=P["rojo"], lw=0.9, ls="--", alpha=0.7)
    ax.set_xticks(ang); ax.set_xticklabels(labels, fontsize=8, color=P["tinta"])
    ax.set_yticks([0.25,0.5,0.75,1.0]); ax.set_yticklabels(["","50%","","100%"], fontsize=7, color=P["gris"])
    ax.set_ylim(0,1.0)
    ax.grid(color=P["gris_linea"], lw=0.6)
    CS.deco(ax, "Las once reglas Seilern", f"{cd['ticker']} · {_pct_es(cd['qg_score'],1)}/100 · tier {cd['qg_tier']}",
            "Sistema qg-seilern · re-verificado 10-jul-2026", fig=fig)
    fig.subplots_adjust(top=0.80, bottom=0.08, left=0.06, right=0.94)
    CS.save(fig, f"radar_{cd['ck']}", outdir)

def dcf_scenarios(cd, outdir):
    v = cd["val"]
    labels = ["Conservador","Base (PWFV)","Optimista"]
    vals = [v["scenario_bear"], v["scenario_base"], v["scenario_bull"]]
    cols = [P["rojo_oscuro"], P["azul"], P["verde"]]
    fig, ax = plt.subplots(figsize=(7.6,4.2))
    bars = ax.bar(labels, vals, color=cols, width=0.6)
    ax.axhline(v["price_today"], color=P["tinta"], lw=1.4, ls="-")
    ax.text(2.4, v["price_today"], f" HOY {v['price_ccy']} {_pct_es(v['price_today'],0)}",
            va="center", ha="left", fontsize=8, color=P["tinta"])
    ax.axhline(v["pwfv"], color=P["rojo"], lw=1.1, ls="--")
    for b,val in zip(bars, vals):
        ax.text(b.get_x()+b.get_width()/2, val, f"{_pct_es(val,0)}", ha="center", va="bottom", fontsize=8.5, color=P["tinta"])
    ax.set_ylabel(f"Valor por acción ({v['price_ccy']})")
    CS.deco(ax, "Valor intrínseco: tres escenarios", f"{cd['ticker']} · PWFV {v['price_ccy']} {_pct_es(v['pwfv'],0)} vs precio {_pct_es(v['price_today'],0)}",
            "DCF sobre owner earnings · val-mos · 10-jul-2026", fig=fig)
    fig.subplots_adjust(top=0.80, bottom=0.10)
    CS.save(fig, f"dcf_{cd['ck']}", outdir)

def zonas_precio(cd, outdir):
    v = cd["val"]
    pwfv = v["pwfv"]
    # zone boundaries as multiples of PWFV
    edges = [0.55, 0.70, 0.85, 1.10, 1.35, 1.65]
    znames = ["GANGA","OPORTUNIDAD","JUSTO","CARO","BURBUJA"]
    zcols = [P["verde"], P["azul_acero"], P["ocre"], P["terracota"], P["rojo_oscuro"]]
    fig, ax = plt.subplots(figsize=(7.6,2.6))
    for i in range(len(znames)):
        ax.axvspan(edges[i]*pwfv, edges[i+1]*pwfv, color=zcols[i], alpha=0.30)
        ax.text((edges[i]+edges[i+1])/2*pwfv, 0.62, znames[i], ha="center", va="center",
                fontsize=7.6, color=P["tinta"])
    ax.axvline(pwfv, color=P["rojo"], lw=1.2, ls="--")
    ax.text(pwfv, 0.9, "PWFV", ha="center", fontsize=8, color=P["rojo"])
    ax.axvline(v["price_today"], color=P["tinta"], lw=1.8)
    ax.text(v["price_today"], 0.12, f"HOY", ha="center", fontsize=8.5, color=P["tinta"], fontweight="bold")
    ax.set_ylim(0,1); ax.set_yticks([])
    ax.set_xlabel(f"Precio ({v['price_ccy']})")
    CS.deco(ax, "Mapa de zonas de precio", f"{cd['ticker']} · zona actual: {v['zone']} · {v['veredicto']}",
            "val-mos · zonas sobre PWFV · 10-jul-2026", fig=fig)
    fig.subplots_adjust(top=0.74, bottom=0.22)
    CS.save(fig, f"zonas_{cd['ck']}", outdir)

def make_all(cd, outdir="charts"):
    radar_seilern(cd, outdir)
    dcf_scenarios(cd, outdir)
    zonas_precio(cd, outdir)

if __name__ == "__main__":
    # smoke test with placeholder
    cd = {"ticker":"TEST","ck":"test","qg_score":75.2,"qg_tier":"Alta convicción",
          "qg_scores":{"R1":13,"R2":8,"R3":11,"R4":13,"R5":9,"R6":9,"R7":8,"R8":9,"R9":8,"R10":8,"R11":6},
          "val":{"price_ccy":"EUR","price_today":90.0,"pwfv":100.0,"scenario_bear":70,"scenario_base":100,
                 "scenario_bull":125,"zone":"OPORTUNIDAD","veredicto":"ACUMULAR EN ZONA"}}
    make_all(cd, "charts")
    print("charts done")
