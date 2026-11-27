# Spec Delta: experiments-q-to-v

## ADDED Requirements

### Requirement: Numbers come from execution
[A2Z:U] Table II 的每個數值 MUST 存在於 experiments/results_real_eval*.json。

#### Scenario: check_a2z.py 檢查結果表
- **WHEN** check_a2z.py 檢查結果表
- **THEN** 沒有出現 'not found in experiments' 錯誤

### Requirement: Unmeasured baselines are TBD
[A2Z:R] 未實作的 baseline SHALL 標示為 \TBD，且 MUST NOT 引用 run_eval.py 的寫死數字。

#### Scenario: 搜尋 main.tex 中的 58.0、62.0、74.0、96.0
- **WHEN** 搜尋 main.tex 中的 58.0、62.0、74.0、96.0
- **THEN** 皆不存在
