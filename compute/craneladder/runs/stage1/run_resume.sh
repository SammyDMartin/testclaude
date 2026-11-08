#!/bin/bash
# The container restarted at about 15:21 and stopped sham seed 1 at epoch 4,993 (its last checkpoint is 4,096).
# cubff is deterministic per epoch, so the sham resumes from that checkpoint into separate log files;
# the overlap with the first part is compared and the two are merged. Then the chance calibration.
cd /home/claude/ladder/ext/cubff
R=/home/claude/ladder/runs/stage1; d=$R/sham_1
echo "$(date +%H:%M) container restarted; sham seed 1 had reached epoch 4993; resuming from checkpoint 4096" >> $R/summary.txt
s=$(date +%s)
bin/main --lang bff_nocopy --seed 1 --load $d/ckpt/0000004096.dat --max_epochs 16384 --print_interval 128 --save_interval 1024 \
  --checkpoint_dir $d/ckpt --log $d/log_b.csv --stats_log $d/stats_b.csv --selfrep_sample 4096 \
  --stop_after_takeover 512 --disable_output
echo "$(date +%H:%M) sham seed 1 exit $? in $(( $(date +%s) - s )) s; last: $(tail -1 $d/stats_b.csv | cut -d, -f1-10)" >> $R/summary.txt
s=$(date +%s); /home/claude/ladder/tools/calib bff_noheads 10000000 1 48 > $R/calib.txt
echo "$(date +%H:%M) calibration done in $(( $(date +%s) - s )) s: $(grep '^N ' $R/calib.txt)" >> $R/summary.txt
echo "$(date +%H:%M) STAGE1 COMPLETE (curtailed)" >> $R/summary.txt
