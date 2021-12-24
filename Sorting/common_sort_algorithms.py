# Insertion sort
def insertion(arr):
	'''
	Approach:
	- In insertion sort, we take each element and find its correct position
	in the sorted array by moving the element which are greater than this element
	ahead. Let's take an example:
	
	- Suppose the array we will sort is  [13, 12, 11, 6, 9].
	Steps:
	For index 0: Do nothing
	For index 1: Start from index 0, whenever you encounter a greater element, move it to right.
				 # [12, 13, 11, 6, 9]
	For index 2: Apply the same step for index 2.
				 # [11, 12, 13, 6, 9]
	For index 3: Apply the same step for index 2.
				 # [6, 11, 12, 13, 9]
	For index 4: Apply the same step for index 2.
				 # [6, 9, 11, 12, 13,]
	
	#########################################################################################################
	
	Complexity Analysis:
	- If the array is already sorted, it takes O(n) times for comparing -> Best-case time complexity O(n)
	- If the array is sorted from reverse, then for each element in position i (0 based) there needs to be i
	comparision. total n * (n+1) / 2 comparision. -> Worst-case time complexity O(n^2)

	
	Note: For small input sizes, insertion sort beats merge sort.
	- Stable
	'''
	n = len(arr)

	# if arr consists of only one element
	# just return.
	if n == 1:
		return arr

	for i in range(1, n):
		# Take the element to be sorted 
		element = arr[i]
		j = i-1
		while j >= 0 and arr[j] > element:
			arr[j+1] = arr[j]
			j-=1

		arr[j+1] = element

	return arr


# Bubble sort
def bubble(arr):
	'''
	Approach:
	-In bubble sort, we put the maximum element among unsorted ones to the correct place each time.
	To do this, we iterate over n times to correctly find the position of n elements. Each time if an element
	is greater than the element next to it we propagate it ahead.
	
	- Suppose the array we will sort is  [13, 12, 11, 6, 9].
	Steps:
	For index 0: [12, 11, 6, 9, 13]
	For index 1: [11, 6, 9, 12, 13]
	For index 2: [6, 9, 11, 12, 13]
	For index 3: [6, 9, 11, 12, 13]
	for index 4: [6, 9, 11, 12, 13]
	
	#########################################################################################################
	
	Complexity Analysis:
	- Best  case time complexity: O(n)
	- Worst case time complexity: O(n^2)
	- Stable
	'''
	n = len(arr)

	if n == 1:
		return arr

	for i in range(n):
		# Indicator that if an element is swapped.
		swapped = False

		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True

		if not swapped:
			break
	return arr



# Selection sort
def selection(arr):
	pass


# Quick sort
def partition(arr, l, r):
	'''
	Partition function is a subroutine of a quick sort. 
	Average time complexity O(n)
	'''
	# Set the pivot element as the first element
	pivot = arr[l]

	i = l-1
	for idx in range(l, r):
		if arr[idx] < pivot:
			i+=1
			arr[i] = arr[idx]
	
	# Put the pivot in the correct position
	arr[i+1] = pivot

	# Return the most recent sorted position.
	return i + 1

def quicksort(arr, l, r):
	'''
	Approach:
	- Quick sort uses `partition` algorithm as subroutine.
	- `partition` subroutine returns the index which contains the element that is correctly
	positioned.
	- After sorting an element, we sort its left half and right half.
	
	########################################################################################

	Complexity Analysis:
	- Best case time complextiy: O(nlogn)
	- Average time complexity: O(nlogn)
	- Worst case complexity: O(n^2)

	- Not stable
	'''

	if l < r:
		q = partition(arr, l, r)
		quicksort(arr, l, q-1)
		quicksort(arr, q+1, r)

	return arr


# Merge sort
def merge(arr, L, R):
	
	i = j = k = 0

	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			arr[k] = L[i]
			i+=1

		else:
			arr[k] = R[j]
			j+=1
		
		k+=1

	while i < len(L):
		arr[k] = L[i]
		i+=1
		k+=1

	while j < len(R):
		arr[k] = R[j]
		j+=1
		k+=1

	return arr

def mergesort(arr):
	
	if len(arr) > 1:
		mid = len(arr) // 2

		L = arr[:mid]
		R = arr[mid:]

		mergesort(L)
		mergesort(R)

		return merge(arr, L, R)




# Count sort
def count_subroutine(arr, exp):
	n = len(arr)

	# Initialize the output array
	output = [0 for i in range(n)]

	# Intitialize the count array
	count =  [0 for i in range(10)]

	for i in range(n):
		idx = arr[i] // exp
		count[idx % 10] += 1

	# count[i] now contains the number of elements whose exp-th last-index
	# is i. Now, we will process the count array such that count[i] will 
	# contain the actual positions of the elements.

	for i in range(1, 10):
		count[i] += count[i-1]

	# Let's take a simple example
	# Consider that input arr = [5, 3, 4, 23, 15]
	# in the first time arr is called by countSort, the count array will
	# look like this:
	# [0 0 0 0 0 0 0 0 0 0] -> [0 0 0 2 1 2 0 0 0 0] -> [0 0 0 2 3 5 0 0 0 0]

	# Build the output array
	i = n - 1
	while i >= 0:
		index = arr[i] // exp
		output[count[index % 10] - 1] = arr[i] 
		count[index % 10] -= 1
		i-=1

# Radix sort
def radix(arr):
	# Since maximum comparision will be based on the length of the
	# max element, take the max element.
	max_element = max(arr)

	# Count sort will be used as a subroutine.
	# Note that, count sort is a stable sorting algorithm.

	exp = 1
	while max_element / exp > 1:
		count_subroutine(arr, exp)
		exp *= 10


	return arr





arr = [13, 12, 11, 6, 9]
print(insertion(arr))
print(bubble(arr))
print(quicksort(arr, 0, 4))
print(mergesort(arr))
print(radix(arr))
