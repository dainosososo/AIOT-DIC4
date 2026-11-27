# Design: Experiment

## Context

本章節依 2020 A-Z SOP 的 Q–V 撰寫；事實來源為 DIC-3 原始碼與 experiments/ 量測結果。

## Goals / Non-Goals

**Goals**
- 新增 experiments/run_real_eval.py：fresh/seq × strict/with-history 四種條件，外加 4 次重複計算 pass^4
- 量測 v1.0（原版）：fresh 40.0%、seq 32.0%
- 量測 v1.1（修兩行：docgen 格式碼、報廢閘門只允許 advice==DISPOSE）：fresh 60.0%、seq 52.0%
- Table II 結果、Table III 失敗原因
- Baselines B1–B3 尚未實作 → \TBD

**Non-Goals**
- 不引用未經執行產生的數字
- 不描述尚未實作的功能為已完成

## Decisions

- [A2Z:U] Numbers come from execution：Table II 的每個數值 MUST 存在於 experiments/results_real_eval*.json。
- [A2Z:R] Unmeasured baselines are TBD：未實作的 baseline SHALL 標示為 \TBD，且 MUST NOT 引用 run_eval.py 的寫死數字。

## Risks / Trade-offs

- 據實回報較低的成功率會降低論文「賣相」，但可避免審稿或口試時被重現實驗推翻。
