"""Exercise 03 -- Repair a check that never says 'finished'.

`state_of` should say `running` while the process runs and its exit code once it has
stopped. Run it: the second line says `running` about a process that has ended
successfully.

The bug is a truth value, and the reason it survived testing is that it only shows up
for one exit code.

Expected output:

    running
    0
    -15

Hint: `process.poll()` returns `None` while the process is alive and the exit code
when it is not. So the question `if process.poll():` asks is not "has it finished" --
it is "is the exit code truthy", and a successful program exits `0`. Compare with
`None` explicitly.
"""

import subprocess
import sys
import time

SLEEPS_BRIEFLY = "import time\ntime.sleep(0.2)\n"
SLEEPS_LONG = "import time\ntime.sleep(30)\n"


def state_of(process):
    """'running' while it runs, otherwise the exit code as a string."""
    if process.poll():  # TODO: the bug is in this line
        return str(process.poll())
    return "running"


quick = subprocess.Popen([sys.executable, "-c", SLEEPS_BRIEFLY])
print(state_of(quick))  # still running

quick.wait(timeout=5)
print(state_of(quick))  # finished, exit code 0

slow = subprocess.Popen([sys.executable, "-c", SLEEPS_LONG])
slow.terminate()
slow.wait(timeout=5)
print(state_of(slow))  # ended by signal 15
