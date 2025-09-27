def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    i += 1
    arr[i], arr[end] = arr[end], arr[i]

    return i    

def quickSort(arr, start, end):
    if end <= start:
        return
    pivot = partition(arr, start, end)
    quickSort(arr, start, pivot - 1)
    quickSort(arr, pivot + 1, end)
    return arr

tests = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [3, 1, 2, 3, 1],
    [7],
    [],
    [5, 3, 8, 4, 2],
    [10, 7, 8, 9, 1, 5],
    [20, 18, 12, 8, 5, -2],
    [100, 90, 70, 80, 60, 50, 40],
    [15, 3, 27, 14, 35, 10, 7, 42, 1]
]

for arr in tests:
    original = arr[:]
    quickSort(arr, 0, len(arr) - 1)
    print(f"Input: {original}, Sorted: {arr}")