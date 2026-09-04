#!/usr/bin/env python3
"""guard-inbox-latency.py — apply the same time-perception principle to Guard's own review queue.

knowledge/guard-reference-inbox.mylog pairs two record types by `topic`:
`reference-candidate` (recorded-at-unix, when proposed) and `review-record`
(reviewed-at-unix, when triaged). Neither alone tells you anything about
backlog health; joined, they answer two real questions: how long does a
reviewed candidate typically wait (latency), and — more important — which
still-pending candidates are actually aging in the backlog right now, not
just "pending" as an undifferentiated flat status.

Cheap and read-only: one file read, no network, no writes.

Usage:
    python3 guard-inbox-latency.py [path-to-guard-reference-inbox.mylog]

Origin: 2026-09-04, Claude Sonnet 5 (Pramāṇa), applying the same
git-commit-rhythm principle (see repo-time-rhythm.py) to Guard's own
candidate queue after the owner asked whether it applied there too. First
real run found 28/72 candidates with zero review-record at all, oldest
over 3 days old, against a ~1h median latency for the ones that did get
reviewed -- a real, previously invisible backlog-age signal.
"""

import argparse
import datetime
import re
import time


def parse_records(content, form_name):
    return re.findall(rf'\({form_name}\b.*?\)\)(?=\s*\n)', content, re.DOTALL)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "path",
        nargs="?",
        default="/home/agents/ecosystem/knowledge/guard-reference-inbox.mylog",
    )
    ap.add_argument("--top-oldest", type=int, default=10, help="how many oldest unreviewed candidates to show")
    args = ap.parse_args()

    with open(args.path) as f:
        content = f.read()

    candidates = parse_records(content, "reference-candidate")
    reviews = parse_records(content, "review-record")

    now = int(time.time())

    cand_recorded_at = {}
    for r in candidates:
        topic_m = re.search(r'\(topic "([^"]*)"\)', r)
        rec_m = re.search(r"\(recorded-at-unix (\d+)\)", r)
        if topic_m and rec_m:
            topic = topic_m.group(1)
            rec = int(rec_m.group(1))
            cand_recorded_at[topic] = min(rec, cand_recorded_at.get(topic, rec))

    reviewed_at = {}
    for r in reviews:
        topic_m = re.search(r'\(topic "([^"]*)"\)', r)
        rev_m = re.search(r"\(reviewed-at-unix (\d+)\)", r)
        if topic_m and rev_m:
            reviewed_at[topic_m.group(1)] = int(rev_m.group(1))

    print(f"reference-candidate records: {len(candidates)} ({len(cand_recorded_at)} unique topics)")
    print(f"review-record records: {len(reviews)} ({len(reviewed_at)} unique topics)")

    latencies = []
    pending = []
    for topic, rec in cand_recorded_at.items():
        if topic in reviewed_at:
            latencies.append((reviewed_at[topic] - rec, topic))
        else:
            pending.append((now - rec, topic))

    latencies.sort()
    pending.sort(reverse=True)

    if latencies:
        n = len(latencies)
        print(f"\nreview latency (reviewed-at - recorded-at), n={n}:")
        print(f"  median: {datetime.timedelta(seconds=latencies[n // 2][0])}")
        print(f"  fastest: {datetime.timedelta(seconds=latencies[0][0])} ({latencies[0][1]})")
        print(f"  slowest: {datetime.timedelta(seconds=latencies[-1][0])} ({latencies[-1][1]})")

    print(f"\ngenuinely unreviewed (no review-record at all): {len(pending)}")
    print(f"oldest {args.top_oldest}:")
    for age, topic in pending[: args.top_oldest]:
        print(f"  {str(datetime.timedelta(seconds=age)):>20}  {topic}")


if __name__ == "__main__":
    main()
