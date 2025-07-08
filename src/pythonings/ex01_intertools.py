"""
TODO: This code uses triple nested loops to find all triples of (a, b, c) where a + b + c == n,
with a, b, c in range(n+1). Replace the slow, verbose code with an efficient solution using
`itertools.product`. See https://docs.python.org/3/library/itertools.html
"""

def find_triples(n):
    result = []
    for a in range(n + 1):
        for b in range(n + 1):
            for c in range(n + 1):
                if a + b + c == n:
                    result.append((a, b, c))
    return result

# After you fix, this should be much shorter and faster.
