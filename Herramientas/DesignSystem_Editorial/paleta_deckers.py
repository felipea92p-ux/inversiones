# -*- coding: utf-8 -*-
"""Paleta 'editorial cálida' — inspirada en el informe de referencia de Deckers Brands.
Portada oscura con degradado cálido, interior color crema, acento terracota.
Prueba para ESLOY únicamente (no reemplaza paleta_qg.py del canon Economist)."""

PALETA = {
    "fondo":        "#F7F4EF",  # crema cálido, interior
    "panel":        "#EDE7DD",  # cajas de acento, filas alternas
    "fondo_osc1":   "#181210",  # portada — esquina superior (casi negro cálido)
    "fondo_osc2":   "#2E2119",  # portada — degradado hacia esta esquina

    "terracota":        "#D97757",  # acento principal — firma visual
    "terracota_oscuro": "#B85C3E",  # texto sobre claro, énfasis fuerte
    "terracota_claro":  "#E8A489",  # relleno suave (barras secundarias, halos)

    "gris_grafico": "#C7C0B4",  # barra secundaria neutra
    "azul_grafico": "#7B99B8",  # tercera serie
    "verde_acento": "#8A9B72",  # cuarta serie / positivo

    "tinta":       "#262220",  # texto principal
    "gris":        "#7A756C",  # texto secundario, captions
    "gris_claro":  "#9C968B",  # etiquetas suaves
    "gris_linea":  "#D8D2C5",  # separadores, cuadrícula
    "blanco":      "#FFFFFF",
    "negro_tabla": "#1A1613",  # cabecera de tabla
}

ORDEN_SERIES = ["terracota", "gris_grafico", "azul_grafico", "verde_acento"]

if __name__ == "__main__":
    for k, v in PALETA.items():
        print(f"{k:16s} {v}")
