#!/bin/bash
# Curtailed Stage 1 (Sammy, 14:07): finish main seed 4, then sham seed 1, then the chance calibration.
cd /home/claude/ladder/ext/cubff
R=/home/claude/ladder/runs/stage1
while pgrep -f "bin/main --lang bff_noheads --seed 4 " >/dev/null; do sleep 15; done
echo "$(date +%H:%M) main seed 4 done; last: $(tail -1 $R/main_4/stats.csv | cut -d, -f1-10)" >> $R/summary.txt
d=$R/sham_1; mkdir -p $d/ckpt; s=$(date +%s)
bin/main --lang bff_nocopy --seed 1 --max_epochs 16384 --print_interval 128 --save_interval 1024 \
  --checkpoint_dir $d/ckpt --log $d/log.csv --stats_log $d/stats.csv --selfrep_sample 4096 \
  --stop_after_takeover 512 --disable_output
echo "$(date +%H:%M) sham seed 1 exit $? in $(( $(date +%s) - s )) s; last: $(tail -1 $d/stats.csv | cut -d, -f1-10)" >> $R/summary.txt
s=$(date +%s); /home/claude/ladder/tools/calib bff_noheads 10000000 1 48 > $R/calib.txt
echo "$(date +%H:%M) calibration done in $(( $(date +%s) - s )) s: $(grep '^N ' $R/calib.txt)" >> $R/summary.txt
echo "$(date +%H:%M) STAGE1 COMPLETE (curtailed)" >> $R/summary.txt
