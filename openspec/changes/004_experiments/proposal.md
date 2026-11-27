# Proposal: Experiment

## Why

原 DIC-3 的 eval/run_eval.py 沒有執行任何 agent，只印出寫死的數字（宣稱 96%）。本 change 改為實際執行 50 題並如實回報。

A2Z 範圍：**Q–V**；對應 `iceib-paper/main.tex` 的 Experiment 部分。

## What Changes

- 新增 experiments/run_real_eval.py：fresh/seq × strict/with-history 四種條件，外加 4 次重複計算 pass^4
- 量測 v1.0（原版）：fresh 40.0%、seq 32.0%
- 量測 v1.1（修兩行：docgen 格式碼、報廢閘門只允許 advice==DISPOSE）：fresh 60.0%、seq 52.0%
- Table II 結果、Table III 失敗原因
- Baselines B1–B3 尚未實作 → \TBD

## Capabilities

### New Capabilities
- `experiments-q-to-v`: Experiment 章節（A2Z Q–V）的寫作規格。

### Modified Capabilities
<!-- none -->

## Impact

- `iceib-paper/main.tex`、`iceib-paper/main.txt`
- 狀態：部分完成：B1–B3 baseline 待實作
