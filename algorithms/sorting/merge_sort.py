
"""Merge Sort Implementation"""


def merge_sort(arr: list) -> list:
    """Sort a list using merge sort algorithm.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: list, right: list) -> list:
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_inplace(arr: list, left: int = 0, right: int = None) -> None:
    """In-place merge sort variant."""
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        _merge_inplace(arr, left, mid, right)


def _merge_inplace(arr, left, mid, right):
    """Helper for in-place merge."""
    left_copy = arr[left:mid + 1]
    right_copy = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1
        k += 1
    
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1
    
    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {data}")
    print(f"Sorted: {merge_sort(data)}")
