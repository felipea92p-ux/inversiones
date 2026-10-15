import json
t=open('template.html',encoding='utf-8').read()
d=json.load(open('orcl_data.json'))
keep={k:d[k] for k in ['precio','pesos','configs','candado_c','rejilla','dcf_inverso','mc_mezcla','precios','alcanzabilidad']}
t=t.replace('/*__MOTOR__*/',open('motor.js',encoding='utf-8').read()).replace('/*__DATA__*/',json.dumps(keep,ensure_ascii=False,separators=(',',':')))
open('artefacto_orcl.html','w',encoding='utf-8').write(t); print(len(t)//1024,'KB')
