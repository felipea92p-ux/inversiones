# -*- coding: utf-8 -*-
"""Gráficos · ULTRA TESIS HERMÈS INTERNATIONAL (HESAY/RMS.PA) · v2, valoración refrescada 04-sep-2026.
Fuentes: URD2025 (2026-03-19), PR_FY2025 (2026-02-12), PR_Q1_2026 (2026-04-15),
resultados H1 2026 (2026-07-29, incl. guía de capex FY2026 ~1.000 M EUR), IBKR (04-sep-2026),
Bund 10a TradingEconomics (04-sep-2026), Damodaran ERP, EUR/USD 1,1624 (04-sep-2026).
Valoración: DCF propio a 10 años, 3 escenarios (dcf_v3.py), reemplaza los dos vintages previos.
"""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save
from paleta_qg import PALETA as P

PRECIO_EUR = 1458.88


# ─────────────────────────────────────────────────────────────────────────────
def g1_margen():
    """Cinco años de margen que nunca baja de 39%, mientras las ventas casi se duplican."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.8, 4.4),
                                 gridspec_kw={"width_ratios": [1.15, 1.0]})
    fig.subplots_adjust(top=0.70, bottom=0.17, left=0.10, right=0.97, wspace=0.32)

    yr = [2021, 2022, 2023, 2024, 2025]
    ing = [8982, 11602, 13427, 15170, 16002]
    a1.bar(yr, ing, 0.62, color=P["azul_cielo"])
    for x, v in zip(yr, ing):
        a1.text(x, v + 280, f"{v:,.0f}".replace(",", "."), ha="center",
                fontsize=8.4, fontweight="bold", color=P["tinta"])
    a1.set_ylabel("Ingresos (millones de EUR)"); a1.set_ylim(0, 18200)
    a1.set_xticks(yr)

    marg = [39.3, 40.5, 42.1, 40.5, 41.1]
    a2.plot(yr, marg, color=P["rojo"], lw=2.4, marker="o", ms=6)
    for x, v in zip(yr, marg):
        a2.text(x, v + 0.55, f"{v:.1f}".replace(".", ",") + "%", ha="center",
                fontsize=9.2, fontweight="bold", color=P["rojo"])
    a2.axhline(39.0, color=P["gris_medio"], ls=":", lw=1.0)
    a2.text(2021.0, 37.6, "suelo de los últimos 5 años: 39%", fontsize=7.6,
            style="italic", color=P["gris"], ha="left")
    a2.set_ylabel("Margen operativo (%)"); a2.set_ylim(35, 45)
    a2.set_xticks(yr)

    deco([a1, a2], "Las ventas casi se duplicaron; el margen nunca se movió más de 3 puntos",
         "Un negocio que crece sin diluir su rentabilidad es la excepción, no la norma, en el lujo.",
         "Fuente: PR_FY2025 (2026-02-12), URD2025 §5.1, serie histórica auditada 2021-2025 (HECHO).", fig)
    save(fig, "g1_margen")


# ─────────────────────────────────────────────────────────────────────────────
def g2_metiers():
    """Dos velocidades dentro de la misma maison — FY2025, tipo de cambio constante."""
    fig, ax = plt.subplots(figsize=(9.6, 4.5))
    fig.subplots_adjust(top=0.72, bottom=0.20, left=0.09, right=0.97)
    lab = ["Marroquinería\ny Talabartería\n(44% de ventas)", "Prêt-à-porter\ny Accesorios",
           "Otros sectores\nHermès", "Perfumes\ny Belleza", "Relojería"]
    val = [13.0, 6.0, 11.0, -8.0, -2.0]
    col = [P["azul"] if v >= 0 else P["rojo_oscuro"] for v in val]
    b = ax.bar(lab, val, 0.55, color=col)
    for r, v in zip(b, val):
        y = v + (0.7 if v >= 0 else -1.3)
        ax.text(r.get_x() + r.get_width() / 2, y, f"{v:+.0f}%",
                ha="center", fontsize=11, fontweight="bold", color=P["tinta"])
    ax.axhline(0, color=P["gris"], lw=0.8)
    ax.set_ylabel("Crecimiento a tipo de cambio constante (%)"); ax.set_ylim(-11, 16)
    deco(ax, "El núcleo acelera; sólo la periferia retrocede",
         "Marroquinería —el corazón del foso, y el 44% de las ventas— creció el doble que el grupo. Perfumes y Relojería, satélites, son lo único que cae.",
         "Fuente: PR_FY2025 (2026-02-12), desglose por métier a tipo de cambio constante (HECHO).", fig)
    save(fig, "g2_metiers")


# ─────────────────────────────────────────────────────────────────────────────
def g3_wacc():
    """De dónde sale el 8,89% — ladrillo a ladrillo, y el cruce con la propia Hermès."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.8, 4.5),
                                 gridspec_kw={"width_ratios": [1.25, 1.0]})
    fig.subplots_adjust(top=0.71, bottom=0.20, left=0.08, right=0.97, wspace=0.32)

    lab = ["Bono soberano\na 10 años\n(en euros)", "+ Riesgo de\nla bolsa\n(beta x prima)",
           "+ Riesgo del país\ndonde vende\n(ponderado por\ningresos)", "= Coste de\nlos fondos\npropios"]
    base = [0, 3.35, 8.17, 0]
    alt = [3.35, 4.82, 0.77, 8.94]
    col = [P["azul_acero"], P["azul"], P["terracota"], P["azul_noche"]]
    x = np.arange(4)
    a1.bar(x, alt, 0.56, bottom=base, color=col)
    for i, (b0, h) in enumerate(zip(base, alt)):
        a1.text(i, b0 + h + 0.20, f"{h:.2f}".replace(".", ",") + "%", ha="center",
                fontsize=9.2, fontweight="bold", color=P["tinta"])
    a1.set_xticks(x); a1.set_xticklabels(lab, fontsize=7.6)
    a1.set_ylabel("Rentabilidad exigida (%)"); a1.set_ylim(0, 10.6)

    a2.bar(["Este documento\n(refrescado\n04-sep-2026)", "26-ago-2026\n(motor v3.1)",
            "Hermès consigo\nmisma (URD2025)"], [8.94, 8.89, 9.16], 0.5,
           color=[P["azul_noche"], P["azul_acero"], P["rojo"]])
    for i, v in enumerate([8.94, 8.89, 9.16]):
        a2.text(i, v + 0.16, f"{v:.2f}".replace(".", ",") + "%", ha="center",
                fontsize=10.5, fontweight="bold", color=P["tinta"])
    a2.set_ylabel("WACC (%)"); a2.set_ylim(0, 10.9)
    a2.set_title("Refrescado y estable: sigue por debajo de Hermès consigo misma", fontsize=8.6,
                 color=P["tinta"], pad=8)

    deco([a1, a2], "El WACC no es una opinión sobre la calidad de Hermès: es una suma de precios de mercado",
         "Refrescado con el bono alemán de hoy (+15pb desde 26-ago); apenas se mueve. Hermès, en sus cuentas auditadas, sigue descontándose más alto.",
         "Rf 3,35% (Bund, 04-sep-2026) + beta 1,1271 (la menor de dos, 26-ago) x ERP 4,28% + prima país\n"
         "0,77% (INFERENCIA). Cruce: URD2025 — «WACC 9,16% en 2025, frente a 8,60% en 2024» (HECHO).", fig)
    save(fig, "g3_wacc")


