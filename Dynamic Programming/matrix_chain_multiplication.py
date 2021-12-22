# Matrix Chain Product
import math

def MCP_Recursive(dimensions, matrix=1, total_operations=0):
	'''
	Problem Definition:
	- Given an array of that contains dimensions, find the most optimal 
	multiplication way.

	Example: [10, 30, 5, 60]
	Output:  4500

	- First  matrix is of shape: 10 x 30
	- Second matrix is of shape: 30 x  5
	- Third  matrix is of shape:  5 x 60

	  Given these matrices, we will paranthesize them in a way that, at the end
	minimum operations are performed. 

	Approach 1: Recursive Solution
	'''

	if matrix == len(dimensions):
		return total_operations


	# Include 
	curr = dimensions[matrix]
	x = MCP_Recursive(dimensions, matrix + 1, total_operations * curr)

	# Exclude
	y = total_operations + math.prod(dimensions[matrix:])

	return min(x, y)


def MCP_DP(dimensions):
	'''
	- In this solution we will use the tabulation method.
	- We will create a dp array of size dp[n][n] where dp[i][j] indicates that
	minimum multiplication if we mutliply matrix_i...matrix_j. 
	'''
	# Create a dp array
	n = len(dimensions)
	dp = [[float('inf') for i in range(n)] 
						for j in range(n)]

	# Set diagonal entries zero since, there is no multiplication there.
	for i in range(n):
		dp[i][i] = 0

	# Build the table
	
	# Take the chain length L
	for L in range(2, n):

		# Take the start point
		for i in range(1, n-L + 1):

			# Take the end point
			j = i + L - 1 # For index: 0 L:2 it will give 1

			for k in range(i, j):

				product = dp[i][k] + dp[k+1][j] + dimensions[i-1] * dimensions[k] * dimensions[j]

				dp[i][j] = min(dp[i][j], product)

	for i in range(n):
		print(dp[i])
	return dp[1][n-1]



dimensions = [1, 2, 3, 4]
# print(MCP_Recursive(dimensions, 2, dimensions[0] * dimensions[1]))
print(MCP_DP(dimensions))
