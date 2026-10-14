# -*- coding: utf-8 -*-
"""Genera los 6 graficos de la Tesis Definitiva INTU. Ejecutar una vez; produce PNGs en charts/."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
import matplotlib.patheffects as pe
from chart_style import deco, save
from paleta_qg import PALETA as P

# ══════════════════════════════════════════════════════════════════
# C1 · DE DONDE SALE CADA DOLAR — ingresos FY2025 por motor, coloreados
#      por quien manda (precio vs unidades vs mixto vs exogeno)
# ══════════════════════════════════════════════════════════════════
motores = [
    ("QBO Accounting\n(~30% de GBS)", 2493, "precio"),
    ("Online Services\n· Pagos", 1800, "unidades"),
    ("Ecosistema\nDesktop", 2775, "precio"),
    ("TurboTax\n(nucleo)", 4870 * 0.74, "precio"),
    ("TurboTax Live\n(53% de TT)", 4870 * 0.53, "unidades_precio_cede"),
    ("Credit Karma", 2263, "exogeno"),
    ("Mailchimp", 1300, "precio_sin_base"),
]
colores = {
    "precio": P["rojo"],
    "unidades": P["verde"],
    "unidades_precio_cede": P["ocre"],
    "exogeno": P["azul_cielo"],
    "precio_sin_base": P["gris_medio"],
}
labels_leyenda = {
    "precio": "Motor = PRECIO",
    "unidades": "Motor = UNIDADES",
    "unidades_precio_cede": "Unidades, cediendo precio",
    "exogeno": "Exogeno (ciclo de credito)",
    "precio_sin_base": "Precio sobre base sin crecer",
}

fig, ax = plt.subplots(figsize=(10.4, 5.6))
nombres = [m[0] for m in motores]
valores = [m[1] for m in motores]
cols = [colores[m[2]] for m in motores]
y = np.arange(len(motores))[::-1]
bars = ax.barh(y, valores, color=cols, height=0.62, zorder=3,
                edgecolor=P["fondo"], linewidth=0.8)
for yi, v, m in zip(y, valores, motores):
    ax.text(v + 60, yi, f"US$ {v:,.0f} M", va="center", ha="left",
            fontsize=8.6, color=P["tinta"], fontweight="bold")
ax.set_yticks(y)
ax.set_yticklabels(nombres, fontsize=8.8)
ax.set_xlim(0, 5600)
ax.set_xlabel("Ingresos anualizados aproximados (US$ millones)", fontsize=8.5)

# leyenda manual
handles = [Rectangle((0, 0), 1, 1, color=c) for c in
           [colores["precio"], colores["unidades"], colores["unidades_precio_cede"],
            colores["exogeno"], colores["precio_sin_base"]]]
labs = [labels_leyenda[k] for k in
        ["precio", "unidades", "unidades_precio_cede", "exogeno", "precio_sin_base"]]
ax.legend(handles, labs, loc="lower right", fontsize=7.6, frameon=False,
          ncol=1, bbox_to_anchor=(0.99, 0.02))

deco(ax, "De donde sale cada dolar de Intuit",
     "Ingresos por motor de negocio, coloreados segun quien manda hoy: el precio o las unidades",
     "Fuente: 10-K FY2025 (acc. 0000896878-25-000035) y 8-K del 20-may-2026. Elaboracion propia sobre datos primarios.")
save(fig, "c1_motores_ingresos")

# ══════════════════════════════════════════════════════════════════
# C2 · EL MERCADO YA HIZO LA REBAJA — precio y multiplo, 12 meses
# ══════════════════════════════════════════════════════════════════
puntos = [
    ("22-sep-2025 — MAXIMO", "2025-09-22", 702.09, 48.6),
    ("Coste medio de Felipe", "2026-01-15", 262.23, 18.3),
    ("Semana 22-jun-2026 — MINIMO", "2026-06-22", 255.07, 17.9),
    ("24-ago-2026 — HOY", "2026-08-24", 369.49, 25.7),
]
import datetime as dt
xs = [dt.date.fromisoformat(p[1]) for p in puntos]
ys = [p[2] for p in puntos]
mult = [p[3] for p in puntos]
x0 = xs[0]
xnum = [(x - x0).days for x in xs]

fig, ax1 = plt.subplots(figsize=(10.6, 6.4))
fig.subplots_adjust(top=0.78, bottom=0.11, left=0.075, right=0.97)
ax1.plot(xnum, ys, color=P["azul"], lw=2.4, zorder=4, marker="o",
         markersize=8, markerfacecolor=P["fondo"], markeredgecolor=P["azul"],
         markeredgewidth=2.2)
ax1.fill_between(xnum, ys, min(ys) - 20, color=P["azul"], alpha=0.08, zorder=1)

ax1.annotate("", xy=(xnum[2] - 8, ys[2] + 18), xytext=(xnum[0] + 8, ys[0] - 18),
             arrowprops=dict(arrowstyle="-|>", color=P["rojo_oscuro"], lw=1.6,
                              connectionstyle="arc3,rad=-0.05"), zorder=3)
ax1.text((xnum[0] + xnum[2]) / 2 - 55, 470,
          "−63,7%\nde cierre a cierre\nen 9 meses", ha="center", va="center", fontsize=9.6,
          color=P["rojo_oscuro"], fontweight="bold", linespacing=1.35)

ax1.annotate("", xy=(xnum[3] - 6, ys[3] - 8), xytext=(xnum[2] + 6, ys[2] + 8),
             arrowprops=dict(arrowstyle="-|>", color=P["verde"], lw=1.6,
                              connectionstyle="arc3,rad=0.25"), zorder=3)
ax1.text(xnum[2] + 22, 205,
          "+43% en 8 semanas\n(incluye 364,53 el 21-ago,\nprecio fijado por el encargo)",
          ha="left", va="center", fontsize=8.2, color=P["verde"], fontweight="bold", linespacing=1.35)

# etiquetas de los 4 puntos: MAXIMO arriba-izq, coste medio abajo, MINIMO abajo-izq, HOY arriba-der
ax1.text(xnum[0] + 14, ys[0] - 8, f"22-sep-2025 — MAXIMO\nUS$ 702,09  ·  48,6× OE",
         ha="left", va="top", fontsize=8.4, color=P["tinta"], fontweight="bold",
         linespacing=1.35, path_effects=[pe.withStroke(linewidth=3.2, foreground=P["fondo"])])
ax1.text(xnum[1] - 8, ys[1] + 95, f"Coste medio de Felipe\nUS$ 262,23  ·  18,3× OE",
         ha="center", va="bottom", fontsize=8.4, color=P["tinta"],
         linespacing=1.35, path_effects=[pe.withStroke(linewidth=3.2, foreground=P["fondo"])])
ax1.text(xnum[2] - 8, ys[2] - 28, f"Semana 22-jun-2026 — MINIMO\nUS$ 255,07  ·  17,9× OE",
         ha="right", va="top", fontsize=8.4, color=P["tinta"], fontweight="bold",
         linespacing=1.35, path_effects=[pe.withStroke(linewidth=3.2, foreground=P["fondo"])])
ax1.text(xnum[3] - 10, ys[3] + 55, f"24-ago-2026 — HOY\nUS$ 369,49  ·  25,7× OE",
         ha="right", va="bottom", fontsize=8.4, color=P["tinta"], fontweight="bold",
         linespacing=1.35, path_effects=[pe.withStroke(linewidth=3.2, foreground=P["fondo"])])

ax1.set_xticks(xnum)
ax1.set_xticklabels(["22-sep-2025", "ene-2026", "22-jun-2026", "24-ago-2026"], fontsize=8.4)
ax1.set_ylabel("Precio de cierre (US$)", fontsize=8.8)
ax1.set_ylim(120, 730)
ax1.set_xlim(xnum[0] - 20, xnum[-1] + 55)

deco(ax1, "El mercado ya hizo la rebaja",
     "Precio de cierre y multiplo sobre owner earnings (base 3.982 M USD) en cuatro fechas ancla, ultimos 12 meses",
     "Fuente: barras diarias y semanales de IBKR, contrato 270662, extraidas el 24-ago-2026.")
save(fig, "c2_precio_multiplo")

# ══════════════════════════════════════════════════════════════════
# C3 · EL MARGEN DEL SEGMENTO SE APAGA — GBS, variacion interanual
# ══════════════════════════════════════════════════════════════════
periodos = ["FY2023–24\n(prom.)", "FY2025", "Q1\nFY2026", "Q2\nFY2026", "Q3\nFY2026"]
delta_margen = [4.5, 1.5, -0.7, -0.9, -0.1]
consolidado = [None, None, None, None, None]  # no se grafica, solo referencia textual

fig, ax = plt.subplots(figsize=(10.2, 5.3))
cols = [P["verde"] if d >= 0 else P["rojo_oscuro"] for d in delta_margen]
bars = ax.bar(periodos, delta_margen, color=cols, width=0.56, zorder=3,
              edgecolor=P["fondo"], linewidth=1)
ax.axhline(0, color=P["gris"], lw=1.1, zorder=2)
for i, d in enumerate(delta_margen):
    va = "bottom" if d >= 0 else "top"
    off = 0.12 if d >= 0 else -0.12
    ax.text(i, d + off, f"{d:+.1f} pp", ha="center", va=va, fontsize=9.4,
            fontweight="bold", color=P["tinta"])
ax.set_ylabel("Variacion interanual del margen operativo\ndel segmento GBS (puntos porcentuales)",
              fontsize=8.4)
ax.set_ylim(-1.6, 5.6)
ax.text(4.35, 4.8, "el precio no esta\nllegando al margen\ndel segmento", fontsize=7.8,
        color=P["rojo_oscuro"], style="italic", ha="right", va="top")

deco(ax, "El margen del segmento se apaga justo cuando el precio se vuelve el motor",
     "Global Business Solutions (GBS): variacion interanual del margen operativo por periodo",
     "Fuente: 10-K FY2024-25 y 10-Q Q1-Q3 FY2026 (segmentos), acc. 0000896878-26-000025. El margen CONSOLIDADO sube en el mismo periodo (ver texto §3.2).")
save(fig, "c3_margen_segmento")

# ══════════════════════════════════════════════════════════════════
# C4 · CUANTO VALE INTU — banda de valoracion (football field)
# ══════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10.6, 5.0))
fig.subplots_adjust(top=0.72, bottom=0.13, left=0.185, right=0.96)

filas = [
    ("Extremo bajista (diablo)\ng∞ = 0",            171, 209, P["rojo_oscuro"]),
    ("SIN correccion\ng∞ = 2,34%",                  227, 319, P["azul_acero"]),
    ("CON correccion — central\ng∞ = 3,58%",   263, 372, P["azul"]),
    ("Techo de la correccion\ng∞ = 4,30%",           None, None, None),
    ("Extremo alcista (angel)\n",                        339, 533, P["verde"]),
]
y = 0
yt, yl = [], []
for nombre, lo, hi, col in filas:
    if lo is None:
        y -= 1
        continue
    ax.barh(y, hi - lo, left=lo, height=0.52, color=col, alpha=0.85, zorder=3,
            edgecolor=P["fondo"], linewidth=0.8)
    ax.text(lo - 6, y, f"{lo}", ha="right", va="center", fontsize=8, color=P["tinta"])
    ax.text(hi + 6, y, f"{hi}", ha="left", va="center", fontsize=8, color=P["tinta"])
    yt.append(y); yl.append(nombre)
    y -= 1

# lineas verticales clave
for val, lab, col, ls, dx in [
    (304, "P_justo\ncentral: 304", P["rojo"], "-", 0),
    (228, "P_tramo1 (N2)\n228", P["ocre"], "--", -18),
    (364.53, "precio hoy\n364,53", P["tinta"], "-", 0),
]:
    ax.axvline(val, color=col, lw=1.6, ls=ls, zorder=5, ymax=0.94)
    ax.text(val + dx, 1.55, lab, ha="center", va="bottom", fontsize=7.8, color=col,
            fontweight="bold", linespacing=1.25)

ax.set_yticks(yt); ax.set_yticklabels(yl, fontsize=8.6)
ax.set_xlim(140, 570)
ax.set_xlabel("US$ por accion", fontsize=8.6)
ax.set_ylim(y - 0.6, 2.35)

deco(ax, "Cuanto vale Intuit, segun quien elija los supuestos",
     "Rango de valor justo por metodo de valoracion (DCF a 10 anos, r = 9,69%). Extremos absolutos: 171-533 USD",
     "Fuente: motor propio (§5.3 de la tesis), que reproduce la matriz del diablo al dolar y las salidas del angel dentro del 1%.")
save(fig, "c4_banda_valoracion")

# ══════════════════════════════════════════════════════════════════
# C5 · MATRIZ DE SENSIBILIDAD — heatmap 3x3, CON correccion
# ══════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(9.6, 5.4))
fig.subplots_adjust(top=0.76, bottom=0.15, left=0.235, right=0.97)
bases = ["3.982 M\n(FY2025, diablo)", "4.250 M\n(FY26E normalizado)", "5.100 M\n(angel)"]
g0s = ["5,58%\n(tope antiguo)", "9,00%\n(central)", "13,95%\n(tope min-de-4)"]
valores_m = np.array([
    [263, 304, 372],
    [281, 325, 398],
    [339, 391, 478],
])
im = ax.imshow(valores_m, cmap="RdYlGn", vmin=150, vmax=500, aspect="auto")
for i in range(3):
    for j in range(3):
        v = valores_m[i, j]
        central = (i == 0 and j == 1)
        ax.text(j, i, f"US$ {v}" + ("\n>> CENTRAL <<" if central else ""),
                ha="center", va="center", fontsize=10.5 if central else 10,
                fontweight="bold", color=P["tinta"],
                path_effects=[pe.withStroke(linewidth=2.6, foreground=P["fondo"])])
ax.set_xticks(range(3)); ax.set_xticklabels(g0s, fontsize=8)
ax.set_yticks(range(3)); ax.set_yticklabels(bases, fontsize=8)
ax.set_xlabel("g₀ — crecimiento inicial (año 1)", fontsize=8.8, labelpad=8)
ax.set_ylabel("Base de owner earnings", fontsize=8.8, labelpad=10)
for s in ax.spines.values():
    s.set_visible(False)
ax.set_facecolor(P["fondo"])
fig.patch.set_facecolor(P["fondo"])

deco(ax, "La matriz de sensibilidad obligatoria",
     "Valor justo por accion (US$) con la correccion del 23-ago (g∞ = 3,58%). Ratio maximo/minimo = 1,82 → DECIDIBLE",
     "Fuente: motor propio, §5.3 de la tesis. El umbral de indecidibilidad es ratio > 2,0.")
save(fig, "c5_matriz_sensibilidad")

# ══════════════════════════════════════════════════════════════════
# C6 · LA REJILLA DE DECISION — acciones a vender por escenario
# ══════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11.6, 5.4))
fig.subplots_adjust(top=0.78, bottom=0.13, left=0.145, right=0.995)
escenarios = [
    "5 · Deterioro de\nfondo de comercio",
    "2 · 2+ piernas\nfallan",
    "1 · CENTRAL\n1 pierna falla",
    "3 · 0 fallan,\n1 pasa",
    "4 · 0 fallan,\n2+ pasan",
]
acciones = [24, 12, 8, 6, 0]
prob = [7, 26, 52, 9, 6]
posicion_pct = [0.0, 3.02, 4.02, 4.52, 6.03]
cols6 = [P["rojo_oscuro"], P["terracota"], P["rojo"], P["ocre"], P["verde"]]

y = np.arange(len(escenarios))
bars = ax.barh(y, acciones, color=cols6, height=0.58, zorder=3,
               edgecolor=P["fondo"], linewidth=0.8)
for yi, a, pr, pp in zip(y, acciones, prob, posicion_pct):
    pp_s = f"{pp:.1f}".replace(".", ",")
    ax.text(a + 0.6, yi, f"{a} acc.  ·  {pp_s}% NAV  ·  ~{pr}% prob.",
            va="center", ha="left", fontsize=7.6, color=P["tinta"], fontweight="bold")
ax.set_yticks(y); ax.set_yticklabels(escenarios, fontsize=8.8)
ax.set_xlim(0, 33.5)
ax.set_xlabel("Acciones vendidas de las 24 vivas", fontsize=8.6)
ax.invert_yaxis()
ax.axvline(8, color=P["tinta"], lw=1.2, ls="--", alpha=0.6, zorder=2)
ax.text(8.5, y[2] + 0.36, "escenario central: ~52% de prob.", ha="left", va="top",
        fontsize=7.6, color=P["gris"], style="italic")

deco(ax, "La rejilla de decision, sellada antes del reporte del 25-ago",
     "Acciones a vender de las 24 vivas, segun el resultado de las cuatro piernas del pre-compromiso",
     "Fuente: §7.6 de la tesis. Probabilidades: predicciones selladas del redactor, 24-ago-2026, sujetas a calificacion posterior.")
save(fig, "c6_rejilla_decision")

print("6 graficos generados en charts/")
