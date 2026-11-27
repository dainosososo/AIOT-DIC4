# Design: References / 投稿前檢查

## Context

本章節依 2020 A-Z SOP 的 References 撰寫；事實來源為 DIC-3 原始碼與 experiments/ 量測結果。

## Goals / Non-Goals

**Goals**
- 12 筆 \bibitem，全部被引用
- 核對每筆文獻的作者、年份、出處（特別是 arXiv:2601.00121 與 Řezníček 一文）
- 填入作者英文姓名、系所、學校、email
- check_a2z.py 回傳 0

**Non-Goals**
- 不引用未經執行產生的數字
- 不描述尚未實作的功能為已完成

## Decisions

- [A2Z:Z] Every bibitem is cited：每個 \bibitem SHALL 至少被 \cite 一次，反之亦然。
- [A2Z:Z] Ready to submit：投稿前 check_a2z.py MUST 回傳 exit code 0（無 \TBD、無作者佔位字）。

## Risks / Trade-offs

- 據實回報較低的成功率會降低論文「賣相」，但可避免審稿或口試時被重現實驗推翻。
