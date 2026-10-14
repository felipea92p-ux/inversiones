#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, html
d=json.load(open('Rankings/2026-08-26/_trabajo/final36.json'))
filas=d['filas']; MOT=d['motivos']; MAR=d['margenes']
def pc(v,p=1):
    try: return f'{float(v)*100:.{p}f}%'.replace('.',',')
    except: return '—'
def num(v,p=1,suf=''):
    try: return f'{float(v):.{p}f}{suf}'.replace('.',',')
    except: return '—'
def pp(v):
    try:
        f=float(v); return f'{f:+.0f} pp'.replace('.',',')
    except: return '—'
def esc(s): return html.escape(str(s or ''))

CLASE_VEC={'SIN VECTOR':'v-limpio','VECTOR SIN RELOJ':'v-limpio','TECHO ESTRUCTURAL':'v-techo',
 'RIESGO DE COLA':'v-techo','RELOJ ARRANCADO':'v-reloj','CAJA OCIOSA':'v-techo','DATO AUSENTE':'v-degradado',
 'GRIETA CONTABLE':'v-grieta','GRIETA MEDIDA':'v-grieta','MECANISMO ROTO':'v-roto','GATE DISPARADO':'v-roto',
 'NO DECIDIBLE':'v-degradado','ALTERNA + VECTOR':'v-degradado','DATO DEGRADADO':'v-degradado',
 'AL FILO':'v-degradado','NO COMPARABLE':'v-degradado','MARGEN ESTRECHO':'v-techo',
 'CONTRACCION MEDIDA':'v-roto','DATO MAL PUBLICADO':'v-degradado','CRITERIO DECIDE':'v-degradado',
 'NO RANKEABLE POR ROIC':'v-degradado','GRIETA MEDIDA - DEGRADADA por fuente unica':'v-grieta',
 'RELOJ ARRANCADO - amenaza MENOR de lo que decia el archivo':'v-reloj'}
NOMBRE_B={1:'Indestructibles',2:'Núcleo',3:'Frontera'}
SUB_B={1:'El mecanismo no tiene grieta medida',2:'Un reloj ya arrancado, con fecha',3:'Foso real con la grieta ya escrita en un filing'}

def bloque_html(b):
    fs=[f for f in filas if f['bloque']==b]
    rows=[]
    for f in fs:
        cls=CLASE_VEC.get(f['tipo_vector'],'v-limpio')
        brecha=f['brecha_pp']
        b_cls='br-neg' if (brecha is not None and float(brecha)<0) else ('br-baja' if (brecha is not None and float(brecha)<20) else 'br-alta')
        sens=f['ratio_sensibilidad']
        sens_flag=''
        if sens and float(sens)>2.0:
            sens_flag=f'<span class="flag" title="Candado C-3: si la ratio de sensibilidad supera 2,0 el veredicto máximo es NO DECIDIBLE">C-3 {num(sens)}</span>'
        rows.append(f'''<tr>
  <td class="rk">{f['orden_en_bloque']}</td>
  <td class="tk"><span class="tick">{esc(f['ticker'])}</span><span class="nom">{esc(f['nombre'])}</span></td>
  <td class="d">{pc(f['roic'])}</td>
  <td class="d">{num(f['ev_sobre_oe'],0,'×') if f['ev_sobre_oe'] else '—'}</td>
  <td class="d">{pc(f['g_exigida_por_precio'],0)}</td>
  <td class="d">{pc(f['g_demostrada_filing'],0)}</td>
  <td class="d br {b_cls}">{pp(brecha)}</td>
  <td class="vec"><span class="chip {cls}">{esc(f['tipo_vector'] or 'sin vector nombrado')}</span>{sens_flag}
      <p class="vtxt">{esc(f['vector_abierto']) or '<em>Sin vector documentado en esta pasada.</em>'}</p></td>
</tr>''')
    return f'''<section class="bloque" id="bloque{b}">
  <header class="bh">
    <div class="bnum">{b}</div>
    <div>
      <h2>{NOMBRE_B[b]}</h2>
      <p class="bsub">{SUB_B[b]}</p>
    </div>
    <div class="bmar"><span class="lbl">Margen exigido</span><strong>{esc(MAR[str(b)])}</strong></div>
  </header>
  <p class="bcrit">{esc(MOT[str(b)])}</p>
  <div class="tw"><table class="t36">
    <thead><tr><th class="rk">#</th><th>Empresa</th><th class="d">ROIC</th><th class="d">EV/OE</th>
    <th class="d">g exigida</th><th class="d">g demostrada</th><th class="d">Brecha</th><th>Vector abierto</th></tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table></div>
</section>'''

