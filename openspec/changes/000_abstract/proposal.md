# Proposal: Abstract

## Why

摘要是審稿人第一個看到的段落，必須在 250 字內交代動機、挑戰、解法、方法、實驗與發現，且發現必須是實測數字。

A2Z 範圍：**A–F**；對應 `iceib-paper/main.tex` 的 Abstract 部分。

## What Changes

- 撰寫 A–F 六句式摘要（≤ 250 words）
- F 段只引用 experiments/results_real_eval*.json 的數字（40.0%、60.0%、100% 管理成功率）
- 同時寫出負面發現（採購 20.0%、報廢路徑僅因 crash 才被擋）

## Capabilities

### New Capabilities
- `abstract-a-to-f`: Abstract 章節（A2Z A–F）的寫作規格。

### Modified Capabilities
<!-- none -->

## Impact

- `iceib-paper/main.tex`、`iceib-paper/main.txt`
- 狀態：完成
