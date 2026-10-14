# Qué es `fiabilidad.py` y para qué sirve

**En una frase:** es una báscula-comprobadora. Le das los datos de cualquier sistema que le ponga
notas a empresas, y te dice si ese sistema es de fiar o no.

## El problema que resuelve

Antes de confiar en cualquier examen de 11 (o las que sean) preguntas que le pone nota a una
empresa, hay que hacerse una pregunta previa, más importante que cualquier otra: **si le pongo
nota a la misma empresa dos veces, ¿me da el mismo resultado?**

Si la respuesta es "no, casi nunca coincide", ese examen no sirve — da igual lo bien pensadas que
estén las preguntas. Es como pesarte dos veces seguidas en la misma báscula y que dé números
distintos: el problema no es tu peso, es la báscula.

## Qué hace exactamente

Le das dos rondas de notas (la misma empresa puntuada dos veces, en momentos distintos) y te dice:

1. **¿El orden final se parece?** — si puntuaste 15 empresas y las ordenaste de mejor a peor,
   ¿el orden de la primera ronda se parece al de la segunda? (Esto es lo más importante de todo.)
2. **¿Qué preguntas del examen son las que más fallan?** — de las 11 preguntas, te dice cuáles dan
   resultados distintos cada vez que las repites, para que sepas cuáles reescribir primero.
3. **¿Hay preguntas que en realidad son la misma pregunta repetida?** — si dos preguntas siempre
   suben y bajan juntas, probablemente están midiendo lo mismo con otras palabras.
4. **¿Sobra alguna pregunta?** — si quitas una pregunta entera y el resultado casi no cambia, esa
   pregunta no estaba aportando nada.

## Cómo se usa

```bash
python3 _diagnostico/fiabilidad.py
```

Necesita, como mínimo, la misma empresa puntuada dos veces con las mismas preguntas, guardado en
un formato sencillo (ticker, fecha, y la nota de cada pregunta). Si algún día vuelves a construir
un sistema de notas —para lo que sea, no solo para empresas— y quieres comprobar si es de fiar
antes de confiar en él, esta herramienta sirve para eso.

## Lo que NO hace

No te dice si el examen está bien diseñado, ni si las preguntas son las correctas. Solo te dice si
el examen **se repite a sí mismo**. Eso es un requisito mínimo, no una garantía de que el examen
sea bueno — pero sin ese mínimo, nada de lo demás importa.
