"""Sort helpers for 2026-04-09"""

def bubble_sort(arr):
    n = len(arr)
    a = arr[:]
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        mi = i
        for j in range(i+1, len(a)):
            if a[j] < a[mi]:
                mi = j
        a[i], a[mi] = a[mi], a[i]
    return a

if __name__ == "__main__":
    d = [64,25,12,22,11]
    print(f"bubble: {bubble_sort(d)}")
    print(f"selection: {selection_sort(d)}")
