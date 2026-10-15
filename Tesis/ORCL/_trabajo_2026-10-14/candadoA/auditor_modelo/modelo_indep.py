"""
Reimplementación INDEPENDIENTE del modelo de dos segmentos de ORCL (auditor de modelo, Candado A, Paso 10).
NO importa motor_orcl.py. Escrito desde el propósito económico de cada línea y los JSON de configuración.
Estilo distinto a propósito (numpy, vectores, opciones de convención explícitas) para que un error de copia
no se reproduzca.

Con los argumentos por defecto reproduce la convención del motor publicado. Cada argumento opcional existe
para medir la sensibilidad a UNA convención o a UN input (ver sensibilidad.py).
"""
import json
import numpy as np

CFG_DIR = '/home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/valoracion'


def load(name):
    return json.load(open(f'{CFG_DIR}/{name}.json'))


def disc(t, r):
    return (1.0 + r) ** (-np.asarray(t, dtype=float))


def value(cfg, *, wacc=None, g_inf=None, mid_period=False, sbc_A=None, sbc_B=None,
          tax=None, tax_negative=False, prepagos=None, pref=None, shares=None, leases_extra=0.0,
          frac_y1=None, t0=None, wacc_A=None, wacc_B=None, nwc_B=0.0, rent_B=None, capex_B=None,
          deuda=None, g_infB=None, stub_B=None, stub_A=None, vida=None, tv_intens=None, tv_margen=None,
          caja_extra=0.0, tv_mode='motor'):
    """
    wacc_A / wacc_B : tasa por segmento (SOTP según Motor v3 §2). Por defecto ambas = wacc.
    nwc_B           : capital circulante de B como fracción del Δ de ingresos de B (0 = motor).
    rent_B          : vector (10) de renta adicional que resta del EBITDA de B (USD M) — p.ej. arrendamientos no iniciados.
    capex_B         : vector (10) que sustituye el capex de B.
    stub_B/stub_A   : (frac_ebitda_restante, capex_restante_USDM) reemplazo del 0.75 en el año 1 (usa Q1 real).
    tv_mode         : 'motor' | 'ss6' (estado estacionario con vida 6 años: D&A = phi*capex).
    """
    r0 = cfg['wacc'] if wacc is None else wacc
    rA = r0 if wacc_A is None else wacc_A
    rB = r0 if wacc_B is None else wacc_B
    tx = cfg['tax'] if tax is None else tax
    gi_raw = cfg['g_inf'] if g_inf is None else g_inf
    if g_infB is not None:
        gi_raw = g_infB
    t_end1 = cfg['t_primer_flujo'] if t0 is None else t0
    f1 = cfg.get('frac_y1', 1.0) if frac_y1 is None else frac_y1
    N = 10
    base_t = t_end1 + np.arange(N)
    if mid_period:
        tt = base_t.copy()
        tt[0] = t_end1 - 0.5 * f1
        tt[1:] = tt[1:] - 0.5
    else:
        tt = base_t
    # ---------------- Segmento A ----------------
    A = cfg['A']
    revA = A['rev0'] * np.cumprod(1.0 + np.array(A['g'], float))
    ebitA = revA * np.array(A['margen_ebit'], float)
    nopatA = ebitA * (1.0 - tx)
    sbcA = A['sbc_pct_rev'] if sbc_A is None else sbc_A
    fcfA = nopatA * (1.0 - A['reinversion_pct_nopat']) - sbcA * revA
    fcfA = fcfA.copy()
    if stub_A is None:
        fcfA[0] *= f1
    else:
        fcfA[0] *= stub_A
    gTA = min(A.get('g_inf', min(gi_raw, rA - 0.02)), rA - 0.02)
    tvA = fcfA[-1] * (1.0 + gTA) / (rA - gTA)
    pvA = float(np.sum(fcfA * disc(tt, rA)))
    pvTVA = float(tvA * disc(tt[-1], rA))
    evA = pvA + pvTVA
    # ---------------- Segmento B ----------------
    B = cfg['B']
    gB = np.array(B['g'], float)
    revB = B['rev0'] * np.cumprod(1.0 + gB)
    capex = np.array(B['capex'] if capex_B is None else capex_B, float)
    hist = np.array(B.get('capex_hist', []), float)
    life = B['vida_util'] if vida is None else vida
    allcap = np.concatenate([hist, capex])
    dep = np.zeros(N)
    for k in range(N):
        j = len(hist) + k
        lo = max(0, j - life)
        dep[k] = allcap[lo:j].sum() / life            # capex de los 'life' años anteriores, lineal
    mg = np.array(B['margen_ebitda'], float)
    ebitdaB = revB * mg
    if rent_B is not None:
        ebitdaB = ebitdaB - np.array(rent_B, float)
    ebitB = ebitdaB - dep
    taxB = (ebitB * tx) if tax_negative else (np.maximum(ebitB, 0.0) * tx)
    sbcB = B['sbc_pct_rev'] if sbc_B is None else sbc_B
    drev = np.diff(np.concatenate([[B['rev0']], revB]))
    fcfB = ebitdaB - taxB - capex - sbcB * revB - nwc_B * drev
    fcfB = fcfB.copy()
    if stub_B is None:
        fcfB[0] *= f1
    else:
        frac_e, capex_rest = stub_B
        fcfB[0] = (ebitdaB[0] * frac_e) - taxB[0] * f1 - capex_rest - sbcB * revB[0] * f1 - nwc_B * drev[0] * f1
    # ----- terminal B -----
    gi = min(gi_raw, rB - 0.02)
    revT = revB[-1] * (1.0 + gi)
    m_T = B['margen_ebitda_terminal'] if tv_margen is None else tv_margen
    I_T = B['intensidad_capex_terminal'] if tv_intens is None else tv_intens
    ebitdaT = revT * m_T
    rentT = 0.0 if rent_B is None else float(np.array(rent_B, float)[-1]) * (1.0 + gi)
    ebitdaT -= rentT
    if tv_mode == 'motor':
        depT = revT * I_T
        nopatT = (ebitdaT - depT) * (1.0 - tx)
        fcfT = nopatT - sbcB * revT - revT * I_T * gi / (1.0 + gi) - nwc_B * (revT - revB[-1])
    else:  # 'ss6': intensidad = capex/ingresos; D&A = phi*capex con vida L y crecimiento gi
        L = life
        phi = sum((1.0 + gi) ** (-k) for k in range(1, L + 1)) / L
        capT = revT * I_T
        depT = phi * capT
        taxT = max(ebitdaT - depT, 0.0) * tx
        fcfT = ebitdaT - taxT - capT - sbcB * revT - nwc_B * (revT - revB[-1])
    tvB = fcfT / (rB - gi)
    pvB = float(np.sum(fcfB * disc(tt, rB)))
    pvTVB = float(tvB * disc(tt[-1], rB))
    evB = pvB + pvTVB
    ev = evA + evB
    # ----- puente -----
    br = cfg['bridge']
    pp = br.get('prepagos_clientes', 0.0) if prepagos is None else prepagos
    pf = br['preferentes'] if pref is None else pref
    d = br['deuda'] if deuda is None else deuda
    claims = d + br['leases_fin'] + br.get('leases_op', 0.0) + leases_extra + pf + pp
    assets = br['caja'] + br.get('inversiones', 0.0) + caja_extra
    equity = ev - claims + assets
    sh = cfg['acciones'] if shares is None else shares
    return dict(vps=equity / sh, equity=equity, ev=ev, evA=evA, evB=evB, pvA=pvA, pvTVA=pvTVA, pvB=pvB, pvTVB=pvTVB,
                tvA=tvA, tvB=tvB, fcfA=fcfA, fcfB=fcfB, tt=tt, revA=revA, revB=revB, dep=dep, ebitB=ebitB,
                ebitdaB=ebitdaB, ebitA=ebitA, claims=claims, assets=assets, fcfT=fcfT, gi=gi, shares=sh,
                depT=depT, revT=revT, taxB=taxB, capex=capex)


