# First Approach: Recursion
def subsetSumRecursive(arr, total):
	'''
		In this implementation, we can find 
		existance of the solution by including or
		excluding the first element of the current array.

		This will yield a tree. Tree elements are:
		1) arr:   current array
		2) total: an integer indicating the requested sum - current_sum

		Worst case time complexity: O(2^n)

	'''
	# Base case
	if total == 0:
		return True

	if total < 0 or len(arr) == 0:
		return False

	x = subsetSum(arr[1:], total)
	y = subsetSum(arr[1:], total - arr[0])


	return x or y

# Second Approach
def subsetSumDynamic(arr, total):
	
	# Create a dp array
	dp = [[False for i in range(total+1)] for j in range(len(arr)+1)]

	# Fill for zero: rows
	for row in range(len(arr)+1):
		dp[row][0] = True

	# After filling first entries of every row, i.e 
	# for every element in the arr, let's fill the 
	# dp array bottom-up manner
	
	for i in range(1, len(arr)+1):
		for j in range(1,total+1):
			
			if j < arr[i-1]:
				dp[i][j] = dp[i-1][j]

			else:
				dp[i][j] = dp[i-1][j] or dp[i][j-arr[i-1]]
	
	return dp[len(arr)][total]


arr = [3, 34, 4, 12, 5, 2]
total = 9

print(subsetSumDynamic(arr, total))
