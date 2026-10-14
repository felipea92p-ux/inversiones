# -*- coding: utf-8 -*-
"""Gráficos · ULTRA TESIS MSCI · 26-ago-2026. Fuente: 10-K FY2025, 10-Q 2T-2026, IBKR."""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save, plt as _plt
from paleta_qg import PALETA as P

W = 11.0   # ancho estándar en pulgadas/1.45 -> figuras apaisadas


# ─────────────────────────────────────────────────────────────────────────────
def g1_aum():
    """De dónde sale el dinero que MSCI cobra."""
    fig, ax = plt.subplots(figsize=(9.6, 4.5))
    fig.subplots_adjust(top=0.74, bottom=0.14, left=0.09, right=0.98)
    lab = ["1T-25", "2T-25", "3T-25", "4T-25", "1T-26", "2T-26"]
    mkt = [16.4, 193.0, 140.0, 62.8, -41.0, 376.0]
    flu = [42.0, 48.5, 46.4, 66.9, 103.0, 39.0]
    x = np.arange(len(lab)); w = 0.38
    ax.bar(x - w/2, mkt, w, color=P["rojo"], label="Subida de la bolsa (no es dinero nuevo)")
    ax.bar(x + w/2, flu, w, color=P["azul"], label="Dinero nuevo que entra de verdad")
    for i, (m, f) in enumerate(zip(mkt, flu)):
        ax.text(i - w/2, m + (9 if m >= 0 else -22), f"{m:+.0f}", ha="center",
                fontsize=8, color=P["tinta"], fontweight="bold")
        ax.text(i + w/2, f + 9, f"{f:+.0f}", ha="center", fontsize=8, color=P["tinta"])
    ax.axhline(0, color=P["gris"], lw=0.8)
    ax.set_xticks(x); ax.set_xticklabels(lab)
    ax.set_ylabel("Variación trimestral del AUM (miles de millones de US$)")
    ax.legend(frameon=False, fontsize=8.2, loc="upper left")
    ax.set_ylim(-90, 440)
    deco(ax, "De dónde sale el dinero sobre el que MSCI cobra",
         "En el último trimestre, nueve de cada diez dólares nuevos los puso la bolsa, no un cliente.",
         "Fuente: MSCI 10-K FY2025 y 10-Q 2T-2026, tabla «Sequential Change in Value» (HECHO).", fig)
    save(fig, "g1_aum")


# ─────────────────────────────────────────────────────────────────────────────
def g2_motor():
    """El motor comercial está parado; el ingreso sube igual."""
    fig, ax = plt.subplots(figsize=(9.6, 4.3))
    fig.subplots_adjust(top=0.72, bottom=0.20, left=0.09, right=0.98)
    lab = ["Ventas brutas\nnuevas", "Ventas netas\nnuevas", "Ingresos\ncontables",
           "Run Rate de\ncomisión s/ activos"]
    val = [0.4, 3.3, 9.7, 25.6]
    col = [P["rojo"], P["terracota"], P["azul_acero"], P["azul"]]
    b = ax.bar(lab, val, color=col, width=0.6)
    for r, v in zip(b, val):
        ax.text(r.get_x() + r.get_width()/2, v + 0.6, f"{v:.1f}%".replace(".", ","),
                ha="center", fontsize=10.5, fontweight="bold", color=P["tinta"])
    ax.set_ylabel("Crecimiento en 2025 (%)")
    ax.set_ylim(0, 30)
    deco(ax, "El motor comercial está parado. El ingreso sube igual.",
         "Lo que MSCI vendió creció 0,4%. Lo que cobra por el nivel de la bolsa, 25,6%.",
         "Fuente: MSCI 10-K FY2025 — tablas de Sales y de Run Rate (HECHO).", fig)
    save(fig, "g2_motor")


