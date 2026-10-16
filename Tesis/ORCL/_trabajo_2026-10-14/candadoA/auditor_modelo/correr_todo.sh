#!/bin/sh
# Reproduce todas las salidas del informe. Ejecutar desde esta carpeta:  sh correr_todo.sh
# Python 3.13 + numpy. Ningún script importa motor_orcl.py (solo lee los JSON y orcl_data.json / resultados_paso9.txt para comparar).
mkdir -p salidas
for s in reproduccion tablas sensibilidad tornado combinados tir_audit dcf_inverso_audit rejilla_diff validar_60 mc_audit mc_audit2 mc_audit3; do
  echo ">>> $s"; python3 -I $s.py > salidas/$s.txt 2>&1
done
