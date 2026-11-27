# Design: Abstract

## Context

本章節依 2020 A-Z SOP 的 A–F 撰寫；事實來源為 DIC-3 原始碼與 experiments/ 量測結果。

## Goals / Non-Goals

**Goals**
- 撰寫 A–F 六句式摘要（≤ 250 words）
- F 段只引用 experiments/results_real_eval*.json 的數字（40.0%、60.0%、100% 管理成功率）
- 同時寫出負面發現（採購 20.0%、報廢路徑僅因 crash 才被擋）

**Non-Goals**
- 不引用未經執行產生的數字
- 不描述尚未實作的功能為已完成

## Decisions

- [A2Z:A] Abstract follows A–F：摘要 SHALL 依序包含 A、B、C、D、E、F 六個 A2Z 標記，且總字數 SHALL 不超過 250 words。
- [A2Z:F] Findings are measured：F 段中的每個數字 MUST 出現在 experiments/results_real_eval*.json 中。

## Risks / Trade-offs

- 據實回報較低的成功率會降低論文「賣相」，但可避免審稿或口試時被重現實驗推翻。
