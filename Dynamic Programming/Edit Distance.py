def editDistance(s, t):
	# We are given 2 strings s and t and we need to find 
	# minimum cost to convert one of the string to the other one
	# Allowed operations are the followings:
		# (i)   Insert
		# (ii)  Remove
		# (iii) Replace: 'cat' -> 'cut'

	# Observe that, indeed we do not need two distinct operations as 
	# insert and remove. We can either use insertion or remove operations.
	# So, in the olution of this problem, we will consider only two operatios:
		# (i)  Remove
		# (ii) Replace

	# Recursive Relation: The optimal solution is the sum of suboptimal solutions.
	# Then, we can create a recursive relation as follow:
		# sol(n) = (1 + min(replace or insert)) if not equal dp[i-1][j-1] else

	# How to build the table?
	# Consider the inputs: s = "sunday", t = "saturday"
	# 
	#    0 1 2 3 4 5 6 7 8
	# 	------------------
	# 0 |0 1 2 3 4 5 6 7 8 
	# 1 |1   
	# 2 |2 
	# 3 |3
	# 4 |4
	# 5 |5
	# 6 |6

	n, m = map(len, [s, t])

	# Create the table
	dp = [[0 for i in range(m+1)] for j in range(n+1)]

	# Build the table
	for i in range(n+1):
		for j in range(m+1):

			# if first string is of length 0
			# there needs to be j operation
			if i == 0:
				dp[0][j] = j

			# if second string is of length 0
			# there needs to be i operations
			elif j == 0:
				dp[i][0] = i

			# if the last characters are the same
			# ignore them and recurse for remaining strings
			elif s[i-1] == t[j-1]:
				dp[i][j] = dp[i-1][j-1]
			# Otherwise, recurse for optimal solution
			else:
				dp[i][j] = 1 + min(
  								   dp[i-1][j],  # Remove from first  string
  								   dp[i][j-1],  # Remove from second string
  								   dp[i-1][j-1] # Replace one of the characters
								  )

	return dp[n][m]


s = "google"
t = "lookat"
print(editDistance(s, t))
