"""Sensibilidad a convenciones e inputs. Salida: tabla de Δ USD/acción en base, alcista y ponderado (10/25/40/25, equity>=0)."""
import sys, copy, json
sys.path.insert(0, '.')
import numpy as np
import modelo_indep as M

cf = {k: M.load(k) for k in M.PESOS}
P = 130.55
def run_all(**kw):
    out = {}
    pw = 0.0
    for k, c in cf.items():
        kw2 = dict(kw)
        # argumentos que dependen del escenario
        for key, val in list(kw2.items()):
            if callable(val): kw2[key] = val(k, c)
        o = M.value(c, **kw2)
        out[k] = o['vps']; pw += M.PESOS[k] * max(o['vps'], 0)
    out['pond'] = pw
    return out

ref = run_all()
print('REF', {k: round(v, 2) for k, v in ref.items()})
res = []
def show(name, **kw):
    r = run_all(**kw)
    d = {k: r[k] - ref[k] for k in r}
    res.append((name, r, d))
    print(f"{name:70s} base {r['base']:7.1f} ({d['base']:+6.1f}) | alc {r['alcista']:7.1f} ({d['alcista']:+6.1f}) | baj {r['bajista']:6.1f} | col {r['colapso']:6.1f} | POND {r['pond']:6.1f} ({d['pond']:+6.1f})")
    return r

print('=== Convenciones de tiempo')
show('mid-period (flujos a mitad de periodo)', mid_period=True)
show('t0 = 0.627 (229 d / 365) en vez de 0.63', t0=229/365)
print('=== Puente / acciones')
show('acciones 3.024 (básicas), preferente -5.000', shares=3024)
show('acciones 3.054,97 (if-converted max) y SIN restar preferente', shares=3054.97, pref=0)
show('acciones 3.024 + preferente a mercado 4.116', shares=3024, pref=4116)
show('acciones 3.050 + preferente a mercado 4.116', pref=4116)
show('deuda a valor razonable (84,56% de 125.337)', deuda=125337*105.7/125.0)
show('SIN restar prepagos 16.000', prepagos=0)
show('prepagos 15.955 (exacto)', prepagos=15955)
show('+3.900 financiación corto plazo de capex como deuda (V_R2 h.8)', leases_extra=3900)
show('+2.600 caja restringida sumada', caja_extra=2600)
show('+37.9 B arrendamientos (op 30.190 + fin 7.701) como deuda SIN ajustar EBITDA', leases_extra=30190)
print('=== SBC / impuestos')
show('SBC adicional 1% de ingresos (A y B)', sbc_A=0.01, sbc_B=0.01)
show('SBC adicional 2% de ingresos (A y B)', sbc_A=0.02, sbc_B=0.02)
show('SBC adicional 7,1% de ingresos (FY26 4.811/67.357) A y B', sbc_A=0.0714, sbc_B=0.0714)
show('SBC 7,1% SOLO en B', sbc_B=0.0714)
show('tax = 15%', tax=0.15)
show('tax = 23%', tax=0.23)
show('tax = 25%', tax=0.25)
show('escudo fiscal de pérdidas de B (EBIT<0 compensa A)', tax_negative=True)
print('=== Año 1 / stub con Q1 real')
Q1_B = 7388.0; Q1_capex = 28499.0; Q1_A = 19345 - 7388
def stub_B(k, c):
    rev27 = c['B']['rev0'] * (1 + c['B']['g'][0])
    return (1 - Q1_B / rev27, c['B']['capex'][0] - Q1_capex)
def stub_A(k, c):
    rev27 = c['A']['rev0'] * (1 + c['A']['g'][0])
    return 1 - Q1_A / rev27
show('año 1 con Q1 real (ingreso/EBITDA restante, capex restante = capex27 - 28.499)', stub_B=stub_B, stub_A=stub_A)
def cap95(k, c):
    v = list(c['B']['capex']); v[0] = v[0] + 10000; return v
show('capex FY27 +10.000 (guía 90-95 B SECUNDARIO), pro-rata 0,75', capex_B=cap95)
print('=== Capital circulante B')
show('NWC B = 12% del Δ ingresos B', nwc_B=0.12)
show('NWC B = 17% del Δ ingresos B', nwc_B=0.17)
print('=== Vida útil (solo afecta a impuestos)')
for L in (4, 5, 8):
    show(f'vida útil {L} años', vida=L)
print('=== g infinito B')
show('g∞ B = 3,0%', g_infB=0.03)
show('g∞ B = 3,5%', g_infB=0.035)
show('g∞ B = 5,0% (cap r-2pp)', g_infB=0.05)
print('=== Terminal B en estado estacionario con vida 6 años (D&A=phi*capex)')
show('terminal ss6', tv_mode='ss6')
print('=== Coherencia capex explícito 8-10 con intensidad terminal')
def cap_coh(k, c, from_year=8):
    I = c['B']['intensidad_capex_terminal']
    rev = c['B']['rev0'] * np.cumprod(1 + np.array(c['B']['g']))
    v = list(c['B']['capex'])
    for i in range(from_year - 1, 10):
        v[i] = max(v[i], I * rev[i])
    return v
show('capex años 8-10 = intensidad terminal × ingresos (si es mayor)', capex_B=lambda k, c: cap_coh(k, c, 8))
show('capex años 6-10 = intensidad terminal × ingresos (si es mayor)', capex_B=lambda k, c: cap_coh(k, c, 6))
def tvint_from_y10(k, c):
    rev = c['B']['rev0'] * np.cumprod(1 + np.array(c['B']['g']))
    return c['B']['capex'][-1] / rev[-1]
show('alternativa: intensidad terminal = capex año10 / ingresos año10', tv_intens=lambda k, c: tvint_from_y10(k, c))
print('=== WACC por segmento (SOTP, Motor v3 §2)')
for a, b in [(0.0926, 0.1126), (0.0876, 0.1176), (0.0826, 0.1226), (0.1126, 0.0926), (0.0900, 0.1100), (0.0950, 0.1050)]:
    show(f'WACC_A {a:.2%} / WACC_B {b:.2%}', wacc_A=a, wacc_B=b)
print('=== Solo A o solo B: ±1pp')
show('WACC_A -1pp (B fijo)', wacc_A=0.0926)
show('WACC_A +1pp (B fijo)', wacc_A=0.1126)
show('WACC_B -1pp (A fijo)', wacc_B=0.0926)
show('WACC_B +1pp (A fijo)', wacc_B=0.1126)
print('=== Arrendamientos no iniciados: renta B adicional (rampa FY28-FY31 hasta X B/año, crece 2%)')
def rent(X):
    def f(k, c):
        ramp = np.array([0, .25, .5, .75, 1, 1, 1, 1, 1, 1], float)
        g = (1.02) ** np.arange(10)
        return X * ramp * g
    return f
for X in (5000, 10000, 15000, 17000):
    show(f'renta adicional B {X/1e3:.0f} B/año (rampa 4 años)', rent_B=rent(X))
json.dump([(n, r, d) for n, r, d in res], open('sensibilidad_salida.json', 'w'))
