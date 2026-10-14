# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis CME v2. Todos los datos verificados en fuente primaria."""
import numpy as np, matplotlib.pyplot as plt
from chart_style import deco, save, P
from matplotlib.patches import Rectangle

# ── 01 · Anatomía del peaje: cuánto cobra por cada tipo de contrato ──────
def c01():
    lin = ["Tipos de\ninterés","Índices de\nrenta variable","Energía","Agrícolas","Metales","Divisas"]
    adv = [14.532, 8.633, 2.667, 2.080, 0.941, 0.989]
    rpc = [0.480, 0.605, 1.131, 1.426, 1.315, 0.813]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.5))
    b = a1.bar(range(6), adv, color=[P["azul"]]*2+[P["azul_acero"]]*4, width=.62)
    for i, v in enumerate(adv): a1.text(i, v+.35, f"{v:.1f}".replace(".",","), ha="center", fontsize=8.4, fontweight="bold")
    a1.set_xticks(range(6)); a1.set_xticklabels(lin, fontsize=7.4)
    a1.set_ylabel("millones de contratos al día"); a1.set_ylim(0, 17)
    a1.set_title("CUÁNTOS contratos mueve", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)
    cols = [P["rojo"] if r < .7 else (P["ocre"] if r < 1.2 else P["verde"]) for r in rpc]
    a2.bar(range(6), rpc, color=cols, width=.62)
    for i, v in enumerate(rpc): a2.text(i, v+.03, f"{v:.3f}".replace(".",","), ha="center", fontsize=8.4, fontweight="bold")
    a2.set_xticks(range(6)); a2.set_xticklabels(lin, fontsize=7.4)
    a2.set_ylabel("dólares de comisión por contrato"); a2.set_ylim(0, 1.62)
    a2.set_title("CUÁNTO cobra por cada uno", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=.76, bottom=.14, wspace=.22)
    deco([a1,a2], "El peaje al revés: cobra menos donde más pasa",
         "Su producto más voluminoso —tipos de interés— es el más barato; el agrícola, casi tres veces más caro. Segundo trimestre de 2026.",
         "Fuente: 8-K de resultados del 2T-2026 (acc. 0001156375-26-000042), tabla Quarterly Operating Statistics.", fig)
    save(fig, "01_peaje")

# ── 02 · La tijera: volumen sube, precio baja ───────────────────────────
def c02():
    an = np.array([2010, 2013, 2016, 2019, 2022, 2025])
    adv = np.array([12.167, 13.7, 15.6, 19.2, 23.3, 28.129])
    rpc = np.array([0.808, 0.760, 0.746, 0.706, 0.643, 0.696])
    fig, ax = plt.subplots(figsize=(11.2, 4.6)); ax2 = ax.twinx()
    ax.plot(an, adv, "-o", color=P["azul"], lw=2.6, ms=7, label="Contratos por día (millones)")
    ax2.plot(an, rpc, "-s", color=P["rojo"], lw=2.6, ms=7, label="Comisión por contrato (US$)")
    for x, y in zip(an, adv): ax.text(x, y+.9, f"{y:.1f}".replace(".",","), ha="center", fontsize=8, color=P["azul"], fontweight="bold")
    for x, y in zip(an, rpc): ax2.text(x, y-.035, f"{y:.3f}".replace(".",","), ha="center", fontsize=8, color=P["rojo"], fontweight="bold")
    ax.set_ylabel("millones de contratos al día", color=P["azul"]); ax.set_ylim(8, 33)
    ax2.set_ylabel("dólares por contrato", color=P["rojo"]); ax2.set_ylim(.58, .87)
    ax2.grid(False); ax2.spines["top"].set_visible(False); ax2.spines["left"].set_visible(False)
    ax.set_xticks(an)
    ax.text(2016.5, 30.4, "+5,75% al año", color=P["azul"], fontsize=9.6, fontweight="bold")
    ax2.text(2016.5, .655, "−0,99% al año", color=P["rojo"], fontsize=9.6, fontweight="bold")
    fig.subplots_adjust(top=.74, bottom=.10, right=.90, left=.075)
    deco(ax, "Quince años vendiendo más unidades cada vez más baratas",
         "El volumen compone al 5,75% anual y la tarifa se deshace al 0,99%. Esa diferencia es todo el crecimiento del negocio.",
         "Fuente: informes de volumen mensuales de CME Group y 10-K de cada ejercicio. Elaboración propia.", fig)
    save(fig, "02_tijera")

