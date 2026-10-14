# El libro mayor — esquema, procedencia, autoridad, frescura, anti-sesgo, ingesta

El ledger (`INVESTMENTS/Rankings/_ledger.json`) es la fuente única de verdad del ranking. Todo lo que
hace estable al tablero vive aquí. Leer completo antes de tocarlo.

## Esquema

```json
{
  "meta": { "actualizado": "2026-07-10", "version_esquema": 1 },
  "tickers": {
    "MSFT": {
      "name": "Microsoft Corp.",
      "sector": "Software / cloud",
      "calidad": {
        "score": 86.0, "tier": "Núcleo",
        "sub_scores": {"R1":14,"R2":9,"R3":13,"R4":13,"R5":9,"R6":8,"R7":9,"R8":10,"R9":7,"R10":7,"R11":6},
        "procedencia": "tesis-individual", "autoridad": "oro",
        "fecha": "2026-07-09", "fuente": "Tesis/MSFT/2026-07-09_Tesis_Ultra_MSFT_v2.pdf"
      },
      "precio": {
        "zona": "OPORTUNIDAD", "mos_pct": 26, "mos_exigido_pct": 15,
        "pwfv": 520, "precio": 384, "ccy": "USD",
        "detector": "PASA", "dcf_inverso": "RAZONABLES", "veredicto": "COMPRAR TRAMO",
        "procedencia": "tesis-individual", "autoridad": "oro",
        "fecha": "2026-07-09", "fuente": "Tesis/MSFT/..._v2.pdf"
      },
      "max_52s": 555,
      "flags": []
    }
  }
}
```

- `calidad` y `precio` son **ejes independientes** con su propia procedencia/autoridad/fecha. Una
  empresa puede tener calidad oro (tesis) y precio provisional (screening), o al revés.
- `sub_scores` se guarda cuando existe: lo usa la compuerta anti-sesgo y los desempates.
- **Convención de banderas (una sola, no mezclar):** las banderas de la compuerta anti-sesgo viven
  DENTRO de cada eje en `flags_ingesta` (las escribe el sync al ingerir). El campo `flags` a nivel
  ticker guarda solo banderas persistentes de conflicto (`conflicto-empate-<eje>(<fecha>)`) o avisos
  manuales. Las banderas de frescura (`refrescar`) NO se almacenan: se calculan en cada BUILD.
- `estado` (opcional, a nivel ticker): `{"estado": "cuarentena"|"knock-out", "motivo", "fecha",
  "fuente"}`. Se ingiere con un record de `eje: "estado"` y **excluye a la empresa del ranking**
  (se lista aparte con su motivo). Así una cuarentena dictada por una corrida (ej. CPRT 08-jul,
  salida abrupta del CEO) no se pierde entre corridas.
- **Metadatos (`name`/`sector`/`max_52s`):** solo los escribe un record que GANA su eje (o que
  rellena un campo vacío); un record perdedor jamás pisa metadatos, y todo cambio de metadato queda
  en el diff. (Regla anti-corrupción: los candidatos rechazados no deben mutar nada.)

## Escalera de procedencia — 3 niveles

Define qué score gana cuando hay varios para la misma empresa/eje. **La tesis siempre supera al lote.**

| Nivel | `autoridad` | Origen | Qué es |
|---|---|---|---|
| **Oro** | `oro` | `tesis-individual` | Una Tesis Ultra (`ultra-tesis-qg`) o una tesis forjada (`tesis-forja`): documento dedicado, ciclo de verificación adversarial propio. **Máxima confianza.** |
| **Plata** | `plata` | `re-verificado` | Un score de lote que pasó verificación adversarial dedicada (ej. la re-puntuación por Workflow del 10-jul con las 3 compuertas anti-bug). Confiable, pero un escalón bajo la tesis. |
| **Provisional** | `provisional` | `screening` | Un score de cribado rápido, sin verificación adversarial dedicada. **Corre optimista de forma sistemática** (ver `project-qg-screening-vs-tesis-bias` en memoria). Solo tapa huecos, con bandera; no compite de igual a igual. |

## Regla de autoridad (el corazón)

Cuando el sync encuentra un score nuevo para un eje de una empresa que ya está en el ledger:

1. **Gana la autoridad más alta.** Oro > plata > provisional. Un score oro NUNCA es reemplazado por
   uno plata o provisional, aunque el nuevo sea más reciente.
