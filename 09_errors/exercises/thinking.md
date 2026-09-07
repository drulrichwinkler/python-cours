# Module 09 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 09_errors`.

---

## Exercise 07 — No checked exceptions

```java
static String read(Path p) throws IOException     // the caller has to deal with it
```

```python
def read(path: Path) -> str: ...                  # says nothing
```

a) Name two things the Java compiler does for you here that nothing in Python does.
   Be specific about *when* each one happens.
b) Checked exceptions are also the most argued-about feature in Java, and the
   languages that came after it declined to follow — Kotlin on the same runtime
   deliberately, C# on another from the start. Give the case against them: what do programmers
   actually write when the compiler insists?
c) You are writing a library function that reads a config file. Nothing forces you to
   document what it raises, and nothing forces the caller to handle it. Say what you
   would do instead, at three places: the signature, the docstring, and the body.

> **Hint on (b):** what is the shortest edit that makes the compiler stop
> complaining, and what does that edit do to the exception?
> **Hint on (c):** should your function let a `FileNotFoundError` through, or turn it
> into something of its own? Both are defensible — say which and why.

**Check yourself:** your answer to (b) has to name a specific piece of code that a
programmer writes to silence the compiler, and say what it costs.

---

## Exercise 08 — The worst line in any codebase

```python
try:
    do_the_work()
except Exception:
    pass
```

a) List what this hides. Not "errors" — name at least three distinct kinds of
   problem that end up looking identical afterwards.
b) There is a version of this that is defensible. Describe it: what has to be true
   about the clause, the block, and what happens instead of `pass`.
c) `except Exception: pass` and `except: pass` differ in one specific way. Say what,
   and describe the symptom a user of the program would report.

> **Hint on (a):** think about a misspelled attribute name, a failing network call,
> and a bug in a function three levels down.
> **Hint on (c):** what does a user do when a program seems to be stuck?

**Check yourself:** your answer to (a) has to include at least one problem that is a
mistake in the code itself, not a failure in the world.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