# ── 03 · Descomposición: ¿mezcla o precio? ──────────────────────────────
def c03():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.3))
    for ax, (mez, pre, inter, tot, lab) in zip((a1, a2), [
            (0.11, -1.23, -0.12, -1.24, "Segundo trimestre de 2026"),
            (1.91, -4.24, 0.00, -2.33, "Primer trimestre de 2026")]):
        vals = [mez, pre, inter]; names = ["Mezcla\n(qué se negocia)", "PRECIO\n(cuánto se cobra)", "Interacción"]
        cols = [P["verde"] if v > 0 else P["rojo"] for v in vals]
        ax.bar(range(3), vals, color=cols, width=.55)
        ax.bar([3], [tot], color=P["azul_noche"], width=.55)
        for i, v in enumerate(vals + [tot]):
            ax.text(i, v + (.16 if v > 0 else -.30), f"{v:+.2f}".replace(".",","), ha="center", fontsize=9, fontweight="bold")
        ax.axhline(0, color=P["tinta"], lw=1)
        ax.set_xticks(range(4)); ax.set_xticklabels(names + ["TOTAL"], fontsize=7.6)
        ax.set_ylim(-5.0, 2.6); ax.set_title(lab, fontsize=9.4, fontweight="bold", color=P["azul_noche"], pad=6)
        if ax is a1: ax.set_ylabel("céntimos de dólar por contrato")
    fig.subplots_adjust(top=.75, bottom=.15, wspace=.16)
    deco([a1,a2], "La tarifa no cae porque cambie la mezcla: cae porque baja el precio",
         "La mezcla de productos incluso AYUDÓ en los dos trimestres: todo el deterioro ocurre dentro de cada línea.",
         "Fuente: cálculo propio sobre el panel trimestral de ADV y comisión por contrato de las seis líneas, 8-K de 2021-2026. Error de reconstrucción máximo: 0,0007 US$ en 21 trimestres.", fig)
    save(fig, "03_mezcla_precio")

# ── 04 · Junio de 2026: el mercado no sabía cuánto valía ────────────────
def c04():
    f = ["26-05","29-05","01-06","02-06","05-06","10-06","12-06","17-06","18-06","22-06","24-06","26-06","29-06","30-06","06-07","15-07","24-07","03-08","12-08","21-08"]
    p = [282.54,273.54,257.76,250.53,257.40,255.94,269.53,252.54,246.38,245.20,231.68,221.00,218.58,220.83,234.76,245.18,255.31,266.17,262.17,275.17]
    fig, ax = plt.subplots(figsize=(11.2, 4.7))
    ax.plot(range(len(p)), p, "-", color=P["azul"], lw=2.4)
    ax.fill_between(range(len(p)), 200, p, color=P["azul_cielo"], alpha=.22)
    ax.axhspan(200, 235, color=P["verde"], alpha=.16)
    ax.text(0.4, 227, "ZONA DE PRIMER TRAMO  (≤235 US$)", fontsize=8.4, color=P["verde"], fontweight="bold")
    ax.scatter([12], [218.58], s=130, color=P["rojo"], zorder=6)
    ax.annotate("29-jun: 218,58 US$\n−20,1% en un mes", (12, 218.58), (5.6, 205),
                fontsize=8.6, color=P["rojo"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=P["rojo"], lw=1.3))
    ax.scatter([19], [275.17], s=110, color=P["azul_noche"], zorder=6)
    ax.annotate("21-ago: 275,17 US$", (19, 275.17), (14.2, 288), fontsize=8.6, color=P["azul_noche"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=P["azul_noche"], lw=1.3))
    ax.annotate("18-jun: CME demanda\na su propio regulador", (8, 246.38), (7.3, 292), fontsize=8, color=P["gris"],
                arrowprops=dict(arrowstyle="->", color=P["gris_medio"], lw=1))
    ax.set_xticks(range(0, len(p), 2)); ax.set_xticklabels([f[i] for i in range(0, len(f), 2)], fontsize=7.6)
    ax.set_ylabel("dólares por acción"); ax.set_ylim(200, 300)
    fig.subplots_adjust(top=.76, bottom=.11, left=.075, right=.975)
    deco(ax, "Una quinta parte del valor se fue y volvió en ocho semanas",
         "Sin un solo informe financiero publicado entre medias. Si el mercado no sabe si vale 218 o 275, nadie lo sabe mejor.",
         "Fuente: histórico diario de Interactive Brokers (contrato 45127739), cierres de sesión. Elaboración propia.", fig)
    save(fig, "04_junio")

