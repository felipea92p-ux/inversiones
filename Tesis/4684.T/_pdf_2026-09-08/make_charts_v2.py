# -*- coding: utf-8 -*-
"""Gráficos NUEVOS/REGENERADOS de la Ultra Tesis OBIC (4684.T) v2, 2026-09-08.
Sólo se regeneran los gráficos cuyo número clave cambió materialmente hoy
(precio vivo, beta corregido, WACC corregido, valor intrínseco, gatillo).
Los demás (02, 04, 05, 06, 07) se REUTILIZAN sin cambios desde _pdf_2026-09-04/.
Ningún número se inventa: cada cifra remite al monólogo fuente o a la
Actualización 2026-09-08 (cross-validación de cinco tesis)."""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save, P

PRECIO_VIVO_JPY = 4774   # 8-sep-2026, antes ¥5.082 el 4-sep
PRECIO_VIVO_USD = 30.01


# ── 01 · Rango de valor intrínseco vs. precio vivo (precio actualizado) ──
def c01():
    filas = [
        ("Crudo, beta 0,47\nsin escrutinar (WACC 5,3%)", 7700, 7800, P["rojo_oscuro"]),
        ("Alcista\n(WACC central, tramo alto)", 5844, 6200, P["verde"]),
        ("Central\n(WACC 7,0%-7,5%)", 4500, 4900, P["azul"]),
        ("Bajista, una variable\n(WACC 9,0%)", 3200, 3500, P["ocre"]),
        ("Bajista combinado\n(triple estrés, Paso 10)", 2500, 2900, P["vino"]),
    ]
    fig, ax = plt.subplots(figsize=(11.2, 5.2))
    ys = np.arange(len(filas))[::-1]
    for y, (lab, lo, hi, col) in zip(ys, filas):
        ax.barh(y, hi - lo, left=lo, height=0.42, color=col, zorder=3)
        ax.text(hi + 140, y, f"¥{lo:,.0f}-{hi:,.0f}".replace(",", "."),
                ha="left", va="center", fontsize=9.0, fontweight="bold", color=P["tinta"], zorder=6)
    ax.set_yticks(ys); ax.set_yticklabels([f[0] for f in filas], fontsize=8.4)
    ax.axvline(PRECIO_VIVO_JPY, color=P["tinta"], lw=2.2, zorder=2)
    ax.text(PRECIO_VIVO_JPY + 60, len(filas) - 0.35,
            f"PRECIO VIVO 8-sep\n¥{PRECIO_VIVO_JPY:,}".replace(",", "."),
            fontsize=8.8, fontweight="bold", color=P["tinta"])
    ax.axvline(5082, color=P["gris"], lw=1.1, ls=":", zorder=1)
    ax.text(5082 + 60, 0.15, "precio 4-sep: ¥5.082", fontsize=7.2, color=P["gris"], style="italic")
    ax.set_xlim(1800, 9300)
    ax.set_xlabel("yenes por acción")
    fig.subplots_adjust(top=0.72, bottom=0.12, left=0.27, right=0.97)
    deco(ax, "El precio ya cayó -6,1% desde el 4-sep — y ahora cae DENTRO del caso central",
         "¥4.774 (8-sep) frente a ¥4.500-4.900 de caso central: casi en línea, sin que el fundamento haya cambiado un ápice.",
         "Fuente: monólogo QG OBIC, Paso 9 y Paso 10 (Golpe 3); precio vivo actualizado 2026-09-08.", fig)
    save(fig, "01_valor_vs_precio")


