# Referencia — Por qué falló el sistema anterior (auditoría 2026-07-19)

## 2. POR QUÉ EL SISTEMA ANTERIOR FALLÓ

**Veredicto:** el sistema de 6 skills no tenía un defecto de calibración corregible — tenía el defecto de fondo de que sus controles eran ritual verificable: se ejecutaban, se escribían, y no cambiaban ninguna conclusión. Esto no es una opinión: está computado sobre 191-229 registros reales y sobre el 100% del código del sistema.

**El ranking estaba por debajo de su propio ruido (HECHO, computado).** Test-retest σ=2,45 puntos. En el top-30, el rango total es 13,6 pts, el gap medio entre vecinos 0,47 pts, y 14 de 29 gaps son exactamente 0. El 71,3% de los 435 pares del top-30 son estadísticamente indistinguibles. Solo 5 de 10 del top-10 sobreviven entre corridas. CSU.TO pasó del puesto 6 al 64. Y ese σ=2,45 es un SUELO: el 72,3% de los pares no cambiaron nada entre corridas, es decir hubo arrastre de valores en vez de re-puntuación independiente — el ruido real es mayor de lo medido.

**Las 11 reglas eran una sola regla (HECHO, PCA propio).** Un factor latente explica el 74,8% de la varianza de los 11 sub-scores, con cargas casi uniformes (0,25–0,33). Ningún leave-one-out baja de ρ=0,938 (auditoría original) ni de 0,9816 (recorrida sobre otro universo). R3~R4 correlacionan 0,759 (hasta 0,89 en una corrida) — dos reglas con el 24% del peso miden lo mismo. R6 y R11 tienen covarianza NEGATIVA con el total: puntúan en contra del instrumento.

**El sesgo de Felipe escala exactamente donde más importa (HECHO).** Screening→tesis, Pearson −0,629 (p<0,0001): tercil alto −12,15 pts, tercil bajo −2,39 pts. El sistema se autoinfla justo en las empresas que más entusiasman.

**Los controles eran ritual, no mecanismo.** CUARENTENA (el salvaguarda epistémico central) se emitió 3 veces en 152 registros mientras el 57% de la evidencia etiquetada HECHO no citaba ningún filing y el 17% citaba fuentes expresamente prohibidas (gurufocus, macrotrends). El techo de 7/10 por dato no verificado se violó 33 veces, algunas con la frase "con tope aplicado" escrita en la misma línea que un 9. La calibración cruzada del 2-jul detectó saturación de R8 (8 empresas clavadas en el techo), escribió "no re-puntúe" y no cambió un solo número. La verificación adversarial sí funcionaba (desinflaba −11,85 pts de media) pero el gate que la activaba (score≥85) eximía al 94,8% del universo del único control que servía.

**Contradicción madre: la calidad fijaba el precio que se permitía pagar (HECHO+cálculo propio).** El ESTÁNDAR MAESTRO y ultra-tesis-qg anclan el WACC al tier de calidad (Núcleo 7,5% · Alta 8,5% · Sólida 9,5%), pese a que cinco documentos declaran por escrito "Calidad y Precio nunca se mezclan". Cruzar de tier Sólida a Núcleo multiplica por **1,889** el precio máximo autorizado a pagar (cálculo de perpetuidad, g=3%: 15,38x→22,22x, MoS exigido 35%→15%). Y esa frontera la cruzan 26 de 38 empresas entre screening y tesis.

**El agujero central: nadie ató crecimiento a reinversión.** g = tasa de reinversión × ROIC incremental no se impone en ninguna de las 6 skills. R5 (crecimiento) y R7 (retorno) se puntuaban como reglas independientes que suman, cuando son un solo motor. Cero apariciones en todo el corpus de "qué limita el crecimiento" o "cuello de botella" como pregunta obligatoria.

**Duplicación sin reconciliación.** La doctrina de superinversores vive en 4 capas con 3 rosters distintos (9 con Graham, 9+Bogle, 12 sin Graham). El panel de 9 inversores, medido en 5 tesis reales, nunca produce un BUY y un PASS simultáneos — 5 de 5 colapsan en 2 categorías adyacentes. Es ritual, no divergencia real.

**Consejo-maestros y rabitt-uqg nunca corrieron.** Cero outputs en el sistema de archivos pese a 9 días de actividad intensa. La banda superior de convicción de consejo-maestros (≥85) es matemáticamente inalcanzable: 0 de 229 registros históricos llegó a Núcleo≥92.

**tesis-forja, el reemplazo espontáneo que Felipe ya inventó, produjo 9 tesis reales: 8 VIGILAR, 1 PASO, 0% de capital.** El candado de degradación (2+ "flaquea" topa VIGILAR) se disparaba siempre — paso 3 (moat) en 7/9, paso 6 (edge) en 9/9. La tasa de descuento fija r=9% (prohibida por el propio protocolo) decidía el veredicto más que los 9 pasos juntos: reproduje el DCF de SGS al céntimo, y con la propia estimación de WACC del dossier (5,5% en vez de 9%) el veredicto salta de "no hay camino honesto a COMPRAR" a MoS +45,9%.

**val-mos v4 nunca se ejecutó.** Escrito el 10-jul 19:33-19:36; todos los artefactos de valoración reales del repo son anteriores. Sobre los 20 outputs que sí existen (v3 y anteriores): el detector de trampas nunca emitió TRAMPA (0/20), los dos candados de MoS nunca cambiaron un veredicto (0/13 cada uno), y la escalera de MoS por tier no es función del tier (mismo tier, 15%-40% de exigencia).

**Cero validación externa (HECHO, y sigue siendo HECHO hoy).** No hay un solo dato de rentabilidad posterior en 191+ registros ni en las 69 tesis. Nadie ha demostrado nunca que un score alto de este sistema prediga nada. Este documento no lo resuelve — lo hereda como límite (§7) y como plazo de caducidad (§3, candado C7).

**Cuantitativo, sobre el sistema completo:** 30.113 líneas de código, de las cuales 57,4% existe para maquetar y 5,2% para valorar (ratio 11:1). El motor de PDF está copiado 18 veces (4.014 líneas, 3.771 son copia literal) y la paleta 19 veces (1.482 líneas, 1.404 copia). Ningún script dentro de `Skills/` importa una librería numérica ni calcula una magnitud de negocio.

---