# ─────────────────────────────────────────────────────────────────────────────
def g4_banda_valor():
    """Tres escenarios explícitos, un mismo veredicto: el precio de hoy está fuera de la banda incluso en el alcista."""
    fig, ax = plt.subplots(figsize=(9.6, 4.5))
    fig.subplots_adjust(top=0.70, bottom=0.15, left=0.24, right=0.965)
    et = ["BAJISTA\ncapacidad sin precio,\nAsia se enfría más", "BASE\nsenda de capex guiada\npor la propia Hermès",
          "ALCISTA\ncapacidad + precio +\nrecuperación de Asia"]
    vv = [817, 1010, 1162]
    cc = [P["rojo_oscuro"], P["azul"], P["verde"]]
    y = np.arange(3)[::-1]
    ax.barh(y, vv, 0.5, color=cc)
    for i, v in enumerate(vv):
        ax.text(v + 20, y[i], f"{v:,.0f}".replace(",", ".") + " EUR", va="center",
                fontsize=10.5, fontweight="bold", color=P["tinta"], zorder=6)
    ax.axvline(PRECIO_EUR, color=P["tinta"], lw=2.2, zorder=2)
    ax.text(PRECIO_EUR + 22, 2.55, "PRECIO HOY\n1.459 EUR", fontsize=9.4,
            fontweight="bold", color=P["tinta"], va="top")
    ax.set_yticks(y); ax.set_yticklabels(et, fontsize=8.6)
    ax.set_xlabel("Valor por acción (EUR, RMS.PA) — DCF a 10 años, WACC 8,94%"); ax.set_xlim(0, 1720)
    ax.set_ylim(-0.55, 2.85)
    deco(ax, "El precio de hoy está por encima del escenario ALCISTA — que ya asume que todo sale bien",
         "Los tres comparten el mismo WACC de mercado y la propia guía de capex 2026 de Hermès; solo cambian crecimiento, margen y ritmo de inversión.",
         "DCF explícito a 10 años, owner earnings, WACC 8,94% (INFERENCIA sobre HECHOs auditados y\n"
         "guía de capex propia de Hermès, H1 2026). Precio: IBKR, 04-sep-2026 (HECHO).", fig)
    save(fig, "g4_banda_valor")


