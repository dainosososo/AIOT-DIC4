# Design: Introduction

## Context

本章節依 2020 A-Z SOP 的 G–L 撰寫；事實來源為 DIC-3 原始碼與 experiments/ 量測結果。

## Goals / Non-Goals

**Goals**
- G 現況、H 三大挑戰（含 τ-bench pass^8 < 25%）
- I 四類既有解法由舊到新
- J 優缺點評判
- K 設計精神與 4 項貢獻
- L 文章結構

**Non-Goals**
- 不引用未經執行產生的數字
- 不描述尚未實作的功能為已完成

## Decisions

- [A2Z:G] Introduction covers G–L：Introduction SHALL 包含 G、H、I、J、K、L 標記各至少一段。
- [A2Z:H] Claims are cited：H 段中每個外部事實 SHALL 附帶 \cite。

## Risks / Trade-offs

- 據實回報較低的成功率會降低論文「賣相」，但可避免審稿或口試時被重現實驗推翻。
