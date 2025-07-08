from pythonings.ex04_functools import fib, power

import functools

def test_fib_speed_and_correctness():
    import time
    start = time.time()
    result = fib(30)
    elapsed = time.time() - start
    assert result == 832040
    assert elapsed < 0.2  # Should be fast with lru_cache!

def test_partial_square():
    from functools import partial
    square = partial(power, exponent=2)
    assert square(3) == 9
    assert square(10) == 100
