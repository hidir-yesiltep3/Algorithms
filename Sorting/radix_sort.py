# Radix sort

def radix(arr):
	# Since maximum comparision will be based on the length of the
	# max element, take the max element.
	max_element = max(arr)

	# Count sort will be used as a subroutine.
	# Note that, count sort is a stable sorting algorithm.

	exp = 1
	while max_element / exp > 1:
		countSort(arr, exp)
		exp *= 10


	return arr

# Subroutine
def countSort(arr, exp):

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


	# Copy from output to arr
	for i in range(n):
		arr[i] = output[i]


arr = [1, 11, 5, 3, 4, 23, 15]
print(radix(arr))
