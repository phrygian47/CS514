def factors(N):
    factors = []

    # Check prime number 2
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    # Check prime number 3
    while N % 3 == 0:
        factors.append(3)
        N //= 3

    # start at i = 5, no need to check even numbers
    # anymore. Properties of prime numbers state
    # that every prime after 3 is next to a multiple
    # of 6. So check i, then i + 2, then iterate by 6.
    # since i starts at 5 it will always be 6k - 1, and
    # i + 2 will be 6k + 1
    i = 5
    while i * i <= N: 
        # factors always come in pairs so we only need to check every number
        # up to the sqaure root of N. We could use math library but I opted
        # to do it by checking if i^2 <= N. Doing this allows us to find
        # every smaller number in a factor pair for the given number.
        while N % i == 0:
            factors.append(i)
            N //= i
        while N % (i+2) == 0:
            factors.append(i+2)
            N //= (i+2)
        i += 6

    # We need to append the final result of N to the result because the loop
    # stops before testing final prime factor, but we do not want to include 1
    # as it is not a prime number.
    if N > 1:
        factors.append(N)
    return factors