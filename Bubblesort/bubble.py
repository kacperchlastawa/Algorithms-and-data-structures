def bubblesort(arr):
	for i in range(len(arr) - 1):
		for j in range(len(arr) - i - 1):
			if arr[j] > arr[j + 1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	return arr


tests = [
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 3, 1], [1, 1, 2, 3, 3]),
    ([7], [7]),
    ([], []),
    ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8])
]

for arr, expected in tests:
    result = bubblesort(arr[:])  
    print(f"Input: {arr}, Output: {result}, Expected: {expected}, OK: {result == expected}")

