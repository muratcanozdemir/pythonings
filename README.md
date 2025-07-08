# List as Problem Statements (for README or scaffolding)
## Efficient Iteration:
Fix code that uses verbose or inefficient nested loops by leveraging itertools for concise, fast combinatorics.

## Pythonic Counting:
Refactor manual dictionary counting to use collections.Counter or defaultdict for idiomatic and robust frequency analysis.

## Resource Safety:
Replace error-prone manual try/finally resource handling with a context manager using contextlib or custom with-blocks.

## Functional Power-ups:
Add performance and clarity by using functools.lru_cache for memoization, partial for API ergonomics, and reduce for aggregation.

## Modern File Paths:
Convert brittle os.path and string manipulation into robust, readable pathlib.Path idioms.

## Safe Concurrency and Subprocesses:
Fix blocking or unsafe thread/process spawning using subprocess.run and concurrent.futures for safe, parallel execution and error handling.

## Comprehensions & Unpacking:
Refactor verbose loops and awkward unpacking into idiomatic list/set/dict comprehensions and advanced tuple unpacking.

## Fast Data Structures:
Improve slow search or copy logic by using bisect for sorted lists and memoryview for zero-copy buffer manipulation.

## Decorators & Generators:
Replace repetitive or clunky code with clear decorators and properly designed generator pipelines.

## Serious Debugging:
Swap print-debugging and exception swallowing for structured logging, effective traceback usage, and interactive debugging with pdb.

## Pitfalls & Gotchas:
Identify and fix real-world anti-patterns: mutable default args, reference aliasing, class-vs-instance variable confusion.

## Multiple Inheritance & Dependency Injection:
Refactor diamond inheritance and tight-coupling into correct MRO usage and dependency-injected, testable classes.

# How to use this repo
## Install uv
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
or for Windows:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

These should run without asking for admin credentials, so you're covered. 

If you want to pin Python 3.12 just like under .python-version yourself, or just go into deep dev mode, install it for yourself:
`uv python install "3.12" --project pythonings --managed-python`

## Run tests using uv run
```
uv run --with '.[dev]' pytest
```
Work until all you see is green.