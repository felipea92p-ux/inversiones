import sys
sys.path.insert(0,'.')
import modelo_indep as M
import numpy as np
np.set_printoptions(linewidth=200, suppress=True)
for k in M.PESOS:
    c=M.load(k); o=M.value(c)
    print('=====',k, 'VPS %.1f'%o['vps'], 'EV_A %.1f EV_B %.1f  PV TV_A %.1f PV TV_B %.1f  PV explicit A %.1f B %.1f'%(o['evA']/1e3,o['evB']/1e3,o['pvTVA']/1e3,o['pvTVB']/1e3,o['pvA']/1e3,o['pvB']/1e3))
    print('tt',o['tt'])
    print('revA ',(o['revA']/1e3).round(1))
    print('fcfA ',(o['fcfA']/1e3).round(1))
    print('revB ',(o['revB']/1e3).round(1))
    print('ebitdaB',(o['ebitdaB']/1e3).round(1))
    print('depB ',(o['dep']/1e3).round(1))
    print('ebitB',(o['ebitB']/1e3).round(1))
    print('capex',(np.array(c['B']['capex'])/1e3).round(1))
    print('fcfB ',(o['fcfB']/1e3).round(1))
    print('fcfTot',((o['fcfA']+o['fcfB'])/1e3).round(1))
    revT=o['revB'][-1]*(1+o['gi'])
    print('B terminal: revT %.1f  ebitdaT %.1f depT=capexT %.1f  fcfT %.2f  tvB %.1f  (tvB/revT=%.2f x ; TV EV/EBITDA %.2f x)'%(revT/1e3, revT*c['B']['margen_ebitda_terminal']/1e3, revT*c['B']['intensidad_capex_terminal']/1e3, o['fcfT']/1e3, o['tvB']/1e3, o['tvB']/revT, o['tvB']/(revT*c['B']['margen_ebitda_terminal'])))
    print('A terminal: tvA %.1f  fcfA10 %.1f  g %.4f  mult FCF %.1f'%(o['tvA']/1e3, o['fcfA'][-1]/1e3, c['A']['g_inf'], o['tvA']/o['fcfA'][-1]))
    print('dep10 %.1f vs capex_T (%.1f) ; capex10 %.1f ; ratio capex10/rev10 %.3f ; dep10/rev10 %.3f ; terminal intens %.2f'%(o['dep'][-1]/1e3, revT*c['B']['intensidad_capex_terminal']/1e3, c['B']['capex'][-1]/1e3, c['B']['capex'][-1]/o['revB'][-1], o['dep'][-1]/o['revB'][-1], c['B']['intensidad_capex_terminal']))
