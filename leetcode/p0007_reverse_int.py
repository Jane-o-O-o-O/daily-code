
"""LeetCode #7: Reverse Integer"""


def reverse(x: int) -> int:
    """Reverse digits of a 32-bit signed integer."""
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    result = 0
    while x > 0:
        result = result * 10 + x % 10
        x //= 10
    
    result *= sign
    
    # Check 32-bit overflow
    if result < -2**31 or result > 2**31 - 1:
        return 0
    return result


if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
    print("All tests passed!")
