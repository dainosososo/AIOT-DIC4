# Spec Delta: introduction-g-to-l

## ADDED Requirements

### Requirement: Introduction covers G–L
[A2Z:G] Introduction SHALL 包含 G、H、I、J、K、L 標記各至少一段。

#### Scenario: check_a2z.py 檢查
- **WHEN** check_a2z.py 檢查
- **THEN** G–L 皆被找到且依序出現

### Requirement: Claims are cited
[A2Z:H] H 段中每個外部事實 SHALL 附帶 \cite。

#### Scenario: H 段提到 Control Yuan 調查或 τ-bench
- **WHEN** H 段提到 Control Yuan 調查或 τ-bench
- **THEN** 該句後面有對應 \cite 與 \bibitem
