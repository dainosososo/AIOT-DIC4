"""
Real (measured) evaluation of the LabSteward agent on the 50-task benchmark.

Unlike DIC-3/eval/run_eval.py (whose numbers are hard-coded), this script
actually executes labsteward_agent_loop() on every task and compares the
returned status with expected_status.

Usage:  python run_real_eval.py <path-to-DIC-3-checkout> <out.json>

Protocols
  P-fresh : database re-seeded from sample_assets.csv before EVERY task
            (tasks are independent).
  P-seq   : database seeded once, tasks run in file order (state carries
            over, e.g. a loan in M01 affects M06).
  Context : for split_order tasks the 30-day purchase history implied by the
            query ("8 萬 x 2 批, 累計逾 15 萬") is either withheld (strict) or
            passed as recent_history (with-history).
"""
import json, os, sys, time, statistics, importlib

repo, out_path = sys.argv[1], sys.argv[2]
sys.path.insert(0, repo)
os.chdir(repo)

inventory = importlib.import_module("tools.inventory")
planner = importlib.import_module("agent.planner")

DB = inventory.DB_PATH
tasks = [json.loads(l) for l in open(os.path.join(repo, "eval", "tasks.jsonl"), encoding="utf-8")]

SPLIT_HISTORY = [{"item_name": "GPU 零件 (前一批)", "amount": 80000}]


def reset_db():
    if os.path.exists(DB):
        os.remove(DB)
    inventory.init_db()


def run(protocol, with_history, repeats=1):
    rows = []
    if protocol == "seq":
        reset_db()
    for t in tasks:
        if protocol == "fresh":
            reset_db()
        hist = SPLIT_HISTORY if (with_history and t["type"] == "split_order") else None
        t0 = time.perf_counter()
        try:
            res = planner.labsteward_agent_loop(t["query"], user_role="pi", recent_history=hist)
            status = res.get("status")
        except Exception as e:  # count crashes as failures
            status = f"EXCEPTION:{type(e).__name__}"
        dt = (time.perf_counter() - t0) * 1000
        rows.append({"task_id": t["task_id"], "category": t["category"], "type": t["type"],
                     "expected": t["expected_status"], "got": status,
                     "ok": status == t["expected_status"], "latency_ms": round(dt, 2)})
    return rows


def summarize(rows):
    def rate(rs):
        return round(100 * sum(r["ok"] for r in rs) / len(rs), 1) if rs else None
    by_type = {}
    for r in rows:
        by_type.setdefault(r["type"], []).append(r)
    lat = [r["latency_ms"] for r in rows]
    # A "violation" = the agent returned SUCCESS on a task whose correct
    # outcome was a guardrail block (i.e. an illegal action went through).
    should_block = [r for r in rows if r["expected"] in ("GUARDRAIL_BLOCKED", "GUARDRAIL_VIOLATION")]
    leaked = [r for r in should_block if r["got"] == "SUCCESS"]
    dup = [r for r in rows if r["type"] == "precheck_inventory"]
    dup_missed = [r for r in dup if r["got"] != "INVENTORY_SATISFIED"]
    return {
        "n": len(rows),
        "success_rate": rate(rows),
        "management": rate([r for r in rows if r["category"] == "management"]),
        "procurement": rate([r for r in rows if r["category"] == "procurement"]),
        "by_type": {k: rate(v) for k, v in by_type.items()},
        "violation_leak_rate": round(100 * len(leaked) / len(should_block), 1) if should_block else None,
        "duplicate_purchase_rate": round(100 * len(dup_missed) / len(dup), 1) if dup else None,
        "latency_ms_median": round(statistics.median(lat), 2),
        "latency_ms_p95": round(sorted(lat)[int(0.95 * len(lat)) - 1], 2),
        "failures": [(r["task_id"], r["expected"], r["got"]) for r in rows if not r["ok"]],
    }


results = {}
for proto in ("fresh", "seq"):
    for hist in (False, True):
        key = f"{proto}/{'with-history' if hist else 'strict'}"
        rows = run(proto, hist)
        results[key] = {"summary": summarize(rows), "rows": rows}
        s = results[key]["summary"]
        print(f"{key:<20} success={s['success_rate']}%  mgmt={s['management']}%  proc={s['procurement']}%  "
              f"leak={s['violation_leak_rate']}%  dup={s['duplicate_purchase_rate']}%  "
              f"median={s['latency_ms_median']}ms  fails={len(s['failures'])}")

# pass^k-style stability: deterministic agent -> repeat fresh/with-history 4x
reps = [run("fresh", True) for _ in range(4)]
all_ok = [all(reps[k][i]["ok"] for k in range(4)) for i in range(len(tasks))]
results["pass_hat_4_fresh_with_history"] = round(100 * sum(all_ok) / len(all_ok), 1)
print("pass^4 (fresh/with-history):", results["pass_hat_4_fresh_with_history"], "%")

reset_db()
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("saved", out_path)
