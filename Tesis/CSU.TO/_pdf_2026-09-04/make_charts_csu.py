# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis CSU.TO (2026-09-04). Todos los datos citados
literalmente del monólogo evidenciado fuente (método 12 pasos + Paso 10
abogado del diablo). Ninguna cifra se inventa aquí."""
import numpy as np
import matplotlib.pyplot as plt
from chart_style import deco, save, P

# ── 01 · Los tres escenarios del DCF original (Paso 9, r=7,0% en el caso BASE) ──
def c01():
    fig, ax = plt.subplots(figsize=(11.2, 4.6))
    esc = ["BAJISTA propio\nr=8,0% · 3/1/0%, term. 2%", "BASE (Paso 9)\nr=7,0% · 9/6/4%, term. 3%",
           "ALCISTA\nr=6,5% · 12/8/5%, term. 3,5%"]
    val = [2152, 4465, 6782]
    cols = [P["rojo_oscuro"], P["azul"], P["verde"]]
    ax.bar(range(3), val, color=cols, width=.5)
    for i, v in enumerate(val):
        ax.text(i, v + 130, f"C${v:,.0f}".replace(",", "."), ha="center", fontsize=12.5,
                fontweight="bold", color=cols[i])
    ax.axhline(3028, color=P["rojo"], lw=2.2, ls="--")
    ax.text(2.42, 3160, "PRECIO HOY\nC$3.028", fontsize=8.8, color=P["rojo"], fontweight="bold", ha="right")
    ax.set_xticks(range(3)); ax.set_xticklabels(esc, fontsize=8.6)
    ax.set_ylim(0, 7400); ax.set_ylabel("valor por acción (C$)")
    ax.text(1, 250, "Este BASE usa el WACC más barato de los dos que\nel propio documento calculó — ver gráfico siguiente",
            ha="center", fontsize=7.8, color="white", style="italic", fontweight="bold")
    fig.subplots_adjust(top=.76, bottom=.15, left=.08)
    deco(ax, "Rango deliberadamente amplio: spread r-g de apenas ~4 puntos",
         "DCF explícito a 10 años, owner earnings = FCFA2S TTM jun-2026 ≈US$2.030M. Cifras del Paso 9 del monólogo fuente.",
         "Fuente: monólogo evidenciado CSU.TO, Paso 9 (2026-09-04). Un solo número aquí sería falsa precisión.", fig)
    save(fig, "01_dcf_escenarios")

# ── 02 · El recálculo del Golpe 3: BASE a la banda de prudencia ─────────
def c02():
    fig, ax = plt.subplots(figsize=(11.2, 4.8))
    cat = ["r=7,5%\ng term.=2,0%", "r=7,5%\ng term.=3,0%", "r=8,0%\ng term.=2,5%\n(centro de banda)",
           "r=8,5%\ng term.=2,0%", "r=8,5%\ng term.=3,0%"]
    pct = [-5.0, 8.6, -8.2, -19.9, -11.3]
    cols = [P["verde"] if v > 0 else P["rojo_oscuro"] for v in pct]
    x = np.arange(5)
    ax.bar(x, pct, color=cols, width=.55)
    for i, v in enumerate(pct):
        ax.text(i, v + (0.9 if v > 0 else -1.6), f"{v:+.1f}%".replace(".", ","), ha="center",
                fontsize=10.5, fontweight="bold", color=cols[i])
    ax.axhline(0, color=P["tinta"], lw=1.1)
    ax.axhline(-28.9, color=P["vino"], lw=2, ls=":")
    ax.text(4.35, -27.2, "BAJISTA (sin cambios): −28,9%", fontsize=8.4, color=P["vino"],
            fontweight="bold", ha="right")
    ax.set_xticks(x); ax.set_xticklabels(cat, fontsize=8.2)
    ax.set_ylim(-32, 13); ax.set_ylabel("% frente al precio actual (C$3.028)")
    fig.subplots_adjust(top=.76, bottom=.15, left=.08)
    deco(ax, "A la banda de prudencia que el propio documento defendió, el upside se comprime a un dígito o desaparece",
         "Recálculo del Paso 10 (Golpe 3): mismo modelo, WACC 7,5-8,5% en vez de 7,0%, sendero 5/4/3% (reversión a la media) en vez de 9/6/4%.",
         "Fuente: monólogo evidenciado CSU.TO, Paso 10, recálculo cuantitativo (2026-09-04). La cifra '1,64:1' del Paso 9 queda retractada.", fig)
    save(fig, "02_sensibilidad_wacc")

# ── 03 · DCF inverso: qué crecimiento exige hoy el precio ───────────────
def c03():
    fig, ax = plt.subplots(figsize=(11.2, 4.7))
    r = np.array([7.0, 8.0, 9.0])
    g = np.array([1.5, 4.3, 6.75])
    ax.axhspan(4, 10, color=P["azul_cielo"], alpha=.28)
    ax.text(7.05, 9.3, "banda de g razonable para owner earnings\nsegún el motor de reinversión (Paso 5): 4%-10%",
            fontsize=8.0, color=P["azul_noche"], fontweight="bold")
    ax.plot(r, g, "-o", color=P["azul"], lw=2.6, ms=9)
    etiquetas_g = ["≈1,5%", "≈4,3%", "≈6,7-6,8%"]
    for x, y, lab in zip(r, g, etiquetas_g):
        ax.text(x, y + .45, lab, ha="center", fontsize=9.5, fontweight="bold", color=P["azul_noche"])
    ax.axvspan(7.5, 8.5, color=P["ocre"], alpha=.22)
    ax.text(8.0, 0.2, "banda de\nprudencia\n(7,5%-8,5%)", ha="center", fontsize=8.0, color="#8a6508", fontweight="bold")
    ax.annotate("interpolado: g≈3-4,5%\nno heroico frente a la banda del\nPaso 5, tampoco evidentemente barato",
                (8.0, 3.9), (8.55, 1.1), fontsize=8.2, color=P["rojo_oscuro"], fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=P["rojo_oscuro"], lw=1.4))
    ax.set_xlim(6.6, 9.4); ax.set_ylim(0, 11)
    ax.set_xlabel("r asumido (%)"); ax.set_ylabel("g implícita a 10 años exigida por el precio real (%)")
    fig.subplots_adjust(top=.76, bottom=.13, left=.08)
    deco(ax, "El mercado ya paga por una desaceleración moderada, no por un colapso",
         "DCF inverso (protocolo Rappaport-Mauboussin) resolviendo para g al precio real de C$3.028.",
         "Fuente: monólogo evidenciado CSU.TO, Paso 9, tabla de DCF inverso (2026-09-04).", fig)
    save(fig, "03_dcf_inverso")

# ── 04 · De-rating sectorial: ¿idiosincrático o de todo el complejo? ────
def c04():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.6), gridspec_kw={"width_ratios": [1.55, 1]})
    nom = ["CSU", "Roper", "OpenText", "Descartes", "Topicus.com", "Lumine Group"]
    val = [-34.6, -22.5, -38.1, -27.8, -44.5, -53.6]
    cols = [P["rojo"] if n == "CSU" else P["azul_acero"] for n in nom]
    y = np.arange(len(nom))
    a1.barh(y, val, color=cols, height=.6)
    for i, v in enumerate(val):
        a1.text(v - 1.6, i, f"{v:.1f}%".replace(".", ","), va="center", ha="right", fontsize=9.5,
                fontweight="bold", color=cols[i])
    a1.set_yticks(y); a1.set_yticklabels(nom, fontsize=9.2)
    a1.set_xlim(-63, 2); a1.set_xlabel("caída desde máximo de 52 semanas (%)")
    a1.invert_yaxis()
    a1.set_title("El drawdown, complejo completo", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)

    cat = ["EV/FCFA2S\nCSU (hoy)", "EV/comparable\nRoper (histórico\naños fuertes)"]
    lo = [23.5, 25]; hi = [23.5, 30]
    for i, (l, h) in enumerate(zip(lo, hi)):
        if l == h:
            a2.scatter([i], [l], s=140, color=P["azul"], zorder=5)
            a2.text(i, h + 1.6, f"{l:.1f}x".replace(".", ","), ha="center", fontsize=9.5,
                    fontweight="bold", color=P["azul_noche"])
        else:
            a2.plot([i, i], [l, h], color=P["gris_medio"], lw=7, solid_capstyle="butt")
            a2.text(i, h + 1.6, f"{l:.0f}-{h:.0f}x", ha="center", fontsize=9.5,
                    fontweight="bold", color=P["azul_noche"])
    a2.set_xticks(range(2)); a2.set_xticklabels(cat, fontsize=8.4)
    a2.set_ylim(0, 34); a2.set_ylabel("múltiplo (x)")
    a2.set_title("El múltiplo, en contexto", fontsize=9.6, fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=.74, bottom=.13, wspace=.32, left=.13, right=.97)
    deco([a1, a2], "CSU cayó dentro del rango del complejo, ni el más ni el menos golpeado",
         "Candado C: esto es contexto de industria, no un ranking contra otras candidatas de cartera.",
         "Fuente: monólogo evidenciado CSU.TO, Paso 9 (IBKR, 4-sep-2026, desde máximo de 52 semanas; EV/FCFA2S cálculo propio).", fig)
    save(fig, "04_derating_pares")

# ── 05 · El motor de reinversión: ritmo de M&A y retorno incremental ────
def c05():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.2, 4.6))
    an1 = ["2021", "2022", "2023", "2024", "2025", "H1-2026\n(corr.)"]
    ratio = [1.39, 1.91, 1.39, 0.91, 0.73, 1.4]
    cols1 = [P["azul"] if v <= 1.0 else P["terracota"] for v in ratio]
    a1.bar(range(6), ratio, color=cols1, width=.6)
    for i, v in enumerate(ratio):
        dy = .10 if abs(v - 1.0) > 0.08 else .16
        a1.text(i, v + dy, f"{v:.2f}x".replace(".", ","), ha="center", fontsize=8.6, fontweight="bold")
    a1.axhline(1.0, color=P["rojo"], lw=1.6, ls="--")
    a1.text(0.0, 1.05, "100% de FCFA2S", fontsize=7.4, color=P["rojo"], fontweight="bold")
    a1.set_xticks(range(6)); a1.set_xticklabels(an1, fontsize=7.8); a1.set_ylim(0, 2.15)
    a1.set_ylabel("M&A(caja) / FCFA2S")
    a1.set_title("Ritmo de reinversión: 3 de 6 años/semestres\nsuperó el 100% de la caja retenida", fontsize=8.8,
                 fontweight="bold", color=P["azul_noche"], pad=8)

    an2 = ["2022*", "2023", "2024", "2025"]
    roic = [-11.2, 19.6, 18.6, 32.7]
    cols2 = [P["gris_medio"], P["azul"], P["azul"], P["azul"]]
    a2.bar(range(4), roic, color=cols2, width=.55)
    for i, v in enumerate(roic):
        a2.text(i, v + (1.3 if v > 0 else -2.6), f"{v:+.1f}%".replace(".", ","), ha="center",
                fontsize=9, fontweight="bold")
    a2.axhline(0, color=P["tinta"], lw=1)
    a2.set_xticks(range(4)); a2.set_xticklabels(an2, fontsize=8.4); a2.set_ylim(-16, 40)
    a2.set_ylabel("ROIC incremental (base EBIT, %)")
    a2.set_title("*2022 distorsionado por Altera —\nbanda limpia 2023-2025: ~15-35%", fontsize=8.8,
                 fontweight="bold", color=P["azul_noche"], pad=8)
    fig.subplots_adjust(top=.72, bottom=.13, wspace=.28, left=.08, right=.97)
    deco([a1, a2], "El motor sigue desplegando capital rápido, con retorno amplio pero método-dependiente",
         "g = tasa de reinversión × ROIC incremental. Serie de ROIC 2015-2025 por añada NO reconstruida — laguna declarada del Paso 10.",
         "Fuente: monólogo evidenciado CSU.TO, Paso 5 (INFERENCIA propia sobre HECHOs degradados por falta de re-cruce, 2026-09-04).", fig)
    save(fig, "05_motor_reinversion")

# ── 06 · WACC: del cálculo mecánico a la banda de prudencia ─────────────
def c06():
    fig, ax = plt.subplots(figsize=(11.2, 4.4))
    filas = [
        ("Ke (coste de\nequity, CAPM)", 6.7, 7.3, P["azul_acero"]),
        ("Kd post-tax\n(~26,5%)", 3.9, 4.8, P["azul_acero"]),
        ("WACC bottom-up\nmecánico", 6.6, 7.1, P["azul"]),
        ("Banda ajustada\npor prudencia", 7.5, 8.5, P["rojo_oscuro"]),
    ]
    y = np.arange(len(filas))[::-1]
    for i, (nom, lo, hi, col) in zip(y, filas):
        ax.plot([lo, hi], [i, i], color=col, lw=7, solid_capstyle="butt", alpha=.85)
        ax.text((lo + hi) / 2, i + .28, f"{lo:.1f}%-{hi:.1f}%".replace(".", ","), ha="center",
                fontsize=9, fontweight="bold", color=col)
    ax.axvline(6.85, color=P["azul"], lw=1.4, ls=":")
    ax.text(6.85, -0.75, "centro mecánico\n~6,8-6,9%", ha="center", fontsize=7.6, color=P["azul"], fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels([f[0] for f in filas], fontsize=9)
    ax.set_xlim(3.2, 9.3); ax.set_ylim(-1.3, 3.7)
    ax.set_xlabel("% anual")
    fig.subplots_adjust(top=.76, bottom=.14, left=.19, right=.97)
    deco(ax, "Este documento se ancla en la banda de prudencia, no en el punto CAPM mecánico",
         "Rf=3,79% (Banco de Canadá, 10 años) + ERP 4,2-5,0% × beta 0,69-0,70. El mecánico probablemente subestima el riesgo prospectivo.",
         "Fuente: monólogo evidenciado CSU.TO, Paso 9 (Banco de Canadá, Damodaran, stockanalysis.com, Yahoo Finance CA — todos 3/4-sep-2026).", fig)
    save(fig, "06_wacc_bottomup")

for f in [c01, c02, c03, c04, c05, c06]:
    f(); print("ok", f.__name__)
