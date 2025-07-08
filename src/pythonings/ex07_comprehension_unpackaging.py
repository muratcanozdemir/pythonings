"""
TODO: Refactor this code to use list, set, and dict comprehensions, as well as advanced unpacking.
See: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
"""

def squares_until(n):
    result = []
    i = 0
    while i < n:
        result.append(i * i)
        i += 1
    return result

def unique_letters(words):
    letters = set()
    for w in words:
        for ch in w:
            letters.add(ch)
    return letters

def invert_dict(d):
    result = {}
    for k, v in d.items():
        result[v] = k
    return result

def split_first_rest(seq):
    first = seq[0]
    rest = seq[1:]
    return first, rest

# Refactor all functions using comprehensions or Pythonic unpacking where possible.
