# Tasks: Experiment

## 1. Writing

- [x] 1.1 撰寫 Experiment（Q–V）段落並加上 `% [A2Z:<code>]` 標記
- [x] 1.2 新增 experiments/run_real_eval.py：fresh/seq × strict/with-history 四種條件，外加 4 次重複計算 pass^4
- [x] 1.3 量測 v1.0（原版）：fresh 40.0%、seq 32.0%
- [x] 1.4 量測 v1.1（修兩行：docgen 格式碼、報廢閘門只允許 advice==DISPOSE）：fresh 60.0%、seq 52.0%
- [x] 1.5 Table II 結果、Table III 失敗原因
- [ ] 1.6 Baselines B1–B3 尚未實作 → \TBD
- [x] 1.7 執行 `python iceib-paper/check_a2z.py`，確認無 STRUCTURE 錯誤
- [x] 1.8 複製 main.tex 為 main.txt，確認 SHA-256 一致
- [x] 1.9 確認無捏造數字（所有數字可追溯到 DIC-3 或 experiments/*.json）
