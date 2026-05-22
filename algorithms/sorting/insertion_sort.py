
"""Insertion Sort Implementation"""


def insertion_sort(arr: list) -> list:
    """Sort a list using insertion sort algorithm.
    
    Time Complexity: O(n^2) worst case, O(n) best case
    Space Complexity: O(1)
    """
    result = arr.copy()
    
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    
    return result


def binary_insertion_sort(arr: list) -> list:
    """Enhanced insertion sort using binary search for position."""
    result = arr.copy()
    
    for i in range(1, len(result)):
        key = result[i]
        left, right = 0, i - 1
        
        while left <= right:
            mid = (left + right) // 2
            if result[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        
        for j in range(i, left, -1):
            result[j] = result[j - 1]
        result[left] = key
    
    return result


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print(f"Original: {data}")
    print(f"Sorted: {insertion_sort(data)}")
    print(f"Binary Sorted: {binary_insertion_sort(data)}")
