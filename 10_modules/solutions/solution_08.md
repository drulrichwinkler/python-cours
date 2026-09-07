# Solution 08 — What belongs at the top of a module

**a) Three things wrong with the snippet**

1. **It runs at import, so it runs whenever anyone imports you** — including
   `import config` from a script that only wants one constant out of it. The caller
   did not ask for a network request and cannot avoid one.
2. **It makes the test suite depend on the network.** Collection alone imports every
   module, so the request happens before a single test has run. On a machine without
   that host, every test in the file fails at import with an error that names none of
   them. This is the failure that happens **even when the network is fine**: it is the
   coupling, not the outage — the suite cannot run offline, cannot run fast, and
   cannot be given a fake.
3. **The failure has nowhere to go.** An exception during import leaves the module in
   a half-built state, and the traceback points at an import line in some other file.
   There is no caller in a position to retry, choose a default, or report it.

Two more worth having: the value is fixed for the life of the process, so a settings
change needs a restart; and import order now matters, because whoever imports first
pays for it.

**b) When a print at import time is a real problem**

`sensorlib/limits.py` prints because this module needs to show that import runs the
file once. In anything real it is a problem for whoever is downstream of your standard
output:

- **A command-line tool whose output is piped.** `mytool | jq` breaks the moment an
  imported module writes a line of its own into the stream.
- **Anything with structured output** — JSON on stdout, a CSV export — where an extra
  line is a parse error at the other end.
- **The person running the tests**, who now reads a page of import noise.

A log line at import is milder but has the same shape: the logging configuration
belongs to the application, and a library that emits before the application has
configured anything either goes to a default handler or is lost. The convention is
that a library gets a logger (`logging.getLogger(__name__)`) at import and **emits
nothing** until it is called.

The rule this generalises to: a module's top level should contain definitions,
constants and imports. Anything that talks to the world belongs in a function.

**c) Rewriting it**

The direct version:

```python
def load_settings(url="https://example.invalid/settings"):
    return requests.get(url).json()
```

Callers write `settings = load_settings()`. What they have to do differently: call it,
and decide where. That is the improvement — the call site chooses **when** it happens,
can pass a different URL in a test, can catch the failure, and can decide to carry on
with a default.

If every caller wanting the same object matters, compute it once on first use:

```python
import functools


@functools.cache
def settings():
    return requests.get("https://example.invalid/settings").json()
```

The request happens at the first call and never again, and a test can still replace
the function. `functools.cache` is a decorator, which is module 14 — the point here is
only that "compute it once" does not require doing it at import.
