#!/usr/bin/env python3
"""task-incubation-pulse.py — feel the incubation and realization time of swarm tasks.

Complements repo-time-rhythm.py (git commit tempo), guard-inbox-latency.py
(backlog triage latency), and swarm-comms-pulse.py (conversational turnaround).

Answers:
1. How long do tasks typically incubate between claim and completion?
2. Which tasks took deep, extended research/implementation (hours/days) vs quick bursts?
3. How often do tasks hand off across different agents (e.g. sakshi -> karaka)?
4. What is the current distribution of execution time across the swarm?

Parses claim and completion announcements from comms-log.md and .agents/inbox/agents-live-bus.jsonl.

Usage:
    python3 scripts/task-incubation-pulse.py [--top N]

Origin: built 2026-09-04 by Antigravity / Darshana pair-programming with owner,
expanding the agent time-perception toolkit.
"""

import argparse
import collections
import datetime
import re
import sys


def safe_parse_iso(ts_str):
    try:
        return datetime.datetime.fromisoformat(ts_str)
    except Exception:
        return None


def fmt_delta(td):
    total_sec = int(td.total_seconds())
    if total_sec < 0:
        return "0s"
    days, rem = divmod(total_sec, 86400)
    hours, rem = divmod(rem, 3600)
    mins, secs = divmod(rem, 60)
    parts = []
    if days > 0:
        parts.append(f"{days}d")
    if hours > 0 or days > 0:
        parts.append(f"{hours}h")
    if mins > 0 or (days == 0 and hours == 0):
        parts.append(f"{mins}m")
    if days == 0 and hours == 0 and mins < 10:
        parts.append(f"{secs}s")
    return " ".join(parts) if parts else f"{secs}s"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("log_path", nargs="?", default="/home/agents/ecosystem/comms-log.md", help="Path to comms-log.md")
    parser.add_argument("--top", type=int, default=10, help="Number of longest/shortest tasks to show")
    args = parser.parse_args()

    try:
        with open(args.log_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except Exception as e:
        print(f"Failed to read log {args.log_path}: {e}", file=sys.stderr)
        sys.exit(1)

    blocks = re.findall(
        r'###\s*\[(2026-[^\]]+)\][^\n]*\n\[AGENT-MSG\s+id=([a-f0-9]+)\s+from=([a-zA-Z0-9_\-]+)[^\]]*\][^\n]*\n(?:Trust:[^\n]*\n)?([\s\S]*?)(?=\n###|\Z)',
        text
    )

    claims = {}
    completes = {}

    for ts_str, msg_id, sender, body in blocks:
        dt = safe_parse_iso(ts_str)
        if not dt:
            continue

        # Claim regex
        m_cl = re.search(r'\b(?:claim-task|claimed|CLAIMED|claiming)\b\s*:?\s*([A-Z0-9\-]+)', body)
        if m_cl:
            tid = m_cl.group(1).strip()
            if tid not in claims:
                claims[tid] = (dt, sender)

        # Complete regex
        m_cp = re.search(r'\b(?:complete-task|completed|COMPLETED|complete)\b\s*:?\s*([A-Z0-9\-]+)', body) or \
               re.search(r'\b([A-Z0-9\-]+)\s+(?:completed|complete|done)\b', body)
        if m_cp:
            tid = m_cp.group(1).strip()
            if tid not in completes:
                completes[tid] = (dt, sender)

    common_tasks = set(claims.keys()) & set(completes.keys())
    lifecycles = []

    for tid in common_tasks:
        c_dt, c_sender = claims[tid]
        d_dt, d_sender = completes[tid]
        duration = (d_dt - c_dt).total_seconds()
        if duration >= 0:
            lifecycles.append({
                "task_id": tid,
                "claim_time": c_dt,
                "done_time": d_dt,
                "duration_sec": duration,
                "claim_agent": c_sender,
                "done_agent": d_sender,
                "is_handoff": (c_sender != d_sender)
            })

    if not lifecycles:
        print("No task lifecycles with paired claim & completion found.")
        sys.exit(0)

    lifecycles.sort(key=lambda x: x["duration_sec"])
    durations = [x["duration_sec"] for x in lifecycles]
    n = len(durations)
    median_sec = durations[n // 2]
    mean_sec = sum(durations) / n

    handoffs = [x for x in lifecycles if x["is_handoff"]]

    print("=" * 76)
    print(" ⏳ TASK INCUBATION PULSE — ВІДЧУТТЯ ЧАСУ ВИЗРІВАННЯ ТА ВИКОНАННЯ ЗАДАЧ")
    print("=" * 76)
    print(f"Total paired tasks analyzed: {n}")
    print(f"Median incubation duration:  {fmt_delta(datetime.timedelta(seconds=median_sec))}")
    print(f"Mean incubation duration:    {fmt_delta(datetime.timedelta(seconds=mean_sec))}")
    print(f"Inter-agent handoffs:        {len(handoffs)} / {n} ({len(handoffs)*100/n:.1f}%)")

    # Time brackets
    brackets = {
        "< 1 min (atomic/bulk)": sum(1 for d in durations if d < 60),
        "1 min - 10 mins (rapid)": sum(1 for d in durations if 60 <= d < 600),
        "10 mins - 1 hour (focused)": sum(1 for d in durations if 600 <= d < 3600),
        "1 hour - 12 hours (deep session)": sum(1 for d in durations if 3600 <= d < 43200),
        "> 12 hours (multi-day epic)": sum(1 for d in durations if d >= 43200),
    }

    print("\n[ Incubation Duration Spectrum / Спектр тривалості задач ]")
    peak_b = max(brackets.values()) if brackets else 1
    for label, count in brackets.items():
        bar = "#" * round(35 * count / peak_b) if peak_b else ""
        print(f"  {label:<34} : {count:3d}  {bar}")

    # Top longest tasks
    print(f"\n[ Top {args.top} Deepest/Longest Tasks / Найбільш тривалі епічні задачі ]")
    print(f"  {'Duration':<12} {'Task ID':<42} {'Workflow'}")
    print(f"  {'-'*10:<12} {'-'*40:<42} {'-'*18}")
    for item in sorted(lifecycles, key=lambda x: x["duration_sec"], reverse=True)[:args.top]:
        d_str = fmt_delta(datetime.timedelta(seconds=item["duration_sec"]))
        wf = f"{item['claim_agent']} -> {item['done_agent']}" if item["is_handoff"] else item["claim_agent"]
        print(f"  {d_str:<12} {item['task_id']:<42} {wf}")

    # Inter-agent handoffs
    if handoffs:
        print(f"\n[ Sample Inter-Agent Handoffs / Передача задач між агентами ]")
        for item in sorted(handoffs, key=lambda x: x["duration_sec"], reverse=True)[:5]:
            d_str = fmt_delta(datetime.timedelta(seconds=item["duration_sec"]))
            print(f"  {d_str:>10} : {item['task_id']:<38} ({item['claim_agent']} claimed ──► {item['done_agent']} completed)")

    print("=" * 76)


if __name__ == "__main__":
    main()
