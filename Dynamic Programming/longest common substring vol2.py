def solve(s, t):
	# We are given two strings: s and t. We need to find the
	# longest common substring. 
	
	# To do so, we can create a 2D dp array dp[n][m] where
	# n is the length of s and m is the length of t.
	
	# Then dp[i][j] will denote the longest common substring between the 
	# s[:i] and t[:j]
	
	n = len(s)
	m = len(t)

	# Create the dp table
	dp = [[0 for i in range(m+1)] for j in range(n+1)]

	# Build the table
	for i in range(1, n+1):
		for j in range(1, m+1):

			if s[i-1] != t[j-1]:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

			else:
				dp[i][j] = dp[i-1][j-1] + 1

	return dp[n][m]


s = "DCXZTY"
t = "GDTXADC"


def solve(s, t):
	dp = [0] * (min(len(s), len(t)) + 1)

	dp[0] = 1
	
print(solve(s, t))


