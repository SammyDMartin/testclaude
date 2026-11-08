// BFF soup engine: cubff's bff_noheads semantics (instruction pointer and both heads start at 0,
// heads wrap at 128, loops test for byte 0, 8,192-step budget), cubff's mutation rate (2^-12 per byte
// per interaction) and cubff's self-replication check (13 random partners x 5 generations, score 0..64).
// Shared by the offline seed search (node) and the page's Web Worker.
(function (root) {
  const L = 64, T2 = 128, STEPS = 8192, MUT = 1 / 4096;
  function rng(seed) { // mulberry32
    let a = seed >>> 0;
    return function () { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  }
  // returns number of executed (non-noop) instructions
  function evaluate(t) {
    let pc = 0, h0 = 0, h1 = 0, ops = 0;
    for (let i = 0; i < STEPS; i++) {
      h0 &= 127; h1 &= 127;
      const c = t[pc];
      switch (c) {
        case 60: h0--; ops++; break;            // <
        case 62: h0++; ops++; break;            // >
        case 123: h1--; ops++; break;           // {
        case 125: h1++; ops++; break;           // }
        case 43: t[h0] = (t[h0] + 1) & 255; ops++; break;   // +
        case 45: t[h0] = (t[h0] + 255) & 255; ops++; break; // -
        case 46: t[h1] = t[h0]; ops++; break;   // .  copy head0 -> head1
        case 44: t[h0] = t[h1]; ops++; break;   // ,  copy head1 -> head0
        case 91: // [
          ops++;
          if (t[h0] === 0) { let d = 1; pc++; for (; pc < T2 && d > 0; pc++) { if (t[pc] === 93) d--; if (t[pc] === 91) d++; } pc--; if (d !== 0) pc = T2; }
          break;
        case 93: // ]
          ops++;
          if (t[h0] !== 0) { let d = 1; pc--; for (; pc >= 0 && d > 0; pc--) { if (t[pc] === 93) d++; if (t[pc] === 91) d--; } pc++; if (d !== 0) pc = -1; }
          break;
      }
      if (pc < 0) break;
      pc++;
      if (pc >= T2) break;
    }
    return ops;
  }
  const OPS = [60, 62, 123, 125, 43, 45, 46, 44, 91, 93];
  // q = probability a starting byte is one of the ten instructions (uniform random bytes give q = 10/256)
  function Soup(n, seed, q) {
    this.n = n; this.seed = seed; this.r = rng(seed); this.q = q || 0;
    this.data = new Uint8Array(n * L);
    for (let i = 0; i < this.data.length; i++) this.data[i] = (q && this.r() < q) ? OPS[(this.r() * 10) | 0] : (this.r() * 256) | 0;
    this.perm = new Uint32Array(n); for (let i = 0; i < n; i++) this.perm[i] = i;
    this.buf = new Uint8Array(T2);
    this.epoch = 0; this.interactions = 0; this.ops = 0;
    // geometric gap to next mutated byte, counted across all interaction bytes
    this.gap = this.nextGap();
  }
  Soup.prototype.nextGap = function () { return Math.floor(Math.log(1 - this.r()) / Math.log(1 - MUT)); };
  Soup.prototype.step = function () { // one epoch: shuffle, pair, mutate, run, split
    const p = this.perm, r = this.r, n = this.n, d = this.data, b = this.buf;
    for (let i = n - 1; i > 0; i--) { const j = (r() * (i + 1)) | 0; const x = p[i]; p[i] = p[j]; p[j] = x; }
    for (let k = 0; k < n; k += 2) {
      const a = p[k] * L, c = p[k + 1] * L;
      b.set(d.subarray(a, a + L), 0); b.set(d.subarray(c, c + L), L);
      let g = this.gap;
      while (g < T2) { b[g] = (r() * 256) | 0; g += 1 + this.nextGap(); }
      this.gap = g - T2;
      this.ops += evaluate(b);
      d.set(b.subarray(0, L), a); d.set(b.subarray(L), c);
      this.interactions++;
    }
    this.epoch++;
  };
  // cubff CheckSelfRep: 13 noise partners, 1 + 4 generations; score = min over halves of positions agreed by >3 runs
  function selfrep(prog, seed) {
    const r = rng(seed ^ 0x9E3779B9), IT = 13, tapes = [];
    for (let i = 0; i < IT; i++) {
      const noise = new Uint8Array(L); for (let j = 0; j < L; j++) noise[j] = (r() * 256) | 0;
      const t = new Uint8Array(T2); t.set(prog, 0); t.set(noise, L); evaluate(t);
      for (let g = 0; g < 4; g++) { t.copyWithin(0, L, T2); t.set(noise, L); evaluate(t); }
      tapes.push(t);
    }
    const res = [0, 0];
    for (let i = 0; i < T2; i++) {
      for (let a = 0; a < IT; a++) {
        if (i < L && tapes[a][i] !== prog[i]) continue;
        let count = 1; for (let b = a + 1; b < IT; b++) if (tapes[a][i] === tapes[b][i]) count++;
        if (count > 3) { res[i < L ? 0 : 1]++; break; }
      }
    }
    return Math.min(res[0], res[1]);
  }
  function h0(data) { const c = new Float64Array(256); for (let i = 0; i < data.length; i++) c[data[i]]++; let h = 0; for (let i = 0; i < 256; i++) if (c[i]) { const f = c[i] / data.length; h -= f * Math.log2(f); } return h; }
  function commonest(data, n) { // returns {idx, count, distinct}
    const m = new Map(); let best = 0, bi = 0;
    for (let i = 0; i < n; i++) { let k = ''; for (let j = 0; j < L; j += 4) k += String.fromCharCode(data[i * L + j] | (data[i * L + j + 1] << 8), data[i * L + j + 2] | (data[i * L + j + 3] << 8)); const v = (m.get(k) || 0) + 1; m.set(k, v); if (v > best) { best = v; bi = i; } }
    return { idx: bi, count: best, distinct: m.size };
  }
  const api = { L, T2, rng, evaluate, Soup, selfrep, h0, commonest };
  if (typeof module !== 'undefined') module.exports = api; else root.BFF = api;
})(typeof self !== 'undefined' ? self : this);
