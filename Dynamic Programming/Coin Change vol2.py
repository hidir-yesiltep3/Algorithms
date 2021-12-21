def solve2D(coins, money):
	# In this problem we are given coin list = {c1, c2 ..., cm}
	# and we need to find the minimum number of coins to obtain
	# money. To solve this question we can utilize from dp in two manner.

	# The first approach is using 2D dp array to memorize previous
	# suboptimal solutions.
	n = len(coins)
	
	# Create a dp array with size dp[money+1][n+1]. dp[i][j] indicates
	# that, number of minimum coins to obtain i coins.
	dp = [[0  for i in range(n+1)] for j in range(money+1)]

	# Fill the 0 coins part with all ones since we can have zero total money
	# by not adding any coins.
	for col in range(n+1):
		dp[0][col] = 1

	# Build the table
	# We will build the table with the following manner:
		# (i)  Including the current coin
		# (ii) Excluding the current coin
	for i in range(1, money+1):
		for j in range(1, n+1):
			
			# Base case
			if i < coins[j-1]:
				dp[i][j] = dp[i][j-1]
			
			else:
				# Including the current coin
				x =  dp[i - coins[j-1]][j]

				# Excluding the current coin
				y = dp[i][j-1]

				dp[i][j] = x + y

	return dp[money][n]


coins = [2, 5, 3, 6]
money = 10
print(solve2D(coins, money))

# coins [1, 2, 3], money = 4
#    
#    coins
#   0 1 2 3
# 0 1 1 1 1 
# 1
# 2
# 3
# 4

