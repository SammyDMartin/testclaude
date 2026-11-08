#!/bin/bash
# Copy Stage 1 results, tools and page sources into the testclaude branch folder.
set -e
L=/home/claude/ladder; T=/home/claude/testclaude/compute/craneladder
mkdir -p $T/runs/stage1/analysis $T/tools $T/page
for d in main_1 main_2 main_3 main_4 sham_1; do mkdir -p $T/runs/stage1/$d; cp $L/runs/stage1/$d/*.csv $T/runs/stage1/$d/; done
cp $L/runs/stage1/{summary.txt,calib.txt,run_stage1.sh,run_rest.sh,run_resume.sh} $T/runs/stage1/
cp $L/runs/stage1/analysis/* $T/runs/stage1/analysis/
cp $L/tools/{analyse_stage1.py,make_evo.py,make_page_data.py,build_page3.py,merge_sham.py,make_replay.py,stage_commit.sh} $T/tools/
cp $L/page/{src3.html,engine.js,page_data.json,evo_main2.json,so-simple-a-beginning.html} $T/page/
du -sh $T
