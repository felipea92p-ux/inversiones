# -*- coding: utf-8 -*-
"""Gráficos CLX · Ultra Tesis método 12 pasos — todos los datos vienen
literalmente del borrador verificado (Paso 9), sin recalcular ni inventar."""
from chart_style import plt, np, deco, save, P
from matplotlib.patches import Rectangle

PRECIO_HOY = 93.06

# ── 01 · Rango de valor por escenario vs. precio de hoy ──────────────────
def c01_rango_valor():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    escenarios = ["BAJISTA / trampa de valor", "BASE", "ALCISTA"]
    lo = np.array([39, 101, 155])
    hi = np.array([51, 109, 180])
    cols = [P["rojo_oscuro"], P["azul"], P["verde"]]
    y = np.arange(3)
    for i in range(3):
        ax.barh(y[i], hi[i]-lo[i], left=lo[i], height=0.46, color=cols[i], alpha=0.92, zorder=3)
        ax.text(hi[i]+3, y[i], f"US$ {lo[i]}-{hi[i]}", ha="left", va="center",
                fontsize=10.5, fontweight="bold", color=cols[i])
    ax.axvline(PRECIO_HOY, color=P["tinta"], lw=2.1, zorder=2)
    ax.annotate(f"PRECIO HOY\nUS$ {PRECIO_HOY}", xy=(PRECIO_HOY, 2.62), xytext=(PRECIO_HOY, 3.35),
                ha="center", fontsize=9, fontweight="bold", color=P["tinta"],
                arrowprops=dict(arrowstyle="-", color=P["tinta"], lw=1.1))
    ax.set_yticks(y); ax.set_yticklabels(escenarios, fontsize=9.5)
    ax.set_xlim(25, 205); ax.set_xlabel("valor de la acción implícito (US$)")
    ax.set_ylim(-0.6, 3.7)
    fig.subplots_adjust(top=0.70, bottom=0.15, left=0.19, right=0.97)
    deco(ax, "El precio de hoy cae entre el caso bajista y el base",
         "Tres escenarios del DCF a 10 años (Paso 9); rangos, no falsa precisión. Tras el Paso 10, el caso "
         "BASE se reclasifica como límite superior razonable, no como centro de gravedad.",
         "Fuente: DCF propio Paso 9 (WACC bottom-up 6,0%-7,5%), 10-K FY2026. Precio de cierre regular, 4-sep-2026.", fig)
    save(fig, "01_rango_valor")

# ── 02 · Supuestos clave del DCF por escenario ───────────────────────────
def c02_supuestos_dcf():
    fig, ax1 = plt.subplots(figsize=(11.2, 4.6))
    escenarios = ["BAJISTA", "BASE", "ALCISTA"]
    margen_fcf = [9.0, 10.0, 12.5]   # bajista estancado ~9%; base recupera 9%→11% (punto medio 10%); alcista 12-13% (punto medio 12.5%)
    g_terminal = [1.0, 2.0, 2.2]
    wacc = [7.5, 6.75, 6.0]
    cols = [P["rojo_oscuro"], P["azul"], P["verde"]]
    x = np.arange(3)
    bars = ax1.bar(x - 0.18, margen_fcf, width=0.34, color=cols, alpha=0.90, label="Margen FCF objetivo")
    for i, v in enumerate(margen_fcf):
        ax1.text(x[i]-0.18, v+0.3, f"{v:.1f}%".replace(".", ","), ha="center", fontsize=8.6,
                  fontweight="bold", color=cols[i])
    ax1.set_ylabel("margen FCF objetivo / ventas (%)"); ax1.set_ylim(0, 15)
    ax1.set_xticks(x); ax1.set_xticklabels(escenarios, fontsize=9.5)

    ax2 = ax1.twinx()
    ax2.plot(x + 0.18, wacc, "D", color=P["azul_noche"], markersize=9, zorder=5)
    for i, v in enumerate(wacc):
        ax2.text(x[i]+0.18, v+0.35, f"WACC {v:.2f}%".replace(".", ","), ha="center", fontsize=8.0,
                 fontweight="bold", color=P["azul_noche"])
        ax2.text(x[i]+0.18, v-0.9, f"g={g_terminal[i]:.1f}%".replace(".", ","), ha="center", fontsize=7.6,
                 color=P["gris"], style="italic")
    ax2.set_ylabel("WACC del escenario (%)"); ax2.set_ylim(0, 15)
    ax2.spines["right"].set_visible(True); ax2.spines["right"].set_color(P["gris_linea"])
    ax2.grid(False)
    fig.subplots_adjust(top=0.72, bottom=0.13, left=0.09, right=0.90)
    deco([ax1], "Los tres supuestos que mueven el DCF",
         "A mayor riesgo asumido, mayor WACC exigido y menor margen de recuperación — los escenarios no son "
         "arbitrarios, están amarrados entre sí.",
         "Fuente: Paso 9 (WACC bottom-up, márgenes FCF históricos 6,8%-12,6%, 10-K FY2022-FY2026).", fig)
    save(fig, "02_supuestos_dcf")

