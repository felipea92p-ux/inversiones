# -*- coding: utf-8 -*-
"""Generador de gráficos del briefing · misma paleta, estilo Economist."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from paleta_qg import PALETA as P

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'figure.facecolor': P['fondo'],
    'axes.facecolor': P['fondo'],
    'savefig.facecolor': P['fondo'],
    'text.color': P['tinta'],
    'axes.edgecolor': P['tinta'],
    'xtick.color': P['gris'],
    'ytick.color': P['tinta'],
    'font.size': 9,
})

OUT = '/tmp/qg_briefing'


def _flag_title(fig, title, sub):
    fig.text(0.045, 0.965, '', fontsize=1)
    # flag rojo
    fig.patches.append(plt.Rectangle((0.045, 0.94), 0.035, 0.022,
                       transform=fig.transFigure, color=P['rojo'], zorder=5))
    fig.text(0.09, 0.945, title, fontsize=12.5, fontweight='bold', color=P['tinta'])
    if sub:
        fig.text(0.09, 0.912, sub, fontsize=8.5, style='italic', color=P['gris'])


def _source(fig, txt):
    fig.text(0.045, 0.02, txt, fontsize=7, style='italic', color=P['gris_medio'])


def _clean(ax, xgrid=False):
    for s in ['top', 'right', 'left']:
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(P['gris_linea'])
    ax.tick_params(length=0)
    if xgrid:
        ax.xaxis.grid(True, color=P['gris_linea'], lw=0.6)
        ax.set_axisbelow(True)
    else:
        ax.yaxis.grid(True, color=P['gris_linea'], lw=0.6)
        ax.set_axisbelow(True)


def chart_ranking_qg(rows, fname='c_ranking.png'):
    """rows: list of (ticker, qg_score). Horizontal, sorted asc for display."""
    rows = sorted(rows, key=lambda r: r[1])
    tk = [r[0] for r in rows]; sc = [r[1] for r in rows]
    fig, ax = plt.subplots(figsize=(7.3, 6.2))
    fig.subplots_adjust(left=0.12, right=0.96, top=0.88, bottom=0.10)
    cols = []
    for s in sc:
        if s >= 10.8: cols.append(P['azul'])
        elif s >= 9.0: cols.append(P['azul_acero'])
        elif s >= 7.5: cols.append(P['ocre'])
        else: cols.append(P['rojo_oscuro'])
    ax.barh(tk, sc, color=cols, height=0.66)
    ax.axvline(10.8, color=P['rojo'], lw=1.3, ls='--')
    ax.text(10.8, len(tk) - 0.3, ' umbral núcleo 10.8', color=P['rojo'], fontsize=7.5, va='center')
    for i, s in enumerate(sc):
        ax.text(s + 0.1, i, f'{s:.1f}', va='center', ha='left', fontsize=8, fontweight='bold', color=P['tinta'])
    ax.set_xlim(0, 13.9)
    _clean(ax, xgrid=True)
    _flag_title(fig, 'Ranking de calidad QG', 'Score Seilern ponderado sobre 13.5 · azul = núcleo (≥10.8)')
    _source(fig, 'Fuente: tesis Ultra QG del portafolio · score ponderado R1/R3/R4 ×1.5')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_margin_safety(rows, fname='c_margin.png'):
    """rows: list of (ticker, mos_pct). Diverging bars."""
    rows = sorted(rows, key=lambda r: r[1])
    tk = [r[0] for r in rows]; ms = [r[1] for r in rows]
    fig, ax = plt.subplots(figsize=(7.3, 6.2))
    fig.subplots_adjust(left=0.12, right=0.93, top=0.88, bottom=0.10)
    cols = [P['verde'] if v >= 0 else P['rojo_oscuro'] for v in ms]
    ax.barh(tk, ms, color=cols, height=0.66)
    ax.axvline(0, color=P['tinta'], lw=1.0)
    for i, v in enumerate(ms):
        off = 1.2 if v >= 0 else -1.2
        ha = 'left' if v >= 0 else 'right'
        ax.text(v + off, i, f'{v:+.0f}%', va='center', ha=ha, fontsize=8, fontweight='bold', color=P['tinta'])
    lim = max(40, max(abs(v) for v in ms) + 12)
    ax.set_xlim(-lim, lim)
    _clean(ax, xgrid=True)
    _flag_title(fig, 'Margen de seguridad actual', 'Valor intrínseco vs precio jun-2026 · verde = infravalorada')
    _source(fig, 'Fuente: DCF ponderado de cada tesis vs precio de mercado junio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_quality_value_map(rows, fname='c_qvmap.png'):
    """rows: list of (ticker, qg_score, mos_pct). Scatter quality vs value."""
    fig, ax = plt.subplots(figsize=(7.3, 5.8))
    fig.subplots_adjust(left=0.10, right=0.96, top=0.86, bottom=0.12)
    xs = [r[2] for r in rows]; ys = [r[1] for r in rows]
    xlim = max(40, max(abs(v) for v in xs) + 12)
    # cuadrante "joya": calidad alta + margen positivo
    ax.axhspan(10.8, 14, 0, 1, color=P['gris_claro'], alpha=0.5, zorder=0)
    ax.axvline(0, color=P['gris_medio'], lw=0.8, ls='--')
    ax.axhline(10.8, color=P['rojo'], lw=1.0, ls='--')
    for tk, qg, ms in rows:
        col = P['azul'] if (qg >= 10.8 and ms >= 0) else (P['verde'] if ms >= 10 else (P['rojo_oscuro'] if ms < -10 else P['ocre']))
        ax.scatter(ms, qg, s=70, color=col, zorder=3, edgecolor=P['fondo'], lw=0.8)
        ax.text(ms + 0.8, qg + 0.06, tk, fontsize=7, color=P['tinta'], zorder=4)
    ax.set_xlim(-xlim, xlim); ax.set_ylim(6.5, 13.9)
    ax.set_xlabel('Margen de seguridad (%)', fontsize=8.5, color=P['gris'])
    ax.set_ylabel('Score QG / 13.5', fontsize=8.5, color=P['gris'])
    ax.text(xlim * 0.97, 13.6, 'BARATAS y de calidad', ha='right', fontsize=7.5, color=P['azul'], style='italic')
    ax.text(-xlim * 0.97, 13.6, 'caras pero de calidad', ha='left', fontsize=7.5, color=P['gris'], style='italic')
    _clean(ax, xgrid=False)
    ax.xaxis.grid(True, color=P['gris_linea'], lw=0.6)
    _flag_title(fig, 'Mapa calidad × valor', 'Arriba-derecha = comprar más · arriba-izquierda = mantener, no añadir')
    _source(fig, 'Fuente: síntesis de las tesis Ultra QG · precios junio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_pnl(rows, fname='c_pnl.png'):
    """rows: list of (ticker, pnl_pct)."""
    rows = sorted(rows, key=lambda r: r[1])
    tk = [r[0] for r in rows]; pn = [r[1] for r in rows]
    fig, ax = plt.subplots(figsize=(7.3, 6.2))
    fig.subplots_adjust(left=0.12, right=0.93, top=0.88, bottom=0.10)
    cols = [P['azul'] if v >= 0 else P['rojo_oscuro'] for v in pn]
    ax.barh(tk, pn, color=cols, height=0.66)
    ax.axvline(0, color=P['tinta'], lw=1.0)
    ax.axvline(-20, color=P['rojo'], lw=1.0, ls='--')
    ax.text(-20, len(tk) - 0.4, ' umbral −20% (re-análisis)', color=P['rojo'], fontsize=7, va='center')
    for i, v in enumerate(pn):
        off = 8 if v >= 0 else -8
        ha = 'left' if v >= 0 else 'right'
        ax.text(v + off, i, f'{v:+.0f}%', va='center', ha=ha, fontsize=7.5, fontweight='bold', color=P['tinta'])
    ax.set_xlim(-60, max(pn) + 80)
    _clean(ax, xgrid=True)
    _flag_title(fig, 'P&L por posición', 'Rentabilidad acumulada del usuario · rojo punteado = gatillo de re-análisis')
    _source(fig, 'Fuente: portafolio del usuario a 22 junio 2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


def chart_reanalysis(ticker, current, bear, base, bull, fname=None):
    """Barras: precio actual vs 3 escenarios de valor intrínseco."""
    fname = fname or f'c_re_{ticker}.png'
    fig, ax = plt.subplots(figsize=(3.5, 3.1))
    fig.subplots_adjust(left=0.16, right=0.95, top=0.80, bottom=0.12)
    labels = ['Precio\nhoy', 'DCF\nbajista', 'DCF\nbase', 'DCF\nalcista']
    vals = [current, bear, base, bull]
    cols = [P['tinta'], P['rojo_oscuro'], P['azul'], P['verde']]
    bars = ax.bar(labels, vals, color=cols, width=0.62)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + max(vals) * 0.02, f'${v:.0f}',
                ha='center', va='bottom', fontsize=8, fontweight='bold', color=P['tinta'])
    ax.axhline(current, color=P['tinta'], lw=0.8, ls=':')
    ax.set_ylim(0, max(vals) * 1.18)
    _clean(ax, xgrid=False)
    ax.tick_params(axis='x', labelsize=7.5)
    _flag_title(fig, f'{ticker}: precio vs valor', 'Escenarios DCF de la tesis vs mercado jun-2026')
    fig.savefig(f'{OUT}/{fname}', dpi=150); plt.close(fig)
    return f'{OUT}/{fname}'


if __name__ == '__main__':
    # smoke test
    demo = [('TSM', 12.1, 8), ('GOOGL', 11.8, 22), ('ADBE', 10.2, 35),
            ('DUOL', 9.1, -15), ('INTU', 11.0, 18), ('BABA', 8.4, 30)]
    chart_ranking_qg([(t, q) for t, q, m in demo])
    chart_margin_safety([(t, m) for t, q, m in demo])
    chart_quality_value_map(demo)
    chart_pnl([('TSM', 551), ('ADBE', -25), ('DUOL', -20), ('INTU', -18.6)])
    chart_reanalysis('ADBE', 195, 210, 310, 420)
    print('charts OK')
