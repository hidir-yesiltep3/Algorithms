# Maximum subsequence sum such that no three are consecutive
def maxSum(arr):
    # In this problem, we will find the maximum sum subsequence with 
    # the constraint that no three selected element are consecutive. 
    
    # Let's take an example:
        # Input: arr[] = {3000, 2000, 1000, 3, 10}
        # Output: 5013 
        # 3000 + 2000 + 3 + 10 = 5013
    
    # To solve this problem, we will utilize from dynamic programming.
    # We will hold 1D dp array: dp[n] where n is the length of the given array.
    # Then, we have three options:
        # (1) We will discard arr[i]   -> dp[i] = dp[i-1]
        # (2) We will discard arr[i-1] -> dp[i] = dp[i-2] + arr[i]
        # (3) We will discard arr[i-2] -> dp[i] = dp[i-3] + arr[i-1] + arr[i]
    n = len(arr)
    # Base cases
    if n == 1:
        return arr[0]
    
    if n == 2:
        return arr[0] + arr[1]
    
    # Create dp table
    dp = [0 for i in range(n)]
    
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(dp[1], arr[1]+arr[2], arr[0] + arr[1])
    
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3]+ arr[i-1] + arr[i])
    
    return dp[n-1]

arr = [100, 1000, 100, 1000, 1]
print(maxSum(arr))
