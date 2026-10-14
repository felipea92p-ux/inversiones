# -*- coding: utf-8 -*-
"""Gráficos NUEVOS de la actualización 2026-09-08 (cross-validación independiente,
corrección de beta vía Hamada, segundo abogado del diablo, verificación de precio
en vivo). Todas las cifras citadas literalmente de la sección "Actualización
2026-09-08" del monólogo evidenciado fuente. Ninguna cifra se inventa aquí —
donde se hace una extensión aritmética simple sobre HECHOs ya declarados
(p.ej. recalcular el descuento al precio en vivo en vez del preliminar), se
marca explícitamente como INFERENCIA en el propio gráfico."""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save, P

# ── 07 · Tres metodologías de beta, tres vetos casi opuestos ────────────
def c07():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.9))

    metodos = ["Hamada\n(n=2 pares líquidos)", "Beta bruto\nsin ajustar", "Sectorial Damodaran\nre-apalancado"]
    betas = [0.52, 0.89, 1.30]
    cols = [P["verde"], P["ocre"], P["rojo_oscuro"]]
    y = np.arange(3)[::-1]
    a1.barh(y, betas, color=cols, height=.55)
    for i, v in zip(y, betas):
        a1.text(v + .04, i, f"β={v:.2f}".replace(".", ","), va="center", fontsize=10.5,
                fontweight="bold", color=cols[list(y).index(i)])
    a1.axvline(0.695, color=P["azul"], lw=1.6, ls=":")
    a1.set_ylim(-0.62, 2.85)
    a1.annotate("beta original\n(0,69-0,79 Blume, 4-sep)", xy=(0.695, 2.55), xytext=(1.02, 2.72),
                fontsize=7.3, color=P["azul"], fontweight="bold", ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=P["azul"], lw=1.1))
    a1.set_yticks(y); a1.set_yticklabels(metodos, fontsize=8.8)
    a1.set_xlim(0, 1.55); a1.set_xlabel("beta re-apalancado a la estructura de CSU")
    a1.set_title("El beta corregido por apalancamiento\nsalió MÁS BAJO, no más alto", fontsize=9.6,
                 fontweight="bold", color=P["azul_noche"], pad=8)

    wacc = [6.87, 8.38, 10.05]
    etiquetas = ["6,87%\nCRUZA el gatillo\n(descuento -44,48%)", "8,38%\ndescuento -23,4%\n(no llega al 30%)",
                 "10,05%\nprecio > valor\nintrínseco (CARA)"]
    a2.bar(range(3), wacc, color=cols, width=.55)
    for i, (v, lab) in enumerate(zip(wacc, etiquetas)):
        a2.text(i, v + .55, lab, ha="center", fontsize=7.7, fontweight="bold", color=cols[i])
    a2.set_xticks(range(3)); a2.set_xticklabels(metodos, fontsize=8.2)
    a2.set_ylim(0, 14.3); a2.set_ylabel("WACC resultante (%)")
    a2.set_title("El mismo negocio, tres veredictos\nsegún qué muestra de beta se elija", fontsize=9.6,
                 fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=.72, bottom=.16, wspace=.32, left=.13, right=.97)
    deco([a1, a2], "De tres metodologías igual de legítimas, la elegida (n=2) es la única que da COMPRAR",
         "Hamada: Roper (β=0,75) y OpenText (β=1,03) desapalancados y re-apalancados a la estructura de CSU (D/E neto ~3,6% vs ROP 61% / OTEX 149%).",
         "Fuente: Actualización 2026-09-08 del monólogo evidenciado CSU.TO — segundo abogado del diablo, sesión limpia (8-sep-2026).", fig)
    save(fig, "07_tres_metodologias_beta")


# ── 08 · Verificación de precio en vivo: el descuento es real, y mayor ──
def c08():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.6), gridspec_kw={"width_ratios": [1, 1.3]})

    cad_lab = ["Precio usado en\nel modelo\n(dato de días atrás)", "Precio real IBKR\n8-sep-2026 en vivo"]
    cad_val = [3070.03, 2853.79]
    cols_cad = [P["gris_medio"], P["azul"]]
    a1.bar(range(2), cad_val, color=cols_cad, width=.5)
    for i, v in enumerate(cad_val):
        a1.text(i, v + 25, f"C${v:,.2f}".replace(",", "."), ha="center", fontsize=9.5,
                fontweight="bold", color=cols_cad[i])
    a1.set_xticks(range(2)); a1.set_xticklabels(cad_lab, fontsize=8.0)
    a1.set_ylim(0, 3400); a1.set_ylabel("precio (C$)")
    a1.set_title("El dato estaba desactualizado,\nno mal convertido", fontsize=9.4, fontweight="bold",
                 color=P["azul_noche"], pad=8)

    usd_lab = ["Preliminar\n(US$2.214,71)", "Verificado en vivo\n8-sep (US$2.071,55)"]
    usd_val = [2214.71, 2071.55]
    cols_usd = [P["ocre"], P["verde"]]
    a2.bar(range(2), usd_val, color=cols_usd, width=.45)
    for i, v in enumerate(usd_val):
        a2.text(i, v + 45, f"US${v:,.2f}".replace(",", "."), ha="center", fontsize=9.5,
                fontweight="bold", color=cols_usd[i])
    a2.axhline(2791.94, color=P["rojo"], lw=2, ls="--")
    a2.text(1.35, 2875, "GATILLO Hamada: US$2.791,94", fontsize=8.2, color=P["rojo"],
            fontweight="bold", ha="right", va="bottom")
    a2.axhline(3988.48, color=P["azul_noche"], lw=1.4, ls=":")
    a2.text(1.35, 4040, "valor intrínseco Hamada: US$3.988,48", fontsize=7.6, color=P["azul_noche"],
            fontweight="bold", ha="right", va="bottom")
    a2.set_xticks(range(2)); a2.set_xticklabels(usd_lab, fontsize=8.4)
    a2.set_ylim(0, 4350); a2.set_ylabel("precio (US$, tipo de cambio 1,37755)")
    a2.set_title("Ambos precios ya cruzaban el gatillo —\nel verificado lo cruza por más margen", fontsize=9.2,
                 fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=.74, bottom=.14, wspace=.34, left=.09, right=.98)
    deco([a1, a2], "La sospecha de error de conversión CAD/USD queda descartada: el precio real es MÁS barato",
         "El segundo abogado del diablo pidió verificar el precio contra IBKR en vivo por sospecha de error — el resultado no resuelve el WACC, pero confirma que el descuento es real.",
         "Fuente: Actualización 2026-09-08 del monólogo evidenciado CSU.TO — verificación en vivo IBKR, 8-sep-2026, USD/CAD 1,37755.", fig)
    save(fig, "08_verificacion_precio")


for f in [c07, c08]:
    f(); print("ok", f.__name__)
