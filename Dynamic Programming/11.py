# Sequences of given length where every element is more than or equal to twice
# of previous

# First Approach: Recursive Solution. O(2^n) worst case complexity
def numberOfSequencesRecursive(m, n):
	# if the number of sequence is greater than upper bound m,
	# there can not be any sequence satisfying the condition.
	if n > m:
		return 0

	# if n is 0, that means we found a sequence.
	if n == 0:
		return 1


	# Other than those, we have 2 options:
	# 	(1) Reduce the last element value.
	#	(2) Reduce the number of terms.
	res = (numberOfSequencesRecursive(m//2, n-1)+
		   numberOfSequencesRecursive(m-1, n))

	return res





def numberOfSequencesDP(m, n):
	# In this solution we are goint to build a dp 
	# bottom-up manner. Dp size will be: (m+1, n+1)
	# where dp[i][j] represents the number of subarrays of size j
	# in which the maximum number is i.

	# Create the dp array
	dp = [[0 for i in range(n+1)] for j in range(m+1)]

	# For the cases m < n there will be no subarrays satisfying the condition
	# So fill 0 for them. (Indeed, they are all filled with 0 in the initialization)

	'''
	At first, dp table has the form:
	m = 10, n= 4
	
	0 1 2 3 4
	0 0 0 0 0
	1 0
	2 0
	3 0
	4 0
	5 0 
	6 0
	7 0
	8 0 
	9 0
   10 0
	'''


	# Fill for other values
	for i in range(1, m+1):
		for j in range(1, n+1):

			# if max number is less than the size, then fill 
			# with zero
			if i < j:
				dp[i][j] = 0

			elif j ==1:
				dp[i][j] = i
			# Otherwise there are two options:
			# 	(1) Reduce the maximum number by looking dp[i-1][j]
			# 	(2) Look for dp[i//2][j-1] 
			else:
				dp[i][j] = dp[i-1][j] + dp[i//2][j-1]

	return dp[m][n]





m = 10
n = 4

print(numberOfSequencesRecursive(m, n))
print(numberOfSequencesDP(m, n))
# Expected Output: 4
