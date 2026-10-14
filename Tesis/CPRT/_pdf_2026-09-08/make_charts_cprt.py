# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis CPRT v2 (actualización 2026-09-08).
Reutiliza integramente 02, 03, 04, 05 del 2026-09-04 (ningún número que muestran
cambió materialmente). Regenera 01 (precio de referencia y el ancla provisional
de 38,49 US$ de la cross-validación del 8-sep) y añade 06 (brecha de margen de
seguridad vs. el umbral de 40% del Bloque 3) y 07 (el caso Progressive/RB Global,
marcado explícitamente como no verificado contra fuente primaria).
Fuente: 2026-09-04_UltraTesis_CPRT_metodo12_borrador.md, Pasos 9-10 y
"Actualización 2026-09-08"."""
import numpy as np, matplotlib.pyplot as plt
from chart_style import deco, save, P

# ── 01 · Rango de valor intrínseco vs. precio actual (actualizado 8-sep) ────
def c01():
    cat = ["BAJISTA\npropio", "BASE PROPIO\n(DCF variable)", "BASE RÉPLICA\nfuente (7,4% flat)",
           "CROSS-VALIDACIÓN\n8-sep (PROVISIONAL)", "ALCISTA\npropio"]
    centro = [21.5, 30.0, 33.4, 38.49, 39.7]
    etiquetas = ["21,5", "30,0", "33,4", "38,49", "39,7"]
    lo = [None, 28.8, 32.0, None, None]
    hi = [None, 31.5, 35.0, None, None]
    cols = [P["rojo_oscuro"], P["azul"], P["azul_acero"], P["ocre"], P["verde"]]
    x = np.arange(5)
    fig, ax = plt.subplots(figsize=(11.6, 5.2))
    ax.bar(x, centro, color=cols, width=0.58, zorder=3)
    for i in range(5):
        if lo[i] is not None:
            ax.plot([x[i], x[i]], [lo[i], hi[i]], color=P["tinta"], lw=1.6, zorder=4)
            ax.plot([x[i]-0.09, x[i]+0.09], [lo[i], lo[i]], color=P["tinta"], lw=1.6, zorder=4)
            ax.plot([x[i]-0.09, x[i]+0.09], [hi[i], hi[i]], color=P["tinta"], lw=1.6, zorder=4)
        y_lab = (hi[i] if hi[i] is not None else centro[i]) + 1.3
        ax.text(x[i], y_lab, etiquetas[i] + " US$",
                ha="center", fontsize=10.5, fontweight="bold", color=cols[i])
    notas = ["g 2% · WACC 10,0%\nterminal 2,5%", "g 3%→6-7,5%→5%\nCAGR 5,8%",
             "g 7,4% flat\nWACC bottom-up", "g 7,4% flat · WACC 9,83%\nAño 1 sin revalidar",
             "g 8,5% · WACC 9,4%\nterminal 4,0%"]
    for i in range(5):
        ax.text(x[i], 2.3, notas[i], ha="center", fontsize=6.9, color="white", style="italic")
    ax.axhspan(32.99, 33.46, color=P["rojo"], alpha=0.16, zorder=2)
    ax.axhline(33.23, color=P["rojo"], lw=2.0, ls="--", zorder=5)
    ax.text(4.5, 34.9, "PRECIO 6-SEP\n32,99-33,46 US$", fontsize=8.6, color=P["rojo"], fontweight="bold", ha="right")
    ax.set_xticks(x); ax.set_xticklabels(cat, fontsize=8.0)
    ax.set_ylabel("valor intrínseco por acción (US$)"); ax.set_ylim(0, 45); ax.set_xlim(-0.65, 4.85)
    fig.subplots_adjust(top=0.76, bottom=0.14, left=0.075, right=0.97)
    deco(ax, "Ningún caso central deja margen de seguridad real — ni el nuevo",
         "El ancla provisional de la cross-validación del 8-sep (38,49 US$) no está revalidada contra el FY2026 real, que se conoce en días.",
         "Fuente: Paso 9 del documento fuente (DCF explícito e inverso) y Actualización 2026-09-08 (valoración recalculada, WACC 9,83%).", fig)
    save(fig, "01_valor_intrinseco")

# ── 06 · Brecha de margen de seguridad frente al umbral de 40% (Bloque 3) ───
def c06():
    fig, ax = plt.subplots(figsize=(11.2, 4.8))
    ancla = 38.49
    precio_lo, precio_hi = 32.99, 33.46
    gatillo = 23.09
    mos_hoy = (ancla - precio_hi) / ancla * 100   # ~13.1%, conservador (precio alto del rango)
    mos_hoy_lo = (ancla - precio_lo) / ancla * 100  # ~14.3%

    cats = ["MoS disponible\nhoy (6-sep)", "MoS exigido\nBloque 3"]
    vals = [ (mos_hoy_lo + mos_hoy)/2, 40.0]
    cols = [P["rojo_oscuro"], P["azul_noche"]]
    x = np.arange(2)
    ax.bar(x, vals, color=cols, width=0.42, zorder=3)
    ax.text(0, vals[0]+1.3, f"~{vals[0]:.0f}%", ha="center", fontsize=13, fontweight="bold", color=P["rojo_oscuro"])
    ax.text(1, vals[1]+1.3, "40%", ha="center", fontsize=13, fontweight="bold", color=P["azul_noche"])
    ax.set_xticks(x); ax.set_xticklabels(cats, fontsize=10)
    ax.set_ylabel("margen de seguridad (%)"); ax.set_ylim(0, 48); ax.set_xlim(-0.7, 1.7)
    ax.annotate("", xy=(0.5, vals[1]-1), xytext=(0.5, vals[0]+1),
                arrowprops=dict(arrowstyle="->", color=P["gris"], lw=1.4))
    ax.text(0.72, (vals[0]+vals[1])/2, "brecha ≈ 26-27 pp", fontsize=8.6, color=P["gris"], style="italic")
    ax.text(-0.62, 43.5, f"Gatillo de compra: {gatillo:.2f}".replace(".", ",") + " US$  (38,49 × 0,60)",
            fontsize=8.8, color=P["ocre"], fontweight="bold", ha="left")
    fig.subplots_adjust(top=0.74, bottom=0.14, left=0.09, right=0.97)
    deco(ax, "El margen de seguridad disponible es un tercio del exigido",
         "Con el ancla provisional de 38,49 US$ y el precio del 6-sep, el MoS disponible (~14%) queda muy por debajo del 40% del Bloque 3.",
         "Fuente: Actualización 2026-09-08 — valoración recalculada; criterio de MoS revisado de Felipe (Bloque 3: 40% mientras «maravillosa» esté en disputa).", fig)
    save(fig, "06_gatillo_mos")

# ── 07 · El caso Progressive: cuota entre Copart y RB Global (NO VERIFICADO) ─
def c07():
    fig, ax = plt.subplots(figsize=(11.2, 5.3))
    periodos = ["Antes\n(pre-nov-2025)", "Después\n(post-nov-2025)"]
    copart = [25, 10]
    rbglobal = [75, 90]
    x = np.arange(2)
    w = 0.5
    ax.bar(x, copart, w, color=P["azul"], label="Copart", zorder=3)
    ax.bar(x, rbglobal, w, bottom=copart, color=P["gris_medio"], label="RB Global (IAA)", zorder=3)
    for i in range(2):
        ax.text(x[i], copart[i]/2, f"~{copart[i]}%", ha="center", va="center", fontsize=11,
                fontweight="bold", color="white")
        ax.text(x[i], copart[i] + rbglobal[i]/2, f"~{rbglobal[i]}%", ha="center", va="center", fontsize=11,
                fontweight="bold", color="white")
    ax.set_xticks(x); ax.set_xticklabels(periodos, fontsize=10)
    ax.set_ylabel("cuota estimada en la cuenta (%)"); ax.set_ylim(0, 108)
    ax.legend(frameon=False, fontsize=9, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.14))
    fig.text(0.5, 0.045, "NO VERIFICADO CONTRA FUENTE PRIMARIA — DEGRADADO, delegado a verificador",
              fontsize=8.6, color=P["rojo_oscuro"], fontweight="bold", ha="center",
              transform=fig.transFigure)
    fig.subplots_adjust(top=0.70, bottom=0.22, left=0.09, right=0.97)
    deco(ax, "El caso Progressive: la cuenta que ilustra el Mecanismo 2, si se confirma",
         "Cuota estimada de Copart en una gran cuenta de seguros cayendo de ~25% a ~10%, nov-2025 — citado por el abogado-diablo del 8-sep, sin documento primario todavía.",
         "Fuente: Actualización 2026-09-08 — hallazgo citado por el abogado-diablo, pendiente de verificación (10-Q/10-K, transcript o comunicado de RB Global).", fig,
         flag_y=0.93)
    save(fig, "07_progressive_cuota")

for f in [c01, c06, c07]:
    f(); print("ok", f.__name__)
