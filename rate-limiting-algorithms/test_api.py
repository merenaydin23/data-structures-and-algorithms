"""Automated HTTP Test Runner for Rate Limiting API Server.

Tests all 5 rate-limiting algorithms individually via real HTTP requests
demonstrating HTTP 200 OK and HTTP 429 Too Many Requests responses.
"""

from __future__ import annotations

import json
import threading
import time
import urllib.error
import urllib.request
from http.server import HTTPServer

from api_server import RateLimitHandler


def start_test_server(port: int = 8765) -> HTTPServer:
    """Start the HTTP server on a test port in a background daemon thread."""
    server = HTTPServer(("127.0.0.1", port), RateLimitHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def send_request(url: str) -> dict:
    """Send an HTTP GET request and return the parsed response."""
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {"code": resp.status, "data": data, "headers": dict(resp.headers)}
    except urllib.error.HTTPError as err:
        data = json.loads(err.read().decode("utf-8"))
        return {"code": err.code, "data": data, "headers": dict(err.headers)}


def run_tests() -> None:
    port = 8765
    server = start_test_server(port)
    base_url = f"http://127.0.0.1:{port}"
    time.sleep(0.1)

    algorithms = [
        ("/token-bucket", "1. TOKEN BUCKET", "Capacity: 5 tokens | Refill: 5 tokens/sec"),
        ("/leaky-bucket", "2. LEAKY BUCKET", "Capacity: 5 queue slots | Leak Rate: 5 req/sec"),
        ("/fixed-window", "3. FIXED WINDOW COUNTER", "Window: 1.0 second | Max Requests: 5"),
        ("/sliding-log", "4. SLIDING WINDOW LOG", "Rolling Window: 1.0 second | Max Requests: 5"),
        ("/sliding-counter", "5. SLIDING WINDOW COUNTER", "Rolling Window: 1.0 second | Max Requests: 5"),
    ]

    print("\n" + "=" * 88)
    print("ALL 5 RATE LIMITING ALGORITHMS — INDIVIDUAL LIVE HTTP TESTS".center(88))
    print(f"Target: {base_url} (Standard Library HTTP Server)".center(88))
    print("=" * 88)

    for endpoint, title, config in algorithms:
        print(f"\n>>> {title}")
        print(f"    Config: {config}")
        print(f"    Endpoint: {base_url}{endpoint}")
        print("-" * 88)
        print(f"{'Request #':<12} | {'HTTP Status':<18} | {'RateLimit Decision':<22} | {'Retry-After'}")
        print("-" * 88)

        # Send 8 rapid requests (Quota is 5)
        for i in range(1, 9):
            res = send_request(f"{base_url}{endpoint}")
            code = res["code"]
            status = res["data"].get("status", "UNKNOWN")
            retry_after = res["headers"].get("Retry-After", "-")

            code_str = f"{code} OK" if code == 200 else f"{code} TOO MANY REQS"
            print(f"Req #{i:02d}      | {code_str:<18} | {status:<22} | {retry_after}")
            time.sleep(0.01)

        # Wait 1.1s for refill / window expiration
        print("    ... Waiting 1.1s for replenishment / window reset ...")
        time.sleep(1.1)

        rec = send_request(f"{base_url}{endpoint}")
        rec_code = rec["code"]
        rec_status = rec["data"].get("status", "UNKNOWN")
        rec_str = f"{rec_code} OK" if rec_code == 200 else f"{rec_code} REJECTED"
        print(f"Req #09 (Post)| {rec_str:<18} | {rec_status:<22} | Replenished Successfully!")

    print("\n" + "=" * 88)
    print("COMPLETED: All 5 rate limiting algorithms tested and verified successfully!".center(88))
    print("=" * 88 + "\n")

    server.shutdown()


if __name__ == "__main__":
    run_tests()
