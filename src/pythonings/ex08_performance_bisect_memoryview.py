"""
TODO: Optimize this code using `bisect` for sorted insertion and `memoryview` for zero-copy slicing.
See: https://docs.python.org/3/library/bisect.html
      https://docs.python.org/3/library/stdtypes.html#memoryview
"""

def insert_sorted(lst, x):
    # Manual slow search
    for i, v in enumerate(lst):
        if x < v:
            lst.insert(i, x)
            return
    lst.append(x)

def zero_copy_prefix(data, n):
    # Inefficient: creates a copy
    return data[:n]

# insert_sorted should use bisect.insort; zero_copy_prefix should use memoryview.
