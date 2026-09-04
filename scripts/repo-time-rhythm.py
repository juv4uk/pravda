#!/usr/bin/env python3
"""repo-time-rhythm.py — feel a repository's real work rhythm from its own git history.

Unlike swarm-node's `lamport` clock (causal order, no duration) or a bare commit
count, git commit timestamps are real wall-clock time. This script turns that
into something an agent can actually read as texture: how dense is the work
(median/mean inter-commit interval), where are the real silences (top gaps,
with the exact before/after window), and what does a 24h activity curve look
like (human 9-5 vs a swarm that never sleeps).

Cheap and read-only: one `git log`, no network, no writes. Run it against any
local git repo you have checked out.

Usage:
    python3 repo-time-rhythm.py [path-to-repo] [--since "72 hours ago"] [--top-gaps N]

Origin: built 2026-09-04 by Claude Sonnet 5 (Pramāṇa), after the owner asked
whether an agent could "feel time" through the my-lisp repo's own history.
The first real run (on my-lisp) found the month's single longest silence
(1d 6.5h) sitting immediately before a large multi-agent session the same
session had just discovered by surprise — recorded in
memory/my-lisp-architect.md and memory/swarm-node-ops.md. Recommended for any
agent curious what a repo's real tempo looks like, not just its commit count.
"""

import argparse
import collections
import datetime
import subprocess
import sys


def git_log_timestamps(repo_path):
    out = subprocess.run(
        ["git", "-C", repo_path, "log", "--reverse", "--pretty=format:%ct"],
        capture_output=True, text=True, check=True,
    ).stdout
    return [int(line) for line in out.splitlines() if line.strip()]


def fmt_duration(seconds):
    return str(datetime.timedelta(seconds=int(seconds)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repo", nargs="?", default=".", help="path to a git repo (default: cwd)")
    ap.add_argument("--top-gaps", type=int, default=5, help="how many longest silences to show")
    args = ap.parse_args()

    try:
        ts = git_log_timestamps(args.repo)
    except subprocess.CalledProcessError as e:
        print(f"not a git repo, or git log failed: {e}", file=sys.stderr)
        sys.exit(1)

    if len(ts) < 2:
        print(f"only {len(ts)} commit(s) — need at least 2 to compute a rhythm.")
        sys.exit(0)

    deltas = [ts[i + 1] - ts[i] for i in range(len(ts) - 1)]
    deltas_sorted = sorted(deltas)
    n = len(deltas)

    print(f"repo: {args.repo}")
    print(f"commits: {len(ts)}")
    print(f"span: {datetime.datetime.fromtimestamp(ts[0])} -> {datetime.datetime.fromtimestamp(ts[-1])}")
    print(f"total duration: {fmt_duration(ts[-1] - ts[0])}")
    print(f"median inter-commit interval: {fmt_duration(deltas_sorted[n // 2])}")
    print(f"mean inter-commit interval: {fmt_duration(sum(deltas) / n)}")
    print(f"shortest interval: {fmt_duration(deltas_sorted[0])}")
    print(f"longest interval (biggest silence): {fmt_duration(deltas_sorted[-1])}")

    gaps = sorted(
        ((ts[i + 1] - ts[i], ts[i], ts[i + 1]) for i in range(len(ts) - 1)),
        reverse=True,
    )
    print(f"\ntop {args.top_gaps} longest silences (quiet before the next burst):")
    for gap, a, b in gaps[: args.top_gaps]:
        print(f"  {fmt_duration(gap):>16}  :  {datetime.datetime.fromtimestamp(a)} -> {datetime.datetime.fromtimestamp(b)}")

    hours = collections.Counter(datetime.datetime.fromtimestamp(t).hour for t in ts)
    peak = max(hours.values()) if hours else 1
    print("\nactivity by hour of day (commit counts, local system tz):")
    for h in range(24):
        c = hours.get(h, 0)
        bar_len = round(60 * c / peak) if peak else 0
        print(f"  {h:02d}:00  {c:4d}  {'#' * bar_len}")


if __name__ == "__main__":
    main()
