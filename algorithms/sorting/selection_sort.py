
"""Selection Sort Implementation"""


def selection_sort(arr: list) -> list:
    """Sort a list using selection sort algorithm.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    result = arr.copy()
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    
    return result


def selection_sort_descending(arr: list) -> list:
    """Sort a list in descending order using selection sort."""
    n = len(arr)
    result = arr.copy()
    
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if result[j] > result[max_idx]:
                max_idx = j
        result[i], result[max_idx] = result[max_idx], result[i]
    
    return result


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print(f"Original: {data}")
    print(f"Ascending: {selection_sort(data)}")
    print(f"Descending: {selection_sort_descending(data)}")
