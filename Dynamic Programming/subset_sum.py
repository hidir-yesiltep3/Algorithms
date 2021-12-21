def solve(arr, m):
	# In this problem we are asked to find the existance of that
	# whether there is a subset in given array arr such that
	# sum of this subset is equal to the given value n.

	# We can solve this question by using 2D dp table where of size
	# dp[m+1][n+1] where n denotes the length of the arr

	# Consider the example input of: arr = [3, 34, 4, 12, 5, 2] and m = 9

	# At first, look up table will look like the following
	#
	#   0 1 2 3 4 5 6
	# 0 T T T T T T T
	# 1 F
	# 2 F
	# 3 F
	# 4 F
	# 5 F
	# 6 F 
	# 7 F
	# 8 F
	# 9 F
	#10 F

	# Note that, for zero sum, we initialized the table with all of True's.
	# The reason for that is empty set will be equal to the sum 0, i.e sum({]}) = 0.
	
	n = len(arr)

	dp = [[False for i in range(n + 1)] for j in range(m + 1)] 

	# Fill for zero-th row
	for i in range(n+1):
		dp[0][i] = True


	# Build the table bottom-up manner
	for i in range(1, m + 1):
		for j in range(1, n + 1):

			if i < arr[j - 1]:
				dp[i][j] = dp[i][j-1]

			else:
				dp[i][j] = dp[i][j-1] or dp[i - arr[j-1]][j]

	return dp[-1][-1]


arr = [1, 5, 3, 7, 4]
m = 12

print(solve(arr, m))
