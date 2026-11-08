"""Evolution data for the page from one takeover run: families (Muller plot) and program space (3D).

Usage: python3 make_evo.py RUN_DIR SEED CKPT_EPOCH END_EPOCH OUT_JSON
Reruns the run bit-exactly from the checkpoint, saving every 16 epochs, then for each kept frame:
  - families: every program's instruction skeleton (its instruction bytes in order, no-ops dropped).
    Skeletons are grouped into families by edit distance; the commonest program of each family is
    tested with the replication check (via the JavaScript port, which matches cubff exactly).
  - program space: 2,000 fixed soup slots, each program one-hot encoded by instruction at each position,
    projected to 3D by PCA fitted across frames.
"""
import base64, collections, glob, json, os, shutil, struct, subprocess, sys
import numpy as np

run, seed, ck, end, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
CUBFF = '/home/claude/ladder/ext/cubff/bin/main'
OPS = [60, 62, 123, 125, 43, 45, 46, 44, 91, 93]          # < > { } + - . , [ ]
GLYPH = {60: '<', 62: '>', 123: '{', 125: '}', 43: '+', 45: '-', 46: '.', 44: ',', 91: '[', 93: ']'}
tmp = os.path.join(run, 'evo_ckpt')
if not os.environ.get('REUSE'):
    shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    subprocess.run([CUBFF, '--lang', 'bff_noheads', '--seed', str(seed), '--load', os.path.join(run, 'ckpt', '%010d.dat' % ck),
                    '--max_epochs', str(end), '--print_interval', '16', '--save_interval', '16',
                    '--checkpoint_dir', tmp, '--disable_output'], check=True)

def load(p):
    with open(p, 'rb') as f:
        _, n, ep = struct.unpack('<QQQ', f.read(24))
        return ep, np.frombuffer(f.read(), dtype=np.uint8).reshape(n, 64)

files = sorted(glob.glob(os.path.join(tmp, '*.dat')))
isop = np.zeros(256, bool); isop[OPS] = True
opidx = np.full(256, -1, np.int16)
for i, o in enumerate(OPS): opidx[o] = i

def skeletons(soup):
    m = isop[soup]
    return [bytes(r[mm]) for r, mm in zip(soup, m)]

# pass 1: skeleton counts per frame
frames = []
for p in files:
    ep, soup = load(p)
    if ep < ck + 1: continue
    sk = skeletons(soup)
    frames.append((ep, p, collections.Counter(sk)))
    print('frame', ep, 'distinct skeletons', len(frames[-1][2]), flush=True)

# candidate skeletons: any that reached 0.2% of the soup in some frame
n = 131072
peak = collections.Counter()
for ep, p, c in frames:
    for k, v in c.items():
        if v > peak[k]: peak[k] = v
cands = [k for k, v in peak.items() if v >= 0.002 * n and len(k) >= 3]
cands.sort(key=lambda k: -peak[k])
cands = cands[:400]

def lev(a, b, cap=6):
    if abs(len(a) - len(b)) > cap: return cap + 1
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * len(b)
        best = cur[0]
        for j, cb in enumerate(b, 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb))
            best = min(best, cur[j])
        if best > cap: return cap + 1
        prev = cur
    return prev[-1]

parent = list(range(len(cands)))
def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]; i = parent[i]
    return i
