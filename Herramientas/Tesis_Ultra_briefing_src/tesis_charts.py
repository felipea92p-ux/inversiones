# -*- coding: utf-8 -*-
"""Gráficos de la Ultra Tesis · paleta congelada, estilo Economist. Data-driven y defensivo."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
from paleta_qg import PALETA as P
from qg_charts import _source, _clean  # reutiliza helpers y rcParams

OUT = '/tmp/qg_briefing'

def _flag_title(fig, title, sub):
    """Versión con más separación título/subtítulo (robusta para figuras bajas)."""
    fig.patches.append(plt.Rectangle((0.045, 0.945), 0.034, 0.021,
                       transform=fig.transFigure, color=P['rojo'], zorder=5))
    fig.text(0.088, 0.949, title, fontsize=12, fontweight='bold', color=P['tinta'])
    if sub:
        fig.text(0.088, 0.905, sub, fontsize=8.3, style='italic', color=P['gris'])

def _save(fig, fname):
    path = f'{OUT}/{fname}'
    fig.savefig(path, dpi=150); plt.close(fig)
    return path

def _ok(*series):
    return all(s is not None and len(s) > 0 for s in series)

# 01 — RADAR SEILERN ----------------------------------------------------------
def radar_seilern(rules, fname):
    if not rules: return None
    rules = sorted(rules, key=lambda r: r.get('n', 0))
    labels = [f"R{r.get('n','?')}" for r in rules]
    vals = [float(r.get('score', 0)) for r in rules]
    n = len(vals)
    ang = np.linspace(0, 2*np.pi, n, endpoint=False).tolist()
    vals_c = vals + vals[:1]; ang_c = ang + ang[:1]
    fig = plt.figure(figsize=(6.6, 5.6))
    fig.subplots_adjust(top=0.84, bottom=0.06)
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor(P['fondo'])
    ax.plot(ang_c, vals_c, color=P['azul_noche'], lw=1.8)
    ax.fill(ang_c, vals_c, color=P['azul'], alpha=0.25)
    ax.plot(ang_c, [8]*len(ang_c), color=P['rojo'], lw=1.1, ls='--')  # umbral 8
    for a, v in zip(ang, vals):
        col = P['azul_noche'] if v >= 8 else (P['ocre'] if v >= 6 else P['rojo_oscuro'])
        ax.scatter(a, v, color=col, s=34, zorder=5)
    ax.set_xticks(ang); ax.set_xticklabels(labels, fontsize=8, color=P['tinta'])
    ax.set_ylim(0, 10); ax.set_yticks([2,4,6,8,10])
    ax.set_yticklabels(['2','4','6','8','10'], fontsize=6.5, color=P['gris_medio'])
    ax.grid(color=P['gris_linea'], lw=0.5)
    ax.spines['polar'].set_color(P['gris_linea'])
    _flag_title(fig, 'Las 10 reglas de Seilern', 'Score 0-10 por regla · anillo rojo = umbral de calidad (8)')
    _source(fig, 'Fuente: re-puntuación QG de la tesis · R1/R3/R4 pesan 1,5x en el total /13,5')
    return _save(fig, fname)

# 02 — SEGMENTOS (barras apiladas) -------------------------------------------
def segments(years, series, fname):
    if not _ok(years) or not series: return None
    fig, ax = plt.subplots(figsize=(6.6, 3.6)); fig.subplots_adjust(left=0.10, right=0.97, top=0.80, bottom=0.12)
    cols = [P['azul'], P['azul_acero'], P['azul_cielo'], P['verde'], P['terracota'], P['ocre']]
    x = np.arange(len(years)); bottom = np.zeros(len(years))
    for i, s in enumerate(series):
        v = np.array(s.get('values', [0]*len(years))[:len(years)], dtype=float)
        if len(v) < len(years): v = np.pad(v, (0, len(years)-len(v)))
        ax.bar(x, v, bottom=bottom, color=cols[i % len(cols)], label=s.get('name', f'Seg{i}'), width=0.6)
        bottom += v
    ax.set_xticks(x); ax.set_xticklabels([str(y) for y in years], fontsize=8)
    ax.legend(fontsize=6.8, frameon=False, ncol=min(3, len(series)), loc='upper left')
    _clean(ax); _flag_title(fig, 'Ingresos por segmento', 'Mezcla del negocio, últimos años')
    _source(fig, 'Fuente: 10-K / informes de la compañía')
    return _save(fig, fname)

# 03 — MÁRGENES (triple línea) -----------------------------------------------
def margins(years, gross, op, net, fname):
    if not _ok(years): return None
    fig, ax = plt.subplots(figsize=(6.6, 3.6)); fig.subplots_adjust(left=0.09, right=0.90, top=0.80, bottom=0.12)
    x = np.arange(len(years))
    for s, col, lab in [(gross, P['gris'], 'Bruto'), (op, P['azul'], 'Operativo'), (net, P['azul_acero'], 'Neto')]:
        if _ok(s):
            s = list(s)[:len(years)]
            ax.plot(x[:len(s)], s, color=col, lw=1.8, marker='o', ms=3)
            ax.text(x[len(s)-1]+0.05, s[-1], f' {lab} {s[-1]:.0f}%', color=col, fontsize=7.5, va='center')
    ax.set_xticks(x); ax.set_xticklabels([str(y) for y in years], fontsize=8)
    _clean(ax); _flag_title(fig, 'Márgenes a 5 años', 'Bruto, operativo y neto (%)')
    _source(fig, 'Fuente: estados financieros de la compañía')
    return _save(fig, fname)

# 04 — FCF (barras + línea margen) -------------------------------------------
def fcf(years, vals, margin, fname):
    if not _ok(years, vals): return None
    fig, ax = plt.subplots(figsize=(6.6, 3.6)); fig.subplots_adjust(left=0.10, right=0.90, top=0.80, bottom=0.12)
    x = np.arange(len(vals))
    ax.bar(x, vals, color=P['azul'], width=0.6)
    for xi, v in zip(x, vals): ax.text(xi, v, f'{v:,.0f}', ha='center', va='bottom', fontsize=7, color=P['tinta'])
    _clean(ax); ax.set_xticks(x); ax.set_xticklabels([str(y) for y in years[:len(vals)]], fontsize=8)
    if _ok(margin):
        ax2 = ax.twinx(); ax2.plot(x[:len(margin)], margin, color=P['rojo'], lw=1.6, marker='o', ms=3)
        ax2.set_ylim(0, max(margin)*1.5); ax2.tick_params(length=0, labelsize=7, colors=P['rojo'])
        for s in ax2.spines.values(): s.set_visible(False)
    _flag_title(fig, 'Flujo de caja libre', 'FCF anual (barras) y margen FCF (línea roja, %)')
    _source(fig, 'Fuente: estados de flujos de la compañía')
    return _save(fig, fname)

# 08 — DCF 3 ESCENARIOS ------------------------------------------------------
def dcf(scenarios, weighted, price, fname):
    if not scenarios: return None
    names = [(s.get('name','').split('(')[0].strip())[:14] for s in scenarios]
    vals = [float(s.get('value',0)) for s in scenarios]
    def _pct(p):
        if not p: return None
        return p*100 if p <= 1 else p
    probs = [_pct(s.get('prob')) for s in scenarios]
    fig, ax = plt.subplots(figsize=(6.6, 3.9)); fig.subplots_adjust(left=0.09, right=0.97, top=0.80, bottom=0.12)
    cols = []
    for s in scenarios:
        nm = (s.get('name') or '').lower()
        cols.append(P['rojo_oscuro'] if ('baj' in nm or 'pesim' in nm or 'bear' in nm or 'conserv' in nm)
                    else (P['verde'] if ('alci' in nm or 'optim' in nm or 'bull' in nm) else P['azul']))
    x = np.arange(len(vals))
    ax.bar(x, vals, color=cols, width=0.55)
    for xi, v, pr in zip(x, vals, probs):
        lab = f'${v:,.0f}' + (f'\n{pr:.0f}%' if pr else '')
        ax.text(xi, v, lab, ha='center', va='bottom', fontsize=8, fontweight='bold', color=P['tinta'])
    if price: ax.axhline(price, color=P['tinta'], lw=1.1, ls=':'); ax.text(len(vals)-0.4, price, f' precio ${price:,.0f}', fontsize=7.5, color=P['tinta'], va='bottom')
    if weighted: ax.axhline(weighted, color=P['rojo'], lw=1.3); ax.text(0, weighted, f' ponderado ${weighted:,.0f}', fontsize=7.5, color=P['rojo'], va='bottom')
    ax.set_xticks(x); ax.set_xticklabels(names, fontsize=8); ax.set_ylim(0, max(vals+[price or 0])*1.18)
    _clean(ax); _flag_title(fig, 'Valoración DCF · 3 escenarios', 'Valor intrínseco por escenario vs precio y valor ponderado')
    _source(fig, 'Fuente: DCF propio ponderado por probabilidad')
    return _save(fig, fname)

# 09 — ZONAS DE PRECIO -------------------------------------------------------
def pricezones(zones, today, fname):
    if not zones: return None
    order = ['Ganga','Oportunidad','Justo','Caro','Burbuja']
    zcol = {'Ganga': P['verde'], 'Oportunidad': P['azul_acero'], 'Justo': P['ocre'], 'Caro': P['terracota'], 'Burbuja': P['rojo_oscuro']}
    zones = sorted(zones, key=lambda z: z.get('lo', 0))
    fig, ax = plt.subplots(figsize=(6.6, 2.9)); fig.subplots_adjust(left=0.04, right=0.97, top=0.80, bottom=0.24)
    for z in zones:
        lo, hi = z.get('lo',0), z.get('hi',0)
        ax.barh(0, hi-lo, left=lo, color=zcol.get(z.get('zone'), P['gris']), height=0.5)
        ax.text((lo+hi)/2, 0, z.get('zone',''), ha='center', va='center', fontsize=7.5, color=P['fondo'], fontweight='bold')
        ax.text((lo+hi)/2, -0.42, f'${lo:,.0f}', ha='center', fontsize=6.5, color=P['gris'])
    if today:
        ax.plot([today], [0.42], marker='v', color=P['rojo'], ms=11, zorder=5)
        ax.text(today, 0.6, f'HOY ${today:,.0f}', ha='center', fontsize=8, fontweight='bold', color=P['rojo'])
    ax.set_ylim(-0.7, 0.9); ax.set_yticks([]); ax.tick_params(length=0, labelsize=7)
    for s in ax.spines.values(): s.set_visible(False)
    _flag_title(fig, 'Mapa operativo de precio', 'Dónde cotiza hoy dentro de las zonas Ganga -> Burbuja')
    _source(fig, 'Fuente: zonas derivadas del valor intrínseco de la tesis')
    return _save(fig, fname)

# 10 — MÚLTIPLOS vs HISTORIA -------------------------------------------------
def multiples(items, fname):
    if not items: return None
    labels = [m.get('metric','') for m in items]
    cur = [float(m.get('current',0)) for m in items]; hist = [float(m.get('hist_avg',0)) for m in items]
    x = np.arange(len(labels)); w = 0.38
    fig, ax = plt.subplots(figsize=(6.6, 3.5)); fig.subplots_adjust(left=0.08, right=0.97, top=0.80, bottom=0.14)
    ax.bar(x-w/2, cur, w, color=P['azul'], label='Actual')
    ax.bar(x+w/2, hist, w, color=P['gris'], label='Media 10a')
    for xi, v in zip(x-w/2, cur): ax.text(xi, v, f'{v:.0f}', ha='center', va='bottom', fontsize=6.8)
    for xi, v in zip(x+w/2, hist): ax.text(xi, v, f'{v:.0f}', ha='center', va='bottom', fontsize=6.8, color=P['gris'])
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=7.5)
    ax.legend(fontsize=7, frameon=False, loc='upper right')
    _clean(ax); _flag_title(fig, 'Múltiplos: hoy vs su historia', 'Cuán barata cotiza contra su propia media de 10 años')
    _source(fig, 'Fuente: múltiplos de mercado vs media histórica')
    return _save(fig, fname)

# 17 — WACC BUILD ------------------------------------------------------------
def wacc_build(comps, fname):
    if not comps: return None
    labels = [c.get('component','')[:18] for c in comps]; vals = [float(c.get('value',0)) for c in comps]
    fig, ax = plt.subplots(figsize=(6.6, 3.3)); fig.subplots_adjust(left=0.26, right=0.95, top=0.80, bottom=0.12)
    cols = [P['azul']]*len(vals); cols[-1] = P['rojo']
    ax.barh(range(len(vals)), vals, color=cols, height=0.6)
    for i, v in enumerate(vals): ax.text(v, i, f' {v:.1f}', va='center', fontsize=7.5, color=P['tinta'])
    ax.set_yticks(range(len(vals))); ax.set_yticklabels(labels, fontsize=7.5); ax.invert_yaxis()
    _clean(ax, xgrid=True); _flag_title(fig, 'Construcción del WACC', 'Cómo se arma la tasa de descuento (%)')
    _source(fig, 'Fuente: cálculo propio del coste de capital')
    return _save(fig, fname)

# 19 — SENSIBILIDAD (heatmap) ------------------------------------------------
def sensitivity(wacc_axis, tg_axis, grid, fname):
    if not _ok(wacc_axis, tg_axis) or not grid: return None
    grid = np.array(grid, dtype=float)
    cmap = LinearSegmentedColormap.from_list('qg', [P['rojo_oscuro'], P['gris_claro'], P['azul']])
    fig, ax = plt.subplots(figsize=(6.4, 3.8)); fig.subplots_adjust(left=0.12, right=0.99, top=0.80, bottom=0.14)
    im = ax.imshow(grid, cmap=cmap, aspect='auto')
    ax.set_xticks(range(len(tg_axis))); ax.set_xticklabels([f'{t:.1f}%' for t in tg_axis], fontsize=7.5)
    ax.set_yticks(range(len(wacc_axis))); ax.set_yticklabels([f'{w:.1f}%' for w in wacc_axis], fontsize=7.5)
    ax.set_xlabel('Crecimiento terminal', fontsize=8, color=P['gris']); ax.set_ylabel('WACC', fontsize=8, color=P['gris'])
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            ax.text(j, i, f'{grid[i,j]:,.0f}', ha='center', va='center', fontsize=6.5,
                    color=P['fondo'] if grid[i,j] < (grid.min()+grid.max())/2 else P['tinta'])
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    _flag_title(fig, 'Sensibilidad del valor intrínseco', 'Valor por acción según WACC x crecimiento terminal ($)')
    _source(fig, 'Fuente: malla de sensibilidad del DCF')
    return _save(fig, fname)

# 14 — PROYECCIÓN ------------------------------------------------------------
def projection(years, base, bull, bear, fname):
    if not _ok(years, base): return None
    fig, ax = plt.subplots(figsize=(6.6, 3.5)); fig.subplots_adjust(left=0.11, right=0.92, top=0.80, bottom=0.12)
    x = np.arange(len(years))
    for s, col, lab in [(bull, P['verde'], 'Optimista'), (base, P['azul'], 'Base'), (bear, P['rojo_oscuro'], 'Pesimista')]:
        if _ok(s):
            s = list(s)[:len(years)]
            ax.plot(x[:len(s)], s, color=col, lw=1.8, marker='o', ms=3)
            ax.text(x[len(s)-1]+0.05, s[-1], f' {lab}', color=col, fontsize=7.5, va='center')
    ax.set_xticks(x); ax.set_xticklabels([str(y) for y in years], fontsize=8)
    _clean(ax); _flag_title(fig, 'Proyección a 5 años', '$10.000 invertidos hoy, tres escenarios ($)')
    _source(fig, 'Fuente: proyección propia a partir del DCF')
    return _save(fig, fname)

# 20 — EPS -------------------------------------------------------------------
def eps(years, vals, fname):
    if not _ok(years, vals): return None
    fig, ax = plt.subplots(figsize=(6.6, 3.2)); fig.subplots_adjust(left=0.09, right=0.97, top=0.80, bottom=0.12)
    x = np.arange(len(vals))
    ax.bar(x, vals, color=P['azul'], width=0.6)
    for xi, v in zip(x, vals): ax.text(xi, v, f'{v:,.2f}', ha='center', va='bottom', fontsize=7)
    ax.set_xticks(x); ax.set_xticklabels([str(y) for y in years[:len(vals)]], fontsize=8)
    _clean(ax); _flag_title(fig, 'Beneficio por acción', 'BPA diluido, compounding a 5 años ($)')
    _source(fig, 'Fuente: resultados de la compañía')
    return _save(fig, fname)

# 12 — MÉTRICA DE NEGOCIO ----------------------------------------------------
def business_metric(title, unit, years, vals, growth, fname):
    if not _ok(years, vals): return None
    fig, ax = plt.subplots(figsize=(6.6, 3.4)); fig.subplots_adjust(left=0.10, right=0.90, top=0.80, bottom=0.12)
    x = np.arange(len(vals))
    ax.bar(x, vals, color=P['azul'], width=0.6)
    for xi, v in zip(x, vals): ax.text(xi, v, f'{v:,.0f}', ha='center', va='bottom', fontsize=7, color=P['tinta'])
    ax.set_xticks(x); ax.set_xticklabels([str(y) for y in years[:len(vals)]], fontsize=8)
    _clean(ax)
    if _ok(growth):
        ax2 = ax.twinx(); ax2.plot(x[:len(growth)], growth, color=P['rojo'], lw=1.5, marker='o', ms=3)
        ax2.tick_params(length=0, labelsize=7, colors=P['rojo'])
        for s in ax2.spines.values(): s.set_visible(False)
    _flag_title(fig, title or 'Métrica de negocio', f'Trayectoria{(" en "+unit) if unit else ""} (barras) y crecimiento (línea roja, %)')
    _source(fig, 'Fuente: métricas operativas de la compañía')
    return _save(fig, fname)

# 13 — PANEL DE INVERSORES ---------------------------------------------------
def investor_panel(panel, fname):
    if not panel: return None
    vmap = {'COMPRAR FUERTE': 5, 'COMPRAR': 4, 'MANTENER': 3, 'REDUCIR': 2, 'EVITAR': 1}
    cmap = {5: P['azul_noche'], 4: P['azul'], 3: P['ocre'], 2: P['terracota'], 1: P['rojo_oscuro']}
    order = sorted(panel, key=lambda p: vmap.get((p.get('verdict') or '').upper(), 3))
    names = [p.get('investor','').split()[-1] for p in order]
    vals = [vmap.get((p.get('verdict') or '').upper(), 3) for p in order]
    cols = [cmap[v] for v in vals]
    fig, ax = plt.subplots(figsize=(6.6, 4.3)); fig.subplots_adjust(left=0.20, right=0.97, top=0.84, bottom=0.10)
    ax.barh(range(len(vals)), vals, color=cols, height=0.66)
    for i, p in enumerate(order):
        ax.text(0.06, i, f" {(p.get('verdict') or '').upper()}", va='center', ha='left', fontsize=7,
                color=P['fondo'], fontweight='bold')
    ax.set_yticks(range(len(names))); ax.set_yticklabels(names, fontsize=8)
    ax.set_xlim(0, 5.4); ax.set_xticks([1,2,3,4,5])
    ax.set_xticklabels(['Evitar','Reducir','Mantener','Comprar','C. fuerte'], fontsize=6.8)
    _clean(ax, xgrid=True); _flag_title(fig, 'Nueve inversores legendarios opinan', 'La divergencia es la señal, no el consenso')
    _source(fig, 'Fuente: panel simulado según el marco de cada inversor')
    return _save(fig, fname)


if __name__ == '__main__':
    radar_seilern([{'n': i, 'name': f'R{i}', 'score': 6+ (i % 4)} for i in range(1, 11)], '_t_radar.png')
    dcf([{'name': 'Pesimista', 'prob': .25, 'value': 215}, {'name': 'Base', 'prob': .5, 'value': 365}, {'name': 'Optimista', 'prob': .25, 'value': 505}], 353, 195, '_t_dcf.png')
    pricezones([{'zone': 'Ganga', 'lo': 150, 'hi': 230}, {'zone': 'Oportunidad', 'lo': 230, 'hi': 320}, {'zone': 'Justo', 'lo': 320, 'hi': 410}, {'zone': 'Caro', 'lo': 410, 'hi': 480}, {'zone': 'Burbuja', 'lo': 480, 'hi': 560}], 195, '_t_zones.png')
    sensitivity([8.5, 9, 9.5, 10, 10.5], [2, 2.5, 3, 3.5, 4], [[300+10*i+5*j for j in range(5)] for i in range(5)], '_t_sens.png')
    investor_panel([{'investor': 'Warren Buffett', 'verdict': 'COMPRAR'}, {'investor': 'Charlie Munger', 'verdict': 'MANTENER'}, {'investor': 'Peter Seilern', 'verdict': 'REDUCIR'}], '_t_panel.png')
    print('tesis charts OK')
