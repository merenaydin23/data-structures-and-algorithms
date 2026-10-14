# Rate Limiting Algorithms in Python

Production-grade reference implementations of the five fundamental API rate-limiting algorithms using Python's standard library.

## Comparison Matrix

| Algorithm | Burst Support | Output Traffic | Memory | Time | Best Use Case |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Token Bucket** | Yes | Bursty | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | API Gateways (Stripe, AWS), LLM Token limits |
| **Leaky Bucket** | No (Queued) | Constant/Smooth | $\mathcal{O}(\text{Cap})$ | $\mathcal{O}(1)$ | Traffic shaping, backend protection |
| **Fixed Window** | Yes (At boundary) | Bursty | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | Simple limits (has boundary spike flaw) |
| **Sliding Window Log** | Moderate | Smooth | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ | High-precision audit/security endpoints |
| **Sliding Window Counter** | Moderate | Smooth (approx.) | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | Distributed high-scale systems (Cloudflare) |

---

## Algorithms & Usage

### 1. Token Bucket (`token_bucket.py`)
Accumulates tokens up to `capacity` at a constant `refill_rate`. Supports weighted requests for LLM prompt/completion tokens.
```python
from token_bucket import TokenBucket

limiter = TokenBucket(capacity=100, refill_rate=10.0)
if limiter.allow_request(tokens_requested=15):  # e.g., 15 LLM tokens
    process_request()
```

### 2. Leaky Bucket (`leaky_bucket.py`)
Buffers requests into a FIFO queue (`collections.deque`) and drains them at a uniform `leak_rate`. Drops when full.
```python
from leaky_bucket import LeakyBucket

shaper = LeakyBucket(capacity=20, leak_rate=5.0)
if shaper.allow_request("req-1"):
    process_request()
```

### 3. Fixed Window Counter (`fixed_window_counter.py`)
Tracks counts inside discrete time windows (`int(time // window_size)`).
> **Vulnerability Note**: Vulnerable to the **Double Quota Leak** (boundary spike). Bursts sent right before and right after the window reset allow up to $2\times$ the limit across a short boundary interval.
```python
from fixed_window_counter import FixedWindowCounter

limiter = FixedWindowCounter(window_size_in_seconds=60.0, max_requests=100)
if limiter.allow_request():
    process_request()
```

### 4. Sliding Window Log (`sliding_window_log.py`)
Stores exact request timestamps in a deque, purging expired ones dynamically. Guarantees 100% boundary accuracy at the cost of memory.
```python
from sliding_window_log import SlidingWindowLog

limiter = SlidingWindowLog(window_size_in_seconds=1.0, max_requests=10)
if limiter.allow_request():
    process_request()
```

### 5. Sliding Window Counter (`sliding_window_counter.py`)
Approximates rolling counts with zero log storage using Cloudflare's weighted interpolation:
$$\text{count} = \text{prev\_count} \times \frac{\text{window\_size} - \text{elapsed}}{\text{window\_size}} + \text{current\_count}$$
```python
from sliding_window_counter import SlidingWindowCounter

limiter = SlidingWindowCounter(window_size_in_seconds=1.0, max_requests=10)
if limiter.allow_request():
    process_request()
```

---

## Running the Simulation

Compare all 5 algorithms side by side under a 50-request burst (10 req/s limit):

```bash
python simulation.py
```
*(Or from repo root: `python rate-limiting-algorithms/simulation.py`)*
