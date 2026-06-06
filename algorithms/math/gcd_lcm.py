"""GCD and LCM implementations"""

import math
from typing import Tuple


def gcd(a: int, b: int) -> int:
    """Compute GCD using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Compute LCM using GCD."""
    return abs(a * b) // gcd(a, b) if a and b else 0


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended Euclidean algorithm: returns (gcd, x, y) where a*x + b*y = gcd."""
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x


if __name__ == "__main__":
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"LCM(48, 18) = {lcm(48, 18)}")
    g, x, y = extended_gcd(48, 18)
    print(f"Extended GCD: {g}, x={x}, y={y}")