# ─────────────────────────────────────────────────────────────────────────────
def g5_ruido():
    """El candado C: la báscula que se inclina con el WACC — recalculada sobre el escenario base."""
    fig, ax = plt.subplots(figsize=(9.6, 4.9))
    fig.subplots_adjust(top=0.70, bottom=0.14, left=0.275, right=0.965)
    et = ["WACC +2pp\n(10,94%)", "CASO BASE\n(8,94%)", "WACC −2pp\n(6,94%,\nimplausible — ver texto)"]
    vv = [764, 1010, 1545]
    y = np.arange(3)[::-1] * 1.35
    cc = [P["rojo_oscuro"], P["azul"], P["verde"]]
    ax.barh(y, vv, 0.62, color=cc)
    extra = ["sigue cara", "", "cruzaría a barata — exige una beta\npor debajo de 0,65 (ya descartada)"]
    ecol = [P["rojo_oscuro"], P["tinta"], P["verde"]]
    for i, v in enumerate(vv):
        txt = f"{v:,.0f}".replace(",", ".") + " EUR"
        ax.text(v + 20, y[i] + 0.16, txt, va="center", fontsize=9.6, fontweight="bold", color=P["tinta"])
        if extra[i]:
            ax.text(v + 20, y[i] - 0.24, extra[i], va="center", fontsize=7.6,
                    style="italic", fontweight="bold", color=ecol[i])
    ax.axvline(PRECIO_EUR, color=P["tinta"], lw=2.1)
    ax.text(PRECIO_EUR + 20, y[0] + 0.65, "PRECIO HOY\n1.459 EUR", fontsize=8.8,
            fontweight="bold", color=P["tinta"], va="top")
    ax.set_yticks(y); ax.set_yticklabels(et, fontsize=8.6)
    ax.set_xlabel("Valor por acción, equivalente en EUR — escenario BASE"); ax.set_xlim(0, 2450)
    ax.set_ylim(y[-1] - 0.85, y[0] + 1.05)
    deco(ax, "Mover el WACC dos puntos SÍ cambiaría el veredicto — pero la esquina que lo cambia exige una beta descartada",
         "Una beta de 0,65 solo aparece en una fuente sin índice de referencia declarado (R² de 0,08) — se descartó ya en el expediente original por incompatibilidad de benchmark.",
         "DCF propio recalculado, escenario base, 04-sep-2026 (INFERENCIA sobre HECHOs auditados).\n"
         "Beta descartada: análisis previo (27-jul-2026), disputa: sesión abogado-diablo (03-sep-2026).", fig)
    save(fig, "g5_ruido")


# ─────────────────────────────────────────────────────────────────────────────
def g6_moat():
    """Las cuatro capas del foso, de la más rápida de imitar a la más lenta."""
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    fig.subplots_adjust(top=0.72, bottom=0.16, left=0.27, right=0.965)
    capas = ["Pricing power\n(subir precio)", "Integración vertical\n(curtiembres propias)",
             "Escasez deliberada\n(listas de espera)", "Saber-hacer artesanal\n(formar un artesano)"]
    lo = [0, 2, 5, 8]
    hi = [2, 6, 10, 18]
    col = [P["ocre"], P["azul_cielo"], P["azul_acero"], P["azul"]]
    y = np.arange(4)[::-1]
    ax.barh(y, [h - l for h, l in zip(hi, lo)], 0.5, left=lo, color=col)
    for i, (l, h) in enumerate(zip(lo, hi)):
        ax.text(h + 0.3, y[i], f"{l}-{h} años", va="center", fontsize=9.2,
                fontweight="bold", color=P["tinta"])
    ax.text(0.15, -0.65, "la capa de abajo es la que ningún rival con capital ha logrado replicar en 189 años",
            fontsize=8.0, style="italic", fontweight="bold", color=P["azul"], ha="left", va="center")
    ax.set_yticks(y); ax.set_yticklabels(capas, fontsize=8.6)
    ax.set_xlabel("Años que tardaría un rival bien financiado en igualar esa capa (estimación)")
    ax.set_xlim(0, 21); ax.set_xticks([0, 5, 10, 15, 20])
    ax.set_ylim(-0.85, 3.6)
    deco(ax, "Cualquiera puede copiar el precio. Nadie ha copiado al artesano",
         "Subir el precio es cosa de una tarde. Formar a alguien capaz de coser un Birkin de principio a fin toma años.",
         "Capas: URD2025 y PR_FY2025 (HECHO). Los años de defensa: ESTIMACIÓN propia\n"
         "(SUPUESTO explícito, no cifra de ningún filing).", fig)
    save(fig, "g6_moat")


