"""
TODO: Refactor this code to use structured logging instead of print, handle exceptions robustly,
and provide a way to debug interactively with pdb if needed.
See: https://docs.python.org/3/library/logging.html
      https://docs.python.org/3/library/pdb.html
"""

def divide(a, b):
    try:
        return a / b
    except:
        print("Something went wrong!")  # Not informative; not real logging
        return None

def main():
    print("Starting...")  # Should be logging
    result = divide(10, 0)
    print("Result:", result)  # Should be logging

# Refactor all prints to use logging, and catch exceptions properly (log the traceback).
# Bonus: add a pdb.set_trace() call when an error occurs (commented out).