# ── 05 · CME contra el índice ───────────────────────────────────────────
def c05():
    lab = ["15 años\n(2011-2026)", "10 años\n(2016-2026)", "5 años\n(2021-2026)", "2026\nen curso"]
    cme = [12.56, 9.44, 4.09, 0.77]; spy = [13.16, 13.64, 10.86, 11.68]
    x = np.arange(4); w = .36
    fig, ax = plt.subplots(figsize=(11.2, 4.4))
    ax.bar(x-w/2, cme, w, color=P["azul"], label="CME Group")
    ax.bar(x+w/2, spy, w, color=P["gris_medio"], label="S&P 500")
    for i in range(4):
        ax.text(x[i]-w/2, cme[i]+.3, f"{cme[i]:.2f}%".replace(".",","), ha="center", fontsize=8.2, fontweight="bold", color=P["azul"])
        ax.text(x[i]+w/2, spy[i]+.3, f"{spy[i]:.2f}%".replace(".",","), ha="center", fontsize=8.2, fontweight="bold", color=P["gris"])
        ax.text(x[i], -1.55, f"{cme[i]-spy[i]:+.2f}".replace(".",","), ha="center", fontsize=9, fontweight="bold",
                color=P["rojo"] if cme[i] < spy[i] else P["verde"])
    ax.text(3.85, -1.55, "diferencia", fontsize=7.4, style="italic", color=P["gris"], ha="left")
    ax.axhline(0, color=P["tinta"], lw=.9)
    ax.set_xticks(x); ax.set_xticklabels(lab, fontsize=8.2); ax.set_ylim(-2.4, 16)
    ax.set_ylabel("rentabilidad anual del precio (%)")
    ax.legend(frameon=False, fontsize=8.6, loc="upper right")
    fig.subplots_adjust(top=.75, bottom=.13, left=.07)
    deco(ax, "Perdió contra el índice justo en su mejor ciclo",
         "Rentabilidad del precio. Con dividendos CME gana por +1,12 puntos a 10 años y +0,45 a 15 — y sigue perdiendo a 5.",
         "Fuente: histórico mensual de Interactive Brokers (CME y SPY), cierres de diciembre. Elaboración propia.", fig)
    save(fig, "05_vs_indice")

