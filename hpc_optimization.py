import time, csv, math
import numpy as np

sizes = [50_000, 200_000, 1_000_000]
rows = []

print("HPC optimization: AoS (python loop) vs SoA (NumPy)")

for n in sizes:
    rng = np.random.default_rng(42)
    a = rng.random(n); b = rng.random(n); c = rng.random(n)

    aos = list(zip(a.tolist(), b.tolist(), c.tolist()))

    t0 = time.perf_counter()
    s1 = 0.0
    for x, y, z in aos:
        s1 += math.sqrt(x*x + y*y) + 0.001*z
    t1 = time.perf_counter()
    t_aos = t1 - t0

    t0 = time.perf_counter()
    s2 = (np.sqrt(a*a + b*b) + 0.001*c).sum()
    t1 = time.perf_counter()
    t_soa = t1 - t0

    speedup = (t_aos / t_soa) if t_soa > 0 else float("inf")

    print(f"N={n:,}")
    print(f"  AoS loop  : {t_aos:.6f}s (sum={s1:.3f})")
    print(f"  SoA NumPy : {t_soa:.6f}s (sum={float(s2):.3f})")
    print(f"  Speedup   : {speedup:.1f}x\n")

    rows.append({"N": n, "method": "AoS_Python", "time_sec": f"{t_aos:.6f}"})
    rows.append({"N": n, "method": "SoA_NumPy",  "time_sec": f"{t_soa:.6f}"})

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["N","method","time_sec"])
    w.writeheader()
    for r in rows: w.writerow(r)

print("Saved results.csv")

with open("run_summary.txt", "w", encoding="utf-8") as f:
    f.write("HPC optimization: AoS (python loop) vs SoA (NumPy)\n\n")
    for r1, r2 in zip(rows[::2], rows[1::2]):
        n = r1["N"]
        t_aos = float(r1["time_sec"])
        t_soa = float(r2["time_sec"])
        speed = t_aos / t_soa if t_soa > 0 else float("inf")
        f.write(f"N={n}: AoS={t_aos:.6f}s, SoA={t_soa:.6f}s, Speedup={speed:.1f}x\n")
print("Saved run_summary.txt")
