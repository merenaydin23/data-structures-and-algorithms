"""Sliding Window Log Rate Limiting Algorithm.

Time Complexity: O(N) worst-case prune, O(1) amortized | Space Complexity: O(N)
Trade-off: 100% boundary accuracy, but high memory footprint storing every timestamp.
"""

from __future__ import annotations

import collections
import time
from typing import Deque, Optional


class SlidingWindowLog:
    """Sliding window log maintaining exact timestamps to eliminate boundary spikes."""

    def __init__(self, window_size_in_seconds: float, max_requests: int) -> None:
        self.window_size_in_seconds: float = float(window_size_in_seconds)
        self.max_requests: int = int(max_requests)
        self.logs: Deque[float] = collections.deque()

    def allow_request(self, current_time: Optional[float] = None) -> bool:
        """Purge expired timestamps and grant request if within capacity."""
        now = time.time() if current_time is None else current_time
        threshold = now - self.window_size_in_seconds

        while self.logs and self.logs[0] <= threshold:
            self.logs.popleft()

        if len(self.logs) < self.max_requests:
            self.logs.append(now)
            return True
        return False
