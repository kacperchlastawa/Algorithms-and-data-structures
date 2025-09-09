def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr,target):
    arr_sorted = sorted(arr)
    left, right = 0, len(arr_sorted) -1 
    while left <= right:
        mid = (left + right) // 2
        if arr_sorted[mid] == target:
            return mid
        elif arr_sorted[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

lista = [3, 2, 5, 3, 6, 9, 1, 4, 8]
print(linear_search(lista, 5))  
print(linear_search(lista, 10))

tests = [
    ([1, 3, 5, 7, 9], 1, 0),
    ([1, 3, 5, 7, 9], 9, 4),
    ([1, 3, 5, 7, 9], 5, 2),
    ([2, 4, 6, 8, 10], 1, -1),
    ([2, 4, 6, 8, 10], 15, -1),
    ([1, 3, 5, 7, 9], 4, -1),
    ([5], 5, 0),
    ([5], 2, -1),
    ([], 3, -1),
]

for arr, x, expected in tests:
    result = binary_search(arr, x)
    print(f"binary_search({arr}, {x}) = {result}, expected = {expected}")