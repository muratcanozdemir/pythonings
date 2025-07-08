"""
TODO: Refactor this manual counting code to use `collections.Counter` for better performance and readability.
See https://docs.python.org/3/library/collections.html#collections.Counter
"""

def count_items(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# After you fix, this should use collections.Counter.
