"""List utility functions"""

from typing import List, Any, Optional


def flatten(nested: list) -> list:
    """Flatten a nested list."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst: list, size: int) -> List[list]:
    """Split a list into chunks of given size."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def find_duplicates(lst: list) -> list:
    """Find duplicate elements in a list."""
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)


def rotate_left(lst: list, k: int) -> list:
    """Rotate list left by k positions."""
    if not lst:
        return lst
    k = k % len(lst)
    return lst[k:] + lst[:k]


def rotate_right(lst: list, k: int) -> list:
    """Rotate list right by k positions."""
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]


if __name__ == "__main__":
    print(f"Flatten: {flatten([1, [2, 3], [4, [5, 6]]])}")
    print(f"Chunk: {chunk([1,2,3,4,5,6,7], 3)}")
    print(f"Duplicates: {find_duplicates([1,2,3,2,4,3,5])}")
    print(f"Rotate left: {rotate_left([1,2,3,4,5], 2)}")
    print(f"Rotate right: {rotate_right([1,2,3,4,5], 2)}")
