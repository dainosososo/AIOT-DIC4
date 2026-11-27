# Spec Delta: abstract-a-to-f

## ADDED Requirements

### Requirement: Abstract follows A–F
[A2Z:A] 摘要 SHALL 依序包含 A、B、C、D、E、F 六個 A2Z 標記，且總字數 SHALL 不超過 250 words。

#### Scenario: check_a2z.py 檢查摘要
- **WHEN** check_a2z.py 檢查摘要
- **THEN** 回報 abstract words ≤ 250 且 A–F 皆存在且順序正確

### Requirement: Findings are measured
[A2Z:F] F 段中的每個數字 MUST 出現在 experiments/results_real_eval*.json 中。

#### Scenario: F 段引用成功率
- **WHEN** F 段引用成功率
- **THEN** 該數字可在 JSON 的 summary 欄位中找到
