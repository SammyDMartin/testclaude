# Stage 1 pre-registration: emergence and takeover

Written and committed before any counted run. Pilot seeds 1001 to 1008 were started before this file to time
the runs and to obtain a replicator for the project page; they are excluded from every count below.

## Question

Does a CPU build of cubff reproduce takeover by self-replicators at the rate published in Agüera y Arcas et al.
(2024), with both fingerprints, and does disabling the two copy instructions prevent it?

## Setup

- Code: cubff `f212e849027c98fcf4b242eccfb5fed435223e23` plus `cubff-patch/` (logging and early stop only;
  the simulation is unchanged) and `bff_nocopy.cu` (sham A).
- Language: `bff_noheads` (instruction pointer and both heads start at 0, as in the paper).
- Soup: 131,072 programs of 64 bytes, uniform random start, cubff's default mutation rate
  (each byte of each joined pair replaced with probability 2^-12 per interaction; the paper's 0.024%).
- Budget: 16,384 epochs per seed. Log every 128 epochs. Checkpoint every 1,024 epochs.
- Main seeds: 1 to 10, `bff_noheads`. Sham A seeds: 1 to 5, `bff_nocopy`. Run in that order, one at a time.
- Command (main; sham identical with `--lang bff_nocopy`):

```
bin/main --lang bff_noheads --seed S --max_epochs 16384 --print_interval 128 --save_interval 1024 \
  --checkpoint_dir runs/stage1/main_S/ckpt --log runs/stage1/main_S/log.csv \
  --stats_log runs/stage1/main_S/stats.csv --selfrep_sample 4096 --stop_after_takeover 512 --disable_output
```

## Definitions

- Replication check: cubff's `CheckSelfRep` (13 random partners, 5 generations each), score 0 to 64.
  A program scoring 48 or more counts as a replicator.
- At each log: high-order entropy of the whole soup (cubff's: order-0 entropy minus brotli-quality-2 bits per
  byte); number of distinct programs; share of the commonest program; the check on 4,096 sampled programs
  and on the commonest program.
- Takeover (the counted event, revised before any counted run, see below): high-order entropy at or above 1
  at three consecutive logs, the first of them at or before epoch 16,384. This is the paper's transition
  ("complexity reaches at least 1"), held for 256 epochs so a single noisy log does not count. A run is not cut
  off mid-streak, and continues 512 epochs after confirmation.
- Replicator present: a sampled program, or the commonest program, scores 48 or more at some log. Reported per
  run as a second row; it does not gate the count.
- Fingerprint 1: the first log with high-order entropy at or above 1 (the takeover time).
  Fingerprint 2: the first log with distinct programs below 65,536 (half the soup). Descriptive only: it is our
  stand-in for the paper's tracer tokens and is untested.

## Predictions and criteria

From the paper: 40% of runs transition within 16,000 epochs and 3 in 1,000 within 128 epochs. Both fit a
constant hazard of about 1 per 31,300 epochs, so P(takeover by 16,384 epochs) is about 0.41.

| Measure | Prediction | Pass | Fail |
| --- | --- | --- | --- |
| Main seeds with a takeover | about 4 of 10 | 2 or more | 0 or 1 |
| Takeovers with a program scoring 48 or more | most of them | reported | reported |
| Distinct programs fall below half the soup within 512 epochs of fingerprint 1 | yes, in each takeover | reported | reported |
| Sham A takeovers | 0 of 5 | reported either way | a nonzero count is written up as a finding |
| Chance calibration: 10^7 uniform random programs through the check (`tools/calib.cc`, seed 1) | about 0.3 hits | 0 to 3 hits | more than 3 hits |

## Ledger rows to compute

- T_rep (a program scoring 48 or more): chance cost cited at log2(2.9e7) = 24.8 bits (Knierim et al. 2026),
  with the calibration result as a check.
- T_HOE (soup high-order entropy above 1): chance cost at least n = 8,388,608 bits by counting (brotli is
  uniquely decodable). P_dyn = k/10 with a Wilson 95% interval. I+ = n - log2(1/P_dyn).
- Designer bits: rule-set rarity pending Stage 2; configurations tried = 1 unless this file is amended.

## Revision before any counted run (11:45, 8 November)

An independent review of this file and the code found that the original counted event (entropy sustained
plus a sampled program scoring 48) is a strict subset of the paper's transition, so the count could only come
out lower than the 0.41 it is compared with; that the 16,384-epoch cut-off could end a run before its
confirmation or follow-up; and that fingerprint 2 is an untested proxy. The counted event is now the paper's
own (above), the 48-point check and fingerprint 2 are reported but do not gate, and the cut-off waits for an
unfinished streak or follow-up. No counted run had started. The replay builder's frame selection was also
fixed (it selected no frames when the takeover began after epoch 1,536).

## Amendments

Any change after the first counted run is recorded here with its time and reason, and adds one to the
configurations-tried count.
