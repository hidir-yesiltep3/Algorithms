# Maximum sum inceasing subsequence
def maximumSumSubsequence(arr):
	# In this problem, we will find increasing subsequence such that
	# summation  of this subsequence is maximum. Then we will simply return
	# the sum value.

	# We can solve this question with 1D dp array. dp[i]
	# represents the maximum sum of increasing subsequence such that
	# maximum element of this array is arr[i].

	# By looking at back at each time, we can determine the 
	# maximum sum value.

	n = len(arr)
	# Create the dp table
	dp = arr[:]

	# Fill the dp table in bottom-up manner
	for i in range(1, n):
		for j in range(0, i):
			if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
				dp[i] = dp[j] + arr[i]

	return max(dp)

arr = [1, 101, 2, 3, 100, 4, 5]
print(maximumSumSubsequence(arr))
