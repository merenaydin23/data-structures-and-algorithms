"""Sliding Window Counter (Weighted Approximation) Rate Limiting Algorithm.

Time Complexity: O(1) | Space Complexity: O(1)
Approximates sliding counts using Cloudflare's weighted overlapping window formula.
"""

from __future__ import annotations

import time
from typing import Optional


class SlidingWindowCounter:
    """Sliding window counter using previous and current window counts."""

    def __init__(self, window_size_in_seconds: float, max_requests: int) -> None:
        self.window_size_in_seconds: float = float(window_size_in_seconds)
        self.max_requests: int = int(max_requests)
        self.current_window: int = int(time.time() // self.window_size_in_seconds)
        self.current_count: int = 0
        self.prev_count: int = 0

    def allow_request(self, current_time: Optional[float] = None) -> bool:
        """Evaluate request using weighted linear interpolation formula."""
        now = time.time() if current_time is None else current_time
        window = int(now // self.window_size_in_seconds)

        if window == self.current_window + 1:
            self.prev_count, self.current_count, self.current_window = self.current_count, 0, window
        elif window != self.current_window:
            self.prev_count, self.current_count, self.current_window = 0, 0, window

        elapsed = min(max(now - (self.current_window * self.window_size_in_seconds), 0.0), self.window_size_in_seconds)
        count = self.prev_count * ((self.window_size_in_seconds - elapsed) / self.window_size_in_seconds) + self.current_count

        if count < self.max_requests:
            self.current_count += 1
            return True
        return False
