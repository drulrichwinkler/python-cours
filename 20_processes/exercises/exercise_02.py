"""Exercise 02 -- Predict what a process does.

Replace each `...` with the value you expect, then run the file.

    uv run 20_processes/exercises/exercise_02.py

Nothing printed means every prediction was right.

There is no "Expected output" section here: what is checked is your prediction.
"""

import signal
import socket
import subprocess
import sys
import time

from sensorreport import LIMIT, load_readings, summarise

# TODO: port 0 asks for any free port. What comes back?
listener = socket.socket()
listener.bind(("127.0.0.1", 0))
port = listener.getsockname()[1]

assert (port == 0) == ...
assert (1024 < port < 65536) == ...


# TODO: a second socket asking for the same port
second = socket.socket()
try:
    second.bind(("127.0.0.1", port))
    outcome = "bound"
except OSError as err:
    outcome = err.strerror

listener.close()
second.close()

assert outcome == ...


# TODO: poll() while the process runs, and after it has finished successfully
process = subprocess.Popen([sys.executable, "-c", "import time\ntime.sleep(0.2)"])
running = process.poll()
process.wait(timeout=5)
finished = process.poll()

assert running is ...
assert finished == ...


# TODO: and what that means for `if process.poll():`
assert bool(finished) == ...


# TODO: SIGINT on a program that does not catch it
ignores = subprocess.Popen(
    [sys.executable, "-c", "import time\ntime.sleep(30)"],
    stderr=subprocess.PIPE,
    text=True,
)
time.sleep(0.4)
ignores.send_signal(signal.SIGINT)
_, errors = ignores.communicate(timeout=5)

assert ignores.returncode == ...
assert errors.strip().splitlines()[-1] == ...


# TODO: the analysis every module of Part 5 imports
readings = load_readings()

assert len(readings) == ...
assert sum(1 for r in readings if r.value is None) == ...
assert LIMIT == ...
assert [s.location for s in summarise(readings)] == ...
assert [s.faults for s in summarise(readings)] == ...
