"""Search algorithms for 2026-04-07"""

def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    d = [1,3,5,7,9,11,13]
    print(f"linear 7: {linear_search(d, 7)}")
    print(f"binary 7: {binary_search(d, 7)}")
