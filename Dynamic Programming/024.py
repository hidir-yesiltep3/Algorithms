# 1395 - Leetcode: Count Number  of Teams
def solve(rating):
	n = len(rating)
	dp = [[1, 0, 0] for i in range(n)]

	for i in range(1, n):
		for j in range(i):

			if rating[i] > rating[j]:
				dp[i][1] += dp[j][0]
				dp[i][2] += dp[j][1]

	a = sum(dp[i][2] for i in range(n))

	dp = [[1, 0, 0] for i in range(n)]

	for i in range(1, n):
		for j in range(i):

			if rating[i] < rating[j]:
				dp[i][1] += dp[j][0]
				dp[i][2] += dp[j][1]


	b = sum(dp[i][2] for i in range(n))

	return a + b

rating = [1, 2, 3, 4]
print(solve(rating))