2. **A igual autoridad, gana el más reciente** (fecha mayor).
3. **Empate exacto (misma autoridad, misma fecha, PAYLOAD distinto — se compara el contenido
   completo del eje, no un resumen):** si el vigente viene de una corrida ANTERIOR, se conserva; si
   AMBOS entraron en esta corrida, se elige de forma determinista por contenido (menor serialización
   canónica — cualquier orden de archivos da el mismo resultado) y ese reemplazo cuenta como cambio
   real (`empate-resuelto`). En ambos casos: bandera `conflicto-empate-<eje>(<fecha>)` al ticker y el
   diff dice explícitamente cuál payload quedó vigente. El ledger nunca decide un conflicto real en
   silencio ni por orden de archivo.
4. **Nunca se promedian.** Reconciliar no es mezclar: es elegir el más confiable y descartar el resto.
5. Cada reemplazo se registra en el diff con el motivo (ej. "MA precio: provisional 0.19 asim →
   oro tesis: JUSTO/ESPERAR — la tesis supera al screening").

**Por qué:** el hallazgo de esta casa (23 empresas cruzadas, 21 corregidas a la baja al pasar de
screening a tesis: NOW 83→62, ICE 76→54, MA 86→75) prueba que promediar o dejar ganar al número
fresco-pero-optimista corrompe el ranking. La autoridad es la defensa.

## Autoridad vs. frescura (el conflicto)

Un score oro viejo (stale) vs. un score plata/provisional fresco para la misma empresa/eje:

- **La autoridad manda igual.** Se usa el score oro aunque esté viejo, y se le pone bandera
  `refrescar`. Un número verificado añejo sigue siendo más confiable que un screening fresco optimista.
- La bandera `refrescar` es la señal de que conviene actualizar esa tesis — no una invitación a
  sustituirla por un screening. Se resuelve corriendo `ultra-tesis-qg`/`tesis-forja`, no bajando la
  autoridad.

## Política de frescura (calculada en cada BUILD, no almacenada)

Un score se marca **`refrescar`** si cumple cualquiera de las dos:

1. **Antigüedad:** su `fecha` tiene más de **90 días** respecto a la fecha de corrida (un trimestre —
   alineado con el Cuadro de Mando trimestral del sistema).
2. **Drawdown:** el precio **ACTUAL** cayó **>25% respecto al precio registrado cuando se puntuó ese
   eje** (`precio` del eje). Mide un derrumbe *posterior* al análisis — que es lo que invalida la
   lectura. NO se mide contra `max_52s` a secas: una tesis nueva que ya analizó la caída quedaría
   marcada "refrescar" el día de su publicación, que es ruido. `max_52s` se guarda como contexto.
   **Este gatillo requiere un feed de precios actuales** (`build_ranking.py --precios <json>`,
   `{ticker: precio}` **en la divisa nativa del ticker** — la del campo `ccy` del eje precio; mezclar
   divisas produce drawdowns falsos). Sin feed, el gatillo queda inactivo y el output lo declara —
   nunca se finge que está operativo. **Cobertura parcial declarada:** el eje calidad no guarda precio
   propio; su drawdown usa como referencia el precio del eje precio del mismo ticker, así que una
   empresa sin eje precio solo tiene el gatillo de antigüedad.

La bandera se calcula en cada BUILD **por eje** (una calidad vigente puede convivir con un precio a
refrescar) y se muestra en el ranking; no borra el score ni se almacena en el ledger. El umbral de
días es un parámetro (`--stale-dias`, default 90) por si Felipe quiere otro.

## Compuerta anti-sesgo (al ingerir cualquier score que NO sea oro)

Antes de admitir un score `plata` o `provisional` al ledger, el sync corre los chequeos derivados de
los bugs reales que encontramos en corridas de lote. Cada fallo agrega una bandera; un fallo duro
(1) degrada el score a `provisional` y exige revisión.

1. **Doble conteo aritmético** (bug de Mastercard 88→75) — *automatizado, solo eje calidad*. Con
   `sub_scores` presentes: ninguna nota puede exceder su tope (R1/R3/R4 ≤ 15; resto ≤ 10) ni ser
   negativa; y **solo si las 11 reglas están presentes y son numéricas**, la suma cruda debe coincidir
   con el score declarado (`raw = Σ sub_scores`, `score_100 = raw/125*100`; tolerancia 0,15, o 0,55 si
   el score declarado viene redondeado a entero). Sub_scores incompletos → el chequeo de suma se
   OMITE con bandera `anti-sesgo-sub-scores-incompletos`, nunca se degrada por reglas ausentes.
   Un sub_score no numérico hace que el record se salte como malformado (con aviso), sin abortar el
   sync — el sync es automático y un record roto no puede frenar la corrida entera.
2. **Tope 7/10 disparejo** (bug de NVIDIA) — **NO automatizado**. Requiere leer la evidencia por
   regla, cosa que solo hace una tesis dedicada. El script NO lo chequea; queda cubierto por la
   bandera del punto 3 y por la escalera de autoridad (es una de las razones por las que plata < oro).
3. **Deterioro de divulgación no penalizado** (bug de ServiceNow: dejó de reportar NRR) — cualitativo.
   **Todo record no-oro de AMBOS ejes** (calidad Y precio) entra con la bandera
   `anti-sesgo-divulgacion-no-auditada` en su `flags_ingesta`: el screening de valoración corre tan
   optimista como el de calidad y merece la misma marca.

**Regla de oro de la compuerta:** la compuerta NUNCA sube la confianza de un score; solo la baja o la
marca. Ante la duda, degrada.

## Ingesta — de dónde salen los scores

El sync lee, en orden de autoridad:

- **Oro:** Tesis Ultra en `INVESTMENTS/Tesis/<TICKER>/` (PDF) y sus fuentes en
  `Herramientas/Tesis_src/*/` — los `dcf_<tick>.py` o los JSON de datos de tesis (ej.
  `_batch_gen_*/thirteen_merged.json`, que contiene los DOS ejes de las 13 tesis del 10-jul).
  Tesis forjadas por `tesis-forja` (diario markdown + CSV).
- **Plata:** JSON de corridas re-verificadas adversarialmente en `Rankings/<fecha>/` (ej.
  `Rankings/2026-07-10/gap_rescored_2026-07-10.json`). Plata exige ataque adversarial DEDICADO a esa
  empresa; participar en el lote no basta.
- **Provisional:** JSON de screening/universo en `Rankings/<fecha>/` (ej. `qg_universo77_*.json`).

**Registro `score record`** (formato mínimo que el sync entiende, uno por empresa/eje). Cuando una
tesis existe solo como PDF, extraer de la **portada** AMBOS ejes (que trae todo): nombre, `score
/100`, `tier` — Y TAMBIÉN `PWFV`, `precio`, `zona`, `MoS`, `veredicto` (y `max_52s` si la portada lo
imprime). Guardar como registro estructurado en `Rankings/_score_records/<TICKER>.json` y re-correr
el sync. **No ingerir solo calidad y dejar el precio atrás**: una tesis con PWFV en la portada que
figura como "necesita valoración" en el ranking es un fallo de ingesta, no un hueco real. Ojo con
layouts de portada distintos entre generaciones de tesis (el formato v7/v4.1 de INTU/DUOL escribe
"NN,N / 100" con espacios): validar que la extracción devolvió score para TODAS las tesis listadas, y
tratar un `null` como error a corregir, nunca como "sin dato". Campos que la fuente no trae (ej.
`detector` en portadas viejas) se dejan AUSENTES — jamás se inventan valores uniformes.

**Records de estado** (cuarentenas, knock-outs, banderas): `{"ticker","eje":"estado",
"estado":"cuarentena"|"knock-out","motivo","fecha","fuente"}` o `{"eje":"estado","add_flags":[...]}`.
Las corridas que dicten cuarentena/veto (ej. `discardedNew`/`trapVetoed` de un workflow) deben
ingerirse así para que la decisión persista entre corridas.

**Changelog en la práctica:** el diff se captura EN LA MISMA corrida que escribe el ledger —
`ledger_sync.py --apply --diff-out Rankings/<fecha>/changelog_<fecha>.md`. Capturarlo en una segunda
corrida da un diff vacío (el ledger ya está actualizado) — ese error ya ocurrió una vez; no repetirlo.

**Semilla inicial (una sola vez):** poblar el ledger desde (a) las ~30+ Tesis Ultra existentes en
`Tesis/` como oro, (b) la re-puntuación adversarial más reciente (10-jul) como plata para los huecos,
(c) el universo canónico (07-02) como provisional para el resto. A partir de ahí, cada tesis nueva que
Felipe forje actualiza el ledger vía sync.
