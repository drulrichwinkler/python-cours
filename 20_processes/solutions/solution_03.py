"""Solution 03 -- Repair a check that never says 'finished'."""

import subprocess
import sys

SLEEPS_BRIEFLY = "import time\ntime.sleep(0.2)\n"
SLEEPS_LONG = "import time\ntime.sleep(30)\n"


def state_of(process):
    """'running' while it runs, otherwise the exit code as a string."""
    # poll() returns None while the process is alive and the exit code once it is
    # not. `if process.poll():` asked whether the code was truthy -- and a
    # successful program exits 0, which is falsy, so a finished process was
    # reported as running. The bug only shows for that one exit code.
    code = process.poll()
    return "running" if code is None else str(code)


quick = subprocess.Popen([sys.executable, "-c", SLEEPS_BRIEFLY])
print(state_of(quick))

quick.wait(timeout=5)
print(state_of(quick))

slow = subprocess.Popen([sys.executable, "-c", SLEEPS_LONG])
slow.terminate()
slow.wait(timeout=5)
print(state_of(slow))
