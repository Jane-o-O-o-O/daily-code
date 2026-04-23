
"""LeetCode #1: Two Sum"""


def two_sum(nums: list, target: int) -> list:
    """Find two indices that add up to target.
    
    Time: O(n), Space: O(n)
    """
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

# [2026-04-23] Tests for p0001_two_sum
class TestP0001TwoSum:
    """Test suite for p0001_two_sum — tree traversal."""

    def setup_method(self):
        """Setup test fixtures."""
        self.fixture = {}
        self.config = {"enabled": True, "debug": False}

    def test_basic_tree_traversal(self):
        """Test basic tree traversal functionality."""
        result = process(self.fixture, config=self.config)
        assert result is not None
        assert result.get("status") == "success"

    def test_tree_traversal_with_empty_input(self):
        """Test tree traversal with empty input."""
        result = process({}, config=self.config)
        assert result is not None

    def test_tree_traversal_error_handling(self):
        """Test tree traversal error handling."""
        with pytest.raises(ValueError):
            process(None, config=self.config)

    def test_tree_traversal_caching(self):
        """Test tree traversal caching behavior."""
        result1 = process(self.fixture, config=self.config)
        result2 = process(self.fixture, config=self.config)
        assert result1 == result2
