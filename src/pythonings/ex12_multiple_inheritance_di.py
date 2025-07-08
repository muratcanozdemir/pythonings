"""
TODO: Refactor for proper multiple inheritance (MRO, diamond problem), and make DataService testable with dependency injection.
See: https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
      https://realpython.com/dependency-injection-python/
"""

# --- MULTIPLE INHERITANCE ---

class Logger:
    def log(self, msg):
        print("Logger:", msg)

class FileLogger(Logger):
    def log(self, msg):
        print("FileLogger:", msg)
        super().log(msg)

class ConsoleLogger(Logger):
    def log(self, msg):
        print("ConsoleLogger:", msg)
        super().log(msg)

class App(FileLogger, ConsoleLogger):
    pass

# App().log("hi") does not call all loggers as intended. Fix via correct super()/MRO usage.

# --- DEPENDENCY INJECTION ---

def default_fetcher(url):
    return "real data from " + url

class DataService:
    def get_data(self, url):
        data = default_fetcher(url)
        return data.upper()

# Refactor DataService to accept a fetcher (function/class), so it's easily testable.
