"""
TODO: This code manually opens and closes a file, but it's easy to forget closing in real code.
Replace it with a `with`-block (context manager), or use `contextlib.closing` for non-file resources.
See https://docs.python.org/3/library/contextlib.html
"""

def read_first_line(path):
    f = open(path, "r")
    try:
        return f.readline().strip()
    finally:
        f.close()

# After you fix, this should use a context manager for safety and brevity.
