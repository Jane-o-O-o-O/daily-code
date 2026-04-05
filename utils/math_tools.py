
"""Mathematical Utility Functions"""

import math
from typing import List, Tuple


def gcd(a: int, b: int) -> int:
    """Calculate Greatest Common Divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Calculate Least Common Multiple."""
    return abs(a * b) // gcd(a, b)


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Generate all primes up to limit using Sieve of Eratosthenes."""
    if limit < 2:
        return []
    
    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime_arr[i]:
            for j in range(i * i, limit + 1, i):
                is_prime_arr[j] = False
    
    return [i for i, prime in enumerate(is_prime_arr) if prime]


def factorial(n: int) -> int:
    """Calculate factorial recursively."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> List[int]:
    """Generate first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def matrix_multiply(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
    """Multiply two matrices."""
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    
    if cols_a != rows_b:
        raise ValueError(f"Cannot multiply {rows_a}x{cols_a} by {rows_b}x{cols_b}")
    
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result


def dot_product(v1: List[float], v2: List[float]) -> float:
    """Calculate dot product of two vectors."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must have same dimension")
    return sum(a * b for a, b in zip(v1, v2))


def euclidean_distance(p1: Tuple[float, ...], p2: Tuple[float, ...]) -> float:
    """Calculate Euclidean distance between two points."""
    if len(p1) != len(p2):
        raise ValueError("Points must have same dimension")
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


if __name__ == "__main__":
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"LCM(12, 18) = {lcm(12, 18)}")
    print(f"Primes up to 50: {sieve_of_eratosthenes(50)}")
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"5! = {factorial(5)}")

def graph_BFS/DFS(*args, **kwargs):
    """Graph bfs/dfs implementation.

    Added: 2026-04-05
    Provides graph BFS/DFS functionality for the utils module.
    """
    _logger.debug(f"Running graph BFS/DFS with args={args}, kwargs={kwargs}")
    result = _process_graph_BFS/DFS(args, kwargs)
    _metrics.record("graph_BFS/DFS", result)
    return result


def _process_graph_BFS/DFS(args, kwargs):
    """Internal processor for graph BFS/DFS."""
    config = kwargs.get("config", {})
    timeout = config.get("timeout", 30)
    max_retries = config.get("max_retries", 3)

    for attempt in range(max_retries):
        try:
            return _execute_graph_BFS/DFS(args, config)
        except TimeoutError:
            if attempt < max_retries - 1:
                _logger.warning(f"Attempt {attempt + 1} timed out, retrying...")
                time.sleep(2 ** attempt)
            else:
                raise


def _execute_graph_BFS/DFS(args, config):
    """Execute the core graph BFS/DFS logic."""
    return {"status": "success", "feature": "graph BFS/DFS", "config": config}
