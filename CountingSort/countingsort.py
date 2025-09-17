def countingSort(arr):
    if len(arr) == 0:
        return arr
    max = arr[0]
    for j in arr:
        if j > max:
            max = j
    new_arr = [0 for i in range(0, max + 1)]
    for i in range(len(arr)):
        new_arr[arr[i]] += 1

    for k in range(1, len(new_arr)):
        new_arr[k] = new_arr[k] + new_arr[k - 1]

    sorted_arr = [0 for i in range(len(arr))]

    for t in range(len(arr)-1,-1,-1): # to make it more stable
        sorted_arr[new_arr[arr[t]] - 1] = arr[t]
        new_arr[arr[t]] -= 1

    return sorted_arr

tests = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 3, 1], [1, 1, 2, 3, 3]),
    ([7], [7]),
    ([], []),
    ([4, 2, 2, 8, 3, 3, 1], [1, 2, 2, 3, 3, 4, 8])
]

for arr, expected in tests:
    result = countingSort(arr[:])
    print(f"Input: {arr}, Output: {result}, Expected: {expected}, OK: {result == expected}")