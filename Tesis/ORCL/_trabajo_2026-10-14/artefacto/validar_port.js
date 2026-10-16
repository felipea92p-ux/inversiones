const M = require('./motor.js'); const casos = require('./casos_validacion.json');
let maxd = 0, maxt = 0;
for (const c of casos) {
  const r = M.run(c.cfg); const t = M.irr10(c.cfg, 130.55);
  maxd = Math.max(maxd, Math.abs(r.vps - c.vps), Math.abs(r.ev - c.ev) / 1000);
  maxt = Math.max(maxt, Math.abs(t - c.tir));
}
console.log('casos', casos.length, '| max |dVPS| =', maxd.toExponential(2), '| max |dTIR| =', maxt.toExponential(2));
process.exit(maxd < 1e-6 && maxt < 1e-6 ? 0 : 1);
