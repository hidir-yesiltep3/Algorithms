# Minimum number of jumps to reach end
def solve(arr):
    n = len(arr)
    dp = [float('inf') for i in range(n)]

    # Base case
    if n == 0 or arr[0] == 0:
        return -1
    
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if dp[j] != float("inf") and i <= j + arr[j]:
                dp[i] = dp[j] + 1

    return dp[n-1]

arr = [1, 3, 6, 1, 0, 9]
print(solve(arr)) 
