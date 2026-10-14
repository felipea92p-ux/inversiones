# -*- coding: utf-8 -*-
"""
═══════════════════════════════════════════════════════════════════
  PALETA OFICIAL · TESIS ULTRA QUALITY GROWTH
  Estilo editorial tipo The Economist
  Extraída pixel-exacta de Tesis_Ultra_ABNB_v1 · v1.0
═══════════════════════════════════════════════════════════════════

  FUENTE ÚNICA DE VERDAD para el color de todas las tesis del portafolio.
  Importar desde aquí en make_charts y en el motor del PDF, para no volver
  a tener el problema del fondo blanco ni del rojo equivocado.

  REGLA DE TEMPERATURA: todos los colores tienen sesgo CÁLIDO
  (grises con tinte marrón, fondo crema, "negro" en realidad #2A2A2A).
  Cualquier color nuevo debe respetar ese sesgo o desentonará.

  REGLA DE JERARQUÍA:
    · UN solo rojo protagonista (carmín)  -> lo que debe captar la atención
    · UN azul de reparto principal (petróleo) -> caballo de batalla de datos
    · El resto (acero, cielo, oliva, terracota, ocre) -> series secundarias
    · Grises cálidos -> todo el texto secundario, en silencio
═══════════════════════════════════════════════════════════════════
"""

PALETA = {
    # — Fondos —
    "fondo":        "#FAF5E9",  # crema cálido — fondo de página Y de gráficos
    "panel":        "#F2ECDC",  # paneles, cajas, filas alternas de tabla

    # — Rojos (acento / firma) —
    "rojo":         "#C60C2A",  # carmín firma — acento principal, flag, líneas clave
    "rojo_oscuro":  "#8C1410",
    "vino":         "#6E1423",  # burdeos profundo — acento sobrio que no grita  # alertas, escenario pesimista

    # — Azules (datos) —
    "azul":         "#2A5A7E",  # petróleo — serie de datos PRINCIPAL
    "azul_noche":   "#1F3A52",  # cabeceras de tabla, titulares oscuros
    "azul_acero":   "#547890",  # segunda serie
    "azul_cielo":   "#8AAEC4",
    "azul_pro":     "#16527A",  # cuarto azul, para 4-5 series juntas  # tercera serie / barras apiladas

    # — Acentos cálidos secundarios —
    "verde":        "#6C7E48",  # oliva — positivo / cuarta serie
    "terracota":    "#C07E66",  # acento cálido secundario
    "ocre":         "#B8860B",  # zona neutral / "mantener"

    # — Texto y grises (todos cálidos) —
    "tinta":        "#2A2A2A",  # texto principal (casi-negro cálido)
    "gris":         "#666054",  # topo — texto secundario, notas al pie
    "gris_medio":   "#847E72",  # etiquetas suaves
    "gris_linea":   "#D2CCC0",  # cuadrícula de gráficos, divisores
    "gris_claro":   "#EAE4D8",  # rellenos sutiles
}

# Orden recomendado para series de datos en gráficos (de mayor a menor protagonismo)
ORDEN_SERIES = ["azul", "azul_acero", "azul_cielo", "verde", "terracota", "ocre"]

# Acceso cómodo como variables sueltas (para los motores que las usan directo)
FONDO       = PALETA["fondo"]
PANEL       = PALETA["panel"]
ROJO        = PALETA["rojo"]
ROJO_OSCURO = PALETA["rojo_oscuro"]
AZUL        = PALETA["azul"]
AZUL_NOCHE  = PALETA["azul_noche"]
AZUL_ACERO  = PALETA["azul_acero"]
AZUL_CIELO  = PALETA["azul_cielo"]
VERDE       = PALETA["verde"]
TERRACOTA   = PALETA["terracota"]
OCRE        = PALETA["ocre"]
TINTA       = PALETA["tinta"]
GRIS        = PALETA["gris"]
GRIS_MEDIO  = PALETA["gris_medio"]
GRIS_LINEA  = PALETA["gris_linea"]
GRIS_CLARO  = PALETA["gris_claro"]

if __name__ == "__main__":
    print("PALETA OFICIAL TESIS ULTRA QG")
    print("=" * 40)
    for nombre, hexv in PALETA.items():
        print(f"  {nombre:14s} {hexv}")
