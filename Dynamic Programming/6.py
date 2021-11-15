def countPairingRec(n):
    '''
    Problem Definition:
        Given n numbers, we are asked to find the maximum number of 
        groups where each group contains at most 2 people.
        
        Example:
        Input n = 3 -> Output = 4
        
        1) {1, 2, 3}
        2) {(1, 2), 3}
        3) {(1, 3), 2}
        4) {1, (2,3)}
        
    Approach:
        This problem can be solved using recursion, recursion with memoization and 
        Dynamic Programming. In this notebook, I will going to show each of these
        approaches.

        This function is pure recursion without any optimization (memoization). Note that,
        for any element among n elements, (let's call it s_i), we can create groups by either
        determining s_i as single element or pairing the s_i with remaining n-1 elements. The
        addition of solution of these subproblems gives the result.
    '''
    if n <= 2:
        return n

    return countPairingRec(n-1) + (n - 1) * countPairingRec(n - 2)

# Note that above solution has overlapping subproblems problem. Meaning that, subproblems are
# calculated again and again. To solve this and optimize our algorithm, let's look at the 
# following implementation which uses the bottom-up dynamic programming.

def countPairingDP(n):
    '''
    This solution utilizes from 1D Dynamic Programming. 
    In simpler words, we will record solutions of each of the subproblems.
    Using this subsolutions we are going to build the final solution.
    '''
    # Create the dp table
    dp = [0 for i in range(n + 1)]
    
    for i in range(n + 1):
        # For i = 0, 1 and 2 there are 0, 1 and 2 ways respectiveley.
        if i <= 2:
            dp[i] = i
        
        # Otherwise, we use the same formula as above function.
        else:
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]

    return dp[n]


