# -*- coding: utf-8 -*-
"""Charts for the dual QG ranking (Economist palette). Self-contained.
All functions write a PNG into OUT and return its path."""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams["text.parse_math"] = False  # avoid $ activating math mode

import sys
BASE = "/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/INVESTMENTS"
sys.path.insert(0, BASE + "/_Ultra Tesis")
from paleta_qg import PALETA as P

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'figure.facecolor': P['fondo'], 'axes.facecolor': P['fondo'],
    'savefig.facecolor': P['fondo'], 'text.color': P['tinta'],
    'axes.edgecolor': P['tinta'], 'xtick.color': P['gris'],
    'ytick.color': P['tinta'], 'font.size': 9,
})

OUT = BASE + "/_ACTIVE/qg_ranking/charts"
os.makedirs(OUT, exist_ok=True)


def _flag_title(fig, title, sub=''):
    fig.patches.append(plt.Rectangle((0.045, 0.94), 0.035, 0.022,
                       transform=fig.transFigure, color=P['rojo'], zorder=5))
    fig.text(0.09, 0.945, title, fontsize=12.5, fontweight='bold', color=P['tinta'])
    if sub:
        fig.text(0.09, 0.912, sub, fontsize=8.5, style='italic', color=P['gris'])


def _source(fig, txt):
    fig.text(0.045, 0.02, txt, fontsize=7, style='italic', color=P['gris_medio'])


def _clean(ax, xgrid=True):
    for s in ['top', 'right', 'left']:
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(P['gris_linea'])
    ax.tick_params(length=0)
    if xgrid:
        ax.xaxis.grid(True, color=P['gris_linea'], lw=0.6); ax.set_axisbelow(True)
    else:
        ax.yaxis.grid(True, color=P['gris_linea'], lw=0.6); ax.set_axisbelow(True)


