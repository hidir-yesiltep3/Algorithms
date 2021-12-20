# Count all subsequences having product less than K

def productLessThanK(arr, k):
    # In this problem, we can count the number of subsequences using 2D dp array.
    # We will define the array as dp[k+1][n+1] where n denotes the length of the arr.
    # Then dp[i][j] will denote total number of subsequence having product less than or equal to i in which
    # arr[j] is involved.

    # For every j value, (and arr[j]) dp[i][j] will be at least dp[i][j-1]. Since total number of subsequences
    # of max length j consists of length j-1 as well.

    # Other than that, we will examine if dp[i // arr[j-1]][j-1] exists and we will increase the count by this amount.
    # Note that, in the above computation, we are looking the total product i // arr[j-1] but we specifically look
    # for sequences of size j-1. Then we add this number to 1: {arr[j-1]}.

    n = len(arr)
    # Create the dp table
    dp = [[0 for j in range(n+1)] for i in range(k+1)]

    # Build the table
    for i in range(1, k+1):
        for j in range(1, n+1):

            dp[i][j] = dp[i][j-1]

            if arr[j-1] <= i:
                dp[i][j] += dp[i // arr[j-1]][j-1] + 1
    
    return dp[k][n]

arr = [1, 2, 3, 4]
k = 10
print(productLessThanK(arr, k))