def tir10(cfg, price, *, interes_neto_aftertax=0.0, **kw):
    """TIR a 10 años: compro a 'price'; recibo FCF_total/acción años 1..10 y el valor de la empresa en t_10
    (VT_A + VT_B, ya valorado en el instante del flujo 10) menos reclamaciones, por acción. Calculado DIRECTO.
    interes_neto_aftertax : USD M/año de coste financiero neto después de impuestos que el motor omite (0 = motor)."""
    o = value(cfg, **kw)
    sh = o['shares']
    cf = (o['fcfA'] + o['fcfB'] - interes_neto_aftertax) / sh
    tt = o['tt']
    tv_t10 = o['tvA'] + o['tvB']
    br = cfg['bridge']
    eq10 = (tv_t10 - br['deuda'] - br['leases_fin'] - br['preferentes'] + br['caja']) / sh
    def npvf(rate):
        return -price + np.sum(cf * (1 + rate) ** (-tt)) + eq10 * (1 + rate) ** (-tt[-1])
    lo, hi = -0.9, 2.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if npvf(mid) > 0: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi), eq10


PESOS = {'colapso': .10, 'bajista': .25, 'base': .40, 'alcista': .25}


def ponderado(cfgs, pesos=PESOS, **kw):
    tot = 0.0; v = {}
    for k, c in cfgs.items():
        v[k] = value(c, **kw)['vps']
        tot += pesos[k] * max(v[k], 0.0)
    return tot, v


if __name__ == '__main__':
    cfgs = {k: load(k) for k in PESOS}
    for k, c in cfgs.items():
        o = value(c)
        print(k, round(o['vps'], 3), round(o['evA'] / 1e3, 2), round(o['evB'] / 1e3, 2))
    print('ponderado', ponderado(cfgs))
