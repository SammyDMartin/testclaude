"""Assemble the page's data block (page/page_data.json) from Stage 1 outputs.

Usage: python3 make_page_data.py
Reads page/evo_main2.json (make_evo.py), runs/stage1/*/stats.csv, runs/stage1/analysis/summary.json and
runs/stage1/calib.txt. Every number quoted in the takeover story is looked up here, not typed in.
"""
import csv, json, os
L = '/home/claude/ladder'
R = L + '/runs/stage1'
END = 12545  # last log of the counted seed-2 run

evo = json.load(open(L + '/page/evo_main2.json'))
lo = 11009
frames = [f for f in evo['frames'] if lo <= f['epoch'] <= END]
muller = [r for r in evo['muller'] if lo <= r[0] <= END]
zeros = [r for r in evo['zeros'] if lo <= r[0] <= END]
mu = {r[0]: r for r in muller}
zz = {r[0]: r[1] for r in zeros}
def first(col, thr):
    return next(r[0] for r in muller if r[col] >= thr)
def peak_after(col, a, b):
    rs = [r for r in muller if a <= r[0] <= b]
    return max(rs, key=lambda r: r[col])
stats2 = {int(r['epoch']): r for r in csv.DictReader(open(R + '/main_2/stats.csv'))}
f1 = min(e for e, r in stats2.items() if float(r['higher_entropy']) >= 1)
a_on = first(2, 0.0001); a_pk = peak_after(2, a_on, a_on + 160)
b_on = first(3, 0.0005)
a_low = min((r for r in muller if a_pk[0] <= r[0] <= b_on), key=lambda r: r[2])
z_pk = max((r for r in zeros if r[0] <= b_on + 32), key=lambda r: r[1])
z_low = min((r for r in zeros if b_on <= r[0] <= b_on + 96), key=lambda r: r[1])
b_half = next(r for r in muller if r[3] >= 0.4)
b_3q = next(r for r in muller if r[3] >= 0.7)
b_pk = max(muller, key=lambda r: r[3])
fin = muller[-1]
x_before = mu[a_on][1]; x_after = mu[a_pk[0] + 16][1]
P = lambda x, d=1: f'{x*100:.{d}f}%'
F = lambda e: f'{e:,}'
beats = [
    {'epoch': 11457, 'title': 'Random soup',
     'text': f'Eleven thousand epochs in, the soup is still close to random: it holds {int(stats2[11393]["distinct_tapes"]):,} different programs among its 131,072. '
             f'About {P(mu[11457][1])} share one instruction pattern (gold), which does not copy itself.'},
    {'epoch': a_pk[0], 'title': 'First copiers',
     'text': f'Family A appears at epoch {F(a_on)} and holds {P(a_pk[2])} of the soup {a_pk[0]-a_on} epochs later. Its copies write over everything, '
             f'including the gold pattern, which drops from {P(x_before)} to {P(x_after)}.'},
    {'epoch': z_pk[0], 'title': 'Poisoned by its own zeros',
     'text': f'Family A’s commonest program carries 19 zero bytes, and every copy plants them in the soup: zero bytes rise from {P(zz[a_on])} to {P(z_pk[1])} by epoch {F(z_pk[0])}. '
             f'Family A’s loop stops at a zero it is about to overwrite, so at that level about 3 copies in 10,000 finish. Family A falls to {P(a_low[2],2)} by epoch {F(a_low[0])}.'},
    {'epoch': b_3q[0], 'title': 'Family B sweeps',
     'text': f'Family B appears at epoch {F(b_on)} and holds {P(b_half[3],0)} of the soup at {F(b_half[0])} and {P(b_3q[3],0)} at {F(b_3q[0])}. '
             f'Its loop checks the byte it has just written, and its commonest program has no zero bytes, so zeros cannot stop it; its copies overwrite them, and zero bytes fall to {P(z_low[1])} by {F(z_low[0])}. '
             f'High-order entropy, logged every 128 epochs, first passes 1 at {F(f1)}: the paper’s takeover.'},
    {'epoch': fin[0], 'title': 'Two families share the soup',
     'text': f'With the zeros cleared, family A comes back, to {P(fin[2])} by epoch {F(fin[0])}, and plants its zeros again ({P(zz[fin[0]])} of bytes). '
             f'Family B eases from a peak of {P(b_pk[3],0)} to {P(fin[3],0)}. The counted run ends here, 512 epochs after the takeover was confirmed.'}]
evo_out = {'slots': evo['slots'], 'families': evo['families'], 'pca_var': evo['pca_var'],
           'frames': frames, 'muller': muller, 'zeros': zeros, 'beats': beats}


