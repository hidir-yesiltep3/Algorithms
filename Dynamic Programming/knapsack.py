# Knapsack Problem
def knapsackRecursive(weight, value, W, total=0):
    """
    Problem Definition:
        In this problem, we are asked to implement the optimum case for
    putting items into a knapsack. Consider that we have different objects
    each of which has a value assigned them and a weight they possess. We will
    try to find the maximum value we can get without exceeding the knapsack weight
    limit.

    Parameters:
        weight:  Weight list assigned to each item.
        value:   Value  list assigned to each item.
        W:       Knapsack capacity.
        total:   total weight up to that function call.

    Approach 1: Recursive solution.
        We can recursively search for all possible combinations and then
    return the maximum profit. To do this we need 2 operations:
            (i)  Include the current element
            (ii) Exclude the current element
        And then, return the maximum.
    """

    if len(weight) == 0:
        return 0

    x = 0
    # Include
    if total + weight[0] <= W:
        x = value[0] + knapsackRecursive(weight[1:], value[1:], W, total + weight[0])

    # Exclude
    y = knapsackRecursive(weight[1:], value[1:], W, total)

    return max(x, y)


def knapsackDP(weight, value, W):
    """
    Problem Definition:
        In this problem, we are asked to implement the optimum case for
    putting items into a knapsack. Consider that we have different objects
    each of which has a value assigned them and a weight they possess. We will
    try to find the maximum value we can get without exceeding the knapsack weight
    limit.

    Parameters:
        weight:  Weight list assigned to each item.
        value:   Value  list assigned to each item.
        W:       Knapsack capacity.

    Approach 2: Dynamic Programming
        Create a 2D dp array of size dp[n+1][W+1] where n is the length of the
    weight (and values) list. Then fill the table by the following algorithm:
        (i)  If weight of the knapsack j is less than the weight of the element weight[i-1],
    then set dp[i][j] = dp[i-1][j] because the optimum solution is recorded previously.
        (ii) Else, return the maximum result between value of the element + dp[knapsack weight - value weight] and
    dp[i-1][j].  
    """
    n = len(weight)
    dp = [[0 for j in range(W + 1)] for j in range(n + 1)]

    # Build the table
    for i in range(1, n+1):
        for j in range(1, W+1):
            
            if j < weight[i-1]:
                dp[i][j] = dp[i-1][j]
            
            else:
                dp[i][j] = max(value[i-1] + dp[i-1][j-weight[i-1]],
                               dp[i-1][j])
    
    return dp[-1][-1]


value = [10, 15, 40]
weight = [1, 2, 3]
W = 6

print(knapsackRecursive(weight, value, W))
print(knapsackDP(weight, value, W))
# print(sum(value[:4]) + value[5])
