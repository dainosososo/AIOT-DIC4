# Design: Proposed Design

## Context

本章節依 2020 A-Z SOP 的 PA–PM 撰寫；事實來源為 DIC-3 原始碼與 experiments/ 量測結果。

## Goals / Non-Goals

**Goals**
- PA–PE：目標、基礎、解法原因、典範轉移、元件
- PF：V_book、V_mkt、TCO、拆單式 (1)–(3)，參數與 DIC-3 原始碼一致
- PG：TikZ 架構圖（Fig. 1）
- PH–PJ：運作方式、Algorithm 1、RTX 4090 範例
- PK–PM：關鍵貢獻、評估計畫、安全性性質（並註明其前提：規則需完整）

**Non-Goals**
- 不引用未經執行產生的數字
- 不描述尚未實作的功能為已完成

## Decisions

- [A2Z:PF] Design matches code：公式中的常數 SHALL 與 DIC-3 tools/ 原始碼一致（δ=0.15、α=5000、τ_s=150000、30 天）。
- [A2Z:PM] Proof states its assumption：PM 段 SHALL 明確說明合規健全性僅在 guardrail 規則完整時成立。

## Risks / Trade-offs

- 據實回報較低的成功率會降低論文「賣相」，但可避免審稿或口試時被重現實驗推翻。