# ── 03 · Sensibilidad del WACC (precio vivo actualizado) ────────────────
def c03():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.8))
    filas = [("5,3%\n(crudo, no usar)", 7700, 7800, P["rojo_oscuro"]),
             ("7,0%-7,5%\n(central)", 4500, 4900, P["azul"]),
             ("9,0%\n(conservador)", 3200, 3500, P["ocre"])]
    for i, (lab, lo, hi, col) in enumerate(filas):
        a1.bar(i, hi - lo, bottom=lo, color=col, width=0.42, zorder=3)
        a1.text(i, hi + 200, f"¥{lo:,.0f}-{hi:,.0f}".replace(",", "."),
                ha="center", va="bottom", fontsize=8.2, fontweight="bold", color=P["tinta"])
    a1.set_xticks(range(3)); a1.set_xticklabels([f[0] for f in filas], fontsize=8.2)
    a1.axhline(PRECIO_VIVO_JPY, color=P["tinta"], lw=1.8, ls="--")
    a1.text(2.05, PRECIO_VIVO_JPY - 320, f"precio vivo 8-sep\n¥{PRECIO_VIVO_JPY:,}".replace(",", "."),
            fontsize=7.8, color=P["tinta"])
    a1.set_ylim(2000, 8900)
    a1.set_ylabel("yenes por acción")
    a1.set_title("Valor por acción según el WACC\n(g terminal 2,0% fijo)", fontsize=9.2, fontweight="bold",
                  color=P["azul_noche"], pad=8)

    filas2 = [("Un solo estrés\n(WACC 9,0%, g 2,0%)", 3200, 3500, P["ocre"]),
              ("Triple estrés\n(+ margen 62-63% + g 1,0-1,5%)", 2500, 2900, P["vino"])]
    for i, (lab, lo, hi, col) in enumerate(filas2):
        a2.bar(i, hi - lo, bottom=lo, color=col, width=0.5)
        a2.text(i, (lo + hi) / 2, f"¥{lo:,.0f}-\n{hi:,.0f}".replace(",", "."),
                ha="center", va="center", fontsize=8.6, fontweight="bold", color="white")
    a2.set_xticks(range(2)); a2.set_xticklabels([f[0] for f in filas2], fontsize=8.0)
    a2.set_ylim(2000, 4000)
    a2.set_title("A WACC 9,0%: qué añade estresar\nmargen y crecimiento terminal", fontsize=9.2,
                  fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=0.72, bottom=0.13, wspace=0.30)
    deco([a1, a2], "El WACC decide más que cualquier dato del negocio — y el precio ya se movió, no el modelo",
         "Múltiplo terminal 1/(WACC-g): 14,3x cae a 12,9x al recortar g de 2,0% a 1,25% — sólo eso ya pesa ~-10% sobre el valor terminal.",
         "Fuente: monólogo QG OBIC, Paso 9 (WACC bottom-up) y Paso 10, Golpe 3a; precio vivo actualizado 2026-09-08.", fig)
    save(fig, "03_sensibilidad_wacc")


