"""LeetCode #1: Two Sum"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Find two indices whose values sum to target."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("All tests passed!")
