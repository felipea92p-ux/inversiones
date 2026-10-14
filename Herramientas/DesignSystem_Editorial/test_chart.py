import numpy as np
import matplotlib.pyplot as plt
import chart_style_deckers as CS
from paleta_deckers import PALETA as P

fig, ax = plt.subplots(figsize=(9.6, 4.6))
years = ["2022", "2023", "2024", "2025"]
vals = [4.0, 4.3, 4.6, 3.75]
ax.bar(years, vals, color=P["terracota"], width=0.55, zorder=3)
for i, v in enumerate(vals):
    ax.text(i, v + 0.1, f"{v:.2f}%".replace(".", ","), ha="center", fontsize=10.5,
            fontweight="bold", family="DejaVu Serif", color=P["tinta"])
ax.set_ylim(0, 6)
CS.deco(ax, "Fuente: prueba de motor — ficticio")
fig.subplots_adjust(top=0.92, bottom=0.16)
CS.save(fig, "test_chart", outdir="charts")
print("ok")
