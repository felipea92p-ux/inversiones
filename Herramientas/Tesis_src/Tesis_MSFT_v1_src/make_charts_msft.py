# -*- coding: utf-8 -*-
"""Gráficos Ultra Tesis MSFT — importan dcf_msft (fuente de verdad) y chart_style."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap
from chart_style import deco, save, P
import dcf_msft as D

plt.rcParams["text.parse_math"] = False

AZUL, NOCHE, ACERO, CIELO = P["azul"], P["azul_noche"], P["azul_acero"], P["azul_cielo"]
ROJO, ROJOSC, VERDE, OCRE, TERRA, GRIS = (P["rojo"], P["rojo_oscuro"], P["verde"],
    P["ocre"], P["terracota"], P["gris"])
TINTA, GLIN, GCLARO = P["tinta"], P["gris_linea"], P["gris_claro"]
pctc = lambda x: D.es(x, 1) + "%"

# ── 01 · Radar de las 11 reglas QG ───────────────────────────────────────
def c01():
    labs = [n for n, _ in D.RADAR]; vals = [v for _, v in D.RADAR]
    N = len(vals); ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    v = vals + vals[:1]; a = ang + ang[:1]
    fig = plt.figure(figsize=(7.6, 5.4)); ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.plot(a, v, color=NOCHE, lw=1.8); ax.fill(a, v, color=NOCHE, alpha=0.16)
    ax.plot(a, [8]*len(a), color=ROJO, lw=1.1, ls=(0, (4, 3)))
    for ai, vi in zip(ang, vals):
        col = VERDE if vi >= 9 else (ROJOSC if vi < 8 else NOCHE)
        ax.scatter(ai, vi, color=col, s=26, zorder=5)
        ax.text(ai, vi + 0.85, D.es(vi, 1), ha="center", va="center", fontsize=7.3, color=TINTA)
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=7.6, color=TINTA)
    ax.set_ylim(0, 10); ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Las 11 reglas Quality Growth",
         "Puntuación 0–10 por regla · anillo rojo = umbral de excelencia (8)",
         f"Fuente: sistema qg-seilern (6-jul-2026). Raw {D.es(D.RAW_QG,1)}/125 → {D.es(D.SCORE_QG,1)}/100 · tier Núcleo. HECHO/INFERENCIA.",
         fig=fig)
    fig.subplots_adjust(top=0.74, bottom=0.08, left=0.06, right=0.94)
    save(fig, "01_radar")

# ── 02 · Segmentos: ingresos + margen operativo ──────────────────────────
def c02():
    labs = [s[0] for s in D.SEG]; rev = [s[1] for s in D.SEG]
    mfy = [s[2] for s in D.SEG]; mq3 = [s[3] for s in D.SEG]
    x = np.arange(3)
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.bar(x, rev, 0.5, color=[AZUL, ROJO, ACERO])
    for i, v in enumerate(rev):
        ax.text(i, v + 2, f"US${v:.0f}B", ha="center", fontsize=8, color=TINTA, fontweight="bold")
    ax2 = ax.twinx()
    ax2.plot(x, mq3, color=NOCHE, lw=0, marker="o", ms=7)
    for i, (a, b) in enumerate(zip(mfy, mq3)):
        ax2.annotate("", xy=(i, b), xytext=(i, a), arrowprops=dict(arrowstyle="->", color=GRIS, lw=1.1))
        ax2.text(i + 0.14, b, f"{D.es(b,1)}%", va="center", fontsize=7.4, color=NOCHE, fontweight="bold")
        ax2.text(i + 0.14, a, f"{D.es(a,1)}%", va="center", fontsize=6.6, color=GRIS)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.6)
    ax.set_ylim(0, 145); ax.set_yticklabels([])
    ax2.set_ylim(20, 75); ax2.set_yticks([]); ax2.spines["top"].set_visible(False)
    deco(ax, "Tres segmentos, tres destinos de margen",
         "Ingresos FY2025 (barras) y margen operativo FY25→Q3 FY26 (flechas) · IC es el ÚNICO que se comprime",
         "Fuente: 10-K FY2025 + IR Q3 FY26. HECHO. PBP expande a 59,9%; Intelligent Cloud (Azure) cae −180pb a 39,7%.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "02_segmentos")

# ── 03 · La tensión: capex explota, FCF margin se comprime ───────────────
def c03():
    yrs = D.YRS_FIN; x = np.arange(len(yrs))
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.bar(x, D.CAPEX, 0.55, color=ROJOSC, label="Capex (US$B)")
    for i, v in enumerate(D.CAPEX):
        ax.text(i, v + 2.5, f"{v:.0f}", ha="center", fontsize=7, color=ROJOSC)
    ax.bar(len(yrs), D.CAPEX_PURO_FY26, 0.55, color=ROJOSC, alpha=0.45)
    ax.text(len(yrs), D.CAPEX_PURO_FY26 + 3, "~107\n(FY26e)", ha="center", fontsize=6.6, color=ROJOSC)
    ax2 = ax.twinx()
    ax2.plot(x, D.FCF_MGN, color=AZUL, lw=2.0, marker="o", ms=4, label="FCF margin (%)")
    for i, v in enumerate(D.FCF_MGN):
        ax2.text(i, v + 1.4, f"{D.es(v,1)}%", ha="center", fontsize=6.6, color=AZUL)
    ax.set_xticks(list(x) + [len(yrs)]); ax.set_xticklabels(yrs + ["FY26e"], fontsize=7.4)
    ax.set_ylim(0, 210); ax.set_yticklabels([])
    ax2.set_ylim(0, 55); ax2.set_yticks([]); ax2.spines["top"].set_visible(False)
    ax.legend(fontsize=7.2, loc="upper left", frameon=False)
    ax2.legend(fontsize=7.2, loc="upper center", frameon=False)
    deco(ax, "La tensión central: capex colosal, FCF comprimido",
         "Capex anual (barras rojas) y margen de FCF (línea azul) · capex/ventas saltó de 12% a 30%",
         "Fuente: 10-K FY2025 + 10-Q Q3 FY26. HECHO. FY26e ~$190B ampliado (incl. leases) / ~$107B capex puro anualizado.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "03_capex_fcf")

# ── 04 · La IA acelera ingresos y comprime margen (a propósito) ──────────
def c04():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    x = [0, 1, 2]
    ax.plot(x, D.MSCLOUD_GM, color=ROJO, lw=2.2, marker="o", ms=5)
    for i, v in enumerate(D.MSCLOUD_GM):
        ax.text(i, v + 0.4, f"{v}%", ha="center", fontsize=8.5, color=ROJO, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(["Q3 FY25", "Q2 FY26", "Q3 FY26"], fontsize=8)
    ax.set_ylim(63, 71); ax.set_yticks([64, 66, 68, 70]); ax.set_yticklabels(["64%", "66%", "68%", "70%"], fontsize=7)
    ax.text(0.5, 64.3, f"Azure  +{D.AZURE_YOY}%  (acelerando)\nIA run-rate  US${D.AI_RUNRATE}B  (+{D.AI_YOY}%)\nMicrosoft Cloud  US${D.es(D.MSCLOUD,1)}B  (+{D.MSCLOUD_YOY}%)",
            fontsize=8, color=NOCHE, va="bottom",
            bbox=dict(boxstyle="round,pad=0.5", fc=P["panel"], ec=GLIN, lw=0.8))
    deco(ax, "La IA acelera los ingresos y comprime el margen — por elección",
         "Margen bruto de Microsoft Cloud (%) · la depreciación de la IA pega primero donde se factura la IA",
         "Fuente: transcript + IR Q3 FY26. HECHO. La compresión (−300pb) es transición anunciada, no erosión estructural.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "04_azure_ai")

# ── 05 · FCF reportado vs Owner earnings normalizado ─────────────────────
def c05():
    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    # waterfall a owner earnings
    cfo = 170.1; maint = 45.0; sbc = 12.4; oe = D.OE_TTM
    etiquetas = ["Flujo\noperativo", "Capex\nmantenim.", "SBC", "Owner\nearnings", "", "FCF\nreportado"]
    ax.bar(0, cfo, 0.6, color=NOCHE)
    ax.bar(1, maint, 0.6, bottom=cfo - maint, color=ROJOSC)
    ax.bar(2, sbc, 0.6, bottom=cfo - maint - sbc, color=ROJOSC)
    ax.bar(3, oe, 0.6, color=VERDE)
    ax.bar(5, D.FCF_REP, 0.6, color=CIELO)
    for i, (v, sign) in enumerate([(cfo, ""), (maint, "−"), (sbc, "−"), (oe, ""), (None, ""), (D.FCF_REP, "")]):
        if v is None: continue
        top = {0: cfo, 1: cfo, 2: cfo - maint, 3: oe, 5: D.FCF_REP}[i]
        ax.text(i, top + 4, f"{sign}{v:.0f}", ha="center", fontsize=8, color=TINTA,
                fontweight="bold" if i in (0, 3, 5) else "normal")
    ax.set_xticks([0, 1, 2, 3, 5]); ax.set_xticklabels([e for j, e in enumerate(etiquetas) if j != 4], fontsize=7.2)
    ax.set_ylim(0, 195); ax.set_yticklabels([])
    ax.annotate("el capex de crecimiento (~$52B)\ndeprime el FCF reportado", xy=(5, D.FCF_REP + 8), xytext=(3.7, 150),
                fontsize=6.8, color=GRIS, style="italic", ha="center",
                arrowprops=dict(arrowstyle="->", color=GRIS, lw=0.9))
    deco(ax, "El FCF reportado engaña: subestima el poder de generación",
         "De flujo operativo a owner earnings (US$B, TTM) · owner = CFO − capex de MANTENIMIENTO − SBC",
         "Fuente: 10-Q Q3 FY26. INFERENCIA. FCF reportado $73B (resta TODO el capex); owner earnings normalizado ~$115B.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "05_owner_earnings")

# ── 06 · Márgenes ────────────────────────────────────────────────────────
def c06():
    yrs = D.YRS_FIN; x = np.arange(len(yrs))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    for serie, col, nm in [(D.GM, GRIS, "Bruto"), (D.OP_MGN, AZUL, "Operativo"), (D.FCF_MGN, ROJO, "FCF")]:
        ax.plot(x, serie, color=col, lw=2.0, marker="o", ms=3.4)
        ax.text(len(yrs) - 0.94, serie[-1], f" {nm} {D.es(serie[-1],0)}%", va="center", fontsize=7.4, color=col)
    ax.set_xticks(x); ax.set_xticklabels(yrs, fontsize=8)
    ax.set_ylim(15, 75); ax.set_yticks([20, 40, 60]); ax.set_yticklabels(["20%", "40%", "60%"], fontsize=7)
    ax.set_xlim(0, len(yrs) + 0.4)
    deco(ax, "Márgenes operativos en máximo; el FCF, no",
         "Margen bruto / operativo / FCF (%) FY21→TTM · el operativo EXPANDE mientras el FCF se comprime por capex",
         "Fuente: 10-K FY2025 + 10-Q. HECHO. Margen operativo 41,6%→46,8% (récord); FCF margin 33%→22,9%.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "06_margenes")

# ── 07 · DCF 3 escenarios ────────────────────────────────────────────────
def c07():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    labs = [f"Bajista\n({D.P_BEAR}%)", f"Base\n({D.P_BASE}%)", f"Alcista\n({D.P_BULL}%)"]
    vals = [D.V_BEAR, D.V_BASE, D.V_BULL]; cols = [ROJOSC, AZUL, VERDE]
    x = np.arange(3); ax.bar(x, vals, 0.5, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 8, f"US${v}", ha="center", fontsize=8.6, fontweight="bold", color=TINTA)
    ax.axhline(D.PRECIO, color=TINTA, lw=1.4)
    ax.text(2.55, D.PRECIO - 18, f"HOY US${int(D.PRECIO)}", va="top", ha="right", fontsize=7.8, color=TINTA)
    ax.axhline(D.PWFV, color=ROJO, lw=1.4, ls=(0, (5, 3)))
    ax.text(2.55, D.PWFV + 5, f"PWFV US${D.PWFV}", va="bottom", ha="right", fontsize=7.8, color=ROJO)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 700); ax.set_yticklabels([])
    deco(ax, "Tres futuros — y el bajista casi toca el precio de hoy",
         f"Valor por acción del DCF sobre owner earnings (US$) · WACC {D.es(D.WACC,1)}% · terminal {D.es(D.TERMINAL,1)}%",
         f"Fuente: modelo propio (val-mos). SUPUESTO. Ponderado = US${D.V_POND}. Bajista US${D.V_BEAR} ≈ precio → downside acotado.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "07_dcf")

# ── 08 · Mapa de zonas de precio ─────────────────────────────────────────
def c08():
    fig, ax = plt.subplots(figsize=(7.6, 2.8))
    lo, hi = 300, 760
    zonas = [("GANGA", lo, D.Z_GANGA, VERDE), ("OPORTUNIDAD", D.Z_GANGA, D.Z_OPORT, ACERO),
             ("JUSTO", D.Z_OPORT, D.Z_JUSTO, OCRE), ("CARO", D.Z_JUSTO, D.Z_CARO, TERRA),
             ("BURBUJA", D.Z_CARO, hi, ROJOSC)]
    for nm, a, b, c in zonas:
        ax.barh(0, b - a, left=a, height=0.5, color=c, alpha=0.88)
        ax.text((a + b) / 2, 0, nm, ha="center", va="center", fontsize=7.0, color="white", fontweight="bold")
        ax.text(b, -0.42, f"${int(b)}", ha="center", fontsize=6.6, color=GRIS)
    ax.scatter([D.PRECIO], [0.42], marker="v", s=95, color=TINTA, zorder=5)
    ax.text(D.PRECIO, 0.62, f"HOY US${int(D.PRECIO)}", ha="center", fontsize=8, fontweight="bold", color=TINTA)
    ax.plot([D.PWFV, D.PWFV], [-0.25, 0.25], color=ROJO, lw=1.6, ls=(0, (4, 2)))
    ax.text(D.PWFV, -0.62, f"PWFV ${D.PWFV}", ha="center", fontsize=7, color=ROJO)
    ax.set_xlim(lo, hi); ax.set_ylim(-0.8, 0.9); ax.axis("off")
    deco(ax, "Mapa operativo de precio",
         f"Zonas ancladas al PWFV-Valor US${D.PWFV} · HOY US${int(D.PRECIO)} = {D.ZONA_HOY} ({D.es(D.DCTO_HOY,1)}%)",
         f"Fuente: val-mos. MoS exigido {D.MOS_EXIG}% (tier Núcleo); MoS hoy ~{D.MOS_HOY}% → COMPRAR TRAMO.",
         fig=fig, flag_y=0.96)
    fig.subplots_adjust(top=0.64, bottom=0.06)
    save(fig, "08_zonas")

# ── 09 · Múltiplos vs historia (de-rating) ───────────────────────────────
def c09():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    x = np.arange(len(D.MULT_YRS))
    cols = [ACERO]*5 + [VERDE]
    ax.bar(x, D.MULT_PE, 0.6, color=cols)
    for i, v in enumerate(D.MULT_PE):
        ax.text(i, v + 0.6, f"{D.es(v,1)}x", ha="center", fontsize=7.4, color=TINTA,
                fontweight="bold" if i == len(D.MULT_PE)-1 else "normal")
    ax.axhline(D.PE_MEDIANA, color=ROJO, lw=1.3, ls=(0, (5, 3)))
    ax.text(0.1, D.PE_MEDIANA + 0.6, f"mediana 10 años {D.es(D.PE_MEDIANA,1)}x", fontsize=7, color=ROJO)
    ax.set_xticks(x); ax.set_xticklabels(D.MULT_YRS, fontsize=7.6)
    ax.set_ylim(0, 40); ax.set_yticklabels([])
    deco(ax, "El múltiplo más barato desde 2022–23",
         "P/E (trailing) · 22,9x hoy vs mediana ~31x — un ~28% por debajo de su propia historia",
         "Fuente: stockanalysis + 10-K. INFERENCIA sobre HECHOs. Forward P/E FY27 ~19,4x; EV/EBITDA 16x vs 19,5x.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "09_multiplos")

# ── 10 · DCF inverso ─────────────────────────────────────────────────────
def c10():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["Implícito\nen el precio", "Conservador\npropio", "CAGR revenue\n(TTM)", "Guiado\n(Azure/IA)"]
    vals = [D.G_IMPL, D.G_CONS, D.G_CAGR, D.G_GUIA]
    cols = [ROJO, OCRE, ACERO, NOCHE]
    x = np.arange(4); ax.bar(x, vals, 0.55, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.4, pctc(v), ha="center", fontsize=8, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.4)
    ax.set_ylim(0, 17); ax.set_yticklabels([])
    ax.text(0.5, 3.0, "el precio descuenta\nMENOS que el peor\ncaso creíble", ha="center", fontsize=6.8, color=GRIS, style="italic")
    deco(ax, "El precio descuenta una desaceleración fuerte",
         "Crecimiento de owner earnings implícito en US$384 vs. referencias (%)",
         "Fuente: DCF inverso (val-mos), WACC 8% y margen base fijos. SUPUESTO. Expectativas modestas = la oportunidad.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "10_dcf_inverso")

# ── 11 · ROIC con y sin goodwill (declive de fase) ───────────────────────
def c11():
    x = np.arange(len(D.ROIC_YRS))
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    ax.plot(x, D.ROIC_EXGW, color=VERDE, lw=2.2, marker="o", ms=5, label="ROIC ex-goodwill")
    ax.plot(x, D.ROIC_GW, color=AZUL, lw=2.2, marker="s", ms=5, label="ROIC con goodwill")
    for i, v in enumerate(D.ROIC_EXGW):
        ax.text(i, v + 2, f"{D.es(v,1)}%", ha="center", fontsize=7.2, color=VERDE)
    for i, v in enumerate(D.ROIC_GW):
        ax.text(i, v - 4, f"{D.es(v,1)}%", ha="center", fontsize=7.2, color=AZUL)
    ax.axhline(9, color=ROJO, lw=1.2, ls=(0, (4, 2)))
    ax.text(0.05, 11, "WACC ~9%", fontsize=7, color=ROJO)
    ax.set_xticks(x); ax.set_xticklabels(D.ROIC_YRS, fontsize=8.2)
    ax.set_ylim(0, 82); ax.set_yticks([20, 40, 60, 80]); ax.set_yticklabels(["20%", "40%", "60%", "80%"], fontsize=7)
    ax.legend(fontsize=7.4, loc="upper right", frameon=False)
    deco(ax, "El ROIC cae — pero sigue tres veces el coste de capital",
         "Retorno sobre capital invertido, con y sin goodwill (%) · descenso de FASE de inversión, no secular",
         "Fuente: cálculo propio sobre 10-K. INFERENCIA. La caída es capex IA + goodwill Activision; sigue de élite.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "11_roic")

# ── 12 · Porter por segmento (/25, menor = mejor foso) ───────────────────
def c12():
    labs = [s[0] for s in D.PORTER_SEG]; vals = [s[1] for s in D.PORTER_SEG]
    y = np.arange(len(labs))[::-1]
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    for yi, (nm, v) in zip(y, D.PORTER_SEG):
        col = VERDE if v <= 9 else (OCRE if v <= 14 else ROJOSC)
        ax.barh(yi, v, 0.6, color=col)
        ax.text(v + 0.3, yi, f"{v}/25", va="center", fontsize=8, color=TINTA, fontweight="bold")
        ax.text(-0.3, yi, nm, va="center", ha="right", fontsize=8, color=TINTA)
    ax.axvline(D.PORTER_POND, color=NOCHE, lw=1.2, ls=(0, (4, 2)))
    ax.text(D.PORTER_POND + 0.2, -0.7, f"ponderado {D.es(D.PORTER_POND,1)}", fontsize=6.8, color=NOCHE)
    ax.set_xlim(0, 22); ax.set_ylim(-1, len(labs) - 0.4); ax.set_yticks([])
    ax.set_xticks([5, 10, 15, 20]); ax.set_xticklabels(["5", "10", "15", "20"], fontsize=7)
    deco(ax, "Cinco Fuerzas de Porter, foso por foso",
         "Score /25 por segmento (menor = mejor foso) · los motores de valor (M365, LinkedIn) tienen los fosos más anchos",
         "Fuente: análisis propio. Los frentes disputados (IA, Gaming, 14–15) son los de menor contribución al beneficio hoy.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10, left=0.24)
    save(fig, "12_porter")

# ── 13 · TAM por mercado + penetración + SOM ─────────────────────────────
def c13():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    y = np.arange(len(D.MERCADOS))[::-1]
    LX = 690   # columna fija de etiquetas a la derecha
    for yi, (nm, tam, msft, som) in zip(y, D.MERCADOS):
        ax.barh(yi, tam, 0.62, color=CIELO, alpha=0.6)
        ax.barh(yi, msft, 0.62, color=AZUL)
        ax.text(-15, yi, nm, va="center", ha="right", fontsize=7.4, color=TINTA)
        ax.text(LX, yi, f"TAM ${tam}B · MSFT ${msft}B · SOM'30 {som}", va="center", fontsize=6.2, color=GRIS)
    ax.set_xlim(0, 1040); ax.set_ylim(-0.7, len(D.MERCADOS) - 0.3); ax.set_yticks([])
    ax.set_xticks([200, 400, 600]); ax.set_xticklabels(["$200B", "$400B", "$600B"], fontsize=7)
    deco(ax, "El TAM más amplio del mercado cotizado",
         "TAM 2026 (claro) vs ingreso MSFT hoy (oscuro), US$B · líder o nº1 en 4 de 6 mercados, penetración baja en IA",
         f"Fuente: IDC/Grand View + 10-K. INFERENCIA. TAM agregado ~US${D.TAM_TOTAL/1000:.1f}T (2026) → ~US${D.TAM_2030/1000:.1f}T (2030).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.09, left=0.175, right=0.995)
    save(fig, "13_tam")

# ── 14 · Radar de management (6 dimensiones) ─────────────────────────────
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
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=7.0, color=TINTA)
    ax.set_ylim(0, 5); ax.set_yticks([1, 2, 3, 4, 5]); ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Gestión: 6 dimensiones",
         f"Puntuación 1–5 por dimensión · total {D.es(D.MGMT_TOTAL,1)}/30 · el SBC NO se recuenta aquí (va en R9)",
         "Fuente: DEF 14A 2025 + 10-K. Nadella/Hood élite; deméritos: ownership <1% e incógnita del capex de $190B.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10, left=0.10, right=0.90)
    save(fig, "14_mgmt")

# ── 15 · Heatmap de riesgos numerado + leyenda ───────────────────────────
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
        fig.text(0.66, ly + 0.012, nm, fontsize=6.6, color=TINTA, va="center")
        fig.text(0.66, ly - 0.028, f"prob {pr} × impacto {im} = {sev}", fontsize=6.1, color=col, va="center", style="italic")
        ly -= 0.108
    deco(ax, "Matriz de riesgos",
         "Probabilidad × impacto (1–5) · el riesgo dominante (1) es que el capex de IA no gane su coste de capital",
         "Fuente: análisis propio. Todo se resuelve con datos de ~8 trimestres, no con narrativa.", fig=fig)
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
    ax.text(0.2, -1.15, "verde = comprar · navy = mantener · ocre = pass", fontsize=6.6, color=GRIS, style="italic")
    deco(ax, "Nueve leyendas opinan",
         "Convicción /10 · consenso de compra amplio; la divergencia (Graham pasa) es la señal",
         "Fuente: doctrina de cada inversor aplicada por el autor. INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.13, left=0.16)
    save(fig, "16_inversores")

# ── 17 · Construcción del WACC ───────────────────────────────────────────
def c17():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    pasos = ["Tasa libre\nde riesgo", f"+ Prima ×\nbeta {D.es(D.BETA,2)}", "= Coste de\nequity (CAPM)", "Ajuste tier\n(Núcleo)", "= WACC\nusado"]
    coe = D.COE_CAPM
    cols = [CIELO, ACERO, AZUL, OCRE, ROJO]
    ax.bar(0, D.RF, 0.6, color=cols[0])
    ax.bar(1, D.BETA * D.ERP, 0.6, bottom=D.RF, color=cols[1])
    ax.bar(2, coe, 0.6, color=cols[2])
    ax.bar(3, coe - D.WACC, 0.6, bottom=D.WACC, color=cols[3])
    ax.bar(4, D.WACC, 0.6, color=cols[4])
    labels = [pctc(D.RF), pctc(D.BETA * D.ERP), pctc(coe), f"−{D.es(coe-D.WACC,1)}", pctc(D.WACC)]
    tops = [D.RF, coe, coe, coe, D.WACC]
    for i in range(5):
        ax.text(i, tops[i] + 0.2, labels[i], ha="center", fontsize=7.4, color=TINTA,
                fontweight="bold" if i in (2, 4) else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels(pasos, fontsize=7.0)
    ax.set_ylim(0, 12); ax.set_yticklabels([])
    deco(ax, "El WACC, ladrillo a ladrillo",
         f"Coste de capital (%) · CAPM ~{D.es(coe,1)}%, anclado a {D.es(D.WACC,1)}% por tier Núcleo (calidad + caja neta)",
         f"Fuente: modelo propio (val-mos). rf {D.es(D.RF,2)}% · ERP {D.es(D.ERP,1)}% · beta {D.es(D.BETA,2)} · deuda mínima.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "17_wacc")

# ── 18 · Sensibilidad WACC × g terminal ──────────────────────────────────
def c18():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    M = np.array(D.SENS)
    cmap = LinearSegmentedColormap.from_list("qg", [ROJOSC, GCLARO, NOCHE])
    ax.imshow(M, cmap=cmap, aspect="auto")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            base = (D.WACC_GRID[i] == D.WACC and D.GT_GRID[j] == D.TERMINAL)
            ax.text(j, i, f"{M[i, j]}", ha="center", va="center", fontsize=7.8,
                    color="white" if M[i, j] > 560 or M[i, j] < 470 else TINTA,
                    fontweight="bold" if base else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels([pctc(g) for g in D.GT_GRID], fontsize=7.2)
    ax.set_yticks(range(5)); ax.set_yticklabels([pctc(w) for w in D.WACC_GRID], fontsize=7.2)
    ax.set_xlabel("Crecimiento terminal", fontsize=7.8, color=GRIS)
    ax.set_ylabel("WACC", fontsize=7.8, color=GRIS)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    deco(ax, "El valor bajo estrés",
         "Valor DCF base por acción (US$) según WACC × crecimiento terminal · negrita = caso central",
         f"Fuente: modelo propio. SUPUESTO. Aun en el peor cuadrante (US${D.SENS_MIN}) el valor supera el precio de hoy (US${int(D.PRECIO)}).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.10, right=0.98)
    save(fig, "18_sensibilidad")

# ── 19 · RPO backlog + concentración OpenAI ──────────────────────────────
def c19():
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    openai = D.RPO * D.OPENAI_RPO / 100
    resto = D.RPO - openai
    ax.barh(0, resto, 0.5, color=AZUL, label="Resto de clientes")
    ax.barh(0, openai, 0.5, left=resto, color=ROJOSC, label=f"OpenAI (~{D.OPENAI_RPO}%)")
    ax.text(resto / 2, 0, f"US${resto:.0f}B", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    ax.text(resto + openai / 2, 0, f"US${openai:.0f}B", ha="center", va="center", fontsize=8, color="white", fontweight="bold")
    ax.set_xlim(0, D.RPO * 1.05); ax.set_ylim(-0.6, 0.6); ax.set_yticks([])
    ax.set_xticks([0, 200, 400, 600]); ax.set_xticklabels(["0", "$200B", "$400B", "$600B"], fontsize=7)
    ax.legend(fontsize=7.4, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.18))
    deco(ax, "Visibilidad enorme — con un talón de Aquiles",
         f"Backlog contractual (RPO) US${D.RPO}B, +{D.RPO_YOY}% · ~2,3× el ingreso anual · pero el {D.OPENAI_RPO}% depende de OpenAI",
         "Fuente: 10-Q Q3 FY26. HECHO. OpenAI pierde ~$14B/año y diversifica a Oracle/AWS: el mayor riesgo de contraparte.",
         fig=fig, flag_y=0.95)
    fig.subplots_adjust(top=0.70, bottom=0.14)
    save(fig, "19_rpo")

# ── 20 · Dashboard de early warning ──────────────────────────────────────
def c20():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    filas = [
        ("Azure (moneda constante)", "+39% (acelerando)", "< +25% cc", VERDE),
        ("Microsoft Cloud gross margin", "66% (−300pb)", "< 63–64% estructural", OCRE),
        ("Intelligent Cloud op. margin", "39,7% (−180pb)", "cae sin fin del capex", OCRE),
        ("Capex / ventas (plateau)", "30,5% (subiendo)", "no hace plateau FY27-28", OCRE),
        ("FCF económico (con leases)", "~$51B", "< $45B", OCRE),
        ("RPO concentración OpenAI", "~45%", "OpenAI renegocia/recorta", OCRE),
        ("Margen operativo consolidado", "46,8% (récord)", "cae bajo 44%", VERDE),
    ]
    ax.axis("off")
    y0 = 1.0; dh = 1.0 / (len(filas) + 1)
    ax.text(0.02, y0, "Indicador (VI.7)", fontsize=7.6, fontweight="bold", color=NOCHE, transform=ax.transAxes)
    ax.text(0.50, y0, "Estado hoy", fontsize=7.6, fontweight="bold", color=NOCHE, transform=ax.transAxes)
    ax.text(0.78, y0, "Umbral rojo", fontsize=7.6, fontweight="bold", color=NOCHE, transform=ax.transAxes)
    for i, (nm, est, umb, col) in enumerate(filas):
        y = y0 - (i + 1) * dh
        ax.add_patch(Rectangle((0.0, y - dh*0.42), 1.0, dh*0.84, transform=ax.transAxes,
                     color=P["panel"] if i % 2 else P["fondo"], zorder=0))
        ax.scatter(0.005, y, s=60, color=col, transform=ax.transAxes, zorder=3, clip_on=False)
        ax.text(0.03, y, nm, fontsize=7.0, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.50, y, est, fontsize=7.0, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.78, y, umb, fontsize=6.7, color=GRIS, va="center", transform=ax.transAxes)
    deco(ax, "Sistema de alerta temprana (fase capex IA)",
         "Semáforo · verde = sano · ámbar = vigilar · el jurado del ROIC incremental delibera ~8 trimestres",
         "Fuente: KPIs primarios MSFT. La tesis se refuta si 2+ ámbar viran a rojo → capex atrapado, no de fase.",
         fig=fig, flag_y=0.97)
    fig.subplots_adjust(top=0.80, bottom=0.05, left=0.02, right=0.98)
    save(fig, "20_early_warning")

if __name__ == "__main__":
    fns = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10,
           c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]
    for fn in fns:
        fn(); print("ok", fn.__name__)
    print("charts done:", len(fns))