# ─────────────────────────────────────────────────────────────────────────────
def g7_premortem():
    """Cuatro relojes con fecha — el más próximo, dentro de seis semanas."""
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    fig.subplots_adjust(top=0.72, bottom=0.17, left=0.24, right=0.975)
    mec = ["1 · Fractura del\npacto H51",
           "2 · Relajación de\nla escasez",
           "3 · Desaceleración\nde China/Asia",
           "4 · Riesgo\nreputacional (pieles)"]
    ini = [2026.68, 2026.68, 2026.68, 2026.68]
    fin = [2031.0, 2028.5, 2027.3, 2028.5]
    col = [P["rojo"], P["terracota"], P["ocre"], P["vino"]]
    y = np.arange(4)[::-1]
    ax.barh(y, [f - i for f, i in zip(fin, ini)], 0.44, left=ini, color=col, alpha=0.92)
    marcas = ["vence 2031",
              "vigilancia continua:\nlead times",
              "ventas 3T-2026\n(~oct-2026)",
              "vigilancia continua:\nescalada a boicot"]
    for i, (f, t) in enumerate(zip(fin, marcas)):
        ax.text(f + 0.06, y[i], t, va="center", fontsize=7.5, style="italic", color=P["gris"])
    ax.axvline(2026.67, color=P["tinta"], lw=1.8)
    ax.text(2026.72, 3.95, "HOY · 03-sep-2026", fontsize=8.4, fontweight="bold",
            color=P["tinta"], ha="left", va="top")
    ax.axvline(2026.79, color=P["rojo"], ls="--", lw=1.3)
    ax.text(2026.85, -0.72, "primer chequeo: ventas 3T-2026, ~medio octubre 2026",
            fontsize=8.0, style="italic", fontweight="bold", color=P["rojo"], ha="left")
    ax.set_yticks(y); ax.set_yticklabels(mec, fontsize=8.2)
    ax.set_xlim(2026.3, 2032.1)
    ax.set_xticks([2027, 2028, 2029, 2030, 2031])
    ax.set_ylim(-1.0, 4.35)
    deco(ax, "Cuatro formas de que esto salga mal — cada una con fecha en el calendario",
         "El más lejano (2031) es también el más citado por el abogado del diablo como el que menos se está vigilando hoy.",
         "Pacto H51: URD2025 (HECHO su existencia; INFERENCIA de prensa la disputa Puech).\n"
         "Ventas 3T-2026: calendario histórico de Hermès (INFERENCIA). Pre-mortem: 03-sep-2026.", fig)
    save(fig, "g7_premortem")


# ─────────────────────────────────────────────────────────────────────────────
def g8_crecimiento():
    """Ni siquiera el escenario alcista bate el coste de capital."""
    fig, ax = plt.subplots(figsize=(9.6, 4.5))
    fig.subplots_adjust(top=0.72, bottom=0.16, left=0.10, right=0.97)
    lab = ["Bono alemán\na 10 años\n(sin riesgo)", "TIR · escenario\nBAJISTA", "TIR · escenario\nBASE",
           "TIR · escenario\nALCISTA", "Coste de capital\n(WACC, el listón)"]
    val = [3.35, 6.10, 7.16, 7.88, 8.94]
    col = [P["gris_medio"], P["rojo_oscuro"], P["azul"], P["verde"], P["azul_noche"]]
    x = np.arange(5)
    b = ax.bar(x, val, 0.55, color=col)
    for r, v in zip(b, val):
        ax.text(r.get_x()+r.get_width()/2, v+0.18, f"{v:.2f}".replace(".", ",")+"%",
                ha="center", fontsize=10, fontweight="bold", color=P["tinta"])
    ax.axhline(8.94, color=P["azul_noche"], ls="--", lw=1.2, alpha=0.6)
    ax.set_xticks(x); ax.set_xticklabels(lab, fontsize=8.2)
    ax.set_ylabel("Rendimiento anual a 10 años (%)"); ax.set_ylim(0, 10.6)
    deco(ax, "Comprando hoy, ni siquiera el escenario alcista paga el listón que el propio mercado exige",
         "Los tres escenarios rinden por debajo del coste de capital — y el bajista apenas 2,75 puntos por encima de un bono soberano sin riesgo.",
         "TIR: tasa que iguala el DCF propio (3 escenarios) al precio de hoy, 1.459 EUR (04-sep-2026).\n"
         "WACC y Bund: ver gráfico anterior. Todo INFERENCIA sobre HECHOs auditados.", fig)
    save(fig, "g8_crecimiento")


if __name__ == "__main__":
    for f in (g1_margen, g2_metiers, g3_wacc, g4_banda_valor, g5_ruido,
              g6_moat, g7_premortem, g8_crecimiento):
        f(); print("ok:", f.__name__)
