"""Exercise 04 -- Ctrl+C, and what a program can do about it.

Write `interrupt(source)`, which starts a program, sends it SIGINT after half a
second, and returns three things: what it printed on standard output (newlines
replaced by ` | `), its exit code, and the last line of standard error -- or the
string `no traceback` if it wrote none.

Then run it on both programs below and print five lines.

Expected output:

    listening | shutting down cleanly
    0
    listening
    -2
    KeyboardInterrupt

Hint: `process.send_signal(signal.SIGINT)` is exactly what Ctrl+C sends.
`communicate(timeout=5)` waits for the end and hands back both streams.
The second program does not catch it, so Python prints a traceback and the exit code
is negative -- `-2` means "ended by signal 2", and signal 2 is SIGINT.
"""

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


# TODO: write interrupt, then five prints
