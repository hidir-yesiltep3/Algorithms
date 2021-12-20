# Maximum sum in a 2 x n grid such that no two elements are adjacent
def solve(grid):
	n = len(grid[0])

	# Create the dp table
	dp = [0 for i in range(n+2)]

	for i in range(2, n+2):

		# Case1: Include
		dp[i] = dp[i-2] + max(grid[0][i-2], grid[1][i-2])

		# Case2: Exclude
		dp[i] = max(dp[i], dp[i-1])

	return max(dp)

arr = [[0, 4, 5],
	   [20, 0, 0]]

print(solve(arr))
