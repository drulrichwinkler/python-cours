# Module 10 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 10_modules`.

---

## Exercise 07 — The same file, two ways to start it

```console
$ python tool/show.py     # sys.path[0] is .../tool
$ python -m tool.show     # sys.path[0] is the current directory
```

a) Explain what each of the two puts on `sys.path`, and why the difference exists at
   all — what is each form assuming about how you meant to run the code?
b) A colleague's script imports a sibling package. It works when they run it from
   the project root with `-m` and fails with `ModuleNotFoundError` when they run it
   by its path from the same directory. Walk through what happens in both cases.
c) The `sensorlib` exercises in this module start with `sys.path.insert(0, str(MODULE))`.
   Name two things that go wrong with that line in a real project, and say what
   replaces it.

> **Hint on (a):** one of the two forms knows the name of a package; the other only
> knows a file path.
> **Hint on (c):** what happens when two projects on the same machine each insert
> their own folder — and what happens when the file is moved?

**Check yourself:** your answer to (b) has to name which directory is missing from
the list in the failing case.

---

## Exercise 08 — What belongs at the top of a module

```python
# config.py
import requests

SETTINGS = requests.get("https://example.invalid/settings").json()  # at import time
```

a) Name three separate things that go wrong with this, given that importing a module
   runs it. At least one of them should be about testing.
b) `sensorlib/limits.py` in this module prints when it is imported. That is a
   teaching device — but say when a print, or a log line, at import time is a real
   problem, and who it is a problem for.
c) Rewrite the snippet so the settings are still available to callers, without the
   import doing it. Say what the caller has to do differently, and why that is an
   improvement rather than an inconvenience.

> **Hint on (a):** when does this run, how often, and what does the test suite do
> before a single test has started?
> **Hint on (c):** a function, or a value computed on first use. Both are defensible.

**Check yourself:** your answer to (a) has to name a failure that happens when the
network is fine.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
