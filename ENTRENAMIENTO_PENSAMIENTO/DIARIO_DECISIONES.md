# DIARIO DE DECISIONES — Felipe

**Cómo se usa:** 1 entrada por sesión (mínimo). Puede ser una jugada de ajedrez o una decisión real (QG, CAYLA, vida). Se califica el PROCESO (1–5), nunca solo el resultado. Los domingos se auditan las entradas de la semana con Claude.

**Plantilla de entrada:**

```
### AAAA-MM-DD — [título corto]
- **Contexto:** qué había que decidir y en qué estado llegué (¿reaccionando o decidiendo?)
- **Candidatas consideradas:** (mínimo 3 en decisiones irreversibles)
- **Qué podría hacer que sea un error:** (pre-mortem en 1 línea)
- **Decisión + por qué:**
- **Predicción:** qué espero que pase, con % de confianza
- **Nota de proceso (1–5):** ¿apliqué las 6 preguntas? ¿decidí o reaccioné?
- **[Revisión posterior]:** qué pasó de verdad; ¿la predicción calibró?
```

---

## Entradas

### 2026-07-05 — Auditoría 1: el día que se diseñó el programa fue el peor día de tilt del mes
- **Contexto:** Entrada escrita por el entrenador con datos de la API de Chess.com (Felipe no reportó a mano; el diario estaba vacío). La decisión bajo examen no es una jugada: es la META-decisión de *seguir jugando* el viernes 4-jul. Ese día — el mismo en que se creó este plan — Felipe llegó a la tarde reaccionando, no decidiendo.
- **Qué pasó (dato duro):** Viernes 4-jul, 15:02–17:30 Lima, 16 partidas a 10|0: **doce derrotas seguidas**. Rating 1439 → 1360 (−79 en 2h28m). Las partidas se aceleraron a medida que la racha crecía (16:43, 16:48, 16:50 — pérdidas a 2 min una de otra): la firma del "juego para recuperar". Esa noche (21:56–23:13 Lima) volvió: 6 partidas más, LLLLL-W, 1353 → 1332. Balance del "mes-hasta-ahora": 7V-21D.
- **Candidatas que existían y no se tomaron:** (1) parar tras la 2ª derrota [regla ya escrita en §3.3]; (2) cambiar a 15|10 para no jugar en modo reactivo; (3) cerrar la laptop e ir a caminar/dormir. Ninguna se ejecutó: se eligió por defecto "una más para recuperar" doce veces.
- **Qué convirtió esto en error:** confundir 12 partidas con 12 decisiones independientes. Fue **una sola mala decisión (no parar) repetida doce veces**. El error de la partida 1 se pagó doce veces por rumiación (§3, primera línea del protocolo).
- **Predicción del entrenador:** si la próxima semana se aplica la regla de 2 derrotas + 15|10, el índice de tilt (blunders en las 3 jugadas post-error) y las rachas ≥3 caen visiblemente. Confianza: 75%. Se revisa el domingo 12-jul.
- **Nota de proceso (1–5):** **1** — se reaccionó, no se decidió; cero de las 6 preguntas aplicadas; formato equivocado (10|0). Se califica el PROCESO, no el rating: proceso reprobado, y eso es la línea base honesta desde donde subir.
- **[Revisión posterior]:** pendiente 12-jul.

