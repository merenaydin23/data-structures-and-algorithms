"""Lightweight HTTP API Server for Testing Rate Limiting Algorithms.

Pure Python standard library (no pip dependencies required).
Listens on http://localhost:8000
"""

from __future__ import annotations

import json
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from fixed_window_counter import FixedWindowCounter
from leaky_bucket import LeakyBucket
from sliding_window_counter import SlidingWindowCounter
from sliding_window_log import SlidingWindowLog
from token_bucket import TokenBucket

LIMITERS = {
    "/token-bucket": TokenBucket(capacity=5, refill_rate=5),
    "/leaky-bucket": LeakyBucket(capacity=5, leak_rate=5),
    "/fixed-window": FixedWindowCounter(window_size_in_seconds=1.0, max_requests=5),
    "/sliding-log": SlidingWindowLog(window_size_in_seconds=1.0, max_requests=5),
    "/sliding-counter": SlidingWindowCounter(window_size_in_seconds=1.0, max_requests=5),
}


class RateLimitHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        path = urlparse(self.path).path
        limiter = LIMITERS.get(path)

        if not limiter:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Endpoint not found"}')
            return

        allowed = limiter.allow_request(f"req-{id(self)}") if path == "/leaky-bucket" else limiter.allow_request()
        status_code = 200 if allowed else 429

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("X-RateLimit-Limit", "5")
        self.send_header("X-RateLimit-Status", "ALLOWED" if allowed else "REJECTED")
        if not allowed:
            self.send_header("Retry-After", "1")
        self.end_headers()

        body = {
            "status": "ALLOWED" if allowed else "RATE_LIMITED",
            "endpoint": path,
            "http_status": status_code,
        }
        self.wfile.write(json.dumps(body, indent=2).encode("utf-8"))

    def log_message(self, format: str, *args) -> None:
        # Custom log formatting for clarity
        print(f"[{args[1]}] {args[0]}")


def run(port: int = 8000) -> None:
    server = HTTPServer(("127.0.0.1", port), RateLimitHandler)
    print(f"HTTP Rate Limit Test Server running on http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
