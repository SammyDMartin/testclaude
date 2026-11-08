# Crane ladder: compute folder

Work for Sammy Martin's crane-ladder project (from random programs to replicators and beyond, with no fitness
function, a sham beside every rung, and an information ledger in Dembski's units). This branch is a scratch
branch on an old test repository; nothing here touches the website on `master`.

- `prereg/` pre-registration files, committed before the runs they describe.
- `cubff-patch/` changes to [cubff](https://github.com/paradigms-of-intelligence/cubff) at commit
  `f212e849027c98fcf4b242eccfb5fed435223e23`: logging, early stop, and the copy-disabled sham language.
- `tools/` the chance-calibration harness, the replay builder, and the JavaScript port used by the page.
- `runs/` per-seed logs (`log.csv`, `stats.csv`) and the ledger. Checkpoints are not committed.

To reproduce: clone cubff at the commit above, apply `cubff-patch/main.cc.diff`, copy `bff_nocopy.cu` in,
`make CUDA=0`, then run the commands in the relevant pre-registration file.

## Stage 1 result (partial, 8 November 2026)

Curtailed by amendment 1 to main seeds 1 to 4, sham seed 1 and the calibration. Takeovers: 1 of 4 main seeds
(seed 2; Wilson 95% interval 5% to 70%, against the paper's 41%); no verdict on the 2-of-10 criterion. Sham seed 1
(copying off): no takeover, entropy never above zero. Calibration: 0 of 10^7 random programs scored 48 or more.
Results in `runs/stage1/`, analysis in `runs/stage1/analysis/`, the page and its data builder in `page/` and `tools/`.
