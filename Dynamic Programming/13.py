# Longest Repeated Subsequence Problem
def lrs(string):
	 # This problem is similar to "Longest Common Subsequence Problem"
	 # where given string is compared with itself.

	 # Only constraint is that, when we compare this string with itself,
	 # we should pay regard that str[i] == str[j] whenever i != j

	 n = len(string)

	 # Create a dp array
	 dp = [[0 for i in range(n+1)] for j in range(n+1)]

	 # Fill the dp table
	 for i in range(1, n+1):
	 	for j in range(1, n+1):

	 		if string[i-1] == string[j-1] and i != j:
	 			dp[i][j] = dp[i-1][j-1] + 1

	 		else:
	 			dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	 return dp[n][n]


string = "AABEBCDD"
print(lrs(string))
# Expected Output: 3
# "ABD"
