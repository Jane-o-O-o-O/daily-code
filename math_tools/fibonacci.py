"""Fibonacci sequence implementations"""

from typing import List


def fibonacci_recursive(n: int) -> int:
    """Get nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Get nth Fibonacci number using iteration."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_sequence(n: int) -> List[int]:
    """Generate first n Fibonacci numbers."""
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def fibonacci_generator():
    """Infinite Fibonacci generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print(f"F(10) recursive: {fibonacci_recursive(10)}")
    print(f"F(10) iterative: {fibonacci_iterative(10)}")
    print(f"First 15: {fibonacci_sequence(15)}")
