# Solution 08 — The worst line in any codebase

**a) What it hides**

Three kinds, and they matter because only one of them is what the author had in mind:

1. **Failures in the world** — the network is down, the disk is full, the file was
   deleted. This is the one the author was thinking about, and even here `pass` is
   wrong: nothing is retried, nothing is reported, and the caller gets a return value
   that says the work was done.
2. **Mistakes in the code itself** — `AttributeError` from a misspelled attribute,
   `TypeError` from the wrong number of arguments, `NameError` from a typo on a path
   that had never run before. These are bugs, they would have been a one-line fix
   with a traceback, and this clause turns them into "the feature silently does
   nothing".
3. **Failures from far below** — a bug in a function three levels down, in code you
   did not write and would want to report. It arrives here, gets swallowed, and the
   symptom surfaces somewhere unrelated with no path back.

Afterwards all three look identical from outside: the program runs, returns, and is
wrong. The information that would have told them apart existed and was discarded on
purpose.

**b) The defensible version**

Four conditions:

- **The clause names the class**, and it is a class this specific block can produce:
  `except (ValueError, KeyError)`, not `Exception`.
- **The block is one operation.** A `try` around twenty lines catches a `ValueError`
  from any of them; around one line, it can only catch the one you reasoned about.
- **Something happens instead of `pass`** — a log line at the very least, so there is
  a record, and preferably a decision: a default, a retry, a skip that is counted and
  reported. `exercise_09.py` is that shape: the row is skipped, the line number is
  logged, and the count comes out at the end.
- **The comment says why**, when the reason is not obvious from the class.

There is one honest use of a truly bare `pass`: a cleanup path where the failure
genuinely does not matter and you say so. `contextlib.suppress(FileNotFoundError)`
around a delete-if-present is that, and it reads better because the class is right
there in the line.

**c) The one specific difference**

`except:` also catches `KeyboardInterrupt` and `SystemExit`, which come from
`BaseException` rather than `Exception`.

The symptom a user reports: **"I pressed Ctrl-C and it kept going."** The interrupt
is delivered as an exception inside the loop, the bare clause catches it, `pass`
throws it away, and the loop starts the next iteration. The user presses it again,
gets the same nothing, and eventually kills the process — losing whatever the program
had not written out yet.

The same clause eats `sys.exit()`: a program that decides to stop, calls it, and
carries on running. Both failures are unreproducible for anyone reading the code,
because the line that causes them mentions neither Ctrl-C nor exit.
