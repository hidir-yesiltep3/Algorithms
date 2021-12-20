# Path with maximum average value
def solve(cost):
    # Given path is of shape N x N
    n = len(cost)
    
    # Create a dp table
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, n+1):

            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i-1][j-1]

    return dp[n][n] / (2 * n - 1)


cost = [[1, 2, 3],
        [6, 5, 4],
        [7, 3, 9]]
    
print(solve(cost))
