#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consolida piloto (3) + tanda (33) -> 36 empresas con motor v3.
Produce: Valor_Intrinseco_v3_36.json (para el PDF) y el CSV auditable con TODOS los inputs."""
import json, csv, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def J(p):
    p = os.path.join(BASE, p)
    return json.load(open(p)) if os.path.exists(p) else None

def cargar():
    emp = []
    pil = J('_piloto_v3/piloto_v3_completo.json')
    if pil: emp += pil.get('piloto', [])
    t33 = J('_tanda33_v3/tanda33_v3_completo.json')
    if t33: emp += t33.get('empresas', [])
    return {e['ticker']: e for e in emp}

# ranking de calidad validado (rho=0,969) -> ordinal 1-36
CAL = {}
f36 = J('_trabajo/final36_v2.json')
for x in sorted(f36['filas'], key=lambda z: (z['bloque'], z['orden'])):
    CAL[x['ticker']] = x
ORDINAL = {t: i + 1 for i, t in enumerate(CAL)}

# margenes de seguridad v3.1 (recalibrados por Felipe 26-ago: comprar calidad a precio justo)
MARGEN = {1: 0.09, 2: 0.18, 3: 0.27}

VIEJO = {}
p = os.path.join(BASE, 'Valor_Intrinseco_36_2026-08-26.csv')
for r in csv.DictReader(open(p)):
    VIEJO[r['ticker']] = r

def g(d, *k, default=None):
    for kk in k:
        if not isinstance(d, dict): return default
        d = d.get(kk)
        if d is None: return default
    return d



# ── CANDADO C CALIBRADO (decision de Felipe, 27-ago) ──────────────────
# La caja mecanica de +-2pp disparaba NO DECIDIBLE en 24 de 33. Varios agentes de senda
# demostraron por separado que esa caja es hasta 6x mas ancha que la incertidumbre que el
# agente de TASA midio de verdad, y dejaron la objecion escrita en vez de doblar la porteria.
# REGLA: NO DECIDIBLE solo si cruza DENTRO de la banda de tasa que el propio agente declaro
# defendible. Quien no hizo ese analisis se queda NO DECIDIBLE por defecto (conservador).
CALIBRADO = {
  'MA':      'Cruza solo bajando el WACC 2pp sin bajar g-infinito — incoherente: un rf menor implica PIB nominal menor. Con la perturbacion coherente el cruce desaparece. En la banda medida (8,07-9,68%) no cruza ni una vez.',
  'MSCI':    'El vertice que cruza exige una beta re-apalancada de ~0,26 contra la beta cruda MEDIDA de 1,23. En el rango defendido (8,42-9,51%) el VI no cruza nunca.',
  'SPGI':    'El WACC de indiferencia es 7,25%: 121pb por debajo del SUELO de la banda medida (8,46-9,11%) e implica una prima de equity de 2,81pp para una beta de 0,98. En la caja calibrada la prima nunca baja del 40%.',
  'MCO':     'Cruzan 2 de 9 esquinas, ambas al WACC de 6,42%. Decidible y cara en el rango real de los insumos del agente de tasa.',
  'TRI':     'Cruce solo por el eje WACC a -2pp; el eje de crecimiento no cruza. Dentro de la banda de resolucion real (7,34-8,19%) TRI es cara en los cuatro puntos.',
  'RMS.PA':  'Una sola esquina conjunta y extrema cruza, por un 2,1%. Y exige bajar el WACC 200pb cuando el propio agente de tasa declara que su 9,29% esta, si acaso, 60-190pb DEMASIADO BAJO. El lado que cruza es el implausible.',
  'CPRT':    'El cruce vive FUERA del rango de WACC que la evidencia soporta, y nunca por el eje del crecimiento.',
  'GE':      'Cruza en una sola esquina y por -1,6%.',
  'ISRG':    'Cruza solo en la esquina apilada wacc-2pp + g+2pp; el cruce lo produce la tasa, no el negocio.',
  '7741.T':  'Cruza por una sola esquina, y la evidencia empuja en la direccion contraria.',
}


# ── AUDITORIA ADVERSARIAL DE CAPEX sobre los 7 vuelcos >=x2,5 (27-ago) ──
# Un agente dedicado por caso, con mandato de refutar la separacion mantenimiento/crecimiento.
# Hallazgo sistemico: la formula de owner earnings (NOPAT_norm + D&A - capex_mant - SBC) NO
# descuenta capital circulante permanente ni la inversion que vive fuera de la linea de capex
# (compra de carteras de servicio, incentivos a clientes capitalizados, M&A de reposicion).
# El VI se reescala por el EV: VI = (EV*k - deuda_neta) / acciones, no VI*k.
CAPEX_AUDIT = {
  'UNP':     ( 0.094, 'Capex de mantenimiento SOBREESTIMADO en 430M: normalizo la linea de caja, que incluye lease buyouts anticipados (311M en 2025) que la propia UNP excluye de su programa de capital ("approximately $3.5 billion", 10-K Item 2). Un buyout convierte alquiler en propiedad, es finito y duplica el cargo. Ademas: la separacion declarada NUNCA ENTRO EN LA ARITMETICA — reconstruido, el OE de 6.604 se calculo con el capex TOTAL (3.650), no con el de mantenimiento.'),
  'AZO':     (-0.252, 'El 47,2% de crecimiento es demasiado generoso y esta mal construido en las dos puntas: corregido a 34,3%. Pero la correccion mayor no esta en el capex — son ~475M/ano de inversion economica real fuera de la linea de capex, sobre todo capital circulante permanente (~330M/ano), que la formula no descuenta. Es mantenimiento competitivo: AutoZone abre para no perder cuota frente a ORLY.'),
  '4684.T':  (-0.009, 'Nivel del capex CONFIRMADO (2.435M reconstruido anio a anio de tres filings) y el riesgo imputado ABSUELTO: OBIC no capitaliza nada de desarrollo (activo inmaterial total 152M) ni el capex es colocacion de tesoreria. Pero elimino el 100% del capex de crecimiento: 577 -> 0.'),
  'STMN.SW': (-0.390, 'RECHAZADA por inservible: la base no cuadra (140+135,3=275,3 contra un capex auditado de CHF 223,5M — el agente trabajo en USD sin declararlo). Y omitio entero el capital circulante permanente: CHF 135,6M en 2025, que absorbio el 132% del ingreso incremental. En implantes el inventario ES el foso y no vuelve nunca.'),
  'OTIS':    (-0.330, 'Omitio integramente la compra de CARTERAS DE SERVICIO: 109M en FY2025 y 193M solo en S1-2026, que Otis capitaliza en un intangible llamado literalmente "Purchased service portfolios". No esta en la linea de capex ni en el CFO: vive en Investing. Es exactamente el coste de comprar la anualidad, y 62M/anio son puro reemplazo del intangible que se amortiza.'),
  'V':       (-0.048, 'La separacion 83/17 es irrelevante: en Visa el capex fisico es ruido (3,5% del ingreso). El dinero esta en los INCENTIVOS A CLIENTES — 17.442M de gasto TTM, 11,1 veces la linea de capex entera, contabilizados como MENOR INGRESO. Visa capitaliza los pagos iniciales: el activo paso de 6.546 (sep-24) a 8.407 (jun-26), +1.861M en 21 meses de capital de captacion que ningun estado llama capex. Mas ~836M/anio de M&A de reposicion cuyo 84-85% va a fondo de comercio que jamas se amortiza.'),
  '6861.T':  (-0.079, 'La separacion mira donde no esta el dinero: Keyence es fabless y su capital de verdad no pasa por el activo fijo. La inversion fuera de la linea de capex es 78.921M de yenes = 2,78 VECES la propia linea. La mayor es capital circulante permanente (46.797M), omitida entera. El split se corrige de 39,3% a 16,5% de crecimiento por mantenimiento competitivo. El punto ciego de intangibles x4,6 sigue ABIERTO, no resuelto.'),
}

# ── NORMALIZACION DE ESCALA ──────────────────────────────────────────
# Los agentes mezclaron convenciones: unos devuelven 0,0824 y otros 8,24 para el mismo WACC.
# Sin esto, Constellation sale con un coste de capital del 824%. Umbral por tipo de campo.
UMBRAL = {  # si abs(valor) supera el umbral, el agente lo dio en puntos porcentuales
    'wacc': 1.0, 'rf': 1.0, 'erp': 1.0, 'prima_pais': 1.0, 'coste_equity': 1.0,
    'coste_deuda': 1.0, 'peso_deuda': 1.0, 'g_inf': 1.0, 'margen_norm': 1.0,
    'margen_ult': 1.0, 'exige': 1.0, 'evidenciado': 1.0, 'tir_10a': 1.0,
    'pct_capex_crecimiento': 1.0, 'tam_cuota': 1.0, 'tam_cuota_max': 1.0,
    'roiic_hist': 15.0, 'roiic_implicado': 15.0,   # un ROIIC de 1,62 (NVDA) es legitimo
}
def _esc(fila):
    for k, u in UMBRAL.items():
        v = fila.get(k)
        if isinstance(v, (int, float)) and abs(v) > u:
            fila[k] = v / 100.0
            fila.setdefault('_reescalados', []).append(k)
    # el premio NO se hereda del agente: se recalcula del precio y del VI
    if fila.get('vi_base') and fila.get('precio'):
        fila['premio'] = fila['precio'] / fila['vi_base'] - 1
    # la etiqueta de ruido: varios agentes escribieron un ensayo dentro del campo
    r = str(fila.get('ruido') or 'DECIDIBLE').strip()
    fila['ruido_nota'] = r if len(r) > 22 else ''
    mec = 'NO DECIDIBLE' if r.upper().startswith('NO DECIDIBLE') else 'DECIDIBLE'
    fila['ruido_mecanico'] = mec
    cal = CALIBRADO.get(fila['ticker'])
    if mec == 'NO DECIDIBLE' and cal:
        fila['ruido'] = 'DECIDIBLE'
        fila['ruido_calibrado_motivo'] = cal
    else:
        fila['ruido'] = mec
        fila['ruido_calibrado_motivo'] = ''
    return fila

def cubo(fila):
    """DESCUENTO CLARO / PRECIO JUSTO / PRIMA / NO DECIDIBLE — nunca ordinal (candado C)."""
    if fila['ruido'] == 'NO DECIDIBLE': return 'NO DECIDIBLE'
    vi, px, m = fila['vi_base'], fila['precio'], MARGEN[fila['bloque']]
    if vi is None or not px: return 'NO DECIDIBLE'
    if px <= vi * (1 - m): return 'DESCUENTO CLARO'
    if px <= vi * 1.15:    return 'PRECIO JUSTO'
    return 'PRIMA'

def construir():
    EMP = cargar()
    filas = []
    for t, cal in CAL.items():
        e = EMP.get(t)
        if not e:
            print(f'  AVISO: falta {t}', file=sys.stderr); continue
        F, T, S, D, FU = (e.get(k) or {} for k in ('flujo','tasa','senda','diablo','fuente'))
        v = VIEJO.get(t, {})
        cm, cc = F.get('capex_mantenimiento'), F.get('capex_crecimiento')
        fila = {
            'ticker': t, 'nombre': cal['nombre'], 'bloque': cal['bloque'],
            'calidad_ordinal': ORDINAL[t], 'nivel_mecanismo': cal['nivel_mecanismo'],
            'mecanismo': cal['mecanismo'], 'vector': cal['vector_y_reloj'], 'dato_clave': cal['dato_clave'],
            'moneda': e.get('moneda'), 'fuente_unica': e.get('fuente_unica', False),
            'segunda_fuente_hallada': FU.get('encontrada'), 'sigue_degradada': FU.get('sigue_degradada'),
            # --- tasa ---
            'wacc': T.get('wacc'), 'rf': T.get('rf'), 'erp': T.get('erp'), 'prima_pais': T.get('prima_pais'),
            'beta_sector': T.get('beta_sector_reapalancada') or T.get('beta_reapalancada'),
            'beta_propia': T.get('beta_propia_blume') or T.get('beta_propia_cruda'),
            'beta_usada': T.get('beta_usada') or T.get('beta_reapalancada'), 'beta_criterio': T.get('beta_criterio'),
            'coste_equity': T.get('coste_equity'), 'coste_deuda': T.get('coste_deuda_pretax'),
            'peso_deuda': T.get('peso_deuda_mercado'), 'caja_neta': T.get('caja_neta'),
            # --- flujo ---
            'oe_mecanico': F.get('oe_mecanico_viejo'), 'oe_normalizado': F.get('oe_normalizado_base'),
            'capex_mant': cm, 'capex_crec': cc,
            'pct_capex_crecimiento': round(cc/(cm+cc), 4) if (cm and cc and (cm+cc)) else None,
            'sbc_gasto': F.get('sbc_gasto'), 'sbc_dilucion': F.get('sbc_dilucion_neta'),
            'margen_norm': F.get('margen_normalizado_pct'), 'margen_ult': F.get('margen_ultimo_pct'),
            'deuda_neta': F.get('deuda_neta_ajustada'), 'roiic_hist': F.get('roiic_historico'),
            'metodo_capex': F.get('metodo_split_capex'), 'defensa_margen': F.get('defensa_margen_actual'),
            'sotp': F.get('sotp'),
            # --- senda ---
            'g_inf': S.get('g_inf'), 'multiplo_terminal': S.get('multiplo_terminal_implicito'),
            'senda_anual': S.get('senda_anual'), 'vi_bajista': S.get('vi_bajista'),
            'vi_base': S.get('vi_base'), 'vi_alcista': S.get('vi_alcista'),
            'precio': S.get('precio_actual') or (float(v['precio_actual_usd']) if v else None),
            'premio': S.get('premio_descuento'), 'tir_10a': S.get('tir_10a'),
            'exige': S.get('crecimiento_implicado_precio'), 'evidenciado': S.get('crecimiento_evidenciado'),
            'tam_pasa': g(S,'candado_tam','pasa'), 'tam_ingr10': g(S,'candado_tam','ingresos_anio10'),
            'tam_cuota': g(S,'candado_tam','cuota_implicada'), 'tam_cuota_max': g(S,'candado_tam','cuota_maxima_defendible'),
            'tam_recorte': g(S,'candado_tam','recorte_aplicado'),
            'reinv_pasa': g(S,'candado_reinversion','pasa'), 'roiic_implicado': g(S,'candado_reinversion','roiic_implicado'),
            'ruido': g(S,'no_decidible','etiqueta', default='DECIDIBLE'),
            'vi_wacc_mas2': g(S,'no_decidible','vi_con_wacc_mas2pp'), 'vi_wacc_menos2': g(S,'no_decidible','vi_con_wacc_menos2pp'),
            # --- diablo ---
            'vi_diablo': D.get('vi_bajista_propio'), 'caso_bajista': D.get('caso_bajista'),
            'veredicto_diablo': D.get('veredicto_adversarial'), 'ataques': D.get('ataques'),
            'triang': D.get('triangulaciones'),
            # --- comparacion con el motor viejo ---
            'vi_viejo': float(v['valor_intrinseco_x_accion_usd']) if v else None,
            'premio_viejo': float(v['premio_descuento_pct']) if v else None,
            'ginf_viejo': float(v['ginf']) if v else None,
        }
        fila = _esc(fila)
        aud = CAPEX_AUDIT.get(t)
        if aud and fila.get('vi_base'):
            k, motivo = aud
            # Escalado directo sobre el VI. El puente por EV seria mas exacto en las apalancadas,
            # pero las unidades que devuelven los agentes (millones vs absolutos) no son homogeneas
            # y producian basura silenciosa. Escalar el VI es transparente y auditable.
            fila['vi_pre_auditoria'] = fila['vi_base']
            for kk in ('vi_base', 'vi_bajista', 'vi_alcista', 'vi_diablo'):
                if fila.get(kk): fila[kk] = fila[kk] * (1 + k)
            fila['capex_audit_pct'] = k
            fila['capex_audit_motivo'] = motivo
            # el premio se recalcula DESPUES del ajuste, no antes
            if fila.get('vi_base') and fila.get('precio'):
                fila['premio'] = fila['precio'] / fila['vi_base'] - 1
            fila['cubo'] = None  # se reasigna abajo
        fila['margen_exigido'] = MARGEN[fila['bloque']]
        fila['cubo'] = cubo(fila)
        fila['precio_gatillo'] = round(fila['vi_base'] * (1 - fila['margen_exigido']), 2) if fila['vi_base'] else None
        fila['factor_vs_viejo'] = round(fila['vi_base']/fila['vi_viejo'], 2) if (fila['vi_base'] and fila['vi_viejo']) else None
        filas.append(fila)
    return filas

if __name__ == '__main__':
    filas = construir()
    out = {'fecha': '2026-08-26', 'motor': 'v3.1', 'n': len(filas), 'filas': filas}
    json.dump(out, open(os.path.join(BASE, 'Valor_Intrinseco_v3_36.json'), 'w'), ensure_ascii=False, indent=1)
    COLS = ['calidad_ordinal','ticker','nombre','bloque','nivel_mecanismo','moneda','cubo','ruido',
            'precio','vi_bajista','vi_base','vi_alcista','vi_diablo','premio','precio_gatillo','margen_exigido','tir_10a',
            'exige','evidenciado','wacc','rf','erp','prima_pais','beta_sector','beta_propia','beta_usada',
            'coste_equity','coste_deuda','peso_deuda','caja_neta','oe_mecanico','oe_normalizado','capex_mant',
            'capex_crec','pct_capex_crecimiento','sbc_gasto','sbc_dilucion','margen_norm','margen_ult','deuda_neta',
            'roiic_hist','g_inf','multiplo_terminal','tam_pasa','tam_ingr10','tam_cuota','tam_cuota_max',
            'reinv_pasa','roiic_implicado','vi_wacc_mas2','vi_wacc_menos2','fuente_unica','segunda_fuente_hallada',
            'sigue_degradada','vi_viejo','premio_viejo','ginf_viejo','factor_vs_viejo','ruido_mecanico','ruido_calibrado_motivo','vi_pre_auditoria','capex_audit_pct','capex_audit_motivo','ruido_nota']
    with open(os.path.join(BASE, 'Valor_Intrinseco_v3_36_AUDITABLE.csv'), 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(COLS)
        for f in sorted(filas, key=lambda z: z['calidad_ordinal']):
            w.writerow([f.get(c) for c in COLS])
    resc = [f['ticker'] for f in filas if f.get('_reescalados')]
    if resc: print(f'  Reescalados de puntos porcentuales a decimal: {", ".join(resc)}')
    fuera = [(f['ticker'], f['wacc']) for f in filas if f.get('wacc') and not (0.04 <= f['wacc'] <= 0.20)]
    if fuera: print(f'  AVISO WACC fuera de rango plausible: {fuera}')
    print(f'Consolidadas {len(filas)} empresas -> Valor_Intrinseco_v3_36.json + _AUDITABLE.csv ({len(COLS)} columnas)')
    from collections import Counter
    for k, n in Counter(f['cubo'] for f in filas).most_common():
        print(f'   {k:<18} {n}')
