"""
TODO: Refactor this code to use a decorator for timing and a generator for prime number generation.
See: https://docs.python.org/3/library/functions.html#property
      https://docs.python.org/3/howto/functional.html#generators
      https://docs.python.org/3/library/time.html
"""

import time

def primes(n):
    result = []
    for x in range(2, n):
        for p in result:
            if x % p == 0:
                break
        else:
            result.append(x)
    return result

def slow_double(x):
    time.sleep(0.01)
    return x * 2

def timeit(fn):
    # TODO: Write a decorator to time function execution and print the time taken
    return fn

# Refactor: primes should be a generator, not return a list; timeit should be a real decorator.
