# -*- coding: utf-8 -*-
"""Gráficos Ultra Tesis GOOGL — importan dcf_googl (fuente de verdad) y chart_style."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap
from chart_style import deco, save, P
import dcf_googl as D

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
        col = VERDE if vi >= 8 else (ROJOSC if vi < 5 else NOCHE)
        ax.scatter(ai, vi, color=col, s=26, zorder=5)
        ax.text(ai, vi + 0.85, D.es(vi, 1), ha="center", va="center", fontsize=7.3, color=TINTA)
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=7.6, color=TINTA)
    ax.set_ylim(0, 10); ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Las 11 reglas Quality Growth",
         "Puntuación 0–10 por regla · anillo rojo = umbral de excelencia (8)",
         f"Fuente: qg-seilern + verificación adversarial (6-jul-2026). Raw {D.es(D.RAW_QG,2)}/125 → {D.es(D.SCORE_QG,1)}/100 · tier Calidad sólida.",
         fig=fig)
    fig.subplots_adjust(top=0.74, bottom=0.08, left=0.06, right=0.94)
    save(fig, "01_radar")

# ── 02 · Segmentos: rev + OI ──────────────────────────────────────────────
def c02():
    labs = [s[0] for s in D.SEG]; rev = [s[1]/1000 for s in D.SEG]
    oi0 = [s[2]/1000 for s in D.SEG]; oi1 = [s[3]/1000 for s in D.SEG]
    x = np.arange(3)
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.bar(x, rev, 0.5, color=[AZUL, ROJO, ACERO])
    for i, v in enumerate(rev):
        ax.text(i, v + 1, f"US${D.es(v,1)}B", ha="center", fontsize=8, color=TINTA, fontweight="bold")
    ax2 = ax.twinx()
    for i, (a, b) in enumerate(zip(oi0, oi1)):
        ax2.annotate("", xy=(i, b), xytext=(i, a), arrowprops=dict(arrowstyle="->", color=GRIS, lw=1.1))
        ax2.scatter([i], [b], color=NOCHE, s=30, zorder=5)
        ax2.text(i + 0.13, b, f"US${D.es(b,1)}B", va="center", fontsize=7.2, color=NOCHE, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.6)
    ax.set_ylim(0, 105); ax.set_yticklabels([])
    ax2.set_ylim(-3, 45); ax2.set_yticks([]); ax2.spines["top"].set_visible(False)
    deco(ax, "Tres negocios: Cloud ya es rentable, Other Bets todavía sangra",
         "Ingresos Q1'26 (barras, US$B) y beneficio operativo Q1'25→Q1'26 (flechas)",
         "Fuente: 8-K Q1 2026. HECHO. Cloud margen 17,8%→32,9%; Other Bets pérdida −$1,2B→−$2,1B.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "02_segmentos")

# ── 03 · Capex explota vs D&A ─────────────────────────────────────────────
def c03():
    yrs = D.YRS_FIN; x = np.arange(len(yrs))
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.bar(x, D.CAPEX, 0.55, color=ROJOSC, label="Capex (US$B)")
    for i, v in enumerate(D.CAPEX):
        ax.text(i, v + 3, f"{v:.0f}", ha="center", fontsize=7, color=ROJOSC)
    ax.bar(len(yrs), D.CAPEX_2026E, 0.55, color=ROJOSC, alpha=0.45)
    ax.text(len(yrs), D.CAPEX_2026E + 3, "~185\n(2026e)", ha="center", fontsize=6.6, color=ROJOSC)
    ax2 = ax.twinx()
    fcf_v = D.FCF
    ax2.plot(x, fcf_v, color=AZUL, lw=2.2, marker="o", ms=5, label="FCF (US$B)")
    for xi, v in zip(x, fcf_v):
        ax2.text(xi, v + 3, f"{v:.0f}", ha="center", fontsize=7.2, color=AZUL, fontweight="bold")
    ax.set_xticks(list(x) + [len(yrs)]); ax.set_xticklabels(yrs + ["2026e"], fontsize=7.4)
    ax.set_ylim(0, 220); ax.set_yticklabels([])
    ax2.set_ylim(0, 90); ax2.set_yticks([]); ax2.spines["top"].set_visible(False)
    ax.legend(fontsize=7.2, loc="upper left", frameon=False)
    ax2.legend(fontsize=7.2, loc="upper center", frameon=False)
    deco(ax, "El capex se duplica; el FCF empieza a resentirse",
         "Capex anual (barras) y flujo de caja libre (línea) · capex 2026e ~US$185B, +2x sobre 2025",
         "Fuente: 10-K FY2025 + 8-K Q1'26. HECHO. Capex FY25 ($91,4B) = 4,3x la D&A ($21,1B): la brecha es crecimiento puro.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "03_capex_fcf")

# ── 04 · Cloud: aceleración + margen ──────────────────────────────────────
def c04():
    x = np.arange(len(D.SEARCH_YOY_SERIE))
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    ax.bar(x, D.CLOUD_GROWTH, 0.55, color=AZUL)
    for i, v in enumerate(D.CLOUD_GROWTH):
        ax.text(i, v + 1.5, f"+{v}%", ha="center", fontsize=8.2, color=AZUL, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(D.SEARCH_YOY_SERIE, fontsize=8)
    ax.set_ylim(0, 74); ax.set_yticklabels([])
    ax.text(0.1, 66, f"Backlog Cloud US${D.es(D.CLOUD_RPO,1)}B (~doblado QoQ)\nMargen operativo 17,8% → 32,9%\nAWS +28% · Azure +40% · GCP +63%",
            fontsize=7.4, color=NOCHE, va="top",
            bbox=dict(boxstyle="round,pad=0.5", fc=PANEL, ec=GLIN, lw=0.8))
    deco(ax, "Google Cloud: el mejor momentum de los tres hiperescaladores",
         "Crecimiento interanual de Google Cloud (%) · #3 en cuota, #1 en velocidad",
         "Fuente: 8-K + transcripts Q1'26. HECHO. Es la evidencia más limpia de que el capex de IA se convierte en demanda contratada.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "04_cloud")

# ── 05 · CTR colapsa pero Search revenue no (la paradoja) ────────────────
def c05():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    labs = ["CTR posición 1\n(sin AI Overview, 2023)", "CTR posición 1\n(con AI Overview, 2025)"]
    vals = [D.CTR_POS1_2023, D.CTR_POS1_2025]
    ax.bar([0, 1], vals, 0.45, color=[ACERO, ROJOSC])
    for i, v in enumerate(vals):
        ax.text(i, v + 0.15, f"{D.es(v,1)}%", ha="center", fontsize=9, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 9); ax.set_yticklabels([])
    ax.annotate("−58%", xy=(1, D.CTR_POS1_2025 + 0.6), fontsize=11, color=ROJOSC, fontweight="bold", ha="center")
    ax.text(0.5, 7.5, f"Pero Search &amp; other creció +{D.es(D.SEARCH_GROWTH[-1],1)}% (Q1'26)\npaid clicks +{D.PAID_CLICKS_YOY}% · CPC +{D.CPC_YOY}%\nzero-click ya es {D.es(D.ZERO_CLICK_PCT,0)}% de las búsquedas".replace("&amp;", "&"),
            ha="center", fontsize=7.4, color=NOCHE,
            bbox=dict(boxstyle="round,pad=0.5", fc=PANEL, ec=GLIN, lw=0.8))
    deco(ax, "La paradoja central: el clic muere, el ingreso no (todavía)",
         "CTR (click-through rate) en la primera posición de resultados (%) · estudio Ahrefs, 300.000 keywords",
         "Fuente: Ahrefs feb-2026 (terceros) + 8-K Q1'26 (HECHO). El test decisivo de trampas.md: ingresos y margen siguen creciendo.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "05_ctr_paradoja")

# ── 06 · Márgenes ─────────────────────────────────────────────────────────
def c06():
    yrs = D.YRS_FIN; x = np.arange(len(yrs))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    fcf_mgn = [round(f/r*100, 1) for f, r in zip(D.FCF, D.REVENUE)]
    ax.plot(x, D.OP_MGN, color=AZUL, lw=2.0, marker="o", ms=3.4, label="Operativo")
    ax.plot(x, fcf_mgn, color=ROJO, lw=2.0, marker="s", ms=3.4, label="FCF")
    for i, v in enumerate(D.OP_MGN):
        ax.text(i, v + 1.4, f"{D.es(v,1)}%", fontsize=6.6, color=AZUL, ha="center")
    for i, v in enumerate(fcf_mgn):
        ax.text(i, v - 3.0, f"{D.es(v,1)}%", fontsize=6.6, color=ROJO, ha="center")
    ax.set_xticks(x); ax.set_xticklabels(yrs, fontsize=8)
    ax.set_ylim(0, 45); ax.set_yticklabels([])
    ax.legend(fontsize=7.4, loc="lower left", frameon=False)
    deco(ax, "Margen operativo en récord; el FCF empieza a ceder",
         "Margen operativo / margen de FCF (%) FY21→TTM · el apalancamiento operativo sigue firme, la caja ya no tanto",
         "Fuente: 10-K FY2025 + 8-K. HECHO. Margen operativo 30,6%→32,7% TTM; FCF margin 26%→15,2% TTM.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "06_margenes")

# ── 07 · DCF 3 escenarios ─────────────────────────────────────────────────
def c07():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    labs = [f"Conservador\n({D.P_BEAR}%)", f"Base\n({D.P_BASE}%)", f"Optimista\n({D.P_BULL}%)"]
    vals = [D.V_BEAR, D.V_BASE, D.V_BULL]; cols = [ROJOSC, AZUL, VERDE]
    x = np.arange(3); ax.bar(x, vals, 0.5, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 8, f"US${v}", ha="center", fontsize=8.6, fontweight="bold", color=TINTA)
    ax.axhline(D.PRECIO, color=TINTA, lw=1.6)
    ax.text(0.02, D.PRECIO + 6, f"HOY US${D.es(D.PRECIO,0)} — zona {D.ZONA_HOY} (85,6% del PWFV)",
            fontsize=7.6, color=TINTA, fontweight="bold")
    ax.axhline(D.PWFV, color=ROJO, lw=1.4, ls=(0, (5, 3)))
    ax.text(2.55, D.PWFV + 6, f"PWFV US${D.PWFV}", va="bottom", ha="right", fontsize=7.6, color=ROJO)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 620); ax.set_yticklabels([])
    deco(ax, "Cerca del valor — pero no lo suficiente para su tier",
         f"Valor por acción del DCF sobre owner earnings (US$) · WACC {D.es(D.WACC,1)}% · terminal {D.es(D.TERMINAL,1)}%",
         f"Fuente: modelo propio (val-mos). SUPUESTO. Ponderado US${D.V_POND}; MoS actual {D.es(D.MOS_ACTUAL,1)}%.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "07_dcf")

# ── 08 · Mapa de zonas — GOOGL en JUSTO ───────────────────────────────────
def c08():
    fig, ax = plt.subplots(figsize=(7.6, 2.8))
    lo, hi = 250, 630
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
    ax.plot([D.GATILLO_OPORT, D.GATILLO_OPORT], [-0.25, 0.25], color=VERDE, lw=1.4)
    ax.text(D.GATILLO_OPORT, 0.62, f"gatillo ${D.GATILLO_OPORT}", ha="center", fontsize=6.8, color=VERDE)
    ax.set_xlim(lo, hi); ax.set_ylim(-0.8, 0.9); ax.axis("off")
    deco(ax, "Mapa operativo de precio",
         f"Zonas ancladas al PWFV US${D.PWFV} · HOY US${D.es(D.PRECIO,0)} = {D.ZONA_HOY}, fuera del rango comprable de su tier",
         f"Fuente: val-mos v3. El tier Calidad sólida exige zona Ganga/Oportunidad (≤US${D.GATILLO_OPORT}) — es un gate, no solo un MoS.",
         fig=fig, flag_y=0.96)
    fig.subplots_adjust(top=0.64, bottom=0.06)
    save(fig, "08_zonas")

# ── 09 · El candado duro: múltiplo vs techo del tier ─────────────────────
def c09():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    labs = ["Techo del tier\n(Calidad sólida)", "Múltiplo normalizado\n(owner earnings)", "Múltiplo FCF\nreal (deprimido)"]
    vals = [D.TECHO_MULT_TIER, D.MULT_NORMALIZADO, D.MULT_FCF_REAL]
    cols = [VERDE, OCRE, ROJOSC]
    x = np.arange(3); ax.bar(x, vals, 0.5, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 1.5, f"{D.es(v,1)}x", ha="center", fontsize=9, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.8)
    ax.set_ylim(0, 78); ax.set_yticklabels([])
    ax.annotate("1,5x - 2,8x\nsobre el techo", xy=(1.5, 45), fontsize=7.4, color=ROJOSC, ha="center", style="italic")
    deco(ax, "El candado duro: violado bajo cualquier lectura",
         "Múltiplo pagado hoy sobre owner earnings vs. el techo de múltiplo del tier de GOOGL (25x)",
         "Fuente: val-mos v3 (candado anti-sobrepago, sin excepción de tier). El techo del TIER manda sobre el genérico 30-40x.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "09_candado_duro")

# ── 10 · DCF inverso ──────────────────────────────────────────────────────
def c10():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["Conservador\npropio", "Implícito\nen el precio", "CAGR revenue\n(histórico)", "Crecimiento\nreciente (Cloud/cons.)"]
    vals = [D.G_CONS, D.G_IMPL, D.G_CAGR, D.G_GUIA]
    cols = [OCRE, ROJO, ACERO, GCLARO]
    x = np.arange(4); ax.bar(x, vals, 0.55, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.5, pctc(v), ha="center", fontsize=8, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.4)
    ax.set_ylim(0, 26); ax.set_yticklabels([])
    deco(ax, "Expectativas razonables, ni heroicas ni regaladas",
         "Crecimiento de owner earnings implícito en US$366 vs. referencias (%)",
         f"Fuente: DCF inverso (val-mos). SUPUESTO. Clasificación: {D.DCF_CLASE} — no activa el candado de expectativas heroicas.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "10_dcf_inverso")

# ── 11 · WACC ─────────────────────────────────────────────────────────────
def c11():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    coe = D.COE_CAPM
    pasos = ["Tasa libre\nde riesgo", f"+ Prima ×\nbeta {D.es(D.BETA,2)}", "= CAPM", "Escalón tier\n(val-mos)", "= WACC\nusado"]
    cols = [CIELO, ACERO, AZUL, OCRE, ROJO]
    ax.bar(0, D.RF, 0.6, color=cols[0])
    ax.bar(1, D.BETA * D.ERP, 0.6, bottom=D.RF, color=cols[1])
    ax.bar(2, coe, 0.6, color=cols[2])
    if coe > D.WACC:
        ax.bar(3, coe - D.WACC, 0.6, bottom=D.WACC, color=cols[3])
    ax.bar(4, D.WACC, 0.6, color=cols[4])
    labels = [pctc(D.RF), pctc(D.BETA * D.ERP), pctc(coe), f"−{D.es(max(coe-D.WACC,0),1)}", pctc(D.WACC)]
    tops = [D.RF, coe, coe, coe, D.WACC]
    for i in range(5):
        ax.text(i, tops[i] + 0.22, labels[i], ha="center", fontsize=7.4, color=TINTA,
                fontweight="bold" if i in (2, 4) else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels(pasos, fontsize=7.0)
    ax.set_ylim(0, 13); ax.set_yticklabels([])
    deco(ax, "El WACC, ladrillo a ladrillo",
         f"Coste de capital (%) · CAPM ~{D.es(coe,1)}% (beta {D.es(D.BETA,2)}, ajustado por apalancamiento nuevo), usado {D.es(D.WACC,1)}%",
         "Fuente: modelo propio (val-mos). El cupón del 6,25% de las preferentes convertibles de jun-2026 confirma un costo marginal ya no trivial.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "11_wacc")

# ── 12 · Sensibilidad ─────────────────────────────────────────────────────
def c12():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    M = np.array(D.SENS)
    cmap = LinearSegmentedColormap.from_list("qg", [ROJOSC, GCLARO, NOCHE])
    ax.imshow(M, cmap=cmap, aspect="auto")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            base = (D.WACC_GRID[i] == D.WACC and D.GT_GRID[j] == D.TERMINAL)
            ax.text(j, i, f"{M[i, j]}", ha="center", va="center", fontsize=7.8,
                    color="white" if M[i, j] > 490 or M[i, j] < 400 else TINTA,
                    fontweight="bold" if base else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels([pctc(g) for g in D.GT_GRID], fontsize=7.2)
    ax.set_yticks(range(5)); ax.set_yticklabels([pctc(w) for w in D.WACC_GRID], fontsize=7.2)
    ax.set_xlabel("Crecimiento terminal", fontsize=7.8, color=GRIS)
    ax.set_ylabel("WACC", fontsize=7.8, color=GRIS)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    deco(ax, "El valor bajo estrés — ninguna celda cruza a Ganga",
         "Valor DCF base por acción (US$) según WACC × terminal · negrita = caso central",
         f"Fuente: modelo propio. SUPUESTO. Rango US${D.SENS[-1][0]}-{D.SENS_MAX}: siempre por encima del gatillo de Oportunidad (${D.GATILLO_OPORT}).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.10, right=0.98)
    save(fig, "12_sensibilidad")

# ── 13 · Porter por segmento ──────────────────────────────────────────────
def c13():
    y = np.arange(len(D.PORTER_SEG))[::-1]
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    for yi, (nm, v) in zip(y, D.PORTER_SEG):
        col = VERDE if v <= 11 else (OCRE if v <= 13 else ROJOSC)
        ax.barh(yi, v, 0.55, color=col)
        ax.text(v + 0.3, yi, f"{v}/25", va="center", fontsize=8, color=TINTA, fontweight="bold")
        ax.text(-0.3, yi, nm, va="center", ha="right", fontsize=8.2, color=TINTA)
    ax.axvline(D.PORTER_POND, color=NOCHE, lw=1.2, ls=(0, (4, 2)))
    ax.text(D.PORTER_POND + 0.2, -0.75, f"ponderado {D.es(D.PORTER_POND,1)}", fontsize=6.8, color=NOCHE)
    ax.set_xlim(0, 18); ax.set_ylim(-1, len(D.PORTER_SEG) - 0.4); ax.set_yticks([])
    ax.set_xticks([5, 10, 15]); ax.set_xticklabels(["5", "10", "15"], fontsize=7)
    deco(ax, "Cinco Fuerzas de Porter, por negocio",
         "Score /25 (menor = mejor foso) · Cloud es el foso más ancho; Search/Ads y YouTube, disputados por primera vez en 20 años",
         "Fuente: análisis propio sobre 10-K/8-K. La IA generativa y el antitrust atacan simultáneamente los mismos dos pilares.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11, left=0.32)
    save(fig, "13_porter")

# ── 14 · TAM por mercado ──────────────────────────────────────────────────
def c14():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    y = np.arange(len(D.MERCADOS))[::-1]
    LX = 720
    for yi, (nm, tam, gg, nota) in zip(y, D.MERCADOS):
        w = min(tam, 700)
        ax.barh(yi, w, 0.6, color=CIELO, alpha=0.6)
        ax.barh(yi, gg, 0.6, color=AZUL)
        ax.text(-15, yi, nm, va="center", ha="right", fontsize=7.4, color=TINTA)
        ax.text(LX, yi, f"TAM ${tam}B · GOOGL ${gg}B · {nota}", va="center", fontsize=6.3, color=GRIS)
    ax.set_xlim(0, 1180); ax.set_ylim(-0.7, len(D.MERCADOS) - 0.3); ax.set_yticks([])
    ax.set_xticks([200, 400, 600]); ax.set_xticklabels(["$200B", "$400B", "$600B"], fontsize=7)
    deco(ax, "Mercados enormes; Alphabet ya domina el más grande",
         "TAM 2026 (claro) vs ingreso GOOGL (oscuro), US$B · el reto no es el mercado, es defender la cuota",
         "Fuente: Gartner/IDC/eMarketer + 10-K. INFERENCIA. Publicidad digital: Alphabet ya captura ~37-40% del TAM total.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.09, left=0.18, right=0.98)
    save(fig, "14_tam")

# ── 15 · Radar de management ───────────────────────────────────────────────
def c15():
    labs = [n for n, _ in D.MGMT]; vals = [v for _, v in D.MGMT]
    N = len(vals); ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    v = vals + vals[:1]; a = ang + ang[:1]
    fig = plt.figure(figsize=(7.6, 5.0)); ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.plot(a, v, color=AZUL, lw=1.8); ax.fill(a, v, color=AZUL, alpha=0.16)
    for ai, vi in zip(ang, vals):
        col = ROJOSC if vi == 0 else AZUL
        ax.scatter(ai, vi, color=col, s=30, zorder=5)
        ax.text(ai, vi + 0.3, D.es(vi, 1), ha="center", fontsize=7.4, color=TINTA)
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=6.6, color=TINTA)
    ax.set_ylim(0, 5); ax.set_yticks([1, 2, 3, 4, 5]); ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Gestión: 6 dimensiones — un cero que no se maquilla",
         f"Puntuación 1–5 · total {D.es(D.MGMT_TOTAL,1)}/30 · «Estructura de voto» en 0/5: Page+Brin, {D.es(D.FUNDADORES_VOTO,1)}% del voto con {D.es(D.FUNDADORES_ECONOMIA,1)}% de la economía",
         "Fuente: DEF 14A 2026. Pichai operador sólido; el defecto de gobernanza es estructural y permanente, no de conducta.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10, left=0.10, right=0.90)
    save(fig, "15_mgmt")

# ── 16 · La asimetría voto/economía (el hallazgo central) ────────────────
def c16():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["Poder de voto\n(Page + Brin)", "Participación\neconómica (Page + Brin)"]
    vals = [D.FUNDADORES_VOTO, D.FUNDADORES_ECONOMIA]
    ax.bar([0, 1], vals, 0.42, color=[ROJOSC, ACERO])
    for i, v in enumerate(vals):
        ax.text(i, v + 1.2, f"{D.es(v,1)}%", ha="center", fontsize=10, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=8.6)
    ax.set_ylim(0, 62); ax.set_yticklabels([])
    ax.annotate(f"~{D.es(D.FUNDADORES_VOTO/D.FUNDADORES_ECONOMIA,1)}x de asimetría", xy=(0.5, 40),
                fontsize=10, color=ROJOSC, fontweight="bold", ha="center")
    deco(ax, "Con 6% del valor, controlan más de la mitad del voto",
         "Page + Brin: poder de voto vs. participación económica (%) · sin rol ejecutivo desde diciembre 2019",
         "Fuente: DEF 14A 2026. HECHO. La propuesta «un voto, una acción» perdió en 2025 pese al 98% de apoyo Clase A no afiliado.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "16_voto_economia")

# ── 17 · Matriz de riesgos numerada ───────────────────────────────────────
def c17():
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
         "Probabilidad × impacto (1–5) · el dominante (1) es la canibalización de Search; la gobernanza (3) es certeza, no riesgo",
         "Fuente: análisis propio. Los riesgos 1 y 2 comparten ventana temporal 2026-2027.", fig=fig)
    save(fig, "17_riesgos")

# ── 18 · Nueve inversores ─────────────────────────────────────────────────
def c18():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    y = np.arange(len(D.INVERSORES))[::-1]
    for yi, (nm, conv, vd) in zip(y, D.INVERSORES):
        col = VERDE if vd == "BUY" else (NOCHE if vd == "HOLD" else OCRE)
        ax.barh(yi, conv, 0.6, color=col)
        ax.text(conv + 0.12, yi, f"{conv}/10 · {vd}", va="center", fontsize=7.2, color=TINTA)
        ax.text(-0.15, yi, nm, va="center", ha="right", fontsize=8, color=TINTA)
    ax.set_xlim(0, 11); ax.set_ylim(-0.6, len(D.INVERSORES) - 0.4)
    ax.set_yticks([]); ax.set_xticks([2, 4, 6, 8, 10]); ax.set_xticklabels(["2", "4", "6", "8", "10"], fontsize=7)
    ax.text(0.2, -1.15, "navy = mantener · ocre = pass · convicción moderada en todo el panel", fontsize=6.6, color=GRIS, style="italic")
    deco(ax, "Nueve leyendas opinan",
         "Convicción /10 · sin consenso claro — el panel se divide entre el negocio (bueno) y el gobierno (malo)",
         "Fuente: doctrina de cada inversor aplicada por el autor. INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.13, left=0.16)
    save(fig, "18_inversores")

# ── 19 · Gemini vs ChatGPT (distribución vs producto) ────────────────────
def c19():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["Gemini\n(app standalone)", "ChatGPT\n(app standalone)"]
    vals = [D.GEMINI_MAU, D.CHATGPT_MAU]
    ax.bar([0, 1], vals, 0.42, color=[AZUL, ROJOSC])
    for i, v in enumerate(vals):
        ax.text(i, v + 20, f"{v}M MAU", ha="center", fontsize=9, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=8.6)
    ax.set_ylim(0, 1150); ax.set_yticklabels([])
    ax.text(0.5, 300, "Pero AI Overviews (dentro de Search)\nalcanza a &gt;2.000M de usuarios/mes\n— la distribución de Google es la real ventaja".replace("&gt;", ">"),
            ha="center", fontsize=7.4, color=NOCHE,
            bbox=dict(boxstyle="round,pad=0.5", fc=PANEL, ec=GLIN, lw=0.8))
    deco(ax, "Gemini cierra la brecha, pero no lidera el producto standalone",
         "Usuarios activos mensuales (M) · Google gana por distribución (Android/Search/Chrome), no por el mejor modelo",
         "Fuente: TechCrunch/9to5google + a16z (terceros). El moat de IA de Google es de canal, igual que en MSFT/AMZN.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "19_gemini")

# ── 20 · Dashboard de early warning ──────────────────────────────────────
def c20():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    filas = [
        ("Search &amp; other (crecimiento)", "+19,1% (récord)", "&lt; 10% sostenido 2+ trim.", VERDE),
        ("Margen operativo consolidado", "36,1% (récord)", "cae &lt; 33%", VERDE),
        ("Google Cloud (crecimiento)", "+63% (acelerando)", "&lt; +40%", VERDE),
        ("CTR posición 1 con AI Overview", "1,6% (−58% desde 2023)", "sigue cayendo sin tope", OCRE),
        ("Fallo AdX/DFP (Brinkema)", "pendiente, plazo vencido", "desinversión estructural ordenada", OCRE),
        ("FCF margin TTM", "15,2% (comprimido)", "sigue cayendo hacia 2027", OCRE),
        ("Estructura de voto dual-class", "52,7% voto / 6,2% economía", "es un hecho permanente, no una señal", "rojo"),
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
        ax.text(0.03, y, nm.replace("&amp;", "&").replace("&lt;", "<"), fontsize=6.8, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.47, y, est, fontsize=6.8, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.78, y, umb.replace("&lt;", "<"), fontsize=6.5, color=GRIS, va="center", transform=ax.transAxes)
    deco(ax, "Sistema de alerta temprana",
         "Semáforo · el negocio (verdes) sostiene; la contabilidad y el gobierno (ámbar/rojo) son las tensiones reales",
         "Fuente: KPIs primarios GOOGL. La fila roja no es una alerta transitoria: es un hecho estructural permanente.",
         fig=fig, flag_y=0.97)
    fig.subplots_adjust(top=0.80, bottom=0.05, left=0.02, right=0.98)
    save(fig, "20_early_warning")

if __name__ == "__main__":
    fns = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10,
           c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]
    for fn in fns:
        fn(); print("ok", fn.__name__)
    print("charts done:", len(fns))
