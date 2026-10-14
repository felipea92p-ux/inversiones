# Estado de la prueba de aceptación (§8) — bloqueada por límite de gasto, no por diseño

> Escrito de madrugada, de forma autónoma, mientras Felipe dormía ("tú decide lo mejor"). Decisión
> tomada: **dejar de reintentar** en vez de machacar un tercer intento — dos intentos consecutivos
> fallaron con el mismo error exacto, lo cual es evidencia de un techo real, no de un fallo
> transitorio. Seguir intentando no habría movido nada, solo gastado más contra la misma pared.

## Qué pasó, en una frase

La medición de las 15 empresas está **técnicamente diseñada y arrancada correctamente** — el
esquema dividido en 5 bloques pequeños resolvió el rechazo inicial del clasificador de seguridad,
y los agentes que sí llegaron a correr funcionaron sin fallos de lógica — pero **la cuenta llegó a
su límite de gasto mensual a mitad de proceso**, dos veces seguidas, y como consecuencia
**ninguna de las 15 empresas terminó con las 3 puntuaciones completas**. No hay ninguna cifra de
fiabilidad que reportar todavía. Cero es cero, no un número parcial disfrazado.

## Los números reales de las dos corridas

| | 1ª corrida | 2ª corrida (resume) |
|---|---|---|
| Agentes previstos | 167 | 188 (incluye reintentos de la 1ª) |
| Cerrados con éxito | 66 | 128 |
| Fallidos por límite de gasto | 101 | 60 |
| Tokens de subagente gastados | 15.891.502 | 28.339.324 |
| Llamadas a herramientas | 4.500 | 7.693 |
| Empresas con las 3 puntuaciones completas | **0 de 15** | **0 de 15** |

**Total combinado: ~44 millones de tokens de subagente, más de 12.000 llamadas a herramientas,
cero empresas medidas.** Es el coste real de este experimento tal como está planteado hoy, y hay
que decirlo sin adornar.

## Por qué no reintenté una tercera vez

El error en ambas corridas fue **idéntico y literal**: *"You've hit your monthly spend limit ·
raise it at claude.ai/settings/usage"*. No es un error de red, de formato, ni de lógica del
workflow — es un techo de facturación de la cuenta. Reintentar sin que el techo se mueva
(reiniciando el mes, o subiéndolo manualmente en esa URL) produce el mismo resultado exacto,
como ya demostraron dos corridas consecutivas. Seguir habría sido ruido, no progreso.

## Lo que SÍ sobrevive de las 44 millones de tokens gastados

Los agentes que completaron con éxito (66 + 128, con solapamiento entre corridas por el caché)
quedan **guardados en caché del workflow**, identificados por `runId = wf_ee513d24-24c`. El
mecanismo de reanudación de la herramienta Workflow (`resumeFromRunId`) los recupera
**automáticamente y sin coste** en el próximo intento — no hace falta reconstruir nada a mano, y
de hecho intentarlo a mano sería peligroso (el journal solo guarda hashes de caché, no las
etiquetas de ticker/bloque que usé, así que reconstruir manualmente arriesgaría atribuir un
bloque de datos a la empresa equivocada). El propio motor de caché no corre ese riesgo porque
compara el (prompt, opciones) exacto, no una atribución manual.

**Traducción práctica: la próxima vez que se reanude, todo lo ya investigado con éxito no se
vuelve a pagar.** Solo se reintentan los ~60-101 bloques que fallaron por el límite. El coste de
terminar debería ser una fracción del ya gastado, no el total de nuevo.

## Qué hacer para retomar

1. Felipe sube el límite de gasto mensual en `claude.ai/settings/usage` (o espera al reinicio del
   ciclo de facturación).
2. En una sesión nueva o continuada, ejecutar:
   ```
   Workflow({
     scriptPath: "/Users/felipealvarez/.claude/projects/-Users-felipealvarez-Library-Mobile-Documents-com-apple-CloudDocs-INVESTMENTS-Rankings/390d2314-5111-4c06-898a-c67734364b64/workflows/scripts/rabitt-uqg-prueba-aceptacion-v2-wf_ee513d24-24c.js",
     resumeFromRunId: "wf_ee513d24-24c"
   })
   ```
3. Si vuelve a fallar por el mismo motivo, es que el límite sigue sin moverse — comprobar antes de
   relanzar, no después.

## Una duda honesta que hay que resolver antes de gastar más en esto

Mientras esta medición corría, Felipe construyó (en otra sesión, en paralelo) **`metodologia-qg`**
— una refundación completa que **abandona el paradigma de puntuar empresas** en favor de un
monólogo evidenciado con candados adversariales, y da por retiradas `qg-seilern` y compañía. No
menciona a Rabitt UQG (nació en esta misma sesión, después). Felipe ya dijo explícitamente
"dejarla terminar igual" respecto a esta medición cuando se le preguntó — así que la decisión de
seguir invirtiendo en Rabitt UQG está tomada, al menos hasta tener el número. Pero vale la pena
que, al despertar, decida con las dos cosas delante: el coste real de terminar esta medición
(barato ya, gracias al caché) contra si `metodologia-qg` hace innecesaria la pregunta que Rabitt
UQG intenta responder.

## Lo que NO se hizo esta noche, a propósito

No se tocó `metodologia-qg` más allá de leer su encabezado hace unas horas. No se intentó un
tercer relanzamiento. No se fabricó ningún número de fiabilidad a partir de datos parciales — eso
habría sido exactamente el tipo de precisión falsa que toda la rúbrica de Rabitt UQG existe para
prohibir.