# cruce final: todas ordenadas por brecha, con su bloque
conb=[f for f in filas if f['brecha_pp'] is not None]
conb.sort(key=lambda x: float(x['brecha_pp']))
cruce=[]
for i,f in enumerate(conb,1):
    brecha=float(f['brecha_pp'])
    b_cls='br-neg' if brecha<0 else ('br-baja' if brecha<20 else 'br-alta')
    cruce.append(f'''<tr>
  <td class="rk">{i}</td>
  <td class="tk"><span class="tick">{esc(f['ticker'])}</span><span class="nom">{esc(f['nombre'])}</span></td>
  <td class="d"><span class="bpill b{f['bloque']}">{f['bloque']}</span></td>
  <td class="d">{num(f['ev_sobre_oe'],0,'×') if f['ev_sobre_oe'] else '—'}</td>
  <td class="d br {b_cls}">{pp(brecha)}</td>
  <td class="d">{esc(f['margen_exigido'].split(' —')[0])}</td>
  <td class="vec"><span class="chip {CLASE_VEC.get(f['tipo_vector'],'v-limpio')}">{esc(f['tipo_vector'] or '—')}</span></td>
</tr>''')
sin=[f for f in filas if f['brecha_pp'] is None]
sind=''.join(f'<li><b>{esc(f["ticker"])}</b> — {esc(f["nombre"])} <span class="bpill b{f["bloque"]}">bloque {f["bloque"]}</span></li>' for f in sin)

