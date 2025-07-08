from pythonings.ex09_decorators_generators import primes, slow_double, timeit
import time


def test_primes_generator():
    gen = primes(10)
    assert hasattr(gen, "__iter__")
    lst = list(gen)
    assert lst == [2, 3, 5, 7]

def test_timeit_decorator(capsys):
    @timeit
    def foo(x):
        time.sleep(0.01)
        return x + 1
    result = foo(41)
    out = capsys.readouterr().out
    assert "took" in out.lower()
    assert result == 42
