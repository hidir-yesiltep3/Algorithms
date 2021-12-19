# Largest Subset where each pair is divisible

def LargestDivisibleSubset(arr):
	# Sort the given array
	arr.sort()
	n = len(arr)

	# Create the dp array
	# dp[i] corresponds to the maximum number of elements
	# in a subset including arr[i]
	dp = [0 for i in range(n)]

	# Obviously, since the last element is the 
	# greatest element overall in the given array,
	# maximum number of elements in a subset containing it will
	# be of size 1.
	dp[-1] = 1

	# Fill the other values for smaller elements
	for i in range(n-2, -1, -1):
		# Since divison, and modulo operations are not defined
		# for denominator 0, we just continue whenever 0 is encountered.
		if arr[i] != 0:
			max_num_of_elements = 0
			for j in range(i+1, n):
				if arr[j] % arr[i] == 0:
					max_num_of_elements = max(max_num_of_elements, dp[j])

			dp[i] = max_num_of_elements + 1

	return max(dp)


arr = [ 1, 3, 6, 13, 17, 18 ]
print(LargestDivisibleSubset(arr))
