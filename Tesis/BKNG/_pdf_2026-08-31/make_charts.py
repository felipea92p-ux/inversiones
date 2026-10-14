# -*- coding: utf-8 -*-
"""Gráficos · ULTRA TESIS BOOKING HOLDINGS (BKNG) · 31-ago-2026.
Fuentes: 10-K FY2025 (accn 0001075531-26-000009), 10-Q 2T-2026 (accn 0001075531-26-000037),
8-K split 25:1 (accn 0001075531-26-000008), Damodaran ene-2026, Treasury.gov, IBKR.

RECORDATORIO DE PITFALLS (ver chart_style.py):
  · NUNCA dos '$' en un título/subtítulo/fuente -> escribir "USD".
  · Fondo crema siempre (rcParams), dpi=150.
"""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save
from paleta_qg import PALETA as P

PRECIO = 200.33


# ─────────────────────────────────────────────────────────────────────────────
def g1_lineas():
    """Las tres formas de cobrar de Booking — no una."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.8, 4.4),
                                 gridspec_kw={"width_ratios": [1.35, 1.0]})
    fig.subplots_adjust(top=0.70, bottom=0.17, left=0.155, right=0.975, wspace=0.30)

    lab = ["Merchant\n(procesa el pago)", "Agency\n(comisión pura)", "Publicidad\ny otros"]
    val = [17755, 7968, 1194]
    pct = [66.0, 29.6, 4.4]
    col = [P["azul"], P["azul_acero"], P["ocre"]]
    y = np.arange(3)[::-1]
    a1.barh(y, val, 0.58, color=col)
    for i, (v, q) in enumerate(zip(val, pct)):
        miles = f"{v:,.0f}".replace(",", ".")
        porc = f"{q:.1f}".replace(".", ",")
        a1.text(v + 380, y[i], f"{miles} M  ({porc}%)",
                va="center", fontsize=9.2, fontweight="bold", color=P["tinta"])
    a1.set_yticks(y); a1.set_yticklabels(lab, fontsize=8.8)
    a1.set_xlabel("Ingresos FY2025 (millones de USD)")
    a1.set_xlim(0, 25500)

    # Panel derecho: concentración por vertical
    ver = ["Alojamiento", "Resto\n(vuelos, coches,\nrestaurantes, ads)"]
    vv = [89.0, 11.0]
    b = a2.bar(ver, vv, 0.52, color=[P["rojo"], P["gris_medio"]])
    for r, v in zip(b, vv):
        a2.text(r.get_x() + r.get_width() / 2, v + 2.2, f"{v:.0f}%",
                ha="center", fontsize=12.5, fontweight="bold", color=P["tinta"])
    a2.set_ylabel("Peso en el ingreso total (%)"); a2.set_ylim(0, 105)
    a2.set_xticks(range(2)); a2.set_xticklabels(ver, fontsize=8.4)
    a2.set_title("Y todo depende de un solo vertical", fontsize=9.4,
                 color=P["tinta"], pad=8)

    deco([a1, a2], "Booking no cobra una comisión: cobra de tres maneras distintas",
         "Dos de cada tres dólares vienen de procesar el pago, no de presentar al hotel con el viajero.",
         "Fuente: 10-K FY2025, Nota 3 «Revenues» y Nota 17 «Segment Reporting» (HECHO). Total 26.917 M USD.", fig)
    save(fig, "g1_lineas")


# ─────────────────────────────────────────────────────────────────────────────
def g2_acciones():
    """La máquina de recomprar: menos dueños cada año."""
    fig, ax = plt.subplots(figsize=(9.6, 4.3))
    fig.subplots_adjust(top=0.72, bottom=0.17, left=0.10, right=0.97)
    lab = ["2016\n(equivalente post-split)", "2022\n(equivalente post-split)",
           "julio de 2026\n(recuento real)"]
    val = [1240.0, 963.3, 751.38]
    col = [P["azul_cielo"], P["azul_acero"], P["azul"]]
    b = ax.bar(lab, val, 0.5, color=col)
    for r, v in zip(b, val):
        ax.text(r.get_x() + r.get_width() / 2, v + 26, f"{v:,.0f} M".replace(",", "."),
                ha="center", fontsize=11.5, fontweight="bold", color=P["tinta"])
    ax.annotate("", xy=(1.72, 800), xytext=(0.30, 1195),
                arrowprops=dict(arrowstyle="->", color=P["rojo"], lw=1.5,
                                connectionstyle="arc3,rad=0.12"))
    ax.text(1.0, 1330, "−4,4% al año durante una década  ·  −22% sólo desde 2022",
            fontsize=9.4, style="italic", fontweight="bold", color=P["rojo"], ha="center")
    ax.set_ylabel("Acciones en circulación (millones)")
    ax.set_ylim(0, 1480)
    deco(ax, "Cada año quedan menos dueños repartiéndose el mismo negocio",
         "Booking devolvió más del 100% de su caja libre al accionista desde 2022. El pastel no crece: se reparte entre menos.",
         "Fuente: portada del 10-Q 2T-2026 (751.380.500 acciones al 27-jul-2026) y serie histórica ajustada "
         "al split 25:1 del 6-abr-2026.\n(HECHO el dato de 2026; INFERENCIA la equivalencia histórica de 2016 y 2022.)", fig)
    save(fig, "g2_acciones")


# ─────────────────────────────────────────────────────────────────────────────
def g3_wacc():
    """De dónde sale el 9,53% — ladrillo a ladrillo."""
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.8, 4.5),
                                 gridspec_kw={"width_ratios": [1.3, 1.0]})
    fig.subplots_adjust(top=0.71, bottom=0.20, left=0.075, right=0.97, wspace=0.30)

    # Panel 1: construcción del coste de los fondos propios (Ke)
    lab = ["Bono del\nTesoro a 10a", "+ Riesgo de\nla bolsa\n(beta x prima)",
           "+ Riesgo de\nlos países\ndonde vende", "= Coste de\nlos fondos\npropios"]
    base = [0, 4.72, 8.59, 0]
    alt = [4.72, 3.87, 1.67, 10.26]
    col = [P["azul_acero"], P["azul"], P["terracota"], P["azul_noche"]]
    x = np.arange(4)
    a1.bar(x, alt, 0.56, bottom=base, color=col)
    for i, (b0, h) in enumerate(zip(base, alt)):
        a1.text(i, b0 + h + 0.22, f"{h:.2f}".replace(".", ",") + "%", ha="center",
                fontsize=9.4, fontweight="bold", color=P["tinta"])
    a1.set_xticks(x); a1.set_xticklabels(lab, fontsize=7.8)
    a1.set_ylabel("Rentabilidad exigida (%)"); a1.set_ylim(0, 12.4)

    # Panel 2: mezcla con la deuda
    a2.bar(["Fondos propios\n88,2% del capital", "Deuda\n11,8% del capital"],
           [10.26, 4.03], 0.5, color=[P["azul_noche"], P["verde"]])
    a2.text(0, 10.55, "10,26%", ha="center", fontsize=10.5, fontweight="bold")
    a2.text(1, 4.32, "4,03%", ha="center", fontsize=10.5, fontweight="bold")
    a2.axhline(9.53, color=P["rojo"], ls="--", lw=1.5)
    a2.set_xlim(-0.62, 1.62)
    a2.text(1.58, 9.88, "WACC = 9,53%", fontsize=10.2, fontweight="bold",
            color=P["rojo"], ha="right")
    a2.set_ylabel("Coste (%)"); a2.set_ylim(0, 12.4)
    a2.set_title("Mezclados según cuánto pesa cada uno", fontsize=9.2,
                 color=P["tinta"], pad=8)

    deco([a1, a2], "El 9,53% no es una opinión: es una suma de cuatro precios de mercado",
         "Ninguno de los cuatro ladrillos viene del «tier de calidad» de la empresa. Todos vienen de fuera.",
         "Rf: Treasury.gov (4,72-4,75%). Beta 0,916 (la menor de dos métodos) x prima de mercado 4,23% "
         "(Damodaran, ene-2026). Prima de país ponderada por ingresos: 1,67%.\n"
         "Kd tras impuestos 4,03% (emisión de mayo-2026). Cálculo propio, INFERENCIA sobre HECHOs.", fig)
    save(fig, "g3_wacc")


# ─────────────────────────────────────────────────────────────────────────────
def g4_banda():
    """La banda de valor: cinco modelos honestos, un precio dentro."""
    fig, ax = plt.subplots(figsize=(9.6, 4.7))
    fig.subplots_adjust(top=0.71, bottom=0.14, left=0.235, right=0.965)
    et = ["Abogado del diablo\n(WACC 11,06%)",
          "Bajista del modelo\n(WACC 11,03%, g0 3%)",
          "CASO BASE\n(WACC 9,53%, g0 6,3%)",
          "Abogado del ángel\n(base sin peso COVID)",
          "Alcista\n(WACC 8,53%, g0 8%)"]
    vv = [104.78, 118.77, 193.55, 228.78, 305.19]
    cc = [P["rojo_oscuro"], P["vino"], P["azul"], P["azul_acero"], P["verde"]]
    y = np.arange(5)[::-1]
    ax.barh(y, vv, 0.52, color=cc)
    for i, v in enumerate(vv):
        ax.text(v + 5, y[i], f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " USD",
                va="center", fontsize=9.6, fontweight="bold", color=P["tinta"])
    ax.axvline(PRECIO, color=P["tinta"], lw=2.1)
    ax.text(PRECIO + 5, 5.00, "PRECIO HOY\n200,33 USD", fontsize=9.0,
            fontweight="bold", color=P["tinta"], va="top")
    ax.set_yticks(y); ax.set_yticklabels(et, fontsize=8.2)
    ax.set_xlabel("Valor por acción (USD)"); ax.set_xlim(0, 395)
    ax.set_ylim(-0.6, 5.05)
    deco(ax, "El precio de hoy cae justo en medio del rango de lo defendible",
         "Cuando el precio está dentro de la banda y no fuera, el modelo no está diciendo «compra» ni «vende»: está diciendo «no lo sé».",
         "Modelo propio de flujos descontados, cinco escenarios, todos construidos sobre el 10-K FY2025 "
         "(INFERENCIA sobre HECHOs).\nPrecio en vivo de Interactive Brokers, 31-ago-2026 (HECHO).", fig)
    save(fig, "g4_banda")


# ─────────────────────────────────────────────────────────────────────────────
def g5_sensibilidad():
    """El candado C: la báscula que se inclina con el dedo gordo del pie."""
    fig, ax = plt.subplots(figsize=(9.6, 4.7))
    fig.subplots_adjust(top=0.71, bottom=0.15, left=0.275, right=0.965)
    et = ["WACC 11,53%\n(crecimiento base)",
          "Crecimiento −2 puntos\n(WACC fijo 9,53%)",
          "CASO BASE",
          "Crecimiento +2 puntos\n(WACC fijo 9,53%)",
          "WACC 7,53%\n(crecimiento base)"]
    vv = [138.55, 184.00, 193.55, 203.42, 316.63]
    y = np.arange(5)[::-1]
    cc = [P["rojo_oscuro"], P["rojo"], P["azul"], P["verde"], P["azul_acero"]]
    ax.barh(y, vv, 0.5, color=cc)
    extra = ["", "   ← aquí está CARO", "", "   ← y aquí está BARATO", ""]
    ecol = [P["tinta"], P["rojo"], P["tinta"], P["verde"], P["tinta"]]
    for i, v in enumerate(vv):
        txt = f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " USD"
        ax.text(v + 6, y[i], txt, va="center", fontsize=9.6, fontweight="bold",
                color=P["tinta"])
        if extra[i]:
            ax.text(v + 72, y[i], extra[i], va="center", fontsize=8.6,
                    style="italic", fontweight="bold", color=ecol[i])
    ax.axvline(PRECIO, color=P["tinta"], lw=2.1)
    ax.text(PRECIO + 6, 5.02, "PRECIO HOY 200,33 USD", fontsize=8.8,
            fontweight="bold", color=P["tinta"], va="top")
    ax.set_yticks(y); ax.set_yticklabels(et, fontsize=8.2)
    ax.set_xlabel("Valor por acción (USD)"); ax.set_xlim(0, 420)
    ax.set_ylim(-0.6, 5.10)
    deco(ax, "Mover el crecimiento dos puntos cambia el veredicto de caro a barato",
         "El mismo modelo, el mismo día, la misma empresa: de 138 a 317 USD. Ratio 2,29x. Eso no es una valoración: es una báscula sin calibrar.",
         "Matriz de sensibilidad propia (candado C, piso de resolución del método de 12 pasos).\n"
         "Crecimiento sensibilizado en los años 3-5. INFERENCIA sobre datos del 10-K FY2025.", fig)
    save(fig, "g5_sensibilidad")


# ─────────────────────────────────────────────────────────────────────────────
def g6_marketing():
    """El gasto de marketing: cada vez menos euros por el mismo resultado."""
    fig, ax = plt.subplots(figsize=(9.6, 4.5))
    fig.subplots_adjust(top=0.72, bottom=0.14, left=0.085, right=0.975)
    yr = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
    ocf = [32.3, 1.3, 25.7, 38.3, 34.4, 35.1, 35.0]
    ax.plot(yr, ocf, color=P["azul"], lw=2.3, marker="o", ms=5.5,
            label="Caja que deja el negocio (OCF / ingresos)")
    ymk = [2019, 2021, 2023, 2025]
    mkt = [33.0, 34.7, 31.7, 30.4]
    ax.plot(ymk, mkt, color=P["rojo"], lw=2.3, marker="s", ms=5.5, ls="--",
            label="Lo que cuesta comprar el tráfico (marketing / ingresos)")
    dy = [2.0, 2.0, -3.4, -3.4]
    for x, v, d in zip(ymk, mkt, dy):
        ax.text(x, v + d, f"{v:.1f}%".replace(".", ","), ha="center",
                fontsize=9.0, fontweight="bold", color=P["rojo"])
    ax.text(2020.22, 1.8, "2020: el mundo dejó de viajar", fontsize=8.2, style="italic",
            color=P["gris"], ha="left", va="center")
    ax.axhline(33.0, color=P["gris_medio"], ls=":", lw=1.0)
    ax.text(2019.02, 40.4, "umbral de alarma del pre-mortem: 33% de los ingresos en marketing",
            fontsize=7.6, style="italic", color=P["gris"], ha="left")
    ax.set_ylabel("Porcentaje sobre ingresos (%)"); ax.set_ylim(0, 46)
    ax.set_xticks(yr)
    ax.legend(frameon=False, fontsize=8.2, loc="lower right")
    deco(ax, "El marketing es cada vez más barato, no más caro — de momento",
         "La intensidad bajó de 34,7% a 30,4% en cuatro años mientras la caja subía. Ésa es la prueba de que el motor todavía funciona.",
         "Fuente: 10-K de Booking Holdings, ejercicios 2019-2025 (HECHO para los márgenes; "
         "marketing/ingresos disponible en 2019, 2021, 2023 y 2025).", fig)
    save(fig, "g6_marketing")


# ─────────────────────────────────────────────────────────────────────────────
def g7_crecimiento():
    """El gate que mata la tesis: 5,0%."""
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    fig.subplots_adjust(top=0.72, bottom=0.20, left=0.085, right=0.975)
    lab = ["Noches de hotel\nreservadas\n2025 (real)",
           "Reservas brutas\n2025 (real)",
           "Guía de la propia\nempresa para 2026\n(«high single digit»)",
           "Lo que el modelo\nconservador supone\n(g0, TAM bloqueado)"]
    val = [8.0, 12.4, 8.0, 6.3]
    col = [P["azul"], P["azul_acero"], P["ocre"], P["verde"]]
    b = ax.bar(lab, val, 0.55, color=col)
    for r, v in zip(b, val):
        ax.text(r.get_x() + r.get_width() / 2, v + 0.35, f"{v:.1f}%".replace(".", ","),
                ha="center", fontsize=11.5, fontweight="bold", color=P["tinta"])
    ax.axhline(5.0, color=P["rojo"], ls="--", lw=1.6)
    ax.annotate("", xy=(0.50, 5.18), xytext=(0.50, 14.75),
                arrowprops=dict(arrowstyle="->", color=P["rojo"], lw=1.1))
    ax.text(0.50, 15.15, "5,0% — por debajo de esta línea, la tesis muere",
            fontsize=8.8, style="italic", fontweight="bold", color=P["rojo"],
            ha="center", va="bottom")
    ax.set_ylabel("Crecimiento interanual (%)"); ax.set_ylim(0, 17.0)
    deco(ax, "El número que hay que mirar en noviembre",
         "Hoy hay holgura de tres puntos sobre el umbral de muerte. El 10-Q del tercer trimestre dirá si sigue habiéndola.",
         "Datos de 2025: 10-K FY2025, MD&A «Key Business Metrics» (HECHO).\n"
         "Guía 2026: comentarios de la dirección vía prensa financiera (INFERENCIA, no verificada contra "
         "transcript íntegro). g0 = supuesto propio del modelo.", fig)
    save(fig, "g7_crecimiento")


# ─────────────────────────────────────────────────────────────────────────────
def g8_moat():
    """Las cinco capas del foso, de la más frágil a la más dura."""
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    fig.subplots_adjust(top=0.72, bottom=0.16, left=0.245, right=0.965)
    capas = ["Marca y confianza\ndel viajero",
             "Densidad de inventario\n(4,4 M propiedades)",
             "Efecto de red\n(cíclico, no monótono)",
             "Datos de conversión\ny algoritmos",
             "Costes de cambio\ndel lado hotelero"]
    lo = [2, 5, 7, 8, 10]
    hi = [4, 7, 10, 12, 15]
    col = [P["terracota"], P["ocre"], P["azul_cielo"], P["azul_acero"], P["azul"]]
    y = np.arange(5)[::-1]
    ax.barh(y, [h - l for h, l in zip(hi, lo)], 0.55, left=lo, color=col)
    for i, (l, h) in enumerate(zip(lo, hi)):
        ax.text(h + 0.28, y[i], f"{l}-{h} años", va="center", fontsize=9.2,
                fontweight="bold", color=P["tinta"])
    ax.text(0.15, -0.62, "la capa de abajo es la que de verdad ha sostenido el negocio "
            "durante quince años", fontsize=8.2, style="italic", fontweight="bold",
            color=P["azul"], ha="left", va="center")
    ax.set_yticks(y); ax.set_yticklabels(capas, fontsize=8.4)
    ax.set_xlabel("Años que tardaría un rival bien financiado en erosionar esa capa")
    ax.set_xlim(0, 19); ax.set_xticks([0, 5, 10, 15])
    ax.set_ylim(-0.85, 4.6)
    deco(ax, "El foso no es la marca: es lo que le cuesta al hotel marcharse",
         "Un competidor puede comprar visibilidad en dos años. Lo que no puede comprar es que 4,4 millones de propiedades cambien de sistema.",
         "Capas y evidencia: 10-K FY2025, Item 1 (HECHO). Los años de defensa son estimación propia, "
         "no cifra de ningún filing (SUPUESTO explícito).", fig)
    save(fig, "g8_moat")


# ─────────────────────────────────────────────────────────────────────────────
def g9_premortem():
    """Cuatro relojes con fecha."""
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    fig.subplots_adjust(top=0.72, bottom=0.17, left=0.195, right=0.975)
    mec = ["1 · Desintermediación\ndel canal",
           "2 · Inflación del coste\nde captar cliente",
           "3 · El patrimonio negativo\nse vuelve frágil",
           "4 · El litigio de la FTC\nescala"]
    ini = [2026.85, 2026.85, 2026.85, 2026.85]
    fin = [2029.15, 2028.15, 2029.60, 2028.15]
    col = [P["rojo"], P["terracota"], P["ocre"], P["vino"]]
    y = np.arange(4)[::-1]
    ax.barh(y, [f - i for f, i in zip(fin, ini)], 0.44, left=ini, color=col, alpha=0.92)
    marcas = ["punto duro:\n10-K FY2028 (feb-2029)", "punto duro:\n10-K FY2027 (feb-2028)",
              "vigilancia continua\ncada 10-Q y 10-K", "punto duro:\n10-K FY2027 (feb-2028)"]
    for i, (f, t) in enumerate(zip(fin, marcas)):
        ax.text(f + 0.06, y[i], t, va="center", fontsize=7.6, style="italic", color=P["gris"])
    ax.axvline(2026.83, color=P["tinta"], lw=1.8)
    ax.text(2026.90, 3.96, "HOY · 31-ago-2026", fontsize=8.6, fontweight="bold",
            color=P["tinta"], ha="left", va="top")
    ax.axvline(2026.85, color=P["rojo"], ls="--", lw=1.3)
    ax.text(2027.02, -0.72, "primer chequeo de los cuatro: 10-Q del 3T-2026 (~nov-2026)",
            fontsize=8.2, style="italic", fontweight="bold", color=P["rojo"], ha="left")
    ax.set_yticks(y); ax.set_yticklabels(mec, fontsize=8.2)
    ax.set_xlim(2026.1, 2030.5)
    ax.set_xticks([2027, 2028, 2029, 2030])
    ax.set_xticklabels(["2027", "2028", "2029", "2030"])
    ax.set_ylim(-1.0, 4.35)
    deco(ax, "Cuatro formas de que esto salga mal — cada una con fecha en el calendario",
         "Un pre-mortem sin fecha es una preocupación. Con fecha y umbral, es un instrumento.",
         "Umbrales y fechas construidos sobre el 10-K FY2025 y el 10-Q 2T-2026 (INFERENCIA sobre HECHOs). "
         "Registrados en gates.md como Gates 1 a 4.", fig)
    save(fig, "g9_premortem")


if __name__ == "__main__":
    for f in (g1_lineas, g2_acciones, g3_wacc, g4_banda, g5_sensibilidad,
              g6_marketing, g7_crecimiento, g8_moat, g9_premortem):
        f(); print("ok:", f.__name__)
