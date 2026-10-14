# Tipos de documento y flujos de actualización

> Rescatado de la versión en nube (snapshot 2026-07-01), traducido y podado.
> **Excluido a propósito:** el "Documento ejecutivo Economist-style (CAYLA / general)" que traía
> la nube. Esta skill es SOLO de inversión. Para documentos de CAYLA, otra herramienta.

La Ultra Tesis completa (esqueleto de 13 secciones) vive en `estructura.md`. Aquí van los otros
dos documentos y los dos flujos de mantenimiento.

---

## Documento B · Informe de portafolio (IBKR)

1. **Portada compacta** (o cabecera con bandera en pág. 1): fecha, NAV, % efectivo, nº de posiciones.
2. **Cuadro de mando del portafolio:** tabla de posiciones principales (cantidad / precio / valor /
   peso / P&L). **Datos vivos por MCP IBKR — jamás de memoria.** Esto no es preferencia de estilo:
   es la disciplina de datos del ADN.
3. **Asignación:** gráficos de geografía y sector (adaptar los tipos 02 y 04 del catálogo).
4. **Confrontación de sesgos** — sección OBLIGATORIA, y la razón de ser del informe:
   concentración real vs tesis escritas, capital en período de prueba, banderas de sunk cost,
   gates pendientes con sus fechas. Sin esta sección el informe es un extracto de bróker con
   mejor tipografía.
5. **Acciones y calendario:** decisiones numeradas, cada una con responsable, fecha y gatillo.
6. **Advertencias** (breve).

**Solo análisis: nunca ejecutar ni recomendar ejecutar operaciones automáticamente.**

Gráficos: subconjunto del catálogo — 02, 04, 09, 14 adaptados a cartera. No los 20.

---

## Flujo 2 · Actualización trimestral (tras resultados)

1. Traer las fuentes primarias del trimestre (8-K / nota de prensa / carta **primero**;
   transcript después; prensa nunca como HECHO).
2. Recalcular el **Cuadro de Mando semáforo** — todos los indicadores, estado nuevo contra umbral,
   destacando los puntos que cambian de color.
3. Contrastar **cada gatillo de §11** contra el dato nuevo. Si alguno se dispara → saltar al Flujo 3.
4. Actualizar: KPIs, gráficos con los puntos nuevos, inputs de §8 si el consenso o el precio
   cambiaron de zona, y la próxima fecha de revisión.
5. **Entregable:** por defecto **(a)** un PDF corto e independiente "Actualización T# 20XX"
   (3-6 págs: cuadro de mando + qué cambió + confirmación o cambio de veredicto). Solo **(b)** una
   reconstrucción completa a v1.X si el veredicto o las zonas cambiaron. Preguntar únicamente si
   es ambiguo.
6. La línea de veredicto debe decir explícitamente: **CONFIRMADO / AJUSTADO / EN REVISIÓN**.

---

## Flujo 3 · Re-análisis por gatillo disparado o caída >20%

Re-puntuación completa obligatoria — **no un parche**.

1. Nombrar en la primera línea el gatillo que se disparó (o el drawdown), con dato y fecha.
2. **Re-correr la rúbrica de calidad desde cero**, sin anclarse a los scores previos. Anotar cada
   regla cuyo score se movió y por qué. (Motor de calidad: `qg-seilern` — o `rabitt-uqg` cuando
   pase su prueba de aceptación. Esta skill NUNCA puntúa calidad por su cuenta.)
3. Re-valorar con los inputs actualizados; recalcular PWFV y zonas (motor: `val-mos`).
4. **Juicio estructural vs cíclico** — la disciplina de la casa: *la caída del precio NO es
   evidencia.* Solo el deterioro en las métricas falsables lo es.
5. Veredicto de salida: **MANTENER / REDUCIR X% / SALIDA ORDENADA / ACUMULAR**, con el mapa de
   zonas y los gatillos actualizados.
6. Entregable: PDF "Re-análisis \<TICKER\>" (8-15 págs), o tesis completa v2 si el veredicto giró.

> Enlace con el ADN: un drawdown >25% desde máximo histórico o de 52 semanas dispara además la
> pregunta de Li Lu — *¿esta caída pone a prueba la autenticidad del círculo de competencia?* Esa
> pregunta se responde en el documento, no se omite.
