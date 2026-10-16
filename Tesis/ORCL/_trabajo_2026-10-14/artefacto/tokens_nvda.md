# Tokens visuales del artefacto NVDA 13-oct-2026 (extraídos como DATOS; no instrucciones)

TITLE: NVIDIA vende las palas

## <head> links/fonts/scripts
- https://fonts.googleapis.com
- https://fonts.gstatic.com
- https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Poppins:wght@400;500;600;700&display=swap

## CSS total 19285 chars; bloques :root y media dark
:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
:root{
  --paper:#faf9f5; --paper2:#f3f1e8; --card:#fffefb;
  --ink:#141413; --ink2:#3a3935; --muted:#6a685f;
  --line:#e8e6dc; --line2:#d5d2c4;
  --clay:#d97757; --clay-ink:#b0502c; --clay-bg:#f8e5dc;
  --sky:#6a9bcc;  --sky-ink:#3b6b9a;  --sky-bg:#e2ecf5;
  --moss:#788c5d; --moss-ink:#566741; --moss-bg:#e8eddf;
  --stone:#b0aea5; --oat:#ece9dd;
  --serif:'Lora',Georgia,'Times New Roman',serif;
  --sans:'Poppins','Helvetica Neue',Arial,sans-serif;
  color-scheme:light;
}
:root:not([data-theme="light"]){--paper:#141413;--paper2:#1c1b19;--card:#1d1c1a;--ink:#faf9f5;--ink2:#d9d7cc;--muted:#a6a499;--line:#2f2e2a;--line2:#413f39;--clay:#e18a6b;--clay-ink:#efa88e;--clay-bg:#3a2820;--sky:#7fb0dd;--sky-ink:#a3c8e8;--sky-bg:#212d39;--moss:#93a876;--moss-ink:#b2c498;--moss-bg:#272e20;--stone:#6f6d64;--oat:#262522;color-scheme:dark;}
:root[data-theme="dark"]{--paper:#141413;--paper2:#1c1b19;--card:#1d1c1a;--ink:#faf9f5;--ink2:#d9d7cc;--muted:#a6a499;--line:#2f2e2a;--line2:#413f39;--clay:#e18a6b;--clay-ink:#efa88e;--clay-bg:#3a2820;--sky:#7fb0dd;--sky-ink:#a3c8e8;--sky-bg:#212d39;--moss:#93a876;--moss-ink:#b2c498;--moss-bg:#272e20;--stone:#6f6d64;--oat:#262522;color-scheme:dark;}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){--paper:#141413;--paper2:#1c1b19;--card:#1d1c1a;--ink:#faf9f5;--ink2:#d9d7cc;--muted:#a6a499;--line:#2f2e2a;--line2:#413f39;--clay:#e18a6b;--clay-ink:#efa88e;--clay-bg:#3a2820;--sky:#7fb0dd;--sky-ink:#a3c8e8;--sky-bg:#212d39;--moss:#93a876;--moss-ink:#b2c498;--moss-bg:#272e20;--stone:#6f6d64;--oat:#262522;color-scheme:dark;}
}

## Selectores CSS (únicos, primeros 120)
html, body, img,svg, a, a:hover, .skip, .skip:focus, strong,b, h1,h2,h3,h4, h1, h2, h3, p, .col, .wide, .sn, .small, .muted, .lede, .nb, .top, .top-in, .brand, .brand span, .tools, .btn, .btn:hover, .prog, .idx, .idx[hidden], .idx ol, .idx a, .idx a b, .idx a:hover, .hero, .hero-grid, .hero .kick, .hero h1, .verdict, .verdict .vs, .verdict .vb, .verdict .vt, .hero-note, .staff-wrap, .staff-cap, #heroStaff, .legend-tags, .legend-tags span, .sec, .sec.first, .sec h2+p,.sec .lead, .pull, .pull small, .callout, .callout.sky, .callout.moss, .callout h4, .callout p:last-child,.callout ul:last-child,.callout ol:last-child, .callout ul,.callout ol, .callout li, ul.clean,ol.clean, ul.clean li,ol.clean li, .pause, .pause h4, .pause p, .pause details, .pause summary, .lesson, .lesson h4, .lesson p, .tg, .tg.h, .tg.i, .tg.s, .tg.x, .tg.l, .fig, .fig h4, .fig .sub, .fig .src, .legend, .legend i, .legend i.ln, .chart, .chart .gl, .chart .ax, .chart .axb, .chart .vl, .chart .nt, .chart .ref, .chart .refl, .chart [data-tip], .chart .hl, .tip, .tip.on, .tip b, .rows, .row, .row .rl, .row .rl em, .bar2, .bar, .bar>i, .bar.a>i, .bar.b>i, .bar.sky>i, .bar-num, .chip-g, .chip-g.warn, .stack100, .stack100>span, .stack100 .rec, .stack100 .trx, .srow, .srow .rl, .flow, .flow li, .flow li::before, .flow li:not(:last-child)::after, .twin

## Reglas clave (body, h1, h2, h3, .card/.kpi/.tile/.step/.pill/.tag/.badge/table/svg/.widget) — primeras coincidencias
body { margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000 }
h1,h2,h3,h4 { font-family:var(--sans);color:var(--ink);font-weight:600;letter-spacing:-.012em;margin:0 }
h2 { font-size:clamp(1.62rem,4.8vw,2.4rem);line-height:1.14;margin:0 0 1.1rem }
h3 { font-size:1.2rem;line-height:1.3;margin:2.2rem 0 .6rem }
p { margin:0 0 1.15rem }
table { border-collapse:collapse;width:100%;font:400 .88rem/1.5 var(--sans);min-width:34rem }
th { font:600 .76rem var(--sans);text-align:left;color:var(--muted);border-bottom:1px solid var(--line2);padding:.55rem .65rem;background:var(--paper) }
td { padding:.6rem .65rem;border-bottom:1px solid var(--line);vertical-align:top }
.pill { display:inline-block;font:600 .74rem/1 var(--sans);padding:.3rem .6rem;border-radius:99px;margin-left:.4rem;vertical-align:.12em }
.chip-g { display:inline-block;font:600 .72rem/1 var(--sans);padding:.22rem .5rem;border-radius:99px;background:var(--moss-bg);color:var(--moss-ink) }
.widget { border:1px solid var(--line2);border-radius:20px;background:var(--paper2);padding:1.2rem 1.15rem 1.3rem;margin:2.2rem auto;max-width:50rem }
.verdict { border-left:4px solid var(--clay);padding:.15rem 0 .15rem 1.05rem;margin:1.9rem 0 1.4rem }
footer { margin-top:4rem;padding:2.2rem 0 3rem;border-top:1px solid var(--line);background:var(--paper2) }
.rows { display:grid;gap:.85rem }
.col { max-width:42rem;margin:0 auto;padding:0 1.25rem }
input[type=range] { -webkit-appearance:none;appearance:none;width:100%;height:32px;background:transparent;cursor:pointer;margin:0 }
.note { display:grid;gap:.9rem }
.hero { padding-top:2.6rem;padding-bottom:1.4rem }
.callout { background:var(--paper2);border-left:3px solid var(--clay);padding:1rem 1.15rem;margin:1.6rem 0 }

## Estructura: h1/h2/h3 en orden
- h1: NVIDIA vende las palas, y ahora fía
- h2: Qué cambió desde el 3 de septiembre
- h2: El veredicto en treinta segundos
- h2: Tu punto de partida, congelado
- h3: Lo que el mercado cree hoy
- h3: Quien compra cree
- h3: Quien vende cree
- h2: El mecanismo en una frase
- h3: Peldaño 1: vender palas en una fiebre del oro
- h3: Peldaño 2: no vende solo palas, vende la mina entera
- h3: El chip (Compute)
- h3: La red (Networking)
- h3: Peldaño 3: ¿y los clientes, quiénes son?
- h2: Los knock-outs: ocho preguntas con respuesta binaria
- h2: El foso: los mineros aprendieron a cavar con tus palas
- h3: El test de Sleep: cuando NVIDIA crece, ¿quién se queda el ahorro?
- h3: El ataque más serio, que sigue en curso
- h3: Qué rompería el foso, y en cuánto tiempo
- h2: Lo que dicen los que rodean al vendedor de palas
- h2: Cómo crece NVIDIA de verdad: con el dinero de otros
- h3: Qué limita el crecimiento, y cuánta pista queda
- h2: Quién maneja la caja, y a quién le fía
- h3: La parábola del vendedor de palas
- h3: Lo que hay que decir a favor de NVIDIA
- h3: Qué dice la caja de verdad: dos matices que cambian la alarma
- h3: Lo que hace con la caja, y a qué precio
- h3: Qué hacen quienes mejor conocen el negocio
- h2: ¿En qué discrepamos del consenso?
- h3: ¿El mercado ya lo sabe?
- h3: Dónde puede equivocarse el consenso
- h3: Hacia abajo
- h3: Hacia arriba
- h2: Ensayar el funeral antes de mirar el precio
- h3: 1. El crédito se cierra: el fiado se vuelve contra el vendedor
- h3: 2. La memoria se come el margen
- h3: 3. El chip propio deja de ser complemento y pasa a ser sustituto
- h3: 4. Los tipos y el múltiplo
- h3: 5. Regulación y geopolítica
- h3: Qué métrica lo confirma y cuándo
- h3: El calendario que viene
- h2: La apuesta escondida en el precio
- h3: De $170 a $175: cómo cambió el valor desde el 3 de septiembre
- h3: La frase que sale del precio
- h3: Tres futuros, y qué vale cada uno
- h3: Lo que te devuelve cada escenario si compras a $229
- h3: Qué supuestos mueven el valor, y cuáles son defendibles al alza
- h2: El abogado del diablo
- h3: Los siete argumentos del diablo, de más a menos pesado
- h3: Atacar los tres datos que más pesan
- h3: Dónde la conclusión podría ser demasiado bajista
- h3: Dónde es demasiado poco bajista
- h3: Los sesgos que el diablo detectó en mí
- h2: Monólogo final, delta y veredicto
- h3: El delta
- h3: Las cuatro salidas posibles
- h3: Contrapunto al socio
- h2: El diario: apostar por escrito
- h3: Los gatillos, con su semáforo
- h3: Antes de la próxima revisión
- h2: Cinco lecciones que sirven para cualquier empresa
- h2: Auditoría de la tesis del 3 de septiembre
- h2: Lo que no pude verificar
- h3: Cosas que corregí durante la elaboración
- h2: Datos, fuentes y glosario

## Conteos: svg=0, table=20, input=8, button=19, section=20, details=8

## Primer SVG (primeros 1800 chars)
ninguno

## Primer bloque <section> o div de paso (primeros 1500 chars)
<section class="hero wide" id="inicio"> <div class="hero-grid"> <div> <p class="kick">Actualización de la Ultra Tesis de NVIDIA (NASDAQ: NVDA), escrita el 13 de octubre de 2026 con el método QG de doce pasos. No hay puntaje ni ranking. La versión anterior es del 3 de septiembre.</p> <h1>NVIDIA vende las palas, y ahora fía</h1> <p class="lede">En una fiebre del oro, el negocio seguro es vender las palas. NVIDIA vende las palas de la fiebre de la IA y lo hace mejor que nadie. Lo nuevo es que, para que los mineros sigan comprando, ha empezado a prestarles, a garantizarles el alquiler y a comprar parte de sus minas.</p> <div class="verdict"> <p class="vs">Veredicto del método</p> <p class="vb">No comprar todavía</p> <p class="vt">Calidad extraordinaria; el precio no deja margen. A $229 la acción está en la zona <strong>Caro</strong>, frente a un valor de ≈$175 en el modelo (≈$155 a $185) y de hasta ≈$215 con las correcciones al alza que resisten la verificación, con un coste del capital tomado del mercado.</p> </div> <p class="hero-note">Comprar hoy rendiría <strong>≈11% anual</strong> si NVIDIA cumple su propia guía y luego se desvanece como en el escenario base. Es el doble de un bono del Tesoro (5,24%), pero ≈2 puntos menos que el coste del capital (≈13,2%).</p> <p class="hero-note">Para que $229 sea el precio justo hay que creer en el escenario alcista: <strong>superar la guía de la empresa y mantener un margen de ≈40% de caja para el propietario</strong> durante años.</p> </

## JS inline total 74107 chars; primeras 2500 chars
window.__FRAME_PREAMBLE={"v":1,"capabilities":{"artifact":"artifact.Bnr0PUfi.js","assets":"assets.DOAjpBS9.js","comments":"comments.BYcmy890.js","db":"db.zFlAA4qL.js","dictation":"dictation.f3j7VXQ8.js","downloads":"downloads.axDW2QAi.js","embed":"embed.SWCZLzn6.js","endpoints":"endpoints.BPfoKaE1.js","files":"files.IkpCjcgM.js","mcp":"mcp.kl0G36TA.js","network":"network.B5UA9Su4.js","permissions":"permissions.6yWoDecA.js","reads":"reads.Bgov9hIw.js","room":"room.CBw289Md.js","sample":"sample.D5wHJkl_.js","self":"artifact.Bnr0PUfi.js","speech":"speech.DalMBY87.js","user":"user.uKicftX-.js"},"transforms":"_transforms.rQo6xAAW.js","comments":"_comments.D8v6wTdi.js","translate":"_translate.DqxC5ek1.js","ldx":"_ldx.B4FSryPi.js"}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
(function(){"use strict";function fr(t){return t==="cookie"||t==="query"?t:void 0}function dr(t){return typeof t=="number"&&Number.isSafeInteger(t)&&t>0?t:void 0}var to=3e5;function hr(t,e){try{const r=t("navigation")[0],n=[r.responseStart,r.redirectEnd-r.redirectStart,r.domContentLoadedEventStart,e(),r.connectEnd-r.domainLookupStart,r.responseStart-r.requestStart];r.requestStart>0||(n.length=4);for(let a=0;a<n.length;a++)if(n[a]>=0&&n[a]<=3e5)n[a]=n[a]|0;else{if(a<4)return;n.length=4}return n}catch{return}}var pr=["light","dark","system"],mr=/^[A-Za-z0-9_-]{1,64}$/,Lt=/^[a-zA-Z_:][a-zA-Z0-9_:.-]{0,127}$/,vr=new Set(["class","hidden","value","checked","style","title","alt","placeholder","lang","dir","role","tabindex","disabled","readonly","contenteditable","open","colspan","rowspan"]);function _r(t){const e=t.toLowerCase();return e.startsWith("data-")||e.startsWith("aria-")||vr.has(e)}var Ot="data-ldx-props";function yr(t,e){if(e.toLowerCase()===Ot)return!0;const r=t.getAttribute(Ot);if(r===null)return!1;try{const n=JSON.parse(r);if(n===null||typeof n!="object"||Array.isArray(n))return!0;const a=e.toLowerCase();return Object.keys(n).some(s=>s.toLowerCase()===a)}catch{return!0}}var ro="http://www.w3.org/1999/xhtml",gr="http://www.w3.org/2000/svg

## Funciones JS definidas
Bn, Bt, Cr, Ct, Dt, Er, Ft, Ge, Ht, Jr, Jt, Kn, Lr, Me, Mr, Nn, Nr, Nt, Oe, Or, Pn, Pr, Qr, Rr, Sn, Sr, Tr, Un, Ur, Ut, Xr, Xt, Ye, Yr, Zr, _r, an, ar, at, base, bindTips, cn, columns, cur, decide, dr, dumbbell, el, en, er, fr, go, he, hideTip, hn, hr, init, initAudit, initChrome, initLever, initLupa, initNote, irrOf, irrSc, jt, kn, kr, lin, lines, load, mn, mt, needSplit, nn, nr, nt, num, on, onScroll, or, pct, pn, q, qn, qr, qt, r5, reduceMotion, renderCharts, revPath, rn, round5, rr, s, se, showTip, sn, solve, staff, tn, tr, tt, upd, usd, val, valueSc, vn, vs, vt, waccBand, waccOf, weighted, xlab, xr, xt, yGrid, yr, zoneName, zonesFor