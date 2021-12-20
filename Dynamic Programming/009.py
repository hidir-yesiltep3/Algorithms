# Perfect Sum Problem

# This problem is similar to the Subset Sum problem except that
# In addition to find existance of a solution, we need to print all of 
# the subset satisfying given sum.

def PerfectSum(arr, total):
	n = len(arr)
	
	# Create a dp array
	dp = [[False for i in range(total+1)] for j in range(n+1)]

	# Fill for zeros: row
	for row in range(n+1):
		dp[row][0] = True

	# We don't need to traverse for filling columns since
	# we set it when initializing step.

	# Fill for other values
	for i in range(1, n+1):
		for j in range(1, total+1):

			if arr[i-1] > j:
				dp[i][j] = dp[i][j-1]

			elif arr[i-1] <= j:
				dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

	# We filled the entire array, now we need to recursiveley 
	# traverse the array to find each of the subset whose sum is
	# equal to the given sum: total.

	def findSubsets(summation, i=n, subset=[]):
		# Base cases: we have two base cases
		# 1. We reached the end and summation is not zero:
			# a. if dp[i][summation] is True we add it to the subset
		# 2. We can get summation 0 before the index is reached to 0.

		if summation == 0:
			print(subset)
			return

		if i == 1:
			if arr[0] == summation:
				print(subset + [arr[0]])
			return

		# If current sum can be reached by excluding the 
		# current element.
		# Note that, we do this operation if and only if 
		# current sum is reachable by previous steps.
		if dp[i-1][summation]:
			new_subset = subset[:] # create a copy
			findSubsets(summation, i-1, new_subset)

		# If current sum can be reached by including the 
		# current element.
		if summation >= arr[i-1] and dp[i-1][summation-arr[i-1]]:
			subset.append(arr[i-1])
			findSubsets(summation-arr[i-1], i-1, subset)


	if dp[n][total] == False:
		print("No subset is present.")
		return

	findSubsets(total)


arr = [2, 3, 5, 6, 8, 10]
total = 10

PerfectSum(arr, total)
