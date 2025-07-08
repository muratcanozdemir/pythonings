"""
TODO: This code recomputes Fibonacci numbers inefficiently, and also shows an awkward way to partially apply a function.
Refactor using `functools.lru_cache` for memoization, and `functools.partial` for ergonomic APIs.
See: https://docs.python.org/3/library/functools.html
"""

# Part 1: Memoization with lru_cache

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Part 2: Partial application

def power(base, exponent):
    return base ** exponent

# The old API expects both arguments every time.
# TODO: Use functools.partial to create a function square(x) == x**2

# Don't remove or rename any functions, just fix inside.
