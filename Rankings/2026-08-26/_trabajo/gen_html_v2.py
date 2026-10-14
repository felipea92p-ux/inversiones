#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, html
d=json.load(open('Rankings/2026-08-26/_trabajo/final36_v2.json'))
filas=d['filas']; FUERA=d['fuera']
def esc(s): return html.escape(str(s or ''))
def pc(v,p=1):
    try: return f'{float(v)*100:.{p}f}%'.replace('.',',')
    except: return '—'
def pp(v):
    try: return f'{float(v):+.0f} pp'
    except: return '—'
NOM={1:'Indestructibles',2:'Núcleo',3:'Frontera'}
SUB={1:'Mecanismo de nivel 1-5 verificado, sin reloj arrancado, knock-outs superados',
     2:'Economía élite con UN reloj ya fechado, o una medida clave degradada y declarada',
     3:'Foso real y grande con la grieta ya escrita en un filing — o donde el instrumento no resuelve'}
NIVTXT={1:'sin vector de disputa',2:'candado de coordinación',3:'ausencia de destino',
        4:'peaje con tarifa propia',5:'candado de un tercero',6:'fuerte con grieta medida',7:'la tarifa la fija otro'}
def bloque(b):
    rows=[]
    for f in [x for x in filas if x['bloque']==b]:
        br=f['brecha_pp_informativa']; roic=f['roic']; gw=f['gw_sobre_capital']
        gwflag=f' <span class="flag" title="goodwill sobre capital empleado">GW {pc(gw,0)}</span>' if (isinstance(gw,(int,float)) and gw>=0.5) else ''
        rows.append(f'''<tr>
  <td class="rk">{f['orden']}</td>
  <td class="tk"><span class="tick">{esc(f['ticker'])}</span><span class="nom">{esc(f['nombre'])}</span></td>
  <td class="d"><span class="nivpill n{f['nivel_mecanismo']}">{f['nivel_mecanismo']}</span></td>
  <td class="mec"><p class="mtx">{esc(f['mecanismo'])}</p></td>
  <td class="vec"><p class="vtxt">{esc(f['vector_y_reloj'])}</p><p class="ref">{esc(f['dato_clave'])}</p></td>
  <td class="d">{pc(roic,0)}{gwflag}</td>
  <td class="d dim">{pp(br) if br is not None else '—'}</td>
</tr>''')
    return f'''<section class="bloque" id="b{b}">
  <header class="bh"><div class="bnum">{b}</div>
    <div><h2>{NOM[b]}</h2><p class="bsub">{SUB[b]}</p></div></header>
  <div class="tw"><table>
    <thead><tr><th class="rk">#</th><th>Empresa</th><th class="d">Nivel</th><th>Mecanismo</th>
    <th>Vector / reloj · evidencia</th><th class="d">ROIC</th><th class="d">Brecha*</th></tr></thead>
    <tbody>{''.join(rows)}</tbody></table></div>
</section>'''
fuera_rows=''.join(f'<tr><td class="tk"><span class="tick">{esc(t)}</span></td><td class="vec"><p class="vtxt">{esc(m)}</p></td></tr>' for t,m in FUERA)
HTML=f'''<title>Los 36 y su precio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{{--papel:#F4F6F4;--papel2:#EAEDEA;--tarjeta:#FFFFFF;--linea:#D3D9D4;--linea2:#BFC7C1;
--tinta:#141A22;--tinta2:#3E4852;--tinta3:#6B7680;--azul:#1F4E79;--azul-suave:#E4ECF3;
--ambar:#A66A00;--ambar-suave:#F6EDDC;--teja:#A33A1F;--teja-suave:#F7E6E1;
--verde:#2C6B52;--verde-suave:#E2EFE8;--violeta:#5B4B8A;--violeta-suave:#ECE8F5;--max:1240px}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--papel:#10151A;--papel2:#161C22;--tarjeta:#1A2128;--linea:#2C353D;--linea2:#3C4750;--tinta:#E8EDEA;--tinta2:#B4BEC4;--tinta3:#8794A0;--azul:#7FB2DC;--azul-suave:#17293A;--ambar:#E0A64A;--ambar-suave:#312512;--teja:#E38A6E;--teja-suave:#33190F;--verde:#6FBF9A;--verde-suave:#122A20;--violeta:#A897D8;--violeta-suave:#221C33}}}}
:root[data-theme="dark"]{{--papel:#10151A;--papel2:#161C22;--tarjeta:#1A2128;--linea:#2C353D;--linea2:#3C4750;--tinta:#E8EDEA;--tinta2:#B4BEC4;--tinta3:#8794A0;--azul:#7FB2DC;--azul-suave:#17293A;--ambar:#E0A64A;--ambar-suave:#312512;--teja:#E38A6E;--teja-suave:#33190F;--verde:#6FBF9A;--verde-suave:#122A20;--violeta:#A897D8;--violeta-suave:#221C33}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--papel);color:var(--tinta);font-family:"IBM Plex Sans",-apple-system,sans-serif;font-size:16px;line-height:1.62;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:var(--max);margin:0 auto;padding:0 24px 96px}}
h1,h2{{text-wrap:balance;margin:0;font-family:"Instrument Serif",Georgia,serif;font-weight:400}}
h1{{font-size:clamp(2.6rem,6vw,4.4rem);line-height:1.02}}
h2{{font-size:clamp(1.7rem,3.2vw,2.4rem);line-height:1.1}}
p{{margin:0 0 1em}}
.lbl{{font-family:"IBM Plex Mono",monospace;font-size:.66rem;font-weight:600;letter-spacing:.13em;text-transform:uppercase;color:var(--tinta3);display:block}}
.mono{{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums}}
header.top{{border-bottom:2px solid var(--tinta);padding:44px 0 26px;margin-bottom:38px}}
.eyebrow{{font-family:"IBM Plex Mono",monospace;font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--azul);font-weight:600;margin-bottom:14px}}
.sub{{font-size:1.12rem;color:var(--tinta2);max-width:64ch;margin-top:16px}}
.meta{{display:flex;flex-wrap:wrap;gap:0 34px;margin-top:24px;padding-top:18px;border-top:1px solid var(--linea)}}
.meta strong{{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;font-size:.94rem;font-weight:500}}
.veredicto{{background:var(--tarjeta);border:1px solid var(--linea);border-left:5px solid var(--azul);padding:28px 30px;margin:0 0 40px;border-radius:2px}}
.veredicto h2{{margin-bottom:12px}}
.taxo{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:22px 0 44px}}
.tx{{background:var(--tarjeta);border:1px solid var(--linea);border-radius:2px;padding:12px 14px}}
.tx .tn{{font-family:"Instrument Serif",Georgia,serif;font-size:1.7rem;color:var(--azul);line-height:1}}
.tx p{{margin:6px 0 0;font-size:.78rem;color:var(--tinta2);line-height:1.4}}
.bloque{{margin:0 0 56px;scroll-margin-top:20px}}
.bh{{display:flex;align-items:flex-start;gap:20px;padding-bottom:14px;border-bottom:2px solid var(--tinta);margin-bottom:16px}}
.bnum{{font-family:"Instrument Serif",Georgia,serif;font-size:3.4rem;line-height:.8;color:var(--azul);min-width:52px}}
.bsub{{margin:2px 0 0;color:var(--tinta2);font-size:.95rem}}
.tw{{overflow-x:auto;border:1px solid var(--linea);border-radius:2px;background:var(--tarjeta)}}
table{{border-collapse:collapse;width:100%;min-width:1040px}}
thead th{{font-family:"IBM Plex Mono",monospace;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--tinta3);font-weight:600;text-align:left;padding:11px 12px;border-bottom:1px solid var(--linea2);background:var(--papel2);position:sticky;top:0}}
tbody td{{padding:13px 12px;border-bottom:1px solid var(--linea);vertical-align:top;font-size:.9rem}}
tbody tr:last-child td{{border-bottom:none}}
tbody tr:hover{{background:var(--papel2)}}
th.d,td.d{{text-align:right;font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;white-space:nowrap}}
th.rk,td.rk{{width:30px;text-align:right;font-family:"IBM Plex Mono",monospace;color:var(--tinta3);font-size:.82rem}}
td.tk{{min-width:150px}}
.tick{{font-family:"IBM Plex Mono",monospace;font-weight:600;font-size:.92rem;display:block}}
.nom{{font-size:.78rem;color:var(--tinta3);display:block;line-height:1.3}}
td.mec{{max-width:300px}} td.vec{{max-width:430px}}
.mtx{{margin:0;font-size:.83rem;line-height:1.5}}
.vtxt{{margin:0 0 4px;font-size:.8rem;line-height:1.48;color:var(--tinta2)}}
.ref{{font-family:"IBM Plex Mono",monospace;font-size:.68rem;color:var(--tinta3);margin:0}}
.dim{{color:var(--tinta3)}}
.nivpill{{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.72rem;font-weight:600;width:24px;height:24px;line-height:24px;text-align:center;border-radius:2px}}
.n1,.n2{{background:var(--verde-suave);color:var(--verde)}}
.n3,.n4{{background:var(--azul-suave);color:var(--azul)}}
.n5{{background:var(--ambar-suave);color:var(--ambar)}}
.n6,.n7{{background:var(--teja-suave);color:var(--teja)}}
.flag{{display:inline-block;margin-left:5px;font-family:"IBM Plex Mono",monospace;font-size:.6rem;padding:2px 5px;border:1px solid var(--linea2);color:var(--violeta);border-radius:2px}}
section.txt{{margin:0 0 48px}}
section.txt h2{{padding-bottom:10px;border-bottom:2px solid var(--tinta);margin-bottom:20px}}
.nota{{background:var(--papel2);border:1px solid var(--linea);border-left:4px solid var(--ambar);padding:18px 20px;margin:20px 0;border-radius:2px;font-size:.92rem}}
.nota strong{{color:var(--ambar)}}
ul.lista{{margin:0 0 1em;padding-left:20px}} ul.lista li{{margin-bottom:.55em}}
footer{{border-top:1px solid var(--linea);padding-top:22px;margin-top:56px;font-size:.82rem;color:var(--tinta3)}}
:focus-visible{{outline:2px solid var(--azul);outline-offset:2px}}
</style>
<div class="wrap">
<header class="top">
  <div class="eyebrow">Ranking de ultracalidad · v2 · 26 de agosto de 2026</div>
  <h1>Los 36 y su precio</h1>
  <p class="sub">Treinta y seis fosos, ordenados por lo único que el instrumento validado sabe medir:
  la <strong>durabilidad del mecanismo que les permite cobrar</strong>, a diez años. El dinero sólo veta
  (knock-outs); el precio es una columna informativa, porque el motor de valoración quedó demostrado
  incapaz de discriminar (B4 cerrado).</p>
  <div class="meta">
    <div><span class="lbl">Universo</span><strong>485 → 173 → 36</strong></div>
    <div><span class="lbl">Puerta</span><strong>mecanismo, no ROIC</strong></div>
    <div><span class="lbl">Agentes de verificación</span><strong>9 sobre filing primario</strong></div>
    <div><span class="lbl">Tasa (candado B)</span><strong>r = 9,70%</strong></div>
    <div><span class="lbl">Precios</span><strong>26-ago-2026</strong></div>
  </div>
</header>
<div class="veredicto">
  <h2>Veredicto primero</h2>
  <p><strong>La v1 de esta lista estaba mal, y la queja de Felipe era correcta.</strong> Usaba filtros
  financieros (ROIC, goodwill) como puerta de calidad — y eso mide un balance, no un foso. Por ahí se
  colaron Adobe y Zoetis y se quedaron fuera GE Aerospace, Union Pacific, O'Reilly o Thomson Reuters,
  que nunca habían pasado por los rankings del archivo. Esta v2 usa como puerta la taxonomía de mecanismos
  del juicio ciego validado (ρ 0,969), verificada empresa a empresa contra filing primario por nueve agentes.</p>
  <p><strong>El precio hoy no ordena nada con fiabilidad.</strong> El re-piloto del candado B4 devolvió
  el mismo múltiplo autorizado — <span class="mono">15,047×</span> — para MercadoLibre y para Microsoft,
  dos negocios sin nada en común. B4 sigue cerrado; la brecha del DCF inverso se publica como columna
  marcada con asterisco, degradada y no ejecutable.</p>
  <p><strong>Cero de las 36 están infravaloradas bajo el motor vigente.</strong> Con el instrumento roto en
  ese eje, el «qué comprar» de hoy es: la lista corta de fosos de nivel 1-3 con la menor exigencia de
  crecimiento implícita — y esperar a que la recalibración de octubre arregle el motor antes de ejecutar.</p>
</div>
<section class="txt">
  <h2>La vara: siete niveles de mecanismo</h2>
  <div class="taxo">
    <div class="tx"><div class="tn">1</div><p>Sin vector de disputa — ni tecnológico, ni regulatorio, ni de contraparte</p></div>
    <div class="tx"><div class="tn">2</div><p>Coordinación: para irse hay que mover dos poblaciones a la vez</p></div>
    <div class="tx"><div class="tn">3</div><p>Ausencia de destino: el cliente no tiene a dónde ir</p></div>
    <div class="tx"><div class="tn">4</div><p>Peaje con la tarifa en manos propias</p></div>
    <div class="tx"><div class="tn">5</div><p>Candado impuesto por un tercero que no cambia de opinión</p></div>
    <div class="tx"><div class="tn">6</div><p>Mecanismo fuerte con una grieta ya medida en filing</p></div>
    <div class="tx"><div class="tn">7</div><p>La tarifa la fija otro, o el foso hay que recomprarlo — no es ultracalidad</p></div>
  </div>
</section>
{bloque(1)}
{bloque(2)}
{bloque(3)}
<section class="txt">
  <h2>Las que cayeron, con su motivo</h2>
  <p>Nada se excluyó a priori: cada una cayó por un hecho fechado, un knock-out o una decisión declarada.</p>
  <div class="tw"><table style="min-width:720px">
    <thead><tr><th>Ticker</th><th>Motivo, con la evidencia</th></tr></thead>
    <tbody>{fuera_rows}</tbody></table></div>
  <div class="nota"><strong>Sobre Adobe, para el registro.</strong> Sale por decisión de Felipe (asedio de la IA).
  El dato dice otra cosa hoy: +11,97% y +12,68% interanual los dos últimos trimestres, ARR 25.200 M$, y cero
  firma del ataque en filings. Si en el trimestre que cierra el 28-ago crece &lt;10,5%, el dato le dará la razón
  a Felipe; si no, la discrepancia queda anotada con fecha. Así se resuelven los desacuerdos en este método:
  con un falsable, no con una discusión.</div>
</section>
<section class="txt">
  <h2>Límites declarados</h2>
  <ul class="lista">
    <li><strong>B4 CERRADO — nada de esta página es ejecutable como compra.</strong> El re-piloto (MELI+BKNG+MSFT+MA) demostró que el motor no discrimina: C-5 comprime un abanico del 303% en uno del 23%, y no hay TAM primario en ninguno de los cuatro 10-K.</li>
    <li><strong>La columna Brecha* es informativa y está degradada</strong>: g exigida por el precio menos CAGR de owner earnings capado por C-6. No ordena los bloques.</li>
    <li><strong>Seis de las 36 son fuente única no-US</strong> (RMS.PA, CSU.TO, 7741.T, 6861.T, 4684.T, STMN.SW, ADYEN.AS): un solo documento auditado cada una; la regla de dos fuentes no se cumple.</li>
    <li><strong>El lote de megacaps del triaje de mecanismo murió a medias por límite de gasto</strong>; sus veredictos (MSFT, GOOGL, AAPL, NVDA, V, MA, TSM, ASML) se apoyan en las verificaciones previas de esta misma sesión, no en ese lote.</li>
    <li><strong>La asignación a bloques es juicio sobre evidencia, no fórmula</strong> — igual que el juicio ciego. Lo que es mecánico son los knock-outs y las cifras; lo que es juicio está a la vista, fila a fila.</li>
    <li><strong>La venta de DUOL sigue ordenada sin ejecutar (21 días).</strong> C-11 declarado.</li>
    <li><strong>Cero validación externa</strong>: esto mide durabilidad estimada, no rentabilidad futura.</li>
  </ul>
</section>
<footer>
  <p>Método: refundación 12 pasos (19-jul-2026) + recalibración v2 (21-ago) + Enmienda 30. Candado B intacto (r única
  9,70% = DGS10 4,70 + 5,00). Motor de knock-outs calibrado contra Kraft Heinz 2017 (4,11% vs 4,17% del archivo).
  Nueve agentes de verificación adversarial sobre EDGAR y fuentes primarias no-US; abogado-diablo en sesión limpia
  tumbó la v1 y esta v2 incorpora sus tres golpes.</p>
  <p>Documento de método dentro del marco propio de Felipe. No es asesoramiento de inversión personalizado y no soy
  asesor registrado. Cifras fechadas al 26-ago-2026; caducan.</p>
</footer>
</div>'''
open('Rankings/2026-08-26/Los36_QG_2026-08-26.html','w',encoding='utf-8').write(HTML)
print('HTML v2:',len(HTML),'bytes')
