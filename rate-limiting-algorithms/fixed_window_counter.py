"""Fixed Window Counter Rate Limiting Algorithm.

Time Complexity: O(1) | Space Complexity: O(1)
"""

from __future__ import annotations

import time
from typing import Optional


class FixedWindowCounter:
    """Fixed window counter dividing time into static slices."""

    def __init__(self, window_size_in_seconds: float, max_requests: int) -> None:
        self.window_size_in_seconds: float = float(window_size_in_seconds)
        self.max_requests: int = int(max_requests)
        self.current_window: int = int(time.time() // self.window_size_in_seconds)
        self.counter: int = 0

    def allow_request(self, current_time: Optional[float] = None) -> bool:
        """Evaluate request within current window.

        VULNERABILITY: Boundary Spike / Double Quota Leak
        Traffic arriving at the tail of window N (e.g. 00:59) and the head of window
        N+1 (e.g. 01:00) both pass, allowing 2x max_requests in a 2-second interval.
        """
        now = time.time() if current_time is None else current_time
        window = int(now // self.window_size_in_seconds)

        if window != self.current_window:
            self.current_window = window
            self.counter = 0

        if self.counter < self.max_requests:
            self.counter += 1
            return True
        return False
