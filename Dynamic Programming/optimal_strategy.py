# Optimal Strategy for a game
def optimalRecursive(coins, turn=True):
	# In a game, two users play against each other.
	# There are coins in a row and each player plays optimally to get
	# maximum coin by permanently taking a coin from start index
	# or end index.

	# We will try to determine the maximum coin that first player can have 
	# at the end of the match. Note that, this is highly depend on the first
	# choice. 

	# Parameters:
		# coins: (Integer Array) -> coins that will be chosen.
		# turn:  (Boolean) -> A boolean indicator that indicates whether
		# its first player's move or not.

	# We can recursively solve this question by the following algorithm:
	
	# If its first player's turn, then we should maximize the result by taking
	# either first or last coin.

	# If its second player's turn, since each player play optimally, second player
	# will try to minimize the result of the maximum coins first player can get. 
	
	if len(coins) == 0:
		return 0

	if not turn:
		return min(optimalRecursive(coins[:-1], not turn), 
				   optimalRecursive(coins[1:],  not turn))

	return max(coins[0]  + optimalRecursive(coins[1:],  not turn), 
			   coins[-1] + optimalRecursive(coins[:-1], not turn))




arr1 = [ 8, 15, 3, 7 ]
print(optimalRecursive(arr1))
 
arr2 = [ 2, 2, 2, 2 ]
print(optimalRecursive(arr2))
 
arr3 = [ 20, 30, 2, 2, 2, 10]
print(optimalRecursive(arr3))
