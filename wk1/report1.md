# Week 1

Write an efficient Python function named `factors(N)` that returns all prime factors of an integer `N ≥ 1`, including multiplicity, in increasing order.

## Source Code

```python
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
```

## Algorithm Time Complexity Analysis

### Best Case

Since we are to assume that multiplication, division (including modulo). addition, and subtraction all takes constant time, then the key consideration is how many iterations does each loop body perform.

Let us take a look at a best case example. For this purpose we will consider the best case to be a number whose only prime factors are small, or specifically a number that is equal to $2^k$ where `k` is any positive integer. We'll start with $2^{11}$ or 2048. We start at `N = 2048` and enter the first loop body since `N` is divisible by 2. we then append a 2 to our factors list which takes constant time. Afterwards we divide `N` by 2 which is also constant time. We continue to do this until `N` is no longer divisible by 2. For this example it will iterate 11 times, finishing with `N = 1`. From this we can conclude that this loop will run `k` times if `N` = $2^k$, or it runs $log_2N$ times. Since `N` is now equal to `1`, the algorithm never enters either remaining loop body, leaving these checks as constant time. The final comparison also runs in constant time. This leaves us with a best case scenario run time of $C_1 \log_2 N + C_0$ where $C_1$ is the constant cost for each loop iteration, and $C_0$ is the cost of all other operations.

Under model b, `N` has `b` bits where `b` is the number of bits required to represent `N` in binary. It would take `b` iterations for the loop with the loop body taking due to the modulo divisionbeing defined as $\Theta(b^2)$ time in this model. So the cost of all iterations is $\theta(b * b^2)$ or $\theta(b^3)$.

### Worst Case

Now let us look at the worst case time complexity. The worst case would be if `N` is a prime number. This would mean that the algorithm never enters the first or second loop body. These would be considered constant time operations. The final loop body is where the biggest cost is. Since `N` is prime in this case, the algorithm will never enter the inner loop body of the final while loop, which means the upper bound is never decreased and instead the loop must iterate through all possible primes up to the $\sqrt{N}$. However, due to the properties of prime numbers, we know we only need to check numbers that multiples of $6 \pm 1$. As a result the algorithm only checks every 2 out of 6 numbers. The loop body itself only takes constant time, as every operation within the loop body takes constant time. This leaves the time efficiency of the algorithm as $C_1 \sqrt{N} + C_0$ where $C_1$ is the constant cost for each loop iteration, and $C_0$ is the constant cost of all other operations. This simplifies directly to $O(\sqrt{N})$ time.

Under model b each iteration now costs $C_0b^2 + C_1b$. Since $b\leq b^2$ for every $b\geq 1$ each iteration can be written as $(C_0 + C_1)b^2$ so we can conclude each iteration runs in $O(b^2)$. If we multiple this by our number of iterations, our time complexity now becomes $b^2 \sqrt N$

### Median and Mean averages

For the mean average time complexity across all possible inputs `N`, the run time is dominated by the worst case. While primes and near primes are rare, their cost in efficiency is much greater. Hence we can expect the mean average run time of the algorithm to be O($\sqrt{N}$), which resembles the worst case.

For the median average time complexity across all possible inputs `N`, I would expect the runtime to be somewhere in the middle. While the worst case cost in efficiency is much greater, there are a greater number of non primes and numbers with small prime factors. This skews the median average towards the best case over the mean average.

### b is proportional to n

We know that b is proportional to n. To represent an integer n in binary $\left\lfloor\\log_2(n) + 1\right\rfloor$ bits are required. Similarly, to represent an integer in decimal, $\left\lfloor\log_{10}(n) + 1\right\rfloor$ are required. The ratio of bits to digits is then $(\left\lfloor\log_2(n) + 1\right\rfloor)/(\left\lfloor\log_{10}(n) + 1\right\rfloor)$. We can then take the $\lim_{n \to \infty} \frac{(\log_2(n) + 1)}{(\log_{10}(n) + 1)}$. As n goes to infinity the constant become insignificant so it can be rewritten as $\lim_{n \to \infty} \frac{(\log_2(n))}{(\log_{10}(n))}$. From here we can use the change of base formula to convert to base 2 $\lim_{n \to \infty} \frac{(\log_2(n))}{(\frac{\log_{2}(n)}{\log_{2}(10)})}$. This simplifies to $\lim_{n \to \infty} \log_2(10)$. Since n is no longer a present variable, the limit of a constant is that constant: $\log_2(10)$ which is about 3.32
