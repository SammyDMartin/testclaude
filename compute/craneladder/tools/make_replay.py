"""Build the page's replay JSON from one cubff run that reached takeover.

Usage: python3 make_replay.py RUN_DIR SEED LANG OUT_JSON [CAPTION]
RUN_DIR holds stats.csv (crane-ladder stats log) and ckpt/ (checkpoints every 1024 epochs).
The run is replayed exactly from the last checkpoint before the rise, saving every 16 epochs,
because cubff's shuffling and mutation are seeded per epoch and so reproduce bit for bit.
"""
import base64, csv, glob, json, os, struct, subprocess, sys, shutil
import numpy as np

run, seed, lang, out = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
caption = sys.argv[5] if len(sys.argv) > 5 else ''
CUBFF = '/home/claude/ladder/ext/cubff/bin/main'
rows = list(csv.DictReader(open(os.path.join(run, 'stats.csv'))))
stats = [[int(r['epoch']), round(float(r['higher_entropy']), 4), round(float(r['top_share']), 5),
          int(r['sample_ge_thr']), int(r['distinct_tapes'])] for r in rows]
confirmed = max(int(r['confirmed']) for r in rows)
assert confirmed > 0, 'no confirmed takeover in this run'
# onset: first log where the commonest program holds 0.1% of the soup or a sampled program scores 48
onset = next(s[0] for s in stats if s[2] >= 0.001 or s[3] > 0)
start = max(0, onset - 1536)
ck_epochs = sorted(int(os.path.basename(p)[:-4]) for p in glob.glob(os.path.join(run, 'ckpt', '*.dat')))
ck = max([e for e in ck_epochs if e <= start] or [ck_epochs[0]])
end = confirmed + 512
tmp = os.path.join(run, 'replay_ckpt')
shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
subprocess.run([CUBFF, '--lang', lang, '--seed', str(seed), '--load', os.path.join(run, 'ckpt', '%010d.dat' % ck),
                '--max_epochs', str(end), '--print_interval', '16', '--save_interval', '16',
                '--checkpoint_dir', tmp, '--disable_output'], check=True)
files = sorted(glob.glob(os.path.join(tmp, '*.dat')))
rng = np.random.default_rng(seed)
pick = None
frames = []
# frame schedule: dense around the rise, sparse elsewhere; about 60 frames
eps = [int(os.path.basename(p)[:-4]) for p in files]
want = set()
span = max(1, end - start)
for e in eps:
    if e < start: continue
    if onset - 256 <= e <= confirmed + 64: want.add(e) if (e - start) % 32 == 0 else None
    elif (e - start) % 128 == 0: want.add(e)
for p, e in zip(files, eps):
    if e not in want: continue
    with open(p, 'rb') as f:
        reset_index, n, ep = struct.unpack('<QQQ', f.read(24))
        soup = np.frombuffer(f.read(), dtype=np.uint8).reshape(n, 64)
    if pick is None:
        pick = np.sort(rng.choice(n, 96, replace=False))
    tapes, counts = np.unique(soup, axis=0, return_counts=True)
    share = counts.max() / n
    frames.append({'epoch': int(ep), 'share': round(float(share), 5),
                   'tapes': base64.b64encode(soup[pick].tobytes()).decode()})
# specimen: commonest program at the end of the run
with open(files[-1], 'rb') as f:
    _, n, _ = struct.unpack('<QQQ', f.read(24)); soup = np.frombuffer(f.read(), dtype=np.uint8).reshape(n, 64)
tapes, counts = np.unique(soup, axis=0, return_counts=True)
spec = tapes[counts.argmax()]
shutil.rmtree(tmp, ignore_errors=True)
data = {'seed': seed, 'lang': lang, 'n': int(n), 'onset': onset, 'confirmed': confirmed, 'tick': 1024,
        'stats': [s for s in stats if s[0] <= end], 'frames': frames, 'specimen': spec.tobytes().hex(),
        'specimen_share': round(float(counts.max() / n), 4), 'caption': caption}
json.dump(data, open(out, 'w'), separators=(',', ':'))
print(f'onset {onset} confirmed {confirmed} checkpoint {ck} frames {len(frames)} specimen share {counts.max()/n:.3f} bytes {os.path.getsize(out)}')
