# Module 14 — Exercises you think through

Two here have no code to write. The rest are `exercises/exercise_*.py`, checked by
`uv run pytest 14_decorators`.

---

## Exercise 07 — Not an annotation

```java
@Override
public String toString() { ... }
```

```python
@loud
def add(a, b): ...
```

The two look alike and are different in kind.

a) Say what each one does and **when** it does it. Name what is left bound to `add`
   after the Python one has run.
b) Java annotations are read by something else — the compiler, a framework, a
   reflection call. Name one thing that is straightforward with annotations and
   awkward with decorators, and one that is the other way round.
c) `@app.route("/readings")` in Flask, `@app.get("/readings")` in FastAPI,
   `@pytest.mark.your_turn` in every test file of this course. One of those three is
   doing something different from the other two. Say which, and what.

> **Hint on (b):** what can you find out about a Java class without running any of
> its methods? And what can a decorator do that no annotation can?
> **Hint on (c):** two of them need the function; one only needs to leave a note on
> it. Look at what each is for.

**Check yourself:** your answer to (a) has to name the object `add` refers to
afterwards.

---

## Exercise 08 — What a decorator costs the reader

```python
@retry(times=3)
@timed
@authorised
def publish(report): ...
```

Somebody calls `publish(report)`.

a) List everything that happens which is not visible at the call site. Then say what
   the reader has to open to find out.
b) `@retry(times=3)` on a function that writes to a database is a decision, not a
   convenience. Say what could go wrong, and what the decorator would have to know
   about `publish` to be safe.
c) Give one concern that belongs in a decorator and one that does not, and state the
   test you would apply to decide. "It is repeated" is not enough on its own — say
   why not.

> **Hint on (a):** count the frames a traceback would show, and ask which of them
> carry a name you recognise.
> **Hint on (c):** does the caller need to know? Does the answer change the meaning
> of the return value?

**Check yourself:** your answer to (b) has to use the word idempotent, or explain the
same idea without it.

The written-out answers are in `solutions/solution_07.md` and `solution_08.md`.