# ── 06 · Cboe alcanza el margen de CME ──────────────────────────────────
def c06():
    an = [2022, 2023, 2024, 2025, "2T-2026"]
    cme = [60.1, 62.3, 63.8, 64.9, 64.9]; cbo = [28.1, 44.0, 55.5, 62.0, 65.1]
    x = np.arange(5)
    fig, ax = plt.subplots(figsize=(11.2, 4.4))
    ax.plot(x, cme, "-o", color=P["azul"], lw=2.8, ms=8, label="CME Group")
    ax.plot(x, cbo, "-s", color=P["rojo"], lw=2.8, ms=8, label="Cboe (sobre ingreso neto)")
    for i in range(5):
        ax.text(x[i], cme[i]+1.4, f"{cme[i]:.1f}%".replace(".",","), ha="center", fontsize=8.2, color=P["azul"], fontweight="bold")
        ax.text(x[i], cbo[i]-3.0, f"{cbo[i]:.1f}%".replace(".",","), ha="center", fontsize=8.2, color=P["rojo"], fontweight="bold")
    ax.annotate("", (4, 64.9), (4, 65.1), arrowprops=dict(arrowstyle="-", color=P["tinta"]))
    ax.text(3.35, 70, "Cboe adelanta a CME\npor 0,2 puntos", fontsize=8.8, color=P["rojo"], fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(an, fontsize=8.6); ax.set_ylim(22, 76)
    ax.set_ylabel("margen de explotación (%)")
    ax.legend(frameon=False, fontsize=8.8, loc="lower right")
    fig.subplots_adjust(top=.75, bottom=.10, left=.07)
    deco(ax, "En cuatro años, el rival pasó de 32 puntos por detrás a adelantarle",
         "Margen de explotación. El de Cboe va sobre ingreso neto, que es la comparación correcta y la más exigente para él.",
         "Fuente: cuentas de resultados de CME Group y Cboe Global Markets ante la SEC (XBRL), cada ejercicio. Elaboración propia.", fig)
    save(fig, "06_margen")

# ── 07 · El foso medido por quien intenta cruzarlo ──────────────────────
def c07():
    fig, ax = plt.subplots(figsize=(11.2, 3.5))
    ax.barh([1], [42], color=P["rojo"], height=.5)
    ax.barh([0], [0.37], color=P["azul"], height=.5)
    ax.text(43, 1, "42%", va="center", fontsize=15, fontweight="bold", color=P["rojo"])
    ax.text(1.6, 0, "0,37%", va="center", fontsize=15, fontweight="bold", color=P["azul"])
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["FUTUROS del Tesoro\n(hay foso: la posición\nno se puede mudar)",
                        "CONTADO del Tesoro\n(no hay foso: cada\noperación empieza de cero)"], fontsize=8.6)
    ax.set_xlim(0, 52); ax.set_xlabel("cuota de mercado de FMX (%)")
    fig.subplots_adjust(top=.72, bottom=.20, left=.235, right=.97)
    deco(ax, "La anchura del foso, medida por el atacante",
         "Misma empresa, misma tecnología y los mismos diez bancos detrás, compitiendo en dos mercados vecinos a la vez.",
         "Fuente: BGC Group, resultados del 2T-2026 (acc. 0001628280-26-055187) y 8-K del 2T-2026 de CME Group. Elaboración propia.", fig)
    save(fig, "07_foso")

# ── 08 · El espectro de la beta ─────────────────────────────────────────
def c08():
    nom = ["1 año diario","36 meses mensual","24 meses semanal","5 años diario","60 meses mensual",
           "Dimson (±2)","10 años diario","Sectorial (pares)","Blume","Anual 2009-2025"]
    b   = [-0.316, -0.003, 0.136, 0.231, 0.275, 0.397, 0.578, 0.638, 0.717, 1.022]
    lo  = [-0.540, -0.607, -0.130, 0.165, -0.065, None, 0.530, None, None, 0.290]
    hi  = [-0.092, 0.601, 0.401, 0.296, 0.615, None, 0.625, None, None, 1.750]
    y = np.arange(10)
    fig, ax = plt.subplots(figsize=(11.2, 5.0))
    ax.axvspan(0.63, 0.84, color=P["ocre"], alpha=.20)
    ax.axvline(0.73, color=P["ocre"], lw=2, ls="--")
    ax.text(0.745, 9.55, "La beta que corresponde\na una cartera de 14 nombres: 0,73", fontsize=8.4, color="#8a6508", fontweight="bold")
    ax.axvline(0.65, color=P["rojo"], lw=1.8)
    ax.text(0.20, -1.35, "← por debajo: CME está barata", fontsize=8.2, color=P["verde"], fontweight="bold")
    ax.text(0.90, -1.35, "por encima: CME está cara →", fontsize=8.2, color=P["rojo"], fontweight="bold")
    for i in range(10):
        if lo[i] is not None:
            ax.plot([lo[i], hi[i]], [y[i], y[i]], color=P["gris_medio"], lw=1.5, alpha=.85)
            ax.plot([lo[i], lo[i]], [y[i]-.16, y[i]+.16], color=P["gris_medio"], lw=1.5)
            ax.plot([hi[i], hi[i]], [y[i]-.16, y[i]+.16], color=P["gris_medio"], lw=1.5)
        ax.scatter([b[i]], [y[i]], s=68, color=P["azul"] if b[i] < .65 else P["rojo_oscuro"], zorder=5)
        ax.text(b[i], y[i]+.28, f"{b[i]:.3f}".replace(".",","), ha="center", fontsize=7.6, fontweight="bold")
    ax.axvline(0, color=P["tinta"], lw=.9, alpha=.6)
    ax.set_yticks(y); ax.set_yticklabels(nom, fontsize=8.2); ax.set_ylim(-1.7, 10.2)
    ax.set_xlim(-.85, 1.85); ax.set_xlabel("beta estimada  (barra gris = margen de error al 95%)")
    fig.subplots_adjust(top=.79, bottom=.13, left=.175, right=.975)
    deco(ax, "Diez formas de medir lo mismo, diez respuestas distintas",
         "La beta mide cuánto se mueve la acción cuando se mueve el mercado. En CME vale desde −0,32 hasta 1,02 según cómo se mida.",
         "Fuente: regresiones propias sobre precios de Interactive Brokers y de la API de Nasdaq, validados entre sí (120 de 121 cierres coinciden al céntimo).", fig)
    save(fig, "08_beta")

