# Cutting Rod Problem

def cutRod(prices):
	n_rods = len(prices)

	# Create the dp table
	dp = [0 for i in range(n_rods+1)]

	# Build the table
	for i in range(1, n_rods+1):
		max_val = -1
		
		for j in range(i):
			max_val = max(max_val, prices[j] + dp[i-j-1])
		dp[i] = max_val

	return dp[n_rods]

arr = [1, 5, 8, 9, 10, 17, 17, 20]
print(cutRod(arr))