for i in range(len(cands)):
    for j in range(i):
        if find(i) != find(j) and lev(cands[i], cands[j]) <= max(2, len(cands[i]) // 5):
            parent[find(i)] = find(j)
groups = collections.defaultdict(list)
for i, k in enumerate(cands): groups[find(i)].append(k)
fam_of = {}
fams = []
for root, ks in groups.items():
    fams.append(ks)
# order families by first epoch they exceed 1% of soup, then by peak
def fam_share(ks, c): return sum(c.get(k, 0) for k in ks) / n
info = []
for ks in fams:
    shares = [fam_share(ks, c) for ep, p, c in frames]
    if max(shares) < 0.01: continue
    first = next(frames[i][0] for i, s in enumerate(shares) if s >= 0.01)
    info.append((first, -max(shares), ks, shares))
info.sort()
info = info[:6]

# representative program of each family: commonest full program whose skeleton is the family's top skeleton
reps = []
for first, negpk, ks, shares in info:
    best_i = int(np.argmax(shares)); ep, p, c = frames[best_i]
    _, soup = load(p)
    top_sk = max(ks, key=lambda k: c.get(k, 0))
    rows = [r for r in soup if bytes(r[isop[r]]) == top_sk]
    progs, counts = np.unique(np.array(rows), axis=0, return_counts=True)
    reps.append(progs[counts.argmax()].tobytes().hex())
js = subprocess.run(['node', '-e', '''
const B=require("/home/claude/ladder/page/engine.js");
const hs=JSON.parse(process.argv[1]);
console.log(JSON.stringify(hs.map(h=>{const p=Uint8Array.from(Buffer.from(h,"hex"));return Math.min(...[1,2,3].map(s=>B.selfrep(p,s)));})));
''', json.dumps(reps)], capture_output=True, text=True, check=True)
scores = json.loads(js.stdout)
for k, (first, negpk, ks, shares) in enumerate(info):
    for s in ks: fam_of[s] = k
    print('family', k, 'first', first, 'peak %.3f' % -negpk, 'skeletons', len(ks), 'score', scores[k],
          ''.join(GLYPH[b] for b in bytes.fromhex(reps[k]) if b in GLYPH), flush=True)

# pass 2: program space, fixed 2,000 slots
rng = np.random.default_rng(seed)
slots = np.sort(rng.choice(n, 2000, replace=False))
def onehot(progs):
    X = np.zeros((len(progs), 64 * 10), np.float32)
    oi = opidx[progs]
    r, c = np.nonzero(oi >= 0)
    X[r, c * 10 + oi[r, c]] = 1
    return X
keep = [f for f in frames if (f[0] - frames[0][0]) % 32 == 0 or 11400 <= f[0] <= 12000]
feats, fam_ids = [], []
for ep, p, c in keep:
    _, soup = load(p)
    progs = soup[slots]
    feats.append(onehot(progs))
    fam_ids.append([fam_of.get(bytes(r[isop[r]]), 255) for r in progs])
fit = np.concatenate([feats[i] for i in range(0, len(feats), 3)])
mu = fit.mean(0)
U, S, Vt = np.linalg.svd(fit - mu, full_matrices=False)
W = Vt[:3].T
P = [ (f - mu) @ W for f in feats ]
scale = max(np.abs(x).max() for x in P) / 127.0
out_frames = []
for (ep, p, c), x, fi in zip(keep, P, fam_ids):
    q = np.clip(np.round(x / scale), -127, 127).astype(np.int8)
    out_frames.append({'epoch': int(ep), 'xyz': base64.b64encode(q.tobytes()).decode(),
                       'fam': base64.b64encode(bytes(fi)).decode(),
                       'shares': [round(fam_share(ks, c), 4) for (_, _, ks, _) in info]})
data = {'seed': seed, 'n': n, 'slots': len(slots), 'families': [
            {'first': int(first), 'peak': round(-negpk, 3), 'rep': reps[k], 'score': scores[k],
             'skeleton': ''.join(GLYPH[b] for b in bytes.fromhex(reps[k]) if b in GLYPH)}
            for k, (first, negpk, ks, shares) in enumerate(info)],
        'muller': [[int(ep)] + [round(fam_share(ks, c), 4) for (_, _, ks, _) in info] for ep, p, c in frames],
        'frames': out_frames, 'pca_var': [round(float(v), 4) for v in (S[:3] ** 2 / (S ** 2).sum())]}
json.dump(data, open(out, 'w'), separators=(',', ':'))
print('frames', len(out_frames), 'muller points', len(data['muller']), 'bytes', os.path.getsize(out))
