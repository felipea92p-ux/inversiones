# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis OBIC (4684.T), 2026-09-04.
Todos los datos verificados en el monólogo fuente (método QG de 12 pasos).
Ningún número se inventa: cada cifra remite a una línea del dossier."""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save, P

PRECIO_VIVO = 5082

# ── 01 · Rango de valor intrínseco vs. precio vivo ──────────────────────
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
    ax.axvline(PRECIO_VIVO, color=P["tinta"], lw=2.2, zorder=2)
    ax.text(PRECIO_VIVO + 60, len(filas) - 0.35, f"PRECIO VIVO\n¥{PRECIO_VIVO:,}".replace(",", "."),
            fontsize=8.8, fontweight="bold", color=P["tinta"])
    ax.set_xlim(1800, 9300)
    ax.set_xlabel("yenes por acción")
    fig.subplots_adjust(top=0.72, bottom=0.12, left=0.27, right=0.97)
    deco(ax, "Cinco escenarios, un solo precio que no se mueve",
         "El caso central (WACC escrutinado 7,0%-7,5%) da -3% a -6% sobre el precio vivo; el bajista combinado da -43% a -51%.",
         "Fuente: monólogo QG OBIC, Paso 9 y Paso 10 (Golpe 3), 2026-09-04.", fig)
    save(fig, "01_valor_vs_precio")


# ── 02 · DCF explícito a 10 años: owner earnings y fade de crecimiento ──
def c02():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.6))
    anios = ["Y1\n(FY2027E)", "Y5", "Y10"]
    oe = [78.884, 110.288, 138.488]
    a1.bar(range(3), oe, color=[P["azul"], P["azul_acero"], P["azul_pro"]], width=0.55)
    for i, v in enumerate(oe):
        a1.text(i, v + 2.5, f"¥{v:,.1f}B".replace(",", "."), ha="center", fontsize=8.8, fontweight="bold")
    a1.set_xticks(range(3)); a1.set_xticklabels(anios, fontsize=8.6)
    a1.set_ylabel("owner earnings (miles de millones de ¥)")
    a1.set_ylim(0, 160)
    a1.set_title("Owner earnings modelados", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)

    x = [0, 9]
    g = [10.0, 3.5]
    a2.plot(x, g, "-o", color=P["rojo"], lw=2.6, ms=9)
    a2.fill_between(x, 0, g, color=P["rojo"], alpha=0.10)
    a2.text(0, 10.6, "10,0%\n(guía FY2027E)", ha="center", fontsize=8.4, fontweight="bold", color=P["rojo"])
    a2.text(9, 4.1, "3,5%\n(terminal, año 10)", ha="center", fontsize=8.4, fontweight="bold", color=P["rojo"])
    a2.set_xlim(-1, 10); a2.set_ylim(0, 12)
    a2.set_xticks([0, 9]); a2.set_xticklabels(["Año 1", "Año 10"], fontsize=8.6)
    a2.set_ylabel("crecimiento de ingresos modelado (%)")
    a2.set_title("Fade de crecimiento (supuesto, no HECHO)", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=0.74, bottom=0.14, wspace=0.28)
    deco([a1, a2], "El DCF explícito: casi duplicar owner earnings en una década desacelerando el crecimiento a la mitad",
         "Margen 65,9%→67,0%, ratio OE/beneficio operativo 80,5% (FY2026). El punto de partida es guía de gerencia, no una g derivada mecánicamente.",
         "Fuente: monólogo QG OBIC, Paso 9 (DCF explícito) y Paso 5 (motor de reinversión), 2026-09-04.", fig)
    save(fig, "02_dcf_trayectoria")


# ── 03 · Sensibilidad del WACC + estrés adicional (margen y g terminal) ─
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
    a1.axhline(PRECIO_VIVO, color=P["tinta"], lw=1.8, ls="--")
    a1.text(2.05, PRECIO_VIVO - 320, f"precio vivo\n¥{PRECIO_VIVO:,}".replace(",", "."), fontsize=7.8, color=P["tinta"])
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
    deco([a1, a2], "El WACC decide más que cualquier dato del negocio — y el estrés correcto es peor que el original",
         "Múltiplo terminal 1/(WACC-g): 14,3x cae a 12,9x al recortar g de 2,0% a 1,25% — sólo eso ya pesa ~-10% sobre el valor terminal.",
         "Fuente: monólogo QG OBIC, Paso 9 (WACC bottom-up) y Paso 10, Golpe 3a, 2026-09-04.", fig)
    save(fig, "03_sensibilidad_wacc")


# ── 04 · Comparación con pares (mecanismo, no ranking) ──────────────────
def c04():
    empresas = ["OBIC", "SAP", "Oracle", "Money\nForward"]
    beta = [0.47, 0.76, 1.73, 1.19]
    pe = [28.2, 28.0, 26.4, 86.3]
    crec = [11.5, 7.05, 17.4, 28.3]
    margen = [65.7, 30.0, 40.0, 1.5]
    cols = [P["azul"], P["azul_acero"], P["terracota"], P["rojo_oscuro"]]

    fig, axs = plt.subplots(1, 4, figsize=(11.6, 4.1))
    datasets = [(beta, "Beta (5 años)", "", axs[0]),
                (pe, "P/E", "x", axs[1]),
                (crec, "Crec. ingresos", "%", axs[2]),
                (margen, "Margen operativo", "%", axs[3])]
    for vals, tit, suf, ax in datasets:
        ax.bar(range(4), vals, color=cols, width=0.6)
        for i, v in enumerate(vals):
            txt = f"{v:.2f}".replace(".", ",") if suf == "" else f"{v:.1f}{suf}".replace(".", ",")
            ax.text(i, v + max(vals) * 0.03, txt, ha="center", fontsize=7.6, fontweight="bold")
        ax.set_xticks(range(4)); ax.set_xticklabels(empresas, fontsize=7.2)
        ax.set_title(tit, fontsize=8.8, fontweight="bold", color=P["azul_noche"], pad=6)
        ax.set_ylim(0, max(vals) * 1.28)
    fig.subplots_adjust(top=0.70, bottom=0.14, wspace=0.45, left=0.045, right=0.985)
    deco(list(axs), "Mecanismos distintos, no una jerarquía: cada uno monetiza un nicho distinto",
         "SAP nota: crecimiento 6,4%-7,7% (punto medio graficado). Money Forward: PER 86,3x financia un crecimiento que aún no es rentable.",
         "Fuente: stockanalysis.com, fichas TYO:4684, TYO:3994 y comparables globales SAP/Oracle, consultadas 2026-09-04.", fig)
    save(fig, "04_pares_comparacion")


# ── 05 · ROIC corregido y expansión de margen ───────────────────────────
def c05():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.5))
    anios = ["FY2022", "FY2023", "FY2024", "FY2025", "FY2026", "TTM"]
    roic = [27.53, 26.05, 25.37, 24.33, 23.51, 21.82]
    a1.plot(range(6), roic, "-o", color=P["azul"], lw=2.6, ms=7)
    for i, v in enumerate(roic):
        a1.text(i, v + 0.5, f"{v:.2f}%".replace(".", ","), ha="center", fontsize=8, fontweight="bold", color=P["azul"])
    a1.set_xticks(range(6)); a1.set_xticklabels(anios, fontsize=8)
    a1.set_ylim(18, 30)
    a1.set_ylabel("ROIC (%)")
    a1.set_title("ROIC corregido: declive suave,\nno deterioro operativo", fontsize=9.2, fontweight="bold",
                  color=P["azul_noche"], pad=8)

    anios2 = ["FY2024", "FY2025", "FY2026", "FY2027E"]
    marg = [60.5, 64.6, 65.7, 65.9]
    a2.bar(range(4), marg, color=[P["azul_cielo"], P["azul_acero"], P["azul"], P["azul_pro"]], width=0.55)
    for i, v in enumerate(marg):
        a2.text(i, v + 0.6, f"{v:.1f}%".replace(".", ","), ha="center", fontsize=8.4, fontweight="bold")
    a2.set_xticks(range(4)); a2.set_xticklabels(anios2, fontsize=8.4)
    a2.set_ylim(55, 70)
    a2.set_title("Margen operativo: cinco ejercicios\nseguidos expandiéndose", fontsize=9.2, fontweight="bold",
                  color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=0.72, bottom=0.13, wspace=0.30)
    deco([a1, a2], "El capital vuelve menos por acción, pero el negocio operativo mejora cada año",
         "La caída del ROIC es mecánica: la caja neta crece más rápido que el beneficio y diluye el retorno consolidado.",
         "Fuente: monólogo QG OBIC, Paso 2 (tabla corregida) y Paso 3, deck 2026-04-22, 2026-09-04.", fig)
    save(fig, "05_roic_margen")


# ── 06 · Evidencia del moat: SS vs SI y mezcla de clientes ──────────────
def c06():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.6))
    seg = ["SS\n(mantenimiento)", "SI\n(implantación)"]
    ing = [71.508, 55.250]
    marg = [74.0, 59.7]
    crec = [13.5, 9.8]
    x = np.arange(2)
    b = a1.bar(x, ing, color=[P["azul"], P["azul_cielo"]], width=0.5)
    for i in range(2):
        a1.text(i, ing[i] + 1.5, f"¥{ing[i]:.1f}B\nmargen {marg[i]:.1f}%\n(+{crec[i]:.1f}%)".replace(".", ","),
                ha="center", fontsize=8, fontweight="bold")
    a1.set_xticks(x); a1.set_xticklabels(seg, fontsize=9)
    a1.set_ylabel("ingresos FY2026 (miles de millones de ¥)")
    a1.set_ylim(0, 95)
    a1.set_title("El mantenimiento crece más rápido\ny con más margen que la venta nueva", fontsize=9.0,
                  fontweight="bold", color=P["azul_noche"], pad=8)

    labels = ["FY2025", "FY2026"]
    pyme = [21, 19]
    grande = [27, 29]
    xw = np.arange(2); w = 0.32
    a2.bar(xw - w/2, pyme, w, color=P["ocre"], label="PYME (<¥10.000M)")
    a2.bar(xw + w/2, grande, w, color=P["azul_pro"], label="Grandes (>¥100.000M)")
    for i in range(2):
        a2.text(xw[i]-w/2, pyme[i]+0.6, f"{pyme[i]}%", ha="center", fontsize=8.4, fontweight="bold", color=P["ocre"])
        a2.text(xw[i]+w/2, grande[i]+0.6, f"{grande[i]}%", ha="center", fontsize=8.4, fontweight="bold", color=P["azul_pro"])
    a2.axhline(19, color=P["rojo"], lw=1.5, ls="--")
    a2.text(1.35, 19.4, "umbral falsador\n(Predicción #4)", fontsize=7.2, color=P["rojo"], fontweight="bold")
    a2.set_xticks(xw); a2.set_xticklabels(labels, fontsize=8.8)
    a2.set_ylim(0, 34)
    a2.set_ylabel("% de ventas SI")
    a2.legend(frameon=False, fontsize=7.6, loc="upper center")
    a2.set_title("Mezcla de clientes: ¿subida de gama\no erosión del segmento móvil?", fontsize=9.0,
                  fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=0.72, bottom=0.13, wspace=0.32)
    deco([a1, a2], "El pilar contable del moat resiste; la lectura de la mezcla de clientes queda indecisa",
         "Golpe 1 del abogado del diablo: con solo mezcla de ingresos (sin conteo de clientes) ninguna de las dos lecturas es descartable hoy.",
         "Fuente: OBIC Yūhō FY2026/3 p.15-16; deck 2026-04-22 diapositiva 7-8; monólogo QG Paso 3 y Paso 10, 2026-09-04.", fig)
    save(fig, "06_ss_si_moat")


# ── 07 · El motor de reinversión: la fórmula mecánica se rompe ──────────
def c07():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    cats = ["g mecánico\n(reinversión×ROIC)\npromedio 5 años", "CAGR ingresos\n4 años", "CAGR ingresos\n10 años",
            "CAGR owner\nearnings 4 años"]
    vals = [-0.22, 10.9, 9.2, 17.8]
    cols = [P["rojo_oscuro"], P["azul"], P["azul_acero"], P["ocre"]]
    b = ax.bar(range(4), vals, color=cols, width=0.55)
    for i, v in enumerate(vals):
        ax.text(i, v + (0.5 if v >= 0 else -0.9), f"{v:+.1f}%".replace(".", ","), ha="center",
                fontsize=9.4, fontweight="bold")
    ax.axhline(0, color=P["tinta"], lw=1)
    ax.set_xticks(range(4)); ax.set_xticklabels(cats, fontsize=8.4)
    ax.set_ylabel("% anual")
    ax.set_ylim(-3, 21)
    ax.text(3, 19.2, "inflado por expansión de margen\n(no extrapolar)", ha="center", fontsize=7.4,
            style="italic", color=P["gris"])
    fig.subplots_adjust(top=0.74, bottom=0.14, left=0.08, right=0.97)
    deco(ax, "La fórmula clásica de crecimiento da ~0% — y sin embargo la empresa creció de doble dígito",
         "OBIC reinvierte vía OPEX de capital humano (consultores, formación), no vía capex: el proxy capex-D&A no lo capta.",
         "Fuente: monólogo QG OBIC, Paso 5 (motor de reinversión, definición Damodaran) y Paso 10, Golpe 2, 2026-09-04.", fig)
    save(fig, "07_motor_crecimiento")


if __name__ == "__main__":
    for fn in (c01, c02, c03, c04, c05, c06, c07):
        fn()
        print(f"  ok: {fn.__name__}")
    print("Todos los gráficos generados en charts/")
