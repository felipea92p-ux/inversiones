# -*- coding: utf-8 -*-
"""Gráficos Ultra Tesis AMZN — importan dcf_amzn (fuente de verdad) y chart_style."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
from chart_style import deco, save, P
import dcf_amzn as D

plt.rcParams["text.parse_math"] = False

AZUL, NOCHE, ACERO, CIELO = P["azul"], P["azul_noche"], P["azul_acero"], P["azul_cielo"]
ROJO, ROJOSC, VERDE, OCRE, TERRA, GRIS = (P["rojo"], P["rojo_oscuro"], P["verde"],
    P["ocre"], P["terracota"], P["gris"])
TINTA, GLIN, GCLARO, PANEL = P["tinta"], P["gris_linea"], P["gris_claro"], P["panel"]
pctc = lambda x: D.es(x, 1) + "%"

# ── 01 · Radar 11 reglas ─────────────────────────────────────────────────
def c01():
    labs = [n for n, _ in D.RADAR]; vals = [v for _, v in D.RADAR]
    N = len(vals); ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    v = vals + vals[:1]; a = ang + ang[:1]
    fig = plt.figure(figsize=(7.6, 5.4)); ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.plot(a, v, color=NOCHE, lw=1.8); ax.fill(a, v, color=NOCHE, alpha=0.16)
    ax.plot(a, [8]*len(a), color=ROJO, lw=1.1, ls=(0, (4, 3)))
    for ai, vi in zip(ang, vals):
        col = VERDE if vi >= 9 else (ROJOSC if vi < 7 else NOCHE)
        ax.scatter(ai, vi, color=col, s=26, zorder=5)
        ax.text(ai, vi + 0.85, D.es(vi, 1), ha="center", va="center", fontsize=7.3, color=TINTA)
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=7.6, color=TINTA)
    ax.set_ylim(0, 10); ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Las 11 reglas Quality Growth",
         "Puntuación 0–10 por regla · anillo rojo = umbral de excelencia (8)",
         f"Fuente: qg-seilern + verificación adversarial (6-jul-2026). Raw {D.es(D.RAW_QG,2)}/125 → {D.es(D.SCORE_QG,1)}/100 · tier Alta convicción.",
         fig=fig)
    fig.subplots_adjust(top=0.74, bottom=0.08, left=0.06, right=0.94)
    save(fig, "01_radar")

# ── 02 · Segmentos: rev + flechas de margen ──────────────────────────────
def c02():
    labs = [s[0] for s in D.SEG]; rev = [s[1] for s in D.SEG]
    m0 = [s[2] for s in D.SEG]; m1 = [s[3] for s in D.SEG]
    x = np.arange(3)
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.bar(x, rev, 0.5, color=[AZUL, ACERO, ROJO])
    for i, v in enumerate(rev):
        ax.text(i, v + 2, f"US${D.es(v,1)}B", ha="center", fontsize=8, color=TINTA, fontweight="bold")
    ax2 = ax.twinx()
    for i, (a, b) in enumerate(zip(m0, m1)):
        ax2.annotate("", xy=(i, b), xytext=(i, a), arrowprops=dict(arrowstyle="->", color=GRIS, lw=1.1))
        ax2.scatter([i], [b], color=NOCHE, s=30, zorder=5)
        ax2.text(i + 0.13, b, f"{D.es(b,1)}%", va="center", fontsize=7.4, color=NOCHE, fontweight="bold")
        ax2.text(i + 0.13, a, f"{D.es(a,1)}%", va="center", fontsize=6.6, color=GRIS)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 125); ax.set_yticklabels([])
    ax2.set_ylim(0, 48); ax2.set_yticks([]); ax2.spines["top"].set_visible(False)
    deco(ax, "Tres segmentos: el retail expande, AWS es el beneficio",
         "Ingresos Q1'26 (barras, US$B) y margen operativo Q1'25→Q1'26 (flechas) · AWS = 59% del beneficio total",
         "Fuente: 8-K Q1 2026. HECHO. NA 6,3→7,9% · Intl 3,0→3,6% · AWS 37,7% con +28% de crecimiento.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "02_segmentos")

# ── 03 · Capex explota, FCF colapsa a negativo ───────────────────────────
def c03():
    yrs = D.YRS_FIN; x = np.arange(len(yrs))
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.bar(x, D.CAPEX, 0.55, color=ROJOSC, label="Capex (US$B)")
    for i, v in enumerate(D.CAPEX):
        ax.text(i, v + 3, f"{v:.0f}", ha="center", fontsize=7, color=ROJOSC)
    ax.bar(len(yrs), D.CAPEX_2026E, 0.55, color=ROJOSC, alpha=0.45)
    ax.text(len(yrs), D.CAPEX_2026E + 3, "~200\n(2026e)", ha="center", fontsize=6.6, color=ROJOSC)
    ax2 = ax.twinx()
    fcf_x = [3, 4, 5]; fcf_v = [38.2, 11.2, -2.5]
    ax2.plot(fcf_x, fcf_v, color=AZUL, lw=2.2, marker="o", ms=5, label="FCF (def. Amazon, US$B)")
    for xi, v in zip(fcf_x, fcf_v):
        ax2.text(xi, v + 4, f"{D.es(v,1)}", ha="center", fontsize=7.4, color=AZUL, fontweight="bold")
    ax2.axhline(0, color=GRIS, lw=0.8, ls=(0, (3, 2)))
    ax.set_xticks(list(x) + [len(yrs)]); ax.set_xticklabels(yrs + ["2026e"], fontsize=7.4)
    ax.set_ylim(0, 230); ax.set_yticklabels([])
    ax2.set_ylim(-25, 65); ax2.set_yticks([]); ax2.spines["top"].set_visible(False)
    ax.legend(fontsize=7.2, loc="upper left", frameon=False)
    ax2.legend(fontsize=7.2, loc="upper center", frameon=False)
    deco(ax, "El FCF ya no existe: colapsó de $38B a NEGATIVO en dos años",
         "Capex anual (barras) y flujo de caja libre (línea) · capex 2026e ~US$200B, la mayor inversión corporativa de la historia",
         "Fuente: 10-K FY2025 + 10-Q Q1'26. HECHO. FCF −71% en 2025 y −$2,5B TTM; el flujo operativo ($148B) sigue fuerte.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "03_capex_fcf")

# ── 04 · AWS: aceleración + margen TTM comprimiendo ──────────────────────
def c04():
    x = np.arange(len(D.AWS_Q))
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    ax.bar(x, D.AWS_YOY_SERIE, 0.55, color=AZUL)
    for i, v in enumerate(D.AWS_YOY_SERIE):
        ax.text(i, v + 0.6, f"+{v}%", ha="center", fontsize=8.2, color=AZUL, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(D.AWS_Q, fontsize=8)
    ax.set_ylim(0, 34); ax.set_yticklabels([])
    ax.text(0.15, 30, f"Backlog AWS US${D.AWS_BACKLOG}B (+93%)\n+ Anthropic &gt;$100B aparte\nmargen TTM 37,0% → 35,2% (comprime)".replace("&gt;", ">"),
            fontsize=7.4, color=NOCHE, va="top",
            bbox=dict(boxstyle="round,pad=0.5", fc=PANEL, ec=GLIN, lw=0.8))
    deco(ax, "AWS re-acelera: el mayor crecimiento en 15 trimestres",
         "Crecimiento interanual de AWS (%) · pero Azure (+40%) y Google Cloud (+63%) corren más rápido",
         "Fuente: 8-K + transcript Q1'26. HECHO. La aceleración es real; la cuota relativa aún se erosiona.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "04_aws")

# ── 05 · Owner earnings waterfall ────────────────────────────────────────
def c05():
    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    cfo = 148.5; maint = D.DYA_TTM; sbc = 19.8; oe = D.OE_TTM
    ax.bar(0, cfo, 0.6, color=NOCHE)
    ax.bar(1, maint, 0.6, bottom=cfo - maint, color=ROJOSC)
    ax.bar(2, sbc, 0.6, bottom=cfo - maint - sbc, color=ROJOSC)
    ax.bar(3, oe, 0.6, color=VERDE)
    ax.bar(5, -2.5, 0.6, color=CIELO)
    vals = [(0, cfo, f"{cfo:.0f}"), (1, cfo, f"−{maint:.0f}"), (2, cfo - maint, f"−{sbc:.0f}"),
            (3, oe, f"{oe:.0f}"), (5, 3, "−2,5")]
    for xi, top, txt in vals:
        ax.text(xi, top + 4, txt, ha="center", fontsize=8, color=TINTA,
                fontweight="bold" if xi in (0, 3, 5) else "normal")
    ax.axhline(0, color=GRIS, lw=0.8)
    ax.set_xticks([0, 1, 2, 3, 5])
    ax.set_xticklabels(["Flujo\noperativo", "Capex mant.\n(proxy D&A)", "SBC", "Owner\nearnings", "FCF\nreportado"], fontsize=7.2)
    ax.set_ylim(-16, 172); ax.set_yticklabels([])
    ax.annotate("~$81B de capex de crecimiento\nse come TODO el FCF", xy=(5, 2), xytext=(3.9, 120),
                fontsize=6.8, color=GRIS, style="italic", ha="center",
                arrowprops=dict(arrowstyle="->", color=GRIS, lw=0.9))
    deco(ax, "La caja del dueño: ~$58B — no los $91B del titular ni los −$2,5B del FCF",
         "De flujo operativo a owner earnings (US$B, TTM) · owner = CFO − mantenimiento (≈D&A) − SBC",
         "Fuente: 10-Q Q1'26. INFERENCIA. Rango honesto $55–75B; bajista $42B si el silicio se deprecia en 2-3 años.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "05_owner_earnings")

# ── 06 · Anthropic infla el neto ─────────────────────────────────────────
def c06():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["EPS Q1'26\nreportado", "Ganancia\nAnthropic", "EPS Q1'26\nnormalizado", "EPS Q1'25\n(comparable)"]
    vals = [D.EPS_Q1_REP, D.EPS_Q1_REP - D.EPS_Q1_NORM, D.EPS_Q1_NORM, 1.59]
    x = [0, 1, 2, 3]
    ax.bar(0, vals[0], 0.55, color=NOCHE)
    ax.bar(1, vals[1], 0.55, bottom=D.EPS_Q1_NORM, color=ROJOSC)
    ax.bar(2, vals[2], 0.55, color=VERDE)
    ax.bar(3, vals[3], 0.55, color=CIELO)
    for xi, (v, top) in enumerate(zip(["$2,78", "−$1,18", "$1,60", "$1,59"],
                                       [vals[0], vals[0], vals[2], vals[3]])):
        ax.text(xi, top + 0.07, v, ha="center", fontsize=8.4, color=TINTA,
                fontweight="bold" if xi in (0, 2) else "normal")
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.4)
    ax.set_ylim(0, 3.4); ax.set_yticklabels([])
    ax.text(2.5, 3.0, "el crecimiento real del EPS operativo:\n$1,59 → $1,60 = PLANO",
            ha="center", fontsize=7.2, color=ROJOSC, style="italic")
    deco(ax, "El beneficio que enseña el titular no es el que gana el negocio",
         "EPS diluido Q1 2026 (US$) · la ganancia no-caja y reversible de Anthropic ($16,8B) infla el neto",
         "Fuente: 10-Q Q1'26 (other income). HECHO. Más de la mitad del pre-tax del trimestre es no operativo.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "06_anthropic")

# ── 07 · DCF 3 escenarios: NI EL ALCISTA alcanza el precio ───────────────
def c07():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    labs = [f"Bajista\n({D.P_BEAR}%)", f"Base\n({D.P_BASE}%)", f"Alcista\n({D.P_BULL}%)"]
    vals = [D.V_BEAR, D.V_BASE, D.V_BULL]; cols = [ROJOSC, AZUL, VERDE]
    x = np.arange(3); ax.bar(x, vals, 0.5, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 5, f"US${v}", ha="center", fontsize=8.6, fontweight="bold", color=TINTA)
    ax.axhline(D.PRECIO, color=TINTA, lw=1.6)
    ax.text(0.02, D.PRECIO + 4, f"HOY US${D.es(D.PRECIO,0)} — por ENCIMA incluso del escenario alcista",
            fontsize=7.6, color=TINTA, fontweight="bold")
    ax.axhline(D.PWFV, color=ROJO, lw=1.4, ls=(0, (5, 3)))
    ax.text(2.55, D.PWFV + 4, f"PWFV US${D.PWFV}", va="bottom", ha="right", fontsize=7.6, color=ROJO)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 280); ax.set_yticklabels([])
    deco(ax, "La asimetría es negativa: ni el escenario alcista alcanza el precio",
         f"Valor por acción del DCF sobre owner earnings (US$) · WACC {D.es(D.WACC,1)}% · terminal {D.es(D.TERMINAL,1)}%",
         f"Fuente: modelo propio (val-mos). SUPUESTO. Ponderado US${D.V_POND}; alcista US${D.V_BULL} &lt; precio US${D.es(D.PRECIO,0)}.".replace("&lt;", "<"), fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "07_dcf")

# ── 08 · Mapa de zonas: HOY en BURBUJA ───────────────────────────────────
def c08():
    fig, ax = plt.subplots(figsize=(7.6, 2.8))
    lo, hi = 20, 300
    zonas = [("GANGA", lo, D.Z_GANGA, VERDE), ("OPORT.", D.Z_GANGA, D.Z_OPORT, ACERO),
             ("JUSTO", D.Z_OPORT, D.Z_JUSTO, OCRE), ("CARO", D.Z_JUSTO, D.Z_CARO, TERRA),
             ("BURBUJA", D.Z_CARO, hi, ROJOSC)]
    for nm, a, b, c in zonas:
        ax.barh(0, b - a, left=a, height=0.5, color=c, alpha=0.88)
        ax.text((a + b) / 2, 0, nm, ha="center", va="center", fontsize=7.0, color="white", fontweight="bold")
        ax.text(b, -0.42, f"${int(b)}", ha="center", fontsize=6.6, color=GRIS)
    ax.scatter([D.PRECIO], [0.42], marker="v", s=95, color=TINTA, zorder=5)
    ax.text(D.PRECIO, 0.62, f"HOY US${D.es(D.PRECIO,0)}", ha="center", fontsize=8, fontweight="bold", color=TINTA)
    ax.plot([D.PWFV, D.PWFV], [-0.25, 0.25], color=ROJO, lw=1.6, ls=(0, (4, 2)))
    ax.text(D.PWFV, -0.62, f"PWFV ${D.PWFV}", ha="center", fontsize=7, color=ROJO)
    ax.plot([D.GATILLO_T1, D.GATILLO_T1], [-0.25, 0.25], color=VERDE, lw=1.4)
    ax.text(D.GATILLO_T1, 0.62, f"gatillo ${D.GATILLO_T1}", ha="center", fontsize=6.8, color=VERDE)
    ax.set_xlim(lo, hi); ax.set_ylim(-0.8, 0.9); ax.axis("off")
    deco(ax, "Mapa operativo de precio",
         f"Zonas ancladas al PWFV-Valor US${D.PWFV} · HOY US${D.es(D.PRECIO,0)} = {D.ZONA_HOY} (prima +{D.es(D.PRIMA,0)}%)",
         f"Fuente: val-mos. MoS exigido {D.MOS_EXIG}% (candado HEROICO) → tramo pleno ≤US${D.GATILLO_PLENO}; GANGA ≤US${D.GATILLO_T1}.",
         fig=fig, flag_y=0.96)
    fig.subplots_adjust(top=0.64, bottom=0.06)
    save(fig, "08_zonas")

# ── 09 · Las tres lentes en desacuerdo ───────────────────────────────────
def c09():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    x = np.arange(3)
    act = [l[1] for l in D.LENTES]
    med = [l[2] if l[2] else 0 for l in D.LENTES]
    ax.bar(x - 0.18, act, 0.34, color=NOCHE, label="Hoy")
    ax.bar(x + 0.18, med, 0.34, color=CIELO, label="Mediana histórica")
    for i, (nm, a, m, lect) in enumerate(D.LENTES):
        ax.text(i - 0.18, a + 0.7, f"{D.es(a,1)}x", ha="center", fontsize=8, fontweight="bold", color=NOCHE)
        if m: ax.text(i + 0.18, m + 0.7, f"{D.es(m,1)}x", ha="center", fontsize=7.4, color=ACERO)
        col = VERDE if "barato" in lect else (OCRE if "razonable" in lect else ROJOSC)
        ax.text(i, -5.5, lect, ha="center", fontsize=7.0, color=col, style="italic")
    ax.set_xticks(x); ax.set_xticklabels([l[0] for l in D.LENTES], fontsize=8)
    ax.set_ylim(0, 52); ax.set_yticklabels([])
    ax.legend(fontsize=7.4, loc="upper left", frameon=False)
    deco(ax, "Tres lentes, tres respuestas — y solo una es la del dueño",
         "Múltiplos hoy vs mediana histórica · el EV/EBITDA «barato» ignora que el capex ya no es opcional",
         "Fuente: 10-Q + valueinvesting.io/GuruFocus. INFERENCIA. La lente del dueño (P/OE 45x) es la que manda en val-mos.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.14)
    save(fig, "09_multiplos")

# ── 10 · DCF inverso: expectativas HEROICAS ──────────────────────────────
def c10():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["CAGR revenue\nhistórico", "Conservador\npropio", "Implícito\nen el precio", "Consenso EPS\n(asume éxito pleno)"]
    vals = [D.G_CAGR, D.G_CONS, D.G_IMPL, D.G_GUIA]
    cols = [ACERO, OCRE, ROJO, GCLARO]
    x = np.arange(4); ax.bar(x, vals, 0.55, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.5, pctc(v), ha="center", fontsize=8, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.4)
    ax.set_ylim(0, 27); ax.set_yticklabels([])
    ax.annotate("el precio exige CASI EL DOBLE\nde la tasa histórica — HEROICO", xy=(2, D.G_IMPL), xytext=(0.9, 24),
                fontsize=7.0, color=ROJO, style="italic", ha="center",
                arrowprops=dict(arrowstyle="->", color=ROJO, lw=0.9))
    deco(ax, "El precio descuenta una década casi perfecta",
         "Crecimiento de owner earnings implícito en US$244,59 vs. referencias (%)",
         "Fuente: DCF inverso (val-mos). SUPUESTO. Expectativas HEROICAS → candado activo: solo se compra en GANGA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "10_dcf_inverso")

# ── 11 · El giro del balance: deuda ──────────────────────────────────────
def c11():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    x = [0, 1]
    ax.bar([i - 0.19 for i in x], D.DEUDA_LP, 0.34, color=ROJOSC, label="Deuda LP (US$B)")
    ax.bar([i + 0.19 for i in x], D.CAJA_NETA, 0.34, color=VERDE, label="Posición neta (liquidez − deuda)")
    for i, (d, c) in enumerate(zip(D.DEUDA_LP, D.CAJA_NETA)):
        ax.text(i - 0.19, d + 2.5, f"{D.es(d,1)}", ha="center", fontsize=8.2, color=ROJOSC, fontweight="bold")
        ax.text(i + 0.19, c + 2.5, f"+{D.es(c,1)}", ha="center", fontsize=8.2, color=VERDE, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(["dic-2025", "mar-2026\n(un trimestre después)"], fontsize=8)
    ax.set_ylim(0, 145); ax.set_yticklabels([])
    ax.legend(fontsize=7.4, loc="upper left", frameon=False)
    ax.text(1, 138, "+$53,4B de deuda nueva\nen un solo trimestre", ha="center", fontsize=7.4, color=ROJOSC, style="italic")
    deco(ax, "El giro histórico: Amazon ya no se autofinancia",
         "Deuda de largo plazo y posición neta (US$B) · el capex de IA se paga con bonos por primera vez",
         "Fuente: 10-Q Q1'26 (proceeds from long-term debt $53.441M). HECHO. Con leases LP ($90,8B), ya es deuda neta.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "11_deuda")

# ── 12 · Porter por segmento ─────────────────────────────────────────────
def c12():
    y = np.arange(len(D.PORTER_SEG))[::-1]
    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    for yi, (nm, v) in zip(y, D.PORTER_SEG):
        col = VERDE if v <= 11 else (OCRE if v <= 13 else ROJOSC)
        ax.barh(yi, v, 0.6, color=col)
        ax.text(v + 0.3, yi, f"{v}/25", va="center", fontsize=8, color=TINTA, fontweight="bold")
        ax.text(-0.3, yi, nm, va="center", ha="right", fontsize=7.8, color=TINTA)
    ax.axvline(D.PORTER_POND, color=NOCHE, lw=1.2, ls=(0, (4, 2)))
    ax.text(D.PORTER_POND + 0.2, -0.75, f"ponderado {D.es(D.PORTER_POND,2)}", fontsize=6.8, color=NOCHE)
    ax.set_xlim(0, 20); ax.set_ylim(-1, len(D.PORTER_SEG) - 0.4); ax.set_yticks([])
    ax.set_xticks([5, 10, 15]); ax.set_xticklabels(["5", "10", "15"], fontsize=7)
    deco(ax, "Cinco Fuerzas de Porter, foso por foso",
         "Score /25 por segmento (menor = mejor foso) · los cuatro mecanismos de moat están intactos o ensanchándose",
         "Fuente: análisis propio sobre 8-K/10-K. La logística pasó de centro de coste a foso más profundo (#1 carrier US).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11, left=0.30)
    save(fig, "12_porter")

# ── 13 · TAM por mercado ─────────────────────────────────────────────────
def c13():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    y = np.arange(len(D.MERCADOS))[::-1]
    LX = 4700 * 1.02
    for yi, (nm, tam, amzn, nota) in zip(y, D.MERCADOS):
        w = min(tam, 4500)
        ax.barh(yi, w, 0.62, color=CIELO, alpha=0.6)
        if amzn: ax.barh(yi, amzn, 0.62, color=AZUL)
        ax.text(-60, yi, nm, va="center", ha="right", fontsize=7.4, color=TINTA)
        ax.text(LX, yi, f"TAM ${tam}B · AMZN ${amzn}B · {nota}", va="center", fontsize=6.2, color=GRIS)
    ax.set_xlim(0, 8200); ax.set_ylim(-0.7, len(D.MERCADOS) - 0.3); ax.set_yticks([])
    ax.set_xticks([1500, 3000, 4500]); ax.set_xticklabels(["$1,5T", "$3T", "$4,5T"], fontsize=7)
    deco(ax, "Cuatro mercados gigantes, penetración de un dígito",
         "TAM 2026 (claro) vs ingreso AMZN (oscuro), US$B · el runway no es el problema; el precio de entrada sí",
         "Fuente: eMarketer/IDC/Grand View + 10-K. INFERENCIA. E-commerce ~9% del retail global: décadas de pista.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.09, left=0.185, right=0.995)
    save(fig, "13_tam")

# ── 14 · Radar de management ─────────────────────────────────────────────
def c14():
    labs = [n for n, _ in D.MGMT]; vals = [v for _, v in D.MGMT]
    N = len(vals); ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    v = vals + vals[:1]; a = ang + ang[:1]
    fig = plt.figure(figsize=(7.6, 5.0)); ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.plot(a, v, color=AZUL, lw=1.8); ax.fill(a, v, color=AZUL, alpha=0.16)
    for ai, vi in zip(ang, vals):
        ax.scatter(ai, vi, color=AZUL, s=26, zorder=5)
        ax.text(ai, vi + 0.3, D.es(vi, 1), ha="center", fontsize=7.4, color=TINTA)
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=6.8, color=TINTA)
    ax.set_ylim(0, 5); ax.set_yticks([1, 2, 3, 4, 5]); ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Gestión: 6 dimensiones",
         f"Puntuación 1–5 · total {D.es(D.MGMT_TOTAL,1)}/30 · compensación la más limpia de las megacaps; capex, la incógnita",
         "Fuente: DEF 14A 2026 + 10-K. Jassy operador de élite; Bezos 8,8% skin real; chair no independiente desde 1994.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10, left=0.10, right=0.90)
    save(fig, "14_mgmt")

# ── 15 · Matriz de riesgos numerada ──────────────────────────────────────
def c15():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.set_position([0.07, 0.14, 0.52, 0.62])
    for xi in range(1, 6):
        for yi in range(1, 6):
            sev = xi * yi
            col = VERDE if sev <= 6 else (OCRE if sev <= 12 else ROJOSC)
            ax.add_patch(Rectangle((xi - 0.5, yi - 0.5), 1, 1, color=col, alpha=0.14))
    for i in range(1, 6):
        ax.axhline(i - 0.5, color=GLIN, lw=0.5); ax.axvline(i - 0.5, color=GLIN, lw=0.5)
    from collections import defaultdict
    grupos = defaultdict(list)
    for idx, (nm, pr, im) in enumerate(D.RIESGOS, 1):
        grupos[(pr, im)].append(idx)
    for (pr, im), idxs in grupos.items():
        n = len(idxs)
        for k, idx in enumerate(idxs):
            dx = (k - (n - 1) / 2) * 0.26
            ax.scatter(pr + dx, im, s=150, color=NOCHE, zorder=5, edgecolors="white", linewidths=0.8)
            ax.text(pr + dx, im, str(idx), ha="center", va="center", fontsize=7.6, color="white", fontweight="bold", zorder=6)
    ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
    ax.set_xticklabels(["1", "2", "3", "4", "5"], fontsize=7); ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=7)
    ax.set_xlabel("Probabilidad", fontsize=8, color=GRIS); ax.set_ylabel("Impacto", fontsize=8, color=GRIS)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    ly = 0.68
    for idx, (nm, pr, im) in enumerate(D.RIESGOS, 1):
        sev = pr * im
        col = VERDE if sev <= 6 else (OCRE if sev <= 12 else ROJOSC)
        fig.text(0.63, ly, f"{idx}", fontsize=8, fontweight="bold", color="white", ha="center",
                 bbox=dict(boxstyle="circle,pad=0.22", fc=NOCHE, ec="none"))
        fig.text(0.66, ly + 0.012, nm, fontsize=6.4, color=TINTA, va="center")
        fig.text(0.66, ly - 0.028, f"prob {pr} × impacto {im} = {sev}", fontsize=6.1, color=col, va="center", style="italic")
        ly -= 0.108
    deco(ax, "Matriz de riesgos",
         "Probabilidad × impacto (1–5) · el dominante (1) es el capex sin ROIC probado; el (2), la reversión de Anthropic",
         "Fuente: análisis propio. Los riesgos 1 y 2 están CORRELACIONADOS: si la IA decepciona, caen juntos.", fig=fig)
    save(fig, "15_riesgos")

# ── 16 · Nueve inversores ────────────────────────────────────────────────
def c16():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    y = np.arange(len(D.INVERSORES))[::-1]
    for yi, (nm, conv, vd) in zip(y, D.INVERSORES):
        col = VERDE if vd == "BUY" else (NOCHE if vd == "HOLD" else OCRE)
        ax.barh(yi, conv, 0.6, color=col)
        ax.text(conv + 0.12, yi, f"{conv}/10 · {vd}", va="center", fontsize=7.2, color=TINTA)
        ax.text(-0.15, yi, nm, va="center", ha="right", fontsize=8, color=TINTA)
    ax.set_xlim(0, 11); ax.set_ylim(-0.6, len(D.INVERSORES) - 0.4)
    ax.set_yticks([]); ax.set_xticks([2, 4, 6, 8, 10]); ax.set_xticklabels(["2", "4", "6", "8", "10"], fontsize=7)
    ax.text(0.2, -1.15, "navy = mantener (si se posee) · ocre = pass · NADIE compra a este precio", fontsize=6.6, color=GRIS, style="italic")
    deco(ax, "Nueve leyendas opinan",
         "Convicción /10 · cero compradores a US$244: el precio, no el negocio, es el veto unánime",
         "Fuente: doctrina de cada inversor aplicada por el autor. INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.13, left=0.16)
    save(fig, "16_inversores")

# ── 17 · WACC ────────────────────────────────────────────────────────────
def c17():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    coe = D.COE_CAPM
    pasos = ["Tasa libre\nde riesgo", f"+ Prima ×\nbeta {D.es(D.BETA,2)}", "= Ke (CAPM)", "Ajuste por\ndeuda", "= WACC\nusado"]
    cols = [CIELO, ACERO, AZUL, OCRE, ROJO]
    ax.bar(0, D.RF, 0.6, color=cols[0])
    ax.bar(1, D.BETA * D.ERP, 0.6, bottom=D.RF, color=cols[1])
    ax.bar(2, coe, 0.6, color=cols[2])
    ax.bar(3, coe - D.WACC, 0.6, bottom=D.WACC, color=cols[3])
    ax.bar(4, D.WACC, 0.6, color=cols[4])
    labels = [pctc(D.RF), pctc(D.BETA * D.ERP), pctc(coe), f"−{D.es(coe-D.WACC,1)}", pctc(D.WACC)]
    tops = [D.RF, coe, coe, coe, D.WACC]
    for i in range(5):
        ax.text(i, tops[i] + 0.22, labels[i], ha="center", fontsize=7.4, color=TINTA,
                fontweight="bold" if i in (2, 4) else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels(pasos, fontsize=7.0)
    ax.set_ylim(0, 13.5); ax.set_yticklabels([])
    deco(ax, "El WACC, ladrillo a ladrillo — corregido por verificación adversarial",
         f"Coste de capital (%) · Ke CAPM {D.es(coe,1)}% (beta {D.es(D.BETA,2)}, ERP Damodaran {D.es(D.ERP,2)}%); WACC ponderado con deuda {D.es(D.WACC,1)}%",
         "Fuente: modelo propio (val-mos), verificado 9-jul-2026 contra GuruFocus/Damodaran/10Y UST. La v1.0 usaba 9,0% (escalón tier sin CAPM propio) — y aun así daba BURBUJA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "17_wacc")

# ── 18 · Sensibilidad ────────────────────────────────────────────────────
def c18():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    M = np.array(D.SENS)
    cmap = LinearSegmentedColormap.from_list("qg", [ROJOSC, GCLARO, NOCHE])
    ax.imshow(M, cmap=cmap, aspect="auto")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            base = (D.WACC_GRID[i] == D.WACC and D.GT_GRID[j] == D.TERMINAL)
            ax.text(j, i, f"{M[i, j]}", ha="center", va="center", fontsize=7.8,
                    color="white" if M[i, j] > 155 or M[i, j] < 120 else TINTA,
                    fontweight="bold" if base else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels([pctc(g) for g in D.GT_GRID], fontsize=7.2)
    ax.set_yticks(range(5)); ax.set_yticklabels([pctc(w) for w in D.WACC_GRID], fontsize=7.2)
    ax.set_xlabel("Crecimiento terminal", fontsize=7.8, color=GRIS)
    ax.set_ylabel("WACC", fontsize=7.8, color=GRIS)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    caida_sens = round((D.SENS_MAX / D.PRECIO - 1) * 100)
    deco(ax, "Ninguna celda alcanza el precio",
         f"Valor DCF base por acción (US$) según WACC × terminal · la MEJOR celda (US${D.SENS_MAX}) queda {caida_sens}% bajo US${D.es(D.PRECIO,0)}",
         "Fuente: modelo propio. SUPUESTO. Para justificar $244 hay que irse al escenario alcista Y bajar el WACC a la vez.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.10, right=0.98)
    save(fig, "18_sensibilidad")

# ── 19 · El flywheel (obligatorio, arquetipo plataforma) ─────────────────
def c19():
    fig, ax = plt.subplots(figsize=(7.6, 5.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    nodes = [
        (5.0, 8.4, "PRECIOS BAJOS\n+ velocidad Prime", AZUL),
        (8.2, 5.8, "TRÁFICO\nunits +15% (máx post-covid)", NOCHE),
        (6.6, 2.6, "VENDEDORES 3P\n60% de las unidades", ACERO),
        (3.4, 2.6, "SELECCIÓN\ncasi ilimitada", ACERO),
        (1.8, 5.8, "ESTRUCTURA DE\nCOSTES BAJA\n(logística #1 US)", NOCHE),
    ]
    for x, y, txt, col in nodes:
        ax.text(x, y, txt, ha="center", va="center", fontsize=7.6, color="white", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.55", fc=col, ec="none"))
    orden = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
    for a, b in orden:
        xa, ya = nodes[a][0], nodes[a][1]
        xb, yb = nodes[b][0], nodes[b][1]
        arr = FancyArrowPatch((xa, ya), (xb, yb), connectionstyle="arc3,rad=-0.25",
                              arrowstyle="-|>", mutation_scale=16, color=ROJO, lw=1.6,
                              shrinkA=32, shrinkB=32)
        ax.add_patch(arr)
    ax.text(5.0, 5.5, "PRIME\nretención", ha="center", va="center", fontsize=7.8, color="white", fontweight="bold",
            bbox=dict(boxstyle="circle,pad=0.5", fc=ROJO, ec="none"))
    ax.text(5.0, 0.7, "Monetizaciones del volante: publicidad US$72B TTM (+22%) · suscripción US$13,4B/trim (+12%) · AWS aparte",
            ha="center", fontsize=7.0, color=GRIS, style="italic")
    deco(ax, "El flywheel de Bezos, girando más rápido que nunca",
         "El volante clásico con sus KPIs de Q1 2026 · la publicidad convierte el giro en margen",
         "Fuente: 8-K Q1'26 (KPIs) + doctrina Amazon. El unit growth +15% prueba que gira por volumen, no por precio.", fig=fig)
    fig.subplots_adjust(top=0.80, bottom=0.04, left=0.02, right=0.98)
    save(fig, "19_flywheel")

# ── 20 · Early warning dashboard ─────────────────────────────────────────
def c20():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    filas = [
        ("Unit growth WW (flywheel)", "+15% (máx post-covid)", "< +8% sostenido", VERDE),
        ("AWS crecimiento", "+28% (acelerando)", "< +20% con capex alto", VERDE),
        ("Margen retail NA", "7,9% (+160 pb)", "cae 2 trim. seguidos", VERDE),
        ("Publicidad", "+22-24% estable", "< +15%", VERDE),
        ("FCF (definición Amazon)", "−$2,5B TTM", "sigue negativo en 2027", "rojo"),
        ("Deuda LP (financiación capex)", "+$53B en un trimestre", "otra duplicación sin plateau", OCRE),
        ("Carrying value Anthropic", "$32B (saltó de $14,8B)", "down-round → reversión", OCRE),
        ("Vida útil de servidores", "5-6 años (whipsaw 5→6→5)", "nuevo alargamiento", OCRE),
    ]
    ax.axis("off")
    y0 = 1.0; dh = 1.0 / (len(filas) + 1)
    ax.text(0.02, y0, "Indicador (VI.7)", fontsize=7.6, fontweight="bold", color=NOCHE, transform=ax.transAxes)
    ax.text(0.47, y0, "Estado hoy", fontsize=7.6, fontweight="bold", color=NOCHE, transform=ax.transAxes)
    ax.text(0.78, y0, "Umbral rojo", fontsize=7.6, fontweight="bold", color=NOCHE, transform=ax.transAxes)
    for i, (nm, est, umb, col) in enumerate(filas):
        y = y0 - (i + 1) * dh
        c = ROJOSC if col == "rojo" else col
        ax.add_patch(Rectangle((0.0, y - dh*0.42), 1.0, dh*0.84, transform=ax.transAxes,
                     color=PANEL if i % 2 else P["fondo"], zorder=0))
        ax.scatter(0.005, y, s=55, color=c, transform=ax.transAxes, zorder=3, clip_on=False)
        ax.text(0.03, y, nm, fontsize=6.9, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.47, y, est, fontsize=6.9, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.78, y, umb, fontsize=6.6, color=GRIS, va="center", transform=ax.transAxes)
    deco(ax, "Sistema de alerta temprana",
         "Semáforo · el negocio (verdes) está sano; las tensiones (rojo/ámbar) son de caja, deuda y contabilidad",
         "Fuente: KPIs primarios AMZN. El moat no es el problema; el precio y la conversión capex→caja, sí.",
         fig=fig, flag_y=0.97)
    fig.subplots_adjust(top=0.80, bottom=0.05, left=0.02, right=0.98)
    save(fig, "20_early_warning")

if __name__ == "__main__":
    fns = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10,
           c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]
    for fn in fns:
        fn(); print("ok", fn.__name__)
    print("charts done:", len(fns))
