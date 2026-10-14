"""Rate Limiting Algorithms Side-by-Side Simulation.

Simulates a 50-request burst with a 10 req/sec limit across all 5 algorithms.
"""

from __future__ import annotations

import os
import sys
import time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from fixed_window_counter import FixedWindowCounter
from leaky_bucket import LeakyBucket
from sliding_window_counter import SlidingWindowCounter
from sliding_window_log import SlidingWindowLog
from token_bucket import TokenBucket


def run_burst_simulation(num_requests: int = 50, limit: int = 10, interval: float = 1.0) -> None:
    """Run side-by-side burst comparison of all 5 rate limiters."""
    tb = TokenBucket(capacity=limit, refill_rate=limit / interval)
    lb = LeakyBucket(capacity=limit, leak_rate=limit / interval)
    fw = FixedWindowCounter(window_size_in_seconds=interval, max_requests=limit)
    swl = SlidingWindowLog(window_size_in_seconds=interval, max_requests=limit)
    swc = SlidingWindowCounter(window_size_in_seconds=interval, max_requests=limit)

    fmt = "{:<10} | {:<5} | {:<12} | {:<12} | {:<12} | {:<12} | {:<14}"
    tag = lambda ok: "ALLOWED" if ok else "REJECTED"

    print("\n" + "=" * 90)
    print(f"BURST SIMULATION: {num_requests} Requests against {limit} req/{interval}s Limit")
    print("=" * 90)
    print(fmt.format("Timestamp", "Req #", "Token Bucket", "Leaky Bucket", "Fixed Window", "Sliding Log", "Sliding Counter"))
    print("-" * 90)

    start = time.time()
    counts = {k: 0 for k in ["tb", "lb", "fw", "swl", "swc"]}

    for i in range(1, num_requests + 1):
        now = time.time()
        res_tb = tb.allow_request(1, current_time=now)
        res_lb = lb.allow_request(f"req-{i}", current_time=now)
        res_fw = fw.allow_request(current_time=now)
        res_swl = swl.allow_request(current_time=now)
        res_swc = swc.allow_request(current_time=now)

        for key, res in [("tb", res_tb), ("lb", res_lb), ("fw", res_fw), ("swl", res_swl), ("swc", res_swc)]:
            counts[key] += int(res)

        print(fmt.format(f"+{now - start:06.3f}s", f"#{i:02d}", tag(res_tb), tag(res_lb), tag(res_fw), tag(res_swl), tag(res_swc)))
        time.sleep(0.005)

    print("-" * 90)
    print(f"SUMMARY: Allowed / {num_requests} Total Requests")
    for name, key in [("Token Bucket", "tb"), ("Leaky Bucket", "lb"), ("Fixed Window", "fw"), ("Sliding Log", "swl"), ("Sliding Counter", "swc")]:
        print(f"  - {name:<23}: {counts[key]} allowed ({counts[key] / num_requests * 100:.1f}%)")
    print("=" * 90 + "\n")


if __name__ == "__main__":
    run_burst_simulation()
