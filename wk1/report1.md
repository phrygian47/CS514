# Week 1

Write an efficient Python function named `factors(N)` that returns all prime factors of an integer `N ≥ 1`, including multiplicity, in increasing order.

## Source Code

```python
def factors(N):
    i = 2
    num = N
    factors = []
    while i * i <= num:
        while num % i == 0:
            factors.append(i)
            num //= i
        i += 1
    if num > 1:
        factors.append(num)
    return factors
```

## Algorithm Run Time Analysis

### Part A

Since multiplication, division, modulo, addition, and subtraction all take constant time, the main part of the algorithm to consider are the 2 while loops and how many times they iterate.

The best case scenario for this algorithm would be if the input `N` is a power of 2 (N = 2<sup>k</sup>). Let us take a look at 2048 (2<sup>11</sup>). For this example the prime factors would be equal to `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]`. On the first iteration of the outer loop `i == 2` and `num` starts at `N`. The inner loop then divides `num` by 2 repeatedly, appending each divisor to the result list, until `num` is reduced to `1`. For 2048, this loop runs a total of 11 times. Since the inner loop halves `num` until it reaches `1`, and N = 2<sup>k</sup>, the inner loop runs k times, where k = log<sub>2</sub>N. Once `num` is reduced to 1, the outer loop condition evalutes to false, causing the loop to terminate after just 1 outer loop iteration. This means the best case scenario time complexity is $\theta$(logN).
