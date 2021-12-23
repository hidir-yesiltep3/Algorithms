# Merge Sort 

def mergeSort(arr):

	if len(arr) > 1:
		# Get the mid of the array
		mid = len(arr) // 2

		# Left half
		L = arr[:mid]

		# Right half
		R = arr[mid:]

		# Sort the left part
		mergeSort(L)
		
		# Sort the right part
		mergeSort(R)

		# Merge subroutine
		i = j = k = 0

		while i < len(L) and j < len(R): 
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1

			else:
				arr[k] = R[j]
				j+=1

			k+=1

		# Check if there exist any element in arr L
		while i < len(L):
			arr[k] = L[i]
			i+=1
			k+=1

		# Check if there exist any element in arr R
		while j < len(R):
			arr[k] = R[j]
			j+=1
			k+=1


arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print(arr)
