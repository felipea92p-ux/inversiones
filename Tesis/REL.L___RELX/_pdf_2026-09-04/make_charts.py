# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis RELX — datos tomados literalmente del documento
fuente 2026-09-04_UltraTesis_REL.L___RELX_metodo12_borrador.md (Pasos 3, 5, 9).
Ningún número aquí está inventado; cada serie cita el paso de origen en su fuente.
"""
import numpy as np
import chart_style as cs
import matplotlib.pyplot as plt
from paleta_qg import PALETA as P

PRECIO_ACTUAL = 26.20  # £, Paso 9

def gbp(x, dec=1):
    """Formatea una cifra en libras con coma decimal (convención del documento fuente)."""
    return f"{x:.{dec}f}".replace(".", ",")

# ─────────────────────────────────────────────────────────────────────────
# 1) Rango de valor intrínseco (bajista / base / alcista) vs precio actual
# ─────────────────────────────────────────────────────────────────────────
def chart_valor_intrinseco():
    fig, ax = plt.subplots(figsize=(11.2, 4.7))
    fig.subplots_adjust(top=.74, bottom=.14, left=.08, right=.97)
    casos = ["Caso bajista\n(WACC 8,5%, g→2,5%,\nmargen congelado)",
             "Caso base\n(WACC 8,0%,\nreinversión conservadora)",
             "Caso alcista\n(WACC 7,5%,\nreinversión ~patrón real)"]
    lo = [16.6, 25.5, 29.0]
    hi = [16.6, 26.9, 31.0]
    mid = [(a + b) / 2 for a, b in zip(lo, hi)]
    err_low = [m - a for m, a in zip(mid, lo)]
    err_high = [b - m for b, m in zip(hi, mid)]
    colores = [P["rojo_oscuro"], P["azul"], P["verde"]]
    x = np.arange(3)
    ax.bar(x, mid, yerr=[err_low, err_high], width=0.5, color=colores,
           capsize=6, ecolor=P["gris"], error_kw={"elinewidth": 1.3})
    for i, (a, b) in enumerate(zip(lo, hi)):
        etiqueta = f"£{gbp(a)}" if a == b else f"£{gbp(a)}–{gbp(b)}"
        ax.text(x[i], hi[i] + 0.9, etiqueta, ha="center", fontsize=9.5,
                fontweight="bold", color=P["tinta"])
    ax.axhline(PRECIO_ACTUAL, color=P["tinta"], lw=1.6, ls="-", zorder=0)
    ax.text(2.30, PRECIO_ACTUAL + 0.4, f"Precio hoy: £{gbp(PRECIO_ACTUAL, 2)}",
            fontsize=9, color=P["tinta"], ha="right", fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(casos, fontsize=8.6)
    ax.set_ylabel("Libras por acción")
    ax.set_xlim(-0.55, 2.75)
    ax.set_ylim(0, 36)
    cs.deco(ax, "El caso base cae casi encima del precio de hoy",
            "Rango de valor intrínseco por escenario vs. precio de mercado (£26,20) — Paso 9",
            "Fuente: documento fuente, Paso 9 (DCF explícito a 10 años, WACC bottom-up 7,5-8,5%).")
    cs.save(fig, "01_valor_intrinseco")


# ─────────────────────────────────────────────────────────────────────────
# 2) Margen operativo ajustado y ROIC, 2020/2021-H1'26
# ─────────────────────────────────────────────────────────────────────────
def chart_margen_roic():
    fig, ax1 = plt.subplots(figsize=(11.2, 4.7))
    fig.subplots_adjust(top=.74, bottom=.12, left=.08, right=.90)
    anios_margen = ["2020", "2021", "2022", "2023", "2024", "2025", "H1'26"]
    margen = [29.2, 30.5, 31.4, 33.1, 33.9, 34.8, 35.5]
    anios_roic = ["2021", "2022", "2023", "2024", "2025"]
    roic = [11.9, None, None, None, 15.4]  # solo extremos son HECHO explícito

    ax1.plot(anios_margen, margen, marker="o", color=P["azul"], lw=2.2,
             markersize=5.5, label="Margen operativo ajustado (%)")
    for i, v in enumerate(margen):
        ax1.annotate(f"{v:.1f}%", (i, v), textcoords="offset points",
                     xytext=(0, 8), ha="center", fontsize=7.8, color=P["azul"])

    ax2 = ax1.twinx()
    # ROIC: solo pintamos los dos extremos verificados como HECHO (2021 y 2025);
    # la línea entre medias es un trazo de tendencia, no un dato interpolado.
    x_roic = [1, 5]  # posiciones equivalentes a 2021 y 2025 en el eje de margen (índices 1 y 5)
    ax2.plot(x_roic, [11.9, 15.4], marker="s", color=P["terracota"], lw=2.0,
             ls=(0, (4, 2)), markersize=6)
    ax2.annotate("ROIC 11,9% (2021)", (1, 11.9), textcoords="offset points",
                 xytext=(0, -22), ha="center", fontsize=7.6, color=P["terracota"])
    ax2.annotate("ROIC 15,4% (2025)", (5, 15.4), textcoords="offset points",
                 xytext=(20, 26), ha="left", fontsize=7.6, color=P["terracota"])
    ax2.set_ylim(8, 18)
    ax2.grid(False)
    ax2.spines["right"].set_visible(True)
    ax2.spines["right"].set_color(P["gris_linea"])
    ax2.tick_params(length=0, colors=P["gris"])
    ax2.set_ylabel("ROIC reportado (%)", color=P["terracota"])

    ax1.set_ylabel("Margen operativo ajustado (%)", color=P["azul"])
    ax1.set_ylim(26, 38)
    cs.deco(ax1, "El ahorro de escala se lo queda la empresa, no el cliente",
            "Margen operativo ajustado del grupo (línea azul) y ROIC reportado, extremos verificados (línea terracota)",
            "Fuente: documento fuente, Pasos 2 y 3 (notas de prensa de resultados/AR2025, HECHO).")
    cs.save(fig, "02_margen_roic")


# ─────────────────────────────────────────────────────────────────────────
# 3) Comparativa de beta: dispersión de fuentes vs. bottom-up
# ─────────────────────────────────────────────────────────────────────────
def chart_beta():
    fig, ax = plt.subplots(figsize=(11.2, 5.2))
    fig.subplots_adjust(top=.72, bottom=.11, left=.30, right=.96)
    filas = [
        ("RELX — beta original\n(Infront/PortfoliosLab/Google, R²=0,21)", 0.64, 0.64, P["gris_medio"]),
        ("RELX — stockanalysis.com\n(LSE, reconsultada 4-sep-2026)", 0.27, 0.27, P["gris_medio"]),
        ("RELX — stockanalysis.com\n(NYSE, reconsultada 4-sep-2026)", 0.26, 0.26, P["gris_medio"]),
        ("Thomson Reuters\n(comparable directo)", 0.17, 0.17, P["azul_cielo"]),
        ("Wolters Kluwer\n(comparable directo)", 0.16, 0.16, P["azul_cielo"]),
        ("Informa\n(más peso en eventos físicos)", 0.68, 0.68, P["azul_acero"]),
        ("Sector Damodaran\n(\"Publishing & Newspapers\", 307 emp., desapalancado)", 0.68, 0.68, P["ocre"]),
        ("RELX — bottom-up Hamada\n(re-apalancado, adoptado para el WACC)", 0.75, 0.85, P["rojo"]),
    ]
    labels = [f[0] for f in filas]
    lo = [f[1] for f in filas]
    hi = [f[2] for f in filas]
    colores = [f[3] for f in filas]
    y = np.arange(len(filas))[::-1]
    for yi, a, b, c in zip(y, lo, hi, colores):
        if a == b:
            ax.plot(a, yi, "o", color=c, markersize=9, zorder=3)
            ax.text(a + 0.025, yi, f"{a:.2f}", va="center", fontsize=8.4, color=P["tinta"])
        else:
            ax.plot([a, b], [yi, yi], color=c, lw=5, solid_capstyle="round", zorder=3)
            ax.text(b + 0.025, yi, f"{a:.2f}–{b:.2f}", va="center", fontsize=8.4,
                    color=P["tinta"], fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=8.0)
    ax.set_xlim(0, 1.05)
    ax.set_xlabel("Beta")
    ax.axvline(0.64, color=P["gris_linea"], lw=1, ls=":")
    cs.deco(ax, "La dispersión de beta es sectorial, no un defecto de RELX",
            "Betas comparables directos vs. la beta bottom-up (Hamada) usada para el WACC — Paso 9",
            "Fuente: documento fuente, Paso 9 (Infront/PortfoliosLab/Google Finance/stockanalysis.com/Damodaran).")
    cs.save(fig, "03_beta_comparativa")


# ─────────────────────────────────────────────────────────────────────────
# 4) Sensibilidad del valor por acción al WACC
# ─────────────────────────────────────────────────────────────────────────
def chart_wacc_sensibilidad():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    fig.subplots_adjust(top=.74, bottom=.13, left=.08, right=.97)
    wacc = ["7,5%", "8,0%\n(central)", "8,5%"]
    valor = [28.7, 26.2, 22.9]  # 8.0% usa el punto medio del rango 25.5-26.9
    colores = [P["verde"], P["azul"], P["rojo_oscuro"]]
    x = np.arange(3)
    ax.bar(x, valor, width=0.45, color=colores)
    for i, v in enumerate(valor):
        ax.text(x[i], v + 0.6, f"£{gbp(v)}", ha="center", fontsize=10, fontweight="bold")
    ax.axhline(PRECIO_ACTUAL, color=P["tinta"], lw=1.6)
    ax.text(2.20, PRECIO_ACTUAL + 0.5, f"Precio hoy £{gbp(PRECIO_ACTUAL, 2)}",
            ha="right", fontsize=8.8, fontweight="bold", color=P["tinta"])
    ax.set_xticks(x); ax.set_xticklabels(wacc, fontsize=9.5)
    ax.set_ylabel("Libras por acción")
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(0, 34)
    cs.deco(ax, "Un punto de WACC mueve el valor un 22%",
            "Valor por acción del DCF explícito según el WACC bottom-up (rango 7,5-8,5%, central 8,0%) — Paso 9",
            "Fuente: documento fuente, Paso 9. No se dispone de un rango de crecimiento terminal adicional "
            "para una malla WACC×g honesta — se muestra solo la sensibilidad al WACC, dato real.")
    cs.save(fig, "04_wacc_sensibilidad")


# ─────────────────────────────────────────────────────────────────────────
# 5) Construcción del DCF explícito: de flujos a valor por acción
# ─────────────────────────────────────────────────────────────────────────
def chart_dcf_construccion():
    fig, ax = plt.subplots(figsize=(11.2, 4.8))
    fig.subplots_adjust(top=.74, bottom=.14, left=.08, right=.97)
    etiquetas = ["VP flujos\nexplícitos\n(10 años)", "VP valor\nterminal\n(g=2,5%)",
                 "= Valor de\nempresa (EV)", "− Deuda neta\ny minoritarios", "= Valor del\nequity"]
    vp_flujos = 20.2
    vp_terminal = 32.7
    ev = vp_flujos + vp_terminal  # ≈52.9
    equity = 44.6
    deuda_y_otros = ev - equity  # ≈8.3, implícito por diferencia, coherente con deuda neta £7.2-8.7bn del Paso 9
    valores = [vp_flujos, vp_terminal, ev, -deuda_y_otros, equity]
    base = [0, vp_flujos, 0, equity + deuda_y_otros, 0]
    colores = [P["azul_cielo"], P["azul"], P["azul_noche"], P["rojo_oscuro"], P["verde"]]
    x = np.arange(5)
    for i, (b, v, c) in enumerate(zip(base, valores, colores)):
        if i in (2, 4):  # barras totales, desde 0
            ax.bar(x[i], v, bottom=0, color=c, width=0.55)
            ax.text(x[i], v + 1.0, f"£{gbp(v)}bn", ha="center", fontsize=9, fontweight="bold")
        else:
            bb = b if v >= 0 else b + v
            ax.bar(x[i], abs(v), bottom=bb, color=c, width=0.55)
            signo = "+" if v >= 0 else "−"
            ax.text(x[i], bb + abs(v) + 1.0, f"{signo}£{gbp(abs(v))}bn", ha="center",
                    fontsize=9, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(etiquetas, fontsize=8.2)
    ax.set_ylabel("£ miles de millones")
    ax.set_ylim(0, 62)
    cs.deco(ax, "De aquí sale el £25,5-26,9 por acción del caso base",
            "Construcción del DCF explícito a 10 años, caso base (WACC 8,0%, M&A £400-450m/año) — Paso 9",
            "Fuente: documento fuente, Paso 9. EV≈£52,9bn, equity≈£44,6bn → £25,5-26,9/acción según supuesto de M&A.")
    cs.save(fig, "05_dcf_construccion")


# ─────────────────────────────────────────────────────────────────────────
# 6) Crecimiento orgánico: RELX por segmento vs. pares directos
# ─────────────────────────────────────────────────────────────────────────
def chart_crecimiento_pares():
    fig, ax = plt.subplots(figsize=(11.2, 5.3))
    fig.subplots_adjust(top=.72, bottom=.10, left=.24, right=.95)
    filas = [
        ("RELX Legal\n(H1'26, subyacente)", 10.0, P["azul"]),
        ("RELX Legal\n(FY23, subyacente)", 6.0, P["azul_cielo"]),
        ("RELX Risk\n(estable)", 8.0, P["azul_acero"]),
        ("RELX STM\n(rango citado)", 5.0, P["azul_pro"]),
        ("Thomson Reuters\nBig-3 (Q2'26, guía)", 9.75, P["terracota"]),
        ("Thomson Reuters\ntotal orgánico (Q2'26)", 8.0, P["terracota"]),
        ("Wolters Kluwer\ntotal orgánico (H1'26)", 5.0, P["ocre"]),
        ("Wolters Kluwer\nrecurrente (H1'26)", 7.0, P["ocre"]),
        ("Clarivate\norgánico (H1'26)", -0.4, P["rojo_oscuro"]),
    ]
    labels = [f[0] for f in filas]
    vals = [f[1] for f in filas]
    colores = [f[2] for f in filas]
    y = np.arange(len(filas))[::-1]
    ax.barh(y, vals, color=colores, height=0.62)
    for yi, v in zip(y, vals):
        ax.text(v + (0.25 if v >= 0 else -0.25), yi, f"{v:+.1f}%", va="center",
                ha="left" if v >= 0 else "right", fontsize=8.6, fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=8.2)
    ax.axvline(0, color=P["gris"], lw=1)
    ax.set_xlabel("Crecimiento (%)")
    ax.set_xlim(-3, 13)
    cs.deco(ax, "En Legal, Thomson Reuters crece igual o más rápido que RELX",
            "Crecimiento orgánico más reciente de RELX por segmento vs. pares directos — Pasos 3 y 4",
            "Fuente: documento fuente, Pasos 3-4 (AR2025, transcript H1'26, notas de resultados Q2/H1 2026 de TRI/WKL/CLVT).")
    cs.save(fig, "06_crecimiento_pares")


if __name__ == "__main__":
    chart_valor_intrinseco()
    chart_margen_roic()
    chart_beta()
    chart_wacc_sensibilidad()
    chart_dcf_construccion()
    chart_crecimiento_pares()
    print("Gráficos generados en charts/")
