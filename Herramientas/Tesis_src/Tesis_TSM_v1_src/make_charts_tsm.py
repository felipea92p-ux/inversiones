# -*- coding: utf-8 -*-
"""Gráficos Ultra Tesis TSM — importan dcf_tsm (fuente de verdad) y chart_style."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap
from chart_style import deco, save, P
import dcf_tsm as D

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
         "Puntuación 0–10 por regla · R6 (concentración geopolítica) es el único punto débil real",
         f"Fuente: qg-seilern + verificación adversarial (6-jul-2026). Raw {D.es(D.RAW_QG,1)}/125 → {D.es(D.SCORE_QG,1)}/100 · tier Alta Convicción.",
         fig=fig)
    fig.subplots_adjust(top=0.74, bottom=0.08, left=0.06, right=0.94)
    save(fig, "01_radar")

# ── 02 · Márgenes en expansión constante ──────────────────────────────────
def c02():
    x = np.arange(len(D.YRS_FIN))
    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    ax.plot(x, D.GROSS_MGN, color=ACERO, lw=2.0, marker="o", ms=4, label="Bruto")
    ax.plot(x, D.OP_MGN, color=AZUL, lw=2.0, marker="s", ms=4, label="Operativo")
    ax.plot(x, D.NET_MGN, color=ROJO, lw=2.0, marker="^", ms=4, label="Neto")
    for i, v in enumerate(D.GROSS_MGN):
        ax.text(i, v + 2, pctc(v), fontsize=6.6, color=ACERO, ha="center")
    ax.set_xticks(x); ax.set_xticklabels(D.YRS_FIN, fontsize=8.2)
    ax.set_ylim(0, 78); ax.set_yticklabels([])
    ax.legend(fontsize=7.6, loc="lower right", frameon=False)
    deco(ax, "Márgenes en expansión constante — ningún trimestre de deterioro",
         "Margen bruto / operativo / neto (%) FY23→Q1'26",
         "Fuente: Form 20-F FY2025 + earnings release Q1'26. HECHO. El detector de trampas da PASA limpio.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "02_margenes")

# ── 03 · HPC/IA domina el mix de ingresos ─────────────────────────────────
def c03():
    x = np.arange(len(D.PLAT_YRS))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.bar(x, D.PLAT_HPC, 0.55, color=AZUL, label="HPC / IA")
    ax.bar(x, D.PLAT_SMARTPHONE, 0.55, bottom=D.PLAT_HPC, color=GCLARO, label="Smartphone")
    for i, v in enumerate(D.PLAT_HPC):
        ax.text(i, v/2, f"{v}%", ha="center", fontsize=7.6, color="white", fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(D.PLAT_YRS, fontsize=8.2)
    ax.set_ylim(0, 100); ax.set_yticklabels([])
    ax.legend(fontsize=7.6, loc="upper left", frameon=False)
    deco(ax, "HPC/IA ya es el 61% del ingreso — y sigue creciendo",
         "Ingreso por plataforma (%) · el smartphone, antes el motor, ahora decrece en participación",
         "Fuente: Form 20-F FY2025. HECHO. HPC creció 48% YoY (2025) en NT$ absolutos.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "03_plataformas")

# ── 04 · Concentración de clientes converge ───────────────────────────────
def c04():
    x = np.arange(len(D.TOP10_YRS))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.plot(x, D.CLIENTE1_PCT, color=ROJOSC, lw=2.0, marker="o", ms=5, label="Cliente 1 (declinante)")
    ax.plot(x, D.CLIENTE2_PCT, color=AZUL, lw=2.0, marker="s", ms=5, label="Cliente 2 (creciendo)")
    for i, v in enumerate(D.CLIENTE1_PCT):
        ax.text(i, v + 1, f"{v}%", fontsize=7.4, color=ROJOSC, ha="center", fontweight="bold")
    for i, v in enumerate(D.CLIENTE2_PCT):
        ax.text(i, v - 2.4, f"{v}%", fontsize=7.4, color=AZUL, ha="center", fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(D.TOP10_YRS, fontsize=8.2)
    ax.set_ylim(0, 30); ax.set_yticklabels([])
    ax.legend(fontsize=7.4, loc="center left", frameon=False)
    ax.text(1, 24, f"Top-10 clientes = {D.TOP10_PCT[-1]}% del ingreso (2025)", fontsize=7.4, color=NOCHE,
            bbox=dict(boxstyle="round,pad=0.4", fc=PANEL, ec=GLIN, lw=0.8))
    deco(ax, "Dos clientes convergen hacia ~el 20% cada uno",
         "% de ingreso por cliente principal (no nombrados en el 20-F; mercado los asume Apple/Nvidia)",
         "Fuente: Form 20-F FY2025 (no divulga nombres). HECHO. Es el principal detractor de R6.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "04_concentracion_clientes")

# ── 05 · Foundry share — TSM gana terreno ─────────────────────────────────
def c05():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    labs = ["TSM", "Samsung", "SMIC", "UMC", "GlobalFoundries"]
    vals = [72.3, 6.5, 5.1, 3.9, 3.3]
    cols = [ROJOSC, ACERO, GCLARO, GCLARO, GCLARO]
    ax.bar(range(5), vals, 0.6, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 1.5, pctc(v), ha="center", fontsize=8, fontweight="bold", color=TINTA)
    ax.set_xticks(range(5)); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 84); ax.set_yticklabels([])
    deco(ax, "El resto de la industria combinada no iguala a TSM",
         "Cuota del mercado global de foundry pure-play (%), Q1 2026 · TSM gana cuota, no la pierde",
         "Fuente: TrendForce/Semiecosystem (terceros). HECHO. Cuota de punta (&lt;5nm) proyectada &gt;92% para fin de 2026.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "05_foundry_share")

# ── 06 · CoWoS: el cuello de botella real de la IA ────────────────────────
def c06():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    labs = ["2024", "2026e", "2027e"]
    vals = [D.COWOS_2024, D.COWOS_2026E, D.COWOS_2027E]
    ax.bar(range(3), vals, 0.5, color=[GCLARO, ACERO, AZUL])
    for i, v in enumerate(vals):
        ax.text(i, v + 4, f"{v}k", ha="center", fontsize=9, fontweight="bold", color=TINTA)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 200); ax.set_yticklabels([])
    ax.text(0.5, 150, "Capacidad vendida hasta 2027\nNvidia solo reservó &gt;50% del total 2026-27",
            ha="center", fontsize=7.4, color=NOCHE,
            bbox=dict(boxstyle="round,pad=0.5", fc=PANEL, ec=GLIN, lw=0.8))
    deco(ax, "No es la oblea — es el empaquetado avanzado",
         "Capacidad de CoWoS (miles de obleas/mes, estimado externo) · TSM controla la puerta, no el cliente",
         "Fuente: estimados de industria (terceros, no divulgado en 20-F). INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "06_cowos")

# ── 07 · DCF 3 escenarios (con prima geopolítica) ─────────────────────────
def c07():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    labs = [f"Conservador\n({D.P_BEAR}%)", f"Base\n({D.P_BASE}%)", f"Optimista\n({D.P_BULL}%)"]
    vals = [D.V_BEAR, D.V_BASE, D.V_BULL]; cols = [ROJOSC, AZUL, VERDE]
    x = np.arange(3); ax.bar(x, vals, 0.5, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 8, f"US${v}", ha="center", fontsize=8.6, fontweight="bold", color=TINTA)
    ax.axhline(D.PRECIO, color=TINTA, lw=1.6)
    ax.text(0.02, D.PRECIO + 8, f"HOY US${D.es(D.PRECIO,0)} — zona {D.ZONA_HOY}",
            fontsize=7.6, color=TINTA, fontweight="bold")
    ax.axhline(D.PWFV, color=ROJO, lw=1.4, ls=(0, (5, 3)))
    ax.text(2.55, D.PWFV + 8, f"PWFV US${D.PWFV}", va="bottom", ha="right", fontsize=7.6, color=ROJO)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 480); ax.set_yticklabels([])
    deco(ax, "El precio hoy duplica incluso el caso optimista con riesgo país",
         f"Valor por ADR del DCF sobre owner earnings (US$) · WACC {D.es(D.WACC,2)}% (con prima geopolítica)",
         f"Fuente: modelo propio (val-mos). SUPUESTO. Sin prima geopolítica, PWFV sería US${D.PWFV_SIN_PRIMA} (aun así, Caro).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "07_dcf")

# ── 08 · Mapa de zonas ────────────────────────────────────────────────────
def c08():
    fig, ax = plt.subplots(figsize=(7.6, 2.8))
    lo, hi = 100, 480
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
         f"Zonas ancladas al PWFV US${D.PWFV} (con prima geopolítica) · HOY US${D.es(D.PRECIO,0)} = {D.ZONA_HOY}",
         f"Fuente: val-mos v3. El candado de expectativas (HEROICAS) exige zona Ganga, no solo Oportunidad.",
         fig=fig, flag_y=0.96)
    fig.subplots_adjust(top=0.64, bottom=0.06)
    save(fig, "08_zonas")

# ── 09 · Candado duro ──────────────────────────────────────────────────────
def c09():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    labs = ["Techo del tier\n(Alta Convicción)", "Múltiplo FY26e\n(owner earnings)", "Múltiplo FY25\ntrailing"]
    vals = [D.TECHO_MULT_TIER, D.MULT_FY26E, D.MULT_NORMALIZADO]
    cols = [VERDE, OCRE, ROJOSC]
    x = np.arange(3); ax.bar(x, vals, 0.5, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 1.6, f"{D.es(v,1)}x", ha="center", fontsize=9, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.8)
    ax.set_ylim(0, 84); ax.set_yticklabels([])
    ax.annotate("1,7x-2,5x\nsobre el techo", xy=(1.5, 66), fontsize=7.4, color=ROJOSC, ha="center", style="italic")
    deco(ax, "El candado duro: violado incluso con el año más favorable (2026e)",
         "Múltiplo pagado hoy sobre owner earnings vs. el techo de múltiplo del tier de TSM (30x)",
         "Fuente: val-mos v3 (candado anti-sobrepago, sin excepción de tier). No tiene excepción por patrón.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "09_candado_duro")

# ── 10 · DCF inverso ──────────────────────────────────────────────────────
def c10():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["Conservador\npropio", "Implícito\n(sin prima)", "Implícito\n(con prima)", "Guidance\nmanagement"]
    vals = [D.G_CONS, D.G_IMPL_SIN_PRIMA, D.G_IMPL, D.G_GUIA]
    cols = [OCRE, TERRA, ROJO, ACERO]
    x = np.arange(4); ax.bar(x, vals, 0.55, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.8, pctc(v), ha="center", fontsize=8, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.6)
    ax.set_ylim(0, 42); ax.set_yticklabels([])
    deco(ax, "El precio exige superar hasta el propio guidance ya elevado",
         "Crecimiento de owner earnings implícito en el precio de referencia (~US$477) vs. referencias (%)",
         f"Fuente: DCF inverso (val-mos). SUPUESTO. Clasificación: {D.DCF_CLASE} en ambos escenarios de WACC.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "10_dcf_inverso")

# ── 11 · WACC — la prima geopolítica lo cambia todo ──────────────────────
def c11():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    coe = D.COE_CAPM
    pasos = ["Tasa libre\nde riesgo", f"+ Prima ×\nbeta {D.es(D.BETA,2)}", "= CAPM\n(sin prima)", "+ Prima\ngeopolítica", "= WACC\ncon prima"]
    cols = [CIELO, ACERO, AZUL, ROJOSC, ROJO]
    ax.bar(0, D.RF, 0.6, color=cols[0])
    ax.bar(1, D.BETA * D.ERP, 0.6, bottom=D.RF, color=cols[1])
    ax.bar(2, coe, 0.6, color=cols[2])
    ax.bar(3, D.WACC - coe, 0.6, bottom=coe, color=cols[3])
    ax.bar(4, D.WACC, 0.6, color=cols[4])
    labels = [pctc(D.RF), pctc(D.BETA * D.ERP), pctc(coe), f"+{D.es(D.WACC-coe,2)}", pctc(D.WACC)]
    tops = [D.RF, coe, coe, D.WACC, D.WACC]
    for i in range(5):
        ax.text(i, tops[i] + 0.25, labels[i], ha="center", fontsize=7.2, color=TINTA,
                fontweight="bold" if i in (2, 4) else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels(pasos, fontsize=6.8)
    ax.set_ylim(0, 15); ax.set_yticklabels([])
    deco(ax, "+250pb de prima geopolítica mueven el PWFV −34%",
         f"Coste de capital (%) · CAPM sin prima ~{D.es(coe,2)}%, con prima {D.es(D.WACC,2)}%",
         f"Fuente: modelo propio (val-mos). El PWFV pasa de US${D.PWFV_SIN_PRIMA} a US${D.PWFV} solo por este ajuste.", fig=fig)
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
            base = (abs(D.WACC_GRID[i] - D.WACC) < 0.01 and D.GT_GRID[j] == D.TERMINAL)
            ax.text(j, i, f"{M[i, j]}", ha="center", va="center", fontsize=7.8,
                    color="white" if M[i, j] > 320 or M[i, j] < 210 else TINTA,
                    fontweight="bold" if base else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels([pctc(g) for g in D.GT_GRID], fontsize=7.2)
    ax.set_yticks(range(5)); ax.set_yticklabels([pctc(w) for w in D.WACC_GRID], fontsize=7.2)
    ax.set_xlabel("Crecimiento terminal", fontsize=7.8, color=GRIS)
    ax.set_ylabel("WACC (incl. prima geopolítica)", fontsize=7.6, color=GRIS)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    deco(ax, "El valor bajo estrés — ninguna celda alcanza el precio de hoy",
         "Valor DCF base por ADR (US$) según WACC × terminal · negrita = caso central",
         f"Fuente: modelo propio. SUPUESTO. Rango US${D.SENS[-1][0]}-{D.SENS_MAX}: siempre por debajo del precio hoy.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.16, left=0.12, right=0.98)
    save(fig, "12_sensibilidad")

# ── 13 · Porter (fuerzas, no segmentos) ───────────────────────────────────
def c13():
    y = np.arange(len(D.PORTER_FUERZAS))[::-1]
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    for yi, (nm, v) in zip(y, D.PORTER_FUERZAS):
        col = VERDE if v <= 2 else (OCRE if v <= 3 else ROJOSC)
        ax.barh(yi, v, 0.55, color=col)
        ax.text(v + 0.08, yi, f"{v}/5", va="center", fontsize=8, color=TINTA, fontweight="bold")
        ax.text(-0.1, yi, nm, va="center", ha="right", fontsize=7.6, color=TINTA)
    ax.axvline(D.PORTER_POND, color=NOCHE, lw=1.2, ls=(0, (4, 2)))
    ax.text(D.PORTER_POND + 0.05, -0.75, f"ponderado {D.es(D.PORTER_POND,1)}", fontsize=6.8, color=NOCHE)
    ax.set_xlim(0, 5.2); ax.set_ylim(-1, len(D.PORTER_FUERZAS) - 0.4); ax.set_yticks([])
    ax.set_xticks([1, 2, 3, 4, 5]); ax.set_xticklabels(["1", "2", "3", "4", "5"], fontsize=7)
    deco(ax, "Cinco Fuerzas de Porter: posición casi ideal, salvo el proveedor",
         "Score /5 (menor = mejor foso) · ASML (monopolio EUV) es la única fuerza claramente adversa",
         "Fuente: análisis propio. TSM es cliente prioritario de ASML, lo que mitiga parcialmente la dependencia.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11, left=0.42)
    save(fig, "13_porter")

# ── 14 · TAM ──────────────────────────────────────────────────────────────
def c14():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    y = np.arange(len(D.MERCADOS))[::-1]
    LX = 145
    for yi, (nm, tam, gg, nota) in zip(y, D.MERCADOS):
        ax.barh(yi, tam, 0.6, color=CIELO, alpha=0.6)
        ax.barh(yi, gg, 0.6, color=AZUL)
        ax.text(-3, yi, nm.replace("&lt;", "<"), va="center", ha="right", fontsize=7.2, color=TINTA)
        ax.text(LX, yi, f"TAM ${tam}B · TSM ${gg}B · {nota}".replace("&gt;", ">"), va="center", fontsize=6.4, color=GRIS)
    ax.set_xlim(0, 230); ax.set_ylim(-0.7, len(D.MERCADOS) - 0.3); ax.set_yticks([])
    ax.set_xticks([50, 100, 150]); ax.set_xticklabels(["$50B", "$100B", "$150B"], fontsize=7)
    deco(ax, "TSM ya captura la mayoría del mercado que importa",
         "TAM 2026 (claro) vs ingreso capturado por TSM (oscuro), US$B",
         "Fuente: estimados de industria + Form 20-F. INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.09, left=0.24, right=0.98)
    save(fig, "14_tam")

# ── 15 · Radar de management ──────────────────────────────────────────────
def c15():
    labs = [n for n, _ in D.MGMT]; vals = [v for _, v in D.MGMT]
    N = len(vals); ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    v = vals + vals[:1]; a = ang + ang[:1]
    fig = plt.figure(figsize=(7.6, 5.2)); ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.plot(a, v, color=AZUL, lw=1.8); ax.fill(a, v, color=AZUL, alpha=0.16)
    for ai, vi in zip(ang, vals):
        ax.scatter(ai, vi, color=AZUL, s=30, zorder=5)
        ax.text(ai, vi + 0.35, D.es(vi, 1), ha="center", fontsize=7.4, color=TINTA)
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=6.2, color=TINTA)
    ax.set_ylim(0, 5); ax.set_yticks([1, 2, 3, 4, 5]); ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Gestión: ejecución excelente, con dos frenos estructurales",
         f"Puntuación 1–5 · total {D.es(D.MGMT_TOTAL,1)}/30 · Presidente+CEO combinado desde jun-2024, Estado taiwanés {D.es(D.TAIWAN_GOB_STAKE,2)}%",
         "Fuente: 20-F + prensa. C.C. Wei ejecuta con solidez; la instrumentalidad geopolítica es un límite estructural.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10, left=0.10, right=0.90)
    save(fig, "15_mgmt")

# ── 16 · El descuento geopolítico se encoge justo cuando no debería ──────
def c16():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["EV/EBITDA hoy", "Mediana 10 años"]
    vals = [D.EV_EBITDA, D.EV_EBITDA_MEDIANA_10A]
    ax.bar([0, 1], vals, 0.42, color=[ROJOSC, ACERO])
    for i, v in enumerate(vals):
        ax.text(i, v + 0.6, f"{D.es(v,1)}x", ha="center", fontsize=10, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 26); ax.set_yticklabels([])
    ax.annotate("+124%\nsobre la mediana", xy=(0.5, 15), fontsize=8.6, color=ROJOSC, fontweight="bold", ha="center")
    deco(ax, "El múltiplo está muy por encima de su propia historia",
         "EV/EBITDA hoy vs. mediana de 10 años · una segunda métrica, sin relación con el DCF, confirma el estiramiento",
         "Fuente: GuruFocus. HECHO. Coincide con el hallazgo del DCF inverso (HEROICAS).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "16_ev_ebitda")

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
        fig.text(0.66, ly + 0.012, nm.replace("&gt;", ">"), fontsize=6.2, color=TINTA, va="center")
        fig.text(0.66, ly - 0.028, f"prob {pr} × impacto {im} = {sev}", fontsize=6.0, color=col, va="center", style="italic")
        ly -= 0.108
    deco(ax, "Matriz de riesgos",
         "Probabilidad × impacto (1–5) · el bloqueo de Taiwán es el único de impacto máximo",
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
    ax.text(0.2, -1.15, "navy = mantener · ocre = pass · el negocio convence, el precio no", fontsize=6.6, color=GRIS, style="italic")
    deco(ax, "Nueve leyendas opinan",
         "Convicción /10 · el freno es 100% de precio, no de negocio",
         "Fuente: doctrina de cada inversor aplicada por el autor. INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.13, left=0.16)
    save(fig, "18_inversores")

# ── 19 · Cuota vs. ceremonia geopolítica (silicon shield / trap) ─────────
def c19():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    labs = ["Concesión de armas\nEEUU-Taiwán ($14.000M)", "Compra en $2.474.000M\n(múltiplo actual)"]
    vals = [1, 5]  # illustrative scale for narrative framing, not numeric data
    ax.axis("off")
    ax.text(0.5, 0.75, "El descuento geopolítico se ENCOGE en 2026", ha="center", fontsize=11,
            fontweight="bold", color=TINTA, transform=ax.transAxes)
    ax.text(0.5, 0.55, "mientras el riesgo subyacente NO mejora:", ha="center", fontsize=9,
            color=NOCHE, transform=ax.transAxes)
    hechos = [
        "Ene-2026: simulacro de cerco militar chino a Taiwán",
        "Xi: \"la reunificación es imparable\"",
        "Paquete de US$14.000M en armas a Taiwán, retrasado por Trump — \"ficha de negociación\" con Xi",
        "Ex-presidente de TSMC confirmó plan de auto-inutilización de las fábricas ante invasión",
    ]
    y = 0.42
    for h in hechos:
        ax.text(0.06, y, f"• {h}", fontsize=7.6, color=TINTA, transform=ax.transAxes, va="top")
        y -= 0.11
    deco(ax, "El riesgo de Taiwán no ha mejorado — el precio actúa como si lo hubiera hecho",
         "Síntesis narrativa · el mercado reduce la prima de riesgo justo cuando la evidencia no lo justifica",
         "Fuente: prensa (Reuters/AP/Al Jazeera), 20-F FY2025. HECHO. Es la variable que R6 y el WACC capturan.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.06)
    save(fig, "19_riesgo_taiwan")

# ── 20 · Dashboard de early warning ──────────────────────────────────────
def c20():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    filas = [
        ("Margen operativo consolidado", "58,1% (récord)", "cae &lt; 45% sostenido", VERDE),
        ("Ingreso HPC/IA (crecimiento)", "+48% YoY (2025)", "&lt; 25% sostenido 2+ trim.", VERDE),
        ("ROE (anualizado)", "40,5% (récord)", "cae &lt; 25%", VERDE),
        ("EV/EBITDA vs mediana 10a", "+124% (estirado)", "sigue expandiéndose sin pausa", OCRE),
        ("Concentración top-2 clientes", "36% (convergiendo)", "supera 45% combinado", OCRE),
        ("2da venta de Samsung a cliente top-10", "1 caso (Tesla AI6)", "2do caso confirmado en 4-6 trim.", OCRE),
        ("Riesgo geopolítico Taiwán/China", "drills + retraso de armas EEUU", "hecho estructural, no transitorio", "rojo"),
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
        ax.text(0.03, y, nm.replace("&lt;", "<"), fontsize=6.6, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.47, y, est, fontsize=6.6, color=TINTA, va="center", transform=ax.transAxes)
        ax.text(0.78, y, umb.replace("&lt;", "<"), fontsize=6.2, color=GRIS, va="center", transform=ax.transAxes)
    deco(ax, "Sistema de alerta temprana",
         "Semáforo · el negocio (verde) es excelente; la valoración y la geopolítica (ámbar/rojo) son las tensiones reales",
         "Fuente: KPIs primarios TSM. La fila roja no es una alerta transitoria: es un hecho estructural permanente.",
         fig=fig, flag_y=0.97)
    fig.subplots_adjust(top=0.80, bottom=0.05, left=0.02, right=0.98)
    save(fig, "20_early_warning")

if __name__ == "__main__":
    fns = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10,
           c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]
    for fn in fns:
        fn(); print("ok", fn.__name__)
    print("charts done:", len(fns))
