"""Token Bucket Rate Limiting Algorithm.

Time Complexity: O(1) | Space Complexity: O(1)
"""

from __future__ import annotations

import time
from typing import Optional


class TokenBucket:
    """Token bucket rate limiter supporting bursts and weighted consumption (LLM tokens)."""

    def __init__(self, capacity: float, refill_rate: float, initial_tokens: Optional[float] = None) -> None:
        self.capacity: float = float(capacity)
        self.refill_rate: float = float(refill_rate)
        self.tokens: float = self.capacity if initial_tokens is None else float(initial_tokens)
        self.last_refill_timestamp: float = time.time()

    def allow_request(self, tokens_requested: int = 1, current_time: Optional[float] = None) -> bool:
        """Allow request if sufficient tokens exist; handles weighted limits."""
        now = time.time() if current_time is None else current_time
        elapsed = max(0.0, now - self.last_refill_timestamp)
        self.tokens = min(self.capacity, self.tokens + (elapsed * self.refill_rate))
        self.last_refill_timestamp = now

        if self.tokens >= tokens_requested:
            self.tokens -= tokens_requested
            return True
        return False
