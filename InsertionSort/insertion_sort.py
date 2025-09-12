def insertion_sort(arr):
	for i in range(1,len(arr)):
		temp = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > temp:
			arr[j +1] = arr[j]
			j -= 1
		
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
	result = insertion_sort(arr[:])
	print(f"Input: {arr}, Output: {result}, Expected: {expected}, OK: {result == expected}")

		
		