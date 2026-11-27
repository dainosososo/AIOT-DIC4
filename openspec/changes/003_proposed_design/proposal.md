# Proposal: Proposed Design

## Why

設計章節須描述實際已實作的系統（規則式 planner），並清楚區分規劃中但尚未實作的部分（LLM planner、LangGraph、Playwright）。

A2Z 範圍：**PA–PM**；對應 `iceib-paper/main.tex` 的 Proposed Design 部分。

## What Changes

- PA–PE：目標、基礎、解法原因、典範轉移、元件
- PF：V_book、V_mkt、TCO、拆單式 (1)–(3)，參數與 DIC-3 原始碼一致
- PG：TikZ 架構圖（Fig. 1）
- PH–PJ：運作方式、Algorithm 1、RTX 4090 範例
- PK–PM：關鍵貢獻、評估計畫、安全性性質（並註明其前提：規則需完整）

## Capabilities

### New Capabilities
- `proposed-design-pa-to-pm`: Proposed Design 章節（A2Z PA–PM）的寫作規格。

### Modified Capabilities
<!-- none -->

## Impact

- `iceib-paper/main.tex`、`iceib-paper/main.txt`
- 狀態：完成，待組員審閱
