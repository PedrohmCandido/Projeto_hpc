from mpi4py import MPI
import argparse
import numpy as np
from utils import Timer, ensure_dir, log, append_csv, now_ts

def estimate_pi(samples: int, seed: int) -> int:
    rng = np.random.default_rng(seed)
    xs = rng.random(samples)
    ys = rng.random(samples)
    inside = np.count_nonzero(xs*xs + ys*ys <= 1.0)
    return inside

def parse_args():
    p = argparse.ArgumentParser(
        description="Estimativa de π por Monte Carlo (MPI)"
    )
    p.add_argument("--samples-per-proc", type=int, default=1_000_000,
                   help="Número de amostras geradas por processo (default: 1e6)")
    p.add_argument("--results-dir", type=str, default="results",
                   help="Pasta para salvar métricas/logs")
    p.add_argument("--metrics-csv", type=str, default="results/metrics.csv",
                   help="Arquivo CSV de métricas")
    p.add_argument("--seed", type=int, default=1234,
                   help="Semente base do RNG")
    return p.parse_args()

def main():
    args = parse_args()

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    timer = Timer()
    if rank == 0:
        ensure_dir(args.results_dir)
        log(f"Início: procs={size}, samples/proc={args.samples_per_proc}", rank)


    comm.Barrier()
    timer.start()

    local_inside = estimate_pi(args.samples_per_proc, seed=args.seed + 1000*rank)
    local_total = args.samples_per_proc

    total_inside = comm.reduce(local_inside, op=MPI.SUM, root=0)
    total_samples = comm.reduce(local_total, op=MPI.SUM, root=0)


    comm.Barrier()
    elapsed = timer.stop()

    if rank == 0:
        pi_est = 4.0 * (total_inside / total_samples)
        throughput = total_samples / elapsed if elapsed > 0 else 0.0
        msg = (f"π≈{pi_est:.6f} | tempo={elapsed:.3f}s | procs={size} | "
               f"samples_total={total_samples} | throughput={throughput:,.0f} pts/s")
        log(msg, rank=0)

        header = "timestamp,procs,samples_total,pi_est,tempo_s,throughput_pts_s"
        row = f"{now_ts()},{size},{total_samples},{pi_est:.8f},{elapsed:.6f},{throughput:.2f}"
        append_csv(args.metrics_csv, header, row)

if __name__ == "__main__":
    main()
