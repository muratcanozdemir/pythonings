"""
TODO: This code runs several shell commands sequentially and blocks on each.
Refactor it to run the commands in parallel using ThreadPoolExecutor, and use subprocess.run for robust command execution.
See: https://docs.python.org/3/library/subprocess.html
      https://docs.python.org/3/library/concurrent.futures.html
"""

import subprocess

def run_commands(cmds):
    results = []
    for cmd in cmds:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        results.append(out.decode().strip())
    return results

# After you fix, this should use concurrent.futures.ThreadPoolExecutor
# and subprocess.run with capture_output=True (no manual Popen).
