import os
import sys
import time
from datetime import datetime

class Timer:
    def __init__(self):
        self.t0 = None
        self.t1 = None
    def start(self):
        self.t0 = time.time()
    def stop(self):
        self.t1 = time.time()
        return self.elapsed
    @property
    def elapsed(self):
        if self.t0 is None:
            return 0.0
        end = self.t1 if self.t1 is not None else time.time()
        return end - self.t0

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def log(msg: str, rank: int = 0, prefix: str = "INFO"):
    # imprime já identificado por rank
    sys.stdout.write(f"[{prefix}][rank={rank}] {msg}\n")
    sys.stdout.flush()

def append_csv(path, header: str, row: str):
    exists = os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if not exists:
            f.write(header.strip() + "\n")
        f.write(row.strip() + "\n")

def now_ts():
    return datetime.now().isoformat(timespec="seconds")
