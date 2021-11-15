def numberOfWays(n):
    # Given 2 x n grid, we will find the
    # number of ways to tile the board 
    # using 2 x 1 tiles.

    # Input: 4
    # Output: 3

    # Explanation:
    # 1) All 4 vertical
    # 2) All 4 horizontal
    # 3) 2 vertical 2 horizontal

    # Solution:
    # Observe that, if we put the 2 x 1 tile vertical, 
    # the problem reduces to finding number of ways to 
    # tile given 2 x (n - 1) board.
    
    # On the other hand, if we put 2 x 1 tile horizontal,
    # we have to put one more 2 x 1 tile horizontal and 
    # problem reduces to finding number of ways to 
    # tile given 2 x (n - 2) board.

    # Base Cases
    if n <= 0:
        return 0

    if n == 1:
        return 1

    # Indeed problem goes to fibonacci problem. We can further optimize the
    # solution putting a memo dictionary as well.
    return numberOfWays(n - 1) + numberOfWays(n - 2)

