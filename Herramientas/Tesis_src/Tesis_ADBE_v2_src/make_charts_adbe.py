# -*- coding: utf-8 -*-
"""Gráficos Ultra Tesis ADBE — importan dcf_adbe (fuente de verdad) y chart_style."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
from chart_style import deco, save, P
import dcf_adbe as D

pct = lambda x: f"{x:.1f}".replace(".", ",") + "%"
AZUL, NOCHE, ACERO, CIELO = P["azul"], P["azul_noche"], P["azul_acero"], P["azul_cielo"]
ROJO, ROJOSC, VERDE, OCRE, TERRA, GRIS = (P["rojo"], P["rojo_oscuro"], P["verde"],
    P["ocre"], P["terracota"], P["gris"])
TINTA, GLIN, GCLARO = P["tinta"], P["gris_linea"], P["gris_claro"]

# ── 01 · Radar de las 11 reglas QG ───────────────────────────────────────
def c01():
    labs = [n.split(" · ")[0] for n, _ in D.RADAR]
    vals = [v for _, v in D.RADAR]
    N = len(vals)
    ang = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
    v = vals + vals[:1]; a = ang + ang[:1]
    fig = plt.figure(figsize=(7.6, 5.4))
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P["fondo"])
    ax.plot(a, v, color=NOCHE, lw=1.8); ax.fill(a, v, color=NOCHE, alpha=0.16)
    ax.plot(a, [8]*len(a), color=ROJO, lw=1.1, ls=(0,(4,3)))
    for ai, vi in zip(ang, vals):
        col = VERDE if vi >= 8 else (ROJOSC if vi < 6.5 else NOCHE)
        ax.scatter(ai, vi, color=col, s=26, zorder=5)
        ax.text(ai, vi+0.9, f"{vi:.1f}".replace(".", ","), ha="center", va="center",
                fontsize=7.3, color=TINTA)
    ax.set_xticks(ang); ax.set_xticklabels(labs, fontsize=7.4, color=TINTA)
    ax.set_ylim(0, 10); ax.set_yticks([2,4,6,8,10])
    ax.set_yticklabels(["2","4","6","8","10"], fontsize=6.5, color=GRIS)
    ax.grid(color=GLIN, lw=0.6); ax.spines["polar"].set_color(GLIN)
    deco(ax, "Las 11 reglas Quality Growth", "Puntuación 0–10 por regla · anillo rojo = umbral de excelencia (8)",
         "Fuente: sistema QG Felipe, ranking v1 (2026-07-01). Raw 91/125 → 72,8/100 · tier Sólida. HECHO.",
         fig=fig)
    fig.subplots_adjust(top=0.74, bottom=0.08, left=0.06, right=0.94)
    save(fig, "01_radar")

# ── 02 · Ingresos por segmento, 3 años ───────────────────────────────────
def c02():
    yrs = ["FY2023", "FY2024", "FY2025"]
    dm = [14.22, 15.86, D.DM_FY25]      # Digital Media
    dx = [4.89, 5.37, D.DX_FY25]        # Digital Experience
    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    x = np.arange(3)
    ax.bar(x, dm, 0.55, color=AZUL, label="Digital Media (Creative + Document)")
    ax.bar(x, dx, 0.55, bottom=dm, color=CIELO, label="Digital Experience")
    for i in range(3):
        ax.text(i, dm[i]/2, f"{dm[i]:.1f}", ha="center", va="center", color="white", fontsize=8.4, fontweight="bold")
        ax.text(i, dm[i]+dx[i]/2, f"{dx[i]:.1f}", ha="center", va="center", color=TINTA, fontsize=8)
        ax.text(i, dm[i]+dx[i]+0.4, f"{dm[i]+dx[i]:.1f}", ha="center", color=TINTA, fontsize=8.6, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(yrs, fontsize=8.4)
    ax.set_ylim(0, 26); ax.set_yticklabels([]); ax.legend(fontsize=7.6, loc="upper left", frameon=False)
    deco(ax, "Dos motores, un peaje creciente", "Ingresos por segmento (USD mil millones) · 89% margen bruto",
         "Fuente: Adobe 10-K FY2025. HECHO. FY23 desglose estimado por mix histórico (INFERENCIA).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "02_segmentos")

# ── 03 · ARR total y crecimiento con umbral ─────────────────────────────
def c03():
    yrs = ["FY22","FY23","FY24","FY25","FY26E"]
    arr = [15.2, 17.1, 19.9, 22.9, 25.2]     # ARR total aprox (DM ARR + DX + AI)
    crec = [14, 12.5, 16.4, 15.1, 10.2]
    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    ax.fill_between(range(5), arr, color=AZUL, alpha=0.13)
    ax.plot(range(5), arr, color=AZUL, lw=2.2, marker="o", ms=4)
    for i,v in enumerate(arr):
        ax.text(i, v+0.6, f"{v:.1f}", ha="center", color=TINTA, fontsize=8)
    ax2 = ax.twinx()
    ax2.plot(range(5), crec, color=ROJO, lw=1.4, ls=(0,(4,2)), marker="s", ms=3)
    for i,v in enumerate(crec):
        ax2.text(i, v+0.7, pct(v), ha="center", color=ROJO, fontsize=7)
    ax.set_xticks(range(5)); ax.set_xticklabels(yrs, fontsize=8.2)
    ax.set_ylim(0, 30); ax.set_yticklabels([])
    ax2.set_ylim(0, 30); ax2.set_yticks([]); ax2.spines["top"].set_visible(False); ax2.spines["right"].set_visible(False)
    deco(ax, "El motor recurrente sigue componiendo", "ARR total (USD mil M, área azul) y crecimiento anual (línea roja)",
         "Fuente: Adobe releases FY22-Q2FY26. HECHO. FY26E = guía (crec. ARR 10,2% incl. Semrush; orgánico ~8,3%). INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "03_arr")

# ── 04 · Campo de batalla: escala de monetización IA-nativa vs Adobe ─────
def c04():
    labs = ["Adobe\n(Creative+Doc ARR)", "Canva\n(ARR)", "Figma\n(ARR est.)", "Midjourney\n(ingresos est.)", "OpenAI Sora\n(no monetiz. directa)"]
    vals = [19.2, 4.0, 1.0, 0.5, 0.1]
    cols = [NOCHE, TERRA, ACERO, OCRE, GCLARO]
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    y = np.arange(len(labs))[::-1]
    ax.barh(y, vals, 0.6, color=cols)
    for yi, v in zip(y, vals):
        ax.text(v+0.3, yi, f"USD {v:.1f}B", va="center", fontsize=8, color=TINTA)
    ax.set_yticks(y); ax.set_yticklabels(labs, fontsize=7.3, color=TINTA)
    ax.set_xlim(0, 22); ax.set_xticklabels([])
    deco(ax, "El retador es real, pero pequeño", "Escala de monetización recurrente (USD mil M) · Adobe DM ARR vs entrantes IA-nativos",
         "Fuente: informes de las empresas y estimaciones de prensa 2025-26. Canva ~$4B ARR (+35%). HECHO/INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.08, left=0.22)
    save(fig, "04_competencia")

# ── 05 · Cascada de caja: de ingresos a owner earnings ──────────────────
def c05():
    etiquetas = ["Ingresos\nFY25", "Costes y\nopex", "Flujo\noperativo", "CapEx", "FCF", "SBC\n(−100%)", "Owner\nearnings"]
    # niveles absolutos; barras flotantes
    rev = D.REV_FY25
    cfo = 10.4
    capex = 0.55
    fcf = D.FCF_FY25
    sbc = D.SBC
    oe = D.OWNER_EARN
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    # dibujar como barras: ingresos, luego flujo operativo, fcf, owner earnings (absolutos) + deltas
    xs = np.arange(7)
    # bottoms/tops for waterfall
    bars = [
        (0, rev, AZUL),                      # ingresos
        (cfo, rev-cfo, GCLARO),              # costes (resta hasta CFO): draw from cfo to rev as gris
        (0, cfo, NOCHE),                     # flujo operativo
        (fcf, cfo-fcf, ROJOSC),              # capex outflow
        (0, fcf, AZUL),                      # FCF
        (oe, fcf-oe, ROJOSC),                # SBC outflow
        (0, oe, VERDE),                      # owner earnings
    ]
    for i,(bot,h,c) in enumerate(bars):
        ax.bar(i, h, 0.62, bottom=bot, color=c)
    lab_vals = [rev, -(rev-cfo), cfo, -(cfo-fcf), fcf, -(fcf-oe), oe]
    for i,v in enumerate(lab_vals):
        top = bars[i][0]+bars[i][1] if v>0 else bars[i][0]
        ax.text(i, max(bars[i][0], bars[i][0]+bars[i][1])+0.4,
                (f"{v:+.1f}" if i in (1,3,5) else f"{abs(v):.1f}"),
                ha="center", fontsize=7.8, color=TINTA, fontweight="bold" if i in (0,2,4,6) else "normal")
    ax.set_xticks(xs); ax.set_xticklabels(etiquetas, fontsize=7.1)
    ax.set_ylim(0, 26); ax.set_yticklabels([])
    deco(ax, "La máquina de caja, ajustada sin piedad", "De ingresos a owner earnings (USD mil M, FY2025) · SBC restado al 100%",
         "Fuente: Adobe 10-K FY2025. HECHO. CFO/CapEx aprox de estado de flujos (INFERENCIA menor).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "05_cascada")

# ── 07 · Márgenes 5 años ────────────────────────────────────────────────
def c07():
    yrs = ["FY22","FY23","FY24","FY25","TTM"]
    bruto = [88, 88, 89, 89, 89]
    op = [35, 35, 36, 36, 37]
    neto = [27, 28, 30, 31, 29]
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    for serie, col, nm in [(bruto, GRIS, "Bruto"), (op, AZUL, "Operativo GAAP"), (neto, ACERO, "Neto")]:
        ax.plot(range(5), serie, color=col, lw=2.0, marker="o", ms=3.4)
        ax.text(4.06, serie[-1], f" {nm} {serie[-1]}%", va="center", fontsize=7.6, color=col)
    ax.set_xticks(range(5)); ax.set_xticklabels(yrs, fontsize=8.2)
    ax.set_ylim(20, 95); ax.set_yticks([30,50,70,90]); ax.set_yticklabels(["30%","50%","70%","90%"], fontsize=7)
    ax.set_xlim(0, 5.8)
    deco(ax, "Márgenes de fortaleza, estables bajo fuego", "Margen bruto / operativo GAAP / neto (%) · no hay compresión estructural",
         "Fuente: Adobe 10-K FY2025 y release Q2FY26. HECHO. Op. non-GAAP ~46%.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "07_margenes")

# ── 08 · DCF 3 escenarios + HOY + PWFV ──────────────────────────────────
def c08():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    labs = ["Oso\n(35%)", "Base\n(45%)", "Toro\n(20%)"]
    vals = [D.V_OSO, D.V_BASE, D.V_TORO]
    cols = [ROJOSC, AZUL, VERDE]
    x = np.arange(3)
    ax.bar(x, vals, 0.5, color=cols)
    for i,v in enumerate(vals):
        ax.text(i, v+7, f"USD {v}", ha="center", fontsize=8.6, fontweight="bold", color=TINTA)
    ax.axhline(D.PRECIO, color=TINTA, lw=1.4)
    ax.text(2.55, D.PRECIO, f"HOY USD {int(D.PRECIO)}", va="bottom", ha="right", fontsize=7.8, color=TINTA)
    ax.axhline(D.PWFV, color=ROJO, lw=1.4, ls=(0,(5,3)))
    ax.text(2.55, D.PWFV, f"PWFV USD {D.PWFV}", va="bottom", ha="right", fontsize=7.8, color=ROJO)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylim(0, 540); ax.set_yticklabels([])
    deco(ax, "Tres futuros, un valor ponderado", f"Valor por acción del DCF sobre owner earnings (USD) · WACC {D.es(D.WACC,1)}% · terminal 2,5%",
         "Fuente: modelo propio dcf_adbe. SUPUESTO. Ponderado = 0,35·oso + 0,45·base + 0,20·toro.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.11)
    save(fig, "08_dcf")

# ── 09 · Mapa de zonas de precio + HOY ──────────────────────────────────
def c09():
    fig, ax = plt.subplots(figsize=(7.6, 2.7))
    lo, hi = 130, 400
    zonas = [("GANGA", lo, D.Z_GANGA, VERDE), ("OPORTUNIDAD", D.Z_GANGA, D.Z_OPORT, ACERO),
             ("JUSTO", D.Z_OPORT, D.Z_JUSTO_SUP, OCRE), ("CARO", D.Z_JUSTO_SUP, D.Z_CARO_SUP, TERRA),
             ("BURBUJA", D.Z_CARO_SUP, hi, ROJOSC)]
    for nm,a,b,c in zonas:
        ax.barh(0, b-a, left=a, height=0.5, color=c, alpha=0.85)
        ax.text((a+b)/2, 0, nm, ha="center", va="center", fontsize=7.2, color="white", fontweight="bold")
        ax.text(b, -0.42, f"${int(b)}", ha="center", fontsize=6.6, color=GRIS)
    ax.scatter([D.PRECIO], [0.42], marker="v", s=90, color=TINTA, zorder=5)
    ax.text(D.PRECIO, 0.62, f"HOY USD {int(D.PRECIO)}", ha="center", fontsize=8, fontweight="bold", color=TINTA)
    ax.plot([D.PWFV,D.PWFV],[-0.25,0.25], color=ROJO, lw=1.6, ls=(0,(4,2)))
    ax.text(D.PWFV, -0.6, f"PWFV ${D.PWFV}", ha="center", fontsize=7, color=ROJO)
    ax.set_xlim(lo, hi); ax.set_ylim(-0.8, 0.9); ax.axis("off")
    deco(ax, "Mapa operativo de precio", f"Zonas ancladas al PWFV-Valor USD {D.PWFV} · HOY USD {int(D.PRECIO)} = {D.ZONA_HOY} ({D.es(D.DCTO_PWFV,1)}%)",
         f"Fuente: modelo propio. Gatillos: OPORTUNIDAD <= USD {D.Z_OPORT} · GANGA <= USD {D.Z_GANGA} · MoS pleno 35% en USD {D.MOS_PLENO}.", fig=fig, flag_y=0.96)
    fig.subplots_adjust(top=0.66, bottom=0.06)
    save(fig, "09_zonas")

# ── 10 · Múltiplos hoy vs historia ──────────────────────────────────────
def c10():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    met = ["P/E (fwd)", "P/FCF", "P/E (ttm)"]
    hoy = [D.PE_FWD, D.PFCF_HOY, D.PE_TTM]
    hist = [28, D.PFCF_HIST, D.PE_HIST_3A]
    x = np.arange(3); w = 0.36
    ax.bar(x-w/2, hoy, w, color=NOCHE, label="Hoy")
    ax.bar(x+w/2, hist, w, color=P["gris_medio"], label="Media 3-5 años")
    for i,(a,b) in enumerate(zip(hoy,hist)):
        ax.text(i-w/2, a+0.7, f"{a:.0f}x", ha="center", fontsize=7.8, color=TINTA, fontweight="bold")
        ax.text(i+w/2, b+0.7, f"{b:.0f}x", ha="center", fontsize=7.8, color=GRIS)
    ax.set_xticks(x); ax.set_xticklabels(met, fontsize=8.2)
    ax.set_ylim(0, 48); ax.set_yticklabels([]); ax.legend(fontsize=7.6, frameon=False, loc="upper left")
    deco(ax, "Una de-rating histórica", "Múltiplos hoy vs su propia media reciente · el mercado paga 8-9x lo que pagaba 28-42x",
         "Fuente: stockanalysis.com 2026-07-02. HECHO (hoy) / INFERENCIA (media histórica).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "10_multiplos")

# ── 11 · Balance ─────────────────────────────────────────────────────────
def c11():
    fig, ax = plt.subplots(figsize=(7.6, 4.0))
    labs = ["Caja e\ninversiones", "Deuda\ntotal", "Deuda\nneta", "FCF anual\n(referencia)"]
    vals = [D.CAJA_STI, -D.DEUDA_TOTAL, -D.DEUDA_NETA, D.FCF_FY25]
    cols = [VERDE, TERRA, OCRE, AZUL]
    x = np.arange(4)
    ax.bar(x, vals, 0.55, color=cols)
    for i,v in enumerate(vals):
        ax.text(i, v+(0.3 if v>=0 else -0.5), f"USD {abs(v):.1f}B", ha="center",
                va="bottom" if v>=0 else "top", fontsize=8, color=TINTA)
    ax.axhline(0, color=GRIS, lw=0.8)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.6)
    ax.set_ylim(-9, 12); ax.set_yticklabels([])
    deco(ax, "Balance de fortaleza, deuda neta trivial", "Caja, deuda y FCF anual (USD mil M) · deuda neta ≈ 0,15× EBITDA",
         "Fuente: stockanalysis.com (may-2026) y 10-K FY25. HECHO. Deuda neta leve por recompras de USD 11B+.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "11_balance")

# ── 13 · Nueve inversores ────────────────────────────────────────────────
def c13():
    inv = [("Graham", 6, OCRE), ("Buffett", 7, NOCHE), ("Munger", 7, NOCHE), ("Fisher", 6, OCRE),
           ("Lynch", 7, NOCHE), ("Templeton", 8, NOCHE), ("Marks", 6, OCRE), ("Seilern", 6, OCRE),
           ("Terry Smith", 7, NOCHE)]
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    y = np.arange(len(inv))[::-1]
    for yi,(nm,conv,col) in zip(y, inv):
        ax.barh(yi, conv, 0.6, color=col)
        ax.text(conv+0.12, yi, f"{conv}/10", va="center", fontsize=7.6, color=TINTA)
        ax.text(-0.15, yi, nm, va="center", ha="right", fontsize=8, color=TINTA)
    ax.set_xlim(0, 10); ax.set_ylim(-0.6, len(inv)-0.4)
    ax.set_yticks([]); ax.set_xticks([2,4,6,8,10]); ax.set_xticklabels(["2","4","6","8","10"], fontsize=7)
    ax.text(0.5, -1.15, "navy = comprar/acumular · ocre = mantener/observar", fontsize=6.8, color=GRIS, style="italic")
    deco(ax, "Nueve leyendas opinan", "Convicción /10 · la divergencia (no el consenso) es la señal",
         "Fuente: doctrina de cada inversor aplicada por el autor. INFERENCIA.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12, left=0.16)
    save(fig, "13_inversores")

# ── 15 · Demanda futura: RPO y AI-first ARR ─────────────────────────────
def c15():
    fig, (a1,a2) = plt.subplots(1, 2, figsize=(7.6, 4.0))
    # RPO trend
    q = ["Q2FY25","Q4FY25","Q2FY26"]; rpo=[19.7, 20.5, D.RPO]
    a1.bar(range(3), rpo, 0.55, color=ACERO)
    for i,v in enumerate(rpo): a1.text(i, v+0.3, f"{v:.1f}", ha="center", fontsize=7.6, color=TINTA)
    a1.set_xticks(range(3)); a1.set_xticklabels(q, fontsize=6.8); a1.set_ylim(0,26); a1.set_yticklabels([])
    a1.set_title("Backlog contratado (RPO, USD mil M)", fontsize=8, color=TINTA, pad=4)
    for s in ["top","right","left"]: a1.spines[s].set_visible(False)
    a1.spines["bottom"].set_color(GLIN); a1.tick_params(length=0); a1.grid(axis="y", color=GLIN, lw=0.5)
    # AI-first ARR
    q2=["Q1FY26","Q2FY26"]; ai=[0.30, D.AI_ARR]
    a2.bar(range(2), ai, 0.5, color=AZUL)
    for i,v in enumerate(ai): a2.text(i, v+0.01, f"${v*1000:.0f}M", ha="center", fontsize=7.6, color=TINTA)
    a2.text(0.5, 0.44, "×3 YoY", ha="center", fontsize=8, color=ROJO, fontweight="bold")
    a2.set_xticks(range(2)); a2.set_xticklabels(q2, fontsize=6.8); a2.set_ylim(0,0.6); a2.set_yticklabels([])
    a2.set_title("AI-first ARR (Firefly, GenStudio…)", fontsize=8, color=TINTA, pad=4)
    for s in ["top","right","left"]: a2.spines[s].set_visible(False)
    a2.spines["bottom"].set_color(GLIN); a2.tick_params(length=0); a2.grid(axis="y", color=GLIN, lw=0.5)
    deco([a1,a2], "La demanda futura no se ha roto", "Backlog contratado y monetización de IA · lo que un P&L trailing no ve todavía",
         "Fuente: Adobe releases Q1-Q2 FY2026. HECHO. AI-first ARR >USD 500M, triplicó YoY.", fig=fig)
    fig.subplots_adjust(top=0.74, bottom=0.10, wspace=0.18)
    save(fig, "15_demanda")

# ── 17 · Construcción del WACC ──────────────────────────────────────────
def c17():
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    pasos = ["Tasa libre\nde riesgo", f"+ Prima x\nbeta {D.es(D.BETA,2)}", "= Coste de\nequity", "Ajuste\ndeuda", "= WACC"]
    base = [0, D.RF, 0, D.COE, 0]
    inc  = [D.RF, D.BETA*D.ERP, D.COE, D.WACC-D.COE, D.WACC]
    cols = [CIELO, ACERO, AZUL, OCRE, ROJO]
    for i in range(5):
        ax.bar(i, inc[i], 0.6, bottom=base[i], color=cols[i])
        ax.text(i, base[i]+inc[i]+0.12, pct(inc[i] if i in (0,1) else (D.COE if i==2 else (D.WACC-D.COE if i==3 else D.WACC))),
                ha="center", fontsize=7.6, color=TINTA, fontweight="bold" if i in (2,4) else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels(pasos, fontsize=7.2)
    ax.set_ylim(0, 11); ax.set_yticklabels([])
    deco(ax, "El WACC, ladrillo a ladrillo", f"Coste de capital construido input a input (%) · rf {D.es(D.RF,1)}% · ERP {D.es(D.ERP,1)}% · beta {D.es(D.BETA,2)}",
         "Fuente: modelo propio. SUPUESTO/INFERENCIA. Estructura ~98% equity.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.12)
    save(fig, "17_wacc")

# ── 18 · Heatmap de sensibilidad WACC × g terminal ──────────────────────
def c18():
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    M = np.array(D.SENS)
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("qg", [ROJOSC, GCLARO, NOCHE])
    im = ax.imshow(M, cmap=cmap, aspect="auto")
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            base = (D.WACC_GRID[i]==D.WACC and D.GT_GRID[j]==2.5)
            ax.text(j, i, f"{M[i,j]}", ha="center", va="center", fontsize=7.8,
                    color="white" if M[i,j]>360 or M[i,j]<300 else TINTA,
                    fontweight="bold" if base else "normal")
    ax.set_xticks(range(5)); ax.set_xticklabels([pct(g) for g in D.GT_GRID], fontsize=7.2)
    ax.set_yticks(range(5)); ax.set_yticklabels([pct(w) for w in D.WACC_GRID], fontsize=7.2)
    ax.set_xlabel("Crecimiento terminal", fontsize=7.8, color=GRIS)
    ax.set_ylabel("WACC", fontsize=7.8, color=GRIS)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    deco(ax, "El valor bajo estrés", "Valor DCF base por acción (USD ) según WACC × crecimiento terminal · negrita = caso central",
         f"Fuente: modelo propio. SUPUESTO. Incluso en el cuadrante más severo (USD {D.SENS_MIN}) el valor supera el precio de hoy (USD {int(D.PRECIO)}).", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.10, right=0.98)
    save(fig, "18_sensibilidad")

# ── 19 · EPS / owner earnings por acción, 5 años ────────────────────────
def c19():
    yrs=["FY22","FY23","FY24","FY25","FY26E"]
    eps=[13.7, 15.9, 18.4, D.EPS_TTM, 24.4]   # EPS (non-GAAP FY26E guía)
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    cols=[NOCHE,NOCHE,NOCHE,NOCHE,CIELO]
    ax.bar(range(5), eps, 0.55, color=cols)
    for i,v in enumerate(eps): ax.text(i, v+0.3, f"${v:.1f}", ha="center", fontsize=7.8, color=TINTA)
    ax.set_xticks(range(5)); ax.set_xticklabels(yrs, fontsize=8.2)
    ax.set_ylim(0, 28); ax.set_yticklabels([])
    ax.text(4, 25.6, "guía non-GAAP", ha="center", fontsize=6.6, color=GRIS, style="italic")
    deco(ax, "El compounding no se ha detenido", "Beneficio por acción (USD ) · FY26E = guía non-GAAP USD 24,35-24,45",
         "Fuente: Adobe releases. HECHO (FY22-25 aprox.) / guía FY26 (INFERENCIA). Recompras reducen el denominador.", fig=fig)
    fig.subplots_adjust(top=0.76, bottom=0.10)
    save(fig, "19_eps")

# ── 20 · Penetración / runway de monetización IA sobre MAU ──────────────
def c20():
    fig, ax = plt.subplots(figsize=(7.6, 2.9))
    # 850M MAU; suscriptores de pago estimados ~40M → penetración monetizada baja
    total = 850; pagados = 40
    ax.barh(0, pagados, 0.5, color=AZUL)
    ax.barh(0, total-pagados, 0.5, left=pagados, color=GCLARO)
    ax.text(pagados/2, 0, f"~{pagados}M\npagados", ha="center", va="center", fontsize=7.4, color="white", fontweight="bold")
    ax.text(pagados+(total-pagados)/2, 0, f"~{total-pagados}M gratuitos / freemium — el runway de conversión", ha="center", va="center", fontsize=7.6, color=TINTA, style="italic")
    ax.set_xlim(0, total); ax.set_ylim(-0.5, 0.5); ax.axis("off")
    deco(ax, "850 millones de razones para el freemium", "Base de usuarios activos mensuales vs base monetizada (M) · el giro que presiona el ARR hoy y lo alimenta mañana",
         "Fuente: Adobe Q2FY26 (850M MAU). HECHO. Pagados = estimación (INFERENCIA).", fig=fig, flag_y=0.95)
    fig.subplots_adjust(top=0.64, bottom=0.08)
    save(fig, "20_runway")

if __name__ == "__main__":
    for fn in [c01,c02,c03,c04,c05,c07,c08,c09,c10,c11,c13,c15,c17,c18,c19,c20]:
        fn(); print("ok", fn.__name__)
    print("charts done")
