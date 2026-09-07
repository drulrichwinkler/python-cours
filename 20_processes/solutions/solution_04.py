"""Solution 04 -- Ctrl+C, and what a program can do about it."""

import signal
import subprocess
import sys
import time

CATCHES = """
import time
print("listening", flush=True)
try:
    time.sleep(30)
except KeyboardInterrupt:
    print("shutting down cleanly", flush=True)
"""

IGNORES = 'import time\nprint("listening", flush=True)\ntime.sleep(30)\n'


def interrupt(source):
    """Start it, send it SIGINT, and report what it said and how it ended."""
    process = subprocess.Popen(
        [sys.executable, "-c", source],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    time.sleep(0.5)
    process.send_signal(signal.SIGINT)  # exactly what Ctrl+C sends
    out, err = process.communicate(timeout=5)
    last = err.strip().splitlines()[-1] if err.strip() else "no traceback"
    return out.strip().replace("\n", " | "), process.returncode, last


said, code, last = interrupt(CATCHES)
print(said)
print(code)

said, code, last = interrupt(IGNORES)
print(said)
# -2 means "ended by signal 2", and signal 2 is SIGINT. A positive code is one the
# program chose; a negative one is a signal it did not survive.
print(code)
print(last)
