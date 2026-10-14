# -*- coding: utf-8 -*-
"""
prep_ultra.py — normaliza ultra_run_raw.json en ultra_data.json + CSV.
Corrida ULTRA QG (indestructibilidad) del 5-jul-2026.
"""
import json, csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
raw = json.load(open(os.path.join(HERE, "ultra_run_raw.json"), encoding="utf-8"))

NAMES = {
    "MA": ("Mastercard", "Pagos / redes"), "ISRG": ("Intuitive Surgical", "MedTech / robótica"),
    "MSFT": ("Microsoft", "Software / cloud"), "V": ("Visa", "Pagos / redes"),
    "SPGI": ("S&P Global", "Ratings / índices"), "MSCI": ("MSCI", "Índices / analytics"),
    "CSU.TO": ("Constellation Software", "Software vertical"), "NOW": ("ServiceNow", "SaaS / workflow"),
    "NVDA": ("Nvidia", "Semis / IA"), "REL.L": ("RELX", "Datos / analytics"),
    "STMN.SW": ("Straumann", "Implantes dentales"), "ZTS": ("Zoetis", "Salud animal"),
    "IDXX": ("IDEXX Laboratories", "Diagnóstico veterinario"), "ASML": ("ASML", "Semis / litografía"),
    "TSM": ("TSMC", "Semis / foundry"), "0388.HK": ("HK Exchanges", "Bolsas / clearing"),
    "CPRT": ("Copart", "Subastas de salvamento"), "4684.T": ("OBIC", "ERP Japón"),
    "CME": ("CME Group", "Derivados / clearing"), "RMS.PA": ("Hermès", "Lujo"),
    "MCO": ("Moody's", "Ratings / analytics"),
}
GRADO_LABEL = {
    "ULTRA_ALPHA": "ULTRA-α", "ULTRA_BETA": "ULTRA-β",
    "CASI_ULTRA": "CASI-ULTRA", "FUERA": "FUERA",
}

calib = {t["ticker"]: t for t in raw["calibracion"]["tiering"]}

companies = []
for g in raw["gates"]:
    tk = g["ticker"]
    nm, sec = NAMES.get(tk, (g.get("empresa", tk), ""))
    cal = calib.get(tk, {})
    gates = {}
    for k in ["G1", "G2", "G3", "G4", "G5", "G6"]:
        gg = g["gates"][k]
        gates[k] = {"verdict": gg["verdict"], "evidencia": gg["evidencia"], "fuente": gg["fuente"]}
    # correccion calibrada: CPRT G4 FALLA->PASA
    if tk == "CPRT":
        gates["G4"]["verdict"] = "PASA"
        gates["G4"]["evidencia"] = ("[CORREGIDO EN CALIBRACIÓN] Investigación DOJ por AML (carta oct-2023) sin cargos "
            "al 5-jul-2026: mismo estadio procesal que la investigación FTC sobre MSFT (PASA). El criterio del gate "
            "exige caso activo o remedio estructural con probabilidad material, no una investigación. ") + gates["G4"]["evidencia"]
    fall = [k for k in gates if gates[k]["verdict"] == "FALLA"]
    cuar = [k for k in gates if gates[k]["verdict"] == "CUARENTENA"]
    companies.append({
        "ticker": tk, "name": nm, "sector": sec,
        "score": g.get("score"), "origen": g.get("origen"),
        "grado": cal.get("grado"), "grado_label": GRADO_LABEL.get(cal.get("grado"), ""),
        "orden": cal.get("orden", 99), "razon_calibrada": cal.get("razon", ""),
        "gates": gates, "fallas": fall, "cuarentenas": cuar,
        "novedades": g.get("novedades_desde_2jul", ""), "resumen": g.get("resumen", ""),
        "obituarios": raw["obituarios"].get(tk, []),
    })

companies.sort(key=lambda c: (c["orden"], -(c["score"] or 0)))

sweep = []
for s in raw["sweep_scoring"]:
    sc = s.get("scored") or {}
    sweep.append({
        "ticker": s.get("ticker"), "status": s.get("status"), "s100": s.get("s100"),
        "motivo": s.get("motivo"), "scores": sc.get("scores"), "thesis": sc.get("thesis", ""),
        "main_risk": sc.get("main_risk", ""), "flags": sc.get("flags", []),
        "data_confidence": sc.get("data_confidence", ""), "name": sc.get("name", s.get("ticker")),
    })

out = {
    "meta": {
        "titulo": "ULTRA QG — Las Indestructibles", "fecha": "2026-07-05",
        "candidatas": len(companies),
        "alpha": [c["ticker"] for c in companies if c["grado"] == "ULTRA_ALPHA"],
        "casi": [c["ticker"] for c in companies if c["grado"] == "CASI_ULTRA"],
        "fuera": [c["ticker"] for c in companies if c["grado"] == "FUERA"],
    },
    "companies": companies,
    "sweep": sweep,
    "calibracion": raw["calibracion"],
}
json.dump(out, open(os.path.join(HERE, "ultra_data.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

# CSV
with open(os.path.join(HERE, "ULTRA_QG_Indestructibles_2026-07-05.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["# Este score mide CALIDAD del negocio, no valoracion ni margen de seguridad. Score alto != comprar."])
    w.writerow(["orden", "ticker", "empresa", "sector", "score_/100", "grado", "G1", "G2", "G3", "G4", "G5", "G6",
                "gates_fallados", "razon_calibrada"])
    for c in companies:
        w.writerow([c["orden"], c["ticker"], c["name"], c["sector"], c["score"], c["grado_label"]]
                   + [c["gates"][k]["verdict"] for k in ["G1", "G2", "G3", "G4", "G5", "G6"]]
                   + [";".join(c["fallas"]), c["razon_calibrada"]])

print("empresas:", len(companies))
for c in companies:
    print(f"{c['orden']:>2} {c['ticker']:<8} {c['grado_label']:<11} {c['score']} fallas={c['fallas']}")
