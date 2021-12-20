def uglyNumber(n):
    # We are going to store the numbers in ugly array
    ugly = [0] * n

    # First ugly number is 1 by convention
    ugly[0] = 1

    # Declare the indexes associated with multiple of 2, 3 and 5
    i2 = i3 = i5 = 0

    # Declare the next multiples of 2, 3 and 5
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    # Loop over the n ugly numbers
    # By the end of this process we will find the n-th ugly number at the
    # location ugly[-1]
    for l in range(1, n):
        # Find the l+1-th ugly number (Since 1 is the first ugly number)
        ugly[l] = min(next_multiple_of_2,
                      next_multiple_of_3,
                      next_multiple_of_5)

        # Check which factor is used while finding the l+1-th ugly number        
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
        
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3

        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
    
    return ugly[-1]


if __name__ == '__main__':
    n = 150
    print(uglyNumber(n)) # Returns 5832
 
