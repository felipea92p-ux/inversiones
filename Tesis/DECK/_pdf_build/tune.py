# -*- coding: utf-8 -*-
"""Afina COLAS en build.py hasta que no queden viudas de final de seccion."""
import re, subprocess, sys, fitz, json
BUILD = "build.py"
PDF = ("/Users/felipealvarez/Library/Mobile Documents/com~apple~CloudDocs/"
       "INVESTMENTS/Tesis/DECK/2026-08-25_Ultra_Tesis_DECK.pdf")

def set_colas(d):
    s = open(BUILD).read()
    s = re.sub(r"^COLAS = \{.*?\}$", "COLAS = " + json.dumps(d, ensure_ascii=False),
               s, flags=re.M | re.S)
    open(BUILD, "w").write(s)

def build():
    r = subprocess.run([sys.executable, "build.py"], capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-2000:], r.stderr[-3000:]); raise SystemExit("build fallo")
    return int(re.search(r"\((\d+) paginas\)", r.stdout).group(1))

def medir():
    d = fitz.open(PDF); out = []
    for i, p in enumerate(d, 1):
        bl = [b for b in p.get_text("blocks") if b[1] > 45 and b[3] < 800]
        if not bl:
            out.append((i, 0.0, "")); continue
        alto = max(b[3] for b in bl) - min(b[1] for b in bl)
        out.append((i, round(100 * alto / 731, 1),
                    " ".join(b[4].replace("\n", " ") for b in bl)[:60]))
    d.close(); return out

if __name__ == "__main__":
    colas = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
    set_colas(colas)
    n = build()
    m = medir()
    flojas = [(i, o, t) for i, o, t in m if o < 22]
    print(f"PAGINAS: {n}   ·   paginas por debajo del 22%: {len(flojas)}")
    for i, o, t in flojas:
        print(f"  p.{i:>3}  {o:>5.1f}%  {t}")
