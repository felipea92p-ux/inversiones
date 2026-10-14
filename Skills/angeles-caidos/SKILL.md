---
name: angeles-caidos
description: >-
  Estudio de patrones históricos de Felipe por COMPARACIÓN: extrae qué hace a una empresa un
  compounder de verdad emparejando cada caso de éxito con su "gemelo fallido" — una empresa que en
  su momento se veía igual de fuerte y después se rompió (Intel 2014, Nokia 2007, Valeant vs
  Constellation Software, Kraft Heinz 2017...). Nace de la idea original de Felipe: leer cientos de
  informes para sacar los 12-21 patrones de las empresas que se multiplican con el tiempo. NUNCA
  produce un score, una nota ni un ranking — produce una biblioteca de patrones con su tasa base y
  su gemelo fallido documentado. Úsalo SIEMPRE que Felipe quiera entender qué distingue a un
  compounder real de uno que lo parecía, investigar un "ángel caído" concreto, poner a prueba si un
  patrón que ve en una empresa actual es genuino o es la misma historia que ya falló antes, o
  alimentar los huecos de evidencia histórica (E1, E6, E7) de `metodologia-qg`. Si el proceso
  empieza a generar un número comparable entre empresas, se ha convertido en el sistema de
  puntuación viejo que ya se demostró que no sirve — se para y se corrige. Español siempre.
---

# Ángeles caídos — patrones históricos por comparación

> Diseño original: `Investigacion/Guias_y_Metodologia/2026-07-20_Diseno_Angeles_Caidos_Patrones_Historicos.md`
> (léelo primero si quieres el razonamiento completo, las metáforas y el porqué). Este archivo es
> la versión operativa — cómo ejecutarlo cuando Felipe lo pide.

## Regla de oro, la misma que gobierna `metodologia-qg`

**Este método nunca produce una nota, un score ni un ranking.** Produce prosa: un patrón nombrado,
el caso que lo confirma, el gemelo fallido que lo desmiente parcialmente, y una idea aproximada de
tasa base ("funciona en N de M casos parecidos"). Si en algún punto el proceso empieza a generar un
número comparable entre empresas, es la enfermedad vieja volviendo con otro nombre — se detiene y
se corrige. Esto no es una alternativa de puntuación a `qg-seilern`/`rabitt-uqg` (ambas retiradas o
en pausa) — es una biblioteca de casos, no un instrumento de medida.

## Cuándo se usa

- Felipe pide entender un patrón concreto ("¿por qué Constellation Software funcionó y otros
  adquirentes en serie no?").
- Felipe quiere poner a prueba una tesis nueva contra la historia ("¿esto que veo en X ya lo vi
  antes en alguna parte, y cómo terminó?").
- Se necesita rellenar evidencia histórica real para `metodologia-qg` — específicamente los
  dominios **E1** (persistencia de ROIC/crecimiento/margen a 5-10 años), **E6** (tasa base del
  propio analista — hoy vacía) y **E7** (frecuencia de eventos destructivos por sector) de la
  Frontera de Precedencia (`_Refundacion/2026-07-19_Refundacion_Metodologia_v1.md`).
- Felipe pide explícitamente "busca un ángel caído de..." o "investiga el gemelo fallido de...".

## El candado central: disciplina de fecha

**Es la regla más importante de todo el método, más que cualquier otra.** Toda lectura de un caso
histórico se hace **solo con lo publicado antes de una fecha de corte fija**, declarada al abrir el
caso. Nunca se usa lo que se sabe hoy sobre cómo terminó. Si el investigador ya sabe el desenlace
mientras lee el informe del año X, su lectura queda contaminada sin que se dé cuenta — es el mismo
sesgo que ya rompió la fiabilidad de todos los sistemas de puntuación de esta casa.

**Verificación obligatoria antes de cerrar cualquier caso:** ¿la evidencia citada tiene fecha
anterior o igual a la fecha de corte declarada? Si una sola cita es posterior, el caso se descarta
y se rehace. No hay excepción "solo para contexto".

## Protocolo, paso a paso

### 1 · Elegir el par
Un patrón candidato necesita **dos** casos: el que lo confirma (compounder real, década+ de
creación de valor) y el gemelo fallido (empresa que en su momento exhibía el mismo patrón visible
y después se rompió, en el mismo sector o uno comparable). Ver `references/candidatos-semilla.md`
para 11 pares ya identificados, listos para investigar.

### 2 · Fijar la fecha de corte
Se elige el año en que el gemelo fallido todavía parecía ganador — el momento exacto antes de que
empezara a torcerse. Esa es la fecha de corte para **ambos** casos del par (para que la comparación
sea justa: los dos se leen con el mismo horizonte de información).

### 3 · Leer ambos casos con esa fecha de corte, en sesiones separadas
Idealmente por agentes/investigadores distintos, o al menos con la fecha de corte escrita primero
y visible durante toda la investigación como recordatorio activo. Documentar cada hecho con su
fuente y fecha de publicación.

### 4 · Extraer la diferencia, no la similitud
La similitud ya se sabe — es lo que hace que parezcan el mismo patrón. La pregunta es: **¿qué los
separaba, que ya era observable en la fecha de corte, antes de saber quién ganaría?** Esa
diferencia es el patrón candidato.

### 5 · Buscar un tercer y cuarto caso
Un patrón sostenido por un solo par es una anécdota. Antes de darlo por bueno, buscar si la misma
diferencia separa a otros pares conocidos del mismo tipo. Ver `references/protocolo-detallado.md`
para el criterio de cuántos pares hacen falta según qué tan fuerte sea la señal.

### 6 · Registrar con tasa base, nunca como certeza
Formato de salida: *"[Patrón] tiende a sostenerse cuando [condición observable], y tiende a fallar
cuando [condición contraria] — visto en N de M pares examinados."* Nunca una probabilidad exacta
inventada; una frecuencia real sobre los casos efectivamente examinados, con el conteo declarado.

## Qué se entrega

Un documento de patrón por caso trabajado, en `Investigacion/Guias_y_Metodologia/patrones_angeles_caidos/`
(crear la carpeta si no existe), con: el par (ganador + gemelo fallido), la fecha de corte, la
diferencia observable identificada, las citas con fecha, y la tasa base declarada. Nunca una tabla
comparativa con notas — eso sería el ranking viejo con un nombre nuevo.

## Referencias

- `references/candidatos-semilla.md` — 11 pares ya identificados para empezar, sin tener que buscar
  desde cero.
- `references/protocolo-detallado.md` — criterio de selección de pares, cuántos casos hacen falta
  para dar un patrón por sostenido, y cómo evitar los errores ya conocidos (muestreo sobre el
  resultado, sesgo de retrospectiva).
- `references/conexion-metodo-nuevo.md` — cómo cada patrón encontrado alimenta directamente los
  Pasos 3 y 8 de `metodologia-qg`, y los dominios E1/E6/E7 de su Frontera de Precedencia.
