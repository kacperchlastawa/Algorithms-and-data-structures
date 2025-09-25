def mergeSort(arr):

	length = len(arr)

	if length <= 1:
		return
	
	middle = length//2
	leftArr = [0] * middle
	rightArr = [0] * (length - middle)
	
	i = 0 #leftArr
	j = 0 #rightArr
	
	for i in range(length):
		if( i < middle):
			leftArr[i] = arr[i]
		
		else:
			rightArr[j] = arr[i]
			j += 1
	mergeSort(leftArr)
	mergeSort(rightArr)
	merge(leftArr, rightArr, arr)






def merge(leftArr, rightArr, arr):
    leftSize = len(arr) // 2
    rightSize = len(arr) - leftSize
    
    i = 0
    l = 0
    r = 0
    
    while l < leftSize and r < rightSize:
        if leftArr[l] < rightArr[r]:
            arr[i] = leftArr[l]
            l += 1
        else:
            arr[i] = rightArr[r]
            r += 1
        i += 1
    
    while l < leftSize:
        arr[i] = leftArr[l]
        l += 1
        i += 1
    
    while r < rightSize:
        arr[i] = rightArr[r]
        r += 1
        i += 1
		

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
    mergeSort(arr)
    print(f"Input: {original}, Sorted: {arr}")

