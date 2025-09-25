#!/bin/bash
#SBATCH --job-name=montecarlo_cpu
#SBATCH --output=results/%x_%j.out
#SBATCH --error=results/%x_%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G
# Ajuste a partição se necessário:
# #SBATCH --partition=cpu

echo "Iniciando job em $(date)"
echo "NTasks=$SLURM_NTASKS"

# Caso o SD exija módulos, descomente e ajuste:
# module load python/3.10 mpi

# Ative seu ambiente se necessário:
# source .venv/bin/activate

# Execute com mpi
srun python3 src/main.py --samples-per-proc 1000000
echo "Finalizado em $(date)"
