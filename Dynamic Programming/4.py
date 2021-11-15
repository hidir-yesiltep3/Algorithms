def getMaxGold(gold, m, n):
    # In this problem, we are given an m x n
    # gold mine where each cell has a positive
    # integer denoting the number of golds in that
    # particular cell.

    # We are supposed to collect the maximum
    # number of golds. 

    # Note that, since every cell contains a positive
    # integer, total number of golds can only accumulate one way,
    # non-decreasing. We can find the optimal solution by 
    # solving subproblems optimally. To do this, we are going  to
    # calculate maximum number of golds that can be reachable from every 
    # particular cell from right to left in the gold mine, as a result,
    # the maximum one accumulating in the first column will give the result.

    goldTable = [[0 for x in range(n)] for y in range(m)]

    for col in range(n-1, -1, -1):
        for row in range(m):
            # Gold collection for right cell (->)
            if col == n-1:
                right = 0
            else:
                right = goldTable[row][col+1]

            # Gold collection for right-up cell (/)
            if row == 0 or col == n-1:
                right_up = 0
            else:
                right_up = goldTable[row-1][col+1]
            
            # Gold collection for right-down cell (\)
            if row == m-1 or col == n-1:
                right_down = 0
            else:
                right_down = goldTable[row+1][col+1]

            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down)
    

    res = goldTable[0][0]
    for i in range(1, m):
        res = max(res, goldTable[0][i])
    
    return res


# Driver Code
if __name__ == '__main__':
    gold = [[1, 3, 1, 5],
            [2, 2, 4, 1],
            [5, 0, 2, 3],
            [0, 6, 1, 2]]

    m = n = 4
    
    print(getMaxGold(gold, m, n))
