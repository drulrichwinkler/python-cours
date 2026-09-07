# Solution 07 — The program that cannot be stopped

**a) Step by step**

1. Ctrl+C makes the terminal send **SIGINT** to the process.
2. Python's default SIGINT handler raises **`KeyboardInterrupt`** in the main thread,
   at whatever line it had reached.
3. That line is inside the `try`, so the `except:` clause is offered the exception.
   A **bare** `except:` catches `BaseException` and every subclass — and
   `KeyboardInterrupt` is one, which is exactly what module 09 was about.
4. `pass` discards it.
5. `while True:` starts the next iteration.

So the interrupt was delivered, caught and thrown away. The program continues, and
nothing anywhere records that somebody asked it to stop.

**b) What the user does, and what it costs**

They press it again — and again — get nothing each time, and then reach for something
that works: Ctrl+Z and `kill`, or `kill -9` from another terminal, or closing the
terminal window, or in the worst case rebooting.

What it costs: **everything the program had not yet written down.** Every one of those
routes ends the process without letting it finish. A batch half inserted, a file
opened for writing and never closed, a lock file left behind that makes the *next*
run refuse to start. And the user has learned that this program has to be killed,
which is a habit they will now apply to it even when a clean shutdown would have
worked.

The second cost is diagnostic: after `kill -9` there is no traceback, no log line, and
no way to tell what the program was doing. The information that would have explained
the next bug was in a process that was shot.

**c) Why `kill -9` works, and why it is a last resort**

SIGKILL is handled by the kernel, not by the process. There is no handler to install
and no code that runs — the process is simply removed. That is why it always works,
and it is the same reason it is the last thing to try: **the process gets no chance to
do anything.**

What a server should have done and now cannot:

- **flush its buffers.** Anything written but not yet on disk is gone — module 08's
  file writes are buffered until the file is closed.
- commit or roll back an open transaction (module 19), leaving the database to recover
  it on next start;
- close its listening socket, so the port may stay unavailable briefly;
- delete its PID or lock file, so the next start thinks an instance is running;
- log the fact that it stopped, which is the line you will want tomorrow.

The escalation, in order: **Ctrl+C** (SIGINT, catchable, tidy) → **`kill`** (SIGTERM,
also catchable, which is what `terminate()` sends) → **`kill -9`** (SIGKILL,
uncatchable). Going straight to the last is how you turn a stuck process into a
corrupted state.

**d) The loop, rewritten**

```python
try:
    while True:
        try:
            do_one_batch()
        except BatchError:              # the failures this loop is meant to survive
            log.exception("batch failed, carrying on")
except KeyboardInterrupt:               # outside the loop: stop, do not retry
    log.info("interrupted, shutting down")
finally:
    close_everything()                  # runs on both paths -- module 09
```

Three things changed and each one matters:

- **the inner clause names its class.** `BatchError`, or whatever this loop is
  actually meant to survive — not `Exception`, and never bare.
- **`KeyboardInterrupt` is caught outside the loop**, so it ends the loop rather than
  one iteration. Catching it inside would still cost the user a Ctrl+C per batch.
- **`finally` does the cleanup**, so it happens whichever way the loop ends.

The ordinary failures are still handled, which was the requirement: what changed is
that "stop" is no longer one of them.
