# Data Structures and Algorithms

A comprehensive, production-grade reference repository of core data structures, classical computer science algorithms, and distributed systems engineering patterns.

> **Zero External Dependencies**: All implementations are written in pure Python using only standard library modules (`time`, `collections`, `typing`, `heapq`). No virtual environment (`venv`) or external packages are required to run any of the modules.

---

## Repository Structure

```
data-structures-and-algorithms/
├── Data Compression Algorithms/   # Information theory & compression
│   └── Huffman/                   # Huffman Coding algorithm
├── Search_Algorithims/            # Search algorithms & trees
│   ├── Binary_Search.py           # Iterative & recursive binary search
│   ├── linear_search.py           # Linear search implementation
│   ├── binary_search_tree.py      # Binary Search Tree (BST) operations
│   ├── graph-algorithms/          # BFS / DFS graph traversals
│   └── Hashing Functions/         # Hash functions & collision handling
├── Sort_Algorihims/               # Classical sorting algorithms
│   ├── Bubble_Sort/               # Bubble sort
│   ├── Bucket_Sort/               # Bucket sort
│   ├── Heap_Sort/                 # Heap sort & binary heaps
│   ├── İnsertion Sort/            # Insertion sort (Python & Java)
│   ├── Merge_Sort/                # Merge sort (Python & Java)
│   ├── Quick_Sort/                # Quick sort
│   └── Selection_Sort/            # Selection sort
└── rate-limiting-algorithms/      # Production API rate-limiting patterns
    ├── token_bucket.py            # Token Bucket (weighted LLM token limits)
    ├── leaky_bucket.py            # Leaky Bucket (FIFO queue traffic shaper)
    ├── fixed_window_counter.py    # Fixed Window (with boundary spike analysis)
    ├── sliding_window_log.py      # Sliding Window Log (100% precision)
    ├── sliding_window_counter.py  # Sliding Window Counter (Cloudflare weighted)
    ├── simulation.py              # Side-by-side 5-algorithm burst benchmark
    ├── api_server.py              # Lightweight HTTP test server (HTTP 200 vs 429)
    └── test_api.py                # Automated live HTTP test client
```

---

## Quickstart & Execution

Every algorithm in this repository can be executed directly from your terminal:

```bash
# Run the 5-algorithm rate limiting simulation:
python rate-limiting-algorithms/simulation.py

# Run the live HTTP rate limiter test (HTTP 200 OK vs HTTP 429 Too Many Requests):
python rate-limiting-algorithms/test_api.py

# Run classical algorithms:
python "Search_Algorithims/Binary_Search.py"
python "Sort_Algorihims/Quick_Sort/quick_sort.py"
```
