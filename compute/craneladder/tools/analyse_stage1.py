"""Stage 1 analysis exactly as pre-registered (compute/craneladder/prereg/stage1.md).

Usage: python3 analyse_stage1.py RUNS_DIR CALIB_TXT OUT_DIR
RUNS_DIR holds main_<seed>/ and sham_<seed>/ folders with stats.csv. Writes summary.json and ledger.jsonl.
"""
import csv, json, math, os, sys

runs, calib, out = sys.argv[1], sys.argv[2], sys.argv[3]
N_PROGRAMS, N_BYTES = 131072, 131072 * 64


def wilson(k, n, z=1.96):
    if n == 0: return (0.0, 1.0)
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d; h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def one(path):
    rows = list(csv.DictReader(open(path)))
    if not rows: return None
    conf = max(int(r['confirmed']) for r in rows)
    f1 = next((int(r['epoch']) for r in rows if float(r['higher_entropy']) >= 1.0), None)
    f2 = next((int(r['epoch']) for r in rows if int(r['distinct_tapes']) < N_PROGRAMS // 2), None)
    last = rows[-1]
    fr = [int(r['first_rep']) for r in rows if 'first_rep' in r and r['first_rep'] not in (None, '')]
    first_rep = max(fr) if fr and max(fr) >= 0 else None
    return {'epochs_run': int(last['epoch']), 'confirmed': conf if conf >= 0 else None,
            'counted': conf >= 0 and f1 is not None and f1 <= 16384, 'first_rep_ge48': first_rep,
            'fp_entropy': f1, 'fp_distinct': f2,
            'distinct_collapse_within_512': (None if conf < 0 else (f2 is not None and abs(f1 - f2) <= 512)),
            'max_hoe': max(float(r['higher_entropy']) for r in rows),
            'max_top_share': max(float(r['top_share']) for r in rows),
            'max_sample_ge48': max(int(r['sample_ge_thr']) for r in rows),
            'final_top_hex': last['top_hex'], 'final_top_score': int(last['top_score'])}


res = {'main': {}, 'sham': {}}
for d in sorted(os.listdir(runs)):
    kind, _, seed = d.partition('_')
    p = os.path.join(runs, d, 'stats.csv')
    if kind in res and os.path.exists(p):
        res[kind][int(seed)] = one(p)

k = sum(1 for r in res['main'].values() if r and r['counted'])
n = len(res['main'])
ks = sum(1 for r in res['sham'].values() if r and r['counted'])
k48 = sum(1 for r in res['main'].values() if r and r['counted'] and r['first_rep_ge48'] is not None)
fp_all = [r['distinct_collapse_within_512'] for r in res['main'].values() if r and r['counted']]
hits = None
if os.path.exists(calib):
    for line in open(calib):
        if line.startswith('N '): hits = int(line.split()[3])
lo, hi = wilson(k, n)
summary = {
    'main_takeovers': f'{k} of {n}', 'main_wilson95': [round(lo, 3), round(hi, 3)],
    'pass_takeover': k >= 2, 'takeovers_with_a_48_replicator': k48, 'distinct_collapse_per_takeover': fp_all,
    'sham_takeovers': f'{ks} of {len(res["sham"])}', 'calibration_hits_in_1e7': hits,
    'pass_calibration': hits is not None and hits <= 3, 'runs': res}
if n < 10:  # amendment 1: curtailed at 4 of the 10 planned main seeds, so the 2-of-10 criterion gets no verdict
    summary['pass_takeover'] = None
    summary['takeover_verdict'] = f'none: curtailed at {n} of 10 main seeds (amendment 1)'
os.makedirs(out, exist_ok=True)
json.dump(summary, open(os.path.join(out, 'summary.json'), 'w'), indent=1)
P = k / n if n else 0
ledger = [
    {'rung': 'copiers', 'stage': 1, 'target': 'T_HOE: soup high-order entropy > 1 bit/byte',
     'SC_u_bits': N_BYTES, 'SC_method': 'counting bound (brotli is uniquely decodable)',
     'P_dyn': f'{k}/{n}', 'P_dyn_wilson95': [round(lo, 3), round(hi, 3)],
     'I_plus_bits': (round(N_BYTES - math.log2(1 / P), 1) if P > 0 else None),
     'D_physics_bits': 'pending Stage 2', 'D_class_bits': 3184, 'D_tuning_bits': 0.0, 'D_injected_bits': 0,
     'sham': {'lang': 'bff_nocopy', 'P_dyn': f'{ks}/{len(res["sham"])}'}},
    {'rung': 'copiers', 'stage': 1, 'target': 'T_rep: a program scoring >= 48/64 on CheckSelfRep',
     'SC_u_bits': round(math.log2(2.9e7), 1), 'SC_method': 'cited (Knierim et al. 2026); calibration hits in 1e7: %s' % hits,
     'P_dyn': 'see T_HOE', 'D_physics_bits': 'pending Stage 2'}]
with open(os.path.join(out, 'ledger.jsonl'), 'w') as f:
    for row in ledger: f.write(json.dumps(row) + '\n')
print(json.dumps({k2: v for k2, v in summary.items() if k2 != 'runs'}, indent=1))