def chart_funnel(stages, fname='c_funnel.png'):
    """stages = [(label, count), ...] from widest to narrowest."""
    fig, ax = plt.subplots(figsize=(7.3, 4.6))
    fig.subplots_adjust(left=0.04, right=0.96, top=0.84, bottom=0.06)
    n = len(stages)
    maxc = max(c for _, c in stages)
    cols = [P['azul_noche'], P['azul'], P['azul_acero'], P['verde'], P['ocre']]
    for i, (lab, cnt) in enumerate(stages):
        w = cnt / maxc
        y = n - 1 - i
        ax.barh(y, w, left=(1 - w) / 2, height=0.74, color=cols[i % len(cols)], zorder=3)
        if w >= 0.32:  # label fits inside the bar
            ax.text(0.5, y, f"{lab}: {cnt}", ha='center', va='center',
                    fontsize=11, fontweight='bold', color=P['fondo'], zorder=4)
        else:  # narrow bar: label to the right in dark ink
            ax.text((1 + w) / 2 + 0.015, y, f"{lab}: {cnt}", ha='left', va='center',
                    fontsize=10.5, fontweight='bold', color=P['tinta'], zorder=4)
    ax.set_xlim(0, 1); ax.set_ylim(-0.6, n - 0.4)
    ax.axis('off')
    _flag_title(fig, 'El embudo de seleccion', 'Descubrimiento sistematico: el universo se filtra, no se asume')
    _source(fig, 'Fuente: FASE 0 screening cuantitativo + FASE 1-3 scoring y verificacion · junio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_qv_map(rows, fname='c_qvmap.png'):
    """rows = [(ticker, qg_score, mos_pct, lista)]  lista in {'A','B','AB'}."""
    fig, ax = plt.subplots(figsize=(7.3, 6.0))
    fig.subplots_adjust(left=0.09, right=0.97, top=0.86, bottom=0.10)
    xs = [r[2] for r in rows]
    xlim = max(35, max(abs(v) for v in xs) + 10)
    # "joya" zone: quality>=12.5 AND MoS>=20
    ax.axhspan(12.5, 13.7, xmin=(20 + xlim) / (2 * xlim), xmax=1.0,
               color=P['verde'], alpha=0.13, zorder=0)
    ax.axvline(0, color=P['gris_medio'], lw=0.9, ls='--')
    ax.axhline(12.0, color=P['rojo'], lw=1.0, ls='--')
    ax.text(-xlim * 0.97, 12.05, ' piso de calidad 12.0', color=P['rojo'], fontsize=7, va='bottom')
    col = {'A': P['azul'], 'B': P['verde'], 'AB': P['rojo']}
    for tk, qg, ms, lista in rows:
        c = col.get(lista, P['ocre'])
        ax.scatter(ms, qg, s=66, color=c, zorder=3, edgecolor=P['fondo'], lw=0.8)
        ax.text(ms + 0.6, qg + 0.03, tk, fontsize=6.4, color=P['tinta'], zorder=4)
    ax.set_xlim(-xlim, xlim); ax.set_ylim(11.7, 13.7)
    ax.set_xlabel('Margen de seguridad vs DCF propio (%)', fontsize=8.5, color=P['gris'])
    ax.set_ylabel('Calidad - score Seilern / 13.5', fontsize=8.5, color=P['gris'])
    ax.text(xlim * 0.96, 13.6, 'la joya: calidad alta + barata', ha='right',
            fontsize=7.5, color=P['verde'], style='italic')
    _clean(ax, xgrid=False)
    ax.xaxis.grid(True, color=P['gris_linea'], lw=0.6)
    # legend
    from matplotlib.lines import Line2D
    leg = [Line2D([0], [0], marker='o', color='w', markerfacecolor=P['azul'], label='Lista A', markersize=8),
           Line2D([0], [0], marker='o', color='w', markerfacecolor=P['verde'], label='Lista B', markersize=8),
           Line2D([0], [0], marker='o', color='w', markerfacecolor=P['rojo'], label='En ambas', markersize=8)]
    ax.legend(handles=leg, loc='lower left', frameon=False, fontsize=7.5)
    _flag_title(fig, 'El mapa del territorio', 'Calidad vs margen de seguridad de las 30 finalistas')
    _source(fig, 'Fuente: re-score Seilern verificado + DCF owner-earnings propio · junio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_lista_a(rows, fname='c_listaA.png'):
    """rows = [(ticker, qg_score)] -> horizontal bars by quality."""
    rows = sorted(rows, key=lambda r: r[1])
    tk = [r[0] for r in rows]; sc = [r[1] for r in rows]
    fig, ax = plt.subplots(figsize=(7.3, 7.4))
    fig.subplots_adjust(left=0.16, right=0.95, top=0.90, bottom=0.06)
    cols = [P['azul'] if s >= 13.0 else (P['azul_acero'] if s >= 12.5 else P['ocre']) for s in sc]
    ax.barh(tk, sc, color=cols, height=0.66)
    for i, s in enumerate(sc):
        ax.text(s + 0.03, i, f'{s:.1f}'.replace('.', ','), va='center', ha='left',
                fontsize=8, fontweight='bold', color=P['tinta'])
    ax.set_xlim(11.5, 13.8)
    _clean(ax, xgrid=True)
    ax.tick_params(axis='y', labelsize=7.5)
    _flag_title(fig, 'Lista A - 18 Ultra Monstruosas', 'Ordenadas por calidad pura (Seilern /13.5)')
    _source(fig, 'Fuente: re-score Seilern verificado · junio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_lista_b(rows, fname='c_listaB.png'):
    """rows = [(ticker, mos_pct, qg_score)] -> bars by MoS, colored by quality."""
    rows = sorted(rows, key=lambda r: r[1])
    tk = [r[0] for r in rows]; ms = [r[1] for r in rows]; q = [r[2] for r in rows]
    fig, ax = plt.subplots(figsize=(7.3, 6.4))
    fig.subplots_adjust(left=0.16, right=0.93, top=0.90, bottom=0.07)
    cols = [P['verde'] if qq >= 13.0 else (P['azul'] if qq >= 12.5 else P['azul_acero']) for qq in q]
    ax.barh(tk, ms, color=cols, height=0.66)
    ax.axvline(0, color=P['tinta'], lw=1.0)
    ax.axvline(20, color=P['rojo'], lw=1.0, ls='--')
    ax.text(20, len(tk) - 0.4, ' ganga fuerte >=20%', color=P['rojo'], fontsize=7, va='center')
    for i, v in enumerate(ms):
        ax.text(v + 0.8, i, f'{v:+.0f}%', va='center', ha='left', fontsize=8,
                fontweight='bold', color=P['tinta'])
    ax.set_xlim(min(0, min(ms) - 5), max(ms) + 12)
    _clean(ax, xgrid=True)
    ax.tick_params(axis='y', labelsize=7.5)
    _flag_title(fig, 'Lista B - 12 Mas Infravaloradas', 'Ordenadas por margen de seguridad · color = nivel de calidad')
    _source(fig, 'Fuente: DCF owner-earnings propio vs precio jun-2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_convergence(rows, fname='c_converg.png'):
    """rows = [(ticker, prev_pe, live_pe)] grouped bars previous vs verified."""
    import numpy as np
    tk = [r[0] for r in rows]; prev = [r[1] for r in rows]; live = [r[2] for r in rows]
    x = np.arange(len(tk)); w = 0.38
    fig, ax = plt.subplots(figsize=(7.3, 4.8))
    fig.subplots_adjust(left=0.08, right=0.96, top=0.86, bottom=0.12)
    ax.bar(x - w / 2, prev, w, color=P['azul_acero'], label='Estimacion previa')
    ax.bar(x + w / 2, live, w, color=P['rojo'], label='Verificado en vivo')
    ax.set_xticks(x); ax.set_xticklabels(tk, fontsize=8)
    for xi, v in zip(x - w / 2, prev):
        ax.text(xi, v + 0.3, f'{v:.0f}', ha='center', fontsize=7, color=P['gris'])
    for xi, v in zip(x + w / 2, live):
        ax.text(xi, v + 0.3, f'{v:.0f}', ha='center', fontsize=7, fontweight='bold', color=P['rojo'])
    ax.legend(frameon=False, fontsize=8, loc='upper right')
    _clean(ax, xgrid=False)
    ax.set_ylabel('P/E adelantado', fontsize=8.5, color=P['gris'])
    _flag_title(fig, 'La prueba de convergencia', 'P/E adelantado: estimacion previa vs verificado junio 2026')
    _source(fig, 'Fuente: tabla de calibracion del prompt vs verificacion en vivo')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_qv_map_v2(rows, fname='c_qvmap.png'):
    """rows = [(ticker, score_100, mos_pct, lista)] — escala /100."""
    fig, ax = plt.subplots(figsize=(7.3, 6.0))
    fig.subplots_adjust(left=0.09, right=0.97, top=0.86, bottom=0.10)
    xs = [r[2] for r in rows]
    xlim = max(60, max(abs(v) for v in xs) + 10)
    ax.axhspan(78, 92, xmin=(25 + xlim) / (2 * xlim), xmax=1.0,
               color=P['verde'], alpha=0.13, zorder=0)
    ax.axvline(0, color=P['gris_medio'], lw=0.9, ls='--')
    ax.axhline(75.0, color=P['rojo'], lw=1.0, ls='--')
    ax.axhline(85.0, color=P['azul'], lw=0.8, ls=':')
    ax.text(-xlim * 0.97, 75.4, ' Alta conviccion >=75', color=P['rojo'], fontsize=7, va='bottom')
    ax.text(-xlim * 0.97, 85.4, ' Nucleo QG >=85', color=P['azul'], fontsize=7, va='bottom')
    col = {'A': P['azul'], 'B': P['verde'], 'AB': P['rojo']}
    for tk, qg, ms, lista in rows:
        c = col.get(lista, P['ocre'])
        ax.scatter(ms, qg, s=66, color=c, zorder=3, edgecolor=P['fondo'], lw=0.8)
        ax.text(ms + 0.6, qg + 0.2, tk, fontsize=6.4, color=P['tinta'], zorder=4)
    ax.set_xlim(-xlim, xlim); ax.set_ylim(60, 92)
    ax.set_xlabel('Margen de seguridad PWFV-Valor v2 (%)', fontsize=8.5, color=P['gris'])
    ax.set_ylabel('Calidad QG Seilern /100', fontsize=8.5, color=P['gris'])
    ax.text(xlim * 0.96, 90, 'la joya: calidad alta + barata', ha='right',
            fontsize=7.5, color=P['verde'], style='italic')
    _clean(ax, xgrid=False)
    ax.xaxis.grid(True, color=P['gris_linea'], lw=0.6)
    from matplotlib.lines import Line2D
    leg = [Line2D([0], [0], marker='o', color='w', markerfacecolor=P['azul'], label='Lista A', markersize=8),
           Line2D([0], [0], marker='o', color='w', markerfacecolor=P['verde'], label='Lista B', markersize=8),
           Line2D([0], [0], marker='o', color='w', markerfacecolor=P['rojo'], label='En ambas', markersize=8)]
    ax.legend(handles=leg, loc='lower left', frameon=False, fontsize=7.5)
    _flag_title(fig, 'El mapa del territorio v2', 'Calidad /100 vs margen de seguridad PWFV-Valor v2')
    _source(fig, 'Fuente: qg-seilern v2 /100 + PWFV-Valor v2 (val-mos skill) · julio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_lista_a_v2(rows, fname='c_listaA.png'):
    """rows = [(ticker, score_100, tier)] — escala /100."""
    rows = sorted(rows, key=lambda r: r[1])
    tk = [r[0] for r in rows]; sc = [r[1] for r in rows]; tiers = [r[2] for r in rows]
    fig, ax = plt.subplots(figsize=(7.3, 7.4))
    fig.subplots_adjust(left=0.17, right=0.95, top=0.90, bottom=0.06)
    tier_colors = {'Nucleo QG': P['azul'], 'Alta conviccion': P['azul_acero'], 'Calidad solida': P['ocre']}
    cols = [tier_colors.get(t, P['ocre']) for t in tiers]
    ax.barh(tk, sc, color=cols, height=0.66)
    ax.axvline(85, color=P['azul'], lw=1.0, ls=':', alpha=0.7)
    ax.axvline(75, color=P['rojo'], lw=1.0, ls='--', alpha=0.5)
    ax.text(85.1, -0.6, 'Nucleo', color=P['azul'], fontsize=7)
    ax.text(75.1, -0.6, 'Alta conv.', color=P['rojo'], fontsize=7)
    for i, s in enumerate(sc):
        ax.text(s + 0.2, i, f'{s:.1f}'.replace('.', ','), va='center', ha='left',
                fontsize=8, fontweight='bold', color=P['tinta'])
    ax.set_xlim(72, 92)
    _clean(ax, xgrid=True)
    ax.tick_params(axis='y', labelsize=7.5)
    _flag_title(fig, 'Lista A - 18 Calidad Maxima', 'Ordenadas por calidad pura (QG Seilern /100)')
    _source(fig, 'Fuente: qg-seilern v2 /100 · julio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_lista_b_v2(rows, fname='c_listaB.png'):
    """rows = [(ticker, mos_pct, score_100)] — coloreado por tier."""
    rows = sorted(rows, key=lambda r: r[1])
    tk = [r[0] for r in rows]; ms = [r[1] for r in rows]; q = [r[2] for r in rows]
    fig, ax = plt.subplots(figsize=(7.3, 5.8))
    fig.subplots_adjust(left=0.16, right=0.93, top=0.90, bottom=0.07)
    cols = [P['verde'] if qq >= 82 else (P['azul'] if qq >= 75 else P['azul_acero']) for qq in q]
    ax.barh(tk, ms, color=cols, height=0.66)
    ax.axvline(0, color=P['tinta'], lw=1.0)
    ax.axvline(35, color=P['rojo'], lw=1.0, ls='--')
    ax.text(35.5, len(tk) - 0.3, 'umbral Solida 35%', color=P['rojo'], fontsize=7, va='center')
    for i, v in enumerate(ms):
        ax.text(v + 0.8, i, f'{v:+.0f}%', va='center', ha='left', fontsize=8,
                fontweight='bold', color=P['tinta'])
    ax.set_xlim(min(0, min(ms) - 5), max(ms) + 15)
    _clean(ax, xgrid=True)
    ax.tick_params(axis='y', labelsize=7.5)
    _flag_title(fig, 'Lista B - 11 Comprables', 'MoS PWFV-Valor v2 · color = tier de calidad')
    _source(fig, 'Fuente: val-mos skill v2 · julio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_mos_vs_old(rows, fname='c_converg.png'):
    """rows = [(ticker, old_mos, new_mos)] — comparativa metodologias."""
    import numpy as np
    tk = [r[0] for r in rows]; old = [r[1] for r in rows]; new = [r[2] for r in rows]
    x = np.arange(len(tk)); w = 0.38
    fig, ax = plt.subplots(figsize=(7.3, 5.0))
    fig.subplots_adjust(left=0.10, right=0.96, top=0.86, bottom=0.12)
    ax.bar(x - w / 2, old, w, color=P['azul_acero'], label='MoS v1 (/13.5, WACC uniforme)')
    ax.bar(x + w / 2, new, w, color=P['verde'], label='MoS v2 (PWFV-Valor, WACC por tier)')
    ax.axhline(0, color=P['tinta'], lw=0.8)
    ax.set_xticks(x); ax.set_xticklabels(tk, fontsize=7.5)
    for xi, v in zip(x - w / 2, old):
        if v is not None:
            ax.text(xi, v + 0.8 if v >= 0 else v - 2.5, f'{v:+.0f}%', ha='center', fontsize=6.5, color=P['gris'])
    for xi, v in zip(x + w / 2, new):
        ax.text(xi, v + 0.8 if v >= 0 else v - 2.5, f'{v:+.0f}%', ha='center', fontsize=6.5,
                fontweight='bold', color=P['verde'])
    ax.legend(frameon=False, fontsize=8, loc='upper right')
    _clean(ax, xgrid=False)
    ax.set_ylabel('Margen de seguridad (%)', fontsize=8.5, color=P['gris'])
    _flag_title(fig, 'Impacto del nuevo sistema de valoracion', 'MoS sistema anterior vs PWFV-Valor v2 (WACC por tier)')
    _source(fig, 'Fuente: val-mos skill v2 · julio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


if __name__ == '__main__':
    chart_funnel([("Universo", 719), ("Screening", 119), ("Long-list", 80), ("Finalistas", 30)])
    chart_qv_map([("MA", 13.5, 18, 'A'), ("SPGI", 13.5, 28, 'AB'), ("WKL", 13.0, 21, 'B'),
                  ("MSFT", 13.5, -5, 'A'), ("ASML", 13.5, -8, 'A')])
    chart_lista_a([("MA", 13.5), ("MSFT", 13.5), ("SPGI", 13.5), ("ISRG", 13.0), ("RACE", 12.5)])
    chart_lista_b([("SPGI", 28, 13.5), ("RACE", 21, 12.5), ("WKL", 21, 13.0), ("MA", 18, 13.5)])
    chart_convergence([("SPGI", 20, 22.8), ("RELX", 17, 20.8), ("MA", 26, 23.9), ("MSCI", 29.7, 29.7)])
    print("ranking charts OK ->", OUT)
