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

Since multiplication, division, modulo, addition, and subtraction all take constant time, the main part of the algorithm to consider is the while loop.

The best case scenario for this algorithm would be if the input `N` only has small prime factors. A good example of this is any `N` where 2<sup>N</sup>
