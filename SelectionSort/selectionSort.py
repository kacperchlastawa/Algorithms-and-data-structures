def selection_sort(arr):
	for i in range(len(arr) - 1):
		min = i 
		for j in range(i+1, len(arr)):
			if(arr[min] > arr[j]):
				min = j
		temp = arr[i]
		arr[i] = arr[min]
		arr[min] = temp
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
    result = selection_sort(arr[:])
    print(f"Input: {arr}, Output: {result}, Expected: {expected}, OK: {result == expected}")