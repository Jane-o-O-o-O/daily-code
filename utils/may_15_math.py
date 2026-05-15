"""Math helpers for 2026-05-15"""

def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)

def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

if __name__ == "__main__":
    print(f"5! = {factorial(5)}")
    print(f"2^10 = {power(2, 10)}")
