"""Leaky Bucket Rate Limiting Algorithm.

Time Complexity: O(1) amortized | Space Complexity: O(Capacity)
"""

from __future__ import annotations

import collections
import time
from typing import Any, Deque, Optional


class LeakyBucket:
    """Traffic-shaping leaky bucket using a FIFO queue to leak requests steadily."""

    def __init__(self, capacity: int, leak_rate: float) -> None:
        self.capacity: int = int(capacity)
        self.leak_rate: float = float(leak_rate)
        self.queue: Deque[Any] = collections.deque()
        self.last_leak_timestamp: float = time.time()

    def allow_request(self, request_id: Any, current_time: Optional[float] = None) -> bool:
        """Drop request if queue is full; otherwise enqueue and leak at constant rate."""
        now = time.time() if current_time is None else current_time
        elapsed = max(0.0, now - self.last_leak_timestamp)

        # Leak processed requests from the queue based on elapsed time
        leaked = int(elapsed * self.leak_rate)
        if leaked > 0:
            for _ in range(min(leaked, len(self.queue))):
                self.queue.popleft()
            self.last_leak_timestamp = now if not self.queue else self.last_leak_timestamp + (leaked / self.leak_rate)

        if len(self.queue) < self.capacity:
            self.queue.append(request_id)
            return True
        return False
