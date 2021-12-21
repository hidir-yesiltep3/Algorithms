def solve(n):
	dp = [0 for i in range(n+1)]

	dp[1] = 1
	dp[2] = 2
	dp[3] = 4

	if n <= 3:
		return dp[n]

	for i in range(4, n + 1):
		dp[i] += dp[i-1] + dp[i-2] + dp[i-3]


	return dp[n]




n = 4
print(solve(n))
