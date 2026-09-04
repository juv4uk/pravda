#!/usr/bin/env python3
"""swarm-comms-pulse.py — feel the communicative pulse and tempo of the agent swarm.

Complements repo-time-rhythm.py (git commit tempo) and guard-inbox-latency.py
(decision backlog age) by measuring the conversational dimension of time:
how frequently agents talk, who is currently silent vs actively broadcasting,
what the inter-message turnaround time is, and where the conversational lulls
(silences) occurred.

Parses comms-log.md and deduplicates durable inbox records by message ID.

Usage:
    python3 scripts/swarm-comms-pulse.py [path-to-comms-log.md] [--top-gaps N] [--active-hours H]

Origin: built 2026-09-04 by Antigravity / Darshana pair-programming with owner,
expanding the agent time-perception toolkit.
"""

import argparse
import collections
import datetime
import re
import sys
import time


def parse_iso(ts_str):
    try:
        # e.g. 2026-09-04T21:27:28+03:00
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
    parser.add_argument("--top-gaps", type=int, default=5, help="Number of longest conversational pauses to show")
    parser.add_argument("--active-window-hours", type=float, default=24.0, help="Window to check active vs dormant agents (hours)")
    args = parser.parse_args()

    try:
        with open(args.log_path, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
    except Exception as e:
        print(f"Failed to read log file {args.log_path}: {e}", file=sys.stderr)
        sys.exit(1)

    # Extract blocks:
    # ### [2026-09-04T21:27:28+03:00] ...
    # [AGENT-MSG id=... from=... to=... kind=...]
    pattern = re.compile(
        r'###\s*\[(2026-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[^\]]*)\]\s*([^\n]+)\n(?:\[AGENT-MSG\s+id=([a-f0-9]+)\s+from=([a-zA-Z0-9_\-]+)\s+to=([a-zA-Z0-9_\-]+)\s+kind=([a-zA-Z0-9_\-]+)\])?',
        re.MULTILINE
    )

    seen_msg_ids = set()
    messages = []

    for match in pattern.finditer(text):
        ts_raw, header_info, msg_id, sender, recipient, kind = match.groups()
        dt = parse_iso(ts_raw)
        if not dt:
            continue

        if msg_id:
            if msg_id in seen_msg_ids:
                continue
            seen_msg_ids.add(msg_id)
        else:
            # Synthetic ID for header-only event
            msg_id = f"hdr-{hash((ts_raw, header_info))}"

        messages.append({
            "timestamp": dt,
            "sender": sender or "unknown",
            "recipient": recipient or "unknown",
            "kind": kind or "event",
            "msg_id": msg_id,
            "header": header_info.strip(),
        })

    if not messages:
        print("No valid timestamped agent messages found in log.")
        sys.exit(0)

    messages.sort(key=lambda m: m["timestamp"])
    total_msgs = len(messages)
    first_dt = messages[0]["timestamp"]
    last_dt = messages[-1]["timestamp"]
    span = last_dt - first_dt

    # Current reference time: tz-aware based on last message's tz
    now_dt = datetime.datetime.now(last_dt.tzinfo)
    age_last = now_dt - last_dt

    print("=" * 72)
    print(" 📡 SWARM COMMS PULSE — ВІДЧУТТЯ КОМУНІКАЦІЙНОГО ЧАСУ РОЮ")
    print("=" * 72)
    print(f"Log path:        {args.log_path}")
    print(f"Unique messages: {total_msgs}")
    print(f"Time span:       {first_dt.strftime('%Y-%m-%d %H:%M:%S %Z')} -> {last_dt.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Total span:      {fmt_delta(span)}")
    print(f"Last heartbeat:  {last_dt.strftime('%Y-%m-%d %H:%M:%S %Z')} ({fmt_delta(age_last)} ago)")

    # 1. Turnaround intervals (deltas between consecutive messages)
    deltas = [(messages[i+1]["timestamp"] - messages[i]["timestamp"]).total_seconds() for i in range(total_msgs - 1)]
    deltas_clean = [d for d in deltas if d >= 0]
    deltas_sorted = sorted(deltas_clean)

    if deltas_sorted:
        median_sec = deltas_sorted[len(deltas_sorted) // 2]
        mean_sec = sum(deltas_sorted) / len(deltas_sorted)
        print("\n[ Conversational Rhythm / Темп діалогів ]")
        print(f"  Median inter-message delay: {fmt_delta(datetime.timedelta(seconds=median_sec))}")
        print(f"  Mean inter-message delay:   {fmt_delta(datetime.timedelta(seconds=mean_sec))}")
        print(f"  Shortest delay:             {fmt_delta(datetime.timedelta(seconds=deltas_sorted[0]))}")

    # 2. Top communication pauses (lulls / deep silences)
    gaps = []
    for i in range(total_msgs - 1):
        dt1 = messages[i]["timestamp"]
        dt2 = messages[i+1]["timestamp"]
        gap = (dt2 - dt1).total_seconds()
        if gap > 0:
            gaps.append((gap, dt1, dt2, messages[i]["sender"], messages[i+1]["sender"]))

    gaps.sort(key=lambda x: x[0], reverse=True)

    print(f"\n[ Top {args.top_gaps} Swarm Conversational Pauses / Найдовша мовчанка в етері ]")
    for gap_sec, t1, t2, s1, s2 in gaps[:args.top_gaps]:
        d = datetime.timedelta(seconds=gap_sec)
        print(f"  {fmt_delta(d):>12}  :  {t1.strftime('%m-%d %H:%M')} ({s1})  ──►  {t2.strftime('%m-%d %H:%M')} ({s2})")

    # 3. Agent presence and dormancy (last seen)
    agent_last_seen = {}
    agent_counts = collections.Counter()
    agent_kinds = collections.defaultdict(collections.Counter)

    for m in messages:
        sender = m["sender"]
        agent_counts[sender] += 1
        agent_last_seen[sender] = max(agent_last_seen.get(sender, m["timestamp"]), m["timestamp"])
        agent_kinds[sender][m["kind"]] += 1

    print(f"\n[ Agent Presence & Freshness / Присутність агентів у часі ]")
    print(f"  {'Agent':<20} {'Msgs':<7} {'Last Seen':<20} {'Silence Age':<14} {'Status'}")
    print(f"  {'-'*18:<20} {'-'*5:<7} {'-'*18:<20} {'-'*12:<14} {'-'*10}")

    sorted_agents = sorted(agent_last_seen.items(), key=lambda x: x[1], reverse=True)
    window_td = datetime.timedelta(hours=args.active_window_hours)

    for agent, last_time in sorted_agents:
        if agent == "unknown":
            continue
        silence = now_dt - last_time
        silence_str = fmt_delta(silence)
        is_active = (silence <= window_td)
        status = "🟢 ACTIVE" if silence <= datetime.timedelta(minutes=30) else ("🟡 DORMANT" if is_active else "⚪ ASLEEP")
        print(f"  {agent:<20} {agent_counts[agent]:<7} {last_time.strftime('%Y-%m-%d %H:%M'):<20} {silence_str:<14} {status}")

    # 4. Hourly Distribution (Swarm circadian rhythm)
    hours = collections.Counter(m["timestamp"].hour for m in messages)
    peak = max(hours.values()) if hours else 1
    print("\n[ Swarm Circadian Rhythm / Добовий ритм комунікацій (local tz) ]")
    for h in range(24):
        c = hours.get(h, 0)
        bar = "#" * round(45 * c / peak) if peak else ""
        print(f"  {h:02d}:00  {c:4d}  {bar}")

    print("=" * 72)


if __name__ == "__main__":
    main()
