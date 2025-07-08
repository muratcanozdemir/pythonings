"""
TODO: Identify and fix classic Python pitfalls: mutable default arguments, class/instance variable confusion,
and aliasing bugs.
See: https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects
"""

def append_item(item, seq=[]):
    seq.append(item)
    return seq

class Counter:
    count = 0  # This is a class variable!
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count += 1

def aliasing_bug(lst):
    result = lst
    result.append(999)
    return result

# Fix: no mutable default, no class/instance variable confusion, no aliasing.