# ── 09 · Los tres escenarios ────────────────────────────────────────────
def c09():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    esc = ["PESIMISTA\n30% de probabilidad", "CENTRAL\n50%", "OPTIMISTA\n20%", "MEDIA\nPONDERADA"]
    val = [142.72, 230.34, 306.33, 219.25]
    cols = [P["rojo_oscuro"], P["azul"], P["verde"], P["azul_noche"]]
    ax.bar(range(4), val, color=cols, width=.56)
    for i, v in enumerate(val):
        ax.text(i, v+7, f"{v:.0f} US$", ha="center", fontsize=11, fontweight="bold", color=cols[i])
    ax.axhline(275.03, color=P["rojo"], lw=2.2, ls="--")
    ax.text(3.52, 280, "PRECIO HOY\n275,03 US$", fontsize=8.8, color=P["rojo"], fontweight="bold", ha="right")
    ax.set_xticks(range(4)); ax.set_xticklabels(esc, fontsize=8.2); ax.set_ylim(0, 345)
    ax.set_ylabel("valor por acción (US$)")
    ax.text(0, 20, "Bajan los tipos,\nel rival gana cuota,\nla tarifa sigue cayendo", ha="center", fontsize=7.4, color="white", style="italic")
    ax.text(1, 20, "Sigue lo que ya hace:\nvolumen +5,75%,\ntarifa −1%", ha="center", fontsize=7.4, color="white", style="italic")
    ax.text(2, 20, "Gana la compensación\ndel Tesoro y el minorista\nsin canibalizar", ha="center", fontsize=7.4, color="white", style="italic")
    fig.subplots_adjust(top=.76, bottom=.13, left=.075)
    deco(ax, "Tres futuros posibles, descontados a hoy",
         "Descuento de flujos a diez años. El precio de hoy sólo lo alcanza el escenario optimista, al que doy un 20%.",
         "Fuente: modelo propio sobre el flujo de caja libre a la firma de 4.344 M US$ (FY2026 estimado). Cada escenario con su narrativa causal y su proyección año a año.", fig)
    save(fig, "09_escenarios")

