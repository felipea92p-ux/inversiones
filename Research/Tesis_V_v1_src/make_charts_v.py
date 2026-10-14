# -*- coding: utf-8 -*-
"""Gráficos Ultra Tesis V (Visa) — importan dcf_v (fuente de verdad) y chart_style."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap
from chart_style import deco, save, P
import dcf_v as D

plt.rcParams["text.parse_math"] = False

AZUL, NOCHE, ACERO, CIELO = P["azul"], P["azul_noche"], P["azul_acero"], P["azul_cielo"]
ROJO, ROJOSC, VERDE, OCRE, TERRA, GRIS = (P["rojo"], P["rojo_oscuro"], P["verde"],
    P["ocre"], P["terracota"], P["gris"])
TINTA, GLIN, GCLARO, PANEL = P["tinta"], P["gris_linea"], P["gris_claro"], P["panel"]
pctc = lambda x: D.es(x, 1) + "%"

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
         "Puntuación 0–10 por regla · R7 (capital/ROIC) en 10/10 — Visa es ancla de calibración del sistema",
         f"Fuente: qg-seilern + verificación adversarial (6-jul-2026). Raw {D.es(D.RAW_QG,2)}/125 → {D.es(D.SCORE_QG,1)}/100 · tier Alta convicción.",
         fig=fig)
    fig.subplots_adjust(top=0.74, bottom=0.08, left=0.06, right=0.94)
    save(fig, "01_radar")

def c02():
    labs = [s[0] for s in D.SEG]; rev = [s[1]/1000 for s in D.SEG]
    x = np.arange(len(labs))
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    cols = [AZUL, VERDE, OCRE, GCLARO]
    ax.bar(x, rev, 0.55, color=cols)
    for i, v in enumerate(rev):
        ax.text(i, v + 0.3, f"US${D.es(v,1)}B", ha="center", fontsize=7.8, color=TINTA, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.0)
    ax.set_ylim(0, 23); ax.set_yticklabels([])
    deco(ax, "Cuatro líneas de ingreso, todas creciendo de doble dígito",
         "Ingreso bruto FY2025 por línea, US$B",
         "Fuente: 10-K FY2025. HECHO. Data processing es la mayor línea; el ingreso internacional, la de mayor margen.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "02_segmentos")

def c03():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    labs = ["Ingreso neto\n(FY25)", "Client incentives\n(contra-revenue)"]
    vals = [11, 14]
    ax.bar([0, 1], vals, 0.4, color=[AZUL, ROJOSC])
    for i, v in enumerate(vals):
        ax.text(i, v + 0.4, f"+{v}%", ha="center", fontsize=11, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 17); ax.set_yticklabels([])
    deco(ax, "Los incentivos a clientes crecen más rápido que el ingreso",
         "Crecimiento interanual (%) · proxy de la intensidad competitiva del duopolio con Mastercard",
         "Fuente: 10-K FY2025. HECHO. Client incentives son la contra-partida contable que reduce el ingreso bruto reportado.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "03_incentivos")

def c04():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    labs = ["VAS\n(Value-Added Services)", "Red central\n(pagos)"]
    vals = [24, 11]
    ax.bar([0, 1], vals, 0.42, color=[VERDE, ACERO])
    for i, v in enumerate(vals):
        ax.text(i, v + 0.6, f"+{v}%", ha="center", fontsize=11, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 29); ax.set_yticklabels([])
    ax.text(0.5, 20, f"VAS ya es ~27% del ingreso bruto\n(US${D.VAS_GROSS}B, FY25)\nla cobertura de Visa frente a RTP/stablecoins",
            ha="center", fontsize=7.4, color=NOCHE,
            bbox=dict(boxstyle="round,pad=0.5", fc=PANEL, ec=GLIN, lw=0.8))
    deco(ax, "VAS crece al doble de velocidad que la red central",
         "Crecimiento interanual (%) FY2025 · el motor estratégico que diversifica a Visa más allá del swipe",
         "Fuente: 10-K FY2025. HECHO.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "04_vas")

def c05():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    labs = ["Visa", "Mastercard", "Resto"]
    vals = [52.2, 21.6, 26.2]
    ax.pie(vals, labels=None, colors=[ROJOSC, ACERO, GCLARO], startangle=90,
           wedgeprops=dict(width=0.42, edgecolor=P["fondo"]))
    ax.text(0, 0, "Duopolio\n~74%", ha="center", va="center", fontsize=11, fontweight="bold", color=TINTA)
    ax.legend(labs, loc="lower center", bbox_to_anchor=(0.5, -0.16), ncol=3, fontsize=7.6, frameon=False)
    deco(ax, "El duopolio de redes de tarjetas, con Visa como líder claro",
         "Cuota global de crédito por red (%, estimado) · Mastercard crece más rápido en el margen (~15% vs. ~11% guía FY26 de Visa)",
         "Fuente: estimados de industria. INFERENCIA/HECHO (guías propias).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.14)
    save(fig, "05_duopolio")

def c06():
    yrs = D.YRS_FIN; x = np.arange(len(yrs))
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    ax.plot(x, D.OP_MGN, color=AZUL, lw=2.0, marker="o", ms=4)
    for i, v in enumerate(D.OP_MGN):
        ax.text(i, v + 1.4, pctc(v), fontsize=6.8, color=AZUL, ha="center", fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(yrs, fontsize=7.6)
    ax.set_ylim(0, 76); ax.set_yticklabels([])
    ax.annotate("Provisión litigiosa\nde $2.562M (one-off)", xy=(4, 60), xytext=(3.3, 45),
                fontsize=6.8, color=ROJOSC, ha="center",
                arrowprops=dict(arrowstyle="->", color=ROJOSC, lw=0.9))
    deco(ax, "El margen \"cae\" solo por un cargo litigioso puntual",
         "Margen operativo GAAP (%) FY21-TTM · el margen subyacente se mantiene estable ~66-67% una década",
         "Fuente: 10-K FY2025. HECHO. La caída de FY25 (65,7%→60,0%) es contable, no operativa.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "06_margenes")

def c07():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    labs = [f"Conservador\n({D.P_BEAR}%)", f"Base\n({D.P_BASE}%)", f"Optimista\n({D.P_BULL}%)"]
    vals = [D.V_BEAR, D.V_BASE, D.V_BULL]; cols = [ROJOSC, AZUL, VERDE]
    x = np.arange(3); ax.bar(x, vals, 0.5, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 10, f"US${v}", ha="center", fontsize=8.6, fontweight="bold", color=TINTA)
    ax.axhline(D.PRECIO, color=TINTA, lw=1.6)
    ax.text(0.02, D.PRECIO + 10, f"HOY US${D.es(D.PRECIO,0)} — zona {D.ZONA_HOY}", fontsize=7.6, color=TINTA, fontweight="bold")
    ax.axhline(D.PWFV, color=ROJO, lw=1.4, ls=(0, (5, 3)))
    ax.text(2.55, D.PWFV + 10, f"PWFV US${D.es(D.PWFV,0)}", va="bottom", ha="right", fontsize=7.6, color=ROJO)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 680); ax.set_yticklabels([])
    deco(ax, "Cerca del valor justo — pero no lo suficiente para su tier",
         f"Valor por acción del DCF sobre owner earnings (US$) · WACC {D.es(D.WACC,1)}%",
         f"Fuente: modelo propio (val-mos). SUPUESTO. Ponderado US${D.es(D.PWFV,0)}; MoS actual {D.es(D.MOS_ACTUAL,1)}% (bajo el 25% exigido).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "07_dcf")

def c08():
    fig, ax = plt.subplots(figsize=(7.6, 2.8))
    lo, hi = 200, 660
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
    ax.text(D.PWFV, -0.62, f"PWFV ${D.es(D.PWFV,0)}", ha="center", fontsize=7, color=ROJO)
    ax.plot([D.GATILLO_OPORT, D.GATILLO_OPORT], [-0.25, 0.25], color=VERDE, lw=1.4)
    ax.text(D.GATILLO_OPORT, 0.62, f"gatillo ${D.GATILLO_OPORT}", ha="center", fontsize=6.8, color=VERDE)
    ax.set_xlim(lo, hi); ax.set_ylim(-0.8, 0.9); ax.axis("off")
    deco(ax, "Mapa operativo de precio",
         f"Zonas ancladas al PWFV US${D.es(D.PWFV,0)} · HOY US${D.es(D.PRECIO,0)} = zona {D.ZONA_HOY}, pero MoS insuficiente para el tier",
         "Fuente: val-mos v3. Alta Convicción exige 25% de MoS numérico, no solo estar en zona Oportunidad.",
         fig=fig, flag_y=0.96)
    fig.subplots_adjust(top=0.64, bottom=0.06)
    save(fig, "08_zonas")

def c09():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    labs = ["MoS actual", "MoS exigido\n(Alta Convicción)"]
    vals = [D.MOS_ACTUAL, 25.0]
    cols = [ROJOSC, VERDE]
    x = np.arange(2); ax.bar(x, vals, 0.42, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.6, pctc(v), ha="center", fontsize=10, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 30); ax.set_yticklabels([])
    ax.annotate("faltan 8,3pp", xy=(0.5, 22), fontsize=9, color=ROJOSC, fontweight="bold", ha="center")
    deco(ax, "Cerca, pero no suficiente: falta margen de seguridad, no calidad",
         "Margen de seguridad actual vs. el exigido por el tier Alta Convicción (%)",
         "Fuente: val-mos v3 (escalón numérico de MoS por tier, mos_sizing.md).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "09_mos_gap")

def c10():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["Techo del tier\n(Alta Convicción)", "Múltiplo normalizado\n(owner earnings)"]
    vals = [D.TECHO_MULT_TIER, D.MULT_NORMALIZADO]
    cols = [VERDE, OCRE]
    x = np.arange(2); ax.bar(x, vals, 0.42, color=cols)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.6, f"{D.es(v,1)}x", ha="center", fontsize=10, fontweight="bold", color=TINTA)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 35); ax.set_yticklabels([])
    deco(ax, "El candado duro NO se viola — es el único freno que Visa sí supera",
         "Múltiplo pagado hoy sobre owner earnings vs. el techo de múltiplo del tier (30x)",
         "Fuente: val-mos v3. A diferencia de MELI/TSM/SPGI, aquí el candado duro no es el problema.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "10_candado_duro")

def c11():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    coe = D.COE_CAPM
    pasos = ["Tasa libre\nde riesgo", f"+ Prima ×\nbeta {D.es(D.BETA,2)}", "= CAPM", "= WACC\nusado"]
    cols = [CIELO, ACERO, AZUL, ROJO]
    ax.bar(0, D.RF, 0.6, color=cols[0])
    ax.bar(1, D.BETA * D.ERP, 0.6, bottom=D.RF, color=cols[1])
    ax.bar(2, coe, 0.6, color=cols[2])
    ax.bar(3, D.WACC, 0.6, color=cols[3])
    labels = [pctc(D.RF), pctc(D.BETA * D.ERP), pctc(coe), pctc(D.WACC)]
    tops = [D.RF, coe, coe, D.WACC]
    for i in range(4):
        ax.text(i, tops[i] + 0.2, labels[i], ha="center", fontsize=7.6, color=TINTA, fontweight="bold")
    ax.set_xticks(range(4)); ax.set_xticklabels(pasos, fontsize=7.4)
    ax.set_ylim(0, 10); ax.set_yticklabels([])
    deco(ax, "El WACC más bajo de la campaña — beta defensivo",
         f"Coste de capital (%) · CAPM ~{D.es(coe,1)}%, usado {D.es(D.WACC,1)}%",
         "Fuente: modelo propio (val-mos). Beta &lt;1 refleja la naturaleza defensiva/no cíclica del negocio de peaje.".replace("&lt;","<"), fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "11_wacc")

def c12():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    M = np.array(D.SENS)
    cmap = LinearSegmentedColormap.from_list("qg", [ROJOSC, GCLARO, NOCHE])
    ax.imshow(M, cmap=cmap, aspect="auto")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            base = (abs(D.WACC_GRID[i] - D.WACC) < 0.01 and D.GT_GRID[j] == D.TERMINAL)
            ax.text(j, i, f"{M[i, j]}", ha="center", va="center", fontsize=7.8,
                    color="white" if M[i, j] > 500 or M[i, j] < 380 else TINTA,
                    fontweight="bold" if base else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels([pctc(g) for g in D.GT_GRID], fontsize=7.2)
    ax.set_yticks(range(5)); ax.set_yticklabels([pctc(w) for w in D.WACC_GRID], fontsize=7.2)
    ax.set_xlabel("Crecimiento terminal", fontsize=7.8, color=GRIS)
    ax.set_ylabel("WACC", fontsize=7.8, color=GRIS)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    deco(ax, "El valor bajo estrés — solo cruza el gatillo de Oportunidad en el extremo generoso",
         "Valor DCF base por acción (US$) según WACC × terminal · negrita = caso central",
         f"Fuente: modelo propio. SUPUESTO. Rango US${D.SENS[-1][0]}-{D.SENS_MAX}.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.10, right=0.98)
    save(fig, "12_sensibilidad")

def c13():
    y = np.arange(len(D.PORTER_FUERZAS))[::-1]
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    for yi, (nm, v) in zip(y, D.PORTER_FUERZAS):
        col = VERDE if v <= 1.5 else (OCRE if v <= 2.5 else ROJOSC)
        ax.barh(yi, v, 0.55, color=col)
        ax.text(v + 0.06, yi, f"{v}/5", va="center", fontsize=8, color=TINTA, fontweight="bold")
        ax.text(-0.1, yi, nm, va="center", ha="right", fontsize=7.6, color=TINTA)
    ax.axvline(D.PORTER_POND, color=NOCHE, lw=1.2, ls=(0, (4, 2)))
    ax.text(D.PORTER_POND + 0.05, -0.75, f"ponderado {D.es(D.PORTER_POND,1)}", fontsize=6.8, color=NOCHE)
    ax.set_xlim(0, 5.2); ax.set_ylim(-1, len(D.PORTER_FUERZAS) - 0.4); ax.set_yticks([])
    ax.set_xticks([1, 2, 3, 4, 5]); ax.set_xticklabels(["1", "2", "3", "4", "5"], fontsize=7)
    deco(ax, "Cinco Fuerzas de Porter: posición casi ideal, con sustitutos en ascenso",
         "Score /5 (menor = mejor foso) · Pix/UPI/stablecoins son la fuerza más dinámica, no la más severa hoy",
         "Fuente: análisis propio.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11, left=0.38)
    save(fig, "13_porter")

def c14():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    y = np.arange(len(D.MERCADOS))[::-1]
    LX = 8000
    for yi, (nm, tam, cap, nota) in zip(y, D.MERCADOS):
        w = min(tam, 20000)
        ax.barh(yi, w, 0.6, color=CIELO, alpha=0.6)
        ax.barh(yi, cap, 0.6, color=AZUL)
        ax.text(-500, yi, nm, va="center", ha="right", fontsize=7.2, color=TINTA)
        ax.text(LX, yi, f"{nota}", va="center", fontsize=6.2, color=GRIS)
    ax.set_xlim(0, 24000); ax.set_ylim(-0.7, len(D.MERCADOS) - 0.3); ax.set_yticks([])
    ax.set_xticks([5000, 10000, 15000]); ax.set_xticklabels(["$5T", "$10T", "$15T"], fontsize=7)
    deco(ax, "El mercado es casi ilimitado; el reto es la conversión, no el tamaño",
         "TAM 2026 (claro) vs. captura de Visa (oscuro), US$B",
         "Fuente: 10-K + Statista/coinlaw (rangos amplios). INFERENCIA. El crecimiento futuro es conversión efectivo→tarjeta + VAS, no captura de TAM.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.09, left=0.24, right=0.98)
    save(fig, "14_tam")

def c15():
    labs = [n for n, _ in D.MGMT]; vals = [v for _, v in D.MGMT]
    N = len(vals); ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    v = vals + vals[:1]; a = ang + ang[:1]
    fig = plt.figure(figsize=(7.6, 5.2)); ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.plot(a, v, color=AZUL, lw=1.8); ax.fill(a, v, color=AZUL, alpha=0.16)
    for ai, vi in zip(ang, vals):
        col = ROJOSC if vi <= 2 else AZUL
        ax.scatter(ai, vi, color=col, s=30, zorder=5)
        ax.text(ai, vi + 0.3, D.es(vi, 1), ha="center", fontsize=7.4, color=TINTA)
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=6.0, color=TINTA)
    ax.set_ylim(0, 5); ax.set_yticks([1, 2, 3, 4, 5]); ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Gestión: ejecución sólida, estructura de tres clases accionarias compleja",
         f"Puntuación 1–5 · total {D.es(D.MGMT_TOTAL,1)}/30 · alineación de incentivos y gobernanza son los frenos",
         "Fuente: DEF 14A + 10-K. Clase B (bancos emisores) no vota directores pero mantiene voto en fusiones/disolución.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10, left=0.10, right=0.90)
    save(fig, "15_mgmt")

def c16():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    labs = ["RuPay India\n(cuota de tarjetas)", ""]
    vals_yrs = ["2025", "2026"]
    vals = [10, 28]
    ax.bar([0, 1], vals, 0.42, color=[ACERO, ROJOSC])
    for i, v in enumerate(vals):
        ax.text(i, v + 1, pctc(v), ha="center", fontsize=11, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(vals_yrs, fontsize=9)
    ax.set_ylim(0, 34); ax.set_yticklabels([])
    deco(ax, "El desplazamiento más rápido: RuPay en India, en un solo año",
         "Cuota de RuPay en tarjetas de crédito indias (%) · Pix ya supera a Visa+Mastercard combinados en transacciones diarias en Brasil",
         "Fuente: prensa/reguladores de India. HECHO. Es la señal aislada #2 del detector de trampas, geográficamente acotada.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "16_rieles_soberanos")

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
        fig.text(0.66, ly + 0.012, nm, fontsize=6.0, color=TINTA, va="center")
        fig.text(0.66, ly - 0.028, f"prob {pr} × impacto {im} = {sev}", fontsize=6.0, color=col, va="center", style="italic")
        ly -= 0.108
    deco(ax, "Matriz de riesgos",
         "Probabilidad × impacto (1–5) · el fin de \"honor all cards\" es el más probable; los rieles soberanos, el más severo",
         "Fuente: análisis propio.", fig=fig)
    save(fig, "17_riesgos")

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
    ax.text(0.2, -1.15, "verde = comprar · navy = mantener · ocre = pass", fontsize=6.6, color=GRIS, style="italic")
    deco(ax, "Nueve leyendas opinan",
         "Convicción /10 · cuatro BUY (Buffett, Munger, Fisher, Seilern) — el panel más alcista de la campaña",
         "Fuente: doctrina de cada inversor aplicada por el autor. INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.13, left=0.16)
    save(fig, "18_inversores")

def c19():
    fig, ax = plt.subplots(figsize=(7.6, 4.3))
    labs = ["Visa\n(guía FY26)", "Mastercard\n(crecimiento actual)"]
    vals = [11, 15]
    ax.bar([0, 1], vals, 0.42, color=[AZUL, ROJOSC])
    for i, v in enumerate(vals):
        ax.text(i, v + 0.4, f"+{v}%", ha="center", fontsize=11, fontweight="bold", color=TINTA)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 18); ax.set_yticklabels([])
    deco(ax, "Visa está perdiendo terreno relativo dentro del duopolio",
         "Crecimiento de ingresos (%) · Mastercard crece más rápido, aunque ambos siguen expandiéndose con fuerza",
         "Fuente: guías corporativas propias. HECHO. Señal aislada #2 del detector — no confirma deterioro estructural.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "19_visa_vs_mastercard")

def c20():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    filas = [
        ("Volumen de pagos (nominal)", "+7% FY25 (récord desde 2013 ex-pandemia)", "cae &lt; 5% sostenido", VERDE),
        ("VAS (crecimiento)", "+24% YoY", "cae &lt; 15% sostenido", VERDE),
        ("ROIC", "~43%", "cae &lt; 30%", VERDE),
        ("Client incentives (contra-revenue)", "+14% (más rápido que ingreso +11%)", "supera +20% sostenido", OCRE),
        ("Crecimiento relativo vs. Mastercard", "+11% (Visa) vs. +15% (MA)", "brecha supera 8pp sostenida", OCRE),
        ("Rieles soberanos (Pix/UPI)", "RuPay 10%→28% en 1 año en India", "un 2do mercado replica el patrón", "rojo"),
        ("Fin de \"honor all cards\" (jun-2026)", "settlement ya vigente", "hecho ya consumado, no reversible", "rojo"),
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
         "Semáforo · el negocio (verde) es excelente; la regulación y los rieles soberanos (rojo) son estructurales",
         "Fuente: KPIs primarios Visa. Las dos filas rojas ya son hechos consumados, no riesgos futuros.",
         fig=fig, flag_y=0.97)
    fig.subplots_adjust(top=0.80, bottom=0.05, left=0.02, right=0.98)
    save(fig, "20_early_warning")

if __name__ == "__main__":
    fns = [c01, c02, c03, c04, c05, c06, c07, c08, c09, c10,
           c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]
    for fn in fns:
        fn(); print("ok", fn.__name__)
    print("charts done:", len(fns))
