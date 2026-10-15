import copy, sys
sys.path.insert(0,'.')
import modelo_indep as M
base=M.load('base'); alc=M.load('alcista')
pub_base={ (0.45,0.25):56.0,(0.45,0.45):5.6,(0.60,0.25):104.8,(0.70,0.45):78.4,(0.55,0.33):72.6,(0.50,0.40):36.7}
def g(c,m,it,mode):
    c2=copy.deepcopy(c); c2['B']['margen_ebitda_terminal']=m; c2['B']['intensidad_capex_terminal']=it
    mg=c2['B']['margen_ebitda']
    if mode=='terminal_only': pass
    elif mode.startswith('cap'):
        k=int(mode[3:]); c2['B']['margen_ebitda']=[min(x,m) if i>=k else x for i,x in enumerate(mg)]
    elif mode.startswith('all'):  # years>=k set to m
        k=int(mode[3:]); c2['B']['margen_ebitda']=[m if i>=k else x for i,x in enumerate(mg)]
    return M.value(c2)['vps']
for mode in ['terminal_only','cap0','cap3','cap5','all3','all5','all9']:
    print(mode,[ (k, round(g(base,*k,mode),1), v) for k,v in pub_base.items()])