# ─────────────────────────────────────────────────────────────────────────────
def g3_segmentos():
    """Un negocio que paga por tres."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.8, 4.4))
    fig.subplots_adjust(top=0.72, bottom=0.13, left=0.10, right=0.97, wspace=0.42)
    seg = ["Índices", "Analytics", "Sosten. y\nClima", "Activos\nprivados"]
    ing = [1786.8, 714.4, 353.9, 279.3]
    ebd = [1366.0, 342.5, 128.5, 69.4]
    mg  = [76.4, 47.9, 36.3, 24.9]
    y = np.arange(len(seg))[::-1]
    a1.barh(y, ing, 0.62, color=P["azul_cielo"], label="Ingresos")
    a1.barh(y, ebd, 0.62, color=P["azul"], label="Beneficio (EBITDA aj.)")
    for i, (r, e) in enumerate(zip(ing, ebd)):
        a1.text(r + 40, y[i], f"{r:,.0f}".replace(",", "."), va="center", fontsize=8.4,
                color=P["gris"])
    a1.set_yticks(y); a1.set_yticklabels(seg, fontsize=8.6)
    a1.set_xlabel("Millones de US$, 2025")
    a1.legend(frameon=False, fontsize=7.8, loc="lower right")
    a1.set_xlim(0, 2150)

    c = [P["azul"], P["azul_acero"], P["terracota"], P["rojo"]]
    b = a2.bar(range(4), mg, 0.6, color=c)
    for r, v in zip(b, mg):
        a2.text(r.get_x() + r.get_width()/2, v + 1.6, f"{v:.1f}%".replace(".", ","),
                ha="center", fontsize=9.4, fontweight="bold", color=P["tinta"])
    a2.set_xticks(range(4)); a2.set_xticklabels(seg, fontsize=8.6)
    a2.set_ylabel("Margen de beneficio (%)"); a2.set_ylim(0, 90)
    deco([a1, a2], "MSCI no son cuatro negocios: es uno que paga por tres",
         "Índices es el 57% de lo que factura y el 72% de lo que gana. Lo demás casi no deja margen.",
         "Fuente: MSCI 10-K FY2025, resultados por segmento (HECHO).", fig)
    save(fig, "g3_segmentos")


# ─────────────────────────────────────────────────────────────────────────────
def g4_retencion():
    """La retención por segmento — y el trimestre que importa."""
    fig, ax = plt.subplots(figsize=(9.6, 4.3))
    fig.subplots_adjust(top=0.73, bottom=0.14, left=0.08, right=0.98)
    seg = ["Índices", "Analytics", "Sosten. y Clima", "Activos privados", "TOTAL"]
    a24 = [94.7, 94.1, 92.8, 90.6, 93.7]
    a25 = [95.9, 94.3, 93.2, 91.3, 94.4]
    q4  = [95.3, 93.7, 91.0, 89.2, 93.4]
    x = np.arange(len(seg)); w = 0.27
    ax.bar(x - w, a24, w, color=P["azul_cielo"], label="Año 2024")
    ax.bar(x,     a25, w, color=P["azul"],       label="Año 2025")
    ax.bar(x + w, q4,  w, color=P["rojo"],       label="Sólo 4T-2025 (el trimestre de renovar)")
    for i in range(len(seg)):
        ax.text(x[i] + w, q4[i] - 1.4, f"{q4[i]:.1f}".replace(".", ","), ha="center",
                fontsize=7.8, color="white", fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(seg, fontsize=8.6)
    ax.set_ylim(85, 98); ax.set_ylabel("Clientes que renuevan (%)")
    ax.legend(frameon=False, fontsize=8, loc="lower left", ncol=3)
    deco(ax, "El 96% de retención del que todos hablan es sólo la mitad del negocio",
         "El dato de la compañía entera es 94,4%. En activos privados, en el trimestre que importa, 89,2%.",
         "Fuente: MSCI 10-K FY2025, tabla Retention Rate (HECHO).", fig)
    save(fig, "g4_retencion")


# ─────────────────────────────────────────────────────────────────────────────
def g5_deuda():
    """El apalancamiento real contra el publicado."""
    fig, ax = plt.subplots(figsize=(9.6, 4.3))
    fig.subplots_adjust(top=0.73, bottom=0.14, left=0.09, right=0.98)
    emp = ["CME", "Cboe", "Moody's", "S&P Global", "FICO", "ICE", "MSCI"]
    val = [-0.25, -0.25, 1.20, 1.50, 2.69, 3.00, 2.98]
    col = [P["verde"], P["verde"], P["azul"], P["azul"], P["ocre"], P["rojo_oscuro"], P["rojo"]]
    b = ax.bar(emp, val, 0.58, color=col)
    for r, v, e in zip(b, val, emp):
        txt = "caja neta" if v < 0 else f"{v:.2f}x".replace(".", ",")
        ax.text(r.get_x() + r.get_width()/2, v + (0.10 if v > 0 else -0.42), txt,
                ha="center", fontsize=8.8, fontweight="bold" if e == "MSCI" else "normal",
                color=P["tinta"])
    ax.axhline(2.5, color=P["rojo"], ls="--", lw=1.1)
    ax.text(-0.42, 2.60, "umbral de vigilancia 2,5x", fontsize=7.6, style="italic",
            color=P["rojo"], ha="left")
    ax.annotate("el documento de agosto\npublicaba 2,7x", xy=(6, 3.02), xytext=(4.30, 3.80),
                fontsize=7.8, style="italic", color=P["gris"],
                arrowprops=dict(arrowstyle="->", color=P["gris"], lw=0.8))
    ax.axhline(0, color=P["gris"], lw=0.8)
    ax.set_ylabel("Deuda neta / EBITDA"); ax.set_ylim(-0.7, 4.2)
    deco(ax, "MSCI no debe 2,7 veces lo que gana. Debe 2,98.",
         "Con su propio EBITDA declarado, queda exactamente donde ICE — la que el ranking castigó por deber demasiado.",
         "MSCI (6.024 M / 1.906 M) y FICO: cálculo propio sobre 10-K y 10-Q [HECHO].\n"
         "Las otras cinco proceden del estudio del 25-ago-2026 y no se han reverificado aquí [SUPUESTO].", fig)
    save(fig, "g5_deuda")


# ─────────────────────────────────────────────────────────────────────────────
def g6_recompra():
    """Recompra apalancada: el tercer color que falta."""
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    fig.subplots_adjust(top=0.72, bottom=0.14, left=0.09, right=0.98)
    emp = ["Moody's", "MSCI", "FICO"]
    fcf = [2575, 1549, 770]
    dev = [2308, 3041, 1415]
    x = np.arange(3); w = 0.36
    ax.bar(x - w/2, fcf, w, color=P["azul"], label="Caja que genera el negocio")
    ax.bar(x + w/2, dev, w, color=P["rojo"], label="Caja que entrega al accionista")
    for i, (f, d) in enumerate(zip(fcf, dev)):
        ax.text(i - w/2, f + 60, f"{f:,}".replace(",", "."), ha="center", fontsize=8.4)
        ax.text(i + w/2, d + 60, f"{d:,}".replace(",", "."), ha="center", fontsize=8.4,
                fontweight="bold")
        pct = d / f * 100
        ax.text(i, -370, f"{pct:.0f}% de su caja".replace(".", ","), ha="center",
                fontsize=9, fontweight="bold",
                color=P["rojo"] if pct > 100 else P["verde"])
    ax.set_xticks(x); ax.set_xticklabels(emp, fontsize=10)
    ax.set_ylabel("Millones de US$, 2025"); ax.set_ylim(-500, 3500)
    ax.legend(frameon=False, fontsize=8.2, loc="upper right")
    deco(ax, "Al gráfico de «cuánta empresa te queda» le falta un color",
         "Recomprar con deuda no te devuelve valor: te cambia acciones por deuda. MSCI entregó el doble de lo que ganó.",
         "Fuente: 10-K FY2025 de cada compañía; recompras + dividendos frente a flujo de caja libre (HECHO).", fig)
    save(fig, "g6_recompra")


# ─────────────────────────────────────────────────────────────────────────────
def g7_valor():
    """Escenarios de valor contra precio (re-corregido: g-inf=0, dos rondas de auditoria 26-ago-2026)."""
    fig, ax = plt.subplots(figsize=(9.6, 4.5))
    fig.subplots_adjust(top=0.72, bottom=0.13, left=0.13, right=0.97)
    et = ["Escenario\npesimista", "Escenario\ncentral", "Escenario\noptimista"]
    vv = [192.12, 260.87, 400.22]
    cc = [P["rojo_oscuro"], P["azul"], P["verde"]]
    y = np.arange(3)[::-1]
    ax.barh(y, vv, 0.5, color=cc)
    for i, v in enumerate(vv):
        ax.text(v + 9, y[i], f"{v:,.0f} US$".replace(",", "."), va="center",
                fontsize=10, fontweight="bold", color=P["tinta"])
    ax.axvline(564.31, color=P["tinta"], lw=2.0)
    ax.text(571, 1.45, "PRECIO HOY\n564,31 US$", fontsize=9.2, fontweight="bold",
            color=P["tinta"], va="center")
    ax.axvline(214.30, color=P["rojo"], ls="--", lw=1.3)
    ax.text(224, 2.74, "zona de compra: 214 US$", fontsize=8.6, style="italic",
            color=P["rojo"], ha="left", va="top")
    ax.set_yticks(y); ax.set_yticklabels(et, fontsize=9)
    ax.set_xlabel("Valor por acción (US$)"); ax.set_xlim(0, 700)
    ax.set_ylim(-0.55, 2.92)
    deco(ax, "Ni forzando todos los diales a favor sale el precio de hoy",
         "El escenario optimista exige ademas que MSCI cambie su politica de recompra. Aun asi vale 400. Cotiza a 564.",
         "Modelo consolidado, r=9,60% (regla vigente sin beta), g-inf=0 (reinversion negativa), "
         "re-corregido 26-ago-2026 (INFERENCIA sobre datos de 10-K).", fig)
    save(fig, "g7_valor")


# ─────────────────────────────────────────────────────────────────────────────
def g8_inverso():
    """DCF inverso: lo exigido contra lo conseguido (corregido 26-ago-2026)."""
    fig, ax = plt.subplots(figsize=(9.6, 4.3))
    fig.subplots_adjust(top=0.72, bottom=0.19, left=0.09, right=0.98)
    lab = ["Lo que el precio de hoy\nexige durante 10 años",
           "Lo que creció el negocio\nrecurrente en 2025",
           "Lo que creció lo que\nMSCI de verdad vendió"]
    val = [15.52, 7.7, 0.4]
    col = [P["rojo"], P["azul"], P["gris_medio"]]
    b = ax.bar(lab, val, 0.55, color=col)
    for r, v in zip(b, val):
        ax.text(r.get_x() + r.get_width()/2, v + 0.4, f"{v:.2f}%".replace(".", ","),
                ha="center", fontsize=12, fontweight="bold", color=P["tinta"])
    ax.set_ylabel("Crecimiento anual (%)"); ax.set_ylim(0, 18)
    deco(ax, "La pregunta al reves: que hay que creer para pagar 564?",
         "Que todo -suscripciones y comisiones a la vez- crezca un 15,5% cada ano hasta 2036, con g-inf=0.",
         "DCF inverso propio (protocolo Rappaport-Mauboussin), r=9,60%, g-inf=0 (reinversion negativa), "
         "re-corregido 26-ago-2026, sobre cifras del 10-K FY2025.", fig)
    save(fig, "g8_inverso")


# ─────────────────────────────────────────────────────────────────────────────
def g9_clima():
    """El segmento que se apaga."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.8, 4.2))
    fig.subplots_adjust(top=0.72, bottom=0.15, left=0.09, right=0.97, wspace=0.34)
    a1.bar(["2024", "2025"], [41.4, 21.9], 0.5, color=[P["azul"], P["rojo"]])
    a1.text(0, 42.6, "41,4", ha="center", fontsize=10, fontweight="bold")
    a1.text(1, 23.1, "21,9", ha="center", fontsize=10, fontweight="bold", color=P["rojo"])
    a1.set_ylabel("Ventas netas del año (millones de US$)"); a1.set_ylim(0, 52)
    a1.set_title("Lo que vendió, neto de bajas", fontsize=9.6, color=P["tinta"], pad=8)

    tr = ["2025\n(año completo)", "2T-2026\n(último dato)"]
    a2.bar(tr, [10.0, 1.9], 0.5, color=[P["azul_acero"], P["rojo"]])
    a2.text(0, 10.4, "10,0%", ha="center", fontsize=10, fontweight="bold")
    a2.text(1, 2.3, "1,9%", ha="center", fontsize=10, fontweight="bold", color=P["rojo"])
    a2.set_ylabel("Crecimiento del Run Rate (%)"); a2.set_ylim(0, 13)
    a2.set_title("Y a qué ritmo crece ya", fontsize=9.6, color=P["tinta"], pad=8)
    deco([a1, a2], "El motor de futuro que se apagó en un año",
         "Sostenibilidad y Clima: las ventas netas cayeron 47% y su crecimiento va camino de cero.",
         "Fuente: MSCI 10-K FY2025 y 10-Q 2T-2026 (HECHO).", fig)
    save(fig, "g9_clima")