HTML=f'''<title>Los 36 y su precio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{{
  --papel:#F4F6F4; --papel2:#EAEDEA; --tarjeta:#FFFFFF; --linea:#D3D9D4; --linea2:#BFC7C1;
  --tinta:#141A22; --tinta2:#3E4852; --tinta3:#6B7680;
  --azul:#1F4E79; --azul-suave:#E4ECF3;
  --ambar:#A66A00; --ambar-suave:#F6EDDC;
  --teja:#A33A1F; --teja-suave:#F7E6E1;
  --verde:#2C6B52; --verde-suave:#E2EFE8;
  --violeta:#5B4B8A; --violeta-suave:#ECE8F5;
  --max:1180px;
}}
@media (prefers-color-scheme: dark){{ :root:not([data-theme="light"]){{
  --papel:#10151A; --papel2:#161C22; --tarjeta:#1A2128; --linea:#2C353D; --linea2:#3C4750;
  --tinta:#E8EDEA; --tinta2:#B4BEC4; --tinta3:#8794A0;
  --azul:#7FB2DC; --azul-suave:#17293A;
  --ambar:#E0A64A; --ambar-suave:#312512;
  --teja:#E38A6E; --teja-suave:#33190F;
  --verde:#6FBF9A; --verde-suave:#122A20;
  --violeta:#A897D8; --violeta-suave:#221C33;
}}}}
:root[data-theme="dark"]{{
  --papel:#10151A; --papel2:#161C22; --tarjeta:#1A2128; --linea:#2C353D; --linea2:#3C4750;
  --tinta:#E8EDEA; --tinta2:#B4BEC4; --tinta3:#8794A0;
  --azul:#7FB2DC; --azul-suave:#17293A;
  --ambar:#E0A64A; --ambar-suave:#312512;
  --teja:#E38A6E; --teja-suave:#33190F;
  --verde:#6FBF9A; --verde-suave:#122A20;
  --violeta:#A897D8; --violeta-suave:#221C33;
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--papel);color:var(--tinta);
  font-family:"IBM Plex Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:16px;line-height:1.62;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:var(--max);margin:0 auto;padding:0 24px 96px}}
h1,h2,h3{{text-wrap:balance;margin:0}}
h1{{font-family:"Instrument Serif",Georgia,serif;font-weight:400;font-size:clamp(2.6rem,6vw,4.4rem);line-height:1.02;letter-spacing:-.01em}}
h2{{font-family:"Instrument Serif",Georgia,serif;font-weight:400;font-size:clamp(1.7rem,3.2vw,2.4rem);line-height:1.1}}
h3{{font-size:1.02rem;font-weight:600;letter-spacing:.01em}}
p{{margin:0 0 1em}}
.lbl{{font-family:"IBM Plex Mono",monospace;font-size:.66rem;font-weight:600;letter-spacing:.13em;
  text-transform:uppercase;color:var(--tinta3);display:block}}
.mono{{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums}}

/* cabecera */
header.top{{border-bottom:2px solid var(--tinta);padding:44px 0 26px;margin-bottom:38px}}
.eyebrow{{font-family:"IBM Plex Mono",monospace;font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--azul);font-weight:600;margin-bottom:14px}}
.sub{{font-size:1.12rem;color:var(--tinta2);max-width:62ch;margin-top:16px}}
.meta{{display:flex;flex-wrap:wrap;gap:0 34px;margin-top:24px;padding-top:18px;border-top:1px solid var(--linea)}}
.meta div{{padding:2px 0}}
.meta strong{{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;font-size:.94rem;font-weight:500}}

/* veredicto */
.veredicto{{background:var(--tarjeta);border:1px solid var(--linea);border-left:5px solid var(--azul);
  padding:28px 30px;margin:0 0 40px;border-radius:2px}}
.veredicto h2{{margin-bottom:12px}}
.veredicto p:last-child{{margin-bottom:0}}
.veredicto strong{{color:var(--tinta)}}

/* rejilla de hallazgos */
.hall{{display:grid;grid-template-columns:repeat(auto-fit,minmax(268px,1fr));gap:16px;margin:26px 0 44px}}
.card{{background:var(--tarjeta);border:1px solid var(--linea);padding:20px 20px 18px;border-radius:2px;
  display:flex;flex-direction:column;gap:8px}}
.card .cifra{{font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;
  font-size:1.85rem;font-weight:600;line-height:1;letter-spacing:-.02em}}
.card p{{margin:0;font-size:.88rem;color:var(--tinta2);line-height:1.5}}
.c-teja .cifra{{color:var(--teja)}} .c-ambar .cifra{{color:var(--ambar)}}
.c-azul .cifra{{color:var(--azul)}} .c-verde .cifra{{color:var(--verde)}}

/* bloques */
.bloque{{margin:0 0 56px;scroll-margin-top:20px}}
.bh{{display:flex;align-items:flex-start;gap:20px;padding-bottom:14px;border-bottom:2px solid var(--tinta)}}
.bnum{{font-family:"Instrument Serif",Georgia,serif;font-size:3.4rem;line-height:.8;color:var(--azul);
  min-width:52px;font-feature-settings:"lnum"}}
.bsub{{margin:2px 0 0;color:var(--tinta2);font-size:.95rem}}
.bmar{{margin-left:auto;text-align:right;flex-shrink:0}}
.bmar strong{{font-family:"IBM Plex Mono",monospace;font-size:.9rem;color:var(--teja);display:block;
  max-width:22ch;line-height:1.35;margin-top:3px}}
.bcrit{{font-size:.9rem;color:var(--tinta2);max-width:88ch;margin:14px 0 18px;padding-left:14px;
  border-left:2px solid var(--linea2)}}

/* tablas */
.tw{{overflow-x:auto;border:1px solid var(--linea);border-radius:2px;background:var(--tarjeta)}}
table{{border-collapse:collapse;width:100%;min-width:940px}}
thead th{{font-family:"IBM Plex Mono",monospace;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--tinta3);font-weight:600;text-align:left;padding:11px 12px;border-bottom:1px solid var(--linea2);
  background:var(--papel2);position:sticky;top:0;z-index:2}}
tbody td{{padding:13px 12px;border-bottom:1px solid var(--linea);vertical-align:top;font-size:.9rem}}
tbody tr:last-child td{{border-bottom:none}}
tbody tr:hover{{background:var(--papel2)}}
th.d,td.d{{text-align:right;font-family:"IBM Plex Mono",monospace;font-variant-numeric:tabular-nums;white-space:nowrap}}
th.rk,td.rk{{width:34px;text-align:right;font-family:"IBM Plex Mono",monospace;color:var(--tinta3);font-size:.82rem}}
td.tk{{min-width:210px}}
.tick{{font-family:"IBM Plex Mono",monospace;font-weight:600;font-size:.92rem;display:block;letter-spacing:.01em}}
.nom{{font-size:.79rem;color:var(--tinta3);display:block;line-height:1.3;margin-top:1px}}
td.br{{font-weight:600}}
.br-neg{{color:var(--verde)}} .br-baja{{color:var(--ambar)}} .br-alta{{color:var(--tinta3)}}
td.vec{{max-width:430px}}
.vtxt{{margin:6px 0 0;font-size:.79rem;line-height:1.48;color:var(--tinta2)}}
.chip{{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.63rem;font-weight:600;
  letter-spacing:.07em;text-transform:uppercase;padding:3px 7px;border-radius:2px;white-space:normal}}
.v-limpio{{background:var(--verde-suave);color:var(--verde)}}
.v-techo{{background:var(--azul-suave);color:var(--azul)}}
.v-reloj{{background:var(--ambar-suave);color:var(--ambar)}}
.v-grieta{{background:var(--teja-suave);color:var(--teja)}}
.v-roto{{background:var(--teja-suave);color:var(--teja);text-decoration:underline}}
.v-degradado{{background:var(--violeta-suave);color:var(--violeta)}}
.flag{{display:inline-block;margin-left:6px;font-family:"IBM Plex Mono",monospace;font-size:.62rem;
  padding:3px 6px;border:1px solid var(--linea2);color:var(--tinta3);border-radius:2px}}
.bpill{{display:inline-block;font-family:"IBM Plex Mono",monospace;font-size:.7rem;font-weight:600;
  width:22px;height:22px;line-height:22px;text-align:center;border-radius:2px}}
.b1{{background:var(--verde-suave);color:var(--verde)}}
.b2{{background:var(--azul-suave);color:var(--azul)}}
.b3{{background:var(--teja-suave);color:var(--teja)}}

/* secciones de texto */
section.txt{{margin:0 0 48px}}
section.txt h2{{padding-bottom:10px;border-bottom:2px solid var(--tinta);margin-bottom:20px}}
.dosco{{display:grid;grid-template-columns:1fr 1fr;gap:28px}}
@media(max-width:820px){{.dosco{{grid-template-columns:1fr}}}}
.nota{{background:var(--papel2);border:1px solid var(--linea);border-left:4px solid var(--ambar);
  padding:18px 20px;margin:20px 0;border-radius:2px;font-size:.92rem}}
.nota strong{{color:var(--ambar)}}
ul.lista{{margin:0 0 1em;padding-left:20px}} ul.lista li{{margin-bottom:.55em}}
.ref{{font-family:"IBM Plex Mono",monospace;font-size:.78rem;color:var(--tinta3)}}
footer{{border-top:1px solid var(--linea);padding-top:22px;margin-top:56px;font-size:.82rem;color:var(--tinta3)}}
a{{color:var(--azul)}}
:focus-visible{{outline:2px solid var(--azul);outline-offset:2px}}
@media(prefers-reduced-motion:no-preference){{tbody tr{{transition:background .12s ease}}}}
</style>

<div class="wrap">
<header class="top">
  <div class="eyebrow">Ranking de calidad · 26 de agosto de 2026</div>
  <h1>Los 36 y su precio</h1>
  <p class="sub">Treinta y seis negocios en tres bloques, ordenados dentro de cada bloque por lo que el precio de hoy
  está pidiendo que la empresa demuestre. Sin puntuaciones: la rúbrica que las producía se midió contra sí misma
  y no resuelve los cortes que se le pedían.</p>
  <div class="meta">
    <div><span class="lbl">Universo</span><strong>485 → 36</strong></div>
    <div><span class="lbl">Fuente</span><strong>EDGAR + informe auditado</strong></div>
    <div><span class="lbl">Tasa (candado B)</span><strong>r = 9,70%</strong></div>
    <div><span class="lbl">g∞ base</span><strong>2,32%</strong></div>
    <div><span class="lbl">Precios</span><strong>26-ago 15:40 UTC</strong></div>
  </div>
</header>

<div class="veredicto">
  <h2>Veredicto primero</h2>
  <p><strong>Ninguna de las 36 está infravalorada bajo el motor vigente, y eso dice más del motor que del mercado.</strong>
  Con la <span class="mono">g∞</span> decretada en 2,32% y la tasa única en 9,70%, el múltiplo que el motor autoriza
  va de 12,7× owner earnings para un negocio plano a 31,0× para uno que compone al 25%. Todo el rango de calidad
  del mundo cabe en un factor de 2,4. Las tres únicas brechas negativas fiables del ejercicio son
  <span class="mono">ADBE</span> (−3 pp a 14× owner earnings), y de las degradadas ninguna sirve para decidir.</p>
  <p><strong>El hallazgo que importa no es la lista: es que el instrumento que la producía estaba midiendo mal.</strong>
  Cuatro de las cinco «expulsiones por unanimidad» no fueron expulsiones — dos empresas ni se evaluaron. Tres de los
  cuatro movimientos grandes de nivel no tienen ni un filing detrás. Y la lista que competía con el juicio ciego está
  construida sobre datos de FY2024 mientras se autoetiqueta <span class="mono">data_confidence: HIGH</span>.</p>
  <p><strong>El candado B4 sigue cerrado.</strong> Este documento es una priorización, no una orden de compra.</p>
</div>

<section class="txt">
  <h2>Lo que este instrumento puede y no puede resolver</h2>
  <p>Antes de la lista, la medición del aparato que la produce. Es la condición que el candado C impone y es lo único
  que separa un ranking de una opinión ordenada.</p>
  <div class="hall">
    <div class="card c-teja"><span class="lbl">Fiabilidad de la rúbrica retirada</span>
      <span class="cifra">ρ 0,289</span>
      <p>Correlación entre las dos rúbricas sumativas del archivo, sobre las mismas 25 empresas y con cinco días de
      diferencia. Error típico: 12,8 puntos sobre 100, contra cortes de 4 y 6 puntos de ancho.</p></div>
    <div class="card c-teja"><span class="lbl">Movimientos sin evidencia</span>
      <span class="cifra">3 de 4</span>
      <p>De los cuatro saltos grandes de nivel entre julio y agosto, tres no tienen ningún filing en la ventana.
      Broadcom no presentó <em>nada</em> ante la SEC entre el 26-jul y el 22-ago.</p></div>
    <div class="card c-ambar"><span class="lbl">Expulsiones que no lo eran</span>
      <span class="cifra">4 de 5</span>
      <p>HOYA y Coloplast no fueron evaluadas; Wolters Kluwer y LSEG quedaron bajo el corte dentro del ruido declarado.
      Sólo Zoetis fue expulsada de verdad.</p></div>
    <div class="card c-azul"><span class="lbl">Rango del motor de precio</span>
      <span class="cifra">2,4×</span>
      <p>Un negocio que no crece justifica 12,7× owner earnings; uno que compone al 25%, 31,0×. La
      <span class="mono">g∞</span> decretada aplasta la escala: el suelo es puro terminal de Gordon.</p></div>
  </div>

  <div class="nota">
    <strong>Contradicción interna del archivo, sin resolver.</strong> La Enmienda 30 escribe
    <span class="mono">g∞ = mín{{4,30%; ROIIC × reinversión}}</span> y afirma en la misma línea que «no lo sube en nadie».
    Ambas cosas no pueden ser ciertas: con base vigente de 2,32%, un negocio de ROIIC alto vería su
    <span class="mono">g∞</span> subir, que es aflojar. El 4,30% pertenece a la pieza 1, en cuarentena hasta el 23-sep.
    Este documento corre con la lectura conservadora — <span class="mono">g∞ = mín{{2,32%; ROIIC × b}}</span> — y lo declara.
  </div>
</section>

{bloque_html(1)}
{bloque_html(2)}
{bloque_html(3)}

<section class="txt" id="cruce">
  <h2>El cruce: calidad como puerta, precio como orden</h2>
  <p>Los dos ejes no se suman nunca — mezclarlos en una nota es exactamente lo que produjo el halo del 43,7%
  en la auditoría de julio. La calidad decide <em>en qué bloque entra</em> y <em>qué margen se le exige</em>.
  El precio decide <em>el orden dentro del bloque</em>. Esta tabla los pone juntos sin fundirlos: la columna
  de bloque es la puerta, la de brecha es el orden.</p>
  <p><strong>Cómo se lee la brecha:</strong> es el crecimiento de owner earnings que el precio de hoy exige,
  menos el que la empresa ya demuestra en su filing. Negativa significa que el mercado pide menos de lo que
  la empresa entrega — margen de seguridad. Positiva, que hay que creerse algo que aún no está en los números.</p>
  <div class="tw"><table>
    <thead><tr><th class="rk">#</th><th>Empresa</th><th class="d">Bloque</th><th class="d">EV/OE</th>
    <th class="d">Brecha</th><th class="d">Margen exigido</th><th>Vector</th></tr></thead>
    <tbody>{''.join(cruce)}</tbody>
  </table></div>
  <div class="nota" style="border-left-color:var(--violeta)">
    <strong style="color:var(--violeta)">Sin brecha calculable ({len(sin)} de las 36).</strong>
    Cotizan fuera de EE.UU. y su capex, su SBC o su recuento de acciones no están en una taxonomía comparable,
    o su balance no admite esta métrica. Entran en el ranking de calidad por dato primario verificado, pero
    <em>no se pueden ordenar por precio en esta pasada</em>. Declararlo es la única forma honesta de tratarlas.
    <ul class="lista" style="margin-top:10px">{sind}</ul>
  </div>
</section>

<section class="txt">
  <h2>Qué se rompió al verificar</h2>
  <div class="dosco">
    <div>
      <h3>El número correcto del periodo equivocado</h3>
      <p>Cinco instancias en cuatro empresas. La dermatología de Zoetis «−7,9%» es el 1T; el 2T fue
      <strong>−15,9%</strong>. Las adquisiciones de Wolters Kluwer «342 M€» son FY2024; FY2025 fueron
      <strong>871 M€</strong>. El goodwill de LSEG «19.700 M£» y su brecha de BPA «+182%» son ambos FY2024,
      citados en agosto de 2026, cuando ya son 18.689 y +76%.</p>
      <h3>El perímetro equivocado</h3>
      <p>«Elanco +10%» es su total, no Pet Health (+12%). «Thomson Reuters +10%» es el agregado Big 3,
      no su segmento (+8%). Homogeneizando, la brecha que expulsó a Wolters Kluwer pasa de 8 puntos a unos 3.</p>
    </div>
    <div>
      <h3>Lo que se corrigió a favor de la empresa</h3>
      <p><strong>Hermès:</strong> capex 7,26% de ventas, no 9-10% — la cifra vieja mezclaba capex con repago de
      arrendamientos IFRS-16. Y el «6-7% de crecimiento de capacidad anual» <em>no existe</em> en las 536 páginas
      del URD: es folclore de sell-side.</p>
      <p><strong>Constellation:</strong> ROIC 20,6% con la fórmula del propio método, no ~10% — ese número sale de
      otra definición de capital. Y su SBC es <em>cero</em>, verificado por ausencia.</p>
      <p><strong>Intuitive Surgical:</strong> Hugo de Medtronic está despejada sólo para <strong>urología</strong>
      (K250725, 510(k), no aprobación). Ottava sólo para abdomen superior, y J&amp;J no la ha declarado en ningún
      filing SEC. El crecimiento de ISRG en EE.UU. viene de cirugía general, donde Hugo hoy no puede competir.</p>
      <p><strong>HOYA:</strong> «desapareció» del ranking la semana en que publicó el mejor trimestre de su historia:
      ingresos +16,0%, beneficio operativo +30,0%, recompra del 2,99% del capital.</p>
    </div>
  </div>
  <div class="nota" style="border-left-color:var(--teja)">
    <strong style="color:var(--teja)">Un hecho de 105.000 millones que ningún juez citó.</strong>
    El 8-K de Nvidia del 17-ago-2026 (acc. 0001045810-26-000069) registra garantías de valor residual con SB Energy
    sobre 4,25 GW, con obligación de pago acumulada <strong>topada en 105.000 millones de dólares</strong> y con el
    inquilino siendo una filial de OpenAI. Seis meses antes, su 10-K decía «no hemos suscrito ningún acuerdo de
    financiación». Es el único movimiento de nivel con un hecho fechado detrás — y no fue el motivo que se declaró.
    <span class="ref">Fuente única: el 10-Q que lo corroboraría aún no existe. DEGRADADO.</span>
  </div>
</section>

<section class="txt">
  <h2>Límites declarados</h2>
  <ul class="lista">
    <li><strong>El candado B4 sigue cerrado.</strong> Ningún veredicto que dependa del motor de valoración es
    ejecutable como compra. Esto es una priorización.</li>
    <li><strong>Cero validación externa.</strong> Nada aquí mide rentabilidad posterior. Mide durabilidad estimada
    y precio exigido, no verdad.</li>
    <li><strong>Ninguna de las 12 empresas no-US tiene doble fuente primaria independiente.</strong> La regla de dos
    fuentes para sostener un knock-out no se cumple en ninguna: cada ficha descansa en un solo documento auditado.</li>
    <li><strong>La ratio de sensibilidad C-3 supera 2,0 en la mayoría de la lista.</strong> Bajo una lectura literal
    del candado, esas empresas serían <span class="mono">NO DECIDIBLE</span>. Se publica la ratio en cada fila para
    que se vea, en vez de esconderla.</li>
    <li><strong>Owner earnings = FCF − SBC con capex total.</strong> En un ciclo de capex de IA la fórmula se rompe:
    Amazon devuelve owner earnings <em>negativos</em> (−11.800 M). No es un veredicto, es una definición pendiente
    de recalibrar en sesión aparte.</li>
    <li><strong>Recuento de acciones multiclase sin ratio de conversión.</strong> Donde hay varias clases se suman en
    crudo, lo que da un suelo, no el equivalente económico exacto.</li>
    <li><strong>La venta de DUOL lleva 21 días ordenada sin ejecutar</strong> (gate roto el 5-ago: MAU +10,0% contra
    umbral +15%). Se declara en portada, como manda C-11.</li>
  </ul>
</section>

<footer>
  <p>Método: refundación de 12 pasos del 19-jul-2026 con las recalibraciones v2 del 21-ago y la Enmienda 30.
  Candado B intacto: tasa única para toda empresa, sin beta ni prima de país; la diferenciación entra por la senda
  (g₀, N₁, ROIIC medido a 4 años, g∞ ganada). ROIC siempre sobre capital total con el fondo de comercio dentro.
  Motor calibrado contra Kraft Heinz 2017: 4,11% frente al 4,17% verificado en el archivo.</p>
  <p>Documento de método dentro del marco propio de Felipe. No es asesoramiento de inversión personalizado y no soy
  asesor registrado. Las cifras de mercado están fechadas al 26-ago-2026 y caducan.</p>
</footer>
</div>'''
open('Rankings/2026-08-26/Los36_QG_2026-08-26.html','w',encoding='utf-8').write(HTML)
print('HTML generado:',len(HTML),'bytes')
