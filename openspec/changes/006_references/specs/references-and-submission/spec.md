# Spec Delta: references-and-submission

## ADDED Requirements

### Requirement: Every bibitem is cited
[A2Z:Z] 每個 \bibitem SHALL 至少被 \cite 一次，反之亦然。

#### Scenario: check_a2z.py
- **WHEN** check_a2z.py
- **THEN** references 數量相等且無錯誤

### Requirement: Ready to submit
[A2Z:Z] 投稿前 check_a2z.py MUST 回傳 exit code 0（無 \TBD、無作者佔位字）。

#### Scenario: 執行 check_a2z.py
- **WHEN** 執行 check_a2z.py
- **THEN** 印出 OK: ready to submit
