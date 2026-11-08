"""Merge sham seed 1's two log parts (stopped at 4,993 by a workspace restart, resumed from the 4,096 checkpoint).
The overlapping logs must be identical, since cubff is deterministic per epoch. Writes stats.csv and log.csv merged,
keeping the parts as stats_a.csv / stats_b.csv and log_a.csv / log_b.csv."""
import os, shutil
d = '/home/claude/ladder/runs/stage1/sham_1'
for name in ('stats', 'log'):
    a_path = f'{d}/{name}_a.csv' if os.path.exists(f'{d}/{name}_a.csv') else f'{d}/{name}.csv'
    if a_path.endswith(f'{name}.csv'):
        shutil.copy(a_path, f'{d}/{name}_a.csv'); a_path = f'{d}/{name}_a.csv'
    A = open(a_path).read().splitlines(); Bl = open(f'{d}/{name}_b.csv').read().splitlines()
    assert A[0] == Bl[0], 'headers differ'
    key = lambda l: l.split(',')[0]
    a_rows = {key(l): l for l in A[1:]}; b_rows = {key(l): l for l in Bl[1:]}
    overlap = sorted(set(a_rows) & set(b_rows), key=int)
    same = [k for k in overlap if a_rows[k] == b_rows[k]]
    print(name, 'overlap logs', len(overlap), 'identical', len(same), overlap[:1], overlap[-1:])
    assert len(same) == len(overlap) and overlap, 'overlap mismatch'
    cut = max(int(k) for k in a_rows)
    merged = [A[0]] + A[1:] + [l for l in Bl[1:] if int(key(l)) > cut]
    open(f'{d}/{name}.csv', 'w').write('\n'.join(merged) + '\n')
    print(name, 'merged rows', len(merged) - 1, 'last', key(merged[-1]))
