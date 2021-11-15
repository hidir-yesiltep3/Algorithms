def count(S, m, n):
    # In this problem, we are given a number n in which
    # that we are supposed to find the number of ways to obtain
    # this number using the numbers in the set S.

    # We can solve this question using both recursive and
    # Dynamic Programming. In this notebook, I will demonstrate both approach.

    ''''
        Args:
            S: Set corresponding the denomination coins.
            m: Length of the S.
            n: Total amount we need to obtain.
        
        Approach:
            This function corresponds to the recursive solution.
            Let elements of S be denoted as S = {S_1, S_2, ..., S_m}
            Then, we can count the total number of ways by adding presence of  a particular element S_i and 
            absence of this particular element S_i.
    '''

    # Control case
    # If n is 0 then there is only
    # one solution. (Not including any S_i)
    if n == 0:
        return 1

    # If n is less than zero, then there is no
    # way to build it.
    if n < 0:
        return 0

    # If there is no coin to include and still n has
    # some amount greater than 0, again there is no way
    # to build.
    if (m <= 0 and n > 0):
        return 0

    # Count is sum of sub-solutions:
    # (i)  Including the S_m
    # (ii) Excluding the S_m

    return count(S, m, n - S[m-1]) + count(S, m - 1, n)

# Note that, above solution obeys the overlapping subproblems property and we solve for the same 
# subproblems again and again.

# In order to disambiguate this we can solve with Dynamic Programming with Bottom up manner.

# Following function solves the Coin Change problem using Dynamic Programming.

def countDP(S, m, n):
    # Observe that table is of the size (n + 1) x m.
    # Extra 1 row is needed for the subproblem n = 0 case.
    table = [[0 for i in range(m)] for j in range(n + 1)]

    # Fill the first row with all 1's. Reason for this is, we can obtain total
    # 0 coins by not adding any coin from the set S.
    for i in range(m):
        table[0][i] = 1
    
    # Then for every subvalue n (from 1 to n) we are going to consider 2 cases:
    # (i)  Including the S_i.
    # (ii) Excluding the S_i.
    for row in range(1, n+1):
        for col in range(m):

            # Count the solutions including S_i
            x = table[row - S[col]][col] if row - S[col] >= 0 else 0

            # Count the solution excluding S_i
            y = table[row][col - 1] if col >= 1 else 0

            table[row][col] = x + y
    
    return table[n][m-1]


if __name__ == '__main__':
    S = [2, 5, 3, 6]
    m = 4
    n = 10
    print(countDP(S, m, n)) # Output: 5
