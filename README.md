# AIOT-DIC4：Overleaf draft for conference using MCP and OpenSpec

把 DIC-3 期末專題 **LabSteward**（實驗室財產管理與合規採購 AI Agent，[dainosososo/DIC-3](https://github.com/dainosososo/DIC-3)）
寫成 **IEEE 會議論文初稿**（目標 ICEIB 2027，IEEEtran conference，英文 4–8 頁），
並以 **OpenSpec** 規格驅動流程管理每一個章節。

> 論文題目：*Utilize Before Acquire: A Guardrailed Tool-Calling Agent for University Laboratory
> Asset Lifecycle Management and Public-Procurement Compliance*

## 作業要求對照

| 要求 | 交付 | 狀態 |
| :--- | :--- | :---: |
| 1. Overleaf draft for IEEE conference | [`iceib-paper/main.tex`](iceib-paper/main.tex)（單檔、無外部圖檔，TikZ 繪圖），[`overleaf_upload.zip`](overleaf_upload.zip) 可直接上傳 Overleaf | ✅ |
| 2. OpenSpec on GitHub | [`openspec/`](openspec/)：`config.yaml` + 7 個 change（000–006），`openspec validate --all --strict` 7/7 通過 | ✅ |
| using MCP | 以 Claude Code（MCP host）透過 MCP 工具讀取 DIC-3 repo、執行實驗、產生 OpenSpec 與 LaTeX，並以 GitHub 工具推送；流程見下方 | ✅ |

## 如何在 Overleaf 開啟

1. Overleaf → **New Project → Upload Project** → 選 `overleaf_upload.zip`
   （或 **New Project → Import from GitHub** 選本 repo，主檔設定為 `iceib-paper/main.tex`）
2. Menu → Compiler 選 **pdfLaTeX**，按 Recompile。

## 章節 ↔ OpenSpec change ↔ 2020 A-Z SOP

| Change | A2Z | 章節 | 狀態 |
| :--- | :---: | :--- | :--- |
| `000_abstract` | A–F | Abstract（197 words） | 完成 |
| `001_introduction` | G–L | I. Introduction | 完成 |
| `002_related_work` | M–O | II. Related Work + 4x5 SWOT（Table I） | 完成 |
| `003_proposed_design` | PA–PM | III. Proposed Design（式 1–3、Fig. 1、Algorithm 1） | 完成，待組員審閱 |
| `004_experiments` | Q–V | IV. Experiment（Table II、III） | 部分完成：baseline B1–B3 待實作 |
| `005_conclusion` | W–Z | V. Conclusion | 完成 |
| `006_references` | — | 12 筆參考文獻、投稿前檢查 | 系所/學校/email 已填，組員姓名待填 |

```bash
npm install -g @fission-ai/openspec@latest
openspec list
openspec validate --all --strict     # 7 passed, 0 failed
python iceib-paper/check_a2z.py      # 38/38 A2Z 標記、5 個章節、結果表數字皆可追溯
```

`check_a2z.py` 目前回傳 **2**（結構正確，但仍有投稿阻擋項：組員姓名佔位字與 2 處 `\TBD`）。

## ⚠️ 重要：實驗數字改為「實際執行」的結果

DIC-3 的 `eval/run_eval.py` **沒有執行 agent**，只印出寫死的數字（例如 LabSteward 96.0%）。
本作業新增 [`experiments/run_real_eval.py`](experiments/run_real_eval.py)，真的把 50 題逐題丟給
`labsteward_agent_loop()`，比對回傳狀態與 `expected_status`：

| | v1.0（DIC-3 原版）fresh | seq | v1.1（修 2 行）fresh | seq |
| :--- | :---: | :---: | :---: | :---: |
| 成功率 | 40.0% | 32.0% | 60.0% | 52.0% |
| 管理 / 採購 | 60.0% / 20.0% | 44.0% / 20.0% | 100.0% / 20.0% | 84.0% / 20.0% |
| 閒置庫存命中（重複採購率） | 0.0% | 0.0% | 0.0% | 0.0% |
| Guardrail 漏放 | 0.0% | 0.0% | 0.0% | 0.0% |

量測過程中找到的問題（論文 Table III）：

1. `tools/docgen.py` 對 float 使用 `:,d` 格式 → 所有報廢路徑 `ValueError`（10 題）。
2. 報廢閘門只擋「已逾年限且堪用」；**未逾年限的閒置設備（LAB-2024-GPU-02）會被放行去產生報廢草稿**，只是剛好被 bug 1 crash 擋下 —— 潛在的合規漏洞。
3. 廠商目錄只涵蓋 RTX 4090 與示波器，且整句 query 被當成規格；guardrail 在搜尋之後才執行，所以拆單偵測永遠走不到（20 題）。

修正 1、2 的 patch：[`experiments/v1_1.patch`](experiments/v1_1.patch)。原始逐題結果：`experiments/results_real_eval*.json`。

重現：

```bash
git clone https://github.com/dainosososo/DIC-3.git
python experiments/run_real_eval.py DIC-3 experiments/results_real_eval.json
```

## MCP 寫作流程

```
Claude Code (MCP host)
 ├─ GitHub 工具 (gh / GitHub MCP) ── 讀取 dainosososo/DIC-3、參考 jimtaerini/AIOT-DIC4、建立並推送本 repo
 ├─ Shell / filesystem 工具 ─────── 執行 run_real_eval.py、openspec validate、check_a2z.py
 └─ 產出 ──────────────────────── openspec/changes/00N_* → iceib-paper/main.tex → Overleaf（GitHub 匯入 / zip 上傳）
```

每一章先寫 OpenSpec change（proposal → specs → design → tasks），再寫對應的 LaTeX 段落，
最後以 `check_a2z.py` 與 `openspec validate` 驗證。

## 投稿前待辦

- [x] 系所、學校、城市、email：Dept. of CSE, National Chung Hsing University, Taichung
- [ ] 填入 5 位組員英文姓名（`main.tex` 的 `\IEEEauthorblockN{}`）
- [ ] 實作並量測 baseline B1–B3（或從論文中移除該列）
- [ ] 核對參考文獻細節（特別是 arXiv:2601.00121 與 Řezníček & Kropík 一文的出處）
- [ ] 組員審閱 Section III 的安全性性質（PM）
- [ ] `python iceib-paper/check_a2z.py` 回傳 0

## Repository 結構

```
AIOT-DIC4/
├── README.md
├── overleaf_upload.zip          # 直接上傳 Overleaf
├── iceib-paper/
│   ├── main.tex                 # IEEE 會議論文初稿
│   ├── main.txt                 # main.tex 的 byte-identical 副本
│   └── check_a2z.py             # A2Z 結構 / 引用 / 數字可追溯檢查
├── experiments/
│   ├── run_real_eval.py         # 實際執行 50 題基準
│   ├── results_real_eval.json   # v1.0 逐題結果
│   ├── results_real_eval_v1_1.json
│   └── v1_1.patch
└── openspec/
    ├── config.yaml
    └── changes/000_abstract … 006_references/
        ├── .openspec.yaml  proposal.md  design.md  tasks.md
        └── specs/<capability>/spec.md
```
