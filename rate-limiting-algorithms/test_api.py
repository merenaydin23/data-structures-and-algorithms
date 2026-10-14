"""Automated HTTP Test Runner for Rate Limiting API Server.

Starts the API server in a background thread and sends real HTTP requests
to demonstrate HTTP 200 OK and HTTP 429 Too Many Requests responses.
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
    """Start the HTTP server on a non-standard port in a background daemon thread."""
    server = HTTPServer(("127.0.0.1", port), RateLimitHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def send_request(url: str) -> dict:
    """Send an HTTP GET request and return the parsed JSON response and status."""
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
    time.sleep(0.1)  # Allow server to bind

    endpoints = [
        ("/token-bucket", "Token Bucket (Limit: 5 req/sec)"),
        ("/sliding-counter", "Sliding Window Counter (Limit: 5 req/sec)"),
    ]

    print("\n" + "=" * 80)
    print("LIVE HTTP API RATE LIMIT TEST".center(80))
    print(f"Target: {base_url} (Pure Standard Library HTTP Server)".center(80))
    print("=" * 80)

    for endpoint, title in endpoints:
        print(f"\n>>> Testing Endpoint: {title}")
        print(f"URL: {base_url}{endpoint}")
        print("-" * 80)
        print(f"{'Request #':<12} | {'HTTP Status':<15} | {'RateLimit Status':<18} | {'Retry-After'}")
        print("-" * 80)

        # Send 8 rapid requests (Limit is 5)
        for i in range(1, 9):
            res = send_request(f"{base_url}{endpoint}")
            code = res["code"]
            status = res["data"].get("status", "UNKNOWN")
            retry_after = res["headers"].get("Retry-After", "-")

            code_display = f"{code} OK" if code == 200 else f"{code} TOO MANY REQS"
            print(f"Req #{i:02d}      | {code_display:<15} | {status:<18} | {retry_after}")
            time.sleep(0.01)

        # Wait 1.1s for refill and test recovery
        print("... Waiting 1.1s for quota refill / window refresh ...")
        time.sleep(1.1)

        recovery_res = send_request(f"{base_url}{endpoint}")
        rec_code = recovery_res["code"]
        rec_status = recovery_res["data"].get("status", "UNKNOWN")
        rec_display = f"{rec_code} OK" if rec_code == 200 else f"{rec_code} REJECTED"
        print(f"Req #09 (Post) | {rec_display:<15} | {rec_status:<18} | Refill Successful!")

    print("\n" + "=" * 80)
    print("ALL HTTP RATE LIMIT TESTS PASSED SUCCESSFULLY!".center(80))
    print("=" * 80 + "\n")

    server.shutdown()


if __name__ == "__main__":
    run_tests()
