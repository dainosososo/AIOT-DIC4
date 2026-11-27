# Spec Delta: proposed-design-pa-to-pm

## ADDED Requirements

### Requirement: Design matches code
[A2Z:PF] 公式中的常數 SHALL 與 DIC-3 tools/ 原始碼一致（δ=0.15、α=5000、τ_s=150000、30 天）。

#### Scenario: 比對 tools/valuation.py、web_search.py、guardrail.py
- **WHEN** 比對 tools/valuation.py、web_search.py、guardrail.py
- **THEN** 所有常數一致

### Requirement: Proof states its assumption
[A2Z:PM] PM 段 SHALL 明確說明合規健全性僅在 guardrail 規則完整時成立。

#### Scenario: 閱讀 PM 段
- **WHEN** 閱讀 PM 段
- **THEN** 有指出 Section IV 的反例