# ── 08 · NUEVO · La corrección de beta del 8-sep: patrón 5 de 5 ─────────
def c08():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.6))

    # Panel izquierdo: el patrón cruzado de 5 tesis (cualitativo, sin inventar cifras de las otras 4)
    nombres = ["CME", "OBIC", "TRI", "RELX", "CSU.TO"]
    y = np.arange(5)
    a1.barh(y, [1]*5, color=P["gris_claro"], height=0.55, zorder=2)
    a1.barh(1, 1, color=P["rojo"], height=0.55, zorder=3)  # OBIC destacado
    a1.set_yticks(y); a1.set_yticklabels(nombres, fontsize=9.4)
    a1.set_xticks([])
    a1.set_xlim(0, 1.35)
    for i in y:
        a1.text(1.04, i, "beta medido en ventana\nde calma sin catalizador", fontsize=7.3,
                va="center", color=P["gris"] if i != 1 else P["rojo"],
                fontweight="bold" if i == 1 else "normal")
    a1.invert_yaxis()
    a1.set_title("Mismo defecto, 5 de 5 empresas\n(hallazgo independiente, sin leer este documento)",
                 fontsize=9.0, fontweight="bold", color=P["azul_noche"], pad=8)

    # Panel derecho: beta crudo vs corregido, y WACC resultante, para OBIC
    cats = ["Beta crudo\n(0,47)", "Beta corregido\n(0,66, sector ERP Japón)"]
    betas = [0.47, 0.66]
    waccs = [6.20, 6.27]
    xw = np.arange(2)
    b = a2.bar(xw, betas, color=[P["rojo_oscuro"], P["azul"]], width=0.5, zorder=3)
    for i, (bt, wc) in enumerate(zip(betas, waccs)):
        a2.text(i, bt + 0.03, f"β = {bt:.2f}".replace(".", ","), ha="center", fontsize=9.4,
                fontweight="bold", color=P["tinta"])
        a2.text(i, bt / 2, f"WACC\n{wc:.2f}%".replace(".", ","), ha="center", va="center",
                fontsize=8.4, fontweight="bold", color="white")
    a2.set_xticks(xw); a2.set_xticklabels(cats, fontsize=8.4)
    a2.set_ylim(0, 0.85)
    a2.set_ylabel("beta (5 años)")
    a2.set_title("OBIC: corregir el beta apenas mueve el WACC\n(+7 puntos básicos, no invalida el rango)",
                 fontsize=9.0, fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=0.74, bottom=0.13, wspace=0.32)
    deco([a1, a2], "8-sep: el patrón “quality flight” se confirma en 5 de 5 tesis — y en OBIC casi no cambia nada",
         "OBIC subió +22% en dos meses sin catalizador; corregir el beta a la ventana sectorial larga (0,66) confirma el rango ya usado, no lo invalida.",
         "Fuente: Actualización 2026-09-08, cross-validación de 5 tesis (CME/OBIC/TRI/RELX/CSU.TO), ejecutada sin lectura previa de este documento.", fig)
    save(fig, "08_correccion_beta_8sep")


# ── 09 · NUEVO · El gatillo Bloque 3 (framework USD, MoS 40%) ───────────
def c09():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    valor = 43.78
    precio = PRECIO_VIVO_USD
    gatillo = 26.27
    descuento_hoy = 31.45
    mos_exigido = 40.0

    labels = ["Gatillo Bloque 3\n(MoS 40% exigido)", "Precio vivo\n8-sep-2026", "Valor intrínseco\ncorregido"]
    vals = [gatillo, precio, valor]
    cols = [P["rojo"], P["tinta"], P["azul"]]
    y = np.arange(3)
    ax.barh(y, vals, color=cols, height=0.45, zorder=3)
    for i, v in enumerate(vals):
        ax.text(v + 0.6, i, f"US$ {v:,.2f}".replace(",", "."), va="center", fontsize=9.6,
                fontweight="bold", color=P["tinta"])
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9.2)
    ax.invert_yaxis()
    ax.set_xlim(0, 52)
    ax.set_xlabel("US$ por acción (convención de la validación cruzada, 2026-09-08)")
    ax.text(34, 2.75,
            f"descuento hoy: -{descuento_hoy:.2f}%  ·  MoS exigido (Bloque 3): {mos_exigido:.0f}%\n"
            f"faltan ~{mos_exigido - descuento_hoy:.1f} puntos de descuento adicional para gatillar COMPRA",
            fontsize=8.4, color=P["gris"], style="italic")
    fig.subplots_adjust(top=0.74, bottom=0.16, left=0.20, right=0.97)
    deco(ax, "Barato de verdad (-31,45%), pero no LO BASTANTE barato para el Bloque 3",
         "El precio tendría que caer otro ~13% más, hasta ~US$26,27 (~¥4.180), para cubrir el 40% de margen de seguridad que exigen los huecos de evidencia abiertos.",
         "Fuente: Actualización 2026-09-08, framework Bloque 3 (tier de incertidumbre, val-mos), en US$.", fig)
    save(fig, "09_gatillo_bloque3")


if __name__ == "__main__":
    for fn in (c01, c03, c08, c09):
        fn()
        print(f"  ok: {fn.__name__}")
    print("Gráficos v2 (regenerados + nuevos) listos en charts/")
