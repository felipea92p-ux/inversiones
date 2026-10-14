# -*- coding: utf-8 -*-
"""Gráficos MA — actualización 2026-09-08. Regenera SOLO las figuras cuyo número
citado cambió materialmente (precio vivo, valor intrínseco corregido, gatillo de
compra) y añade dos figuras nuevas para hechos nuevos del 8-sep (margen operativo
acelerando, gatillo de compra). Ningún número aquí está inventado: todos son citas
directas de la sección "Actualización 2026-09-08" del dossier fuente.
Cifras SIN cambio (beta, motor de reinversión, pares) no se regeneran — se copian
tal cual desde _pdf_2026-09-04/charts/."""
import numpy as np
import matplotlib.pyplot as plt
import chart_style as cs
from paleta_qg import PALETA as P

OUTDIR = "charts"

# ─────────────────────────────────────────────────────────────────────────
# 02 · Rango de valor intrínseco vs precio actual — ACTUALIZADO (precio 596,79;
# valor intrínseco corregido ~595 dentro del rango 590-730; gatillo de compra 446,25)
# ─────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 3.9))
lo, hi = 590, 730
precio = 596.79
intrinseco_pt = 595
gatillo = 446.25
ax.barh([0], [hi - lo], left=[lo], height=0.40, color=P["azul_cielo"], zorder=3,
        edgecolor=P["azul_noche"], linewidth=1.0)
ax.scatter([intrinseco_pt], [0], color=P["azul_noche"], s=70, zorder=5, marker="D")
ax.text(intrinseco_pt - 7, 0.30, "VALOR CORREGIDO\n~595 (8-sep)", color=P["azul_noche"],
        fontsize=8.2, fontweight="bold", ha="right", va="bottom")
ax.axvline(precio, color=P["rojo"], lw=2.2, zorder=4, linestyle="--", ymax=0.86)
ax.text(precio, 0.46, f"PRECIO HOY: {precio:.2f}".replace(".", ","), color=P["rojo"],
        fontsize=9.5, fontweight="bold", ha="center", va="bottom")
ax.axvline(gatillo, color=P["verde"], lw=2.0, zorder=4, linestyle=":", ymax=0.86)
ax.text(gatillo, -0.46, f"GATILLO DE COMPRA\n{gatillo:.2f} (MoS 25%)".replace(".", ","),
        color=P["verde"], fontsize=8.2, fontweight="bold", ha="center", va="top")
ax.text(lo, -0.28, f"{lo}", color=P["azul_noche"], fontsize=9.2, fontweight="bold", ha="center", va="top")
ax.text(hi, -0.28, f"{hi}", color=P["azul_noche"], fontsize=9.2, fontweight="bold", ha="center", va="top")
ax.text((lo + hi) / 2, 0.02, "RANGO RAZONABLE\nDE VALOR INTRÍNSECO (4-sep)", ha="center", va="center",
        fontsize=8.0, color=P["azul_noche"], fontweight="bold")
ax.set_xlim(420, 760)
ax.set_ylim(-0.62, 0.55)
ax.set_yticks([])
ax.set_xlabel("US dólares por acción")
cs.deco(ax, "Precio en valor justo: sin margen de seguridad al precio de hoy",
        "Cruce independiente 8-sep confirma el rango 4-sep; el gatillo de compra (MoS 25%, Bloque 1) queda 25% por debajo",
        "Fuente: dossier de valoración, Paso 9 (4-sep) + cross-validación independiente (8-sep).",
        fig)
plt.tight_layout(rect=[0, 0.16, 1, 0.88])
cs.save(fig, "02_valor_intrinseco_vs_precio", OUTDIR)

# ─────────────────────────────────────────────────────────────────────────
# 03 · DCF explícito: sensibilidad al crecimiento terminal perpetuo — precio actualizado
# ─────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.8))
g_term = [2.0, 2.5, 3.0, 3.5, 4.5]
val = [590, 630, 675, 730, 900]
ax.plot(g_term, val, marker="o", color=P["azul"], lw=2.4, markersize=7, zorder=3)
for gx, vy in zip(g_term, val):
    etiqueta = f"{vy}+" if gx == 4.5 else f"{vy}"
    ax.annotate(etiqueta, (gx, vy), textcoords="offset points", xytext=(0, 10),
                ha="center", fontsize=9.2, fontweight="bold", color=P["azul_noche"])
ax.axhline(596.79, color=P["rojo"], lw=1.8, linestyle="--", zorder=2)
ax.text(4.4, 596.79 + 8, "precio hoy: 596,79", color=P["rojo"], fontsize=8.6,
        ha="right", fontweight="bold")
ax.annotate("DCF inverso: el escenario\nque iguala el precio de hoy\nimplica g terminal ≈ 2,0%\n(≈ PIB nominal, sin prima)",
            xy=(2.0, 590), xytext=(2.55, 480), fontsize=8.2, color=P["gris"],
            arrowprops=dict(arrowstyle="->", color=P["gris"], lw=1.0))
ax.set_xlabel("Crecimiento terminal perpetuo asumido (%)")
ax.set_ylabel("Valor implícito por acción (US$)")
ax.set_xlim(1.7, 4.8)
ax.set_ylim(450, 950)
cs.deco(ax, "El valor de Mastercard es extremadamente sensible al crecimiento a perpetuidad",
        "DCF explícito a 10 años, owner earnings base 2025 = US$16.562M, WACC central 7,8% (Paso 9)",
        "Fuente: dossier de valoración, Paso 9, tabla de sensibilidad al g terminal — actualizado con precio 8-sep-2026.",
        fig)
plt.tight_layout(rect=[0, 0.14, 1, 0.88])
cs.save(fig, "03_dcf_sensibilidad_g", OUTDIR)

# ─────────────────────────────────────────────────────────────────────────
# 07 · NUEVO — margen operativo GAAP: la aceleración que ya supera el falsador
# ─────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9.2, 4.6))
cats = ["FY2021", "FY2025", "Q2 FY2026\n(trimestral)"]
vals = [53.4, 57.6, 60.2]
colores = [P["azul_cielo"], P["azul_acero"], P["rojo"]]
x = np.arange(len(cats))
ax.bar(x, vals, color=colores, width=0.5, zorder=3)
for xi, v in zip(x, vals):
    ax.text(xi, v + 1.0, f"{v:.1f}".replace(".", ",") + "%", ha="center", fontsize=10,
            fontweight="bold", color=P["tinta"])
ax.axhline(57.6, color=P["ocre"], lw=1.6, linestyle=":", zorder=2)
ax.text(0.02, 58.3, "falsador Paso 12 (#5): 57,6% FY2025", color=P["ocre"], fontsize=7.8,
        transform=ax.get_yaxis_transform(), ha="left", fontweight="bold")
ax.set_xticks(x); ax.set_xticklabels(cats, fontsize=9.2)
ax.set_ylim(0, 72)
ax.set_ylabel("Margen operativo GAAP (%)")
cs.deco(ax, "El margen ya superó su propio falsador — antes del cierre del año fiscal",
        "Q2 2026 (60,2%) ya excede el 57,6% de FY2025 que el Paso 12 fijó como techo a vigilar en el 10-K FY2026",
        "Fuente: earnings release Q2 2026, cruzado con GuruFocus — DEGRADADO hasta cierre de año fiscal (feb-2027).",
        fig)
plt.tight_layout(rect=[0, 0.15, 1, 0.86])
cs.save(fig, "07_margen_operativo_actualizado", OUTDIR)

print("Gráficos actualizados generados en", OUTDIR)
