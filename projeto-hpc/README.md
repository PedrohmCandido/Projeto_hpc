# Projeto HPC — Estimativa de π por Monte Carlo (MPI)

## Visão geral
Estimamos π por simulação de Monte Carlo: geramos pontos aleatórios no quadrado [0,1]×[0,1] e contamos a fração que cai dentro do círculo de raio 1 (x² + y² ≤ 1). 
O algoritmo é “embaraçosamente paralelo”: cada processo gera um conjunto de pontos e retorna contagens locais.

**Métricas principais:** tempo total, throughput (pontos/s), speedup e eficiência (variando nº de processos).

## Requisitos
- Python 3.10+
- `mpi4py` (MPI instalado: OpenMPI/MPICH)
- (Opcional) NumPy para RNG mais rápido
- SLURM (no Santos Dumont)

Instalação local:

python3 -m venv .venv && source .venv/bin/activate
pip install -r env/requirements.txt


Como rodar (local)

scripts/build.sh
scripts/run_local.sh

Altere SAMPLES_PER_PROC em scripts/run_local.sh para variar o tamanho.

Como rodar (Santos Dumont)

Crie/ative seu ambiente e instale deps (ou use módulos do SD).

Ajuste módulos (se necessário) dentro do job_cpu.slurm.

Submeta o job:

sbatch scripts/job_cpu.slurm

Acompanhe:

squeue -u $USER
tail -f results/*.out

Estrutura

src/main.py: código MPI (mpi4py) para Monte Carlo.

src/utils.py: utilitários (timer, logging por rank).

scripts/*.sh: build, execução local, submissão SLURM, perfilamento.

results/: logs e métricas (metrics.csv).

report/RELATORIO.md: esqueleto do relatório (5–8 págs).

Resultados

results/metrics.csv: (timestamp, procs, samples_total, pi_est, tempo_s, throughput_pts_s).

Rodar com 1, 2, 4, 8, 16 processos e comparar speedup/eficiência.