# ─────────────────────────────────────────────────────────────────────────────
def g10_historia():
    """Ingresos y acciones: la doble palanca."""
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    fig.subplots_adjust(top=0.73, bottom=0.14, left=0.09, right=0.91)
    yr = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    ing = [1558, 1695, 2044, 2249, 2529, 2856, 3134]
    acc = [85.5, 84.5, 83.5, 81.2, 79.8, 79.0, 76.6]
    ax.bar(yr, ing, 0.62, color=P["azul"], label="Ingresos (millones de US$)")
    for x, v in zip(yr, ing):
        ax.text(x, v + 45, f"{v:,}".replace(",", "."), ha="center", fontsize=8)
    ax.set_ylabel("Ingresos (millones de US$)"); ax.set_ylim(0, 3800)
    a2 = ax.twinx()
    a2.plot(yr, acc, color=P["rojo"], lw=2.2, marker="o", ms=5, label="Acciones (millones)")
    a2.set_ylabel("Acciones en circulación (millones)", color=P["rojo"])
    a2.tick_params(colors=P["rojo"]); a2.set_ylim(60, 92)
    a2.grid(False)
    for s in ["top", "left"]:
        a2.spines[s].set_visible(False)
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    a2.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0, 0.90))
    deco(ax, "Seis años de ejecución que nadie discute",
         "Los ingresos se duplicaron (+12,3% al año) y las acciones bajaron un 10%. El negocio funciona.",
         "Fuente: 10-K de MSCI, ejercicios 2019 a 2025 (HECHO).", fig)
    save(fig, "g10_historia")


