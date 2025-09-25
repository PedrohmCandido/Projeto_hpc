#!/usr/bin/env bash
set -e

# Pequena variação de processos para medir speedup/eficiência localmente.
for p in 1 2 4 8; do
  echo "---- PROCS=$p ----"
  mpirun -np $p python3 src/main.py --samples-per-proc 500000
done

echo "Métricas acumuladas em results/metrics.csv"
