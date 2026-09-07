"""Solution 02 -- Predict what a process does.

port             is not 0. Asking for port 0 means "any free one -- you choose",
                 and getsockname() reports what you were given, somewhere above
                 1024. That is what module 16's and 17's servers do so their tests
                 cannot clash.
outcome          is 'Address already in use'. A port is held by one listener at a
                 time. The message is stable; the errno is not -- 48 on macOS, 98
                 on Linux, 10048 on Windows -- which is why the assertion is on
                 strerror.
poll()           is None while the process runs and 0 once it has finished
                 successfully. Both of those are FALSY, which is the whole of
                 exercise 03: `if process.poll():` asks whether the exit code is
                 truthy, not whether the process has ended, and a successful
                 program exits 0.
returncode       is -2. A negative code means "ended by signal", and signal 2 is
                 SIGINT -- what Ctrl+C sends. A positive code is one the program
                 chose. The traceback's last line is KeyboardInterrupt, which
                 module 09 said comes off BaseException rather than Exception; this
                 is the moment that mattered.
sensorreport     has 50 readings, 3 of them unreadable, a limit of 85.0, and three
                 locations with 0, 0 and 3 faults. The same numbers as module 18's
                 pandas summary and module 19's SQL query, computed a third way --
                 and imported with no sys.path line, because pyproject.toml lists
                 it as a package of this project.
"""

import signal
import socket
import subprocess
import sys
import time

from sensorreport import LIMIT, load_readings, summarise

listener = socket.socket()
listener.bind(("127.0.0.1", 0))
port = listener.getsockname()[1]

assert (port == 0) is False
assert (1024 < port < 65536) is True


second = socket.socket()
try:
    second.bind(("127.0.0.1", port))
    outcome = "bound"
except OSError as err:
    outcome = err.strerror

listener.close()
second.close()

assert outcome == "Address already in use"


process = subprocess.Popen([sys.executable, "-c", "import time\ntime.sleep(0.2)"])
running = process.poll()
process.wait(timeout=5)
finished = process.poll()

assert running is None
assert finished == 0


assert bool(finished) is False


ignores = subprocess.Popen(
    [sys.executable, "-c", "import time\ntime.sleep(30)"],
    stderr=subprocess.PIPE,
    text=True,
)
time.sleep(0.4)
ignores.send_signal(signal.SIGINT)
_, errors = ignores.communicate(timeout=5)

assert ignores.returncode == -2
assert errors.strip().splitlines()[-1] == "KeyboardInterrupt"


readings = load_readings()

assert len(readings) == 50
assert sum(1 for r in readings if r.value is None) == 3
assert LIMIT == 85.0
assert [s.location for s in summarise(readings)] == ["Hall", "Office", "Test rig"]
assert [s.faults for s in summarise(readings)] == [0, 0, 3]
