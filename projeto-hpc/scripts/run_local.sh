#!/usr/bin/env bash
set -e

# Ajuste quantos processos e amostras por processo
PROCS=4
SAMPLES_PER_PROC=1000000

echo "[local] Executando com $PROCS processos, $SAMPLES_PER_PROC amostras/proc"
mpirun -np $PROCS python3 src/main.py --samples-per-proc $SAMPLES_PER_PROC