# ── 10 · El valor depende de una sola variable ──────────────────────────
def c10():
    betas = np.array([0.275, 0.397, 0.490, 0.578, 0.630, 0.730, 0.850, 1.022])
    v25 = np.array([405, 351, 319, 293, 280, 252, 235, 208])
    v30 = np.array([468, 398, 356, 324, 308, 276, 254, 223])
    fig, ax = plt.subplots(figsize=(11.2, 4.7))
    ax.fill_between(betas, v25, v30, color=P["azul_cielo"], alpha=.42, label="Rango según el crecimiento a perpetuidad (2,5%–3,0%)")
    ax.plot(betas, v30, "-", color=P["azul"], lw=2.2)
    ax.plot(betas, v25, "-", color=P["azul_acero"], lw=2.2)
    ax.axhline(275.03, color=P["rojo"], lw=2.2, ls="--")
    ax.text(0.29, 283, "PRECIO HOY  275,03 US$", fontsize=9, color=P["rojo"], fontweight="bold")
    ax.axvspan(0.63, 0.84, color=P["ocre"], alpha=.22)
    ax.text(0.735, 430, "beta de TU cartera", fontsize=8.6, color="#8a6508", fontweight="bold", ha="center")
    ax.scatter([0.73], [276], s=150, color=P["rojo_oscuro"], zorder=6, marker="D")
    ax.annotate("Con tu beta: 252–276 US$\nEl margen de seguridad es cero", (0.73, 276), (0.80, 350),
                fontsize=8.8, fontweight="bold", color=P["rojo_oscuro"],
                arrowprops=dict(arrowstyle="->", color=P["rojo_oscuro"], lw=1.4))
    ax.set_xlabel("beta empleada  (cuánto riesgo de mercado se le atribuye a CME)")
    ax.set_ylabel("valor por acción (US$)"); ax.set_ylim(180, 480); ax.set_xlim(.24, 1.06)
    ax.legend(frameon=False, fontsize=8.4, loc="lower left")
    fig.subplots_adjust(top=.76, bottom=.13, left=.075)
    deco(ax, "Toda la valoración cuelga de un solo número",
         "Mover la beta de 0,275 a 1,022 cambia el valor de 468 a 223 dólares. Ningún dato del negocio tiene esa palanca.",
         "Fuente: modelo propio. Tipo sin riesgo 4,74% (Tesoro a 10 años, 21-ago-2026) y prima de riesgo 4,23% (Damodaran, 1-ago-2026).", fig)
    save(fig, "10_beta_valor")

# ── 11 · Mapa de zonas de precio ────────────────────────────────────────
def c11():
    fig, ax = plt.subplots(figsize=(11.2, 3.2))
    zonas = [(150, 200, P["verde"], "COMPRA PLENA"), (200, 235, "#9aab72", "PRIMER TRAMO"),
             (235, 290, P["ocre"], "PRECIO JUSTO"), (290, 330, P["terracota"], "CARO"), (330, 360, P["rojo_oscuro"], "MUY CARO")]
    for a, b, c, l in zonas:
        ax.add_patch(Rectangle((a, 0), b-a, 1, color=c, alpha=.80))
        ax.text((a+b)/2, .5, l, ha="center", va="center", fontsize=8.2, fontweight="bold",
                color="white" if c != P["ocre"] else P["tinta"])
    for x, lab, col, dy in [(275.03, "HOY\n275,03", P["rojo"], 1.30), (218.31, "mínimo de junio\n218,31", P["azul_noche"], 1.30),
                            (321.32, "máximo 52s\n321,32", P["gris"], -0.55), (267, "valor central\n267", P["tinta"], -0.55)]:
        ax.plot([x, x], [0, 1], color=col, lw=2.4)
        ax.text(x, dy, lab, ha="center", fontsize=8.4, fontweight="bold", color=col,
                va="bottom" if dy > 1 else "top")
    ax.set_xlim(150, 360); ax.set_ylim(-1.0, 2.1); ax.set_yticks([])
    ax.set_xticks([150, 200, 235, 267, 290, 330, 360])
    ax.set_xlabel("dólares por acción")
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.grid(False)
    fig.subplots_adjust(top=.70, bottom=.20, left=.05, right=.975)
    deco(ax, "Dónde está el precio hoy, y dónde tendría que estar",
         "El mínimo de junio entró en zona de compra durante seis sesiones. Hoy el precio está en la banda de «precio justo».",
         "Fuente: elaboración propia sobre los cuatro motores de valoración (flujos descontados, PER, valor de empresa y rentabilidad total).", fig)
    save(fig, "11_zonas")

