"""
Dynamic Programming Review

Fibonacci ->
    fib(0) = 0
    fib(1) = 1
    fib(2) = 1
    ...
    fib(n) = fib(n-1) + fib(n-2)
"""

def fib_naive(n):
    if not n:
        return 0
    elif n < 3:
        return 1
    return fib_naive(n-1) + fib_naive(n-2)

def fib_mem(n, memoizer={0: 0, 1: 1, 2: 1}):
    if n in memoizer:
        return memoizer[n]
    memoizer[n] = fib_mem(n-1) + fib_mem(n-2)
    return memoizer[n]

def fib_bottom_up(n):
    fib = {0: 0, 1: 1, 2: 1}
    for i in range(n+1):
        if i in fib: continue
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


def test():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for fib_func in [fib_naive, fib_mem, fib_bottom_up]:
        calculated = [fib_func(i) for i in range(10)]
        assert(expected == calculated)


if __name__ == "__main__":
    test()