# ── 03 · Sensibilidad del valor sin crecimiento al WACC (DCF inverso) ────
def c03_sensibilidad_wacc():
    fig, ax = plt.subplots(figsize=(11.2, 4.4))
    waccs = [6.0, 6.5, 7.0]
    nopat = 940.0
    valores = [nopat/(w/100) for w in waccs]
    primas = ["7%", "14%", "20%"]
    ev_actual = 16800.0
    cols = [P["verde"], P["ocre"], P["rojo_oscuro"]]
    x = np.arange(3)
    ax.bar(x, valores, width=0.5, color=cols, alpha=0.92)
    for i, v in enumerate(valores):
        ax.text(x[i], v+350, f"US$ {v:,.0f} M".replace(",", "."), ha="center", fontsize=9.5,
                fontweight="bold", color=cols[i])
        ax.text(x[i], v/2, f"prima de\ncrecimiento\nimplícita\n{primas[i]} del EV", ha="center",
                va="center", fontsize=7.6, color="white", fontweight="bold")
    ax.axhline(ev_actual, color=P["tinta"], lw=2.2, ls="--")
    ax.text(2.42, ev_actual+300, f"EV actual ≈ US$ 16.800 M", ha="right", fontsize=9,
            fontweight="bold", color=P["tinta"])
    ax.set_xticks(x); ax.set_xticklabels([f"WACC {w:.1f}%" for w in waccs], fontsize=9.5)
    ax.set_ylabel("valor sin crecimiento — NOPAT/WACC (US$ M)")
    ax.set_ylim(0, 19000)
    fig.subplots_adjust(top=0.72, bottom=0.13, left=0.11, right=0.97)
    deco(ax, "Cuánto del precio de hoy exige crecimiento futuro",
         "DCF inverso (Rappaport-Mauboussin): a mayor WACC, menor valor \"sin crecimiento\" y mayor la prima "
         "que el precio de hoy exige.",
         "Fuente: Paso 9, NOPAT implícito guía FY2027 (≈US$940 M, margen operativo ~16%, tasa 23%).", fig)
    save(fig, "03_sensibilidad_wacc")

# ── 04 · Comparación con pares (descriptiva, sin score ni ranking) ───────
def c04_pares():
    fig, axs = plt.subplots(2, 2, figsize=(11.2, 7.6))
    empresas = ["CLX", "PG", "CHD", "CL"]
    cols = [P["rojo_oscuro"], P["azul"], P["azul_acero"], P["verde"]]

    datos = [
        ("Deuda neta / EBITDA", [4.6, 1.4, 1.7, 1.5], ["4,4-4,8x", "1,4x", "1,7x", "1,5x"], axs[0, 0]),
        ("Margen bruto", [42.3, 50.9, 45.6, 60.4], ["42,3%", "50,9%", "45,6%", "60,4%"], axs[0, 1]),
        ("ROIC (año más débil / reportado)", [14.9, 21.5, 14.0, 45.6],
         ["14,9%", "21,5%", "14,0%", "45,6%"], axs[1, 0]),
        ("Dividend yield", [5.4, 3.0, 1.25, 2.4], ["5,4%", "3,0%", "1,25%", "2,4%"], axs[1, 1]),
    ]
    for titulo, valores, etiquetas, ax in datos:
        ax.bar(empresas, valores, color=cols, width=0.6)
        for i, et in enumerate(etiquetas):
            ax.text(i, valores[i] + max(valores)*0.03, et, ha="center", fontsize=8.6,
                    fontweight="bold", color=cols[i])
        ax.set_title(titulo, fontsize=9.6, fontweight="bold", color=P["tinta"], loc="left", pad=8)
        ax.set_ylim(0, max(valores)*1.22)
        ax.grid(axis="y", color=P["gris_linea"], lw=0.6, alpha=0.9)
        ax.set_axisbelow(True)
        for s in ["top", "right", "left"]:
            ax.spines[s].set_visible(False)
        ax.spines["bottom"].set_color(P["gris_linea"]); ax.tick_params(length=0, labelsize=8.6)

    fig.subplots_adjust(top=0.70, bottom=0.06, left=0.06, right=0.97, hspace=0.55, wspace=0.22)
    fig.patches.append(Rectangle((0.012, 0.975), 0.045, 0.014,
                       transform=fig.transFigure, color=P["rojo"], zorder=5))
    fig.text(0.012, 0.935, "CLX frente a tres pares directos de consumo masivo — lectura descriptiva",
             fontsize=12, fontweight="bold", family="DejaVu Serif", ha="left", color=P["tinta"])
    fig.text(0.012, 0.905, "Sin score ni ranking de calidad (Candado C): CLX es el outlier de apalancamiento\n"
             "por 2-3x cualquier par; su margen bruto más bajo refleja mezcla de categorías-commodity,\n"
             "no mala ejecución.", fontsize=8.4, style="italic", ha="left", va="top", color=P["gris"],
             linespacing=1.6)
    fig.text(0.012, 0.012, "Fuente: Paso 9, datos estructurados de mercado cruzados con 10-K de cada compañía. "
             "RKT excluida de este panel por datos incompletos (ROIC/yield n.d.).",
             fontsize=7.2, style="italic", ha="left", color=P["gris"])
    save(fig, "04_pares")

if __name__ == "__main__":
    c01_rango_valor()
    c02_supuestos_dcf()
    c03_sensibilidad_wacc()
    c04_pares()
    print("4 gráficos generados en charts/")
