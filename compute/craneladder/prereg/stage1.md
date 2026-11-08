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
- Takeover confirmed: high-order entropy at or above 1 at three consecutive logs, and at least one sampled
  program (or the commonest program) scoring 48 or more. The run continues 512 epochs after confirmation.
- Fingerprint 1: the first log with high-order entropy at or above 1.
  Fingerprint 2: the first log with distinct programs below 65,536 (half the soup).

## Predictions and criteria

From the paper: 40% of runs transition within 16,000 epochs and 3 in 1,000 within 128 epochs. Both fit a
constant hazard of about 1 per 31,300 epochs, so P(takeover by 16,384 epochs) is about 0.41.

| Measure | Prediction | Pass | Fail |
| --- | --- | --- | --- |
| Main seeds with confirmed takeover | about 4 of 10 | 2 or more | 0 or 1 |
| Fingerprints in each takeover | both present, within 512 epochs of each other | both, every takeover | either missing in any takeover |
| Sham A takeovers | 0 of 5 | reported either way | a nonzero count is written up as a finding |
| Chance calibration: 10^7 uniform random programs through the check (`tools/calib.cc`, seed 1) | about 0.3 hits | 0 to 3 hits | more than 3 hits |

## Ledger rows to compute

- T_rep (a program scoring 48 or more): chance cost cited at log2(2.9e7) = 24.8 bits (Knierim et al. 2026),
  with the calibration result as a check.
- T_HOE (soup high-order entropy above 1): chance cost at least n = 8,388,608 bits by counting (brotli is
  uniquely decodable). P_dyn = k/10 with a Wilson 95% interval. I+ = n - log2(1/P_dyn).
- Designer bits: rule-set rarity pending Stage 2; configurations tried = 1 unless this file is amended.

## Amendments

Any change after the first counted run is recorded here with its time and reason, and adds one to the
configurations-tried count.
