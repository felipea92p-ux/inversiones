# -*- coding: utf-8 -*-
"""Owner earnings: capitalizacion de I+D y marketing de marca. Ejemplo trabajado."""

def capitalizar(gasto_hist, vida):
    """gasto_hist: lista [t0(actual), t-1, t-2, ...]. Devuelve (activo, amortizacion_anual)."""
    activo=0.0; amort=0.0
    for i,g in enumerate(gasto_hist):
        if i==0: 
            activo += g          # el del anio actual aun no amortiza
            continue
        frac_restante = max(0.0,(vida-i)/vida)
        activo += g*frac_restante
        if i<=vida: amort += g/vida
    return activo, amort

print("="*76)
print("EJEMPLO A — SOFTWARE (vida util de I+D = 3 anios)")
print("="*76)
# empresa tipo: ventas 10.000, EBIT reportado 2.000, I+D 2.500, capital invertido contable 4.000
rd=[2500,2100,1750,1450]   # t0 .. t-3
activo_rd, amort_rd = capitalizar(rd,3)
ebit_rep=2000
ebit_aj = ebit_rep + rd[0] - amort_rd
cap_rep=4000
cap_aj = cap_rep + activo_rd
tax=0.21
print(f"  I+D gastado este anio ............ {rd[0]:>8,.0f}")
print(f"  Activo de I+D capitalizado ....... {activo_rd:>8,.0f}")
print(f"  Amortizacion anual de I+D ........ {amort_rd:>8,.0f}")
print()
print(f"  EBIT reportado ................... {ebit_rep:>8,.0f}   margen {ebit_rep/10000:>5.1%}")
print(f"  EBIT ajustado .................... {ebit_aj:>8,.0f}   margen {ebit_aj/10000:>5.1%}")
print(f"  NOPAT reportado .................. {ebit_rep*(1-tax):>8,.0f}")
print(f"  NOPAT ajustado ................... {ebit_aj*(1-tax):>8,.0f}")
print()
print(f"  Capital invertido reportado ...... {cap_rep:>8,.0f}   ROIC {ebit_rep*(1-tax)/cap_rep:>6.1%}")
print(f"  Capital invertido ajustado ....... {cap_aj:>8,.0f}   ROIC {ebit_aj*(1-tax)/cap_aj:>6.1%}")
print()
print("  LECTURA: el ROIC contable ({:.0%}) es un espejismo — no hay capital en el balance.".format(ebit_rep*(1-tax)/cap_rep))
print("  El ROIC economico ({:.0%}) es el que se mete en el DCF inverso.".format(ebit_aj*(1-tax)/cap_aj))
print("  Y la reinversion NO es el capex: es el I+D. rr = I+D neto / NOPAT ajustado = {:.0%}".format((rd[0]-amort_rd)/(ebit_aj*(1-tax))))

print()
print("="*76)
print("EJEMPLO B — MARCA DE CONSUMO (vida util de marketing de marca = 5 anios)")
print("="*76)
mk=[1200,1150,1100,1050,1000,950]
# regla: solo la porcion de CONSTRUCCION de marca, no la promocional de mantenimiento
frac_construccion=0.35
mk_c=[m*frac_construccion for m in mk]
activo_mk, amort_mk = capitalizar(mk_c,5)
ebit_rep2=1800
ebit_aj2 = ebit_rep2 + mk_c[0] - amort_mk
cap_rep2=3000
cap_aj2 = cap_rep2 + activo_mk
print(f"  Marketing total anio actual ...... {mk[0]:>8,.0f}")
print(f"  Porcion de construccion ({frac_construccion:.0%}) .... {mk_c[0]:>8,.0f}")
print(f"  Activo de marca capitalizado ..... {activo_mk:>8,.0f}")
print(f"  Amortizacion anual ............... {amort_mk:>8,.0f}")
print(f"  EBIT reportado {ebit_rep2:>7,.0f}  ->  ajustado {ebit_aj2:>7,.0f}")
print(f"  ROIC reportado {ebit_rep2*(1-tax)/cap_rep2:>6.1%}  ->  ajustado {ebit_aj2*(1-tax)/cap_aj2:>6.1%}")
print()
print("  LECTURA: en marcas el ajuste es MENOR que en software (la marca ya construida")
print("  se mantiene con poco). El efecto grande es sobre el CAPITAL, no sobre el beneficio.")

print()
print("="*76)
print("EJEMPLO C — EL ERROR QUE MAS DUELE: SBC")
print("="*76)
fcf=3000; sbc=800; recompras_antidilucion=700
print(f"  FCF reportado .................... {fcf:>8,.0f}")
print(f"  SBC (coste real, no 'no-cash') ... {-sbc:>8,.0f}")
print(f"  Owner earnings ................... {fcf-sbc:>8,.0f}   ({(fcf-sbc)/fcf-1:>+.0%} vs FCF)")
print(f"  Chequeo cruzado: recompras solo para tapar dilucion = {recompras_antidilucion:,.0f}")
print("  Si recompras_antidilucion ~ SBC, la resta esta bien calibrada.")
