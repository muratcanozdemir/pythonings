"""
TODO: This code manipulates file paths using string concatenation and os.path.
Refactor it to use pathlib.Path for safer, more Pythonic code.
See: https://docs.python.org/3/library/pathlib.html
"""

import os

def list_py_files(dirname):
    files = []
    for name in os.listdir(dirname):
        if name.endswith(".py"):
            files.append(os.path.join(dirname, name))
    return files

# After you fix, this should use only pathlib, no os.path or string concatenation.
# Looks a lot cleaner, too!