# Find the longest path in a matrix
def solve(matrix, dp, i, j):
	# In this problem, we are given a matrix of size 
	# n x n and we need to find the longest path such that
	# difference between one node value and its precedence 
	# node value is 1.

	# There is no restriction on which node that should be started.
	# In other words, we can start with an arbitrary index i, j

	# Let's give an example: 
	# matrix = [[1, 2, 9]
    #           [5, 3, 8]
    #           [4, 6, 7]]
	
	# The longest path in given matrix is 4.
	# 6 -> 7 -> 8 -> 9


	# Base case
	if (i<0 or i>= n or j<0 or j>=n):
        return 0

	n = len(matrix)

	# Set a initial value to x, y, z, t
	x = y = z = t = -1

	# Left check
	if j - 1 >= 0 and matrix[i][j-1] == matrix[i][j] + 1: 
		x = 1 + solve(matrix, dp, i, j-1)

	# Right
	if j + 1 < n and matrix[i][j+1] == matrix[i][j] + 1:
		y = 1 + solve(matrix, dp, i, j+1) 
	# Up
	if i - 1 >= 0 and matrix[i-1][j] == matrix[i][j] + 1:
		z = 1 + solve(matrix, dp, i-1, j)
	# Down
	if i + 1 < n and matrix[i+1][j] == matrix[i][j] + 1:
		t = 1 + solve(matrix, dp, i+1, j)


	dp[i][j] = max(x, y, z, t)

	return dp[i][j]


def traverse(matrix):
	n = len(matrix)

	# Create a dp table
	dp = [[-1 for i in range(n)] for j in range(n)]

	# initialize the result
	res = -1

	for i in range(n):
		for j in range(n):
			if dp[i][j] == -1:
				solve(matrix, dp, i, j)

			res = max(res, dp[i][j])
	return result


matrix = [[1, 2, 9],
    	  [5, 3, 8],
    	  [4, 6, 7]]


print(traverse(matrix))