# ── 12 · La prueba del bono ─────────────────────────────────────────────
def c12():
    fig, ax = plt.subplots(figsize=(11.2, 4.3))
    cat = ["Bono del Tesoro\nde EE.UU. a 10 años", "CME: beneficio\nnormalizado", "CME: flujo de caja\nlibre sobre el valor\nde la empresa", "CME: dividendo\n(regular + variable)"]
    val = [4.74, 4.06, 4.21, 4.09]
    cols = [P["gris_medio"], P["azul"], P["azul_acero"], P["azul_cielo"]]
    ax.bar(range(4), val, color=cols, width=.5)
    for i, v in enumerate(val):
        ax.text(i, v+.09, f"{v:.2f}%".replace(".",","), ha="center", fontsize=11.5, fontweight="bold", color=cols[i] if i else P["tinta"])
    ax.axhline(4.74, color=P["rojo"], lw=2, ls="--")
    ax.text(3.45, 4.83, "el activo SIN RIESGO", fontsize=8.6, color=P["rojo"], fontweight="bold", ha="right")
    ax.set_xticks(range(4)); ax.set_xticklabels(cat, fontsize=8.0); ax.set_ylim(0, 5.6)
    ax.set_ylabel("rentabilidad anual (%)")
    fig.subplots_adjust(top=.74, bottom=.17, left=.07)
    deco(ax, "El accionista cobra menos que quien no corre ningún riesgo",
         "Todo lo que CME paga por encima del bono tiene que venir del crecimiento. Y su crecimiento es volumen menos tarifa.",
         "Fuente: curva diaria del Tesoro de EE.UU. (21-ago-2026) y cálculo propio sobre el beneficio de los últimos doce meses y el flujo de caja libre.", fig)
    save(fig, "12_bono")

# ── 13 · De dónde salió el dinero repartido ─────────────────────────────
def c13():
    fig, ax = plt.subplots(figsize=(11.2, 4.2))
    ax.bar([0], [2207.0], color=P["azul"], width=.5, label="Caja generada por el negocio")
    ax.bar([1], [3165.7], color=P["azul_acero"], width=.5)
    ax.bar([1], [1236.9], bottom=[3165.7], color=P["azul_cielo"], width=.5)
    ax.text(0, 2320, "2.207 M US$", ha="center", fontsize=10, fontweight="bold", color=P["azul"])
    ax.text(1, 1500, "Dividendos\n3.166 M", ha="center", fontsize=9, fontweight="bold", color="white")
    ax.text(1, 3720, "Recompras\n1.237 M", ha="center", fontsize=9, fontweight="bold", color=P["tinta"])
    ax.text(1, 4530, "4.403 M US$", ha="center", fontsize=10, fontweight="bold", color=P["rojo"])
    ax.annotate("", (1.36, 2207), (1.36, 4402.6), arrowprops=dict(arrowstyle="<->", color=P["rojo"], lw=2))
    ax.text(1.42, 3300, "Faltan 2.196 M US$.\nLos puso la venta de OSTTRA\n(1.591 M cobrados a KKR)\ny la caja del balance,\nque cayó un 51,5%.", fontsize=8.6, color=P["rojo"], fontweight="bold", va="center")
    ax.set_xticks([0, 1]); ax.set_xticklabels(["LO QUE ENTRÓ\npor el negocio", "LO QUE SALIÓ\nhacia el accionista"], fontsize=8.8)
    ax.set_xlim(-.55, 2.65); ax.set_ylim(0, 5200); ax.set_ylabel("millones de dólares")
    fig.subplots_adjust(top=.76, bottom=.13, left=.085)
    deco(ax, "En el primer semestre repartió el doble de lo que generó",
         "Primer semestre de 2026. Repartir el 199,5% de la caja operativa es sostenible una vez, cuando se acaba de vender un activo. No todos los años.",
         "Fuente: 10-Q del 2T-2026 (acc. 0001156375-26-000047), estado de flujos de efectivo y balance consolidado.", fig)
    save(fig, "13_payout")

for f in [c01,c02,c03,c04,c05,c06,c07,c08,c09,c10,c11,c12,c13]:
    f(); print("ok", f.__name__)
