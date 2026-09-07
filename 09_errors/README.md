# Module 09 — Exceptions, `with` and logging

**Assumes:** modules 01–08 · **Feedback:** the predictions in `explore.ipynb` fail until they are
right, and `uv run pytest 09_errors` says whether your exercises are done

## What this is about

Module 08 left two loose ends: what `with` actually is, and what to do about a missing file
instead of checking for it first. This module ties both, and adds the thing that makes a program
debuggable once it runs somewhere you cannot watch it.

- **There are no checked exceptions.** Nothing in a signature says what a function raises, and
  nothing forces you to handle it. Four semesters of `throws IOException` have no counterpart —
  what replaces it is documentation, types, and the habit of catching narrowly.
- **`except Exception`, never a bare `except:`.** `KeyboardInterrupt` and `SystemExit` are not
  `Exception`, which is exactly why the bare form catches your Ctrl-C as well.
- **`else` and `finally`.** Java has `finally`; `else` — the block that runs only when nothing
  raised — has no equivalent, and it is what keeps a `try` down to the one line that can fail.
- **Ask forgiveness, not permission.** `if path.exists()` followed by `open` has a hole between
  the two lines. `try`/`except FileNotFoundError` does not.
- **Exceptions chain.** Raise inside an `except` block and Python keeps the first one, and prints
  both. `raise ... from err` says the connection was deliberate.
- **`with` is a protocol**, not a keyword with a fixed list of types: `__enter__` and `__exit__`,
  and you can write one in four lines. It is Java's try-with-resources, generalised — the object
  decides what "leaving the block" means, and it can decide to swallow the exception.
- **`logging`, not `print`.** Levels, a logger per module, and formatting arguments that are only
  formatted if the message is actually emitted.

## What you can do afterwards

1. **catch** the exception you meant and let the others through, and say why bare `except:` is
   worse than it looks;
2. **use** `else` and `finally`, and say what `finally` does to a `return`;
3. **raise**, with and without `from`, and read what Python prints for a chained exception;
4. **write** a context manager, as a class and with `@contextmanager`;
5. **replace** a `print` with a logger, and say what that buys once the program runs unattended.

## Order of work

0. **`selfcheck.ipynb`** — six statements. All `True` means skip the module.
1. **`explore.ipynb`** — the predictions
2. **`exercises/`** — seven files to fill in, two to think through in `thinking.md`
3. **`uv run pytest 09_errors`**
4. **`solutions/`** — last

## One line of class syntax, ahead of module 11

A custom exception is `class ParseError(Exception): pass` — a name, a parent, and nothing else.
That is used here because an exception type is the natural thing to raise, and it is the whole of
what you need to know about classes to do it. Module 11 is where classes get their own module.
