"""Number utils for 2026-04-26"""

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)

def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def is_perfect(n):
    if n < 2: return False
    return sum(i for i in range(1, n) if n % i == 0) == n

if __name__ == "__main__":
    print(f"153 armstrong? {is_armstrong(153)}")
    print(f"digit sum 9876: {digit_sum(9876)}")
    print(f"28 perfect? {is_perfect(28)}")