def g_sotp():
    """Suma de partes: valor de empresa por segmento."""
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    fig.subplots_adjust(top=0.72, bottom=0.14, left=0.20, right=0.95)
    seg = ["Índices", "Analytics", "Sostenibilidad\ny Clima", "Activos\nPrivados"]
    val = [19182, 3887, 1438, 961]
    col = [P["azul"], P["azul_acero"], P["terracota"], P["ocre"]]
    y = np.arange(4)[::-1]
    b = ax.barh(y, val, 0.6, color=col)
    tot = sum(val)
    for i, v in enumerate(val):
        pct = v/tot*100
        ax.text(v + 350, y[i], f"{v:,.0f} M  ({pct:.0f}%)".replace(",", "."),
                va="center", fontsize=9.2, fontweight="bold", color=P["tinta"])
    ax.set_yticks(y); ax.set_yticklabels(seg, fontsize=9.5)
    ax.set_xlabel("Valor de empresa, EV (millones de US$)")
    ax.set_xlim(0, 24000)
    deco(ax, "Indices son las tres cuartas partes del valor de MSCI",
         "Suma de partes: 25.467 M de EV. Sostenibilidad y Activos Privados, juntos, son solo el 9%.",
         "Modelo propio por segmento, r=9,60% comun, g-inf=0 (ROIIC no medible por segmento), 26-ago-2026.", fig)
    save(fig, "g_sotp")


if __name__ == "__main__":
    for f in (g1_aum, g2_motor, g3_segmentos, g4_retencion, g5_deuda,
              g6_recompra, g7_valor, g8_inverso, g9_clima, g10_historia, g_sotp):
        f(); print("ok:", f.__name__)
