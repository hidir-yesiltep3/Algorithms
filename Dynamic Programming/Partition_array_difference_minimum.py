# Partition a set into two subsets 
# such that the difference of subset sums is minimum
def partitionDP(arr):
	n = len(arr)
	dp  = [0 for i in range(n + 1)]

	total = sum(arr)
	
	for i in range(2, n+1):

		# include
		x = dp[i-1] - 2 * arr[i-1]

		# exclude
		y = dp[i-1]

		dp[i] = min(abs(x), abs(y))
	print(dp)
	return dp[n]
	



arr = [69, 62, 31]
print(partitionDP(arr))



# arr:    [1, 6, 11, 5]
# output: 1
