# -*- coding: utf-8 -*-
"""Grafico titular: lo que el precio EXIGE frente a lo que el filing EVIDENCIA."""
import json, os
import chart_style  # noqa: F401  (aplica rcParams de la casa)
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
D = json.load(open(os.path.join(BASE, 'Valor_Intrinseco_v3_36.json')))
F = [f for f in D['filas'] if f.get('exige') is not None and f.get('evidenciado') is not None]
F.sort(key=lambda z: (z['exige'] - z['evidenciado']))

COL = {'DESCUENTO CLARO': '#2C6B52', 'PRECIO JUSTO': '#A66A00', 'PRIMA': '#A33A1F', 'NO DECIDIBLE': '#6B7680'}
y = np.arange(len(F))
ex = np.array([f['exige'] * 100 for f in F])
ev = np.array([f['evidenciado'] * 100 for f in F])

fig, ax = plt.subplots(figsize=(10.4, max(4.2, 0.30 * len(F) + 2.2)))
for i, f in enumerate(F):
    ax.plot([ev[i], ex[i]], [i, i], color=COL.get(f['cubo'], '#6B7680'), lw=2.1, alpha=.55, zorder=1,
            solid_capstyle='round')
ax.scatter(ev, y, s=34, color='#1F4E79', zorder=3, label='Evidenciado en filing')
ax.scatter(ex, y, s=44, color=[COL.get(f['cubo'], '#6B7680') for f in F], zorder=3,
           label='Exigido por el precio de hoy')
ax.set_yticks(y); ax.set_yticklabels([f['ticker'] for f in F], fontsize=7.6)
ax.set_xlabel('CAGR de owner earnings a 10 años, %', fontsize=8.4)
ax.axvline(0, color='#BFC7C1', lw=.8)
ax.set_title('Lo que el precio exige frente a lo que el filing evidencia',
             fontsize=12.5, loc='left', pad=24)
ax.text(0, 1.006, 'Cada línea es la brecha. Cuanto más larga, más tiene que pasar para que el precio de hoy tenga razón.',
        transform=ax.transAxes, fontsize=8.4, color='#6B7680', style='italic')
ax.legend(loc='lower right', fontsize=7.8, frameon=False)
ax.grid(axis='x', lw=.5, alpha=.35); ax.set_axisbelow(True)
for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
ax.invert_yaxis()
plt.tight_layout()
out = os.path.join(HERE, 'charts', 'exige_vs_evidencia.png')
plt.savefig(out, dpi=150); print('chart ->', out)
