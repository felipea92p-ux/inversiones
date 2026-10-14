# -*- coding: utf-8 -*-
"""Gráficos Ultra Tesis MELI — importan dcf_meli (fuente de verdad) y chart_style."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap
from chart_style import deco, save, P
import dcf_meli as D

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
         f"Fuente: qg-seilern + verificación adversarial, corregido (6-jul-2026). Raw {D.es(D.RAW_QG,2)}/125 → {D.es(D.SCORE_QG,1)}/100 · tier Calidad sólida.",
         fig=fig)
    fig.subplots_adjust(top=0.74, bottom=0.08, left=0.06, right=0.94)
    save(fig, "01_radar")

# ── 02 · NIMAL colapsa (gráfico de firma) ─────────────────────────────────
def c02():
    x = np.arange(len(D.NIMAL_YRS))
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    cols = [ACERO if v >= 30 else (OCRE if v >= 20 else ROJOSC) for v in D.NIMAL_SERIE]
    ax.bar(x, D.NIMAL_SERIE, 0.55, color=cols)
    for i, v in enumerate(D.NIMAL_SERIE):
        ax.text(i, v + 1, pctc(v), ha="center", fontsize=8.4, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(D.NIMAL_YRS, fontsize=8.2)
    ax.set_ylim(0, 44); ax.set_yticklabels([])
    ax.annotate("−18,4pp en 5 trimestres\n(FY23→Q1'26)", xy=(4.3, 26), fontsize=7.6,
                color=ROJOSC, fontweight="bold", ha="center")
    deco(ax, "NIMAL: la rentabilidad del crédito se desploma",
         "Net interest margin after losses (%) · no es una caída monotónica: se sostuvo 2021-2023, colapsó después",
         "Fuente: 10-K FY2023/FY2025 + 10-Q Q1'26. HECHO. Mix hacia tarjeta de crédito (menor spread) + mayores provisiones en Brasil.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "02_nimal")

# ── 03 · Libro de crédito crece 2x más rápido que el ingreso ─────────────
def c03():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    labs = ["Ingreso\nconsolidado", "Libro de\ncrédito (gross)"]
    vals = [49, 87]
    ax.bar([0, 1], vals, 0.42, color=[AZUL, ROJOSC])
    for i, v in enumerate(vals):
        ax.text(i, v + 2, f"+{v}%", ha="center", fontsize=11, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 100); ax.set_yticklabels([])
    ax.text(0.5, 65, "Crecimiento YoY Q1'26\nManagement: \"~2/3 de la compresión de\nmargen es puro efecto de escala\"",
            ha="center", fontsize=7.3, color=NOCHE,
            bbox=dict(boxstyle="round,pad=0.5", fc=PANEL, ec=GLIN, lw=0.8))
    deco(ax, "El libro de crédito crece casi 2x más rápido que el negocio",
         "Crecimiento interanual Q1 2026 (%) · el capital se redirige hacia el segmento de menor y más volátil retorno",
         "Fuente: 10-Q Q1'26, carta a accionistas. HECHO. Tarjeta de crédito ya es 46% del libro (vs 42% hace un año).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "03_credito_vs_ingreso")

# ── 04 · Deuda neta se duplica ────────────────────────────────────────────
def c04():
    x = np.arange(len(D.NET_DEBT_YRS))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.plot(x, D.NET_DEBT_SERIE, color=ROJOSC, lw=2.2, marker="o", ms=5)
    ax.fill_between(x, 0, D.NET_DEBT_SERIE, color=ROJOSC, alpha=0.12)
    for i, v in enumerate(D.NET_DEBT_SERIE):
        ax.text(i, v + 130, f"${v:,}M".replace(",", "."), ha="center", fontsize=7, color=ROJOSC, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(D.NET_DEBT_YRS, fontsize=7.6)
    ax.set_ylim(0, 6800); ax.set_yticklabels([])
    deco(ax, "Deuda neta: +156% en cinco trimestres",
         "Deuda neta de MELI (US$M, cifra propia no-GAAP) · financia casi en su totalidad el crecimiento del libro de crédito",
         "Fuente: 8-K trimestrales (reconciliación oficial de deuda neta). HECHO.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "04_deuda_neta")

# ── 05 · Brasil: margen de contribución directa colapsa ──────────────────
def c05():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    labs = [s[0] for s in D.SEG_MARGEN]
    fy23 = [s[1] for s in D.SEG_MARGEN]; fy25 = [s[3] for s in D.SEG_MARGEN]
    x = np.arange(len(labs)); w = 0.35
    ax.bar(x - w/2, fy23, w, color=ACERO, label="FY2023")
    ax.bar(x + w/2, fy25, w, color=ROJOSC, label="FY2025")
    for i, (a, b) in enumerate(zip(fy23, fy25)):
        ax.text(i - w/2, a + 1, pctc(a), ha="center", fontsize=7.4, color=ACERO, fontweight="bold")
        ax.text(i + w/2, b + 1, pctc(b), ha="center", fontsize=7.4, color=ROJOSC, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8.6)
    ax.set_ylim(0, 54); ax.set_yticklabels([])
    ax.legend(fontsize=7.6, loc="upper right", frameon=False)
    deco(ax, "Brasil es donde más duele: −10,1pp en dos años",
         "Margen de contribución directa por país (%) · Argentina sigue siendo el más rentable — y el más flotante",
         "Fuente: 10-K FY2025, Nota 8 Segmentos. HECHO. Brasil Q1'25→Q1'26: 17,6%→8,2% (−9,4pp en un año).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "05_margen_brasil")

# ── 06 · Márgenes consolidados ────────────────────────────────────────────
def c06():
    yrs = D.YRS_FIN; x = np.arange(len(yrs))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.plot(x, D.OP_MGN, color=AZUL, lw=2.0, marker="o", ms=3.6, label="Operativo")
    ax.plot(x, D.NET_MGN, color=ROJO, lw=2.0, marker="s", ms=3.6, label="Neto")
    for i, v in enumerate(D.OP_MGN):
        ax.text(i, v + 1.0, pctc(v), fontsize=6.6, color=AZUL, ha="center")
    for i, v in enumerate(D.NET_MGN):
        ax.text(i, v - 2.2, pctc(v), fontsize=6.6, color=ROJO, ha="center")
    ax.set_xticks(x); ax.set_xticklabels(yrs, fontsize=7.6)
    ax.set_ylim(0, 18); ax.set_yticklabels([])
    ax.legend(fontsize=7.4, loc="upper left", frameon=False)
    deco(ax, "Compresión sostenida en 2025, aguda en Q1'26",
         "Margen operativo / margen neto (%) FY21→Q1'26",
         "Fuente: 10-K/10-Q. HECHO. Operativo 12,9%→6,9% (Q1'25→Q1'26): −600pb en un trimestre.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "06_margenes")

# ── 07 · DCF 3 escenarios ─────────────────────────────────────────────────
def c07():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    labs = [f"Conservador\n({D.P_BEAR}%)", f"Base\n({D.P_BASE}%)", f"Optimista\n({D.P_BULL}%)"]
    vals = [D.V_BEAR, D.V_BASE, D.V_BULL]; cols = [ROJOSC, AZUL, VERDE]
    x = np.arange(3); ax.bar(x, vals, 0.5, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 30, f"US${v}", ha="center", fontsize=8.6, fontweight="bold", color=TINTA)
    ax.axhline(D.PRECIO, color=TINTA, lw=1.6)
    ax.text(0.02, D.PRECIO + 30, f"HOY US${D.es(D.PRECIO,0)} — zona {D.ZONA_HOY}",
            fontsize=7.6, color=TINTA, fontweight="bold")
    ax.axhline(D.PWFV, color=ROJO, lw=1.4, ls=(0, (5, 3)))
    ax.text(2.55, D.PWFV + 30, f"PWFV US${D.PWFV}", va="bottom", ha="right", fontsize=7.6, color=ROJO)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 2250); ax.set_yticklabels([])
    deco(ax, "El precio ya está por encima incluso del caso optimista propio",
         f"Valor por acción del DCF sobre owner earnings normalizados (US$) · WACC {D.es(D.WACC,1)}%",
         f"Fuente: modelo propio (val-mos). SUPUESTO. Ponderado US${D.V_POND}; asimetría {D.es(D.ASIMETRIA,2)}:1 (débil).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "07_dcf")

# ── 08 · Mapa de zonas ────────────────────────────────────────────────────
def c08():
    fig, ax = plt.subplots(figsize=(7.6, 2.8))
    lo, hi = 400, 1950
    zonas = [("GANGA", lo, D.Z_GANGA, VERDE), ("OPORT.", D.Z_GANGA, D.Z_OPORT, ACERO),
             ("JUSTO", D.Z_OPORT, D.Z_JUSTO, OCRE), ("CARO", D.Z_JUSTO, D.Z_CARO, TERRA),
             ("BURBUJA", D.Z_CARO, hi, ROJOSC)]
    for nm, a, b, c in zonas:
        ax.barh(0, b - a, left=a, height=0.5, color=c, alpha=0.88)
        ax.text((a + b) / 2, 0, nm, ha="center", va="center", fontsize=7.0, color="white", fontweight="bold")
        ax.text(b, -0.42, f"${int(b)}", ha="center", fontsize=6.4, color=GRIS)
    ax.scatter([min(D.PRECIO, hi-30)], [0.42], marker="v", s=95, color=TINTA, zorder=5)
    ax.text(min(D.PRECIO, hi-30), 0.62, f"HOY US${D.es(D.PRECIO,0)}", ha="center", fontsize=8, fontweight="bold", color=TINTA)
    ax.plot([D.PWFV, D.PWFV], [-0.25, 0.25], color=ROJO, lw=1.6, ls=(0, (4, 2)))
    ax.text(D.PWFV, -0.62, f"PWFV ${D.PWFV}", ha="center", fontsize=7, color=ROJO)
    ax.plot([D.GATILLO_OPORT, D.GATILLO_OPORT], [-0.25, 0.25], color=VERDE, lw=1.4)
    ax.text(D.GATILLO_OPORT, 0.62, f"gatillo ${D.GATILLO_OPORT}", ha="center", fontsize=6.8, color=VERDE)
    ax.set_xlim(lo, hi); ax.set_ylim(-0.8, 0.9); ax.axis("off")
    deco(ax, "Mapa operativo de precio",
         f"Zonas ancladas al PWFV US${D.PWFV} · HOY US${D.es(D.PRECIO,0)} = {D.ZONA_HOY} (164% del PWFV)",
         f"Fuente: val-mos v3. El tier Calidad sólida exige zona Ganga/Oportunidad (≤US${D.GATILLO_OPORT}) — es un gate, no solo un MoS.",
         fig=fig, flag_y=0.96)
    fig.subplots_adjust(top=0.64, bottom=0.06)
    save(fig, "08_zonas")

# ── 09 · Candado duro ──────────────────────────────────────────────────────
def c09():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    labs = ["Techo del tier\n(Calidad sólida)", "Múltiplo normalizado\n(owner earnings)", "Múltiplo CFO\nsimple (ilusorio)"]
    vals = [D.TECHO_MULT_TIER, D.MULT_NORMALIZADO, D.MULT_FCF_REAL]
    cols = [VERDE, ROJOSC, GCLARO]
    x = np.arange(3); ax.bar(x, vals, 0.5, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 1.2, f"{D.es(v,1)}x", ha="center", fontsize=9, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.6)
    ax.set_ylim(0, 44); ax.set_yticklabels([])
    ax.annotate("1,5x sobre\nel techo", xy=(1, 41), fontsize=7.4, color=ROJOSC, ha="center", style="italic")
    deco(ax, "El candado duro: violado incluso con la lectura más generosa",
         "Múltiplo pagado hoy sobre owner earnings vs. el techo de múltiplo del tier de MELI (25x)",
         "Fuente: val-mos v3. El múltiplo de CFO simple (8,7x) es ilusorio: distorsionado por el crecimiento del libro de crédito.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "09_candado_duro")

# ── 10 · DCF inverso ──────────────────────────────────────────────────────
def c10():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["Conservador\npropio", "Implícito\nen el precio", "Optimista\npropio"]
    vals = [D.G_CONS, D.G_IMPL, D.G_OPT]
    cols = [OCRE, ROJO, VERDE]
    x = np.arange(3); ax.bar(x, vals, 0.55, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.8, pctc(v), ha="center", fontsize=8.6, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 45); ax.set_yticklabels([])
    deco(ax, "El precio exige superar incluso el propio caso optimista",
         "Crecimiento de owner earnings implícito en US$1.806 vs. referencias (%)",
         f"Fuente: DCF inverso (val-mos). SUPUESTO. Clasificación: {D.DCF_CLASE} — 38,1% está al 95% de la banda hacia el techo.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "10_dcf_inverso")

# ── 11 · WACC ─────────────────────────────────────────────────────────────
def c11():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    coe = D.COE_CAPM
    pasos = ["Tasa libre\nde riesgo", f"+ Prima ×\nbeta {D.es(D.BETA,2)}", "= CAPM\nUS", "+ Riesgo país\n(blend LatAm)", "= WACC\nusado"]
    cols = [CIELO, ACERO, AZUL, OCRE, ROJO]
    ax.bar(0, D.RF, 0.6, color=cols[0])
    ax.bar(1, D.BETA * D.ERP, 0.6, bottom=D.RF, color=cols[1])
    ax.bar(2, coe, 0.6, color=cols[2])
    ax.bar(3, D.WACC - coe, 0.6, bottom=coe, color=cols[3])
    ax.bar(4, D.WACC, 0.6, color=cols[4])
    labels = [pctc(D.RF), pctc(D.BETA * D.ERP), pctc(coe), f"+{D.es(D.WACC-coe,1)}", pctc(D.WACC)]
    tops = [D.RF, coe, coe, D.WACC, D.WACC]
    for i in range(5):
        ax.text(i, tops[i] + 0.3, labels[i], ha="center", fontsize=7.4, color=TINTA,
                fontweight="bold" if i in (2, 4) else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels(pasos, fontsize=6.8)
    ax.set_ylim(0, 16); ax.set_yticklabels([])
    deco(ax, "El WACC, ladrillo a ladrillo: LatAm pesa",
         f"Coste de capital (%) · CAPM US ~{D.es(coe,1)}%, usado {D.es(D.WACC,1)}% tras sumar el riesgo-país ponderado por ingresos",
         "Fuente: modelo propio (val-mos), Damodaran (spreads país). Brasil 54%/México 22%/Argentina 19%/Otros 5% del ingreso.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.14)
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
            ax.text(j, i, f"{M[i, j]}", ha="center", va="center", fontsize=7.6,
                    color="white" if M[i, j] > 1300 or M[i, j] < 950 else TINTA,
                    fontweight="bold" if base else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels([pctc(g) for g in D.GT_GRID], fontsize=7.2)
    ax.set_yticks(range(5)); ax.set_yticklabels([pctc(w) for w in D.WACC_GRID], fontsize=7.2)
    ax.set_xlabel("Crecimiento terminal", fontsize=7.8, color=GRIS)
    ax.set_ylabel("WACC", fontsize=7.8, color=GRIS)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    deco(ax, "El valor bajo estrés — ninguna celda alcanza el precio de hoy",
         "Valor DCF base por acción (US$) según WACC × terminal · negrita = caso central",
         f"Fuente: modelo propio. SUPUESTO. Rango US${D.SENS[-1][0]}-{D.SENS_MAX}: siempre por debajo del precio hoy (US${D.es(D.PRECIO,0)}).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.10, right=0.98)
    save(fig, "12_sensibilidad")

# ── 13 · Porter por negocio ────────────────────────────────────────────────
def c13():
    y = np.arange(len(D.PORTER_SEG))[::-1]
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    for yi, (nm, v) in zip(y, D.PORTER_SEG):
        col = VERDE if v <= 2.5 else (OCRE if v <= 3.2 else ROJOSC)
        ax.barh(yi, v, 0.55, color=col)
        ax.text(v + 0.08, yi, f"{D.es(v,1)}/5", va="center", fontsize=8, color=TINTA, fontweight="bold")
        ax.text(-0.1, yi, nm, va="center", ha="right", fontsize=8.2, color=TINTA)
    ax.axvline(D.PORTER_POND, color=NOCHE, lw=1.2, ls=(0, (4, 2)))
    ax.text(D.PORTER_POND + 0.05, -0.75, f"ponderado {D.es(D.PORTER_POND,1)}", fontsize=6.8, color=NOCHE)
    ax.set_xlim(0, 5.2); ax.set_ylim(-1, len(D.PORTER_SEG) - 0.4); ax.set_yticks([])
    ax.set_xticks([1, 2, 3, 4, 5]); ax.set_xticklabels(["1", "2", "3", "4", "5"], fontsize=7)
    deco(ax, "Cinco Fuerzas de Porter, por negocio",
         "Score /5 (menor = mejor foso) · logística es el foso más ancho; fintech, el más disputado (Nubank)",
         "Fuente: análisis propio sobre 10-K. El propio 10-K admite: \"usuarios y comercios pueden cambiar fácilmente\" de plataforma.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11, left=0.28)
    save(fig, "13_porter")

# ── 14 · TAM por mercado ──────────────────────────────────────────────────
def c14():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    y = np.arange(len(D.MERCADOS))[::-1]
    LX = 820
    for yi, (nm, tam, gg, nota) in zip(y, D.MERCADOS):
        w = min(tam, 800)
        ax.barh(yi, w, 0.6, color=CIELO, alpha=0.6)
        ax.barh(yi, gg, 0.6, color=AZUL)
        ax.text(-15, yi, nm, va="center", ha="right", fontsize=7.4, color=TINTA)
        ax.text(LX, yi, f"TAM ${tam}B · MELI ${gg}B · {nota}", va="center", fontsize=6.2, color=GRIS)
    ax.set_xlim(0, 1350); ax.set_ylim(-0.7, len(D.MERCADOS) - 0.3); ax.set_yticks([])
    ax.set_xticks([200, 400, 600]); ax.set_xticklabels(["$200B", "$400B", "$600B"], fontsize=7)
    deco(ax, "Mercados enormes; MELI ya captura una fracción líder",
         "TAM 2026 (claro) vs ingreso MELI (oscuro), US$B · el reto es sostener la calidad de crecimiento, no el tamaño",
         "Fuente: reportes de mercado + 10-K. INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.09, left=0.18, right=0.98)
    save(fig, "14_tam")

# ── 15 · Radar de management ──────────────────────────────────────────────
def c15():
    labs_full = [n for n, _ in D.MGMT]; vals = [v for _, v in D.MGMT]
    # etiquetas cortas para el radar (evita solapamiento entre ejes adyacentes);
    # el detalle completo de cada etiqueta va en la subtítulo/fuente, no en el eje.
    labs = ["Transición\nCEO", "Independencia\ndel consejo", "Compensación\nejecutiva",
            "Partes\nrelacionadas", "Disciplina\nde capital", "Transparencia"]
    N = len(vals); ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    v = vals + vals[:1]; a = ang + ang[:1]
    fig = plt.figure(figsize=(7.6, 5.2)); ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.plot(a, v, color=AZUL, lw=1.8); ax.fill(a, v, color=AZUL, alpha=0.16)
    for ai, vi in zip(ang, vals):
        col = ROJOSC if vi <= 2 else AZUL
        ax.scatter(ai, vi, color=col, s=30, zorder=5)
        ax.text(ai, vi + 0.35, D.es(vi, 1), ha="center", fontsize=7.4, color=TINTA)
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=6.6, color=TINTA)
    ax.set_ylim(0, 5); ax.set_yticks([1, 2, 3, 4, 5]); ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Gestión: 6 dimensiones — ISS Board en el peor decil",
         f"Total {D.es(D.MGMT_TOTAL,1)}/30 · consejo 7/9 independiente · transición Galperin→Szarfsztejn ene-2026 · recompra 2025 solo US${D.es(D.BUYBACK_2025,2)}M",
         "Fuente: DEF 14A + ISS (probable, no verificado en fuente primaria). Galperin pasó de CEO a Presidente Ejecutivo, ene-2026.", fig=fig)
    fig.subplots_adjust(top=0.72, bottom=0.10, left=0.12, right=0.88)
    save(fig, "15_mgmt")

# ── 16 · Recompra irrisoria vs de-rating ──────────────────────────────────
def c16():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["P/E hace 3 años\n(~64x)", "P/E hoy\n(~44x)"]
    vals = [D.PE_MEDIANA_3A, D.PE_TRAILING]
    ax.bar([0, 1], vals, 0.42, color=[ACERO, ROJOSC])
    for i, v in enumerate(vals):
        ax.text(i, v + 1.5, f"{D.es(v,1)}x", ha="center", fontsize=10, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 76); ax.set_yticklabels([])
    ax.text(0.5, 20, f"Recompra ejecutada en 2025:\nsolo US${D.es(D.BUYBACK_2025,2)}M\n(vs. mercado ~US${D.es(D.MKTCAP,0)}B)",
            ha="center", fontsize=7.6, color=NOCHE,
            bbox=dict(boxstyle="round,pad=0.5", fc=PANEL, ec=ROJOSC, lw=1.0))
    deco(ax, "El múltiplo se desplomó y la recompra no se movió",
         "P/E histórico (3 años) vs. P/E hoy · la disciplina de capital no aprovechó el de-rating",
         "Fuente: agregadores + 8-K ago-2025. La recompra 2025 compensa dilución del plan de directores, no es retorno de capital.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "16_buyback")

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
        fig.text(0.66, ly + 0.012, nm, fontsize=6.3, color=TINTA, va="center")
        fig.text(0.66, ly - 0.028, f"prob {pr} × impacto {im} = {sev}", fontsize=6.0, color=col, va="center", style="italic")
        ly -= 0.108
    deco(ax, "Matriz de riesgos",
         "Probabilidad × impacto (1–5) · gobernanza y deterioro crediticio comparten la ventana temporal 2026-2027",
         "Fuente: análisis propio.", fig=fig)
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
    ax.text(0.2, -1.15, "navy = mantener · ocre = pass · el panel se inclina hacia cautela por precio, no por negocio", fontsize=6.6, color=GRIS, style="italic")
    deco(ax, "Nueve leyendas opinan",
         "Convicción /10 · el negocio convence más que el precio de hoy",
         "Fuente: doctrina de cada inversor aplicada por el autor. INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.13, left=0.16)
    save(fig, "18_inversores")

# ── 19 · GMV por país ──────────────────────────────────────────────────────
def c19():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    x = np.arange(len(D.KPI_QTRS))
    ax.plot(x, D.GMV_GROWTH_BRASIL, color=AZUL, lw=2.0, marker="o", ms=4, label="Brasil")
    ax.plot(x, D.GMV_GROWTH_MEXICO, color=OCRE, lw=2.0, marker="s", ms=4, label="México")
    ax.plot(x, D.GMV_GROWTH_ARG, color=ROJOSC, lw=1.6, marker="^", ms=4, label="Argentina", alpha=0.75)
    ax.set_xticks(x); ax.set_xticklabels(D.KPI_QTRS, fontsize=8)
    ax.set_ylim(0, 135); ax.set_yticklabels([])
    ax.legend(fontsize=7.6, loc="upper right", frameon=False)
    deco(ax, "Crecimiento robusto en todas las geografías clave",
         "GMV, crecimiento interanual FX-neutral por país (%) · Argentina desacelera desde una base extrema",
         "Fuente: cartas a accionistas trimestrales. HECHO. El volumen de negocio no muestra la fragilidad que sí muestra el margen.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "19_gmv_paises")

# ── 20 · Dashboard de early warning ──────────────────────────────────────
def c20():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    filas = [
        ("GMV / TPV / MAU fintech", "+36-50% (sólido)", "desaceleración &lt;20% sostenida", VERDE),
        ("Ingreso consolidado", "+49% (récord)", "&lt; 25% sostenido 2+ trim.", VERDE),
        ("NIMAL", "17,8% (mínimo histórico)", "sigue perforando sin estabilizar", "rojo"),
        ("Write-off rate anualizado", "~19,4% (reacelerando)", "supera 22% sin mejora de NPL", OCRE),
        ("NPL 15-90 días", "8,0% (estable)", "empieza a subir de forma sostenida", OCRE),
        ("Margen operativo consolidado", "6,9% (mínimo)", "sigue cayendo bajo 6%", OCRE),
        ("Gobernanza (ISS Board)", "10 — peor decil", "hecho estructural permanente", "rojo"),
    ]
    ax.axis("off")
    y0 = 1.0; dh = 1.0 / (len(filas) + 1)
    ax.text(0.02, y0, "Indicador", fontsize=7.6, fontweight="bold", color=NOCHE, transform=ax.transAxes)
    ax.text(0.47, y0, "Estado hoy", fontsize=7.6, fontweight="bold", color=NOCHE, transform=ax.transAxes)
    ax.text(0.78, y0, "Umbral de alerta", fontsize=7.6, fontweight="bold", color=NOCHE, transform=ax.transAxes)
    for i, (nm, est, umb, col) in enumerate(filas):
        y = y0 - (i + 1) * dh
        c = ROJOSC if col == "rojo" else col
        ax.add_patch(Rectangle((0.0, y - dh*0.42), 1.0, dh*0.84, transform=ax.transAxes,
                     color=PANEL if i % 2 else P["fondo"], zorder=0))
        ax.scatter(0.005, y, s=55, color=c, transform=ax.transAxes, zorder=3, clip_on=False)
        ax.text(0.03, y, nm.replace("&lt;", "<"), fontsize=6.7, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.47, y, est, fontsize=6.7, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.78, y, umb.replace("&lt;", "<"), fontsize=6.3, color=GRIS, va="center", transform=ax.transAxes)
    deco(ax, "Sistema de alerta temprana",
         "Semáforo · el volumen de negocio (verde) sostiene; el crédito y la gobernanza (ámbar/rojo) son las tensiones reales",
         "Fuente: KPIs primarios MELI. NIMAL y write-off rate son los gatillos de re-análisis de tier, no solo de precio.",
         fig=fig, flag_y=0.97)
    fig.subplots_adjust(top=0.80, bottom=0.05, left=0.02, right=0.98)
    save(fig, "20_early_warning")

if __name__ == "__main__":
    fns = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10,
           c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]
    for fn in fns:
        fn(); print("ok", fn.__name__)
    print("charts done:", len(fns))