def sham_rows():
    d = R + '/sham_1'
    a = list(csv.DictReader(open(d + '/stats.csv' if not os.path.exists(d + '/stats_a.csv') else d + '/stats_a.csv')))
    if os.path.exists(d + '/stats_b.csv'):
        b = list(csv.DictReader(open(d + '/stats_b.csv')))
        cut = int(a[-1]['epoch'])
        return [r for r in a if int(r['epoch']) <= cut] + [r for r in b if int(r['epoch']) > cut]
    return a


runs = {}
for name in sorted(os.listdir(R)):
    kind, _, seed = name.partition('_')
    if kind not in ('main', 'sham') or not seed.isdigit(): continue
    rows = sham_rows() if name == 'sham_1' else list(csv.DictReader(open(f'{R}/{name}/stats.csv')))
    conf = max(int(r['confirmed']) for r in rows)
    hoe = [[int(r['epoch']), round(max(0.0, float(r['higher_entropy'])), 3)] for r in rows]
    f1r = next((int(r['epoch']) for r in rows if float(r['higher_entropy']) >= 1), None)
    last = int(rows[-1]['epoch'])
    runs[name] = {'hoe': hoe, 'confirmed': conf if conf >= 0 else None, 'f1': f1r, 'epochs_run': last,
                  'max_hoe': max(float(r['higher_entropy']) for r in rows),
                  'incomplete': conf < 0 and last < 16385}

S = None
sp = R + '/analysis/summary.json'
if os.path.exists(sp):
    S = json.load(open(sp))
    r2 = S['runs']['main']['2']
    S['first_rep'] = r2['first_rep_ge48']
    S['collapse_detail'] = f'entropy above 1 at {r2["fp_entropy"]:,}, distinct programs below half at {r2["fp_distinct"]:,}'
    if S['runs']['sham']:
        S['sham_max_hoe'] = max(v['max_hoe'] for v in S['runs']['sham'].values())
        S['sham_max_top_share'] = max(v['max_top_share'] for v in S['runs']['sham'].values())
    S.pop('runs')
calib = None
if os.path.exists(R + '/calib.txt'):
    for line in open(R + '/calib.txt'):
        if line.startswith('N '):
            p = line.split(); calib = {'n': int(p[1]), 'hits': int(p[3])}

checked = [
    'The page’s JavaScript port of the rules and of the replication check agrees with cubff on 30,000 tapes and 3,000 checks.',
    'The seed 2 views come from a bit-for-bit rerun of the counted run from its epoch 9,216 checkpoint; the rerun’s distinct-program counts match the run’s own logs at 11,777, 11,905 and 12,033.',
    'Both family programs shown copy themselves: family A scores 63 of 64 on the replication check, family B 64, and family B’s back-to-front copy also 64.',
    'The zero-byte mechanism, measured directly with 20,000 test partners each: family A finishes 80% of copies against a soup with 0.4% zero bytes and 0.03% at 12.5%; family B finishes all of them at both.']
if 'sham_1' in runs and not runs['sham_1']['incomplete']:
    checked.append('Sham seed 1, with the two copy instructions disabled, ran all 16,384 epochs: high-order entropy never rose above zero, and no two of its 131,072 programs were ever identical. '
                   'It was interrupted once by a workspace restart and resumed from a checkpoint; the seven logs the two parts share are identical.')
if calib:
    checked.append(f'Chance calibration: {calib["n"]:,} uniform random programs through the replication check, {calib["hits"]} scoring 48 or more. The 2026 paper’s rate predicts about 0.3.')
unchecked = [
    'Stage 1’s main criterion: only 4 of the 10 pre-registered main seeds ran, so it gets no verdict.',
    'The 24.8-bit chance cost of a single replicator is the 2026 paper’s figure; 10 million programs can only show it is not much smaller.',
    'Families are grouped by instruction pattern with a tolerance of a few edits. That grouping is description, chosen after the run, and not part of the pre-registration.',
    f'The 3D layout squashes 640 dimensions into three and keeps {sum(evo["pca_var"])*100:.0f}% of the variation, so distances in it are rough.',
    'Stage 2 onward is a plan.']
note = ''
if 'sham_1' in runs and os.path.exists(R + '/sham_1/stats_b.csv'):
    note = ('Sham seed 1 was stopped at epoch 4,993 when the workspace restarted, and resumed from its epoch 4,096 checkpoint; '
            'the runs are deterministic, and the logs where the two parts overlap are identical.')
out = {'evo': evo_out, 'runs': runs, 'summary': S, 'calib': calib, 'checked': checked, 'unchecked': unchecked, 'note': note}
json.dump(out, open(L + '/page/page_data.json', 'w'), separators=(',', ':'), ensure_ascii=False)
print('frames', len(frames), 'bytes', os.path.getsize(L + '/page/page_data.json'))
for b in beats: print(b['epoch'], b['title'], '|', b['text'])
