# Longest subsequence such that difference between adjacents is one
def solve(arr):
    # This problem is an extension to the problem of longest increasing subsequence problem.
    n = len(arr)
    dp = [1 for i in range(n)]

    for i in range(1, n):
        for j in range(0, i):

            if abs(arr[i] - arr[j]) == 1 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    
    return dp[n-1]


arr = [10, 9, 4, 5, 4, 8, 6]
print(solve(arr))
