"""
Dynamic programming problem:
    Given n, return l a list of the least amount of numbers squared
    necessary to sum to n

E.g. 1 = 1**2, 2 = 1**2 + 1**2, 3 = 1**2 + 1**2 + 1**2, 4 = 2**2, ...,
    12 = 3**2 + 1**2 + 1**2 +
"""
import math

def prime_sum(n, memoizer={}):
    if n in memoizer:
        return memoizer[n]
    elif int(math.sqrt(n))**2 == n:
        memoizer[n] = 1
        return 1
    elif n <= 3:
        memoizer[n] = n
        return n

    res = n

    for i in range(1, n):
        if i*i > n:
            break
        res = min(res, 1 + prime_sum(n-i))

    memoizer[n] = res
    return res



def test_prime_sum():
    res = ([(val, prime_sum(val)) for val in range(1, 20000)])


if __name__ == "__main__":
    test_prime_sum()
