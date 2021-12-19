# Longest Common Subsequence
# First Approach: Recursion
# Complexity: O(2^n)
def LCS(A, B, m, n):
	# If either A or B has a length zero at the end of the 
	# process, we just return 0.
	if m == 0 or n == 0:
		return 0

	if A[m-1] == B[n-1]:
		return 1 + LCS(A, B, m-1, n-1)

	return max(LCS(A, B, m-1, n),
			   LCS(A, B, m, n-1)) 




# Second Approach: Dynamic Programming
def lcsDP(A, B):
	m = len(A)
	n = len(B)

	# Create the dp array
	dp = [[0 for i in range(n+1)] for j in range(m+1)]

	# Build the table bottom-up manner
	# dp[i][j] represents longest common subsequence 
	# between up to A[i] and up to B[j]

	for i in range(1, m+1):
		for j in range(1, n+1):

			if A[i-1] == B[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1

			else:
				dp[i][j] = max(dp[i-1][j],
							   dp[i][j-1])

	return dp[m][n]






A = "AGGTAB"
B = "GXTXAYB"
print(LCS(A, B, len(A), len(B)))
print(lcsDP(A, B))
