# Quick Sort implementation

def partition(start, end, arr):
	# Set the last element as pivot
	pivot = arr[end]

	# We will use the index i for putting next sorted element in order.
	i = start -1

	for j in range(start, end):
		# Whenever an element which is smaller than the pivot element is 
		# encountered, put it in the place of i.

		# Do not forget to increment the index i before the replacing operation.
		if arr[j] <= pivot:
			i+=1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[end] = arr[end], arr[i+1]

	return i + 1


def quickSort(start, end, arr):
	
	if start < end:
		# q gives the last element index which has the correct position.
		q = partition(start, end, arr)
		quickSort(start, q-1, arr)
		quickSort(q+1, end, arr)

arr = [12, 11, 5, 3, 2, 1]
start = 0
end = len(arr) - 1

quickSort(start, end, arr)
print(arr)
