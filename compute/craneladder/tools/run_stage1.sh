#!/bin/bash
# Stage 1 counted runs, exactly as pre-registered (commit 6d7148d): main seeds 1-10, then sham seeds 1-5,
# then the chance calibration. One run at a time on both cores.
cd /home/claude/ladder/ext/cubff
R=/home/claude/ladder/runs/stage1
run() { # kind lang seed
  local d=$R/$1_$3; mkdir -p $d/ckpt
  local s=$(date +%s)
  bin/main --lang $2 --seed $3 --max_epochs 16384 --print_interval 128 --save_interval 1024 \
    --checkpoint_dir $d/ckpt --log $d/log.csv --stats_log $d/stats.csv --selfrep_sample 4096 \
    --stop_after_takeover 512 --disable_output
  local rc=$?
  echo "$(date +%H:%M) $1 seed $3 exit $rc in $(( $(date +%s) - s )) s; last: $(tail -1 $d/stats.csv | cut -d, -f1-10)" >> $R/summary.txt
}
for s in 1 2 3 4 5 6 7 8 9 10; do run main bff_noheads $s; done
for s in 1 2 3 4 5; do run sham bff_nocopy $s; done
s=$(date +%s); /home/claude/ladder/tools/calib bff_noheads 10000000 1 48 > $R/calib.txt
echo "$(date +%H:%M) calibration done in $(( $(date +%s) - s )) s: $(grep '^N ' $R/calib.txt)" >> $R/summary.txt
echo "$(date +%H:%M) STAGE1 COMPLETE" >> $R/summary.txt
