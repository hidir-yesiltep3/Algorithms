# insertion sort implementation
def insertSort(arr):
	n = len(arr)
	for i in range(1, n):
		
		key = arr[i]

		# Move the elements that are greater than
		# key to one posistion ahead.
		
		j = i-1
		while j >= 0 and arr[j] > key:
			arr[j+1] = arr[j]
			j-=1

		arr[j+1] = key


arr = [12, 11, 13, 5, 6]
insertSort(arr)
print(arr)


