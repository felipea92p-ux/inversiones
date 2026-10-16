import json, sys
sys.path.insert(0,'.')
import modelo_indep as M
casos=json.load(open('/home/user/inversiones/Tesis/ORCL/_trabajo_2026-10-14/artefacto/casos_validacion.json'))
md=mt=0
for c in casos:
    o=M.value(c['cfg'])
    t,_=M.tir10(c['cfg'],130.55)
    md=max(md,abs(o['vps']-c['vps'])); mt=max(mt,abs(t-c['tir']))
print('casos',len(casos),'máx|Δ VPS|',md,'máx|Δ TIR|',mt)
