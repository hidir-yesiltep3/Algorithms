# Minimum cost to fill given weight in a bag
def solve(W, cost):
	# In this problem, we will look for minimum cost
	# to fill a bag with exactly W kg. If it is not possible, i.e
	# There is no combination of kg's to fill by exactly W kg, print -1.

	# We can solve this question with 1D dp array where dp[i] denote the
	# minimum cost to fill the bag with exactly i kg.
	
	n = len(cost)

	# Create the dp array
	dp = [0 for i in range(n + 1)]

	# Build the table
	for i in range(1, n+1):
		min_cost = float("inf")
		 
		for j in range(i):
			if j < n and cost[j] != -1:
				min_cost = min(min_cost, cost[j] + dp[i - j - 1]) # since we pad the dp
																# array with a leading zero														
																# i - (j+1)
		
		dp[i] = min_cost
		 
	print(dp)
	return dp[n]


cost = [20, 10, 4, 50, 100]
W = 5

print(solve(W, cost))