### 2026-07-06 — Día 1 de Semana 1: se rompieron las DOS reglas duras (registrado por el entrenador con datos API)
- **Contexto:** primer día laborable de la Semana 1, cuyo fallo-foco es la pregunta #1 (¿decido o reacciono?) materializada en dos compromisos NO negociables: (1) cambiar el ritmo a 15|10, (2) 2 derrotas = fin del día. Felipe no reportó a mano; entrada reconstruida con la API de Chess.com.
- **Qué pasó (dato duro):** 20 partidas el lunes, **todas 10|0** (ni una sola 15|10 — regla #1 rota al 100%). Tres tandas: mañana 09:18–10:19 con una **racha de 6 derrotas seguidas** (09:30→10:19), 1348→1300 (−48), con aceleración al final (10:03, 10:14, 10:19); tarde W-L-W; noche 21:42 que se estiró **hasta las 00:27 del martes** (jugar rapid pasada la medianoche = violación HALT por cansancio). Balance del día: 8V-11D-1T. Rating cerró ~1307.
- **Candidatas que existían y no se tomaron:** parar tras la 2ª derrota de la mañana (regla #2, habría evitado 4 derrotas); abrir un tablero 15|10 en vez de 10|0 (regla #1); no reabrir la sesión de noche / no cruzar la medianoche.
- **Qué convirtió esto en error:** la regla existía escrita hace 24h y no se ejecutó ni una vez. La racha de 6 es, otra vez, **una sola decisión (no parar) repetida seis veces**, calcada al patrón del 4-jul. El compromiso conductual no falló por difícil, falló por no haberse activado el gatillo — no hubo momento de "manos fuera del mouse".
- **Matiz honesto (no todo es rojo):** el domingo 5-jul SÍ hubo freno (5 partidas, paró a las 18:51). El lunes fue recaída, no continuidad. La capacidad de parar existe; falta hacerla la respuesta por defecto bajo frustración, no solo en un día tranquilo.
- **Nota de proceso (1–5):** **1** — cero de las 6 preguntas, ambas reglas de la semana rotas, formato equivocado. Se califica el proceso, no el rating.
- **[Revisión posterior]:** se evalúa en la auditoría del domingo 12-jul junto con el resto de la semana.

### 2026-07-07 — Día 2 de Semana 1: primera señal buena (sin racha de tilt) pero las reglas duras siguen sin instalarse
- **Contexto:** martes, Semana 1. Fallo-foco = pregunta #1 (¿decido o reacciono?) con dos compromisos: (1) jugar 15|10, (2) 2 derrotas = fin del día. Entrada reconstruida con la API (Felipe no reportó a mano).
- **Qué pasó (dato duro):** 14 partidas, **todas 10|0** otra vez (regla #1 rota al 100%, tercer día seguido). PERO el resultado de la tarde-noche fue **alternado y sin espirales**: L-W-W-L-W-L-W-L-W-L-W-L-W → balance **7V-7D**, y —el dato clave— **cero rachas de ≥2 derrotas seguidas en todo el martes.** Rating prácticamente plano (1299→1305). El único lastre horario: la sesión de la noche se estiró hasta las **23:58**, y la del lunes ya había cruzado a las 00:27 del martes.
- **Lo que esto significa (la novedad):** por primera vez con dato, **la métrica-objetivo de la Semana 1 se cumplió**: "cero rachas de ≥3 derrotas en una sesión". El martes NO fue un día de tilt. Cuando no se encadenaron derrotas, la regla de "2 = parar" ni siquiera tuvo que dispararse — y aun así jugó 14 partidas. Es decir: el tilt-espiral bajó, pero el **volumen compulsivo** sigue. El fallo cambió de forma, no de raíz: ya no es "una más para recuperar tras perder", es "una más" a secas.
- **Candidatas que existían y no se tomaron:** abrir un tablero 15|10 (nunca, en 3 días); cerrar antes de medianoche; jugar 2-3 partidas *deliberadas* con checklist en vez de 14 en piloto automático.
- **Nota de proceso (1–5):** **2** (sube desde 1) — no por el marcador 7-7, sino porque hubo autorregulación real: no hubo espiral. Se descuenta por: formato equivocado por tercer día, sesión pasada de medianoche (HALT-cansancio), y cero evidencia de checklist aplicado. Se sigue calificando proceso, no rating.
- **[Revisión posterior]:** se consolida en la auditoría del domingo 12-jul.

### 2026-07-08 — Día 3: la ganancia no se guarda (espejo de sesión del patrón #1)
- **Contexto:** miércoles, Semana 1. Fallo-foco = pregunta #1. Entrada reconstruida con la API (Felipe no reportó a mano).
- **Qué pasó (dato duro):** 18 partidas, **todas 10|0** (regla #1 rota al 100%, cuarto día seguido). La secuencia lo dice todo: **WWWWWWWW-LLWLLWLLLL** — abrió con **8 victorias seguidas** y cerró con racha de 4 derrotas. Balance 10V-8D, rating 1314→1318 (+4, plano). Sesión de 09:13 a **23:57** (otra vez pegado a medianoche).
- **Lo que esto significa:** por primera vez el problema no fue el tilt de arranque — jugó **muy bien** las primeras 8. El error fue no *guardar* esa ganancia: en vez de cerrar arriba, siguió hasta devolverlo casi todo. Es el patrón #1 del baseline ("regalar la partida ganada") pero a escala de **sesión**, no de partida. La capacidad de jugar bien está demostrada; falta la decisión de parar cuando ya ganaste.
- **Candidatas que existían y no se tomaron:** cerrar la laptop tras la 8ª victoria (o incluso tras la 2ª derrota que rompió la racha buena); abrir un tablero 15|10.
- **Nota de proceso (1–5):** **2** — sube el ajedrez, no baja el proceso: el mérito de las 8 se anula por no cerrar y por 4º día a 10|0.
- **[Revisión posterior]:** auditoría 12-jul.

### 2026-07-09 — Día 4: recaída suave, sin las 8 buenas
- **Contexto:** jueves, Semana 1. Fallo-foco = pregunta #1. Reconstruida con la API.
- **Qué pasó (dato duro):** 19 partidas, **todas 10|0** (quinto día). Arranque a las **00:08** (la sesión del miércoles cruzó medianoche). Balance 8V-10D-1T, rating 1326→1301 (**−25**). Racha máx de derrotas: 3. Sin la explosión de las 8 del miércoles: día de piloto automático parejo-negativo.
- **Lo que esto significa:** la compulsión de volumen (18-19-18-19 en cuatro días) es ya el patrón dominante, por encima del tilt-espiral. El rating vuelve a bajar no por una paliza sino por el **goteo** de jugar demasiadas partidas mediocres. El "una más" a secas sigue intacto.
- **Nota de proceso (1–5):** **1,5** — sin espiral grave, pero cero reglas aplicadas, cruce de medianoche y goteo de rating.
- **[Revisión posterior]:** auditoría 12-jul.

### 2026-07-10 — Día 5 (HOY): jugó ANTES de la sesión y la regla de 2 derrotas volvió a no dispararse
- **Contexto:** viernes, Semana 1. Fallo-foco = pregunta #1, con las dos reglas duras (15|10; 2 derrotas = fin del día). Entrada del entrenador con la API a las 07:43; la sesión formal es 7:45–8:45.
- **Qué pasó (dato duro):** **9 partidas entre las 06:10 y las 07:43** — antes de sentarse a entrenar — **todas 10|0**. Secuencia **LLL**WWLWLW: abrió con **3 derrotas seguidas**. La regla #2 (parar tras la 2ª) debió cortar a la 2ª y siguió siete partidas más. Rating 1293→1296.
- **Qué convierte esto en el dato más importante de la semana:** el patrón ya no espera a la tarde ni a una paliza. Jugar 9 partidas rápidas *como calentamiento involuntario antes del entrenamiento* es el piloto automático en su forma más pura: no hubo decisión de jugar, hubo hábito. Y la 3ª derrota seguida confirma que el gatillo físico de corte (§ hipótesis del registro de tilt) sigue sin existir.
- **Candidatas que existían y no se tomaron:** no abrir la app antes de la sesión; tras la 2ª derrota, cerrar; jugar la partida seria a 15|10 *dentro* del bloque de entrenamiento, no 9 sueltas fuera de él.
- **Nota de proceso (1–5):** **1** — reacción pura, formato equivocado (5º día), regla de 2 derrotas rota en vivo esta mañana.
- **[Revisión posterior]:** auditoría 12-jul (pasado mañana).

### 2026-07-12 — AUDITORÍA 2: cierre de la Semana 1. El tilt-espiral bajó; el hábito ganó 92-0
- **Contexto:** domingo, auditoría semanal (no sesión estándar). Se revisa la Semana 1 completa (5–11 jul) con datos de la API. Fallo-foco de la semana: pregunta #1 (¿decido o reacciono?), materializada en dos reglas duras: (1) jugar 15|10, (2) 2 derrotas = fin del día.
- **El marcador de la semana (dato duro):**
  - **92 partidas en 7 días, TODAS 10|0.** Regla #1 rota al **100%, los 7 días**. Cero partidas a 15|10 en toda la semana.
  - **Racha de ≥3 derrotas en 4 de 7 días** (7-06 racha de **6**, 7-08 de 4, 7-09 de 3, 7-10 de 3). La métrica-objetivo de la semana era *"cero rachas de ≥3 en una sesión"* → **fallada 4 de 7**. Matiz: la única racha grande fue la del 7-06 (6); las de 7-09/7-10 fueron de 3 y en días netos-positivos.
  - **Volumen:** 5–17–17–18–19–13–3. Promedio **13 partidas/día**. La compulsión de volumen es ya el patrón dominante, por encima del tilt-espiral.
  - **Horario:** sesiones cruzando o pegadas a medianoche casi todos los días (7-06→23:41, 7-07 arrancó 00:02, 7-09 arrancó 00:08, 7-08→23:57). El sábado 7-11 empezó a las **23:13**.
  - **Rating:** ~1332 (inicio semana) → **1305** hoy. Otros −27. El sangrado continúa, pero mucho más lento que el −184 del colapso abril→julio.
  - **Notas de proceso de la semana:** 1 · 1 · 2 · 2 · 1,5 · 1 → **sin tendencia de mejora.** El proceso no se instaló.
- **Diagnóstico central (la verdad incómoda):** las dos reglas duras no fallaron por difíciles. **Fallaron porque nunca se ejecutaron ni una vez.** Conocer la regla no cambió la conducta ni un ápice: el conocimiento perdió **92-0** contra la fricción-cero de abrir un 10|0 (1 clic). El problema de la Semana 1 no fue cognitivo (Felipe SABE la regla) sino de **arquitectura de hábito**: no existe fricción ni gatillo físico que interrumpa el automatismo. Y el hábito se dispara en los dos extremos —perdiendo (7-06) y ganando (7-08, siguió tras 8 victorias)—, lo que confirma que ya no es "tilt": es piloto automático.
- **Lo que SÍ mejoró (no todo es rojo):** el tilt-espiral *grande* casi desapareció (solo 1 racha ≥5 en la semana vs. las de 12 y 6 de la semana previa). El sábado 7-11 el volumen cayó a 3 partidas. La capacidad de jugar bien está probada (8 victorias seguidas el 7-08). El material bruto es bueno; falta la **decisión de parar**.
- **Predicción del entrenador:** si la Semana 2 sustituye "recordar la regla" por **fricción física + tope duro pre-comprometido**, el volumen medio baja de 13 a ≤5/día y aparecen las primeras partidas a 15|10. Confianza: 70%. Se revisa el domingo 19-jul.
- **Nota de proceso de la SEMANA (1–5):** **1,5** — el proceso no se instaló, pero el tilt-espiral bajó y hubo un día de freno real. Se califica el proceso, no el rating.
- **[Revisión posterior]:** auditoría 3, domingo 19-jul.

### 2026-07-13 — Día 1 de Semana 2: la primera prueba de la hora tope, jugada de madrugada
- **Contexto:** lunes, arranca la Semana 2 (del CONOCER al INSTALAR). Fallo-foco migrado a **compulsión de volumen + arquitectura de hábito**, con tres gatillos físicos nuevos: (1) única partida = la seria a 15|10 dentro del bloque 7:45–8:45, (2) tope duro 3/día y **nada después de las 22:00**, (3) intención de implementación física de corte. Entrada del entrenador con la API a las 07:45; la sesión formal empieza ahora.
- **Qué pasó (dato duro):** **3 partidas, todas 10|0, a las 00:20 / 00:24 / 00:40** de la madrugada del lunes (secuencia L-W-W, rating 1274→1290). Es la cola de la noche del domingo cruzando la medianoche — es decir, la regla nueva **"0 partidas después de las 22:00" nació rota**, en su primera noche de vigencia. PERO: volumen bajísimo (3), y —dato que sí cuenta— **esta mañana NO hubo calentamiento involuntario pre-sesión** (nada entre las 00:40 y las 07:45). El anti-patrón del 7-10 (9 partidas antes de entrenar) no se repitió.
- **Lectura honesta (matiz en ambos sentidos):** no puedo llamar esto ni victoria ni recaída — es demasiado pronto, son 3 partidas de arrastre de la noche previa, no una decisión limpia del día 1. Lo que sí es señal: el frente de batalla de la Semana 2 quedó marcado en la primera madrugada — no es el volumen de la tarde, es **la hora**. El 10|0 de medianoche es el hábito que hay que desarmar con fricción, no con memoria.
- **Candidatas que existían y no se tomaron (anoche):** cerrar la app a las 22:00 (regla nueva #2); no reabrir un tablero después de medianoche; dejar el dispositivo fuera del alcance en horario nocturno (el compromiso físico aún sin elegir — pendiente abierto).
- **Nota de proceso (1–5):** **2** — sin espiral, volumen mínimo, y sin el calentamiento pre-sesión que sí hubo el viernes; pero la hora tope se rompió en su primera noche y el gatillo físico sigue sin instalarse. Se califica proceso, no rating.
- **[Revisión posterior]:** auditoría 3, domingo 19-jul — ¿la hora tope de las 22:00 aguantó de martes a sábado?

---

## Registro de tilt

Cada episodio de frustración súbita se anota aquí en 1 línea: fecha, disparador, cuánto duró, qué lo cortó. El patrón que emerja define los ajustes del protocolo anti-tilt.

- **2026-07-04 tarde** · disparador: 1ª-2ª derrota en 10|0 · duración: ~2h28m (16 partidas, racha de 12 derrotas) · qué lo cortó: nada interno — se agotó la sesión sola tras bajar 79 puntos. Tempo de partidas acelerándose = señal de "jugar para vengarse".
- **2026-07-04 noche** · disparador: reanudar la misma sesión mental tras la paliza de la tarde · duración: ~1h17m (6 partidas, LLLLL-W) · qué lo cortó: una victoria al final (peligroso: refuerza "seguir hasta ganar una").
- **Patrón emergente (2 episodios, mismo día):** el tilt de Felipe no explota y se corta — *se sostiene y se reanuda*. La regla crítica para él no es la del reencuadre (§3.2) sino la del **freno duro: 2 derrotas = fin del día, sin excepción** (§3.3). Es la palanca #1 de la Semana 1.
- **2026-07-06 mañana** · disparador: 2ª derrota consecutiva a las 09:40 en 10|0 · duración: ~49 min (racha de 6 derrotas, 09:30→10:19, −48 pts) · qué lo cortó: nada interno; la tanda se agotó sola. Idéntico al 4-jul: el gatillo de "manos fuera del mouse" no se activó tras la 2ª derrota.
- **2026-07-06 noche** · disparador: reabrir sesión a las 21:42 tras un día ya negativo · duración: hasta las 00:27 del martes (jugar rapid pasada la medianoche) · qué lo cortó: una victoria al filo (00:27) — de nuevo el refuerzo peligroso de "seguir hasta ganar una".
- **Lectura acumulada (3 episodios en 3 días con dato):** el freno duro sigue sin instalarse. El único día con freno real fue el domingo 5-jul (día tranquilo, sin tilt de fondo). Hipótesis para la auditoría: el problema no es *conocer* la regla sino que **no hay ritual físico de corte** en el instante de la 2ª derrota. Candidato a probar Semana 1: cerrar la laptop/salir de la app como acción obligatoria y pre-comprometida tras perder la 2ª, antes de que aparezca el "una más".
- **2026-07-07 · NO hubo episodio de tilt-espiral** (primer día con dato limpio en ese sentido: 7V-7D alternado, ninguna racha ≥2). El disparador que sí persiste es otro: **compulsión de volumen** (14 partidas) y **cruce de horario** (hasta 23:58; el lunes hasta 00:27). Lectura: el freno duro ya no se necesita para cortar espirales — se necesita ahora para cortar *cantidad y hora*. El gatillo a instalar migra de "2 derrotas = parar" a "**hora tope + tope de partidas por sesión**", porque en un día sin espiral la regla de 2 derrotas nunca se activa y aun así el patrón de piloto automático sigue.
- **2026-07-08 · no fue espiral sino ganancia-devuelta:** abrió 8V seguidas y cerró LLLL. El "tilt" aquí no es rabia, es no-parar-arriba. Nuevo disparador identificado: **estar ganando** también dispara el "una más" (para seguir la racha), igual que perder. Corte necesario en ambos extremos.
- **2026-07-09 · goteo, no explosión:** 19 partidas, cruce de medianoche (arranque 00:08), −25 de rating por volumen mediocre. Sin racha grave. Confirma compulsión de volumen como patrón dominante de la semana.
- **2026-07-10 mañana · la regla de 2 derrotas rota en vivo, ANTES de la sesión:** 9 partidas 06:10–07:43, abriendo LLL. Disparador nuevo y revelador: el juego ya no es reacción a un evento, es **hábito de fondo** (jugar de calentamiento sin decidir jugar). Lo que lo cortó: nada — se detuvo solo al llegar la hora del entrenamiento. Refuerza la hipótesis del 5-jul: falta un **ritual físico de corte pre-comprometido**; conocer la regla no basta cuando no hay decisión, solo automatismo.
- **2026-07-11 · el mejor día conductual de la semana (por poco):** solo 3 partidas (WLL), pero arrancó a las **23:13**. Volumen bajo = bien; hora = mal. Un día de baja actividad no prueba autorregulación si simplemente hubo menos ganas de jugar.
- **Lectura de cierre de Semana 1 (auditoría 2):** el patrón mutó definitivamente de *tilt-espiral* a *compulsión de volumen/hábito de fondo*. En 7 días el gatillo físico de corte no se activó **ni una vez** (regla 15|10 rota 92-0; regla de 2 derrotas rota en cada racha). Conclusión operativa para la Semana 2: dejar de pedir "aplicar la regla" y pasar a **cambiar el entorno** — subir la fricción del 10|0 y bajar la del 15|10, con un tope duro pre-comprometido de partidas y una hora tope. El gatillo debe ser físico y ambiental, no mental.
- **2026-07-13 madrugada · la hora tope, rota en su primera noche:** 3 partidas 10|0 a las 00:20–00:40 (arrastre de la noche del domingo). Volumen mínimo (bueno) pero cruce de medianoche otra vez (malo), y la regla nueva "nada después de las 22:00" nació rota. Lo positivo del día: **cero calentamiento pre-sesión** por la mañana (roto el anti-patrón del 7-10). Frente de la Semana 2 confirmado: el enemigo del hábito ahora es **la franja nocturna**, no la tarde. El dispositivo físico de corte nocturno sigue sin elegirse — es el pendiente que decide la semana.
