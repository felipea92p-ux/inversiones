# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis SPGI v2 (actualización 2026-09-08). Todos los datos citados del
monólogo fuente (2026-09-04_UltraTesis_SPGI_metodo12_borrador.md, Pasos 2, 4, 9, 10, y la
Actualización 2026-09-08). Sin cifras inventadas — sólo 01 y 03 se regeneran, porque el precio
vivo cambió de 443,35 (4-sep) a 433,84 (8-sep) y ambos gráficos dibujan la línea de precio."""
import numpy as np, matplotlib.pyplot as plt
from chart_style import deco, save, P

PRECIO_HOY = 433.84

# ── 01 · Rango de valor intrínseco vs. precio de hoy (Paso 9) ───────────
def c01():
    esc = ["BAJISTA\n6%→2%, terminal 2,5%", "BASE\n9%→4,5%, terminal 3,5%",
           "ALCISTA CENTRAL\n10%→6%, terminal 4,0%", "ALCISTA EXTREMO\nfade lento, OE0 alto"]
    val = [260, 360, 425, 462]
    var = [round((v / PRECIO_HOY - 1) * 100, 1) for v in val]
    cols = [P["rojo_oscuro"], P["azul"], P["azul_acero"], P["verde"]]
    fig, ax = plt.subplots(figsize=(11.2, 4.8))
    ax.bar(range(4), val, color=cols, width=0.56)
    # Offset por barra: si el valor cae a menos de 25 US$ de la línea de precio,
    # el rótulo se coloca por ENCIMA de la línea en vez de justo sobre la barra,
    # para que nunca se solape con el guion rojo (afecta a "alcista central").
    label_y = []
    for v in val:
        y = v + 10
        if abs(y - PRECIO_HOY) < 25:
            y = PRECIO_HOY + 18
        label_y.append(y)
    for i, (v, pc, ly) in enumerate(zip(val, var, label_y)):
        ax.text(i, ly, f"{v} US$", ha="center", fontsize=12.5, fontweight="bold", color=cols[i])
        ax.text(i, v * 0.5, f"{pc:+.1f}%".replace(".", ","), ha="center", fontsize=9.4,
                fontweight="bold", color="white")
    ax.axhline(PRECIO_HOY, color=P["rojo"], lw=2.2, ls="--")
    ax.text(-0.48, PRECIO_HOY + 14, "PRECIO HOY: 433,84 US$", fontsize=8.8, color=P["rojo"],
            fontweight="bold", ha="left")
    ax.set_xticks(range(4)); ax.set_xticklabels(esc, fontsize=8.0)
    ax.set_xlim(-0.6, 3.6)
    ax.set_ylim(0, 520); ax.set_ylabel("valor por acción (US$)")
    fig.subplots_adjust(top=0.76, bottom=0.15, left=0.075)
    deco(ax, "Cuatro escenarios, y sólo el más optimista supera el precio de hoy",
         "DCF a 10 años de owner earnings, descontado al coste de equity (9,3%). El caso base y el precio ya cruzan.",
         "Fuente: Paso 9 del monólogo evidenciado, 2026-09-04, actualizado con precio vivo del 8-sep-2026. Owner earnings FY2025 continuing ops: cifra DEGRADADA, INFERENCIA propia (4.200-5.000 M US\\$, central 4.600 M US\\$).", fig)
    save(fig, "01_valor_intrinseco")

# ── 02 · Trayectoria de crecimiento por escenario (interpolación lineal) ─
def c02():
    anos = np.arange(1, 11)
    # Interpolación lineal entre la tasa de arranque y la terminal documentadas (Paso 9).
    base = np.linspace(9.0, 4.5, 10)
    alza = np.linspace(10.0, 6.0, 10)
    baja = np.linspace(6.0, 2.0, 10)
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    ax.plot(anos, alza, "-o", color=P["verde"], lw=2.2, ms=5, label="Alcista central (10%→6%, terminal 4,0%)")
    ax.plot(anos, base, "-o", color=P["azul"], lw=2.6, ms=5.5, label="Base (9%→4,5%, terminal 3,5%)")
    ax.plot(anos, baja, "-o", color=P["rojo_oscuro"], lw=2.2, ms=5, label="Bajista (6%→2%, terminal 2,5%)")
    ax.axhline(9.6, color=P["ocre"], lw=1.8, ls=":")
    ax.text(1.05, 10.55, "lo que exige el precio de hoy: ~9,5%-9,7% sostenido, sin fade (DCF inverso)",
            fontsize=7.8, color="#8a6508", fontweight="bold")
    ax.set_xlabel("año del DCF explícito"); ax.set_ylabel("crecimiento anual de owner earnings (%)")
    ax.set_xticks(anos); ax.set_ylim(0, 11.6)
    ax.legend(frameon=False, fontsize=8.4, loc="lower left")
    fig.subplots_adjust(top=0.76, bottom=0.13, left=0.075)
    deco(ax, "El precio de hoy exige el ritmo del escenario alcista, sin desaceleración",
         "Interpolación lineal entre la tasa de arranque y la terminal de cada escenario (Paso 9). El DCF inverso exige ~9,5%-9,7% sostenido 10 años.",
         "Fuente: Paso 9 del monólogo evidenciado, 2026-09-04. Trayectorias del dossier original; interpolación propia solo para visualizar el fade.", fig)
    save(fig, "02_trayectoria_dcf")

# ── 03 · El falsador duro: qué pasa si se usa el WACC auditado ──────────
def c03():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    cats = ["WACC bottom-up\n(8,5%-9,0%, usado en el caso base)",
            "WACC auditado del JV SPDJI\nsi alcanza ≥11,0% (feb-2027)"]
    lo = [360, 260]; hi = [360, 280]
    xs = [0, 1]
    ax.bar(xs[0], lo[0], color=P["azul"], width=0.46)
    ax.bar(xs[1], hi[1], color=P["rojo_oscuro"], width=0.46)
    ax.text(xs[0], lo[0] + 8, "360 US$\n(-17,0%)", ha="center", fontsize=10.5, fontweight="bold", color=P["azul"])
    ax.text(xs[1], hi[1] + 8, "cae a 260-280 US$\n(-40% o peor)", ha="center", fontsize=10.5, fontweight="bold", color=P["rojo_oscuro"])
    ax.axhline(PRECIO_HOY, color=P["rojo"], lw=2, ls="--")
    ax.text(1.42, PRECIO_HOY + 6, "PRECIO HOY\n433,84 US$", fontsize=8.4, color=P["rojo"], fontweight="bold", ha="right")
    ax.annotate("+150-250 pb de WACC", (0.5, 400), fontsize=9, color=P["tinta"], fontweight="bold", ha="center",
                arrowprops=None)
    ax.annotate("", xy=(0.85, 340), xytext=(0.15, 340),
                arrowprops=dict(arrowstyle="->", color=P["tinta"], lw=1.6))
    ax.set_xticks(xs); ax.set_xticklabels(cats, fontsize=8.6)
    ax.set_xlim(-0.6, 1.9); ax.set_ylim(0, 480)
    ax.set_ylabel("valor por acción (US$)")
    fig.subplots_adjust(top=0.76, bottom=0.16, left=0.08)
    deco(ax, "El falsador duro del Paso 12: el caso base cuelga de qué WACC se use",
         "El propio 10-K audita, para el JV de Indices, un WACC más alto (9%→10%→10,8%) que el bottom-up de mercado usado en el DCF.",
         "Fuente: Paso 9 y Paso 10 (Golpe 3) del monólogo evidenciado, 2026-09-04, actualizado con precio vivo del 8-sep-2026; 10-K FY2021/FY2023/FY2025, materia crítica de auditoría del JV S&P Dow Jones Indices.", fig)
    save(fig, "03_wacc_falsador")

# ── 04 · Ciclo 2025: guía vs. resultado, y quién se quedó el margen ─────
def c04():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.5))
    # Panel 1: sorpresa vs. punto medio de la guía (normalizada en %, evita mezclar US$/acción con millones)
    nombres = ["Moody's", "MSCI"]
    sorpresa = [(14.94 / np.mean([14.00, 14.50]) - 1) * 100,
                (1420.9 / np.mean([1405, 1445]) - 1) * 100]
    y = [1, 0]
    sorpresa_y = [sorpresa[0], sorpresa[1]]
    cols1 = [P["verde"], P["gris_medio"]]
    a1.barh(y, sorpresa_y, color=cols1, height=0.42)
    a1.axvline(0, color=P["tinta"], lw=1)
    a1.text(0.15, 1.32, "+4,8%: real 14,94 vs. guía 14,00-14,50\n(EPS ajustado FY2025)",
            ha="left", va="bottom", fontsize=7.8, fontweight="bold", color=P["verde"])
    a1.text(0.15, 0.32, "-0,3%: real 1.420,9 M vs. guía 1.405-1.445 M\n(gasto operativo FY2025)",
            ha="left", va="bottom", fontsize=7.8, fontweight="bold", color=P["gris"])
    a1.set_yticks(y); a1.set_yticklabels(nombres, fontsize=9.2)
    a1.set_xlim(-1.5, 8); a1.set_ylim(-0.5, 2.1)
    a1.set_xlabel("desvío del resultado real vs. punto medio de la guía (%)")
    a1.set_title("Guía vs. resultado real (FY2025)", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)
    # Panel 2: margen — variación de puntos porcentuales en el periodo (comparable entre ambas)
    nom2 = ["SPGI Ratings\nmargen operativo, 2023→2025", "FactSet\nmargen ajustado, en el año"]
    deltas = [8.0, -1.5]
    cols2 = [P["verde"], P["rojo_oscuro"]]
    a2.bar([0, 1], deltas, color=cols2, width=0.5)
    a2.text(0, 8.7, "+8 puntos\n(56%→64%)", ha="center", fontsize=9, fontweight="bold", color=P["verde"])
    a2.text(1, -3.6, "-150 pb\npese a ingresos +5,4%", ha="center", fontsize=9, fontweight="bold", color=P["rojo_oscuro"])
    a2.axhline(0, color=P["tinta"], lw=1)
    a2.set_xticks([0, 1]); a2.set_xticklabels(nom2, fontsize=8.2)
    a2.set_xlim(-0.6, 1.6); a2.set_ylim(-6, 11.5)
    a2.set_ylabel("variación del margen operativo (puntos)")
    a2.set_title("Quién se quedó el ahorro de escala", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=0.72, bottom=0.24, wspace=0.32, left=0.10, right=0.975)
    deco([a1, a2], "El ciclo de 2025 fue bueno para el sector, pero no todos lo capturaron igual",
         "Moody's y MSCI batieron o cumplieron su propia guía en el mismo ciclo de emisión; FactSet, más cerca del terminal tradicional, tuvo apalancamiento operativo negativo.",
         "Fuente: Paso 4 del monólogo evidenciado, 2026-09-04 (comunicados de resultados de Moody's, MSCI y FactSet; 10-K FY2025 de SPGI, segmento Ratings).", fig)
    save(fig, "04_scuttlebutt_margen")

for f in [c01, c02, c03, c04]:
    f(); print("ok", f.__name__)
