# Maximum product in an increasing sequence
def maximumProduct(arr):
    # We can solve this question by utilizing 1D dp array.
    # The algorithm resembles maximum sum in an increasing sequence.
    # dp will have size of len(arr). dp[i] denotes maximum product of elements in
    # which the maximum element in the sequence is arr[i].
    n = len(arr)
    # Create the dp table: In this case since the maximum sum of 
    # sequence with size of 1 is that elements itself, we initialize
    # the dp table as same with arr.
    dp = arr[:]

    # build the dp table
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] * arr[i])
    
    return max(dp)


arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(maximumProduct(arr))
