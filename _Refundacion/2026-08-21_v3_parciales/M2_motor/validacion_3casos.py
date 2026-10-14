exec(open('/private/tmp/claude-502/-Users-felipealvarez-Library-Mobile-Documents-com-apple-CloudDocs-INVESTMENTS/034721e7-f736-44c3-aa65-bed18e955c55/scratchpad/MOTOR_V3.py').read())
r15=0.0235+0.05; g15=0.0187          # 30-jun-2015
r26=0.0469+0.05; g26=0.0234          # 21-ago-2026 (M1: prima +5,00)
print(f'### CORTE 30-jun-2015: r={r15:.2%} g_inf={g15:.2%} | piso 1/r={1/r15:.1f}x')
print(f"{'caso':<30}{'EV/NOPAT':>9}{'N1 impl':>9}{'techo':>7}{'justo@techo':>12}{'TIR@techo':>10}{'realizado 10a':>14}")
FILA=[('MCO FY2014',990.8,0.515,0.132,22169,10,'+16,2%/a'),
      ('INTC FY2014 (ROIIC 4,1%)',11368.,0.041,0.011,155456,3,'-4,4%/a'),
      ('GILD FY2014 NOPAT pico',12391.,0.774,0.288,142276,7,'-2,1%/a'),
      ('GILD normalizado+g acotada',6178.,0.774,0.08,142276,7,'-2,1%/a')]
for nm,nop,ro,g0,ev,tc,real in FILA:
    m=ev/nop; n=n1_implicito(m,ro,g0,r15,g15)
    s='<0' if n is None else (f'{n:.1f}' if n!=float('inf') else '>40')
    print(f'{nm:<30}{m:8.1f}x{s:>9}{tc:>7}{mult(ro,g0,r15,tc,g15):>11.1f}x{tir(m,ro,g0,tc,g15):>10.2%}{real:>14}')
print('  INTC alternativa (ROIIC -5,8%, b=73,3% mantenida):')
for a in (0,3,5):
    print(f'    reinvierte {a} años mas -> justo {valor_destruccion(-0.058,0.733,r15,g15,a):.1f}x  vs 13,7x pagados')
print(f'\n### TABLA DE USO HOY: EV/NOPAT justo (r={r26:.2%}, g_inf={g26:.2%}, phi=0,87). Piso sin exceso={1/r26:.1f}x')
print(f"{'ROIIC / g0':<16}"+''.join(f'N1={n:<7}' for n in [0,3,5,7,10,12,15]))
for ro,g0 in [(0.60,0.12),(0.40,0.10),(0.30,0.10),(0.25,0.08),(0.20,0.08),(0.15,0.06),(0.12,0.05),(0.10,0.04)]:
    print(f'{ro:>5.0%} / {g0:>4.0%}    '+''.join(f'{mult(ro,g0,r26,n,g26):>8.1f}' for n in [0,3,5,7,10,12,15]))
print(f'\n### Cuanto vale un año mas de fade (MCO-tipo: ROIIC 40%, g 10%, r={r26:.2%})')
prev=None
for n in range(0,21):
    v=mult(0.40,0.10,r26,n,g26)
    if prev: print(f'   N1={n:2d}  {v:6.1f}x   (+{(v/prev-1):.1%} vs N1={n-1})')
    prev=v
