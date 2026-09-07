# Solution 07 — Not an annotation

**a) What each does, and when**

**`@Override`** is metadata attached to the method. It changes nothing about the
method itself; it is a claim, checked by the compiler at compile time, and then either
discarded or kept in the class file for something to read later by reflection. The
method after compilation is the method you wrote.

**`@loud`** is a call. At **import time** — when the `def` statement executes —
`loud(add)` runs, and whatever it returns is bound to the name `add`.

What `add` refers to afterwards: **the wrapper function** that `loud` returned. Not
the function in the source. The function you wrote still exists, reachable as a
closure variable inside the wrapper (and as `add.__wrapped__` if `functools.wraps`
was used), but the name no longer points at it.

That is the whole difference: an annotation describes, a decorator replaces.

**b) One each way**

**Straightforward with annotations, awkward with decorators:** finding out what is
there without running anything. `@Deprecated` on a hundred methods can be listed by a
tool that reads class files — no code executes, no imports happen, no side effects. In
Python the decorator *is* code, and it has already run by the time you can inspect the
result; to discover what is decorated you have to import the module, which runs
everything in it. Static analysis of Python decorators is correspondingly harder, and
that is why the ecosystem leans on conventions and plugins (`mypy` has to special-case
`@dataclass`).

**Straightforward with decorators, awkward with annotations:** changing behaviour. A
decorator can retry, time, cache, validate arguments, or return something else
entirely, in the ten lines it takes to write it. An annotation cannot do any of that
by itself — it needs a framework that reads it and then does the work: an
`@Transactional` only means something because Spring generates a proxy around the
class. Python skips the framework because the language feature already replaces the
object.

**c) Which one is different**

**`@pytest.mark.your_turn`** is the odd one out. It attaches a mark to the function
and hands the same function back — the test is not wrapped and its behaviour is
unchanged. `pytest` reads the marks later to decide what to run or skip. That makes it
the closest thing in this course to a Java annotation, and it is exactly the shape of
exercise 09's registry.

`@app.route("/readings")` and `@app.get("/readings")` both **register** the function
in a routing table so the framework can call it when a request arrives — and they also
return it unchanged. So all three are non-wrapping, and the real division is what the
note is for: two put the function somewhere the framework will fetch it from, one
leaves a label on it for a later filter.
