def fibonacci_1(n):
    # This solution has O(N) time complexity
    # and O(N) space complexity

    # We simply initiate a fibonacci array
    # and add the other fibonacci numbers looking at the
    # previous ones.
    if n <= 2:
        return 1
    
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    
    return fib[-1]


def fibonacci_2(n):
    # This solution has O(N) time complexity 
    # and O(1) space complexity

    # Instead of keeping a fib list and storing all the fibonacci 
    # numbers, we can accomplish the same process keeping only two variables
    if n <= 2:
        return 1

    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    
    return b

def fibonacci_3(n, memo={}):
    if n <= 2:
        return 1

    if memo.get(n, None):
        return memo[n]
    
    memo[n] = fibonacci_3(n - 1, memo) + fibonacci_3(n - 2, memo)
    return memo[n]

    

if __name__ == '__main__':
    print(fibonacci_1(55)) # 139583862445
